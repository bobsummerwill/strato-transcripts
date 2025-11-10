#!/usr/bin/env python3
"""
Extract technical terms from Ethereum documentation and articles
Creates a comprehensive list of blockchain/Ethereum terminology
"""

import re
from pathlib import Path
from collections import Counter

def extract_from_early_days_articles():
    """Extract technical terms from EarlyDaysOfEthereum articles"""
    articles_dir = Path("../EarlyDaysOfEthereum/source/_articles")
    
    if not articles_dir.exists():
        print(f"Warning: {articles_dir} not found")
        return []
    
    # Common Ethereum/blockchain technical terms pattern
    # Look for capitalized technical terms and common patterns
    terms = []
    
    # Known technical term patterns
    patterns = [
        r'\bEthereum\b',
        r'\bERC-\d+\b',
        r'\bEIP-\d+\b',
        r'\b(?:smart|Smart)\s+(?:contract|Contract)s?\b',
        r'\b(?:decentralized|Decentralized)\s+(?:application|Application)s?\b',
        r'\bdApps?\b',
        r'\bDeFi\b',
        r'\bNFTs?\b',
        r'\bWeb3\b',
        r'\bSolidity\b',
        r'\b(?:gas|Gas)\s+(?:fee|Fee)s?\b',
        r'\b(?:proof|Proof)\s+of\s+(?:stake|Stake|work|Work)\b',
        r'\bPoS\b',
        r'\bPoW\b',
        r'\b(?:consensus|Consensus)\s+(?:mechanism|algorithm)\b',
        r'\b(?:ethereum|Ethereum)\s+(?:virtual|Virtual)\s+(?:machine|Machine)\b',
        r'\bEVM\b',
        r'\b(?:layer|Layer)\s+(?:1|2|one|two)\b',
        r'\b(?:rollup|Rollup)s?\b',
        r'\b(?:shard|Shard)(?:ing)?\b',
        r'\b(?:validator|Validator)s?\b',
        r'\b(?:staking|Staking)\b',
        r'\b(?:blockchain|Blockchain)\b',
        r'\b(?:cryptocurrency|Cryptocurrency)\b',
        r'\b(?:token|Token)s?\b',
        r'\b(?:wallet|Wallet)s?\b',
        r'\b(?:mining|Mining)\b',
        r'\b(?:miner|Miner)s?\b',
    ]
    
    for md_file in articles_dir.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                for pattern in patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    terms.extend([m.lower() for m in matches])
        except Exception as e:
            print(f"Warning: Could not parse {md_file}: {e}")
    
    # Count and return frequent terms
    term_counts = Counter(terms)
    return list(term_counts.keys())

def get_common_ethereum_terms():
    """Return hardcoded list of common Ethereum terms"""
    return [
        # Core concepts
        "Ethereum",
        "blockchain",
        "smart contract",
        "smart contracts",
        "decentralized",
        "decentralization",
        "cryptocurrency",
        "crypto",
        
        # Token standards
        "ERC-20",
        "ERC-721",
        "ERC-1155",
        "NFT",
        "NFTs",
        "non-fungible token",
        "fungible token",
        "token",
        "tokens",
        
        # DeFi
        "DeFi",
        "decentralized finance",
        "liquidity",
        "liquidity pool",
        "liquidity pools",
        "yield farming",
        "staking",
        "lending",
        "borrowing",
        "AMM",
        "automated market maker",
        "swap",
        "swaps",
        
        # Technical
        "Solidity",
        "Vyper",
        "Web3",
        "web3",
        "dApp",
        "dApps",
        "decentralized application",
        "decentralized applications",
        "Ethereum Virtual Machine",
        "EVM",
        "bytecode",
        "gas",
        "gas fee",
        "gas fees",
        "gas limit",
        "gas price",
        "gwei",
        "wei",
        "ether",
        "ETH",
        
        # Consensus
        "proof of stake",
        "proof of work",
        "PoS",
        "PoW",
        "consensus",
        "consensus mechanism",
        "validator",
        "validators",
        "mining",
        "miner",
        "miners",
        "block",
        "blocks",
        "block production",
        "block proposer",
        "attestation",
        "attestations",
        
        # Scaling
        "layer 1",
        "layer 2",
        "L1",
        "L2",
        "rollup",
        "rollups",
        "optimistic rollup",
        "zero-knowledge rollup",
        "zk-rollup",
        "zkSync",
        "Optimism",
        "Arbitrum",
        "sidechain",
        "sidechains",
        "sharding",
        "shard",
        "shards",
        "state channel",
        "state channels",
        "plasma",
        
        # Wallets & Security
        "wallet",
        "wallets",
        "MetaMask",
        "hardware wallet",
        "cold storage",
        "hot wallet",
        "private key",
        "public key",
        "seed phrase",
        "mnemonic",
        "multisig",
        "multi-signature",
        
        # Governance
        "DAO",
        "decentralized autonomous organization",
        "governance",
        "voting",
        "proposal",
        "proposals",
        
        # Network
        "mainnet",
        "testnet",
        "Goerli",
        "Sepolia",
        "Rinkeby",
        "Ropsten",
        "node",
        "nodes",
        "client",
        "clients",
        "Geth",
        "Prysm",
        "Lighthouse",
        "Nethermind",
        "Besu",
        
        # Standards & Protocols
        "EIP",
        "Ethereum Improvement Proposal",
        "ERC",
        "Ethereum Request for Comment",
        "JSON-RPC",
        "ABI",
        "Application Binary Interface",
        
        # Organizations
        "Ethereum Foundation",
        "ConsenSys",
        "Parity",
        "Parity Technologies",
        "OpenEthereum",
        
        # Merge & Upgrades
        "The Merge",
        "Beacon Chain",
        "execution layer",
        "consensus layer",
        "Shanghai upgrade",
        "Shapella",
        "Dencun",
        "proto-danksharding",
        
        # Development
        "Truffle",
        "Hardhat",
        "Remix",
        "Foundry",
        "Brownie",
        "OpenZeppelin",
        "Chainlink",
        "oracle",
        "oracles",
        "subgraph",
        "The Graph",
        "IPFS",
        "ENS",
        "Ethereum Name Service",
    ]

def main():
    print("="*60)
    print("Ethereum Technical Terms Extractor")
    print("="*60)
    
    # Extract from articles
    print("\n1. Extracting from articles...")
    article_terms = extract_from_early_days_articles()
    print(f"   Found {len(article_terms)} terms from articles")
    
    # Get common terms
    print("\n2. Adding common Ethereum terms...")
    common_terms = get_common_ethereum_terms()
    print(f"   Added {len(common_terms)} known terms")
    
    # Combine and deduplicate (case-insensitive)
    all_terms_lower = {}
    for term in article_terms + common_terms:
        term_lower = term.lower()
        if term_lower not in all_terms_lower:
            all_terms_lower[term_lower] = term
    
    # Sort alphabetically
    sorted_terms = sorted(all_terms_lower.values(), key=str.lower)
    
    # Save to file
    output_file = Path("intermediates/ethereum_technical_terms.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        for term in sorted_terms:
            f.write(f"{term}\n")
    
    print(f"\n✓ Saved {len(sorted_terms)} unique terms to {output_file}")
    
    # Show preview
    print("\nPreview (first 30 terms):")
    for term in sorted_terms[:30]:
        print(f"  - {term}")
    
    if len(sorted_terms) > 30:
        print(f"  ... and {len(sorted_terms) - 30} more")

if __name__ == "__main__":
    main()
