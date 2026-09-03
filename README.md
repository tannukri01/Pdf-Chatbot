# 🤖 DocuMind AI

### AI-Powered PDF Chatbot using Retrieval-Augmented Generation (RAG)

<p align="center">
  <b>Upload a PDF → Ask questions → Get intelligent, context-grounded answers</b>
</p>

<p align="center">
  <a href="https://pdf-chatbot-ai.netlify.app">Live Demo</a> •
  <a href="https://github.com/tannukri01/Pdf-Chatbot">GitHub Repository</a> •
  <a href="https://pdf-chatbot-cik6.onrender.com">Backend API</a>
</p>

---

## 📌 About The Project

**DocuMind AI** is a full-stack AI-powered document intelligence application that allows users to upload PDF documents and interact with them using natural language.

Instead of manually searching through lengthy documents, users can simply upload a PDF and ask questions about its content.

The application follows a **RAG-style document question-answering pipeline**, where the uploaded document content is processed and provided as context to the Large Language Model (LLM) to generate relevant and document-grounded responses.

### 💡 The Idea

```text
Traditional Approach
--------------------
Open PDF → Search manually → Read multiple pages → Find information


DocuMind AI
-----------
Upload PDF → Ask a question → AI processes document context → Get answer
```

---

## 🚀 Live Application

### 🌐 Frontend

https://pdf-chatbot-ai.netlify.app

### ⚡ Backend API

https://pdf-chatbot-cik6.onrender.com

### 💻 Source Code

https://github.com/tannukri01/Pdf-Chatbot

> **Deployment Note:** The backend is hosted on the free Render tier. If the service has been inactive, the first request may take approximately **30–50 seconds** while the server wakes up.

---

# 🎯 Problem Statement

Large PDF documents such as resumes, research papers, academic notes, reports, and company documents often contain a large amount of information.

Finding a specific piece of information manually can be:

* Time-consuming
* Difficult to navigate
* Inefficient for large documents
* Repetitive when multiple questions need to be answered

**DocuMind AI solves this problem by providing a conversational interface for interacting with PDF documents.**

Users can upload their document and ask questions in natural language instead of manually searching through the entire file.

---

# ✨ Key Features

| Feature                           | Description                                                   |
| --------------------------------- | ------------------------------------------------------------- |
| 📄 **PDF Upload**                 | Upload PDF documents for AI-powered analysis                  |
| 📚 **Multiple Documents**         | Supports multiple PDF documents                               |
| 🧠 **Context-Aware Q&A**          | Ask natural-language questions about uploaded documents       |
| 🤖 **AI-Powered Answers**         | Uses Groq LLM for intelligent response generation             |
| 🎯 **Context-Grounded Responses** | Answers are generated using document context                  |
| ⚡ **Fast Inference**              | Powered by Groq for fast LLM inference                        |
| 🌐 **REST API**                   | FastAPI-based backend architecture                            |
| 💻 **Responsive UI**              | Clean and responsive web interface                            |
| 🔐 **Environment Variables**      | API credentials are handled through environment configuration |
| ☁️ **Cloud Deployment**           | Frontend and backend deployed independently                   |

---

# 🧠 How DocuMind AI Works

The application follows a document question-answering pipeline:

```text
                    ┌─────────────────┐
                    │   PDF Document  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Text Extraction │
                    │     (PyPDF)      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Text Chunking  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Document Context│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ User Question   │
                    └────────┬────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │ Context + Question     │
                 │       Prompt           │
                 └────────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │    Groq LLM     │
                    │ openai/gpt-oss-20b│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Final Answer  │
                    └─────────────────┘
```

### 🔄 Processing Flow

**1. Upload PDF**

The user uploads one or more PDF documents through the web interface.

**2. Extract Text**

The backend extracts readable text from the PDF using **PyPDF**.

**3. Process Document**

The extracted content is processed and divided into manageable text chunks.

**4. Prepare Context**

The processed document content is stored as the context used for answering questions.

**5. Ask a Question**

The user enters a natural-language question related to the uploaded document.

**6. Generate Answer**

The document context and user question are passed to the Groq-powered LLM.

**7. Return Response**

The generated answer is returned to the frontend and displayed to the user.

---

# 🛠️ Tech Stack

## Frontend

* **HTML5**
* **Tailwind CSS**
* **Vanilla JavaScript**

## Backend

* **Python**
* **FastAPI**
* **Uvicorn**

## AI & Document Processing

* **LangChain**
* **Groq LLM**
* **PyPDF**

## LLM Model

```text
openai/gpt-oss-20b
```

## Deployment

```text
Frontend  → Netlify
Backend   → Render
Source    → GitHub
```

---

# 📂 Project Structure

```text
Pdf-Chatbot/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   └── index.html
│
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

## Prerequisites

Before running the project locally, make sure you have:

* Python installed
* Git installed
* A Groq API key

---

## 1. Clone the Repository

```bash
git clone https://github.com/tannukri01/Pdf-Chatbot.git
cd Pdf-Chatbot
```

---

## 2. Create a Virtual Environment

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file inside the `backend` directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your Groq API key from the Groq Console.

> ⚠️ **Security:** Never commit your actual `.env` file or API key to GitHub.

---

## 6. Start the Backend

Run the FastAPI server:

```bash
uvicorn main:app --reload --port 8000
```

Backend will be available at:

```text
http://localhost:8000
```

---

## 7. Start the Frontend

Open a new terminal:

```bash
cd frontend
python -m http.server 5500
```

Open the application in your browser:

```text
http://localhost:5500
```

---

# 🔌 API Documentation

DocuMind AI exposes REST API endpoints for document processing and question answering.

## 📤 Upload Document

```http
POST /upload
```

Uploads and processes PDF document(s).

### Purpose

* Accept PDF files
* Extract document text
* Process the uploaded content
* Prepare document context for question answering

---

## 💬 Ask Question

```http
POST /ask
```

Accepts a natural-language question and generates an answer based on the uploaded document context.

### Example

```text
Question:
"What technical skills are mentioned in this resume?"

Response:
AI-generated answer based on the uploaded document.
```

---

## ❤️ Health Check

```http
GET /
```

Returns the current backend status.

---

# 🎯 Real-World Use Cases

DocuMind AI can be used for a variety of document-based tasks:

### 📄 Resume Analysis

Ask questions about skills, education, experience, projects, and other resume information.

### 📚 Study Material

Interact with long academic notes and study PDFs.

### 🎓 Academic Documents

Quickly find information from assignments, course material, and academic documents.

### 🏢 Company Reports

Ask questions about business reports and internal documents.

### 📑 Research Papers

Interact with research papers without manually searching through every page.

### 📋 Policy Documents

Find specific information from lengthy policies and guidelines.

### 🧾 Internal Documentation

Make technical and organizational documentation easier to explore.

---

# 💻 Example

### Input Document

```text
Resume.pdf
```

### User Question

```text
What technical skills are mentioned in the resume?
```

### Processing

```text
PDF
 ↓
Text Extraction
 ↓
Text Processing
 ↓
Document Context
 ↓
Question + Context
 ↓
Groq LLM
```

### Output

```text
The resume mentions Java, Python, JavaScript,
React, Spring Boot, SQL, and other technical skills.
```

The answer is generated using the content available in the uploaded document.

---

# 📚 Key Learnings

This project provided practical experience in building an end-to-end AI document application.

### AI & LLM

* LLM integration
* Context-grounded question answering
* Prompt construction
* Groq API integration
* Document-based AI interaction

### Backend Development

* FastAPI REST API development
* File upload handling
* PDF processing
* CORS configuration
* API endpoint design

### Frontend Development

* HTML5
* Tailwind CSS
* Vanilla JavaScript
* Frontend–backend API integration
* Responsive UI development

### Deployment

* Git and GitHub workflow
* Netlify deployment
* Render deployment
* Environment variable management
* Cloud-based application deployment

---

# ⚠️ Current Limitations

The current version has some limitations:

* Optimized mainly for text-based PDFs
* Document context is currently stored in memory
* Document data is cleared when the server restarts
* No user authentication
* No permanent chat history
* No persistent document storage
* No multi-user document isolation
* Free Render instance may sleep after inactivity

---

# 🔮 Future Roadmap

The project can be extended with the following improvements:

### 🧠 Advanced RAG

* Persistent vector database using **FAISS / Chroma**
* Embedding-based semantic search
* Improved document retrieval
* Full retrieval-augmented generation pipeline

### 💬 Chat Experience

* Persistent chat history
* Conversation management
* Streaming responses

### 👤 User Management

* User authentication
* Multi-user document isolation
* User-specific document storage

### 📄 Document Support

* DOCX support
* TXT support
* Additional document formats

### 🔎 Better Answers

* Source citations
* Page-level document references
* Improved context retrieval

---

# 🔐 Security

DocuMind AI uses environment variables for sensitive API configuration.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

The actual `.env` file should **never be committed to the repository**.

Make sure `.env` is included in `.gitignore`.

---

# ☁️ Deployment Architecture

```text
                  USER
                    │
                    ▼
          ┌──────────────────┐
          │    Netlify       │
          │    Frontend      │
          └────────┬─────────┘
                   │
                   │ REST API
                   ▼
          ┌──────────────────┐
          │     Render       │
          │   FastAPI        │
          │    Backend       │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │    Groq LLM      │
          │ openai/gpt-oss-20b│
          └──────────────────┘
```

---

# 🌟 Why This Project?

DocuMind AI demonstrates how modern AI capabilities can be integrated with a traditional full-stack application to solve a practical problem.

The project combines:

```text
Frontend Development
        +
Backend API Development
        +
PDF Processing
        +
LLM Integration
        +
Context-Grounded AI
        +
Cloud Deployment
```

This makes DocuMind AI a practical example of building an **AI-powered full-stack application from end to end**.

---

# 👩‍💻 Author

### Tannu Kumari

**MCA | Full Stack Developer | AI Enthusiast**

* GitHub: github.com/tannukri01
* LinkedIn: linkedin.com/in/tannu-kumariofficial

---

# ⭐ Support

If you find **DocuMind AI** useful or interesting, consider giving the repository a ⭐ on GitHub.

Your support is appreciated!
