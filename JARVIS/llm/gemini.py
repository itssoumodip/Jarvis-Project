import google.generativeai as genai
from func.speak import speak
def auto(query):
  # from func.listen import takeCommand
  # from JARVIS.func.speak import speak

  # Set up the API key directly
  api_key = "AIzaSyAVlVXv1q7M_DD5FFv8EHYeNDSsDWJ8--4"

  # Configure the API
  genai.configure(api_key=api_key)

  # Create the model
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
  )

  # Starting a chat session (update according to the documentation)
  chat_session = model.start_chat()  # Assuming no 'message' parameter is needed

  # Send a message to the chat session
  response = chat_session.send_message(query)
  print(f"JARVIS: {response.text}")
  speak(response.text)
