# Virtual Assistant with Gemini API
## Objective
This project demonstrates how to use the Gemini API to build your own virtual assistant. The assistant responds to a wake word, processes user input, and provides intelligent answers. This project is designed as a hands-on tutorial for developers looking to learn how to integrate the Gemini API into their own projects, with a focus on voice interaction.

## Features
Wake Word Activation: The assistant listens for the wake word "Hey ADA" before processing any input.
Voice Recording: Once activated, the assistant records the user's voice, sends the audio input to the Gemini API, and receives a text response.
Custom Responses: Based on user prompts, the assistant provides intelligent responses in both text and voice formats.
## Requirements
Python 3.x
Gemini API Access
Libraries: pyaudio, speech_recognition
## How It Works
Wake Word Detection: The virtual assistant continuously listens for the phrase "Hey ADA". Once heard, the assistant starts recording the user's voice.
Processing: The recorded voice is sent to the Gemini API, where the user's query is processed.
Response: The assistant receives a text response from the API, which is then converted to a voice response for the user.
## Installation
Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
```
Install the required dependencies:


```bash
pip install -r requirements.txt
```
Set up your Gemini API key in the environment variables:


``` bash 
GEMINI_API_KEY='your-api-key'
```
Run the application:


```bash
python app1.py
```
# Files
- app1.py: Main application file that integrates wake word detection, voice recording, and communication with the Gemini API.
- grabar_audio2.py: Handles the audio recording and processing.
- on_start.py: Initializes the application and sets up necessary configurations.
# Contribution
Feel free to contribute by opening issues or submitting pull requests.
