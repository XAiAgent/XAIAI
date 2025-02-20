connect on https://x.com/XAIdotfun

# XAIAI: Bridging AI and Blockchain

XAIAI is an innovative project that combines artificial intelligence (AI) with blockchain technology to create tools for engagement and fun. This project leverages AI for generating images and processing audio, integrates BSC blockchain for NFT creation, and includes a modern frontend to interact with these features.

---

## Features

### **1. AI-Powered Image Generation**
- Generate stunning AI-based images using OpenAI's DALL-E API.
- Accepts text prompts to create unique visuals.

### **2. Audio Transcription**
- Transcribe audio files to text using OpenAI's Whisper API.
- Supports common audio formats such as MP3, WAV, and FLAC.

### **3. Blockchain Integration**
- Create NFTs on the BSC blockchain.
- Use smart contracts to mint and manage NFTs.

### **4. Interactive Frontend**
- Modern React-based frontend to interact with AI tools and blockchain features seamlessly.

---

## Project Structure

```
XAIAI/
├── backend/
│   ├── ai/
│   │   ├── imageGeneration.py
│   │   ├── voiceProcessing.py
│   ├── BSC/
│   │   ├── createNFT.js
│   │   ├── BSCWallet.js
├── contracts/
│   ├── imageNFT
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ImageGenerator.js
├── scripts/
│   ├── generateImage.py
│   ├── transcribeAudio.py
├── requirements.txt
├── README.md
```

---

## Installation

### Prerequisites

- Python 3.9+
- Node.js 16+
- BSC CLI
- Metaplex CLI

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/XAIAI.git
   cd XAIAI
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the backend directory.
   - Add the following keys:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     BSC_PRIVATE_KEY=your_BSC_wallet_private_key
     ```

4. Run the Flask backend:
   ```bash
   python scripts/generateImage.py
   python scripts/transcribeAudio.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React app:
   ```bash
   npm start
   ```

### Smart Contracts

1. Deploy the `imageNFT` smart contract using your preferred idity toolchain.
2. Ensure the BSC wallet is funded with  for transaction fees.

---

## Usage

### 1. Generate Images
- Navigate to the Image Generator in the frontend.
- Enter a text prompt and generate an image.

### 2. Transcribe Audio
- Upload an audio file through the frontend.
- View the transcribed text in real time.

### 3. Create NFTs
- Use the NFT creation feature to mint AI-generated images on the BSC blockchain.

---

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for review.

---

## Acknowledgments

- OpenAI for their DALL-E and Whisper APIs.
- BSC blockchain for seamless NFT integration.
- The open-source community for providing excellent resources and tools.
