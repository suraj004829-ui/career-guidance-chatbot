from crewai import Task
from agents import (
    profile_analyzer,
    career_advisor,
    roadmap_generator,
    learning_agent
)

def create_tasks(user_input):

    task1 = Task(
        description=f"""
        Analyze the following profile:

        {user_input}

        Identify:
        - Skills
        - Interests
        - Strengths
        - Weaknesses
        """,
        expected_output="""
        A profile analysis containing:
        skills, interests, strengths and weaknesses.
        """,
        agent=profile_analyzer
    )

    task2 = Task(
        description="""
        Suggest suitable career options based on profile analysis.
        Explain why each career fits.
        """,
        expected_output="""
        A list of career options with explanations.
        """,
        agent=career_advisor
    )

    task3 = Task(
        description="""
        Generate a step-by-step study roadmap.
        """,
        expected_output="""
        A structured learning roadmap with steps and timelines.
        """,
        agent=roadmap_generator
    )

    task4 = Task(
        description="""
        Recommend:
        - Courses
        - Certifications
        - Job preparation tips
        """,
        expected_output="""
        Recommended courses, certifications and preparation tips.
        """,
        agent=learning_agent
    )

    return [task1, task2, task3, task4]