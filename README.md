
# 🧠 Smart Resume & Cover Letter Generator Agent

An AI-powered resume assistant that takes your resume (or LinkedIn export) and a job description, then generates:

- ✅ Tailored resume bullet points  
- 📝 Personalized cover letters  
- ❓ Interview preparation Q&A  
- 📊 Skill gap and job match analysis  

Runs completely **locally** using a LLaMA-based large language model — no internet or API keys needed!

---

## ⚙️ Features

- Upload resume in PDF, DOCX, or text
- Paste or upload job description
- Generates custom application content with local LLM
- Uses Retrieval-Augmented Generation (RAG) and memory
- Clean UI built in Streamlit

---

## 🛠️ Tech Stack

| Component        | Tool/Library              |
|------------------|---------------------------|
| Frontend         | Streamlit                 |
| Backend          | Python                    |
| LLM              | LLaMA (via `llama-cpp-python`) |
| Embeddings       | `sentence-transformers`   |
| Vector Store     | FAISS                     |
| File Parsing     | PyPDF2, docx2txt          |
| AI Logic         | LangChain                 |

---

## 🧪 Local Setup Instructions

### Step 1: Clone this repo

```bash
git clone https://github.com/your-username/smart-resume-agent.git
cd smart-resume-agent
````

### Step 2: Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download a LLaMA model

* Download a `.ggml` or `.gguf` model file (e.g., LLaMA 2 7B) from Hugging Face or other sources.
* Place the file in the `models/` directory.
* Example: `models/ggml-model.bin`

### Step 5: Create a `.env` file

Manually create a `.env` file in the root directory:

```ini
# .env
MODEL_PATH=models/ggml-model.bin
```

You can add more environment variables here if needed.

---

### Step 6: Run the app

```bash
streamlit run app.py
```



## 📦 requirements.txt

```txt
streamlit
langchain
llama-cpp-python
faiss-cpu
python-dotenv
PyPDF2
docx2txt
spacy
tiktoken
transformers
sentence-transformers
```



## 👤 Author

Created by \Rashi Makadia
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/rashi-makadia-11a10a249/)

```
