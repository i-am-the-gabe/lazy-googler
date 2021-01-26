import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

print(sr.Microphone.list_microphone_names())

mic = sr.Microphone(device_index=0)

while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        result = r.recognize_google(audio, language="en")
        result = result.lower()

        if result.startswith("google"):
            webbrowser.open(f"https://www.google.com/search?q={result[6:]}")

        print(result)

    except sr.UnknownValueError as failed:
        print("Sorry, didn't get it.")
