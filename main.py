import os
from openai import OpenAI

# Get your API key from an environment variable.
# Never put your API key directly into this file.
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise SystemExit(
        "ERROR: OPENAI_API_KEY is not set. "
        "Set your API key as an environment variable and run again."
    )

client = OpenAI(api_key=api_key)

instructions = """
You are My AI Assistant, a helpful, friendly and intelligent AI assistant.
Answer clearly and accurately.
If you are unsure about something, say so instead of making it up.
"""

print("=" * 50)
print("        MY AI ASSISTANT")
print("=" * 50)
print("Type 'exit' or 'quit' to stop.")
print()

previous_response_id = None

while True:
    user_message = input("You: ").strip()

    if user_message.lower() in {"exit", "quit"}:
        print("AI: Goodbye!")
        break

    if not user_message:
        continue

    try:
        request = {
            "model": "gpt-5.6-luna",
            "instructions": instructions,
            "input": user_message,
        }

        if previous_response_id:
            request["previous_response_id"] = previous_response_id

        response = client.responses.create(**request)

        print("\nAI:", response.output_text)
        print()

        previous_response_id = response.id

    except Exception as error:
        print("\nERROR:", error)
        print()
