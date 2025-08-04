RAG System: Technical Document Q&A 

A simple Retrieval-Augmented Generation (RAG) system for question-answering on technical PDF documents, powered by Streamlit, sentence-transformers, and Hugging Face transformers.

## Features

- **Upload any PDF**: Supports both text and scanned PDFs (OCR fallback).
- **Chunking and Indexing**: Splits extracted text and builds a semantic search index using Sentence Transformers and FAISS.
- **Semantic Search**: Retrieves relevant chunks from the document for a given question.
- **LLM Answering**: Generates relevant, context-grounded answers using a local language model.
- **Interactive UI**: Ask questions and explore retrieved context directly in your browser.

---

- **PDF Text Extraction:** Uses PyMuPDF and Tesseract OCR for image-based content.
- **Text Chunking:** Breaks long texts into overlapping chunks for retrieval.
- **Vector Search:** Embeds chunks with Sentence Transformers, indexes with FAISS.
- **Generative QA:** Uses a small LLM (distilgpt2) to generate answers, conditioned on the top-matching context chunks from your document.

