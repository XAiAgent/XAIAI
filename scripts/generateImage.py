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

@app.route('/api/generate-image', methods=['POST'])
def generate_image():
    """
    Generate an image based on a text prompt using OpenAI's DALL-E API.
    """
    try:
        # Get the prompt from the request
        data = request.json
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Call OpenAI's DALL-E API
        response = openai.Image.create(
            prompt=prompt,
            n=1,                # Number of images to generate
            size="1024x1024"    # Image resolution
        )

        # Extract the image URL
        image_url = response['data'][0]['url']

        # Return the image URL
        return jsonify({"imageUrl": image_url})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to generate image"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)
print("Generate AI Image")
N e w   f e a t u r e   a d d e d  
 R e f a c t o r   i m a g e   g e n e r a t i o n   l o g i c  
 