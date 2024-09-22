const { Connection, Keypair, LAMPORTS_PER_SOL, clusterApiUrl, PublicKey } = require('@solana/web3.js');

// Set up connection to the Solana devnet (can also switch to mainnet or testnet)
const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');

// Generate a new wallet (Keypair)
function createWallet() {
    const wallet = Keypair.generate();
    console.log('Wallet Created!');
    console.log('Public Key:', wallet.publicKey.toBase58());
    console.log('Secret Key:', wallet.secretKey);
    return wallet;
}

// Check balance of a wallet
async function checkBalance(publicKey) {
    try {
        const balance = await connection.getBalance(new PublicKey(publicKey));
        console.log(`Wallet Balance: ${balance / LAMPORTS_PER_SOL} SOL`);
    } catch (error) {
        console.error('Error fetching balance:', error);
    }
}

// Airdrop SOL to a wallet on devnet (useful for testing)
async function airdropSol(publicKey, amount = 1) {
    try {
        const airdropSignature = await connection.requestAirdrop(
            new PublicKey(publicKey),
            amount * LAMPORTS_PER_SOL
        );
        console.log(`Airdropped ${amount} SOL to wallet...`);
        await connection.confirmTransaction(airdropSignature);
    } catch (error) {
        console.error('Error airdropping SOL:', error);
    }
}

// Send SOL from one wallet to another
async function sendSol(senderWallet, recipientPublicKey, amount) {
    try {
        const transaction = await connection.requestAirdrop(
            new PublicKey(recipientPublicKey),
            amount * LAMPORTS_PER_SOL
        );
        const signature = await connection.sendTransaction(transaction, [senderWallet]);
        await connection.confirmTransaction(signature);
        console.log(`Successfully sent ${amount} SOL from ${senderWallet.publicKey.toBase58()} to ${recipientPublicKey}`);
    } catch (error) {
        console.error('Error sending SOL:', error);
    }
}

// Example usage

async function runExample() {
    // Create wallet and check balance
    const senderWallet = createWallet();
    await checkBalance(senderWallet.publicKey);

    // Airdrop 1 SOL to the wallet
    await airdropSol(senderWallet.publicKey, 1);

    // Check balance again
    await checkBalance(senderWallet.publicKey);

    // Create another wallet to send SOL to
    const recipientWallet = Keypair.generate();
    console.log('Recipient Wallet Public Key:', recipientWallet.publicKey.toBase58());

    // Send 0.1 SOL to the recipient
    await sendSol(senderWallet, recipientWallet.publicKey.toBase58(), 0.1);

    // Check balances of both wallets
    await checkBalance(senderWallet.publicKey);
    await checkBalance(recipientWallet.publicKey.toBase58());
}

runExample();
console.log("Solana Wallet Integration")
