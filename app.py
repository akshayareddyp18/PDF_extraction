import streamlit as st
import fitz
import io
from PIL import Image
import pytesseract
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import pipeline

# --- Functions from earlier ---
def extract_text_from_pdf_filelike(filelike, ocr_lang='eng'):
    doc = fitz.open(stream=filelike.read(), filetype="pdf")
    all_text = []
    for page in doc:
        text = page.get_text()
        if not text.strip():
            image_bytes = page.get_pixmap().pil_tobytes(format="PNG")
            img = Image.open(io.BytesIO(image_bytes))
            text = pytesseract.image_to_string(img, lang=ocr_lang)
        all_text.append(text)
    return '\n'.join(all_text)

def chunk_text(text, chunk_size=512, chunk_overlap=64):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len
    )
    return splitter.split_text(text)

class DocumentVectorDB:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.embedder = SentenceTransformer(model_name)
        self.index = None
        self.chunks = []

    def build(self, text_chunks):
        self.chunks = text_chunks
        embs = self.embedder.encode(text_chunks, show_progress_bar=True)
        embs = np.array(embs).astype('float32')
        self.index = faiss.IndexFlatL2(embs.shape[1])
        self.index.add(embs)

    def search(self, query, top_k=4):
        q_emb = self.embedder.encode([query]).astype('float32')
        D, I = self.index.search(q_emb, top_k)
        return [self.chunks[i] for i in I[0]]

def answer_query(question, retrieved_chunks, llm_pipe, system_prompt="Answer using the provided context."):
    prompt = f"{system_prompt}\n\nContext:\n{retrieved_chunks}\n\nQuestion: {question}\nAnswer:"
    return llm_pipe(prompt, max_new_tokens=256)[0]['generated_text']

# --- Streamlit App ---
st.title("RAG System: Technical Document Q&A (Drag-n-Drop PDF)")

uploaded_pdf = st.file_uploader("Upload a PDF document", type=['pdf'])

if uploaded_pdf:
    st.write("Extracting and indexing document...")
    raw_text = extract_text_from_pdf_filelike(uploaded_pdf)
    chunks = chunk_text(raw_text)
    vectordb = DocumentVectorDB()
    vectordb.build(chunks)
    llm_pipe = pipeline("text-generation", model="distilgpt2")
    st.success("Document loaded! Ask your question.")

    query = st.text_input("Type your question here:")
    if query:
        context = "\n".join(vectordb.search(query, top_k=4))
        answer = answer_query(query, context, llm_pipe)
        st.markdown("**Answer:**")
        st.write(answer)

        with st.expander("See retrieved context"):
            st.code(context)
else:
    st.info("Please drag and drop or select a PDF to begin.")

