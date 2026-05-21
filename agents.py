from crewai import Agent, LLM


llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key="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"
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