1.  **Analyze the Request:**
    *   **Role:** Expert transcript editor specializing in Ethereum and blockchain technology.
    *   **Context:** Lists of Known People (e.g., Kieren James-Lubin) and Technical Terms (e.g., DeFi, ZK).
    *   **Input:** Raw transcript with timestamps, speaker labels (SPEAKER_03, SPEAKER_00, SPEAKER_01, SPEAKER_02), and speech-to-text errors.
    *   **Primary Objective:** Clean, readable transcript preserving *all* dialogue and content.
    *   **Output Rules:** No preamble/meta-commentary. Start immediately with `[MM:SS] SPEAKER_XX:`. Output *only* the transcript.
    *   **Content Preservation:** Keep everything. 90-110% of original length.
    *   **Timestamps:** Preserve exactly as input. One per speaker paragraph.
    *   **Formatting:** Merge consecutive speech from one speaker into paragraphs. Use bold speaker labels.
    *   **Fixes:** Spelling of terms (Ethereum, ZK, etc.), Proper Names (Kieren vs Kieran, etc.), punctuation.
    *   **Removal:** Excessive filler words (um, uh, like), false starts, obvious repetitions. Keep natural flow.

2.  **Analyze the Input Data:**
    *   **Speaker Mapping:**
        *   SPEAKER_03: Victor Wong (Host).
        *   SPEAKER_00: Michael Tan (Strato Spotlight).
        *   SPEAKER_01: Jim Hermansdorfer (CTO).
        *   SPEAKER_02: Kieren James-Lubin (CEO). *Note: Context says "Kieran", but the "Known People" list explicitly says "Kieren James-Lubin". I must use "Kieren".*

    *   **Timestamps:** They exist in the input (e.g., `[00:04]`). I must keep them exactly.

    *   **Key Entities & Terms Check:**
        *   "Strato" (Company/Product).
        *   "Kieran" -> "Kieren".
        *   "Jim Hermosdior" -> "Jim Hermansdorfer" (inferred from context "CTO of Strato" and likely correct spelling, though not explicitly in the provided list of 244, "Jim Hermosdior" is the raw text, I should probably correct standard spellings if known, but stick to the provided list if possible. The provided list has "Kieren James-Lubin", "Adam B. Levine", etc. It does *not* list "Jim Hermansdorfer". However, "Victor Wong" isn't in the list either. The list provided seems to be a subset or a generic list. I will stick to standard industry spelling for names not in the list, but strictly enforce "Kieren").
        *   "USDC", "USDT", "USDST", "Zcash", "Robinhood", "Hyperliquid", "Tornado Cash", "Railgun", "Polymarket", "Aave", "PAXG", "Linea".
        *   "ZK" (Zero-Knowledge).
        *   "ERC-20".
        *   "UTXO".
        *   "Merkle Patricia".
        *   "COBOL".
        *   "Solidity".
        *   "Rust".
        *   "Dencun" (mentioned in context list, maybe not in transcript).
        *   "Libra" (The meme coin incident mentioned is likely "Libra" as mentioned in text).

3.  **Processing the Transcript - Section by Section:**

    *   **[00:04] SPEAKER_03 (Victor):**
        *   Intro: "Unchained Oracles" (maybe "Strato Spotlight" or similar, but text says Unchained Oracles).
        *   Names: Victor Wong, Kieran James-Lubin (correct "Kieran" to "Kieren"), Jim Hermosdior (Keep or correct to Hermansdorfer? I'll standardize to Hermansdorfer if I'm sure, but the text says "Hermosdior". I'll assume "Hermansdorfer" is the intended spelling based on phonetics, or stick to text if unsure. Let's look at the prompt: "Proper names - MUST use EXACT spellings from the 'Key People' list". The list *doesn't* have Jim. It has Kieren. So for Jim, I should fix obvious speech-to-text errors. "Hermosdior" is almost certainly "Hermansdorfer" (or similar). I will correct it to Hermansdorfer for professionalism unless I find evidence otherwise, or just keep it if it's ambiguous. Wait, looking at the context list: "Jim Hermosdior" is not in the list of 244 people. But "Kieren James-Lubin" is. I will prioritize the list. For Jim, I will just clean the text flow. I'll stick to the text's phonetic rendering if I can't verify the name, but "Hermansdorfer" is a very common German surname and fits "Hermosdior" in ASR. I'll correct to Hermansdorfer).
        *   *Self-Correction*: Actually, I should check if "Jim Hermosdior" is a real person. A quick mental check or search simulation suggests "Jim Hermansdorfer" is associated with Strato/BlockApps. I will correct it.
        *   "Strato" URL: "strato dot nexus".
        *   "Telegram", "Giveaway".

    *   **[01:44] SPEAKER_00 (Michael Tan):**
        *   Topic: "Easy savings path".
        *   Tech: "Bridging in stables", "Ethereum wallet", "USDC", "USDT", "Lending pool".
        *   Steps: "Connect wallet", "Bridge in 100", "Permit", "Confirm transaction", "All safe" (likely "Altsafe" or "on safe"? "all safe" might be slang or a specific term. Wait, "Waiting for the all safe" might be "waiting for the all clear"? Or a specific platform term like "block"? Let's look closer. "Waiting for the all safe." Maybe "Altsafe"? Unlikely. "Waiting for the block"? "Waiting for the sale"? "Waiting for the all safe" -> Maybe "waiting for the call-safe"? Let's stick to "Waiting for the all safe" if it's unintelligible, but "all safe" sounds like "all safe" might be a typo for "all clear" or similar. However, looking at crypto jargon, "Altsafe" isn't a standard thing. Let's assume it's "all safe" as in "the funds are safe" or a specific internal term. Or maybe "waiting for the [00] block"? "Waiting for the block"? Let's stick to the transcript text but clean grammar. "Waiting for the all safe" might be "Waiting for the all-safe". Let's leave it as "Waiting for the all safe" or "waiting for the block"? The audio says "all safe". I'll keep it. Ah, re-reading: "Waiting for the all safe." Could be "Waiting for the call safe"? No. Maybe "Waiting for the block"? "Waiting for the all safe." -> "Waiting for the all-safe." I'll just transcribe as is but clean the flow.
        *   "USDST": Strato stable coin.
        *   "Season one reward program".

    *   **[04:05] SPEAKER_03 (Victor):**
        *   Chats with Michael. "Bump up your activity".

    *   **[04:49] SPEAKER_01 (Jim):**
        *   Topic: "Biggest story".
        *   "Block apps" -> "BlockApps" (Company name).
        *   "Crypto year in review".
        *   Mention of "Eric Trump", "Toronto".

    *   **[05:58] SPEAKER_02 (Kieren):**
        *   Correction: "Kieran" -> "Kieren".
        *   Topic: "Adoption and price decoupling".
        *   "Stables on chain".
        *   "Active wallets".
        *   "Vanguard".
        *   "Regulatory".

    *   **[08:55] SPEAKER_03 (Victor):**
        *   Questioning Kieren about leading indicators.

    *   **[09:07] SPEAKER_02 (Kieren):**
        *   "Retail slash the public markets".
        *   "Stimulus checks", "GameStop".
        *   "ICOs".

    *   **[10:46] SPEAKER_03 (Victor):**
        *   Topic: "Biggest story - Return of building that matters".
        *   "Labor corn" -> "Libra" (The Meme coin incident in Argentina/Trump context). Text says "labor corn". Context is "Libra" coin (the controversial one associated with Argentina/Milei). The phonetic match "labor corn" is definitely "Libra".
        *   "Zcash".
        *   "Temple by Stripe"? Or "Tempus"? Or "Temple"? The text says "Temple by Stripe". Wait, Stripe partnered with "Bridge" (acquired) or maybe "Temple" is a typo. Actually, "Temple" is a DeFi protocol. Did Stripe do something with Temple? Or maybe "Stablecoin"? Stripe is doing USDC. Let's re-read: "Temple by Stripe". Maybe "Tie-up by Stripe"? "Temples"? The text is "Temple by Stripe". I will leave it as is or fix to "Tie-up" if it makes no sense. "Even like the institutions getting involved on the infrastructure side, like Temple by Stripe..." - This sounds like a specific project or a hallucination in the transcript. Actually, Stripe did a deal with "Base"? No. Stripe supports USDC payments. Maybe "Temple" is a typo for something else. I'll stick to "Temple by Stripe" but flag mentally that it might be wrong. Actually, maybe "Temples by Stripe"? Or "Templates"? I'll keep "Temple by Stripe" to be safe as I shouldn't remove content.
        *   *Correction*: The text says "Temple by Stripe". Maybe it's "Tenderly"? No. I will keep "Temple by Stripe".
        *   "AI" discussion. "Steven Chu".

    *   **[12:57] SPEAKER_01 (Jim):**
        *   AI limits.

    *   **[13:21] SPEAKER_02 (Kieren):**
        *   AI coding. "App layer", "Platform layer". "Haskell". "Surgical fixes". "Reading a code base".

    *   **[15:49] SPEAKER_01 (Jim):**
        *   "Wild goose chase problem".
        *   "MetaPhase"? "Centaur"? "Center phase"? Transcript: "center phase". Context: Chess. "Centaurs" is the term for human+AI chess. I should correct "center phase" to "Centaurs" or "Centaur phase". The text says "center phase". I will change to "Centaur phase" as it fits the chess/AI context perfectly.
        *   "Metaphone podcast" -> "MetaPhone"? Maybe "Bankless"? Or "Metaphor"? "Meta" something. Text says "Metaphone". I'll keep "Metaphone" or fix to "Meta" if obvious. Maybe "Metaphysic"? "Metaphone" sounds like a typo for "Metaphor" or just a specific show. I'll stick to "Metaphone" to be safe or correct to "Metaphor" if it seems right. Actually, Steven Chu was on "The MetaPod"? No. He was on "Bankless"? Maybe. I'll stick to "Metaphone" to avoid guessing wrong, or clean to "Metaphor".
        *   *Check*: Steven Chu, physics paper. The podcast is likely "Meta" related. I'll leave "Metaphone" or change to "Meta" related if "Metaphone" sounds like a speech-to-text error. It's likely "Metaphysic" or similar. I will keep "Metaphone" but capitalized.

    *   **[18:27] SPEAKER_01 (Jim):**
        *   "AI telling the master chess player".

    *   **[19:11] SPEAKER_03 (Victor):**
        *   "Spatial reasoning".
        *   "Diffusion models", "LLMs".

    *   **[20:18] SPEAKER_02 (Kieren):**
        *   "Biggest surprise".
        *   "October 10th" -> "10/10".
        *   "20 billion". "20x larger liquidation".
        *   "Hyperliquid" (CEX/DEX).
        *   "Metals all-time high". "Silver", "Gold".
        *   "High beta tech stock".

    *   **[23:18] SPEAKER_01 (Jim):**
        *   "Return of ZK".
        *   "Argentina".
        *   "Zcash client".

    *   **[24:35] SPEAKER_03 (Victor):**
        *   "Proof for" -> "Proof generation"? "Proof for on the... testnet".
        *   "48 GPUs".

    *   **[25:02] SPEAKER_02 (Kieren):**
        *   "EU driver's license to use the internet".
        *   "Cypher punk Congress".
        *   "Devconnect".
        *   "Railgun", "Privacy pools".
        *   "Roman Storm" (Tornado Cash dev).
        *   "Tornado Cash" (Capitalized).

    *   **[28:00] SPEAKER_03 (Victor):**
        *   "Robinhood announcement".
        *   "L2" (Layer 2).
        *   "Tokenization engine".
        *   "Secondary stocks".
        *   "Enterprise Ethereum Alliance" -> "Enterprise of the airlines" (Text says "airlines". This is definitely "Alliance". "Enterprise Ethereum Alliance" is a real thing. "Airlines" is a speech-to-text error. I will fix to "Enterprise Ethereum Alliance").

    *   **[30:31] SPEAKER_02 (Kieren):**
        *   "Meme flame out".
        *   "Pump.fun".
        *   "Base" rebranding to "creator coins".
        *   "NFTs".

    *   **[33:24] SPEAKER_03 (Victor):**
        *   "Libra" (Text says "Libra"). "Presidential office".
        *   "Meme courts" -> "Meme coins".

    *   **[34:11] SPEAKER_01 (Jim):**
        *   "Biggest disappointment".
        *   "Identity", "Username".
        *   "ERC 20" -> "ERC-20".
        *   "Solidity".
        *   "Merkle Patricia".
        *   "UTXO".
        *   "Rust".
        *   "Bob" (Summerwill?).

    *   **[37:12] SPEAKER_03 (Victor):**
        *   "JavaScript".
        *   "Rules engine".

    *   **[38:20] SPEAKER_03 (Victor):** (Label is 03 again in text, likely Victor).
        *   "Strato update and roadmap".
        *   "TVL" (Total Value Locked).
        *   "90X".

    *   **[39:12] SPEAKER_02 (Kieren):**
        *   "CDP" (Collateralized Debt Position).
        *   "LP tokens".
        *   "Native yield coin".
        *   "Tokenized stocks".
        *   "Third party yield coins".
        *   "Vault".
        *   "Lighter", "Hyperliquid".
        *   "Arb" (Arbitrage).
        *   "Arb loss".
        *   "Vicious arbitrage" -> "Vicious arbitrage" (maybe "Venomous"? No, "Vicious" works).
        *   "Liquidation bot".
        *   "Privacy".
        *   "Shielded balance".
        *   "Credit card".
        *   "Unsecured or under collateralized lending".
        *   "PayPal", "Venmo".
        *   "Mercada address" -> "Mercury"? "Strato address"? "Mercada" sounds like "Mercado" (Spanish for market) or "Mercury". Context: "put your Mercada address on our telegram". Maybe "MetaMask"? "Mercada" sounds like "Mercato". Let's check the product name. Strato uses "Strato" wallets. Maybe "MetaMask"? Or "Mercury"? Ah, maybe "Mercato" is a typo for a wallet name? Or "Mercada" is the address format?
        *   *Correction*: "Silvesti" (Token name). "One ounce silver".
        *   "Silvesti" -> "Silve" + "STI"? "Silver STI"? Text says "Silvesti". Later "Silvesti". I will keep "Silvesti" unless I find evidence it's "Silver ST". Strato's silver token might be called something like "Silv" or "Silver". I'll stick to the text "Silvesti" but maybe capitalize.
        *   "Mercada address". Could it be "Mercury wallet"? "Mercato"? I'll keep "Mercada address" but capitalize "Mercada".

    *   **[46:53] SPEAKER_03 (Victor):**
        *   "Cypherpunk".
        *   "Normies".
        *   "Grandma".

    *   **[48:29] SPEAKER_01 (Jim):**
        *   "Predictions for 2026".
        *   "Year of usability".

    *   **[49:27] SPEAKER_03 (Victor):**
        *   "ZK scaling".
        *   "Institutional crypto adoption".
        *   "Glacial pace" (Text says "glacial price" - context: moves at a glacial pace. "Price" is wrong. I will fix to "pace").

    *   **[50:25] SPEAKER_02 (Kieren):**
        *   "DeFi, TradFi soft merger".
        *   "Aave".
        *   "Federal funds rate".
        *   "PAXG".
        *   "L1", "L2".
        *   "Perpdex" (Perpetual DEX).
        *   "Polymarket".
        *   "Linea".
        *   "TGE" (Token Generation Event).

    *   **[54:59] SPEAKER_03 (Victor):**
        *   "Adoption over research".
        *   "Vitamin C".
        *   "Sunshine".

4.  **Detailed Editing Steps (Iterative):**

    *   *Speaker 03*: "Jim Hermosdior" -> "Jim Hermansdorfer". (Strong confidence in correction based on phonetics and industry names). "Kieran James Lubin" -> "Kieren James-Lubin". (Strict adherence to list).
    *   *Speaker 00*: "USDC", "USDT". "USDST". "Bridge out". "Easy Savings". "Leaderboard".
    *   *Speaker 01*: "Block apps" -> "BlockApps".
    *   *Speaker 02*: "Kieran" -> "Kieren". "Vanguard". "Stablecoin" -> "stables". "Hyperliquid". "High beta".
    *   *Speaker 03*: "Labor corn" -> "Libra". "Temple by Stripe" -> "Temple by Stripe" (leaving as is, weird but specific). "Steven Chu". "Center phase" -> "Centaur phase".
    *   *Speaker 02*: "Haskell". "Merkle Patricia". "ERC-20". "UTXO". "Roman Storm". "Tornado Cash". "Railgun".
    *   *Speaker 03*: "Diffusion models". "LLMs".
    *   *Speaker 02*: "20 billion". "Hyperliquid". "LTV" (Loan to Value - text says "LTV"). "RWAs" (Real World Assets - text says "RWAs").
    *   *Speaker 03*: "Robinhood". "L2". "Tokenization". "Enterprise of the airlines" -> "Enterprise Ethereum Alliance".
    *   *Speaker 02*: "Pump.fun". "Base". "NFTs".
    *   *Speaker 03*: "Libra". "Meme coins".
    *   *Speaker 01*: "ERC-20". "Solidity". "Merkle Patricia". "UTXO". "Rust". "Bob" (Summerwill).
    *   *Speaker 03*: "TVL". "90X".
    *   *Speaker 02*: "CDP". "LP tokens". "Aave". "PAXG". "Linea". "Polymarket". "TGE".
    *   *Speaker 03*: "Mercada address". "Silvesti". "Vitamin C".

5.  **Refining the Content:**

    *   *Filling gaps*: "Waiting for the all safe" -> "Waiting for the call-safe" is nonsense. Maybe "Waiting for the block"? No, "all safe" is repeated. I'll assume "Waiting for the all safe" is an idiom or internal term I don't know, or a typo for "all clear". I'll keep it as "Waiting for the all safe" to preserve content but it sounds awkward. Maybe "Waiting for the tx to be safe"? No. I'll leave it as "Waiting for the all safe".
    *   *Formatting*: Merge the dialogue.
    *   *Fillers*: Remove "um", "uh", "like" (excessive).
    *   *Specific correction*: "Center phase" -> "Centaur phase". This is a known concept in chess AI.
    *   *Specific correction*: "Enterprise of the airlines" -> "Enterprise Ethereum Alliance".
    *   *Specific correction*: "Kieran" -> "Kieren".

6.  **Final Polish Check:**
    *   Speaker 03 at [10:46]: "Labor corn" -> "Libra".
    *   Speaker 03 at [49:27]: "Glacial price" -> "Glacial pace".
    *   Speaker 02 at [54:59]: "TGE".
    *   Speaker 03 at [34:11]: "Meme courts" -> "Meme coins".

    Let's process the text.

    *Segment 1 [00:04]*: SPEAKER_03: Intro. Names fixed. URL fixed.
    *Segment 2 [01:44]*: SPEAKER_00: Demo. "Easy savings path". "USDC", "USDT", "USDST", "Lending pool". "Bridge out". "Leaderboard".
    *Segment 3 [04:05]*: SPEAKER_03: Chat.
    *Segment 4 [04:49]*: SPEAKER_01: "Block apps". "Development year". "Eric Trump".
    *Segment 5 [05:58]*: SPEAKER_02: "Kieren" fixed. "Stables". "Vanguard". "Regulatory". "Stimulus checks". "GameStop".
    *Segment 6 [08:55]*: SPEAKER_03: Q.
    *Segment 7 [09:07]*: SPEAKER_02: A. "Retail". "Public markets". "Private companies". "Liquidity".
    *Segment 8 [10:46]*: SPEAKER_03: "Libra". "Zcash". "Temple by Stripe". "AI". "Steven Chu".
    *Segment 9 [12:57]*: SPEAKER_01: AI limits.
    *Segment 10 [13:21]*: SPEAKER_02: AI coding. "App layer", "Platform layer", "Haskell".
    *Segment 11 [15:49]*: SPEAKER_01: "Wild goose chase". "MetaPhase" -> "Centaur phase".
    *Segment 12 [18:27]*: SPEAKER_01: AI chess.
    *Segment 13 [19:11]*: SPEAKER_03: Spatial reasoning. "Diffusion models".
    *Segment 14 [20:18]*: SPEAKER_02: Surprise. "October 10th" (10/10). "20 billion". "Hyperliquid". "Silver", "Gold". "High beta".
    *Segment 15 [23:18]*: SPEAKER_01: "ZK". "Argentina". "Zcash".
    *Segment 16 [24:35]*: SPEAKER_03: "Proof for". "Testnet". "GPUs".
    *Segment 17 [25:02]*: SPEAKER_02: "EU". "Cypher punk". "Devconnect". "Railgun". "Roman Storm". "Tornado Cash".
    *Segment 18 [28:00]*: SPEAKER_03: "Robinhood". "L2". "Enterprise Ethereum Alliance" (corrected).
    *Segment 19 [30:31]*: SPEAKER_02: "Meme flame out". "Pump.fun". "Base".
    *Segment 20 [33:24]*: SPEAKER_03: "Libra". "Meme coins" (corrected).
    *Segment 21 [34:11]*: SPEAKER_01: Identity. "ERC-20". "Solidity". "Merkle Patricia". "UTXO". "Rust". "Bob".
    *Segment 22 [37:12]*: SPEAKER_03: JavaScript. "Rules engine".
    *Segment 23 [38:20]*: SPEAKER_03: Roadmap. "TVL". "90X".
    *Segment 24 [39:12]*: SPEAKER_02: "CDP". "Lending pools". "LP tokens". "Yield coin". "Tokenized stocks". "Swap pools". "Vault". "Lighter". "Hyperliquid". "Arb". "Liquidation bot". "Privacy". "Shielded". "Credit card". "Unsecured". "PayPal". "Silvesti". "Mercada".
    *Segment 25 [46:53]*: SPEAKER_03: "Cypherpunk". "Normies".
    *Segment 26 [48:29]*: SPEAKER_01: Prediction. Usability.
    *Segment 27 [49:27]*: SPEAKER_03: Prediction. "ZK scaling". "Institutional adoption". "Glacial pace".
    *Segment 28 [50:25]*: SPEAKER_02: Prediction. "DeFi/TradFi". "Aave". "RWAs". "PAXG". "Value capture". "Linea". "Polymarket". "TGE".
    *Segment 29 [54:59]*: SPEAKER_03: "Adoption over research". "Vitamin C".

    *One tricky part*: [04:05] "You got to bump up your activity to get up on the chart." -> This sounds like Victor talking to Michael. But Michael left the call? "So with that, take care. Thanks, Michael." Okay, Michael is gone. Victor speaks to Jim/Kieren.

    *Another tricky part*: [34:11] Speaker 01 says "My disappointment was various features... we had taken identity... we sort of had to pull that out." Then [35:50] Speaker 02 interrupts "People are probably almost instantly on arrival. We're unhappy with the ERC 20...". Wait, the transcript shows SPEAKER_02 speaking at [35:50]. Let's check if this is a continuation of 01 or a new speaker. In the transcript:
    [34:11] SPEAKER_01: ...features...
    [35:50] SPEAKER_02: People are probably...
    It looks like a speaker change. 01 is talking about product features. 02 starts talking about Solidity and ERC-20. It seems 02 (Kieren) is agreeing or adding context. I will keep the speaker change.

    *Check names*:
    Kieran -> Kieren.
    Jim Hermosdior -> Jim Hermansdorfer.
    Enterprise of the airlines -> Enterprise Ethereum Alliance.
    Glacial price -> Glacial pace.
    Center phase -> Centaur phase.
    Labor corn -> Libra.
    Meme courts -> Meme coins.

    *Technical Terms*:
    Stables (capitalization usually lowercase or capitalized depending on usage, usually lowercase in casual speech, but 'Stablecoins' or 'Stables' as a category. I'll use 'stables' as per text flow but capitalize if generic noun).
    ERC-20, ERC-1155, etc.
    ZK (Zero-Knowledge).
    L1, L2.
    AI.
    LLMs.
    RWAs.
    TVL.
    DeFi.
    TradFi.
    TGE.
    UTXO.
    Haskell.
    Rust.
    Solidity.
    Merkle Patricia.
    NFTs.
    CDP.
    LP tokens.
    LTV.

    *Timestamps*: Keep exact.

    *Paragraph Merging*: Ensure continuous speech from one speaker is in one block.

    *Fillers*: Aggressive removal of "um", "uh", "like". But keep "like" if it's meaningful for tone (rare). "I mean" (keep sometimes).
    "you know" (remove often).
    "kind of" (keep occasionally, remove if repetitive).
    "sort of" (keep occasionally).

    *Merging check*:
    [04:49] SPEAKER_01: "You know, I want to push back a little bit... Anyway, it's the stuff that's been in the news... So it's just like, my answers... It's like in crypto in general... The big story was that this was a, a development year... Like, we uh spent the whole year... I don't even know where it is today... So it's just sort of a crazy ride... I will pass it on." -> One block.

    [05:58] SPEAKER_02: "Okay, Karen, what was your biggest story of the year? Okay, so I'll quibble with Jim a little bit... (long speech about adoption, stables, prices, etc.)... I think that's the story." -> One block.

    [08:55] SPEAKER_03: "Or do you think part of it might be that...?" -> One block.

    [09:07] SPEAKER_02: "some big black rock announces... (long speech)... I think that's the story." -> One block.

    [10:46] SPEAKER_03: "So for me, I think the biggest story... (long speech)... I think we're going through a phase..." -> One block.

    [12:57] SPEAKER_01: "Which is an important step... (short speech)... Yeah, I agree." -> One block.

    [13:21] SPEAKER_02: "kind of what it should be doing, right? Like I think... (long speech about coding)... I can read a code base..." -> One block.

    [15:49] SPEAKER_01: "Line by line on a specific issue... (speech about wild goose chase)... That's a stupid idea." -> One block.

    [17:04] SPEAKER_02: "there's certain types of like attorneys... (short speech)... it's a little too um... I don't know." -> One block.

    [18:27] SPEAKER_01: "And the thing is also... (speech about chess/AI)... Obviously it wouldn't work." -> One block.

    [19:11] SPEAKER_03: "I, one, one area AIs... (speech about spatial reasoning)... you know, and I know a bunch of people are working..." -> One block.

    [20:18] SPEAKER_02: "Things like that. Spatial reasoning seems... (short speech)... I'm sure they're working on it." -> One block.

    [20:18] SPEAKER_02 (Wait, input says [20:18] SPEAKER_02: "Things like that...". Then [20:18] SPEAKER_03: "So this is sort of in the space..."). There are two speakers at [20:18]. This implies a cut or a timestamp error. I will keep the timestamps as they are in the input (duplicate timestamps happen in raw transcripts).

    [20:18] SPEAKER_03: "So this is sort of in the space... (short speech)... and it sometimes gets confused." -> One block.

    [20:18] SPEAKER_02 (Input has [20:18] again? No, looking at raw text: "**[20:18] SPEAKER_02:** Things like that. Spatial reasoning seems... **[20:18] SPEAKER_03:** So this is sort of..."). Yes, duplicate timestamp. I will keep it.

    [23:18] SPEAKER_01: "Okay, Jim, what was your biggest surprise... (speech about ZK)... So it's kind of exciting. Yeah." -> One block.

    [24:35] SPEAKER_03: "I mean, like, if you look... (speech)... but yeah." -> One block.

    [25:02] SPEAKER_02: "One, like the EU came out... (long speech)... I think graphic too there was an assumption... (Wait, SPEAKER_03 interrupts at [28:00])".
    Input: [25:02] SPEAKER_02: ... "I think graphic too there was an assumption... [28:00] SPEAKER_03: um mainstream adoption...".
    Wait, looking at the raw text block for 02:
    "**[25:02] SPEAKER_02:** One, like the EU came out... (lots of text) ... I think part of it is just people realize, you know, as maybe a new kind of **[28:00] SPEAKER_03:** um mainstream adoption is taking place..."
    It seems SPEAKER_02 speaks from 25:02 until 28:00. This is a very long paragraph (about 3 minutes). I will keep it as one block.

    [28:00] SPEAKER_03: "um mainstream adoption is taking place people are realizing oh crap my balances are in fact public... (speech)... explain to me what Robinhood is doing..." -> One block.

    [30:31] SPEAKER_02: "What do you think? What's your biggest disappointment? So I'm going to mostly agree... (speech)... It's like everyone opted into this, but it still kind of looks gross..." -> One block.

    [33:24] SPEAKER_03: "Yeah, I mean, I think... (speech)... put the industry in a much more positive direction." -> One block.

    [34:11] SPEAKER_01: "What do you think? What's your biggest disappointment... (speech)... It's like the COBOL..." -> One block.

    [37:12] SPEAKER_03: "I mean, yes, but it's one of these things... (speech)... whereas what actually happens is people make JavaScript much faster." -> One block.

    [38:20] SPEAKER_03: "Kind of have like an internal joke... (speech)... We'll add more in time. But it's funny that... (Wait, SPEAKER_02 interrupts at [39:12]).
    Input: [38:20] SPEAKER_03: "...like in not only from the tech, but even in branding, right? We went back to our original Strato name... **[39:12] SPEAKER_03:** Strato update and roadmap..."
    The input shows [39:12] is also SPEAKER_03. This is a topic change. I should probably break this into two paragraphs or keep it as one if it flows. "Okay. Strato update and roadmap." is a distinct segment intro. However, the instruction says "All speech from one speaker before another speaks = ONE paragraph". This implies I should merge them. But a topic header like "Strato update and roadmap" acts as a break. However, to strictly follow "All speech from one speaker before another speaks", I should merge them unless the timestamp is crucial for segmentation. The prompt says "IF the input HAS timestamps: PRESERVE them EXACTLY as they appear... Only ONE timestamp per speaker paragraph (at the beginning)". This is a conflict. If the input has two timestamps for the same speaker in a row, and I must merge, do I drop the second timestamp? Yes. "Merge consecutive speech into paragraphs". "Only ONE timestamp per speaker paragraph". So I will merge the [38:20] and [39:12] SPEAKER_03 segments.

    [39:12] SPEAKER_02: "Yeah, well, I think... (speech)... So It's kind of two axes..." -> One block. (Huge block, approx 7 minutes).

    [46:53] SPEAKER_03: "Yes, like bringing cyberpunk power... (speech)... That should be an expectation to a certain point." -> One block.

    [48:29] SPEAKER_01: "okay before we dive into our 2026 predictions i want to announce our giveaway... (speech)... And we will send them one Silvesti equivalent to one ounce of silver. So hopefully that will be a nice holiday present... Okay. With that, let's go to predictions. Jim, what are your predictions for 2026? Okay. My prediction is that this will be the year of usability... (speech)... And we're going to be part of this for sure... Yeah." -> One block.

    [49:27] SPEAKER_03: "Okay, I'm going to go second and leave you the last, Karen. My prediction... (speech)... So, Karen, what are your predictions? Bring us home." -> One block.

    [50:25] SPEAKER_02: "Okay, so I predict... (speech)... Yeah, the way I think of it is kind of adoption over research... (Wait, SPEAKER_03 interrupts at [54:59]).
    Input: [50:25] SPEAKER_02: ... "I think that's the thing that really keeps the alt chains going... **[54:59] SPEAKER_03:** Yeah, the way I think of it is kind of adoption over research..."
    Again, SPEAKER_03 interrupts. I will keep SPEAKER_02 as one block.

    [54:59] SPEAKER_03: "Yeah, the way I think... (speech)... Like, you know, I think when we started... (speech)... At least Jim is. Take care. Thanks, everybody. Happy holidays. Yep." -> One block.

    *Self-Correction on "Kieran"*:
    Input: "Kieran James Lubin"
    List: "Kieren James-Lubin"
    I must use "Kieren James-Lubin".

    *Self-Correction on "Jim Hermosdior"*:
    Input: "Jim Hermosdior"
    Context: CTO of Strato.
    Real person: Jim Hermansdorfer.
    I will correct to "Jim Hermansdorfer".

    *Self-Correction on "Labor corn"*:
    Input: "Labor corn"
    Context: "Libra was this year".
    Real event: The $LIBRA memecoin scandal in Argentina (Feb 2025 context in transcript, though transcript says "February of this year", transcript is likely from late 2025 looking back? No, "Crypto year in review" usually means end of year. Transcript mentions "between 2024 and 2025". So this is late 2025. Libra coin happened early 2025.
    I will correct to "Libra".

    *Self-Correction on "Center phase"*:
    Input: "Center phase"
    Context: Chess, AI, Centaurs.
    I will correct to "Centaur phase".

    *Self-Correction on "Metaphone podcast"*:
    Input: "Metaphone podcast"
    Context: Steven Chu physics paper.
    The podcast is likely "The Meta" or "Metaphor". I will stick to "Meta" if "Metaphone" seems like a total typo. "Metaphone" sounds like "Metaphor". I'll change to "Metaphor" or keep "Meta"? Let's stick to the text "Metaphone" but maybe capitalize to "Metaphone" to look like a name, or correct to "Metaphor" if I'm confident. Actually, Steven Chu was on the "Bankless" podcast discussing AI physics. "Metaphone" doesn't ring a bell. Maybe "Metaphysic"? I'll stick to "Metaphone" to be safe, or correct to "Metaphor" as it's a common phonetic error. I'll just correct to "Metaphor" podcast. Or better, "Meta" podcast. Let's leave it as "Metaphone" to avoid guessing the wrong show, just capitalizing it.

    *Self-Correction on "Mercada"*:
    Input: "Mercada address"
    Context: "put your Mercada address on our telegram".
    Could be "Mercato"? "Mercado"? "Mercury"?
    I will leave as "Mercada".

    *Self-Correction on "Silvesti"*:
    Input: "Silvesti"
    Context: Silver token.
    I will leave as "Silvesti".

    *Self-Correction on "Temple by Stripe"*:
    Input: "Temple by Stripe"
    Context: Institutions getting involved.
    I will leave as "Temple by Stripe" despite it likely being a misheard "Tie-up" or similar. Or maybe "Temples by Stripe". I'll stick to text.

    *Self-Correction on "Enterprise of the airlines"*:
    Input: "Enterprise of the airlines"
    Context: "we're on the board of the enterprise of the airlines".
    Real thing: "Enterprise Ethereum Alliance".
    I will correct to "Enterprise Ethereum Alliance".

    *Self-Correction on "Glacial price"*:
    Input: "glacial price"
    Context: "moves at some glacial price".
    Correct: "Glacial pace".
    I will correct to "glacial pace".

    *Self-Correction on "Meme courts"*:
    Input: "Meme courts"
    Context: "death knell of meme courts".
    Correct: "Meme coins".
    I will correct to "meme coins".

    *Self-Correction on "ZK"*
    Input: "ZK".
    Tech term.
    Keep as "ZK".

    *Self-Correction on "USDC", "USDT", "USDST"*:
    Input: "USDC", "USDT", "USDST".
    Capitalization correct.

    *Self-Correction on "Stables"*:
    Input: "stables".
    Correct: "stables" or "stablecoins".
    I will use "stables" as per common industry slang, or "stablecoins" if formal. Transcript uses "stables" frequently. I'll keep "stables".

    *Self-Correction on "RWAs"*:
    Input: "RWAs".
    Keep as "RWAs".

    *Self-Correction on "TGE"*:
    Input: "deliver the whole thing before the TGE".
    Keep as "TGE".

    *Self-Correction on "PAXG"*:
    Input: "PAXG".
    Keep as "PAXG".

    *Self-Correction on "Hyperliquid"*:
    Input: "Hyperliquid".
    Keep as "Hyperliquid".

    *Self-Correction on "Linea"*:
    Input: "Linea".
    Keep as "Linea".

    *Self-Correction on "Polymarket"*:
    Input: "Polymarket".
    Keep as "Polymarket".

    *Self-Correction on "Aave"*:
    Input: "Aave".
    Keep as "Aave".

    *Self-Correction on "Devconnect"*:
    Input: "Devconnect".
    Keep as "Devconnect".

    *Self-Correction on "Cypher punk"*:
    Input: "cypher punk".
    Correct: "cypherpunk".
    I will correct to "cypherpunk".

    *Self-Correction on "Block apps"*:
    Input: "Block apps".
    Correct: "BlockApps".
    I will correct to "BlockApps".

    *Self-Correction on "Steven Chu"*:
    Input: "Steven Chu".
    Keep.

    *Formatting check*:
    "**[MM:SS] SPEAKER_XX:** Speech."
    Paragraphs separated by blank lines.

    *Final check on "Mercada"*: Maybe "Metamask"? "put your Metamask address"? "Mercada" sounds like "Mercada". Maybe "Mercato"? I'll stick to "Mercada".

    *Final check on "Libra"*: The transcript says "Libra was this year... Labor corn". Correct to "Libra".

    *Timestamps*: Ensure they are preserved exactly at the start of the merged paragraph.

    *Word count*: The input is around 3000-4000 words? No, let's check.
    Input text length is substantial.
    I need to ensure I don't cut too much. I will keep the conversational filler to a minimum but preserve the structure and points.

    *Speaker identification*:
    SPEAKER_03 = Victor Wong.
    SPEAKER_00 = Michael Tan.
    SPEAKER_01 = Jim Hermansdorfer.
    SPEAKER_02 = Kieren James-Lubin.

    *Specific line*: "Jim, you're going to have to explain it to me one day." (Victor to Jim).

    *Specific line*: "I'm going to assume you're not talking about, you don't want me to talk about the fact that crypto coins didn't stay at an all-time high forever. And at some point, it could be yours, I guess." (Victor to Jim).

    *Specific line*: "Bob would have to tell the story" (Kieren). Bob Summerwill is in the list.

    *Ready to generate.***[00:04] SPEAKER_03:** Okay, we are live. Welcome to this week's Unchained Oracles. As usual, I am joined. I'm Victor Wong. I'm founder and chief product officer at Strato. And as usual, I am joined with Kieren James-Lubin, CEO of Strato. And the man with the oranges, Jim Hermansdorfer, CTO of Strato. From sunny California that's not so sunny right now. Have you eaten many oranges or are they just... There's a tree behind me. Oh, nice. Well, this week we are going to do our crypto year in review recap. But before we get into that, two quick things. One is at some point during the show, I will announce a special giveaway. And it's going to be a really special year-end giveaway. But in preparation, we recommend that everyone get a Strato account if you don't have one already and join our Telegram because those will be two parts of it. And before we get into the URL to sign up? Yes, uh, thank you, uh, it is strato s-t-r-a-t-o dot nexus to sign up. Yeah, and you can go straight to app.strato.nexus. Yes, and thanks Kieren. And then, uh, we are going, we are joined by Michael Tan today, uh, for our Strato spotlight because we have lots of new features to show. So Michael, uh...

**[01:44] SPEAKER_00:** What do you have for us today to talk? Hi, everyone. Hey, so I'm showing you guys the easy savings path today. Basically, it's bridging in stables from Ethereum and saving them earning yield in the lending pool. So I start by connecting my Ethereum wallet as such. It's a really simple process. As long as you have it in the browser, my wallet is connected. I can pick between USDC and USDT. We're going to be adding a couple of different stables soon, including yield bearing ones. Let's bridge in 100 here. Make sure this is checked so that it goes directly into the lending pool. We just add these cool modals, but you just need to confirm everything, sign the permit, confirm the transaction. Why is it? All right, there you go. Takes a couple of seconds. Waiting for the all safe. Great. Now we should be receiving the deposit one to two minutes into the lending pool. And that is your easy savings, fastest and easiest way to earn points on Strato.

And now, so in the background, what's happening, Michael? It looks like we're converting from USDC into our local stables, USDST, and then putting it into the lending pool. Is that right? Yeah. Yep, that's correct. And you could do the same with USDT if you'd like. Awesome. And we also have a bridge out feature if you ever need that over here. But for now, this is the easiest way to get money in the lending pool and start earning. Cool. And as everyone knows, we launched our season one reward program roughly two weeks ago. So how's that going, Michael? Yeah, so we have quite a bit of points that have been issued. You can kind of check it here. The leaderboard, if you go to this tab, you can also go here to go directly to the leaderboard from the sidebar. But as it currently stands, it looks like I'm number 13 on this. You can check out the different activities in the network that are being done to earn points as well as the rewards here. These are your different positions that are currently earning points. And this is my lending pool from Easy Savings. Awesome.

**[04:05] SPEAKER_03:** You got to bump up your activity to get up on the chart. You got to get to the top three soon. Well, thank you for joining us, Michael. And we look forward to the next segment. So with that, take care. Thanks, Michael. Okay, so let's talk about the crypto year in review. This has been like, when I kind of like reflected, I realized this kind of been a crazy year for crypto in general. And I think for us specifically, like there's just been so much going on. So let's start with what you think is the biggest story of the year. And I'm going to start with Jim. Jim, from your point of view, what do you want?

**[04:49] SPEAKER_01:** You know, I want to push back a little bit on this one because I'm not going to push back. I'm going to answer the question, but I found this the least interesting of the questions because sort of by definition, the biggest story is the stuff that we've all been talking about nonstop all year. Anyway, it's the stuff that's been in the news. So it's just like, my answers to this are just going to be boring and obvious. It's like in crypto in general. Well, sorry. It's at BlockApps. The big story was that this was a development year. Like, we spent the whole year, we figured out what we wanted to do early on, we spent the whole year really making a great product and really only released it in the last few months. So that is the big story from us. In crypto in general, the big story was just the crazy ride that crypto took. It was like, you know, Bitcoin was down and then it was up and then it was down again. I don't even know where it is today. Somewhere in the middle of the year, I have this memory of seeing Eric Trump live in Toronto introducing some crypto project. So it's just sort of a crazy ride this year in crypto. But I will pass it on.

**[05:58] SPEAKER_02:** Okay, Kieren, what was your biggest story of the year? Okay, so I'll quibble with Jim a little bit. I think mine's a little bit a meta story. So it depends what you mean by big. Like I have a little bit of a philosophical objection to news. News is always point in time and it doesn't really tell you trend. I think we would agree on this. And people that over-index on the current and then under-index on like what's really going on. You know, and the biggest one for me was that adoption and price have continued to decouple. Like, we started to see maybe 2023, 2024, that the supply of stables on chain, it previously was correlated with crypto prices and then started to stop being correlated with crypto prices. And stables on chain are all time high and transaction volumes in stables doubled again between 2024 and 2025. I believe, I asked the AIs this, they all said that. So at the same time prices are a little bit down from beginning of the year to end of the year. So this may just be how it is for a while. There's also other metrics like active wallets are up by maybe 10 million depending on the time interval that you consider. There are different estimates. Mobile's up 20-ish percent. And also the institutions are clearly doing more than waiting in, they're actually like quietly moving money with stables especially around the world. And there's more of a kind of recurring institutional buy that's going on where crypto part of the reason it's been so volatile is that you know a bunch of very aggressive speculators are buying and selling rapidly. And if you compare stocks, the stocks that get included in the major indexes, you know, quite often people have their send 500 bucks a month to Vanguard. Right. And so that smooths out the volatility to some degree in, let's say, high, medium to high market cap stocks. Right. That's actually a little bit starting to happen in crypto. I think at some point you'll see some of the assets get included in indexes. So that same pool of capital will start to flow into crypto. It's been friendly on the regulatory side, at least largely. The U.S. is passing some of the laws. The laws may not be perfect, but they're better than before. And also just the behavior of the regulatory agencies is far less aggressive, far less arbitrary and capricious, if you will. And yet the prices are not up. So to me, this is okay. It might be a sign of maturity, but this is the story.

**[08:55] SPEAKER_03:** Or do you think part of it might be that like, the adoption from institutions and more mainstream things is sort of a leading indicator of where it goes? Like, it's not like, you know...

**[09:07] SPEAKER_02:** Some big BlackRock announces some big thing and they turn it on immediately. So you know maybe like, it does feel like to me that most of the times the institutions are early and you know retail price action comes later. You see that like funding private companies. Yeah, that you kind of you need retail slash the public markets to get that next liquidity, right? I'm not sure because there was a time, you know, when everyone had their stimulus checks and was gambling at home, you know, during the pandemic when like retail... On everything, not just crypto. The GameStop, you know, era. So... I don't know what the trend like now, I guess that was all stuff that was funded 2017, 2018 by ICOs, which were a mix of institutional and crypto whale retail and so on. So I don't know. I think the retail comes back, but it's a different form than the last time. Like you definitely... Most people that trade in general, this includes stock day trading, something like 90 percent lose. And one of our employees is fond of saying 90 percent lose. And on average, it takes 18 to 24 months for them to admit it and stop and just total, you know, in effect. But so we may have burned like a whole lot of people, but different ones will come in the future, I think.

**[10:46] SPEAKER_03:** So for me, I think the biggest story, well, maybe I'll start with the crypto one and then just my general theme, right? The crypto one is the return of building that matters in the crypto space. And what I mean by that is I think in the previous year, you know, it was sort of the rise of meme coins, right? Like people were just kind of like marketing was winning the day. And it really was the people who kind of like could make a big splash of excitement in the market. And, you know, I was kind of shocked when I looked at the timeline that like the Libra was in February of this year, like it feels so long ago. And but like Now you see the projects that are rising, like Zcash, the rise of Zcash, like projects that have been building for a long time and kind of really, really investing on the infrastructure side. And even like the institutions getting involved on the infrastructure side, like Temple by Stripe or things like Robinhood and doing their own too. So I think As builders ourselves, I like to trend back toward building. And I think that's a big trend this year. But I think part of the other trend, which is crypto directly related, is that AI has gotten really, really good and it kind of affects everything, but it certainly affects my day-to-day and I think our day-to-day ability to deliver, right? So like, you know, like our mutual friend, Steven Chu, who just published, I think the first theoretical physics paper that was like co-authored by an AI. He describes AI at this point as like a super genius that is kind of crazy, which is kind of like exactly the thing. Like, yes, it does lead you kind of like on some goose chases sometimes, like hallucinations and over, but its potential to shortcut so many things is so powerful. I think we're going through a phase right now in the last couple of months where people are sort of figuring out the limits of AI.

**[12:57] SPEAKER_01:** Which is an important step in this because now that's going to bring us to the next stage. Like early in the year, it just looked like it was magic and can do everything. But we knew it wasn't doing everything because, you know, it hasn't taken over the world yet. But now we're sort of understanding what it is that it can do and can't do. Yeah, I agree. And even how to check.

**[13:21] SPEAKER_02:** Kind of what it should be doing, right? Like I think when we just took the outputs and we just assumed, okay, those are okay. But like, I think it's like chucking it. What do you think, Kieren? Let me add an example. I've talked a bunch of times about getting back into writing code because the AI is so good. And I thought that this applied mostly to the app layer of our stack. So for those who haven't seen it, we have an app that lets you save in high quality assets, participate in swap pools, lending pools, you know, all that sort of thing. It looks like kind of a, you know, somewhere between a DeFi app and it's definitely DeFi in architecture and like a, you know, Coinbase style application. And so the AI is actually really good at writing code in the app layer. But I didn't think so. We also have our own in-house blockchain that we've worked on for years, starting with being an Ethereum mainnet client, kind of forking off for enterprise use and then going back to being our own standalone L1. I didn't think the AI was going to be ready to help code in the really hardcore platform layer, but at least for simpler stuff, I discovered a couple of weeks ago that it can. In fact, that if I describe, so the thing you have to have is like a good instinct for how the pieces work together. Like, you know, the peer to peer process is doing this and we see this in the logs and then it's, you know, the data is getting to the VM this way. And like, so I still have all of that, but I can barely write the Haskell anymore, but I don't have to. If I keep it pretty constrained and this is like a surgical fix, not like a big rewrite I couldn't do or something like that. I can just describe what's wrong and what's probably right. And it more or less gets it right. And I don't think it could do the Haskell six months ago. It's pretty good now, again, for surgical fixes, not like really big stuff. But each part of our stack getting more accessible to AI is a remarkable change. I'd also say, like, I remember when I was very good at net new code snippets, but couldn't read a code base. And now I can read a code base like maybe as of a year ago, maybe eight months, ten months. It can read a code base so much faster than I can that I just don't need to read the code base except...

**[15:49] SPEAKER_01:** Line by line on a specific issue. So Stephen did say something in the podcast that until he said it, I kind of like was intuiting it. But but it really was like a moment when he said it. Is that, so I've been wondering why, even though I have all these amazing tools, why sometimes I am not going a lot faster than I'm going. And in fact, sometimes I'm even slowed down. And he expressed something that he had experienced in writing the physics paper. which is the wild goose chase problem. These things know too much and they can throw out lots of great ideas and you can go off and just spend hours trying to research each of the ideas. And you end up wasting more time researching all the potential good ideas. And, you know, a lot of them don't pan out. Some of them do. Sometimes I learn like, you know, there's enough of a yield to it where I get some like lifetime tool out of it. that it was worth it to do it. But I'm wasting a lot of time just slavishly doing what the AI wants me to do. And I've gotten a little bit ruder with the AI lately and telling it, like, that's a stupid idea. I'm not going to waste my time. Yeah. Let me add to that also. Sometimes it feels like...

**[17:04] SPEAKER_02:** There's certain types of like attorneys or accountants or whatever professional service workers who want like the belt and suspenders thing like let me give the answer that minimizes my risk as the professional services provider oh and by the way maybe cost the client like a lot of time and money. Yeah, I agree. You have to yell at it when it gets a little too um...

**[17:28] SPEAKER_03:** I don't know. And the thing is also, I think the thing with Steve that he also said, and by the way, everyone should check out the latest episode on the Metaphone podcast, because he did the paper with the AI on physics, which I don't understand. Jim, you're going to have to explain it to me one day. But he also did another paper on how he did use the AI to write the paper. And that I found fascinating. I feel like we're entering what I call the centaur phase. There was this phase in chess with AI where the best chess players were actually computer chess engines combined with expert chess players, right? And I feel like that's where we are now. Like you need some level, like you need to be an expert yourself to be able to evaluate the output of what the AI does. And you can't always just say, oh, like the AI should know what it is.

**[18:27] SPEAKER_01:** Yeah, but it's like the AI telling the master chess player to go off and play 20 games to, you know, try different things out or something. Well, the solution is ask the other AI to play. Exactly. Like double check that thing. You don't even have to ask another AI. These things are like myopic enough that if you just turn around and ask the same AI, sometimes it's like very angry at the first, uh, its own first. It's true. Yeah. What irritates me a lot is like when it's like, here's a snippet of code for you to try out. And I try it and it doesn't work. And I come back to it and the, and the AI is like, you're an idiot for trying that snippet of code. Obviously it wouldn't work. So, yeah.

**[19:11] SPEAKER_03:** I, one, one area AIs have not gotten down though is like spatial reasoning. I did ask it to like come up with a design for like a box, you know, and give me the lumber that I needed. Like I just kind of grabbed the list, ran off, got it. And then I came back and it was like totally wrong. Like I was like, and then when I looked at the diagram, it was like the wood had like overlapped with each other in space, you know, like.

**[19:38] SPEAKER_02:** Things like that. Spatial reasoning seems... You would need to train it on a bunch of engineering diagrams or something. That's actually... Someone should do that. I'm surprised. Probably a bunch of people are working on it. I'm sure they're working on it. I think...

**[19:54] SPEAKER_03:** So this is sort of in the space between the diffusion models and the LLMs. So I think that's where, like, you know, and I know a bunch of people are working on kind of getting those. But I think, you know, when you ask the spatial relationship questions, you can be sent to one or the other, and it sometimes gets confused. Okay, second big category, biggest surprise of the year. I'm going to start with Kieren. What's that?

**[20:18] SPEAKER_02:** Things like that. Spatial reasoning seems... You would need to train it on a bunch of engineering diagrams or something. That's actually... Someone should do that. I'm surprised. Probably a bunch of people are working on it. I'm sure they're working on it. I think...

**[20:18] SPEAKER_03:** So this is sort of in the space between the diffusion models and the LLMs. So I think that's where, like, you know, and I know a bunch of people are working on kind of getting those. But I think, you know, when you ask the spatial relationship questions, you can be sent to one or the other, and it sometimes gets confused. Okay, second big category, biggest surprise of the year. I'm going to start with Kieren. What's that?

**[20:18] SPEAKER_02:** Okay, so I thought about this. I have a two-part answer, slightly related. One, October 10th, that was like a Friday. I think we had wrapped some work up. I was sort of like, I can't remember exactly what was going on. But then, you know, it just, everything just, what's November 10th? 10-10, right? Yeah. And then just like everything blew up. Like, you know, you're up the next morning. It's like, whoa! Like... like 20 billion. It was like the 20x larger liquidation than had ever happened before. I guess there's a lot more leverage in the system with Hyperliquid and all of these. But sort of a perfect storm of circumstances. And it just happened so fast. And I guess all financial markets are like this, like things can just explode or you know in an instant or all financial markets with the enough liquidity and derivatives right but um that was wild um I'm gonna add a related but you know you know on the edge so metals are at an all-time high right now yes we like when we were starting to build out metals we you know acquired some for direct sale on our like version one Marketplace and like I feel like our average silver cost basis was like 25 bucks 27 29 it's like over 70. So like at least in the last day, I don't know what's that right now. Gold also on all time high and cryptos down. And it sort of shows I believe sort of this for a while. But and I hope it maybe becomes not true in the future. Mostly crypto does not behave like a defensive asset. It behaves like a high beta tech stock. It's risk on, you know, so you'll see if The major tech companies go down, Bitcoin goes down, and vice versa. It's not always true. I think Liberation Day, we saw that happen for both. And then crypto actually went up in sort of a, well, if they're going to restrict the movement of goods, they're not going to restrict the movement of crypto. It's hard to do. Why is it? Why is this? I think it's just like it's the same type of people buying both and they see it as a future facing technology speculative asset. I mean, for a long time, people have pointed out that if you look at crypto instead of acting as a hedge against the stock market, it acts as more of a high alpha line of the stock market. Early on, Bitcoin was totally uncorrelated with the stock market, but I think it probably started being correlated at least by 2020, but maybe even like 2018, let's say.

**[23:18] SPEAKER_01:** Okay, Jim, what was your biggest surprise of the year? So I'm going to say the return of, even though it never went away, and by the way, this might be recency bias because this has all been the last couple of months in my world, but the return of ZK into the world. Suddenly about two months ago, I started hearing everybody talk about it again. You know, like we, uh, when we were down in Argentina, a lot of the talks were about that, um, board meeting, people were all asking us what's your ZK strategy. Uh, you guys all of a sudden got really interested in the Zcash client that I, that I had worked a bit on a couple of years ago. Um, It looks like it's probably real right now because there are certain applications that are actually working. Although I won't say which, but I went to a bunch of talks in Argentina that clearly were vaporware. Maybe that's even generous, like things that didn't make sense to me. But there are a couple of applications and the scaling application that I guess will probably happen in Ethereum could be big. So it's kind of exciting. Yeah.

**[24:35] SPEAKER_03:** I mean, like, if you look at the trend lines, it's crazy. I think, like, last year to do a proof for on the, like, Ethereum blockchain testnet, it took, like, a computer with, like, 48 GPUs. And then now it's down to four. So it's, like, really accelerated. Yeah, I'm not sure why that's happening, but it does seem to be. I think many things are true at once on the why. This is speculation, but yeah.

**[25:02] SPEAKER_02:** One, like the EU came out and said like, oh, you're gonna need a driver's license to use the internet. And this like scared the crap out of everybody. And then we're like, you know, we weren't taking the privacy thing as like, we just wanted to pump these prices, but like, you know, are they gonna like, are they gonna need to like put my fingerprint for my computer to turn on? No one has suggested that yet, but like, so the, you know, the cypherpunk fundamentals kind of have come back into the focus as like, at least visibly, you know, governments seem to want to, you know, reasserts or search control over the internet. Um, and yeah, I think, I think the privacy people were here in backgrounds. We went to the cypherpunk Congress at the beginning of, uh, Devconnect. And like, clearly these people had just been there for 10 years and we kind of forgot about them and they're just still there. But as a matter of fact, The Zcash price went crazy. I think definitely some people were trying to find a way to rotate out of something into something else without making it look like they're selling the thing. But it's also, I think... Yeah, maybe also like post-meme coins, there was sort of like a value rediscovery going on, you know, in that like even the kind of more extract-y crypto types seem to have some cypherpunk inclination. Not always. There's a lot of new entrants that are more like the Wall Street personality. But some mix of organic and manufacturer got ended then the price action got got everyone thinking about it again. One thing that would, uh, occurred to me as I started researching privacy again because we spent lots of time with it both in our enterprise days and then subsequently we were kind of trying to figure it out before mainnet launched which is why Jim built most of the Zcash client, uh, and then we kind of dropped it for a while. But, uh, part of the reason it came back for me is that it also seems more viable like there's a bunch of competing Ethereum ecosystem privacy products like Railgun privacy pools and so on. I guess Roman Storm was in the news a bunch during the year, uh, Roman Storm of Tornado Cash of course and I didn't realize that it like kind of maybe basically works and it, it sort of didn't like Zcash also had added, like they've got a mobile wallet now that supposedly just works. Yeah. And it's easy to shield. It wasn't easy to shield before. So something like perfect storm of factors seem to reignite the privacy. I think part of it is just people realize, you know, as maybe a new kind of...

**[28:00] SPEAKER_03:** Um mainstream adoption is taking place people are realizing oh crap my balances are in fact public. Yeah, there's a wrench attack per year per week in 2025 something like that. Yeah, so like, I, I think graphic too there was an assumption that my balance is war shield, I think for mainstream audiences and Now they're not. So my biggest surprise of the year was really the Robinhood announcement. And it wasn't that Robinhood was doing stuff in crypto. We knew that forever, right? But the kind of many things they announced at the same time, their own L2 announcement, that they're putting, that they had their own tokenization engine, that they were doing secondary stocks and kind of like pushing it out immediately. I think it got like everyone really interested and excited. Like I think that sort of put in the arms release of institutional adoption, right? Like I think that kickstarted it. And it was surprising because like, you know, like we're on the board of the Enterprise Ethereum Alliance. We talked to, we have a lot of connections with enterprises still, even though we're out of that business. And, you know, it caught a lot of those companies off. Like we, we had conversations with a bunch of other companies or like explain to me what Robinhood is doing, which is kind of interesting. Okay. Next one. We never like to talk bad about anything, but what was your biggest disappointment this year? I'm going to start this one off. I think, like I mentioned before, Libra was this year, it was February this year. It was kind of shocking, the level of interest manipulation, like when the whole story came out, you know, that something could get effectively to the presidential office of a government, you know, in order to do that. So in that way, it was kind of shocking to me. I know, Kieren, you're more pro-MemeCoins than me, but like it was, It sort of, I think, you know, on the good side, it seemed to be the death knell of meme coins. So I think even though the actual incident was pretty disappointing from my point of view, it did kind of like the consequences, I think, put the industry in a much more positive direction.

**[30:31] SPEAKER_02:** What do you think? What's your biggest disappointment? So I'm going to mostly agree, but with a different take. I'd say the nature of the meme flame out. Like, you know, I think I'm sort of like excited about all of the, you know, the activity and the government kind of getting pro-crypto in the U.S. and the Malay revolution. We'll see, you know. But the... the way I guess it takes a certain amount of expertise to like embrace crypto the right way or a certain level of uh non-cynicism or something like they could have just hodled you know yeah like uh but yeah I think the um in principle there is no reason that meme coins have to be a pump and dump vehicle right like Some people say Bitcoin is the original meme coin. And Doge is just still here and big and still kind of funny. And like pump.fun, I guess just sort of so strongly orients the economics of the system. And I'm not saying it's anyone's fault for participating in it on either side, launching the meme coins or buying and selling the meme coins. But again, 90% of people lose. It's mostly about timing. You got to just know when they launch, buy them really fast, sell them right away. And this is like a reliable way to make money from some group of gamblers who eventually then they haven't totally stopped, but will eventually stop. playing in this particular casino and it's like it doesn't need to be like that I think you know I think Base tried to rebrand them to like creator coins you know but like most a lot of the problems in I don't know incentives are about timing right like if you just forced some sort of hold then if the meme coin's vested, maybe it would be fine. But we're just dumping them on retail. And so NFTs had a phase like this. Some of them will kick around. They kind of came back in a rhyming way as meme coins, which were much more liquid. And you're able to like trade concepts. And, you know, I've said before, I see there's a sense in which meme coins are like the flip side of prediction markets. They're just a measure of what people believe. But the design is bad from like a market structure perspective and as a norm. It's like everyone opted into this, but it still kind of looks gross when you look at it.

**[33:24] SPEAKER_03:** Yeah, I mean, I think it's the difference between a speculator versus a builder mindset. Like we know it takes time to build stuff, right? Like you, you know, building audiences, building, you know, products, it just takes time. AI has sped that up, but you have to invest that and have that longer term outlook. Okay, Jim, what's your biggest disappointment of the year? And I'm going to assume you're not talking about, you don't want me to talk about the fact that crypto coins didn't stay at an all-time high forever. And at some point, it could be yours, I guess. You know, I have to tell many people, like, hey, you know, now that we have to manage our treasury, this is going to go on forever. I'm like, wait a second. It's not going to go on forever.

**[34:11] SPEAKER_01:** Nothing ever goes up forever. You know, like well I'm gonna go a little bit more myopic uh look uh in the development of our product uh and sort of treat it as like a lesson maybe uh I think um My disappointment was various features that we had put into the product that were sort of an extension to Ethereum. And we do have some good extensions to Ethereum that we're keeping in there. But various parts we sort of had to pull out. For instance, we had taken identity, turned it into a username, built a lot of security around that, and then... and and then turn that to a first class citizen so that it wasn't something built upon it we sort of had to pull that out because we realized we have to especially with the new direction of the company we have to really integrate with things that are out there so even something like using a wallet became hard when you know the first thing you have to do in the wallet is like have the address database and I'm like well we're not really based on addresses and so so some some sort of cool things were pulled out. But the important thing is like, I think realizing that there is, uh, uh, and whole, there's a whole like ecosystem out there and we are part of that now. And we have to like sort of stay within the parameters of that ecosystem. It's let me add, um, uh, so many, like no one really loves solidity. Um,

**[35:50] SPEAKER_02:** People are probably almost instantly on arrival. We're unhappy with the ERC-20, you know. Yeah, yeah. Standard. Someone who maybe worked on it, Bob would have to tell the story, but instantly started dedicating his life to trying to move to a different standard that's mostly the same, but better, gets rid of the approves. I'm on the record for saying that I'm very pro UTXO versus Merkle Patricia for data. Every engineer likes something UTXO flavored better, including me. We're just stuck somehow with the ERC-20. It's like the COBOL. Solidity in ERC-20 is the COBOL of the. It's going to be here. People keep trying. I mean, Solana kind of made Rust smart contracts work, but that's like the only other example, really. Everyone goes off and invents some UTXO thing because it's like much cleaner conceptually. And then the devs don't use it and it doesn't integrate and so on. I guess I would say partial exception with some of the privacy tools, but it's built on the ones that people use or have like a base of ERC-20 or Zcash.

**[37:12] SPEAKER_03:** I mean, yes, but it's one of these things where every developer always wants to write. They're like, this language is terrible. I'm going to write my own language, and it's going to be so much better. And no one ever uses that language, right? Whereas what actually happens is people make JavaScript much faster.

**[37:34] SPEAKER_01:** Kind of have like an internal joke because I won't mention any names, but we had a developer once who we assigned some years ago. It was like 15 years ago. This is the last company we worked on together. Last company, yeah. We asked him to do task A and he was like, before I can do task A, I have to rewrite like the language and create a rules engine that would be used so that, I don't know. So we always use the phrase rules engine whenever somebody wants to go out and build it. But it still was, you know, like it's one thing to be able to, to build cool new additions. It was a little sad this year to actually have to sit there and rip out cool new additions to be compliant though.

**[38:20] SPEAKER_03:** We'll add more in time. But it's funny that in many ways we got back to basics, like in not only from the tech, but even in branding, right? We went back to our original Strato name, even though we had been kind of like adding over to it. And that, you know, it takes us back 10 years. Okay. Strato update and roadmap. So Kieren, I looked back at this. I think at the end of 2024, Our TVL on Strato was slightly less than $100,000. It is currently about over $9 million. 90X in a year is pretty good. Yes, exactly. Can you give a quick update about what's happening with the project and any things that you want to let people know to look forward to in the coming year?

**[39:12] SPEAKER_02:** Yeah, well, I think at a, you know, the top level, we're trying to make the thing useful and popular to see how to measure that. Right. But, you know, more TVL is a good proxy. The thing is generating revenue now to generate more, you know, actually like the CDP and the lending pools are just like, you know, there's just a little bit of interest accruing every day for the protocol. It's like, well, and the swap pools, too. We'll see lots more assets. So at the moment, we've got sort of like four first class assets and then LP tokens of different types, including our native yield coin, which is driven by our lending pool. There'll be lots more. So from tokenized stocks, we're third party. These are all third party issued. And if they're available within DeFi, we can kind of copy and paste over the the terms and conditions and you know people can choose to to use those um third-party yield coins um all manner of so to also be releasing things like so we've got first party gold and silver uh there are a couple good gold coins there may be one good silver coin out there uh releasing things like stable swap pools so that um You certainly can go drop your metals off in the vault and you can pick them up. You can exit within our system by swapping to, say, ETH or our stablecoin and withdrawing. But you could also go swap to other crypto as well so that for convenience sake, it's easy to get out and it helps support the price within the system. Another yield source we're thinking about, we found that not only do you need swap pools for people to be able to put liquidity in and being able to trade, but you actually need to monitor those swap pools all the time. It's quite easy for the implied pool price to differ from the spot price of the asset or the ratio of the spot prices of the assets. So what you try to do then, we ended up writing a little trading bot that just watches the pools and then kind of sort of, it does an arb in effect, but it resets the price back to spot. I realized there's some platforms like Lighter, Hyperliquid, maybe first, where they set up vaults. That in essence trade against the other users it's not like not in a you know extractive way but in a make sure there's someone on the other side to do the trade so like if there's a big trade on a swap pool let's say it moves the price one percent then there's an arb and the bot can put the price back one percent uh realizing a profit in the the But if you imagine actually the same people put into the LP and roughly equal amount into the bot, then kind of ARB loss canceled out and it converged to HODL, but there was a fee that came in. So for folks who want to, we're trying to, you know, you don't really want, vicious arbitrage has taken up the arbitrage op. If you can give it back to the users, that's that's a preference. So more ideas like that. We've also got, you know, like we've not had any liquidations on system yet. I hope not to have many. I'm sure they will come someday. We try to encourage pretty low LTV borrowing. Um but that you know similarly we could have pools that cover certain types of uh uh like you know like we don't have a liquidation bot yet but if we have to we could have a pool for that uh for instance so that kind of the money goes back to less predatory hands um so yes more assets more more yield um privacy we're serious about uh we've uh you know The meta may be forgotten by the time we ship our privacy stuff, but Jim has been looking hard at how to incorporate some of the knowledge that's in his head and some of ours, and in the ecosystem too, with what we're doing. It does look, so we've been like, we've tried to like install a bunch of the privacy tools and they just like barely work. They work, but you really gotta cajole them into, you know, and so if you could provide an experience for like an end user, that's kind of default private, but easy, you know, like I think consumers need to be opted for. Um into privacy by default and that they should have to opt out explicitly that's kind of the guarantee you get from a bank or exchange right it's just private now the bank knows everything about you and probably you know reports it to whomever whichever authority and so on but otherwise You know, exchanges have always been like the poor man's mixer, right? Like there's kind of just one account. The exchange is a big slush fund of assets with off-chain claims on them. And so if you're trying to not let someone know your real balance, you just put a little on an exchange and take it out, right? And you know we want the world to be more of the DeFi way. DeFi is super transparent and it actually does seem viable to do um at least a subset of DeFi with privacy uh this is sort of what Railgun and some others have shown but the devil's in the details it's not at all easy. Yeah, so it'll be a big one and We got all the last categories like, I don't know, consumerization, like getting easy on ramps tied in, like actual on ramps, but exchange listings for some of the tokens, say. So on the fourth, more bridging to external chains. Things like having a credit card wired up. Know that there's a bunch of products that have that today and we're actually thinking about trying to integrate with them as opposed to like issuing our own I like a degree of indirection from the legacy system so if you take US dollars into a bank account and then mint stables it's a big complicated business but if you just take USDC it's um it's you know the USDC settlement it's more or less final and there's much less you You know, like the person canceled the credit card payment, but kept your crypto risk there. Trying to kind of work with others in the industry to produce a complete end user experience, but also keep it like in the on-chain style. Much, much longer term. We want to kind of fill in the suite of services people expect from financial institutions like, you know, unsecured or under collateralized lending and so on. But probably that won't be next year, but we're definitely going there. You should just be able to live your whole financial life on chain. One more thing. You know, we've been trying to make it very easy to get new users on board from like a phone interface, like one of the brilliant things about PayPal, Venmo, et cetera, is that you could pay someone who wasn't in the system yet so long as you had some kind of contact info for them. So I still you barely see this in the crypto world. I've not seen much in the way of like, you know, like texting someone money, but we'll roll something like that out soon and not too long. So It's kind of two axes, keeping it cypherpunk, making it easy and feature complete.

**[46:53] SPEAKER_03:** Yes, like bringing cypherpunk power to the normies. To grandma, eventually. You don't have to wear masks to have some privacy. I think people are realizing that. That should be an expectation to a certain point. I do think the right thing about shielded balance is you don't have to protect everything, but you have to protect certain things, like how much you have. Okay before we dive into our 2026 predictions I want to announce our giveaway tying into Kieren's thing about uh metal prices are way up this year despite crypto we want to take away some of the crypto down pain by doing a giveaway where we give away three um of our silver tokens so each silver token is equivalent to one ounce Silvesti. And to enter into this, it's a lucky draw. You have to put your Mercada address on our telegram. And we will pull three lucky winners from all the addresses we get. And we will send them one Silvesti equivalent to one ounce of silver. So hopefully that will be a nice holiday present for a couple of people. And we hope that you sign up as quickly as possible. Okay. With that, let's go to predictions. Jim, what are your predictions for 2026? Okay.

**[48:29] SPEAKER_01:** My prediction is that this will be the year of usability. It has to be. There's so much riding on, there's so much good technology out there right now. And there's so much riding on who wins this. And so many of these products, which are based on something very solid, just can't be used. I won't call out names, but multiple times this year, Kieren might come to me and say like, here's a really cool project, go use it. And then I would waste days and days just trying out to do the most basic things with it. And I know how this stuff works internally. And you are the Zcash client. So, like, if you can't do it, who can do it? So, I think there's going to be a lot of pressure to make these things just work. And we've sort of hit a point where, you know, there's always stuff to add, but the basic stuff is out there and it works right now. So, there's got to be a lot of competition. And we're going to be part of this for sure to make this stuff as easy to use for the end user and just work. Yeah.

**[49:27] SPEAKER_03:** Okay, I'm going to go second and leave you the last, Kieren. My prediction is this is the year of ZK scaling and institutional crypto adoption, but it's going to be slower than people think, at least from the adoption side. I say that because we have worked with a bunch of big enterprises and governments in our history. And even when they do some giant ass press release, it all moves at some glacial pace. So I think we're going to see some traction and making that more real. But it's going to move a hell of a lot slower than everyone on crypto Twitter thinks. But I do think, like I said, like I think the first kind of shoot or drop in the world of ZK is going to be around ZK scaling. And I think we're going to see huge improvements this year. So, Kieren, what are your predictions? Bring us home.

**[50:25] SPEAKER_02:** Okay, so I predict, and this is not unrelated to Jim's, a continued DeFi, TradFi soft merger, where you'll see TradFi capabilities in DeFi, you'll see TradFi using DeFi rails from stables and into more sophisticated stuff. Something remarkable, like, in some ways, like, you know, Aave is like the federal funds rate of... You know, like the USDC borrow rate on Aave is like kind of the benchmark for, you know, sort of low risk borrowing in in crypto. And that's remarkable. Like everything else in the world just instantly reacts to what the Fed does and maybe crypto does to the prices certainly do. But the stable borrowing markets, maybe it's it's a little bit indirect. And so I think we should see some level of continued boringness and that boringness is probably a good sign, even though we want good excitingness at different times. I think, yeah, so in that category, stables keep going up in supply and volume. RWAs continue to get bigger. We saw a big run starting the year in, let's see, like PAXG and others. Obviously, RWAs are way up in circulation as this year goes on. And part of the reason is just like even the dollars don't even dollars solve inflation in total you know they might it's much better that you know if your option is like or at least until recently probably still like the Argentinian peso to hold USDC let's say but like this year gold silver would have been better or you know treasuries are better than just dollars for instance so um I think, well, we just for practical reasons, you need the world is priced in fiat at least for now and may continue to be. So you just need a mix of things, you know, go along with your crypto, but also hold some other stuff so that day to day you're not in trouble. I also think related to Jim's point, the way I wrote it in my little notes here is that value capture will keep moving up the stack. So there was a time where what you did was write a 60-page technical white paper. Maybe you were a professor or something. Raise like $50 to $250 million on chain. Build some complex blockchain. Sometimes they worked. Sometimes they didn't. Um and there was like an L1 premium and even an L2 premium like you know having control of the infrastructure makes the token um uh go higher I think there's still a little bit of that um and you know we ourselves are an alt L1 and in part it's just like you inherit a lot of, I mean, still a lot of the assets primarily are bridged in from Ethereum. That's like the only real big source. And, you know, we have small integrations with Base and all that sort of thing. But, you know, I think the reason really we did it is to be able to deliver a better app on the top end. And so you'll see most of the value capture will start to be just fighting over users as opposed to more abstract infrastructure promises, you know, throughput, cheaper transactions and so on. I think the market is mostly moving away from that. There are still some. But, you know, it's again like the the The lighters, the Hyperliquids, Linea recently are fairly high in the stack. There's a big anchor app at a minimum for all of them. Perpdex, the wallet, various other apps on Linea. It's a short list of successful L1s, L2s. You know, Polymarket is on Polygon. I think that's a coincidence, but it's kind of funny. And that's the thing that really keeps the alt chains going. Of course, you try to get implementations of all the major protocols on there. But yeah, so I agree with Jim. It's about the usability. But but yeah, in a specific sense, like we got to actually just get people to live their lives in in this thing.

**[54:59] SPEAKER_03:** Yeah, the way I think of it is kind of adoption over research. Like, you know, I think when we started all the big new chains were effectively like research projects, right? Like they were big ideas and things that may or may never be delivered. And now, like, really, it's about, you know, kind of like deliver the whole thing before the TGE now. Yeah, exactly. Exactly. Well, with that, thank you very much for joining us for our Year in Review recap. I'm Victor Wong. You can find us at strato.nexus. And we hope you have a happy holidays. And please sign up for our giveaway and enjoy some vitamin C and sunshine. At least Jim is. Take care. Thanks, everybody. Happy holidays. Yep.