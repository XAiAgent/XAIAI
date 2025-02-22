import os
import openai
from flask import Flask, request, jsonify

# Load environment variables (API keys)
from dotenv import load_dotenv
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/api/transcribe-audio', methods=['POST'])
def transcribe_audio():
    """
    Transcribe an audio file using OpenAI's Whisper API.
    """
    try:
        # Check if an audio file is included in the request
        if 'audio' not in request.files:
            return jsonify({"error": "No audio file provided"}), 400

        # Retrieve the uploaded file
        audio_file = request.files['audio']

        # Call OpenAI's Whisper API for transcription
        response = openai.Audio.transcribe("whisper-1", audio_file)

        # Extract the transcription text
        transcription = response.get('text', '')

        # Return the transcription
        return jsonify({"transcription": transcription})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to transcribe audio"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host="0.0.0.0", port=5001)
print("Transcribe Audio logic here")
B u g   f i x e s   i n   a u d i o   t r a n s c r i p t i o n  
 I m p r o v e d   p e r f o r m a n c e   o f   t r a n s c r i p t i o n   a l g o r i t h m  
 