#  RAG System: Technical Document Q&A

A simple **Retrieval-Augmented Generation (RAG)** system for question-answering on **technical PDF documents**, powered by **Streamlit**, **Sentence Transformers**, and **Hugging Face Transformers**.

---

## Features

-  **Upload PDF** – Supports both text-based and scanned PDFs (OCR fallback).  
-  **Chunking and Indexing** – Splits extracted text and builds a semantic search index using **Sentence Transformers** and **FAISS**.  
-  **Semantic Search** – Retrieves relevant chunks from the document for a given question.  
-  **LLM Answering** – Generates relevant, context-grounded answers using a local language model.  
-  **Interactive UI** – Ask questions and explore retrieved context directly in your browser.  
-  **PDF Text Extraction** – Uses **PyMuPDF** for text and **Tesseract OCR** for image-based content.  
-  **Text Chunking** – Breaks long texts into overlapping chunks for retrieval.  
-  **Vector Search** – Embeds chunks with Sentence Transformers, indexes with **FAISS**.  
-  **Generative QA** – Uses a small LLM (**distilgpt2**) to generate answers, conditioned on the top-matching context chunks.  

---

##  Workflow Overview

1.  **PDF Upload**  
   - Extract text with PyMuPDF.  
   - OCR fallback via Tesseract for scanned PDFs.  

2.  **Chunking**  
   - Split text into overlapping chunks for better retrieval.  

3.  **Embedding & Indexing**  
   - Generate vector embeddings with Sentence Transformers.  
   - Store & search with FAISS index.  

4.  **Question Answering**  
   - Retrieve top-N relevant chunks.  
   - Pass context + question to local LLM (distilgpt2).  
   - Generate final answer.  

5.  **Interactive UI**  
   - Streamlit app to upload docs, ask questions, and view retrieved chunks + answers.  

---

##  Tech Stack

- **Frontend/UI**: Streamlit  
- **LLM**: Hugging Face Transformers (distilgpt2)  
- **Embeddings**: Sentence Transformers  
- **Indexing/Search**: FAISS  
- **PDF Processing**: PyMuPDF, Tesseract OCR  
- **Language**: Python  

---

##  How to Run

```bash
# 1 Clone the repository
git clone https://github.com/akshayareddyp/PDF_extraction.git
cd PDF_extraction

# 2️ Install dependencies
pip install -r requirements.txt

# 3️ Run the Streamlit app
streamlit run app.py
