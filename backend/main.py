from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
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

vectorstore = None
uploaded_files = []

@app.post("/upload")
async def upload_pdf(files: List[UploadFile] = File(...)):
    global vectorstore, uploaded_files

    all_docs = []
    new_files = []

    for file in files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        loader = PyPDFLoader(tmp_path)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents)
        all_docs.extend(docs)
        new_files.append(file.filename)

        os.unlink(tmp_path)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    if vectorstore is None:
        vectorstore = FAISS.from_documents(all_docs, embeddings)
    else:
        vectorstore.add_documents(all_docs)

    uploaded_files.extend(new_files)

    return {
        "message": f"{len(new_files)} PDF(s) uploaded successfully!",
        "chunks": len(all_docs),
        "files": uploaded_files
    }


@app.post("/ask")
async def ask_question(question: str = Form(...)):
    global vectorstore

    if vectorstore is None:
        return {"answer": "Please upload at least one PDF first."}

    try:
        llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

        prompt = ChatPromptTemplate.from_template("""
        Answer the question based only on the following context from the uploaded documents.
        If you don't know the answer, just say you don't know.

        Context:
        {context}

        Question: {question}
        """)

        retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        answer = chain.invoke(question)
        return {"answer": answer}

    except Exception as e:
        print("======= ERROR =======")
        print(str(e))
        print("=====================")
        return {"answer": f"Error: {str(e)}"}


@app.get("/files")
def get_files():
    return {"files": uploaded_files}


@app.get("/")
def home():
    return {"message": "DocuMind AI Backend is running!"}