import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import requests
from ai_engine import ask_kalki

# pip install pocketsphinx

newsapi = "Your News Api"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # Fixes the TTS freeze after the header line

def ProcessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open cricbuzz" in c.lower():
        webbrowser.open("https://www.cricbuzz.com")

    elif "open bts website" in c.lower():
        webbrowser.open("https://www.usbtsarmy.com")

    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        # 1. Fetch news from NewsAPI
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

        # 2. Check if HTTP request was successful (status code 200)
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            # 3. Check if any articles were returned
            if articles:
                speak("Here are the top five news headlines.")
                print("\n--- Top 5 Headlines ---")

                # 4. Read only the first 5 headlines
                for article in articles[:5]:
                    print("Speaking:", article['title'])
                    speak(article['title'])
                    print("Finished:", article['title'])

            else:
                # No articles were returned
                speak("Sorry, I couldn't find any news headlines at the moment.")
                print("No news articles were returned.")

        else:
            # NewsAPI request failed
            speak("Sorry, I was unable to fetch the news at the moment.")
            print("NewsAPI Error. Status code:", r.status_code)

    else:
        # Fallback to Groq AI if the command isn't a hardcoded website or tool
        print(f"Thinking...: {c}")
        ai_response = ask_kalki(c)
        print(f"Kalki: {ai_response}")
        speak(ai_response)


if __name__ == "__main__":
    speak("Initializing Kalki.....")

    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=5, phrase_time_limit=4)

            word = r.recognize_google(audio)

            if "kalki" in word.lower():
                speak("Ya")

                # Listen for command
                with sr.Microphone() as source:
                    print("Kalki Active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    ProcessCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))