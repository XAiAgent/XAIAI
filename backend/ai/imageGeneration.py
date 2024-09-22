print("Image Geimport openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set the environment variable or hardcode it

def generate_image(prompt):
    try:
        # Call OpenAI's DALL·E API to generate an image
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )

        # Retrieve the URL of the generated image
        image_url = response['data'][0]['url']
        return image_url

    except Exception as e:
        print(f"Error generating image: {e}")
        return None


if __name__ == "__main__":
    # Example of how to use the function
    prompt = "A futuristic city in the sky, with flying cars and neon lights"
    image_url = generate_image(prompt)
    
    if image_url:
        print(f"Generated Image URL: {image_url}")
    else:
        print("Failed to generate image.")
neration logic here")
