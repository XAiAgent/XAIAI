# AetherAI: AI-Powered NFT Creation Platform

AetherAI is a cutting-edge platform that combines artificial intelligence (AI) with blockchain technology to create autonomous NFT generation workflows. This project leverages Hermes for prompt enhancement, Flux/Ideogram for ultra HD image generation, Claude for storytelling, Solana for NFT minting, and includes a Telegram bot for seamless interaction.

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

### **5. Killer Features (New)**

#### **Hermes-Powered Intelligent Prompt Engineer**
- User simple prompt → Hermes better prompt → Flux/Ideogram ultra HD image generate.

#### **Claude Storyteller Agent**
- Image → full lore, Twitter thread, description auto-generated.

#### **Autonomous Solana NFT Minter**
- Image + metadata → Arweave upload → Solana NFT mint (using Metaplex Core) → Collection created.

#### **Voice-to-NFT (Enhanced)**
- Audio upload → Hermes transcribe + summarize → Claude story → Image generate → NFT.

#### **On-Chain AI Memory**
- User's past creations stored on-chain (or Vector DB + Supabase).

#### **Telegram Autonomous Bot**
- `/create cyberpunk cat` → entire flow executes automatically.

---

## Project Structure

```
AetherAI/
├── backend/
│   ├── ai/
│   │   ├── imageGeneration.py
│   │   └── voiceProcessing.py
│   ├── solana/
│   │   ├── createNFT.js
│   │   └── solanaWallet.js
│   └── services/
│       ├── hermes_prompt_engineer.py
│       ├── claude_storyteller.py
│       ├── solana_nft_minter.py
│       ├── voice_to_nft.py
│       ├── on_chain_memory.py
│       └── telegram_bot.py
├── contracts/
│   └── imageNFT.sol
├── frontend/
│   └── src/
│       └── components/
│           ├── ImageGenerator.js
│           └── VoiceAssistant.js
├── scripts/
│   ├── generateImage.py
│   └── transcribeAudio.py
├── requirements.txt
└── README.md
```

---

## Installation

### Prerequisites

- Python 3.9+
- Node.js 16+
- BSC CLI
- Metaplex CLI
- Solana CLI
- Arweave wallet key
- Telegram Bot Token
- Supabase account (for vector DB) or Solana devnet for on-chain storage

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/XAiAgent/AetherAI.git
   cd AetherAI
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
     SOLANA_PRIVATE_KEY=your_solana_wallet_private_key
     ARWEAVE_KEY=your_arweave_key.json
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     SUPABASE_URL=your_supabase_url
     SUPABASE_KEY=your_supabase_key
     HERMES_API_KEY=your_hermes_api_key  # For prompt enhancement
     CLAUDE_API_KEY=your_claude_api_key   # For story generation
     FLUX_API_KEY=your_flux_api_key       # For ultra HD image generation
     IDEOGRAM_API_KEY=your_ideogram_api_key # Alternative to Flux
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

1. Deploy the `imageNFT` smart contract using your preferred Solidity toolchain.
2. Ensure the BSC wallet is funded with BNB for transaction fees.

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

### 4. Killer Features Usage

#### Hermes-Powered Intelligent Prompt Engineer
- Access via `/api/hermes/enhance-prompt` endpoint with a simple prompt.
- Returns an enhanced prompt for ultra HD image generation.

#### Claude Storyteller Agent
- Access via `/api/claude/generate-story` with an image URL.
- Returns lore, Twitter thread, and description.

#### Autonomous Solana NFT Minter
- Access via `/api/solana/mint-nft` with image URL, metadata, and collection details.
- Mints NFT on Solana using Metaplex and stores metadata on Arweave.

#### Voice-to-NFT
- Access via `/api/voice/to-nft` with an audio file.
- Returns the minted NFT details after processing through the pipeline.

#### On-Chain AI Memory
- Access via `/api/memory/store` to save a creation.
- Access via `/api/memory/retrieve` to get past creations.

#### Telegram Autonomous Bot
- Talk to your Telegram bot and send `/create cyberpunk cat` (or any description).
- The bot will execute the full flow and return the NFT.

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
- Solana and Metaplex for NFT minting capabilities.
- Arweave for permanent storage.
- Supabase for vector database and backend services.
- Telegram for bot API.
- The open-source community for providing excellent resources and tools.

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
    git clone https://github.com/your-repo/AetherAI.git
    cd AetherAI
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
