import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set the environment variable or hardcode it

def transcribe_audio(audio_file_path):
    try:
        # Open the audio file
        with open(audio_file_path, "rb") as audio_file:
            # Transcribe audio using OpenAI Whisper
            transcription = openai.Audio.transcribe("whisper-1", audio_file)
            
            # Return the transcribed text
            return transcription['text']

    except Exception as e:
        print(f"Error processing audio: {e}")
        return None


if __name__ == "__main__":
    # Example usage: Path to the audio file you want to transcribe
    audio_file_path = "path_to_audio_file.wav"
    
    transcribed_text = transcribe_audio(audio_file_path)
    
    if transcribed_text:
        print(f"Transcription: {transcribed_text}")
    else:
        print("Failed to transcribe audio.")
print("Voice Processing logic here")
