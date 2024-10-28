import speech_recognition as sr
from grabar_audio2 import record_prompt
from app1 import answer

recognizer = sr.Recognizer()
microphone = sr.Microphone()
def listen_for_wake_word():
    
    """Continuously listens for the wake word 'Hey ADA'."""
    with microphone as source:
        print("Listening for wake word 'Hola ADA'...")
        while True:
            try:
                # Recognize the speech using Google Speech Recognition
                audio_data = recognizer.listen(source,timeout=10, phrase_time_limit=10)
                text = recognizer.recognize_google(audio_data)
                print(f"Heard: {text.lower()}")
                if "hola" in text.lower():  # If wake word is detected
                    print("Hola soy Ada")
                    record_prompt() # Records the prompt
                    answer() # answer to the user
                    break
            except sr.WaitTimeoutError:
                print("Listening timeout... continuing")
            except sr.UnknownValueError:
                pass  # Ignore unrecognized speech
            except sr.RequestError as e:
                print(f"Error with recognition service: {e}")

listen_for_wake_word() # calls the funtion to start the program
