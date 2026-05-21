import os

os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["OTEL_SDK_DISABLED"] = "true"

from crew_setup import run_crew

print("\n===== Career Guidance Chatbot =====")

while True:

    user_input = input(
        "\nEnter your skills, interests and goals (type 'exit' to quit):\n"
    )

    if user_input.lower() == "exit":
        print("\nThank you for using Career Guidance Chatbot!")
        break

    try:
        result = run_crew(user_input)

        print("\n===== Result =====")
        print(result)

    except Exception as e:
        print("\nError:", e)
        print("Please try again.")