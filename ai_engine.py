from groq import Groq

# Initialize Groq client with your API key
client = Groq(api_key="Your_Api_Key")

def ask_kalki(prompt: str) -> str:
    """
    Passes user input to Groq and returns Kalki's concise text response.
    """
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",  # Active model on Groq
            messages=[
                {
                    "role": "system",
                    # Keeping responses brief helps pyttsx3 speak without long delays
                    "content": "You are Kalki, an intelligent voice assistant. Give short, direct, and concise answers suitable for speech output."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_completion_tokens=200 # Keeps answers short and conversational
        )
        return completion.choices[0].message.content

    except Exception as e:
        print(f"Groq API Error: {e}")
        return "Sorry, I am having trouble connecting to my AI core."