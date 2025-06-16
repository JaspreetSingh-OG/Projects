import speech_recognition as sr
import webbrowser
import pyttsx3
from musiclib import play  # Your custom module
import requests

engine = pyttsx3.init()
newsapi="e7cc0ef0a364474bb081a7385af88f2a"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open chatgpt" in command:
        webbrowser.open("https://chatgpt.com")
    elif command.startswith("play"):
        song = command.replace("play", "", 1).strip()
        if song:
            speak(f"Playing {song} on YouTube")
            play(song)
        else:
            speak("Please say the name of the song after 'play'.")
    elif "news" in command:
        try:
            r = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=in&apiKey=e7cc0ef0a364474bb081a7385af88f2a")
            if r.status_code == 200:
                data = r.json()
                if data["status"] == "ok":
                    articles = data["articles"]
                    speak("Here are the top headlines:")
                    for i, article in enumerate(articles[:5], 1):  # Top 5 headlines
                        title = article['title']
                        print(f"{i}. {title}")
                        speak(f"Headline {i}: {title}")
                else:
                    speak("Failed to fetch news from the API.")
            else:
                speak("Something went wrong while connecting to the news server.")
        except Exception as e:
            print("Error fetching news:", e)
            speak("Sorry, I could not fetch the news right now.")
    else:
        # Let OpenAI handle the request
        #will Introduced Soon...
        pass


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                print("Say 'Jarvis' to wake...")
                audio = recognizer.listen(source, timeout=5)
                wake_word = recognizer.recognize_google(audio)

                if wake_word.lower() == "jarvis":
                    speak("Yes, I'm listening...")
                    print("Jarvis Active. Say your command...")

                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio)
                    print("Command received:", command)
                    processCommand(command)

        except sr.WaitTimeoutError:
            print("Timeout. No voice detected.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
