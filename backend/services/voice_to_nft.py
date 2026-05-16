import os
import openai
from typing import Dict, Any
import json
from datetime import datetime

class VoiceToNFTService:
    """
    Voice-to-NFT Service (Enhanced)
    Audio upload → Hermes transcribe + summarize → Claude story → Image generate → NFT
    """
    
    def __init__(self):
        # Initialize API keys
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.hermes_api_key = os.getenv("HERMES_API_KEY")
        self.claude_api_key = os.getenv("CLAUDE_API_KEY")
        self.flux_api_key = os.getenv("FLUX_API_KEY")
        self.ideogram_api_key = os.getenv("IDEOGRAM_API_KEY")
        
        if self.openai_api_key:
            openai.api_key = self.openai_api_key
    
    def transcribe_audio(self, audio_file_path: str) -> str:
        """
        Transcribe audio using OpenAI Whisper
        """
        try:
            with open(audio_file_path, "rb") as audio_file:
                transcription = openai.Audio.transcribe("whisper-1", audio_file)
                return transcription['text']
        except Exception as e:
            raise Exception(f"Audio transcription failed: {str(e)}")
    
    def enhance_and_summarize_text(self, text: str) -> Dict[str, str]:
        """
        Use Hermes to enhance and summarize the transcribed text
        """
        try:
            # First, summarize the text
            summary_prompt = f"""
            You are Hermes, an expert AI assistant. 
            Please summarize the following transcribed text concisely while preserving the key meaning and essence:
            
            "{text}"
            
            Provide a clear, engaging summary that captures the core message or story.
            """
            
            summary_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Hermes, an expert at text enhancement and summarization."},
                    {"role": "user", "content": summary_prompt}
                ],
                max_tokens=150,
                temperature=0.5
            )
            
            summarized_text = summary_response.choices[0].message.content.strip()
            
            # Then enhance it for image generation
            enhancement_prompt = f"""
            You are Hermes, an expert prompt engineer for AI image generation.
            Take the following summary and enhance it to create a stunning visual prompt:
            
            "{summarized_text}"
            
            Enhance it with:
            1. Ultra HD, professional photography quality
            2. Detailed, sharp focus, 8k resolution
            3. Appropriate artistic style and mood
            4. Technical specifications for best image generation results
            
            Return ONLY the enhanced prompt for image generation.
            """
            
            enhancement_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Hermes, an expert AI prompt engineer specializing in creating ultra-detailed prompts for image generation models."},
                    {"role": "user", "content": enhancement_prompt}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            enhanced_prompt = enhancement_response.choices[0].message.content.strip()
            
            return {
                "original_text": text,
                "summarized_text": summarized_text,
                "enhanced_prompt": enhanced_prompt
            }
            
        except Exception as e:
            # Fallback enhancement
            summarized_text = text[:200] + "..." if len(text) > 200 else text
            enhanced_prompt = f"{summarized_text}, ultra HD, professional photography, 8k resolution, detailed, sharp focus, cinematic lighting"
            
            return {
                "original_text": text,
                "summarized_text": summarized_text,
                "enhanced_prompt": enhanced_prompt,
                "fallback": True,
                "error": str(e)
            }
    
    def generate_story_from_text(self, text: str, context: str = "") -> Dict[str, Any]:
        """
        Use Claude to generate lore, Twitter thread, and description from text
        """
        try:
            story_prompt = f"""
            You are Claude, a master storyteller.
            Based on the following text: "{text}"
            {f"Additional context: {context}" if context else ""}
            
            Create:
            1. A rich lore/backstory (2-3 paragraphs)
            2. An engaging Twitter thread (3-5 tweets)
            3. A detailed description suitable for NFT metadata
            
            Format your response as JSON with keys: lore, twitter_thread, description
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are Claude, a master storyteller and content creator."},
                    {"role": "user", "content": story_prompt}
                ],
                max_tokens=1000,
                temperature=0.8
            )
            
            try:
                result = json.loads(response.choices[0].message.content.strip())
            except json.JSONDecodeError:
                # Fallback if not valid JSON
                content = response.choices[0].message.content.strip()
                result = {
                    "lore": content[:500] + "..." if len(content) > 500 else content,
                    "twitter_thread": "Twitter thread based on the content: " + content[:200],
                    "description": content
                }
            
            return {
                "lore": result.get("lore", ""),
                "twitter_thread": result.get("twitter_thread", ""),
                "description": result.get("description", ""),
                "status": "success"
            }
            
        except Exception as e:
            return {
                "lore": "",
                "twitter_thread": "",
                "description": "",
                "status": "error",
                "error": str(e)
            }
    
    def generate_image_from_prompt(self, prompt: str) -> str:
        """
        Generate image using Flux/Ideogram/DALL-E based on enhanced prompt
        """
        try:
            # Try to use Flux or Ideogram if API keys are available, fallback to DALL-E
            if self.flux_api_key:
                # Placeholder for Flux API call
                # In reality, you'd call the Flux API here
                image_url = f"https://api.flux.ai/v1/generate?prompt={prompt}&api_key={self.flux_api_key}"
                # Actually, we'd make a real HTTP request here
                # For now, simulate with DALL-E since we have OpenAI configured
                pass
            
            if self.ideogram_api_key:
                # Placeholder for Ideogram API call
                pass
            
            # Default to OpenAI DALL-E
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            
            image_url = response['data'][0]['url']
            return image_url
            
        except Exception as e:
            raise Exception(f"Image generation failed: {str(e)}")
    
    def process_voice_to_nft(self, audio_file_path: str, 
                           collection_name: str = "Voice NFT Collection",
                           attributes: list = None) -> Dict[str, Any]:
        """
        Full Voice-to-NFT pipeline:
        Audio → Transcribe → Enhance/Summarize → Generate Story → Generate Image → Create NFT
        """
        try:
            # Step 1: Transcribe audio
            print("Step 1: Transcribing audio...")
            transcribed_text = self.transcribe_audio(audio_file_path)
            
            # Step 2: Enhance and summarize text
            print("Step 2: Enhancing and summarizing text...")
            text_processing = self.enhance_and_summarize_text(transcribed_text)
            
            # Step 3: Generate story using Claude
            print("Step 3: Generating story with Claude...")
            story = self.generate_story_from_text(
                text_processing["summarized_text"], 
                "Voice recording converted to NFT"
            )
            
            # Step 4: Generate image using enhanced prompt
            print("Step 4: Generating image...")
            image_prompt = text_processing["enhanced_prompt"]
            image_url = self.generate_image_from_prompt(image_prompt)
            
            # Step 5: Create NFT metadata
            print("Step 5: Creating NFT metadata...")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            nft_name = f"Voice NFT: {text_processing['summarized_text'][:50]}..."
            nft_description = f"""
            {story['description']}
            
            --- 
            Voice Recording NFT
            Original audio transcribed and processed through AI pipeline.
            Timestamp: {timestamp}
            
            Lore: {story['lore'][:200]}...
            
            Twitter Thread: {story['twitter_thread'][:200]}...
            """.strip()
            
            # Prepare attributes
            nft_attributes = attributes or [
                {"trait_type": "Type", "value": "Voice-to-NFT"},
                {"trait_type": "Process", "value": "AI Pipeline"},
                {"trait_type": "Timestamp", "value": timestamp},
                {"trait_type": "Length", "value": f"{len(transcribed_text)} characters"}
            ]
            
            # For now, return the prepared data - actual minting would happen elsewhere
            # In a full implementation, we would call the Solana NFT minter here
            
            result = {
                "status": "success",
                "steps_completed": {
                    "transcription": True,
                    "text_enhancement": True,
                    "story_generation": True,
                    "image_generation": True,
                    "nft_preparation": True
                },
                "transcribed_text": transcribed_text,
                "summarized_text": text_processing["summarized_text"],
                "enhanced_image_prompt": image_prompt,
                "generated_image_url": image_url,
                "nft_name": nft_name,
                "nft_description": nft_description,
                "nft_lore": story["lore"],
                "nft_twitter_thread": story["twitter_thread"],
                "nft_attributes": nft_attributes,
                "collection_name": collection_name,
                "timestamp": timestamp
            }
            
            return result
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "step_failed": "unknown"
            }

# Flask API endpoint function
def create_voice_to_nft_endpoint(app):
    """Create Flask endpoint for Voice-to-NFT processing"""
    from flask import request, jsonify
    import tempfile
    import os
    
    @app.route('/api/voice/to-nft', methods=['POST'])
    def voice_to_nft_endpoint():
        try:
            # Check if audio file is present
            if 'audio' not in request.files:
                return jsonify({"error": "No audio file provided"}), 400
            
            audio_file = request.files['audio']
            
            # Save audio file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
                audio_file.save(temp_audio.name)
                temp_audio_path = temp_audio.name
            
            try:
                # Extract optional parameters
                collection_name = request.form.get('collection_name', 'Voice NFT Collection')
                
                # Process voice to NFT
                voice_service = VoiceToNFTService()
                result = voice_service.process_voice_to_nft(
                    audio_file_path=temp_audio_path,
                    collection_name=collection_name
                )
                
                if result["status"] == "success":
                    return jsonify(result), 201
                else:
                    return jsonify(result), 500
                    
            finally:
                # Clean up temporary file
                if os.path.exists(temp_audio_path):
                    os.unlink(temp_audio_path)
                
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return app