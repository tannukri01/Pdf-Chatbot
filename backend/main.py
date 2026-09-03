from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import shutil
import tempfile
from typing import List

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store document text in memory (lightweight)
documents_text = ""
uploaded_files = []

@app.post("/upload")
async def upload_pdf(files: List[UploadFile] = File(...)):
    global documents_text, uploaded_files

    all_text = []
    new_files = []

    for file in files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        loader = PyPDFLoader(tmp_path)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
        chunks = text_splitter.split_documents(docs)

        for chunk in chunks:
            all_text.append(chunk.page_content)

        new_files.append(file.filename)
        os.unlink(tmp_path)

    documents_text = "\n\n".join(all_text)
    uploaded_files.extend(new_files)

    return {
        "message": f"{len(new_files)} PDF(s) uploaded successfully!",
        "chunks": len(all_text),
        "files": uploaded_files
    }


@app.post("/ask")
async def ask_question(question: str = Form(...)):
    global documents_text

    if not documents_text:
        return {"answer": "Please upload at least one PDF first."}

    try:
        llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

        # Keep context reasonable size
        context = documents_text[:12000]

        prompt = ChatPromptTemplate.from_template("""
        Answer the question based only on the following document content.
        If you don't know, say you don't know.

        Document:
        {context}

        Question: {question}
        """)

        chain = prompt | llm
        result = chain.invoke({"context": context, "question": question})

        return {"answer": result.content}

    except Exception as e:
        print("ERROR:", str(e))
        return {"answer": f"Error: {str(e)}"}


@app.get("/")
def home():
    return {"message": "DocuMind AI Backend is running!"}