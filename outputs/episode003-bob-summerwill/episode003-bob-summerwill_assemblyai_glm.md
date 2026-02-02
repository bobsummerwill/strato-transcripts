1.  **Analyze the Request:**
    *   **Role:** Expert transcript editor specializing in Ethereum/blockchain.
    *   **Context:** Knowledge of known people (244) and technical terms (163) provided.
    *   **Input:** A raw transcript of a conversation about Ethereum's early days, focusing on Bob Summerwill's perspective.
    *   **Primary Objective:** Create a clean, readable transcript preserving *all* dialogue and content.
    *   **Critical Rules:**
        *   NO preamble/intro/meta-commentary.
        *   Start immediately with the first speaker label.
        *   Output must be ~90-110% of input length.
        *   Handle timestamps: Preserve exactly if present (Input has them).
        *   Format: **[MM:SS] SPEAKER_XX:** followed by speech. Merge consecutive speech into paragraphs. Separate paragraphs with blank lines.
    *   **Corrections (What to Fix):**
        *   Technical terms (e.g., "blockchain", "Solidity", "mainnet").
        *   Proper names using the provided list (Crucial check: "Bob Summerwell" vs "Bob Summerwill" - The list says "Bob Summerwill". "Vitalik", "Gav", "Anthony D'Onofrio", "Anthony Di Iorio" (Context suggests Anthony Di Iorio for "Anthony Diorio"), "Aya Miyaguchi" (Context: "Ming's been sacked" -> "Ming" might be Aya Miyaguchi's predecessor, but check text. Actually, "Ming" usually refers to **Ming Chan**. Wait, Ming Chan is *not* in the provided list of 244 people. The prompt says "Known People (244): ... Aya Miyaguchi". Ming Chan was the Executive Director before Aya. Since she is not in the list, I should leave it as "Ming" or verify if I can correct it based on general knowledge if the list is *exhaustive*? The prompt says "Known People (244)... Use EXACT spellings from the 'Key People' list above". It doesn't explicitly forbid correcting names *not* in the list if they are obvious errors, but usually, I should stick to the list or the transcript if ambiguous. "Ming" is a nickname for Ming Chan. I will keep it as "Ming" or "Ming Chan" if the transcript implies a surname, but the transcript says "Ming's been sacked". I'll stick to the transcript's spelling for names not in the list to be safe, but fix names in the list.
        *   "Bob Summerwell" -> "Bob Summerwill".
        *   "Anthony Diorio" -> "Anthony Di Iorio" (in list).
        *   "Gav" -> usually refers to Gavin Wood. "Gavin Wood" is not in the list. Wait. The list has "Aaron Davis... Aya Miyaguchi". It seems to be a *partial* list or maybe I need to look closer? Let me check the list provided in the prompt again.
        *   List: Aaron Davis, Aaron Wright, Adam B Levine, Adam B. Levine, Addison Cameron Huff, Addison Cameron-Huff, Aeron Buchanan, Albert Ni, Alex 'axic' Beregszaszi, Alex Beregszaszi, Alex Leverington, Alex Van De Sande, Alex van de Sande, Alexander Grossman, Alistair Stewart, Amir Chetrit, Amir Taaki, Andreas Antonopoulos, Andreas Lubbe, Andrei Maiboroda, Andrew Keys, Anthony D Onofrio, Anthony D'Onofrio, Anthony Di Iorio, Anton Nashatyrev, Arkadiy Paronyan, Aron Fisher, Artur Zawlocki, Artur Zawłocki, Aya Miyaguchi...
        *   It ends at Aya Miyaguchi. It seems truncated or it's a sample list? The prompt says "Known People (244): ... Aya Miyaguchi". It looks like the provided list *ends* there in the prompt text. This is tricky. "Gav" (Gavin Wood) is definitely a major figure. "Vitalik" (Vitalik Buterin) is not in the list. "Jeff" (Jeffrey Wilcke) is not in the list.
        *   *Constraint Check:* The prompt says: "Proper names - MUST use EXACT spellings from the 'Key People' list above". If the name isn't in the list (like Vitalik, Gav, Gavin Wood, Jeff), what do I do? Usually, in these tasks, the list provided is the source of truth for spellings of the names *present* in the transcript. If the name is missing from the list but is a real person (like Vitalik), I should probably spell it correctly (Vitalik Buterin) based on general knowledge and the context of being an "expert editor", or stick to the transcript. However, standard capitalization (Ethereum, Bitcoin, Vitalik, Gav) applies regardless of the list.
        *   *Strategy:* I will capitalize proper names (Ethereum, Bitcoin, Vitalik, Gav, Jeff, etc.) correctly based on standard industry knowledge. I will strictly adhere to the list for names *in* the list (e.g., if "Anthony D'Onofrio" appears, fix it to that). Since the list seems to stop at 'A' and the transcript mentions people like 'Vitalik', 'Gav', 'Bob', 'Jim', 'Kieran', 'Laura', 'Stefan', 'George Hallam', 'Ian Meikle', 'Fabian', 'Joe', 'Christian', 'Christoph', 'Barry Silver', 'Virgil', 'Anthony Busadi'.
        *   Let's look for specific corrections I can make:
            *   "Bob Summerwell" -> Bob Summerwill (Note: The transcript says "Bob Summerwell" but the prompt list has "Bob Summerwill". Wait, looking at the list again... "Bob Summerwill" is *not* in the list provided in the prompt text (A to Aya). This is weird. The prompt introduction says "Known People (244)" but the list provided only goes up to 'A'. This might be a copy-paste error in the prompt's "Context" section, or I am expected to know these people. The transcript introduces him as "Bob Summerwell" (pronounced/typed). I know his name is Bob Summerwill. I will correct it to **Bob Summerwill** because the prompt identifies him as the guest and calls him "Bob Summerwill" in the prompt description (or implies it? No, the transcript says "reconnect with Bob Summerwell"). Ah, the prompt introduction says "reconnect with Bob Summerwell". However, standard knowledge says Summerwill. I will use **Bob Summerwill**.
            *   "Anthony Diorio" -> Anthony Di Iorio (He is in the list).
            *   "Gav" -> Gav (Usually Gavin Wood, but transcript uses Gav. I will keep "Gav" or capitalize "Gav").
            *   "Vitalik" -> Vitalik.
            *   "Bitcoin" -> Bitcoin.
            *   "Ethereum" -> Ethereum.
            *   "mainlet" -> mainnet.
            *   "cpp" -> C++.
            *   "PI Ethereum" -> PyEthereum (Usually spelled PyEthereum or C++ Ethereum. Transcript says PI. I should probably fix to C++ or Py? Context: "PI Fapp or PI Ethereum as it was CPP Ethereum". Ah, "CPP" stands for C++. "PI" is likely a typo for "Py" or just the phonetic "C++". The transcript says "PI Fapp or PI Ethereum as it was CPP Ethereum". I will change "PI Ethereum" to "C++ Ethereum" or "cpp-ethereum" based on context. The text says "PI Ethereum as it was CPP Ethereum". I'll use C++ Ethereum / cpp-ethereum for readability).
            *   "go Ethereum" -> Go Ethereum / Geth.
            *   "ETH Zurich" -> ETH Zurich.
            *   "F" (Ether) -> ETH.
            *   "Dencun" -> Dencun.
            *   "Solc" -> Solc / Solidity.
            *   "SOLSI" -> Solc.
            *   "Salsa" -> Solc.
            *   "web3 umbrella" -> Web3 umbrella.
            *   "Dev P2P" -> devp2p.
            *   "FDEV" -> ethDEV (The text says FDEV AG. The company was ethDEV. The transcript says "FDEV". I'll stick to FDEV if it's ambiguous, but ethDEV is the real name. Actually, the transcript says "FDEV AG". I will keep FDEV as written but capitalize FDEV or correct if obvious. I'll leave FDEV as a proper noun if that's how they referred to it, but "ethDEV" is better. I'll stick to the transcript's specific term if unsure, but "FDEV AG" seems to be the name used in the conversation. I will fix "FDEV" to "ethDEV" only if I'm 100% sure. The transcript says "for profit FDEV". I will leave it or maybe capitalize FDEV).
            *   "Slocket" -> Slock.it (The company is Slock.it. Transcript says "Slock It", "Slocket". I will correct to Slock.it).
            *   "Dow" / "dao" / "DAW" -> DAO.
            *   "ds" -> DAOs (Vitalik wrote about DAOs).
            *   "Dow Link" -> DAO Link?
            *   "Bit coin" -> Bitcoin.
            *   "A two" -> Augur? No, likely "Augur" or "Maker". Transcript says "A two". I'll keep "A two" or "Augur" if context implies. Transcript says "You had Digix, this, this gold thing. You had dai...". "A two" might be "Augur". I'll leave it as "Augur" if I'm sure, otherwise "Augur" was very big then. Transcript says "A two". I'll stick to "Augur" if it fits, but maybe just fix capitalization.
            *   "Dow Hub" -> DAO Hub.
            *   "Christian Wright Weisner" -> Christian Reitwiessner.
            *   "Fabian" -> Fabian Vogelsteller (Maybe).
            *   "Joe" -> Joseph Lubin (Maybe).
            *   "Laura" -> Laura Shin.
            *   "Barry Silver" -> Barry Silbert.
            *   "Virgil" -> Virgil Griffith (Maybe).
            *   "Anthony Busadi" -> Anthony Di Iorio? No, "Busadi" sounds like "Bassil"? Maybe "Anthony Di Iorio" again? Or "Anthony Lusardi"? Let's stick to the transcript's "Anthony Busadi" unless it's obvious. Actually, looking at "Anthony Busadi" in context of ETC... might be Anthony Lusardi? The text says "Anthony Busadi". I will keep "Anthony Busadi" as it's a specific phonetic attempt that might be wrong, but without the name in the provided list, I should be careful. However, the prompt says "MUST use EXACT spellings from the 'Key People' list above" for names. The list stops at A. This is a major constraint conflict. I will assume the "Known People" list in the prompt was truncated but implies "Use standard spellings for known entities". I will fix "Slocket" to "Slock.it", "Ethereum" to "Ethereum", "Vitalik" to "Vitalik".
            *   "Kieren" vs "Kieran" in transcript. Prompt says "IMPORTANT: 'Kieran' -> 'Kieren' (Kieren James-Lubin, NOT Kieran)". I must change "Kieran" to "Kieren".
            *   "Ming" -> Ming Chan. (Not in list A-Aya, but I'll capitalize Ming).
            *   "A two" -> Augur.
            *   "Dow" -> DAO.

2.  **Step-by-Step Processing:**

    *   **Segment 1 (00:00 - 00:57):**
        *   SPEAKER_00: "Bob Summerwell" -> **Bob Summerwill**. "Identity" (Video title context). "mainlet launch" -> **mainnet launch**.
    *   **Segment 2 (00:57 - 03:57):**
        *   SPEAKER_01: "Vitalik". "Anthony Diorio" -> **Anthony Di Iorio**. "bitcoin decentral co working space" -> **Bitcoin Decentral** co-working space. "seaport" -> **Sierra**? No, "15 years of seaport, 15 years of C plus plus". Probably "C++". "seaport" might be "Sierra" (engine)? Or just a typo for "software"? I'll leave "seaport" or remove if it's nonsensical filler. "15 years of C plus plus". "cpp" -> **C++**. "smartwatch". "Bing" -> **bing**? Or "ka-ching"? Transcript says "Bing, there's some money". I'll leave "bing". "Gav". "parting company". "Hyperledger". "Ethereum Classic".
    *   **Segment 3 (03:57 - 04:25):**
        *   SPEAKER_02: "Nelson Mandela" (Joke). "Bob Summerwell" -> **Bob Summerwill**.
    *   **Segment 4 (04:25 - 04:46):**
        *   SPEAKER_02: "nolla size" -> **novella size**. "blog post".
    *   **Segment 5 (04:46 - 06:50):**
        *   SPEAKER_01: "Ethereum Foundation People". "DEVCON 0". "proof of state" -> **proof of stake**.
    *   **Segment 6 (06:50 - 08:17):**
        *   SPEAKER_01: "Ming's been sacked" -> **Ming's** (Capitalized). "Hudson". "Vitalik".
    *   **Segment 7 (08:17 - 09:47):**
        *   SPEAKER_01: "Bing was terrible" -> **Ming**? Or "Bing"? Context: "to my mind, Bing was terrible". Probably refers to **Ming** (previous director). "Bing" sounds like "Ming". I will change "Bing" to "Ming".
    *   **Segment 8 (09:47 - 10:37):**
        *   SPEAKER_02: "survivorship bias". "glaze over" -> **glaze over**.
    *   **Segment 9 (10:37 - 12:13):**
        *   SPEAKER_01: "Tim Berners Lee". "founding".
    *   **Segment 10 (12:14 - 13:09):**
        *   SPEAKER_00: "mainlet" -> **mainnet**. "Gav" -> **Gav**. "Jim" (SPEAKER_03?). "clients". "Gaff" -> **Gav**?
    *   **Segment 11 (13:09 - 13:30):**
        *   SPEAKER_03: "Jim". "Karen" -> SPEAKER_00 (Kieran? No, Kieren is SPEAKER_00. Wait. The labels are SPEAKER_00, 01, 02, 03. SPEAKER_02 calls him "Karen"? Transcript says "as Karen has mentioned". Maybe the host's name is Kieran/Karen? Or "Karen" is a typo for "Kieran". I will change "Karen" to "Kieran". SPEAKER_00 is likely Kieren.
        *   SPEAKER_03: "Jim".
    *   **Segment 12 (13:30 - 14:27):**
        *   SPEAKER_01: "Brian Bellendorf" -> **Brian Behlendorf**. "EA" -> **EEA** (Enterprise Ethereum Alliance). "Hyperledger". "Gaff" -> **Gav**. "Geth". "Parity".
    *   **Segment 13 (14:27 - 17:03):**
        *   SPEAKER_01: "Ethereum 2" -> **Ethereum 2.0**. "Consensus clients". "Grant".
    *   **Segment 14 (17:03 - 18:07):**
        *   SPEAKER_00: "bitcoin". "pre. Mine" -> **pre-mine**. "token presale".
    *   **Segment 15 (18:07 - 19:04):**
        *   SPEAKER_01: "specification". "PI Fapp or PI Ethereum" -> **cpp-ethereum** (as the text explains "CPP Ethereum"). "GO. Ethereum" -> **Go Ethereum**. "ethereum J" -> **Ethereum-J** or **EthereumJ**.
    *   **Segment 16 (19:04 - 20:28):**
        *   SPEAKER_02: "Jim Kieran" -> **Jim** (SPEAKER_03), **Kieren** (SPEAKER_00). "Ethereum H" -> **Ethereum-H** or **EthereumJ** (Jim is from EthereumJ/Enterprise Ethereum Group). The transcript says "Ethereum H". Probably **EthereumJ** or **EEA** context. I'll stick to "Ethereum J" based on later context or just "EthereumJ". Wait, the transcript says "Ethereum H". Jim Zhang/Jim? The text later says "PI Fapp or PI Ethereum as it was CPP Ethereum... Ethereum J". So "Ethereum H" is likely a transcription error for "EthereumJ". I will correct to **EthereumJ**.
    *   **Segment 17 (20:28 - 22:10):**
        *   SPEAKER_00: "Berkeley". "New York". "SPEAKER_00: Jim, go ahead."
    *   **Segment 18 (22:10 - 23:20):**
        *   SPEAKER_01: "November 19, 2013". "December 23rd of of December" -> **December 23rd**. "December 26th". "April or May 2014". "September 2014". "PI Ethereum" -> **cpp-ethereum**. "PI Fapp" -> **cpp-ethereum**. "GO. Ethereum" -> **Go Ethereum**. "bandits". "Gaff" -> **Gav**.
    *   **Segment 19 (23:20 - 24:30):**
        *   SPEAKER_00: "C client". "go Ethereum" -> **Go Ethereum**. "CPP Ethereum".
        *   SPEAKER_01: "Gabby" -> **Gav**.
    *   **Segment 20 (24:30 - 25:00):**
        *   SPEAKER_03: "Jim". "C client". "Go client".
    *   **Segment 21 (25:00 - 27:08):**
        *   SPEAKER_01: "CPP Ethereum". "go Ethereum" -> **Go Ethereum**. "test suites". "SOL C" -> **Solc**. "Absuron Mist" -> **AlethZero/Mist**? "Absuron" is likely a typo for a name. Maybe "Alex"? Or "AlethZero"? The text says "with Absuron Mist". I'll change to "with Mist". "Christian and Christoph".
    *   **Segment 22 (27:08 - 27:28):**
        *   SPEAKER_02: "SOL C" -> **Solc**. "C".
    *   **Segment 23 (27:28 - 28:37):**
        *   SPEAKER_01: "web 3 umbrella" -> **Web3 umbrella**. "F" (client) -> **cpp-ethereum**? No, "You had F and G". Probably referring to clients. "E" (executable). "Mix". "Aleph 0". "Aleph 1".
    *   **Segment 24 (28:40 - 29:10):**
        *   SPEAKER_01: "web3 umbrella". "Lib web based" -> **libweb3**? "web 3 base" -> **libweb3core**?
    *   **Segment 25 (29:10 - 31:31):**
        *   SPEAKER_00: "dev P2P" -> **devp2p**.
        *   SPEAKER_01: "Gab" -> **Gav**. "Web3 umbrella". "Lib, Ethereum, Lib web based, web 3 base". "SALSI" -> **Solc**. "Salsa" -> **Solc**.
    *   **Segment 26 (31:31 - 32:56):**
        *   SPEAKER_02: "brew".
        *   SPEAKER_01: "homebrew". "Salsa" -> **Solc**. "SOLS" -> **Solc**.
    *   **Segment 27 (32:56 - 35:10):**
        *   SPEAKER_01: "it" (IT).
        *   SPEAKER_00: "Zug". "ETH Zurich". "Amir and Charles". "Gavin" -> **Gav**. "Berlin". "Bay Area".
    *   **Segment 28 (35:10 - 37:53):**
        *   SPEAKER_01: "FDEV AG". "Amsterdam". "London". "Stefan" -> **Stefan George**? "George Hallam". "Ian Meikle". "FDEV". "Joe" -> **Joseph Lubin**?
    *   **Segment 29 (37:53 - 38:41):**
        *   SPEAKER_02: "Holon". "Mihai" -> **Mihai Alisie**. "Consensus" -> **ConsenSys**. "Ea" -> **EEA**. "Slocket" -> **Slock.it**.
    *   **Segment 30 (38:41 - 42:34):**
        *   SPEAKER_01: "Christoph Jens" -> **Christoph Jentzsch**? "Stefan Tual". "Left Terrace" -> **Lefteris Karapetsas**? "Slocket" -> **Slock.it**. "Defcon1" -> **Devcon1**. "pot of. It was like a petal. Like a pot." -> "Pot of tea". "tea". "Vitalik". "ds" -> **DAOs**. "Slock it Dao" -> **Slock.it DAO**. "Defcon 1" -> **Devcon 1**. "Slock it" -> **Slock.it**. "DOW" -> **DAO**. "A two" -> **Augur**? Or just "Augur". I'll leave as "Augur" if context fits. "Digex" -> **Digix**. "dai" -> **Dai**. "F" -> **ETH**. "Bitcoin Swiss".
    *   **Segment 31 (42:34 - 44:22):**
        *   SPEAKER_01: "Ethereum foundation". "Christian Wright Weisner" -> **Christian Reitwiessner**. "Dow Hub" -> **The DAO Hub**. "Fabian" -> **Fabian Vogelsteller**. "Gav backed out".
    *   **Segment 32 (44:22 - 47:01):**
        *   SPEAKER_01: "child dao" -> **child DAO**. "Dow wars" -> **DAO wars**. "top, the top now" -> **The DAO**. "white hat".
        *   SPEAKER_02: "soft fork". "hard fork".
    *   **Segment 33 (51:09 - 54:58):**
        *   SPEAKER_01: "Dell" -> **DAO**. "Laura Shin". "The Cryptopians".
    *   **Segment 34 (54:58 - 57:59):**
        *   SPEAKER_01: "Mount Gox". "E. Money" -> **Ether**. "F" -> **ETH**. "Air" -> **ETH**. "100F" -> **100% ETH**.
    *   **Segment 35 (58:32 - 01:06:14):**
        *   SPEAKER_01: "Ethereum Classic 1" -> **r/EthereumClassic**. "100F" -> **100% ETH**. "Joe" -> **Joseph Lubin**? "grayscale ETC fund". "Ethereum classic cooperative".
    *   **Segment 36 (01:06:19 - 01:07:31):**
        *   SPEAKER_02: "Dell" -> **DAO**. "Edcon" -> **Edcon**. "Anthony Busadi" -> **Anthony Lusardi** (He was the Director of ETC Cooperative). "Virgil" -> **Virgil Griffith**. "Bitmain". "Antpool".
    *   **Segment 37 (01:14:22 - 01:16:02):**
        *   SPEAKER_02: "Victor" -> SPEAKER_00 is Kieren. Transcript says "Victor, you were saying...". I will change "Victor" to **Kieran**.
        *   SPEAKER_00: "Cosmos", "filecoin" -> **Filecoin**, "Hedera", "Internet computer" -> **Internet Computer**, "Aptos", "Lido", "near" -> **NEAR**, "Optimism", "Arbitrum", "the graph" -> **The Graph**.
    *   **Segment 38 (01:16:02 - 01:17:55):**
        *   SPEAKER_01: "Coingecko" -> **CoinGecko**. "VC chains". "Antpool".
    *   **Segment 39 (01:17:55 - 01:18:35):**
        *   SPEAKER_00: "Vanity metrics".
        *   SPEAKER_02: "Tree clippings" -> **Tree saplings**? Transcript says "Can we call them tree clippings instead of...". I'll keep "tree clippings".
        *   SPEAKER_01: "20,000".
        *   SPEAKER_00: "Victor" -> **Kieran**.
    *   **Segment 40 (01:18:35 - End):**
        *   SPEAKER_02: "ea" -> **EEA**? "block apps".
        *   SPEAKER_03: "block apps".
        *   SPEAKER_02: "bobsonworld.com". "Ethereumclassic.org". "ECC" -> **ETC**?
        *   SPEAKER_00: "Cheers".

3.  **Detailed Edits & Formatting:**

    *   **Timestamps:** Keep original [MM:SS].
    *   **Paragraphs:** Merge consecutive speech. Blank line between speakers.
    *   **Capitalization:** Blockchain, Ethereum, Bitcoin, ETH, DAO, Smart Contract, Mainnet, Solidity, Solc, Geth, C++, Go, PyEthereum (cpp-ethereum), Parity, Slock.it, Devcon, EEA, ConsenSys, ETC, US/USD, etc.
    *   **Names:**
        *   Bob Summerwell -> Bob Summerwill
        *   Anthony Diorio -> Anthony Di Iorio
        *   Kieran -> Kieren
        *   Jim -> Jim (Zhang? Or Kieren James-Lubin? Wait, Kieren is SPEAKER_00. SPEAKER_03 is "Jim". Transcript says "Jim Kieran". Likely "Jim [Zhang] and Kieren". But I will leave "Jim". Wait, earlier SPEAKER_02 says "Jim Kieran". SPEAKER_00 is Kieren. SPEAKER_03 is Jim. So "Jim and Kieren". I'll fix "Jim Kieran" to "Jim and Kieren" if it implies two people. "When did we get quarter 2014. Yeah, we were." It seems Jim is answering. I'll just clean the name to "Kieren" where appropriate.
        *   "Karen" -> Kieren.
        *   "Victor" -> Kieren.
        *   "Bing" -> Ming (Context: "Ming's been sacked", "to my mind, Bing was terrible").
        *   "Christian Wright Weisner" -> Christian Reitwiessner.
        *   "Anthony Busadi" -> Anthony Lusardi (ETC Director). *Correction*: I'll check if "Busadi" is close enough to "Di Iorio" (Busadi vs Di Iorio). No. It's likely Lusardi. I'll use Anthony Lusardi.
        *   "Fabian" -> Fabian Vogelsteller.
        *   "Barry Silver" -> Barry Silbert.
        *   "Virgil" -> Virgil Griffith.
        *   "Laura" -> Laura Shin.
        *   "Christoph Jens" -> Christoph Jentzsch.
        *   "Stefan Tual".
        *   "Left Terrace" -> Lefteris.
        *   "Gaff" -> Gav.
        *   "PI Ethereum" -> cpp-ethereum / C++ Ethereum.
        *   "Ming" -> Ming Chan.
        *   "Hudson" -> Hudson Jameson.

4.  **Refining the Text (Self-Correction during drafting):**
    *   *Timestamp check:* Input is [00:00], [00:57], [03:57], etc. Output must match.
    *   *Word count check:* Input is roughly ~5000 words? No, let's estimate. Input is quite long. I need to keep it long. Do not summarize.
    *   *Formatting:*
        **[00:00] SPEAKER_00:** Alrighty. Well, thanks everyone for coming back. We've done a couple of videos...
    *   *Specific Phrase Fixes:*
        *   "mainlet launch" -> **mainnet launch**.
        *   "seaport" -> "Sierra"? Or just remove? "15 years of seaport, 15 years of C plus plus". "Seaport" is a game engine? No, maybe "Software"? "15 years of C++". I'll assume "seaport" is an error and remove it or replace with "software" if it makes sense. Actually, maybe "15 years of [game dev], 15 years of C++". "Seaport" is unintelligible. I'll remove it. "So like 15 years of C++".
        *   "Bing, there's some money" -> "bing" -> "ching"? "cha-ching"? I'll write "cha-ching".
        *   "Gaff" -> **Gav**.
        *   "PI Ethereum" -> **cpp-ethereum** (Context: "as it was CPP Ethereum").
        *   "SALSI" / "Salsa" -> **Solc**.
        *   "A two" -> **Augur**.
        *   "Digex" -> **Digix**.
        *   "Dow" -> **DAO**.
        *   "Dell" -> **DAO**.
        *   "Air" -> **ETH**.
        *   "Bobsonworld" -> **bobsummerwill.com**? Transcript says "bobsonworld". I'll keep "bobsonworld" or check. Bob's site is bobsummerwill.com. But he said "bobsonworld". I'll keep what he said, maybe capitalize "Bobsonworld".
        *   "Ethereumclassic.org".
        *   "ECC" -> **ETC Cooperative**?
        *   "Anthony D Onofrio" -> "Anthony D'Onofrio".
        *   "Vitalik".
        *   "Bitcoin".
        *   "Zug".
        *   "Amir and Charles".
        *   "FDEV".
        *   "Stefan and George Hallam".
        *   "Ian Meikle".
        *   "Mihai".
        *   "ConsenSys" (Transcript: "Consensus").
        *   "Holon".
        *   "Christoph Jentzsch".
        *   "Lefteris".
        *   "Devcon 1".
        *   "Slock.it".
        *   "Digix".
        *   "Christian Reitwiessner".
        *   "Fabian Vogelsteller".
        *   "Laura Shin".
        *   "Joseph Lubin".
        *   "Virgil Griffith".
        *   "Anthony Lusardi".
        *   "Barry Silbert".
        *   "Grayscale".
        *   "Bitmain".
        *   "Antpool".
        *   "CoinGecko".
        *   "Cosmos", "Filecoin", "Hedera", "Internet Computer", "Aptos", "Lido", "NEAR", "Optimism", "Arbitrum", "The Graph".
        *   "Jim" (SPEAKER_03).
        *   "Karen" -> **Kieren**.
        *   "Victor" -> **Kieren**.

    *   *Technical/Formatting cleanup:*
        *   "SPEAKER_01: So, yeah. Hi. You know, thanks so much for the invite. You know, like I said to you guys, you know, I, I love those first two videos, you know, I, I love this history and it was great to, you know, both hear that and, and have, you know, a slightly different perspective as well." -> Remove excessive "you know"s. "So, yeah. Hi. Thanks so much for the invite. Like I said to you guys, I love those first two videos. I love this history and it was great to both hear that and have a slightly different perspective as well."
        *   "SPEAKER_02: Can we call them tree clippings instead of..." -> Keep the joke.
        *   "SPEAKER_02: EA" -> **EEA** (Enterprise Ethereum Alliance).
        *   "SPEAKER_03: Block apps" -> **BlockApps**.
        *   "SPEAKER_02: ECC" -> **ETC** (Context: "landing page for ECC" - he probably means ETC Cooperative or ETC). He said "ECC". I'll keep it or change to "ETC" if clear. He works for the Ethereum Classic Cooperative.
        *   "SPEAKER_00: We've told him plenty of ours." -> Keep.

    *   *Merged Paragraphs:*
        *   Ensure timestamps are only at the start of the first paragraph.
        *   If a speaker has a long monologue, break into paragraphs for readability.

5.  **Final Review of the Output Text:**
    *   Check "Bob Summerwill".
    *   Check "Kieren".
    *   Check "Anthony Di Iorio".
    *   Check "Gav".
    *   Check "Solc".
    *   Check "DAO".
    *   Check "Slock.it".
    *   Check "Mainnet".
    *   Check "C++".
    *   Check "Bitcoin".
    *   Check "Ethereum".
    *   Check "Web3".
    *   Check "Devcon".
    *   Check "ConsenSys".
    *   Check "ETC".

    *   *Special Cases:*
        *   "mainlet" -> mainnet.
        *   "seaport" -> removed.
        *   "Bing" -> Ming (Contextually: "Bing was terrible", previous "Ming's been sacked").
        *   "A two" -> Augur.
        *   "Dow" -> DAO.
        *   "Dell" -> DAO.
        *   "F" -> ETH.
        *   "100F" -> 100% ETH.
        *   "Air" -> ETH.
        *   "Jim Kieran" -> Jim and Kieren.
        *   "Karen" -> Kieren.
        *   "Victor" -> Kieren.
        *   "Anthony Busadi" -> Anthony Lusardi.
        *   "Christian Wright Weisner" -> Christian Reitwiessner.
        *   "Christoph Jens" -> Christoph Jentzsch.
        *   "Left Terrace" -> Lefteris.
        *   "Barry Silver" -> Barry Silbert.
        *   "Ming" -> Ming (Capitalized).
        *   "Stefan" -> Stefan George (maybe just Stefan). "George Hallam".
        *   "Ian Meikle".
        *   "Joe" -> Joseph Lubin.
        *   "Virgil" -> Virgil Griffith.
        *   "PI Fapp" -> cpp-ethereum.
        *   "Salsa" / "SALSI" -> Solc.

Let's assemble.**[00:00] SPEAKER_00:** Alrighty. Well, thanks everyone for coming back. We've done a couple of videos, so we've done two on the early days of Ethereum and I actually did another video on Identity following that, which you can check out on my channel. And in the process we're excited to reconnect with Bob Summerwill. So Bob will ask to introduce himself in a second, but he actually went quite in depth, you know, in reaction to the videos and helping to work together to patch up the whole story from our collective memory on the early days of Ethereum. Wrote a long blog post that you should check out and we'll link in the notes and we asked him to join us here today to kind of dig more into the story and also just generally catch up. So with that, maybe I'll hand it to Bob to do a quick intro and we can just kind of get into it.

**[00:57] SPEAKER_01:** So, yeah. Hi. You know, thanks so much for the invite. You know, like I said to you guys, you know, I love those first two videos, you know, I, I love this history and it was great to, you know, both hear that and, and have, you know, a slightly different perspective as well. You know, our paths have overlapped in some ways and haven't in others. So, you know, there are a few things that came up which I, you know, I, I wasn't myself aware of. I mean just for, just for everyone's background about, about me and who I am. So I got interested in blockchain in 2014, but it was 2015 where I really like kind of jumped in and that happened because I was, I was working in Toronto, I had a six month contract and was working in Toronto around the same time that Ethereum was, was doing a mainnet launch. And I'd actually met Vitalik for the first time in 2014, but you know, just kind of following along a little bit, not actually doing anything. But then moving to Toronto, it's just like orders of magnitude more stuff going on and you know, meetups and you know, Anthony Di Iorio's Bitcoin Decentral co-working space and everything. So I got like really very addicted through that year and it was like, right, I can't not get involved, right? It's like, it's like you're there at the birth of the web or whatever and you've, you know, you, you've met Tim Berners Lee and he's about to like go live on the web and it's like, you know, how can you not like want to get involved? So I just started sort of volunteering and helping. My background prior to that was in the games industry. So like 15 years of C++.

So I was like, well, you know, I can, I can do something with, with C++, Ethereum. And I was really into mobile and wearables. So my first thing I set myself is, you know, can I get Ethereum running on my smartwatch? You know, could you get a smartwatch and go around it, like bing, there's some money, you know, that'd be really cool. So. So yeah, I just started doing stuff on there that was about the time that Gav was parting company with, with the foundation as well. So there was kind of a, a dearth of people on that team. So, you know, like that period, I ended up being like, I think the only person in the world who was actually helping on that. Like, you know, no companies, no, no nobody was helping. And then I ended up getting hired into the foundation in early 2016. And yeah, I've been involved on Ethereum Enterprise, Ethereum Hyperledger, then more recently Ethereum Classic for nearly a decade now.

**[03:57] SPEAKER_02:** Yeah, Bob, well, and to be open to everyone, like world friends, and we're happy to have you as our first guest who's on this thing. But also you are like, you know, the Nelson Mandela of the Ethereum ecosystem. You're friends with everyone, you know, you've been in everywhere. So it's great to have your perspective on things.

**[04:23] SPEAKER_01:** Thank you.

**[04:25] SPEAKER_02:** So, and as Kieren has mentioned, for anyone who hasn't seen Bob's blog post, it's notionally a blog post, almost a full novel, probably a novella size. It has pictures of a lot of the people we're talking about. You dug up so much content out of there. Were those your personal pictures? It's just stuff.

**[04:46] SPEAKER_01:** Yeah, yeah, just stuff. I, I had. I mean, another thing here is there's a couple of articles on my own blog from earlier that I linked into there as well, which was there's one called Ethereum Foundation People and one called Ethereum Foundation Timeline. So I made those in late 2017, early 2018, because there was no canonical history of any of this. Yeah, it's like, how did Ethereum start? I mean, it's in people's heads. It's all secondhand stories that you hear from people that were around. But, you know, it's like, what's true, what isn't? Because I think especially on that like, foundation side, it was such a mess. Right. Just like all different people weren't getting on, blowing up kind of like parity versus the foundation and Charles, you know, and like, God, what. You know, so it, I think some people had almost taken this position of like that we don't talk about that. Right, right. Because anything I say, like it's going to offend somebody else. So just la, la, la. It doesn't matter that, you know. But, but yeah, so I started gathering that list of, well, you know, who were the people that were around in the pre foundation days and in that. And so, yeah, I've got this, got this one page, this people page, which I think is really cool. Just, it's got. So that's basically from 2013 through to early 2018, identifying anyone that I could. That was involved with Ethereum, Pre foundation or who worked for the foundation in those early years. And one of the things that's really great there is DEVCON 0, which happened in, I think October 2014. So that was the very first DEVCON. But it was a closed event. That wasn't a public event.

**[06:50] SPEAKER_02:** Yeah.

**[06:51] SPEAKER_01:** And it was, it was foundation people at that time. But there were also, you know, some other key community sort of people there as well. And they did this one thing at the start that was introductions. So there's this video that's about 15 or 20 minutes long of everybody, like, hi, I'm Vlad. I'm here doing, you know, proof of stake research. Just see these, these, you know, so young, so many people that, you know, like really early 20s.

**[07:22] SPEAKER_02:** Yeah.

**[07:22] SPEAKER_01:** You know, and turning up and it's like that's, you know, that's so. And so. Right. And, and some of these people as well, you know, they, they're not involved anymore. You know, they're, they're sort of like footnotes in history. But, but, but you have that record. And so, yeah, that list of people, I got all of that together. And the reason that that came about was in late 2017, I got a message from Laura Shin saying, hey, I hear Ming's been sacked at the Foundation. Like, do you know anything about this? And I said, well, no, I don't, but it wouldn't surprise me. But you know, basically it would be like Vitalik or maybe Hudson could tell you. But like nobody, nobody else could tell you anyway. And, you know, it sort of came out well, yeah, she's, you know, she's not been sacked, but she's agreed to leave.

**[08:17] SPEAKER_02:** Right.

**[08:17] SPEAKER_01:** And then it's like, well, what's, what's next? So I contacted Vitalik and said, you know, hey, is there anything I can do to help? You know, what can I do, you know, and he said, well, the one thing you can do is can you, like, try and talk to people and work out, like, you know, what would good look, like, what do people think a good Ethereum foundation would look like? And so that started my sort of adventure, really, of like, right, I'm gonna go and talk to all the founders, all the other people, and try and work out like, you know, what, what. And then that just turned into really mind, you know, a thought experiment on my side of like, okay, so, you know, to my mind, Ming was terrible. So how did she get hired? Like, what was going on? You know, whatever, two and a half years back, that, that looked like a good option, you know, like, what. How. How did it work before, you know, like, what. How did the foundation come about? And like, what. What were the group of leaders and like, what were all the dynamics between all of these people? So, yeah, I went down quite a rabbit hole there. And that's, that was the, the sort of the genesis for that information gathering. And I learned a lot. And that information as well, I gave to Laura and to the other two authors that were doing their Ethereum books is kind of like, right, there is no canonical, but this is kind of what I found, which is maybe like the best information that there was at that time.

**[09:47] SPEAKER_02:** Yeah, well, and also it's to your point is that I think generally people have sort of survivorship bias about, you know, like, everything works smooth, but innovation is messy. You know, it's messy and it's like, you know, there are a million and one different paths that things could have went to. And we just want to kind of acknowledge all that, like, you know, like, given where the ecosystem is today. And even though, you know, it's amazing to me that so many people know about it, that later I spent, we all spent the first years trying to get anyone to listen to us talk about blockchain, and no one, you know, everyone just glaze over. Right. So it's, it's just kind of nice to take that retrospective view at this point. Oh, went a little bit far. We'll just go with it.

**[10:37] SPEAKER_01:** One of the things that I, I know that Vitalik said, and again, it was maybe in Laura Shin's book was like the, the founding of Ethereum was very atypical because it was essentially like, here's. Here's a white paper out to a bunch of random people who may be interested, and it's like basically like, first people that turn up, right? You're the founders, like, you know, a number of them. They'd, you know, they'd not even met each other before that. You know, not really a lot of knowledge. And so, yeah, like, there were lots of interpersonal things that just didn't work at all. It's just like. No, like founding a company. And I'm sure you guys, you know, have this experience yourself. Right. You want to start with people that you kind of know and trust a bit because you know that you're going through the fire together. So, you know, you better have some stickability with you and, you know, common alignment or at least knowing that you've got good communication to go through those bad times. Right. You know that, you know that you can work it out.

**[11:56] SPEAKER_02:** Yeah.

**[11:57] SPEAKER_01:** And what seems to happen on Ethereum is absolutely the polar opposite of that. It's just random bunch of people who were there, didn't really know each other. Like, make that commitment before you even know what you're even doing. Right.

**[12:09] SPEAKER_02:** Yeah.

**[12:10] SPEAKER_01:** And so that didn't work so great.

**[12:13] SPEAKER_02:** And I think.

**[12:14] SPEAKER_00:** Also, let me. Actually, I wanted to ask about that. I'm also just looking at the list of the Ethereum foundation people, which is remarkably long for the type of initiative it was. You know, we talk about this because we're a management team and we're trying to get people to focus on particular goals and things our company wants to do and such. Do you think there is any benefit to this level of. You could call it disorganization or just, you know, I kind of think if there were a benefit and it wasn't merely just an inefficient and painful process that Ethereum succeeded in spite of, it's kind of. It embodied the ethos and it let people like Vitalik put the idea out there, and then people fought for its destiny, like Ethereum existed, and then they wanted to be part of taking it, too. And he saw just the clients and all that, too. Sorry, Jim, go ahead.

**[13:09] SPEAKER_03:** I was gonna say it kind of worked like a blockchain works, in fact.

**[13:12] SPEAKER_02:** Yeah.

**[13:12] SPEAKER_03:** Lots of random people coming together with some underlying principle to organize things and then they fight it out.

**[13:18] SPEAKER_02:** But what's that law that organization technology reflects the organization? So, yeah, something like that. Like. Yes. Sorry.

**[13:30] SPEAKER_01:** Yeah, I mean, I guess in general. Yes. You know, having that, like, frothing, emergent, like, stuff is. Is good. I think where it was really screwed, though, was to do with money and. And, you know, the ICO funding. Right. That it's basically like, okay, here we're doing the thing, and here the money is all actually in this organizational group and the people in that group are being funded, you know, are in this privileged position. It's something which Brian Behlendorf said to me in later years was it's sort of like the original sin of Ethereum is if you want to have that kind of collaboration. So, you know, whatever stuff like the EEA and Hyperledger or even just, you know, the rather looser protocol development around Ethereum, you don't want to pay one team and not the others.

**[14:27] SPEAKER_02:** Right?

**[14:27] SPEAKER_01:** Because that just screws that battlefield. So you have this situation, for example, where you know, you've got the C client and you've got a Gav. You know, you did have the Python client as well, so you had that good triangulation, but it was essentially like the, the funded ones were C and go. And then they had the, the money crisis of like, oh my God, is this thing even going to happen? Right, We've got cut scope, C is gone, Gav ends up going out of the way. And then you had parity, you know, having one of the major clients, but without funding. So it's like Geth. Oh, Geth. That's the, you know, that's the, it's not like the official client, but it is the official client. So all that sort of like separation of implementation versus specification and you know, in that free market around that was really skewed because the money was with Gav and Geth were in the foundation and they've got, you know, Vitalik's kind of blessing and everything. So I think that's where things were great because you did have the diversity, but it wasn't fair diversity. And I think if you look at what's happening now on the consensus clients for, I was going to say Ethereum 2.0, it's not called Ethereum 2.0 anymore. But you know, the separation that you have with those execution clients and consensus clients, none of those consensus clients are made by the foundation. The foundation doesn't have client teams. They do funding like they got the grants and I think all of those teams are going to be grant recipients. So that's kind of centralization in a way, but it is an even playing field in terms of the development. Right, because you've got an evenness of funding. And that wasn't the case, you know, originally for Ethereum. And I think that that made a lot of bitterness as well, because it's like, well, why have you guys got the money? Like we're, we're making another one as well and. Or you Know, or other parts of the ecosystem. Like there wasn't a grants program for a number of years. Yeah, between about 2015 and 2018 there wasn't even a grants program. You know, you got the foundation sitting on hundreds of millions of dollars and teams couldn't even get funded for doing anything. So, so yeah, I think the diversity is good, but the money was bad.

**[17:03] SPEAKER_00:** Interesting. Yeah, I, I think. Right, okay, that's a, it's a good strong point. So if you compare to like a Bitcoin, which I know less about the history of the development of Bitcoin, but it was kind of similar. There was less of a. There was no pre-mine and no token presale. And so the people who were in it were in it for general interest and it was really sincerely an even playing field. And I would argue, you know, and in some ways Ethereum has made bigger strides than Bitcoin, especially since let's say 2015. Some of the value prop of Bitcoin is that it never changes and that's kind of part of why it holds its value in some way. But it's I think been stifled a little bit for that reason. I think it's pretty hard probably to make step function positive changes in a fully decentralized manner.

**[18:07] SPEAKER_01:** Another major difference there, talking about clients is it was a very deliberate decision right on Ethereum to, to separate the specification from the clients and that there were multiple clients from day one. I, I see if I can find my Twitter thread. I was finding these the other day. I was finding the first commits for, for cpp-ethereum. And they were all, I think they were all November or December, I think they were all 2013, not even 2014 for those three. And then EthereumJ looked like it started in about April I think. But you know.

**[18:52] SPEAKER_02:** Yeah, Jim Kieren, you guys started EthereumJ in 2014.

**[18:56] SPEAKER_00:** Yeah, we were much later.

**[18:58] SPEAKER_02:** We were.

**[19:01] SPEAKER_03:** When did we get quarter 2014.

**[19:03] SPEAKER_00:** Yeah, that's right.

**[19:04] SPEAKER_02:** That's about right.

**[19:07] SPEAKER_00:** And I had worked on Ethereum just in the summer. So starting kind of maybe June 2014, I got to know the project pretty well and then I gone back to Berkeley. I was in New York for the summer and met Jim September, October, something like that. And we started work more or less right away. More Jim than me. But so yeah, so there was a big time delay on, on our side and yeah, I think. Okay, yeah, Bob, it's an interesting point, right. I think probably they could have. There was some, some real mismanagement at different times, both with the running out of funds, not doing any hedging. And then later, I guess I agree that it could have just been more fair and open feeling and that would have alienated fewer people and it could have even just been bigger than it is today. Obviously we're talking about a smashing success here, but it's sort of the idea and the community was so powerful that it, you know, this definitely succeeded in, in spite of aspect, I think there was value still in this. Like throw it out there, get people to fight over it, but probably overcorrected. And lots of these people also just went and started their own thing.

**[20:28] SPEAKER_01:** I mean the other thing is right at the start there, it's like, well, the people that doing it, that was the whole world, right. You know, that was everything. Right. Was several months. I mean, all of that early work on the clients actually was before the foundation even existed. That was actually unfunded.

**[20:44] SPEAKER_02:** Yeah.

**[20:46] SPEAKER_01:** Because I'm looking at the dates. So the. The white paper came out in November 2013. Sorry, 2013. cpp-ethereum was started on November 19, 2013. GAV actually was in contact with Vitalik on that same day. CPP Ethereum started four days later, 23rd of of December. Obviously some over Christmas hacking on these things going on and then Go Ethereum was December 26th. So just three further days. The foundation got formed I think in May, April or May 2014, but the crowd sale didn't conclude until September 2014. So you'd actually got about nine months worth of development on all of these three clients that was actually unfunded. So, you know, I think, I think that unfairness kind of came in a little bit later. I think for that phase it was like nobody got funded. Oh, sorry. You know, nobody got funded though there was the retrospective payback. Right. You know, when, when the crowd sale had gone through, you had, you know, money for early contributors, which I think, I think that was nearly 10%.

**[22:10] SPEAKER_02:** Yeah.

**[22:10] SPEAKER_01:** For like 100, 120 people. Like some people made out like absolute bandits for, for those early months. But then, yeah, following that, there was hiring of actual, you know, staff onto those teams. And that I think is when it became kind of uneven because you already had EthereumJ for a number of months there and that, you know, that. That never got funded and then you. And then you guys starting whenever you were starting. So yeah, it kind of became uneven I think at that point. And, and probably the worst of it of all was for Parity you know, when, when that team spun out and you basically did have a major, you know, rapidly load bearing client and it was just, you know, unfunded. Especially in with Gab who was, you know, had been the CTO and wrote the yellow paper and had the first working client and you know, all of the value he delivered and then it's like, right, sorry, you're out and you're not getting any money, you know.

**[23:20] SPEAKER_00:** Yes.

**[23:21] SPEAKER_02:** Do you.

**[23:23] SPEAKER_00:** So my memory around the C client was that there were funds to do a security audit for two clients, but one at a time and it was tight. Right. And so they did Go Ethereum first and I think they did actually do the security audit on CPP Ethereum, but I'm not quite sure they did.

**[23:47] SPEAKER_01:** You know, maybe there'd been an intention to do that, but then the money. Right. Ran out before it happened. I mean, my understanding in terms of uptake as well is CPP Ethereum was like working first but then Go Ethereum just like caught up and overtook it like really fast. So when they were making those decisions on cutting funding, which would have been mid-2015, it's like, hey Gav, you're the CTO, but it's your code base that's got a copy. And then that's what happened.

**[24:27] SPEAKER_00:** And I mean, I was sort of.

**[24:30] SPEAKER_03:** Building the various clients quite a bit because I was trying to integrate with.

**[24:34] SPEAKER_02:** Them at the time.

**[24:36] SPEAKER_03:** And my memory was that the C client had all the newest stuff in it first. So if I wanted to see something first I would go there. But the Go client was more stable like because I think because they were putting so much stuff into the C client, it was often in an unstable situation. And so I would typically kind of go to C first to see the new stuff, but if it wasn't building that day, I would run over to Go and try it out.

**[25:00] SPEAKER_01:** Yeah, I mean, and that would make complete sense because the other thing to know with the C client is that was where the test suites were done. You know, like all the tests were generated out of that code base. So as you say, all of the protocol changes or whatever would happen there first. Then you do the test generation through that and then those were the tests for, for, for other clients. So even when CPP Ethereum as a client like died, it didn't die within that testing suite for years. It's like, right, even though nobody's actually like running this or using it on Mainnet or anything, you know, we've got to keep, we've got to keep maintaining that One, because that's where the tests are coming from. So yeah, that, that front line was really like leading across Solidity, the tests and CPP Ethereum, you know, all of those actually were bundled together into a single workspace as well with all of the GUI apps, like with Mix and Aleph Zero, Alice One, Aleph Five. Like it took 24 hours to build the bloody thing. But that will be because it was all around Gav. Right. You know, Gav was leading all of that. You know, he was, he was building that client, he was writing the yellow paper, he was, you know, working there with, with, with Christian and, and Christoph on that specification and testing stuff like that. You know, all of that was, was there and then on Geth on Jeff's side, you know, but, you know, just, just doing Geth. Right. It wasn't, wasn't a broader thing. And, and that. That Geth team were working closer with Mist, you know, with Mist, like for a, for a good while. I don't think CPP Ethereum even worked with Mist. You know, it's like all these groups not really talking to each other. But yeah, that would make sense. Like a lot of it was Gav, LED.

**[27:08] SPEAKER_02:** And wait, SOLC, the Solidity compiler, that was part of that C group too. That makes sense because it was written.

**[27:18] SPEAKER_01:** In C. But yeah, it was all under web3 umbrella.

**[27:24] SPEAKER_00:** I remember web3 umbrella.

**[27:26] SPEAKER_02:** I remember web3 umbrella. Yes.

**[27:28] SPEAKER_01:** So yeah, web3 umbrella was a git repo with sub repos for, you know, for, for E. It was called E, just called E, the executable. So you had F and G. But yeah, you had F, you had Solc, you had Mix, which was the original ide. Cute, um, client. You had Aleph 0, which was the GUI miner.

**[28:03] SPEAKER_02:** Yeah, that's right.

**[28:04] SPEAKER_01:** So it's like right here, here's a go, press the Mine button and you know, and then you had Aleph 1, which was sort of, I guess it was like kind of like a GUI client runner thing. I can't remember the exact scope, but. But it was sort of like, right, you're running a node, but you've kind of got a GUI on it and I, I can't remember what it had, but you know, whatever logs going by and I guess you could like fiddle with settings or whatever. But yeah, all of that was in Web3 umbrella.

**[28:37] SPEAKER_02:** That's a lot.

**[28:40] SPEAKER_01:** Yeah. And all of the dependent. They were all really test. And the tests as well. Right. But then they were all really codependent. I mean, when I started one of the first things I did was like, what are the dependencies on all of these things? Like, what is all of this stuff? Because you had like libraries with it as well. It's like Lib, Ethereum, Lib web based, web3 base.

**[29:02] SPEAKER_00:** Yeah, devp2P. There were documentation all over the place.

**[29:10] SPEAKER_01:** I mean, I think, you know, I think what had happened there that Gab was sort of trying to do, but it never came to fruition and then he left was. It's like, right, let's try and make this modular. Right, we're going to try and do a modular thing and pull apart the networking and the database and this, that and the other. But it was kind, it was pulled apart into separate repos before there were actually stable interfaces between any of these. So you had to use the latest stuff of anything anyway. Like you couldn't mix and match because there was no versioning, there was no interface discipline on any of it. You had to use all the latest ones together. But then it was all split into these separate repos. So it's like, right, you're making a change on one of them and then whatever, updating the sub modules and like, like that wasn't atomic, it was, it was just a big old mess. So yeah, one of the first things I did was like, you know, work out in Infer a dependency diagram, map a path to pulling it all back into a, into a monolithic workspace, doing like automated builds that we somehow didn't have and specifically decoupling Solc and the tests from the client. Right, right. So for Solc, for example, because it was tied in with this full workspace, it was literally a 24 hour build. It was like compiling chromium from source twice, compiling Qt, all of this stuff. So just to get, you know. And there weren't binaries available for Solc either. Like you had to build all of this stuff yourself to be able to like compile, you know, a smart contract to do anything, you have to do all of that. So I remember, you know, after all that decomposition I, you know, I got it so you could just do Solc and you know, that was a quick build. And then I did like homebrew and it's like, so you could do like brew, install Solc and it did it in like five seconds. And that was like, oh my God, this is amazing. But yeah, it was, yeah, it was a bit of a mess.

**[31:31] SPEAKER_02:** I do remember waiting like, you know, many times, trying to build things, coming back, looking at it, saying like, this can't be like, my machine's got to be broken because like, it can't be this long. Can't be like eight hours. Like nothing I could imagine would take more than eight hours to do, you know, but you're right, it just like.

**[31:52] SPEAKER_01:** You know, talking about that, you know, creative brew of lots of different people and uncoordinated and everything. One of my first observations on joining the. The foundation is these people seem allergic to professionalism because that seems, you know, in an organized way. Well, you're one of the baddies, you know, you're the status quo. You're trying to subvert it and take it over. You know, things as simple as like, like, you know, have we got like technical leads that actually lead? You know, have, have we got any project management? Have we got any IT. Have we got anything? And it's like, no, it's just like a jumble of people doing stuff. And it's like, well, how. How on earth can you develop software in such a chaotic environment? But that was kind of the vibe as well. That was seen as a good thing, you know, because it's. Because that's a defensive cultural thing. Right. You know, we don't, we don't want this to be a Silicon Valley thing.

**[32:56] SPEAKER_02:** Yeah.

**[32:56] SPEAKER_00:** You know, I think I just have a comment. It's interesting and maybe I commented on this in one of the other videos, one of these rare big software projects that did not very much come from the United States. It's Canada, it's different parts of Europe. And one of those confusing things about, to your point about who got paid for the clients on the foundation. I think I remember there being a deal struck with, with Zug, the canton basically around it. There's tax stuff and all that sort of thing. But they also sort of intended to hire and operate locally. People would either move there or they'd hire ETH Zurich grads or whatever. And I don't know the details specifically, but I think that didn't quite end up happening that way and sort of as a surprise. And I saw some of this firsthand at the meeting in which, you know, Amir and Charles were, you know, sent on their way. The. The client team set up in their own countries. And that was like a bit of a script flip. Like Gavin wanted to be in Berlin because the, I guess the devs were good and expensive and they'd be like living there, you know, inexpensive. Excuse me. And yeah, I think it's just, you know, you would. Running my own business, you would never make such a decision. In such a flip manner where like overnight we're like, oh, we're doing a different country, you know. But they, that was kind of a regular occurrence to some extent. Major things changing, you know, as part of how the foundation plus sort of operated that, that I saw. And again, it didn't seem to hurt, you know, quite as much as you might expect. But. Yeah, but I think, you know, you, you had to have, you were lucky in how people works, how excited people were about the project, that it survived all of this. And again, from our side, you know, we're sitting in the Bay Area at that time and we're like, why, why do they keep doing all of these things? Like they're trying to build a thousand things and it's hard to build one thing.

**[35:10] SPEAKER_01:** Yeah, I mean, so there were separate legal entities for those as well. Right. So you have FDEV AG in, in, in, in Berlin. And then, you know, there was, then there was an Amsterdam thing for, for the Geth team. You had the London stuff as well, which was mainly communications sort of stuff, you know, with, with Stefan and George Hallam, Ian Meikle and one other person who. I forget. But you know, you sort of talk about, you know, these people working for the Ethereum foundation, like, but it's, it was always woollier than that. So yeah, you did have the, this, the stick home in, in Zug, but most people, even if they're working full time, they weren't actually working for that, you know. So when I had my contract, it was with the, the for profit FDEV in Berlin. That was who I was actually working for. And then they were funded by the foundation and an FDEV in general. That was another big split that there was, right, was you got the foundation, but then you had FD that was like the kind of umbrella group for that, that GAV was leading essentially. So I think the, the Amsterdam thing like rolled into Berlin. I think that was all sort of FDEV side. And that in itself was, you know, a huge item of conflict. I know again, in Laura's book, I think Joe was talking about that, right. Was, was that GAV kind of like wanted a big chunk of money. It's like, right, you know, the funds are there from the crowd sale now, so, you know, give them all to us. Right. And it's like, I don't know that we want to give you all the funds like, you know, as you go. But that, you know, that was typical of that period is just a mess of complexity and interpersonal things and organizational complexity. And with that, with that Swiss people thing. So my understanding on that was that was like a, a main motivation for like getting renting that spaceship building. Right. Was the intention was that there were going to be a load of people there. Like maybe it was, I think tests testing was one of the ones I heard was maybe a goal. There is like right, we're going to get a load of Swiss people to, to test things. And there's also like Mihai with his Holon ideas, Holon of these co working spacey things around the world.

**[37:53] SPEAKER_02:** And when and also to make it a little bit more woolier like you know, same time like very shortly. ConsenSys emerged out of that too and they were doing a bunch of work. You know, we were working, you know, we were technically working under ConsenSys for you know, the first low parts of it too. And all of that was like in the mix, you know, like everywhere. So I want to jump ahead a bit because we have you as an ETC expert and in our last one we had a lot of questions around what we've remembered from Slock.it and the DAO hack. So maybe you could walk us through that and you know how ETC emerged out of that. That part was a little bit vague to us because we didn't, we didn't follow much on, you know, how those pieces all came together.

**[38:41] SPEAKER_01:** Yeah. So I mean one of the groups or companies that came out of this kind of like shrinking of the foundation was that on that C team that got most of the cuts, a good chunk of those people went to, just went straight to Parity and just like carried on with that new client. But Christoph Jentzsch, who had been working, leading that testing effort that we're just talking about those same tests, he and Stefan Tual who had been community communication, communications lead, you know, that's sort of community stuff and Lefteris, who'd also been on C team, those three went off and formed a company called Slock.it. So Slock.it being smart locks, just the idea that you, you know, whatever, if you're doing an Airbnb or something that you can, you know, that you could have a smart lock and that you could go and do your contract with someone for, for the rental and then that could be, you know, enabling something on the lot that's checking a, an Oracle or a non chain thing and, and so on. And so that, that was the, the, their, their product area at Devcon 1 they did like an on stage demo that was, it was like a pot of. It was like a petal. Like a pot.

**[40:15] SPEAKER_02:** Yeah, I remember that like doing A.

**[40:17] SPEAKER_01:** Transaction that turned it on to make a cup of tea. Yeah, like that. That was the. The onstage demo. But what seemed to happen there was like, they didn't want to do an ICO. They wanted it to be fairer, I guess, because around that era, the more later, you know, you saw lots of cash grab ICOs, and it's like, right, here's all the money up front. You know, we're not going deliver. What are you gonna do?

**[40:47] SPEAKER_02:** Right.

**[40:48] SPEAKER_01:** So. So they didn't want to do that, you know, because they were very genuine people who come out of the foundation and were, you know, kind of, you know, ideologically driven. So Vitalik had written stuff about DAOs. Right. You know, I think they were mentioned in the white paper even. And it's like, well, maybe we can make a DAO. So. And I think that was just Slock.it DAO, really originally. And it was like, right, we're going to have a DAO. The money is going to go into there, but then it's only going to get released to us as we deliver milestones. So it's kind of like this separation of like, right, the DAO is where the money is and that's controlled by the token holders. Slock.it as a company is a service provider into that. But we're a sackable service provider and we're only going to get paid as we go through the milestones. So it's like, oh, that's really interesting. Yeah. And I. To my understanding, that's what was presented at Devcon 1.

**[41:54] SPEAKER_02:** Okay.

**[41:55] SPEAKER_01:** I remember was like, hey, we're Slock.it. This is what we're doing, and we're going to do a DAO with it. And it's like, oh, cool. But then they kept working on that, that DAO stuff after Devcon 1, and it just seemed to like, warp into, well, we've made like a DAO framework. It's a DAO library, you know, because we want other people to be able to do this as well. But then that sort of turned into, well, actually, how about it isn't just us. How about it could be anything. Like, anyone could have a service provider. You could propose any. Anything into it. And then it became The DAO.

**[42:32] SPEAKER_02:** Okay.

**[42:34] SPEAKER_01:** And it wasn't capped. There was no cap on the contributions into it. There was really nothing else that you could do on Ethereum at that point. It was kind of like the first application, really. Well, I mean, you did have Augur, a few. You had Digix, this, this gold thing. You had Dai, I think, was sort of coming to Life just about at that point. But the DAO was kind of like the first big thing, right? And it just sort of snowballed and snowballed, right? Because it's like there was, it was also touted as zero risk because you could exit with your funds, right. If you didn't like the result of what was happening, you could just exit and have your ETH back. So it's kind of like this is risk free, right? It's like a risk, you know, it's like a sovereign bond or whatever.

**[43:24] SPEAKER_02:** Right, right.

**[43:24] SPEAKER_01:** There's no downside here. This is risk free though. Tons of people are like, well, what else am I going to do? I'm just sitting here on my Ether, I can't do anything. Well, you know, pile on in. And the Ethereum crowd sale raised what is 16 million, I think, in Bitcoin, which was, I think it was my number five crowd sale of all time. You know, it was like comparing to Kickstarter projects, right? So it's like, you know, maybe they'll do, you know, 2 or 3 million, maybe 5. And it just went until it was, you know, it was just absolutely gigantic. And I remember at the time thinking, you know, this is, I don't like this, like the DAO. It's not, this is not a good idea.

**[44:13] SPEAKER_02:** Yeah.

**[44:14] SPEAKER_01:** And, and the main reason I was thinking of that was is this a security.

**[44:21] SPEAKER_02:** Right.

**[44:22] SPEAKER_01:** Is this seen as, you know, money transfer stuff? Because you've got Slock.it the company. And then they had this thing called DAO Link that was sort of a service company for paying people in real life it was, that was some at Swiss thing, I think, or what's Bitcoin Swiss. And then you have the DAO itself, you had the curators as well. So anyone could, could propose, you know, a smart contract that encoded their proposal. Right. They would make a written description of the thing and here's a smart contract doing it. And the curator's role was like to verify. Yeah. What they've sort of said in text is kind of what they've done. It was meant to be like, you know, this kind of administrative role. But what happened is all of those guys, that was their name, their names and faces up on the website, you know, so like DAO Hub website is just like a who's who of the Ethereum foundation, basically. And it didn't say, you know, Christian Reitwiessner, creator of Solidity, it said, Christian Reitwiessner Ethereum Foundation, Vitalik Ethereum foundation. You know, so lots of people were like, this is an Ethereum foundation project. Right. Because you, you're all got your names on everything. So I thought there was, firstly, there was huge, like, legal liability on those guys because where Slock.it had got these layers of legal protection, these guys haven't. They're just doing it as individuals. And I remember Fabian talking to me and talking to the group in the foundation is like, you know, I've been talking to some of my friends and they're like, you know, they don't think this is a great idea. And I'm thinking of talking to a lawyer. And Gav backed out. Right. A couple of weeks before the disaster, Gav just backed out. He's like, you know, this is, you know, this, this is not what I signed up for. I thought it was just a small role, and now it's like, presented as a lot more. And, you know, so he, he backed out. A lot of the others didn't because. Because it was like, well, if we back out, it's going to, like, ruin it. And it's like a great experiment. But I thought there was huge liability to them. I thought there were legal risks. And I also just thought it was a stupid idea. Like, why would you have thousands of random people putting their money in a bucket and then let's like, vote on what to do with it?

**[47:00] SPEAKER_02:** Right?

**[47:01] SPEAKER_01:** Who are these people? Like, what do they even know, like, about a business proposal or anything? It's just like, this is a stupid idea. But, you know, I didn't have my eye on the fact that all of the tech stack was incredibly immature at that point. Right.

**[47:17] SPEAKER_02:** Yeah.

**[47:17] SPEAKER_01:** There's no best practices, there's no libraries. It's just, here's some code. And. And they just went all in. Right. It was like, code is law.

**[47:26] SPEAKER_02:** Yeah.

**[47:27] SPEAKER_01:** You know, the smart contract is the contract. You know, YOLO, you can't stop us.

**[47:36] SPEAKER_02:** But. But okay. And then the hack happens. Right. And. And I remember the details of the hack being they found a flaw in the smart contract code and they could basically withdraw those funds into another account. And I remember there was some kind of race between, like, the people at the DAO slash Slock.it who were like, using the same exploit to like, drain the account. Like using the same hack, basically. Is that right?

**[48:07] SPEAKER_01:** Yeah. So there was this reentrancy bug where it's really sort of like to do with atomic operations or order of operations. So your reentrancy was that you could be calling because people were supplying, like, their proposals, and it's like, hey, here's a smart contract that's implementing mine. You Were like calling into their code, but you can't know what theirs is going to do. So there was this reentrancy issue where within that other person supplied code you could like kind of call back in. And it was sort of like, so it was to do with child DAOs. So this whole zero risk thing was like, if you didn't like proposals that were happening, you could make a child DAO of saying, well, hey, I'm, I'm out, right? I'm taking my ether and my voting off into this other one. Right. I'm not, I'm not following you. I'm, I'm going there. And other people could join you as well. So I guess the idea was like, right, you know, here we've got this totally over General DAO, but we're going to make a, you know, like a DeFi DAO or an NFT DAO or whatever, right? And, and it's like, I guess a little bit like some of the thoughts for, for consensus and hub and spoke is like, you know, you're going to get this universe of stuff just flourishing out and childs and, and so on. But yeah, the problem on that child DAO thing is that there was this reentrancy bug where rather than just being able to pull your ETH or your share, you can actually go in and pull more and more. So you have this, using this had a child DAO and pulling a giant amount of the funds into that child DAO and then within 30 days they'd be able to exit with the funds. But, but kind of the, the blessings, I guess of that setup is they're not immediately exiting with the funds, right? They haven't gone already and sold it on an exchange and they're done before you notice. You have got this period. And then the other thing is that you could join them. You can go into the child now as well. So after the hack, you know, there was this appeal out. Hey, you know, did, did anyone participate in this, you know, specific child? There was anyone in there. It's like, yeah, you know, yeah, somebody else is in there. And then what you could do is you could, you know, you could child DAO again. It's like, you can do it. Another one. It's like, right, well, I'm going to grab it off you and you're going to grab it off me. And so, you know, you could have had this, this DAO wars thing of like, you can never stop it, but you could delay it indefinitely. So that was one of them. But then the other white hat thing is like, okay, well, we know about the bug, so we can do it too. You can have white hat people like, well, we're going to steal all of the money out of the top, the DAO now as well. But we're doing it for good, right? We're doing it here to keep it, to give it back.

**[51:09] SPEAKER_02:** Right?

**[51:09] SPEAKER_01:** So, so yeah, you had all of those games going on within that existing setup, but then as a reaction to that, you had all of this discussion about, well, you know, are we going to react, are we not going to react first? The first proposal was a, was a soft fork, but, you know, it was just gonna like blacklist out stuff to do with the, with the hacker. Right?

**[51:35] SPEAKER_02:** And they did do that soft fork. Right, I remember they did that soft.

**[51:38] SPEAKER_01:** Fork first, what was done for it. And I think it might even have gone on testnets and things, but it never went live.

**[51:45] SPEAKER_02:** Okay.

**[51:46] SPEAKER_01:** Because it was spotted that it was a denial of service attack because that blacklisting was like, you know, not accounted for in the crypto economics. So it was like, yeah, yeah, you, you, you had a denial of service attack thing on that soft fork. So it got done and then it got undone and then the hard fork was like, okay, well we can, we can go in and we can do an irregular state transaction where at a certain block, you know, you're just going to have a hardcoded thing which sticks different bytecode into, into the address of the, of the DAO, which is like, okay, yeah, that thing, it didn't happen. You know, what's actually at that address is a simple refund thing where you can all get your money back. So, so that's, that was the now hard fork.

**[52:50] SPEAKER_02:** Okay.

**[52:53] SPEAKER_00:** I just wanted to ask where were you at this time? Because I know you got involved, I believe later with ETC, because it didn't exist yet. And so you know how in terms of your personal perspective on all this, we're actually implementing anything yourself because obviously you've got pretty deep knowledge of the technical internals.

**[53:16] SPEAKER_01:** Yes.

**[53:17] SPEAKER_00:** Where are you?

**[53:18] SPEAKER_01:** I was, I was working for the foundation. I was on C team at that point. I, you know, this is about three or four months after I'd started. The thing that was really interesting to me was how different people's thoughts or perspectives were even within the foundation. You know, that you'd have people say, working on Geth, going, well, of course we shouldn't do anything. Well, of course we should. And it's like, you know, been working with you for a year. Like, what, what you think that, like, whoa, you Know, you had this real mixture of, of reactions. And I mean, my, my first reaction was, well, you know, of course you don't do anything. Like it's an immutable blockchain. That's the whole point. Like, you know, you don't like the outcome. Well, you know, tough titties, you know, you. So you've seen so many, you know, like Mount Gox. You know, with Mount Gox, you didn't have the Bitcoiners going, all that. You know, let's, let's, you know, let's try and fix this up or, you know, I, and I think the only reason it happened was because of the scale of it, you know, that it was a significant chunk of the entire ETH money supply. And also I, I think that, you know, things weren't super great on funding and you know, it wasn't like Ethereum was sure to succeed. It was quite, you know, nascent at that point.

**[54:57] SPEAKER_02:** Yeah.

**[54:58] SPEAKER_01:** And I know that there were also worries about the proof of stake transition and the fact that if you had a large amount of, of the ether in, you know, hostile hands, that you could maybe have years of like griefing attacks and stuff like that. But also I think there was just, you know, a lot of people were like, well, you know, this is theft, right. You know, that money was intended for building the ecosystem and you know, some guys come in and stolen it and if we can fix that, well, we should. So, so yeah, I mean, I, you know, my immediate reaction was you shouldn't. But I, I also, it was like, well, you know, whatever. That seems to be the consensus that we do it, you know, and okay, off, off, you know, off we go though. I wasn't at the foundation many more months after that anyway. But, you know, there was this real schism though. I think from what I saw. I think probably about 85% of people wanted to do the hard fork and 15 didn't, or maybe 80, 20. But I think there was pretty strong consensus to do it. But that was, you know, very contentious for, you know, a not tiny group of people, you know, that a lot of people that had got involved with Ethereum have done so because they, they kind of wanted smart, you know, Bitcoin with smart contracts. And, and if you're of that bitcoiny mindset, then, yeah, like, of course you don't, you know, don't screw with things. But, but I think there's also this larger group that were like, well, ether isn't money anyway. Like that was a messaging that had been given out at the time is like, no, no, it's fuel, right? It's fuel for the engine, though. I think part of that is just like trying to dodge legal liability. But, but you know, that was also true as well. You know, this whole world computer, you know, here's a platform, right? You know, it's a platform like the web or Android. So I think it was sort of like that, that was the mental split is like, is it money? And if it's money, you don't move people's monies without private keys. Like, you know, that's, that's a mortal sin. And on the other side you're like, well, no, it's a bug, right? It's a bug in the platform and it's like, well, but it's, but it was a bug in the smart contract. Well, you know, if you've worked on serious software projects, you know, people hack on the wrong layers all the time, right? Because it's going to give you a better user experience. Like, you know, you don't have to be, you know, pure on that. It's really about how the thing works. So, you know, you get hacks in the wrong layers all the time. And if, if you're just seeing it as a, as a software platform, then yeah, it's a bug. You fix the bug.

**[57:59] SPEAKER_02:** So it's rare in life that you can actually see a counterfactual, but in this case we can because ETC was created at that time and kind of emerged out of that. So like, you know, can you talk a little bit about that? And how has that gone? Because you're deep into that ecosystem, obviously, as the, you know, director of the Ethereum classic cooperative, like, how does it work now? Like, you know, what, how did those words divide and then, you know, how are those words continuing so over that.

**[58:32] SPEAKER_01:** Month or so, right, where it's like, you know, the money's been stolen into the sub DAO, we're going to do anything. You know, you have the most, you know, vigorous debate on all platforms, right? You know, it was the, the topic, you know, what's going to happen, how's it going to go and everything, right? So, you know, I don't think there's anyone that was like unaware of this stuff happening. You know, it's very, very. Everyone with their eyes open. But yeah, you know, you just, you just have this group of people kind of gathering together and it's like, no, you know, we're not going to go with it. This is not going to happen. Or at least like, you know, we're not following that hard fault. Maybe people do, but you know, a bunch of people deciding not to. The other thing I thought was really interesting at the time and was to my mind the best thing of all about that chain split is to that point I don't think there'd ever been a minority chain that survived. Right. The standard thinking is like you're going to have a winning side and a losing side and you know that it's going to happen and we'll see where, where's the thing, you know, where are the people going which is the winner and then the losers, you know, well, you know like people will stop mining, it'll just die, right, because it's the loser chain. So there's no economic value there and you know, forget it. But what actually happened on the ETC side is you know, you had miners that were like well you know, just going to keep on mining. I'm not updating, you know, you know, some of it going, you know, the evil Ethereum foundation and you know, Vitalik's a dictator, you know, I mean I don't think any of that's true but you have got people that were like no, I'm going to keep going. And then look, block production's still going and you know it's still happening there. And then Poloniex listed it and then it's got a market value and then you've got speculative activity around that. You've got Ether holders like dumping their ETC. You know it's hey, it's free money. But also you've got other people on the other side going well you know I see real value here and like this ETC is going cheap. So you know, noticeably, notably Barry Silbert who first non bit in Ethereum to that point presumably like based on pre mine and various other things but was like well oh actually like you know an immutability focused ETC, you know would be, would be really interesting. So yeah, you just got this sort of grassroots thing forming. You got volunteers jumping up saying hey you know, I'm a developer, I'll keep maintaining the, the classic geth clients and so on and you know, and it found its own lifestyle. You know you had like the, the Ethereum subreddit was like a primary communication platform at that point and then you had like an Ethereum Classic one, you know being created and some people in, you know, one side, some on the other but you know it got quite bitter in the end. Right. You know you've got a lot of people that were like, you know, foundation, you Guys, you just ruined, you know, you've just ruined the project. And you had people on the other side seeing ETC. Is really illegitimate, you know, as saying, well, look, you, you know, it's just a money grab. You just want your free money. You know, why are these Bitcoiners kind of coming over like they weren't interested in Ethereum before and now they are, like, that's not, you know, you know, that's, that's not good. And you did obviously have a bunch of speculators in there as well, so that's sort of a bit nasty too. But I think the thing that like severed those communities finally was this like 100% ETH meme, which came about because somebody tweeted, hey, Vitalik, I hear that you're working on Ethereum Classic. Is there any truth to this? And he said, no, you know, I'm. I'm only working on Ethereum. And the person then said, well, what if ETC had more market cap than Ethereum? And he said, no, I still wouldn't work on it. 100% ETH. Like, he wasn't saying it in a purity pledge way. He was just in the way he does, being just making a factual statement. But then I remembered Joe replied, I'm 100% ETH. And then it's like everyone's doing it, right? It's this purity pledge, you know, everyone is expected to, you know, pledge allegiance to ETH. So it became a, you know, oh, is this an either or? Like, you can't be in both. Like, if you, if you, you're interested in ETC, then you, you know, you're a dirty person. So I think that that really wedged it, you know, wedged it permanently apart at that point. And also, you know, a number of the people that were volunteering on ETC, you know, they were really angry. They were like, you know, well, I, you know, been involved for two, two and a bit years in this project, you know, really pumped about everything that you can do with Ethereum. And then you guys have, you know, have wrecked it. So there was a lot of, you know, bitterness from that ETC side back. But then, you know, things kind of split apart and over time, ETC, you know, found its own path. So with the real differentiation being, well, firstly that the DAO hack didn't happen. That was the only initial difference. Very rapidly though, there was this conclusion that fixed economic policy was needed. You know, that ETC was really like Bitcoin with Ethereum technology. But, you know, Bitcoin, you know, culture and, and ethos, right? So it's like Right. You know, there's no fixed monetary policy for, for Ethereum. And I mean you see this over many years is like, you know, change of, change of block rewards, ice age delays, fee burning, you know, many, many changes. So that was the first kind of like major change on the ETC side was introduction of that fixed monetary policy because there was consensus that that was an important, you know, that was like bad inheritance that we, that we want to fix. And the other thing that that enabled was the, the grayscale ETC fund. So at that point it's like right, okay, this is really a bitcoin feeling thing and you know there's a feeling that there's, there's a value here. So then from, from that grayscale then created the ETC cooperative that I work from. You know, so a share of the fees went into that kind of, not quite a foundation, but a bit like a foundation, you know, a non profit to support the ecosystem. And then the other thing more recently is, is just proof of work. You know there was, there was sort of fairly rapidly a, a consensus that ETC wanted to stick with proof of work indefinitely. That, that proof of stake was seen as a, you know, as a centralizing oligarchic kind of thing that didn't really fit with that, with that ethos. But more generally, ETC is tracking protocol changes in Ethereum, you know, very compatible.

**[1:06:09] SPEAKER_02:** So there have been forks but not the hard fork along the way because.

**[1:06:14] SPEAKER_01:** Well, so yeah, I mean they hard forks but not chain splits.

**[1:06:19] SPEAKER_02:** Got it. Okay.

**[1:06:20] SPEAKER_01:** In the, in, in the all protocol updates on Ethereum as well, you know that they're all hard forks and the old side doesn't actually go away. You know, you could run a, you could run a frontier node if you wanted. You can mine on Frontier Mine, the Olympic test net mine, any of these ones. It's just, it's just you have had the wither and die because there hasn't been contention. But on ETC you have sufficient contention that you had a chain split. But yeah, I guess that's a sort of a bitcoiner thing is saying, you know, forks are bad.

**[1:06:58] SPEAKER_02:** Right.

**[1:06:58] SPEAKER_01:** But it's like contentious. Hard forks are bad. Hard forks are an upgrade mechanism for the protocol.

**[1:07:07] SPEAKER_02:** Got it.

**[1:07:08] SPEAKER_03:** Yeah, I mean I remember I, I had to implement that for a few years ago and it was pretty blatant. It was just like take money from here and place it here. By the way, it didn't bug me.

**[1:07:19] SPEAKER_01:** But we had people in BlockApps.

**[1:07:21] SPEAKER_03:** Who thought of it as like a stab to the back. They were like so Upset by it.

**[1:07:26] SPEAKER_01:** Yeah, well, I mean it's literally here's an array of addresses. Right. To fuck with.

**[1:07:31] SPEAKER_00:** Yep.

**[1:07:32] SPEAKER_03:** I remember that was, I don't remember what else was in there, but I remember like the majority of it was just like take a bunch of money and put it into these addresses. And that was the, that was the fork.

**[1:07:42] SPEAKER_01:** Yeah. You know, for this list of addresses. Replace, you know it was, yeah, you know, replace the, the bytecode with this other bytecode. And also. Yeah, I think the moving was consolidating the child DAOs. I think, I think that's what that was doing. So it's like move the money from the child DAOs back into the parent DAO and change the bytecode. Like I think, you know, if block equals this, do a horrible thing.

**[1:08:13] SPEAKER_02:** But yeah, in the ETC world where the DAO hack happened, are those fun? Like did the hacker pull out those funds? Did. Okay, so like.

**[1:08:27] SPEAKER_01:** Yeah, yeah.

**[1:08:28] SPEAKER_02:** Interesting.

**[1:08:29] SPEAKER_01:** Yeah. I mean again, Laura Shin has a great write up of all of this in her book, The Cryptopians, including working out who it probably was.

**[1:08:40] SPEAKER_02:** Oh, wow. Okay.

**[1:08:41] SPEAKER_01:** Well, so she didn't name names in the book, but then she did a, an article like on the release day or just before naming who she thinks it was. So that's an interesting story. I can, I'll, I'll dig out that article and send it to you guys so you can add it to the description here.

**[1:09:03] SPEAKER_02:** Cool. And, but you know, Bob, you're a natural born bridge builder. As we said, you get along with everyone. Do you ever see the, you know, valley between Ethereum and Ethereum Classic narrowing or getting better? Or do you think it is getting better?

**[1:09:25] SPEAKER_01:** I mean the problem that Ethereum Classic has always had from the time of the split and it comes back to money again. Like I, I think that was the one thing that the foundation did wrong, you know, like not, not talking about the developers or the decision on that or whatever was to only put the money on one side. Because what that did is disenfranchised a good chunk of people who had, you know, invested in the pre sale, who'd been part of that community, who'd genuinely been, you know, actively involved for those first two years and they were just left in the dust. It's like, well, you know, you guys, we don't care what you think. Goodbye. You know, and the trademark's going this way and all the funds are going this way and you know, and all the developers went that way as well. And I mean obviously like the foundation can control that. People choose to work on. But what that meant is effectively that group of people got defunded, like, totally done. You. I'm sorry, my child. I. I disavow you and I'll kick you out of the house, you know, forever. And we shall never talk to you again. You know, I think in retrospect it should have been like, okay, funding is available for that other fork as well. And you may hate us, you know, and not want to talk to us, but, you know, I guess it's like, you know, a child, you know, whatever teenager, I'm, I'm out, you down, I'm leaving home. And it's like, okay, I'm not gonna stop putting aside savings and money for you. I, you know, you might not love me now, but, you know, I'm. You're my child too. And, you know, we'll. We'll find a way of making it happen, you know, because, say, with this ETC. Cooperative, you know, it could have been. Well, when that came into, you know, into existence, the foundation could have gone, well, okay, you know, like, here's a body that can help. And there you go, we're going to fund it as well. And that there was something a little tiny bit like that with Virgil. So Virgil was also a huge bridge builder between Ethereum, Ethereum classic. So in 2018, he invited Anthony Lusardi, who was my predecessor, to speak at Edcon. So this was May 2018, and that was the first Ethereum Classic talk at an Ethereum event. You know, it been nearly two years at that point. And you know, and it was fine and it was cool and everyone was, you know, everyone was friendly and you know, Vitalik and various others came to that talk and, you know, it was all. All kind of friendly. And Anthony invited me to Ethereum Classic Summit, which was in September 2018. So myself and Virgil went and spoke at that event. And around that time, Virgil, they somehow they found some ETC that the foundation still had. You know, generally they did a market dump at that time, but there was some stuff that they found. You know, it's like 50 grand or something like that. And so we got that donated to the co-op. That was a. That was a really nice, nice kind of thing, but, you know, it was kind of like, here's a little gesture. But really I think, I think that was a. That was a real failing because it was a legitimate, you know, irreconcilable difference. But. But it was made even worse by this, you know, 100% ETH purity pledge combined again with all the money's gone. So you end up with you know, a very small community of mainly people who are, you know, very ideologically outraged by it. You know, if you've got speculative token holders obviously that you know they're going to stick with Ethereum, you know, what's this other thing, this new thing and there's nothing, you know, so, so that's always been the, the issue that, that ETC's had is you know, lack of, you know, lack of, lack of money and interest really. More recently we've had support from Bitmain after the merge with Ethereum, moving to proof of stake. All of a sudden ETC is one of the larger mining ecosystems. So all of a sudden, you know we're very aligned with, with, with Bitmain. You know they want to sell ASICs, they want to be using Antpool for mining. So, so they're supporting a grant program now. But yeah, you know ETC's, you know it's small but you have, you know, you have some people and that's, you know, that's their, that's what they want.

**[1:14:22] SPEAKER_02:** Yeah and as you said like, you know like it's broken the mode of like side chain surviving. Right. Like it really like you know these, it's possible, you know. Oh, sorry, go ahead Kieren.

**[1:14:36] SPEAKER_00:** I wanted to talk quickly about you know, this, the definition of success for blockchains, market caps and all that sort of thing. And I was looking today because so Ethereum's market cap is in the 200 billions theorem classic is still at number 28 which is quite impressive and is you know, 2.6 billion in market cap. I think market cap is probably more of an indicator of popularity than anything sort of truly long term, you know, it's not quite like with companies where market cap is probably a better indicator of how important they are but it is also still and if you look, yeah.

**[1:15:24] SPEAKER_01:** If you look in CoinGecko. So Ethereum Classic is higher than Cosmos, than Filecoin, than Hedera, than Internet Computer, than Aptos, than Lido, than NEAR, than Optimism, than Arbitrum, than The Graph, you.

**[1:15:43] SPEAKER_00:** know and so I wanted to, to follow, you know, is market cap a good goal? What, what is your goal for ETC? If you were trying to, you know, make up the gap with Ethereum, what you know, would you do anything differently?

**[1:16:02] SPEAKER_01:** I mean I think to do that you just need vast investment into application layer. I mean I think, I think that's somewhere where ETC really can't compete with many other VC chains, you know that have huge treasuries that can be spending you know, tens or Hundreds of millions on grant programs, you know, that's, you know, we can't compete that way. But also it, as you say it, it's a bit of a vanity metric in a way. You know, like there are many other vanity metrics that we, we commonly see in the space. Because yeah, you know, if you want whatever the fastest chain or the most money or whatever, like, yeah, that's not going to be ETC, like it can never be ETC. But for people that are interested, that's not the goal. Right. They, you know, they're looking for something which is basically like Bitcoin plus smart contracts, you know, with that kind of strong non intervention kind of bias. And also proof of work, you know, a lot of people see, you know, real value in proof of work and are very skeptical of proof of stake systems. So you know, it's not, you know, it's not a winner takes all.

**[1:17:29] SPEAKER_00:** It's, it's been interesting just how not a winner takes all the blockchain space has been. They've had this. They're like cockroaches. They just kind of, you know, keep going. I know they get delisted occasionally, but you know, how many, let's see how many pages you can get to on.

**[1:17:46] SPEAKER_02:** Can we call them tree clippings instead of.

**[1:17:50] SPEAKER_01:** 20,000 is the figure I've heard. Yeah, 20,000 live chains.

**[1:17:55] SPEAKER_00:** Yeah, that's, that's quite a number and very interesting kind of in and of itself. Kieren, you were saying something when I made my comment.

**[1:18:04] SPEAKER_02:** Oh no, no, no. I was just saying I was going to ask you more questions about, you know, the early days of EEA. But I think we will have to invite you back because I'm pretty sure we could have another, you know, another 90 minute conversation on that. But it's been great to have you, Bob, as always. You're always been a great friend and a wealth of information on the space. So thank you for joining us and we hope you'll come back again soon.

**[1:18:35] SPEAKER_01:** Well, thank you and, and sorry for monopolizing me.

**[1:18:39] SPEAKER_02:** No, this. Exactly.

**[1:18:40] SPEAKER_00:** That's why you're here. Yeah, exactly your story. We've told him plenty of ours. Should we, you know, I see on, on other podcasts, should we send people anywhere? Where can people find you, do you want them to find you, etc.

**[1:18:56] SPEAKER_01:** Yeah, I can, yeah, I can, I can, I can drop you some links afterwards. But yeah, my own website is bobsummerwill.com Ethereumclassic.org is the main sort of landing page for ETC.

**[1:19:10] SPEAKER_02:** Awesome.

**[1:19:11] SPEAKER_00:** Fantastic. Well, thank you very much really appreciate your time, and I'm sure we will follow up. We'll put our heads together and do another one when we're all ready.

**[1:19:21] SPEAKER_02:** Yes, we'll have to have around two. There's plenty. There's plenty more stories that we haven't even touched on yet.

**[1:19:27] SPEAKER_01:** Okay, Cheers, guys.

**[1:19:29] SPEAKER_00:** Cheers.