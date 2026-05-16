import os
import openai
from typing import Dict, Any
import json

class ClaudeStorytellerAgent:
    """
    Claude Storyteller Agent
    Generates full lore, Twitter thread, and description for images
    """
    
    def __init__(self):
        # Initialize OpenAI client (using GPT-4 as Claude alternative for now)
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if self.openai_api_key:
            openai.api_key = self.openai_api_key
        self.claude_api_key = os.getenv("CLAUDE_API_KEY")
        
    def generate_story(self, image_url: str, context: str = "") -> Dict[str, Any]:
        """
        Generate lore, Twitter thread, and description for an image
        
        Args:
            image_url: URL of the image to create story for
            context: Additional context about the image (optional)
            
        Returns:
            Dictionary with lore, Twitter thread, description, and metadata
        """
        try:
            # Since we don't have direct image input in text-only API,
            # we'll work with the image URL as context and ask for creative interpretation
            # In a real implementation with Claude Vision API, we would analyze the image directly
            
            story_prompt = f"""
            You are a master storyteller and content creator. 
            Given an image at this URL: {image_url}
            {f"Additional context: {context}" if context else ""}
            
            Create:
            1. A rich lore/backstory for this image (2-3 paragraphs)
            2. A engaging Twitter thread (3-5 tweets) about this image
            3. A detailed description suitable for NFT metadata or art gallery
            
            Make it creative, engaging, and suitable for an NFT collection.
            Format your response as JSON with keys: lore, twitter_thread, description
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Using GPT-4 as Claude alternative
                messages=[
                    {"role": "system", "content": "You are Claude, a master storyteller and content creator who specializes in creating engaging narratives, lore, and social media content for visual art and NFTs."},
                    {"role": "user", "content": story_prompt}
                ],
                max_tokens=1000,
                temperature=0.8
            )
            
            # Parse the JSON response
            try:
                result = json.loads(response.choices[0].message.content.strip())
            except json.JSONDecodeError:
                # If not valid JSON, structure it ourselves
                content = response.choices[0].message.content.strip()
                lines = content.split('\n')
                lore = ""
                twitter_thread = ""
                description = ""
                
                current_section = None
                for line in lines:
                    if "lore" in line.lower() or "backstory" in line.lower():
                        current_section = "lore"
                    elif "twitter" in line.lower() or "thread" in line.lower():
                        current_section = "twitter_thread"
                    elif "description" in line.lower():
                        current_section = "description"
                    elif current_section and line.strip():
                        if current_section == "lore":
                            lore += line + " "
                        elif current_section == "twitter_thread":
                            twitter_thread += line + " "
                        elif current_section == "description":
                            description += line + " "
                
                result = {
                    "lore": lore.strip(),
                    "twitter_thread": twitter_thread.strip(),
                    "description": description.strip()
                }
            
            return {
                "image_url": image_url,
                "context": context,
                "lore": result.get("lore", ""),
                "twitter_thread": result.get("twitter_thread", ""),
                "description": result.get("description", ""),
                "status": "success"
            }
            
        except Exception as e:
            return {
                "image_url": image_url,
                "context": context,
                "lore": "",
                "twitter_thread": "",
                "description": "",
                "status": "error",
                "error": str(e)
            }

# Flask API endpoint function
def create_claude_endpoint(app):
    """Create Flask endpoint for Claude storyteller"""
    from flask import request, jsonify
    
    @app.route('/api/claude/generate-story', methods=['POST'])
    def generate_story_endpoint():
        try:
            data = request.json
            image_url = data.get("image_url")
            context = data.get("context", "")
            
            if not image_url:
                return jsonify({"error": "Image URL is required"}), 400
                
            storyteller = ClaudeStorytellerAgent()
            result = storyteller.generate_story(image_url, context)
            
            return jsonify(result)
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return app