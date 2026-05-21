from crewai import Agent, LLM
import os

llm = LLM(
    model="groq/llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

profile_analyzer = Agent(
    role="Profile Analyzer",
    goal="Analyze user skills, interests and identify strengths and weaknesses",
    backstory="You are an expert student profile analyst.",
    llm=llm,
    verbose=True
)

career_advisor = Agent(
    role="Career Advisor",
    goal="Suggest suitable career options.",
    backstory="You are an experienced career counselor.",
    llm=llm,
    verbose=True
)

roadmap_generator = Agent(
    role="Roadmap Generator",
    goal="Generate study roadmap.",
    backstory="You create structured learning plans.",
    llm=llm,
    verbose=True
)

learning_agent = Agent(
    role="Learning Agent",
    goal="Recommend courses, certifications and job tips.",
    backstory="You suggest learning resources.",
    llm=llm,
    verbose=True
)
