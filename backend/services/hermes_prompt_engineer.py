import os
import openai
from typing import Dict, Any

class HermesPromptEngineer:
    """
    Hermes-Powered Intelligent Prompt Engineer
    Takes a simple prompt and enhances it for ultra HD image generation
    """
    
    def __init__(self):
        # Initialize OpenAI client for prompt enhancement
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if self.openai_api_key:
            openai.api_key = self.openai_api_key
        self.hermes_api_key = os.getenv("HERMES_API_KEY")
        
    def enhance_prompt(self, simple_prompt: str, style: str = "ultra HD", 
                      details: str = "professional photography, 8k, detailed, sharp focus") -> Dict[str, Any]:
        """
        Enhance a simple prompt for better image generation results
        
        Args:
            simple_prompt: User's basic prompt
            style: Desired style (ultra HD, cinematic, artistic, etc.)
            details: Additional quality descriptors
            
        Returns:
            Dictionary with enhanced prompt and metadata
        """
        try:
            # If we have a specific Hermes API, we would use it here
            # For now, we'll use OpenAI to enhance the prompt
            
            enhancement_prompt = f"""
            You are an expert prompt engineer for AI image generation. 
            Take the following simple prompt and enhance it to create stunning, 
            ultra-high quality images suitable for professional use.
            
            Simple prompt: "{simple_prompt}"
            
            Enhance it with:
            1. Style: {style}
            2. Quality details: {details}
            3. Technical specifications (lighting, composition, camera settings if applicable)
            4. Artistic direction and mood
            5. Appropriate modifiers for the target AI model (Flux/Ideogram/DALL-E)
            
            Return ONLY the enhanced prompt, nothing else.
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Hermes, an expert AI prompt engineer specializing in creating ultra-detailed prompts for image generation models like Flux, Ideogram, and DALL-E."},
                    {"role": "user", "content": enhancement_prompt}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            enhanced_prompt = response.choices[0].message.content.strip()
            
            return {
                "original_prompt": simple_prompt,
                "enhanced_prompt": enhanced_prompt,
                "style": style,
                "details": details,
                "status": "success"
            }
            
        except Exception as e:
            # Fallback enhancement if API fails
            enhanced_prompt = f"{simple_prompt}, {style}, {details}, professional photography, 8k resolution, ultra detailed, sharp focus, cinematic lighting, award-winning"
            
            return {
                "original_prompt": simple_prompt,
                "enhanced_prompt": enhanced_prompt,
                "style": style,
                "details": details,
                "status": "fallback",
                "error": str(e)
            }

# Flask API endpoint function
def create_hermes_endpoint(app):
    """Create Flask endpoint for Hermes prompt enhancement"""
    from flask import request, jsonify
    
    @app.route('/api/hermes/enhance-prompt', methods=['POST'])
    def enhance_prompt_endpoint():
        try:
            data = request.json
            simple_prompt = data.get("prompt")
            style = data.get("style", "ultra HD")
            details = data.get("details", "professional photography, 8k, detailed, sharp focus")
            
            if not simple_prompt:
                return jsonify({"error": "Prompt is required"}), 400
                
            hermes = HermesPromptEngineer()
            result = hermes.enhance_prompt(simple_prompt, style, details)
            
            return jsonify(result)
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return app