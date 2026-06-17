from ollama import chat

def generate_code(prompt):

    print("CALLING OLLAMA")

    response = chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("OLLAMA FINISHED")

    return response["message"]["content"]