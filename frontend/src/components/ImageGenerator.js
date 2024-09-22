import React, { useState } from "react";
import axios from "axios";
import "./ImageGenerator.css"; // Optional: For styling

const ImageGenerator = () => {
  const [prompt, setPrompt] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleGenerateImage = async () => {
    if (!prompt.trim()) {
      setError("Please enter a valid prompt.");
      return;
    }

    setError("");
    setLoading(true);
    setImageUrl("");

    try {
      const response = await axios.post("/api/generate-image", { prompt });
      setImageUrl(response.data.imageUrl); // Assuming the API returns the image URL in response.data.imageUrl
    } catch (err) {
      console.error("Error generating image:", err);
      setError("Failed to generate image. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="image-generator">
      <h1>AI Image Generator</h1>
      <div className="form-group">
        <label htmlFor="prompt">Enter your prompt:</label>
        <textarea
          id="prompt"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Describe the image you want to generate..."
        />
      </div>
      <button onClick={handleGenerateImage} disabled={loading}>
        {loading ? "Generating..." : "Generate Image"}
      </button>

      {error && <p className="error">{error}</p>}

      {imageUrl && (
        <div className="image-preview">
          <h2>Generated Image:</h2>
          <img src={imageUrl} alt="Generated AI" />
        </div>
      )}
    </div>
  );
};

export default ImageGenerator;
console.log("Image Generator Component")
