import speech_recognition as sr
from textblob import TextBlob

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Say something...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=20)
        print("🔍 Recognizing...")

        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Sorry, could not understand audio.")
            return None
        except sr.RequestError:
            print("⚠️ Could not request results. Check internet connection.")
            return None

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "😊 Positive"
    elif sentiment < 0:
        return "😠 Negative"
    else:
        return "😐 Neutral"

if __name__ == "__main__":
    text = speech_to_text()
    if text:
        sentiment = analyze_sentiment(text)
        print(f"Sentiment: {sentiment}")
