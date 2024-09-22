const fs = require('fs');
const path = require('path');
const { Connection, PublicKey, Keypair } = require('@solana/web3.js');
const { createMint, createAssociatedTokenAccount, mintTo, transfer } = require('@solana/spl-token');
const { TOKEN_PROGRAM_ID } = require('@solana/spl-token');
const { Metadata, CreateMetadataV2 } = require('@metaplex/js'); // Metaplex for NFT metadata

// Set up connection to Solana devnet
const connection = new Connection('https://api.devnet.solana.com', 'confirmed');

// Load wallet (replace with your actual private key or use environment variables)
const wallet = Keypair.fromSecretKey(Uint8Array.from([/* Your private key array here */]));

// Function to create and mint NFT
async function createNFT(imageUrl, name, symbol, uri) {
    try {
        // 1. Create the mint address for the token (NFT)
        const mint = await createMint(connection, wallet, wallet.publicKey, null, 0);

        // 2. Create an associated token account for the wallet
        const associatedTokenAccount = await createAssociatedTokenAccount(connection, wallet, mint, wallet.publicKey);

        // 3. Mint the token (NFT) to the associated account
        await mintTo(connection, wallet, mint, associatedTokenAccount, wallet.publicKey, 1);

        // 4. Create NFT metadata using Metaplex (store image URL, name, symbol, etc.)
        const metadata = await createMetadata({
            connection,
            wallet,
            mint,
            name,
            symbol,
            uri,
        });

        console.log('NFT Minted Successfully!');
        console.log('Metadata:', metadata);
        console.log('Mint Address:', mint.toBase58());
        console.log('Associated Token Account:', associatedTokenAccount.toBase58());

    } catch (error) {
        console.error('Error creating NFT:', error);
    }
}

// Function to create metadata for the NFT
async function createMetadata({ connection, wallet, mint, name, symbol, uri }) {
    // Create metadata instruction using Metaplex
    const metadataPDA = await Metadata.getPDA(mint);
    const metadataData = {
        name: name,
        symbol: symbol,
        uri: uri,
        sellerFeeBasisPoints: 500, // 5% seller fee for future sales
        creators: null,
    };

    const metadataTx = new CreateMetadataV2({
        metadata: metadataPDA,
        mint: mint,
        mintAuthority: wallet.publicKey,
        payer: wallet.publicKey,
        updateAuthority: wallet.publicKey,
        data: metadataData,
    });

    // Send the transaction
    await metadataTx.send(connection, wallet);

    return metadataData;
}

// Example Usage
const imageUrl = 'https://example.com/your-ai-generated-image.png'; // Replace with your AI-generated image URL
const nftName = 'AI Generated Artwork';
const nftSymbol = 'AIART';
const nftUri = 'https://example.com/nft-metadata'; // A URL pointing to the metadata of the NFT (e.g., a JSON file with description, attributes)

createNFT(imageUrl, nftName, nftSymbol, nftUri);

