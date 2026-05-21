from crewai import Crew
from agents import (
    profile_analyzer,
    career_advisor,
    roadmap_generator,
    learning_agent
)

from tasks import create_tasks


def run_crew(user_input):

    tasks = create_tasks(user_input)

    crew = Crew(
        agents=[
            profile_analyzer,
            career_advisor,
            roadmap_generator,
            learning_agent
        ],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    return result