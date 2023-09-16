import speech_recognition as sr
import pyttsx3
class Speech_recognition:

    def __init__(self):
        self.recognizer = sr.Recognizer()



    def mic_testing(self):
        try:    
            with sr.Microphone() as mic:
                self.recognizer.adjust_for_ambient_noise(mic, duration= 0.2)
                audio = self.recognizer.listen(mic)
                text = self.recognizer.recognize_google(audio)
                text.lower()
                print(f"Output: {text}")

        except sr.UnknownValueError:
            
            self.recognizer = sr.Recognizer()

Speech_recognition().mic_testing()