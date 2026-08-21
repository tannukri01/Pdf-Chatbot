\# 🤖 DocuMind AI



\### AI-Powered Document Intelligence using Retrieval-Augmented Generation (RAG)



> \*\*Upload a PDF → Ask questions → Get answers grounded in the document\*\*



DocuMind AI is a full-stack \*\*Retrieval-Augmented Generation (RAG)\*\* application that allows users to upload PDF documents and interact with them using natural language.



Instead of sending the entire document directly to an LLM, DocuMind AI converts the document into searchable vector representations, retrieves the most relevant sections for each query, and uses an LLM to generate a context-aware response.



\---



\## 🚀 Why This Project?



Large PDF documents are difficult to search manually.



DocuMind AI solves this problem by combining:



\* 📄 PDF document processing

\* 🧩 Intelligent text chunking

\* 🔎 Semantic similarity search

\* 🧠 Vector embeddings

\* ⚡ FAISS vector database

\* 🤖 Groq-powered LLM inference

\* 🔗 Retrieval-Augmented Generation (RAG)

\* 🌐 FastAPI REST APIs

\* 💻 Responsive web interface



This project demonstrates an \*\*end-to-end AI application\*\*, from document ingestion and retrieval to LLM-based response generation.



\---



\## ✨ Features



\* 📑 Upload single or multiple PDF documents

\* 🔍 Semantic search instead of simple keyword matching

\* 🧠 Context-aware answers using RAG

\* ⚡ Fast response generation using Groq

\* 🆓 Uses free/open-source components instead of paid OpenAI APIs

\* 📱 Responsive and clean web interface

\* 🔗 RESTful backend APIs using FastAPI

\* 🛡️ Answers are grounded in retrieved document context

\* 📚 Works with resumes, notes, reports, study material and other text-based PDFs



\---



\## 🧠 How RAG Works



```mermaid

flowchart TD

&#x20;   A\[User Uploads PDF] --> B\[PDF Document Loader]

&#x20;   B --> C\[Text Extraction]

&#x20;   C --> D\[Text Chunking]

&#x20;   D --> E\[HuggingFace Embeddings]

&#x20;   E --> F\[(FAISS Vector Store)]



&#x20;   G\[User Question] --> H\[Query Embedding]

&#x20;   H --> F

&#x20;   F --> I\[Relevant Document Chunks]

&#x20;   I --> J\[Prompt with Retrieved Context]

&#x20;   J --> K\[Groq LLM]

&#x20;   K --> L\[Context-Grounded Answer]

&#x20;   L --> M\[User]

```



The architecture follows the standard RAG flow: documents are transformed into embeddings, relevant chunks are retrieved for a query, and the LLM generates the final response using that retrieved context.



GitHub supports Mermaid diagrams directly inside Markdown files.



\---



\## 🏗️ System Architecture



\### Document Ingestion



```text

PDF

&#x20;↓

Document Loader

&#x20;↓

Text Extraction

&#x20;↓

Recursive Text Splitting

&#x20;↓

Embedding Model

&#x20;↓

FAISS Vector Store

```



\### Question Answering



```text

User Question

&#x20;↓

Query Embedding

&#x20;↓

FAISS Similarity Search

&#x20;↓

Top Relevant Chunks

&#x20;↓

Prompt Construction

&#x20;↓

Groq LLM

&#x20;↓

Final Answer

```



\---



\## 🛠️ Tech Stack



\### Frontend



\* HTML5

\* Tailwind CSS

\* Vanilla JavaScript



\### Backend



\* Python

\* FastAPI

\* Uvicorn



\### AI / RAG



\* LangChain

\* HuggingFace Sentence Transformers

\* `all-MiniLM-L6-v2`

\* FAISS

\* Groq LLM



\### Development Tools



\* Git

\* GitHub

\* Python Virtual Environment

\* REST APIs



\---



\## 🔥 Key Technical Highlights



\### 1. Retrieval-Augmented Generation



Implemented an end-to-end RAG pipeline where the LLM receives relevant document context before generating an answer.



\### 2. Semantic Search



Instead of relying only on exact keywords, user questions are converted into embeddings and matched against document embeddings using vector similarity.



\### 3. Vector Database



FAISS is used to efficiently store and retrieve document embeddings.



\### 4. Local Embedding Model



The project uses:



```text

sentence-transformers/all-MiniLM-L6-v2

```



This provides lightweight semantic embeddings without depending on a paid embedding API.



\### 5. LLM Integration



Groq is integrated for fast LLM inference, allowing the application to generate responses with low latency.



\### 6. REST API Backend



FastAPI handles:



\* PDF uploads

\* Document processing

\* Query requests

\* RAG pipeline execution

\* Response generation

\* CORS configuration



\---



\## 📂 Project Structure



```text

pdf-chatbot/

│

├── backend/

│   ├── main.py

│   ├── requirements.txt

│   └── .env

│

├── frontend/

│   └── index.html

│

├── .gitignore

└── README.md

```



\---



\## ⚙️ Installation \& Setup



\### 1. Clone Repository



```bash

git clone https://github.com/YOUR\_USERNAME/pdf-chatbot.git



cd pdf-chatbot

```



\### 2. Create Virtual Environment



```bash

cd backend



python -m venv venv

```



\### 3. Activate Virtual Environment



\#### Windows



```bash

venv\\Scripts\\activate

```



\#### macOS / Linux



```bash

source venv/bin/activate

```



\### 4. Install Dependencies



```bash

pip install -r requirements.txt

```



\### 5. Configure Environment Variables



Create a `.env` file inside the `backend` folder:



```env

GROQ\_API\_KEY=your\_groq\_api\_key

```



> Never commit your `.env` file or API keys to GitHub.



\### 6. Start Backend



```bash

uvicorn main:app --reload --port 8000

```



Backend:



```text

http://localhost:8000

```



\### 7. Start Frontend



Open a new terminal:



```bash

cd frontend



python -m http.server 5500

```



Open:



```text

http://localhost:5500

```



\---



\## 🔌 API Overview



\### Upload PDF



```http

POST /upload

```



Uploads a PDF and processes it for semantic retrieval.



\### Ask Question



```http

POST /ask

```



Accepts a natural-language question and returns an answer generated from retrieved document context.



\### Example



```json

{

&#x20; "question": "What are the main skills mentioned in this resume?"

}

```



Response:



```json

{

&#x20; "answer": "The resume highlights Java, Python, React, FastAPI and SQL..."

}

```



> Update the endpoint names above if your actual `main.py` uses different routes.



\---



\## 🖥️ Application Flow



```text

1\. User uploads PDF

&#x20;       ↓

2\. PDF text is extracted

&#x20;       ↓

3\. Text is divided into meaningful chunks

&#x20;       ↓

4\. Chunks are converted into embeddings

&#x20;       ↓

5\. Embeddings are stored in FAISS

&#x20;       ↓

6\. User asks a question

&#x20;       ↓

7\. Query is converted into an embedding

&#x20;       ↓

8\. Similar document chunks are retrieved

&#x20;       ↓

9\. Retrieved context is passed to Groq LLM

&#x20;       ↓

10\. User receives the generated answer

```



\---



\## 📸 Screenshots



Add screenshots of your actual application here:



```text

docs/

├── upload-screen.png

├── chat-screen.png

└── result-screen.png

```



Then add:



```markdown

\### Upload PDF



!\[Upload PDF](docs/upload-screen.png)



\### Ask Questions



!\[Chat Interface](docs/chat-screen.png)



\### AI Response



!\[AI Response](docs/result-screen.png)

```



\*\*Tip:\*\* Add 2–3 clean screenshots. A recruiter should be able to understand the UI without running the project.



\---



\## 🎯 Real-World Use Cases



DocuMind AI can be adapted for:



\* 📄 Resume analysis

\* 📚 Study material

\* 🏢 Company reports

\* 📑 Research papers

\* 📋 Policy documents

\* ⚖️ Legal documents

\* 📊 Business reports

\* 🧾 Internal documentation

\* 🎓 Academic notes



\---



\## 💡 What I Learned



Through this project, I gained practical experience in:



\* Building an end-to-end RAG pipeline

\* Working with unstructured PDF data

\* Document loading and text extraction

\* Recursive text splitting

\* Vector embeddings

\* Semantic similarity search

\* FAISS vector stores

\* LLM integration

\* Prompt construction

\* FastAPI REST API development

\* File upload handling

\* CORS configuration

\* Frontend-backend integration

\* Environment variable management

\* Git and GitHub project management



\---



\## 🚧 Current Limitations



\* Primarily designed for text-based PDFs

\* Vector data is currently not persistent across server restarts

\* No user authentication yet

\* Chat history is not permanently stored

\* Large documents may require optimized chunking and retrieval strategies



\---



\## 🔮 Future Improvements



\* \[ ] Persistent vector database

\* \[ ] Chat history

\* \[ ] User authentication

\* \[ ] Multi-user document isolation

\* \[ ] DOCX and TXT support

\* \[ ] Streaming LLM responses

\* \[ ] Source citations for retrieved chunks

\* \[ ] Conversation memory

\* \[ ] Cloud deployment

\* \[ ] RAG evaluation and retrieval metrics

\* \[ ] Document-level access control



\---



\## 📊 Future RAG Evaluation



A future version can evaluate retrieval quality using metrics such as:



```text

Retrieval Accuracy

Context Relevance

Answer Relevance

Faithfulness

Response Latency

```



This would make the project more suitable for production-oriented AI engineering workflows.



\---



\## 🔐 Security Notes



\* API keys are stored using environment variables.

\* `.env` should never be committed to GitHub.

\* Uploaded documents should be validated before processing.

\* Production deployment should include authentication and document-level authorization.



\---



\## ⭐ Project Highlights



```text

✔ End-to-End RAG Application

✔ Semantic PDF Search

✔ Vector Embeddings

✔ FAISS Retrieval

✔ Groq LLM Integration

✔ FastAPI Backend

✔ REST API

✔ Responsive Frontend

✔ Free/Open-Source AI Stack

```



\---



\## 👩‍💻 Author



\### Tannu Kumari



\*\*MCA | Full Stack Developer | AI/RAG Enthusiast\*\*



\* GitHub: https://github.com/tannukri01

\* LinkedIn: https://www.linkedin.com/in/tannu-kumariofficial



\---



\## 📌 Project Summary



\*\*DocuMind AI demonstrates how modern AI systems can combine traditional backend engineering with vector search, embeddings, and Large Language Models to build practical document-intelligence applications.\*\*



The project focuses on solving a real-world problem: \*\*making large PDF documents easier to understand and interact with through natural language.\*\*



\---



\## ⭐ If you find this project useful



Give the repository a ⭐ on GitHub!



