// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ImageNFT
 * @dev A smart contract for minting NFTs representing AI-generated images.
 */
contract ImageNFT is ERC721URIStorage, Ownable {
    uint256 private _tokenIds; // Counter for token IDs

    constructor() ERC721("AI Image NFT", "AII") {}

    /**
     * @notice Mint a new NFT.
     * @param recipient The address of the recipient who will own the minted NFT.
     * @param tokenURI The URI pointing to the metadata of the NFT (including the image URL).
     * @return The ID of the minted token.
     */
    function mintNFT(address recipient, string memory tokenURI)
        public
        onlyOwner
        returns (uint256)
    {
        _tokenIds += 1;
        uint256 newItemId = _tokenIds;

        // Mint the NFT
        _mint(recipient, newItemId);

        // Set the token URI (metadata URI)
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }
}
contract ImageNFT {}
