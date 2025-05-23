from langchain.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import CharacterTextSplitter

class ResumeAgent:
    def __init__(self, resume_text, job_text, skills_required, model_path="./models/ggml-model.bin"):
        self.resume_text = resume_text
        self.job_text = job_text
        self.skills_required = skills_required

        # Initialize local LLaMA model
        self.llm = LlamaCpp(model_path=model_path, temperature=0.7)

        self.memory = ConversationBufferMemory()
        self.vector_store = self._build_vector_store()

    def _build_vector_store(self):
        splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = splitter.create_documents([self.resume_text + self.job_text])
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        return FAISS.from_documents(docs, embeddings)

    def generate_resume_lines(self):
        prompt = (
            "Given the resume and job description, generate bullet points tailored to this job."
        )
        retriever = self.vector_store.as_retriever()
        qa = RetrievalQA.from_chain_type(llm=self.llm, retriever=retriever)
        return qa.run(prompt)

    def generate_cover_letter(self):
        prompt = (
            "Generate a personalized cover letter based on the resume and job description."
        )
        return self.llm(prompt)

    def generate_interview_questions(self):
        prompt = (
            "Generate behavioral and technical interview questions relevant to this candidate."
        )
        return self.llm(prompt)

    def analyze_skill_gaps(self):
        prompt = f"List missing skills compared to job requirements: {self.skills_required}"
        return self.llm(prompt)
