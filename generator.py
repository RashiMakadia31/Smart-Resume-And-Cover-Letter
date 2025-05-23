from .resume_parser import parse_resume
from .job_description_parser import parse_job_description
from .llm_agent import ResumeAgent

def generate_all_outputs(resume_file, job_file):
    resume_text = parse_resume(resume_file)
    job_text, skills_required = parse_job_description(job_file)

    agent = ResumeAgent(resume_text, job_text, skills_required)

    return {
        "resume_lines": agent.generate_resume_lines(),
        "cover_letter": agent.generate_cover_letter(),
        "interview_qa": agent.generate_interview_questions(),
        "skill_gap": agent.analyze_skill_gaps()
    }
