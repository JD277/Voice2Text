import os # OS module to manage files
import google.generativeai as genai # Gemini's module

API_KEY= "YOUR_API_KEY" 
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-1.5-flash") # The model of IA that you will use
chat_session = model.start_chat( # To save the historial of the conversation
  history=[
  ]
)
def answer():
    myfile = genai.upload_file("graba.wav") # Upload the audio to google service
    result = model.generate_content([ myfile,"Transcribe Lo que dice este audio"]) # Transcribe the audio file to text
    print("pregunta enviada") 
    result2 = chat_session.send_message(result.text) # Send the transcription to gemini model to get the response
    print(result2.text) # Print the response in the console