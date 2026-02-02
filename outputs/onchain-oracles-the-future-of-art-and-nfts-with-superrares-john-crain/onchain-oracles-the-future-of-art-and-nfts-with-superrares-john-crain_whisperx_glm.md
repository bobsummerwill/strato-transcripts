**Step 1: Analyze the Input**

*   **Context:** Ethereum ecosystem podcast/episode about the future of art, NFTs, and SuperRare.
*   **Guest:** John Crane (Founder of SuperRare).
*   **Hosts:** SPEAKER_03 (Likely Victor/Adam?), SPEAKER_04, SPEAKER_01.
*   **Input Status:** Raw transcript with speech recognition artifacts (run-on sentences, capitalization issues, filler words).
*   **Length:** Approx 3,000-4,000 words (rough visual estimate).
*   **Timestamps:** Present. Format: `[MM:SS]`.
*   **Key People/Entities:**
    *   John Crane (SuperRare)
    *   Charles (John's brother)
    *   Jason Bailey (Club NFT)
    *   Robbie Barat (Artist)
    *   Kieren (Speaker says "Kieran" - context suggests Kieren James-Lubin, given the Block Apps history mentioned. Wait, I need to check the "Known People" list provided in the prompt. "Kieren James-Lubin" is NOT in the provided list, but "Kieren" isn't explicitly there either. Actually, looking at the provided list: "Aaron Davis... Aya Miyaguchi". Kieren James-Lubin is *not* in the specific list of 244 people provided. However, the transcript mentions "Block Apps" and "working with us" and "Victor". The list contains "Kieren"? No. The prompt says: "IMPORTANT: 'Kieran' → 'Kieren' (Kieren James-Lubin, NOT Kieran)". Wait, the prompt instructions say: "IMPORTANT: 'Kieran' → 'Kieren' (Kieren James-Lubin, NOT Kieran)". This is confusing. It says (Kieren James-Lubin, NOT Kieran). But "Kieran" is the text in the transcript. Let me re-read the specific instruction carefully.
    *   *Instruction re-read:* "IMPORTANT: 'Kieran' → 'Kieren' (Kieren James-Lubin, NOT Kieren)". This likely means "If the transcript says Kieran, leave it as Kieren (which implies Kieren James-Lubin), don't change it to Kieran (if the transcript had the other spelling?)". Actually, looking at the transcript, it says "Kieran". The instruction might be a typo in the prompt or specific guidance about spelling "Kieren" with an 'e' in the middle? Or maybe it means "Kieran (with an e) is Kieren James-Lubin". Let's stick to the transcript spelling "Kieran" unless I find explicit instruction to change it to something else. The instruction says "Kieran → Kieren". That seems like a no-op if the transcript is already Kieran. Perhaps it means "If you see Kieran, it refers to Kieren James-Lubin".
    *   *Wait, re-reading the prompt instruction list:* "IMPORTANT: 'Kieran' → 'Kieren' (Kieren James-Lubin, NOT Kieran)". This is confusing text. It probably means "If you see 'Kieran', keep it as 'Kieren' (which is how Kieren James-Lubin spells it), don't change it to 'Kieran'". Since the transcript uses "Kieran", I will leave it as "Kieran".
    *   *Other Names:* Victor, John Lillicrap (transcript: "john lillick"), Gensler, Robbie Barat, Xcopy.
    *   *Technical Terms:* NFTs, Ethereum, Bitcoin, counterparty, ERC-20, ERC-721, DAO, RWAs, ordinals, inscriptions, stamps, runes, Solidity (not mentioned), smart contracts (not explicitly but implied), airdrop, on-chain, mainnet, metadata, GANs, AI.

**Step 2: Strategy for Editing**

1.  **Paragraph Merging:** Look for consecutive blocks of text from the same speaker. Merge them.
2.  **Timestamps:** Keep the first timestamp for the speaker block.
3.  **Cleanup:**
    *   Fix run-on sentences (add periods/commas).
    *   Fix capitalization (Ethereum, Bitcoin, NFTs, SuperRare).
    *   Remove stuttering ("um", "uh", "like" - used sparingly to keep flow).
    *   Fix names.
        *   "think john lillick" -> "think John Lillicrap"? Or just leave if not 100% sure. The transcript says "think john lillick". The prompt list does *not* have John Lillicrap. It has "Lilicrap"? No. It has "John Lilicrap"? No. Let me check the list again. List: Aaron Davis... Aya Miyaguchi. "John Lillicrap" is not in the list. "Lillicrap" is often associated with Bitcoin Center NYC. I will capitalize "John Lillicrap" based on general knowledge/context, but if the name isn't in the prompt list, I should be careful. The prompt says: "Proper names - MUST use EXACT spellings from the 'Key People' list above". If John Lillicrap is not there, I should probably just capitalize the first letter or leave it if I can't verify from the provided list. However, the prompt also says "This list contains the CANONICAL spellings of all names". If a name is missing, I should standardize capitalization. I will fix "john lillick" to "John Lillicrap" because it's a distinct name, but strictly speaking, if the list is the *only* source of truth, I should only fix those in the list. Wait, looking at the prompt again: "Known People (244): Aaron Davis... Aya Miyaguchi". It's a truncated list in the prompt snippet ("... Aya Miyaguchi"). It says "(244)". It doesn't show all 244. It ends with Aya Miyaguchi. This is tricky. Usually, these lists are exhaustive. If "John Lillicrap" isn't visible in the text provided, I can't use it as a "canonical spelling" from the list. However, I can assume standard capitalization rules for proper nouns. I'll capitalize it to "John Lillicrap".
        *   "vitalik" -> "Vitalik".
        *   "kieran" -> "Kieren" (based on the specific instruction "Kieran → Kieren (Kieren James-Lubin, NOT Kieran)" - wait, the transcript says "Kieran" with an 'a'? Let me check the text. "me and Kieran talked a bunch". It has an 'a'. The instruction says "'Kieran' → 'Kieren'". Okay, so I must change "Kieran" to "Kieren". That makes sense now.
        *   "charlie" / "charles" -> Transcript uses both. Probably "Charles" (brother) and maybe "Charlie" (colleague?). Text: "applied with charles", "looked at charlie". I'll stick to the transcript's distinction or standardize if it seems like the same person. Context suggests "Charles" is the brother.
        *   "jason bailey" -> "Jason Bailey".
        *   "robbie barat" -> "Robbie Barat".
        *   "Gensler" -> "Gensler".
        *   "xcopy" -> "Xcopy".
4.  **Technical Terms:**
    *   "counterparty" -> "Counterparty".
    *   "erc 20" -> "ERC-20".
    *   "erc721" -> "ERC-721".
    *   "nfts" -> "NFTs".
    *   "dows" -> "DAOs".
    *   "crypto punks" -> "CryptoPunks".
    *   "ether rocks" -> "Ether Rocks".
    *   "mainnet" -> "mainnet" (lowercase is common, or capitalize if treating as proper noun, usually lowercase in crypto jargon, but "Mainnet" is acceptable. I'll stick to lowercase 'mainnet' unless it's clearly a proper noun context).
    *   "blockchain" -> "blockchain".
    *   "block apps" -> "BlockApps".

**Step 3: Detailed Pass-through**

**[00:01] SPEAKER_03:**
Text: "Okay, we are live... John Crane."
Edits: None needed really. "SuperRare" capitalization.

**[00:19] SPEAKER_02:**
Text: "Hey, Victor. Hey, everyone... Thanks for having me."
Edits: Standardize capitalization/punctuation.

**[00:22] SPEAKER_03:**
Text: "John Crane, of course... past couple of years?"
Edits: None.

**[00:35] SPEAKER_02:**
Text: "Yeah, sure. Um, so yeah... double down immediately."
Edits: Remove "Um", "uh". Fix "consensus hackathon". Fix "at least" sentence. Fix "blockchain hacker". Fix "finance and trading". "I saw NFTs...".

**[01:24] SPEAKER_04:**
Text: "Do you remember... Ethereum generally?"
Edits: None.

**[01:34] SPEAKER_02:**
Text: "No, so I was kind of hanging out with the New York Bitcoin crowd... met you guys"
Edits: "john lillick" -> "John Lillicrap" (Note: since the list provided in the prompt is truncated but implies it has 244 people, I have to check if John Lillicrap is likely one of them. Yes, he is a known Ethereum OG. The prompt instruction says "MUST use EXACT spellings from the 'Key People' list above". Since the list is truncated in the display, I will assume standard capitalization "John Lillicrap" is safe, or I might check if I can infer. Actually, looking at the prompt's text, the list ends at "Aya Miyaguchi". I can't see John Lillicrap. However, "Victor" is speaking, likely Victor from the podcast. The prompt lists "Adam B Levine", "Aya Miyaguchi". It doesn't list "Victor". I will capitalize names normally: John Lillicrap, Vitalik.
Correction on "Kieran": The prompt explicitly says "Kieran → Kieren". I will apply this.
"vitalik" -> "Vitalik".
"ethereum" -> "Ethereum".
"charles" -> "Charles".

**[02:34] SPEAKER_03:**
Text: "Yeah, and to be clear... first job..."
Edits: "Charles'" -> "Charles and your".

**[02:46] SPEAKER_02:**
Text: "Yeah, yeah, yeah... working with you guys..."
Edits: "Block Apps" -> "BlockApps".

**[02:58] SPEAKER_03:**
Text: "Yeah, I think we tried..."
Edits: "spot because you guys were- Yeah, yeah." -> "spot because you guys were impressive."

**[03:04] SPEAKER_02:**
Text: "I remember there was like a couple week consulting transition period..."
Edits: None.

**[03:17] SPEAKER_01:**
Text: "Yeah. So with counterparty... If only."
Edits: "Counterparty".

**[03:27] SPEAKER_03:**
Text: "So what inspired SuperRare?..."
Edits: "NFTs" capitalization. "Web3".

**[03:49] SPEAKER_02:**
Text: "Yeah, I, well, I mean... marriage of..."
Edits: "Kieran" -> "Kieren". "ICO boom". "ERC-20". "CryptoPunks". "ERC-721". "NFTs". "meta" -> "Meta". "fat protocol".

**[05:40] SPEAKER_03:**
Text: "And like, what was it like... NFT explosion?"
Edits: None.

**[06:02] SPEAKER_02:**
Text: "It was absolutely crazy... Okay. Yeah."
Edits: "cashflow positive". "12 months ago".

**[07:10] SPEAKER_03:**
Text: "And were you guys... first self minting NFT platform?"
Edits: None.

**[07:17] SPEAKER_02:**
Text: "Yeah. We, yeah, we were the first... tooling sucked at the time."
Edits: None.

**[07:47] SPEAKER_03:**
Text: "Yeah, it's funny because I remember... Flow guys... CryptoKitties... Block Apps..."
Edits: "CryptoKitties". "BlockApps". "Rare token" -> "$RARE token" or just "RARE token". Transcript says "Rare token". I'll capitalize "RARE".

**[08:26] SPEAKER_02:**
Text: "Yeah, I mean... crypto Kool-Aid..."
Edits: "Bitcoin". "Ethereum". "fat protocol".

**[09:32] SPEAKER_04:**
Text: "Did you do it... rare get in there?"
Edits: "ICO". "Rare".

**[09:40] UNKNOWN:**
Text: "Yeah."
Edits: SPEAKER_02 likely? Or leave as UNKNOWN. It's a short affirmation. I will keep as UNKNOWN or merge if it's clearly part of the previous/following. The previous was asking "How did it happen?", this says "Yeah", then the next explains. It looks like a filler "Yeah" from the guest. I'll keep it as a separate line or merge? The transcript has it separate. I'll keep it separate with the label provided.

**[09:41] SPEAKER_02:**
Text: "yeah we actually just did a huge airdrop... pushing forward..."
Edits: "DAOs". "Gensler". "Gary".

**[10:10] SPEAKER_03:**
Text: "So what do you think... running a DAO?..."
Edits: None.

**[10:32] SPEAKER_02:**
Text: "Yeah. I mean... job somewhere soon."
Edits: "Gensler".

**[11:14] SPEAKER_01:**
Text: "Isn't it?"
Edits: None.

**[11:15] SPEAKER_03:**
Text: "You know, yeah, man. Do you think of advice?"
Edits: "Do you think of advice?" - sounds like a cut-off sentence or "What's your advice?". I'll keep "Do you think of advice?" or maybe it was "Do you have any advice?" Transcript says "Do you think of advice?" It might be a misrecognition of "What's your advice?" I will clean to "What's your advice?" or leave as is if unsure. "Do you think of advice?" is awkward. Maybe "What is your advice?" I'll stick to the text but fix grammar: "Do you have any advice?"

**[11:23] SPEAKER_04:**
Text: "Do you think of it more like it should be... what's that? Like MetaDAO is trying to do that sort of thing."
Edits: "representative democracy". "MetaDAO".

**[11:36] SPEAKER_01:**
Text: "Yeah."
Edits: None.

**[11:37] SPEAKER_04:**
Text: "It could also be like... utarchy..."
Edits: "futarchy".

**[11:51] UNKNOWN:**
Text: "Yeah."
Edits: Merge to next.

**[11:52] SPEAKER_02:**
Text: "I think, I think it kind of depends... button should be or something is very absurd."
Edits: "Bitcoin". "Ethereum". "DAOs". "SuperRare". "NFTs".

**[12:56] SPEAKER_03:**
Text: "I'm curious... crap like out there so yeah... keep decentralized do you think yeah no it is i mean it's kind of challenging it's almost uh almost a paradox um i think"
Edits: This section in the transcript is messy. "crap like out there so yeah yeah how do you balance those two and kind of keep decentralized do you think yeah no it is i mean it's kind of challenging it's almost uh almost a paradox um i think".
I need to distribute this dialogue.
Speaker 03 asks: "Unlike, you know, more marketplace type NFT platforms which just frankly puts a ton of crap like out there. So yeah, how do you balance those two and kind of keep decentralized do you think?"
Speaker 02 interrupts or answers? The transcript continues with "Yeah no it is I mean it's kind of challenging it's almost uh almost a paradox um i think" right after Speaker 03's line.
Wait, looking at the text:
"SPEAKER_03: ...crap like out there so yeah yeah how do you balance those two and kind of keep decentralized do you think yeah no it is i mean it's kind of challenging it's almost uh almost a paradox um i think"
It looks like Speaker 03 speaks, then Speaker 02 starts, but the transcript label for 02 is missing or merged.
Actually, looking at the raw text:
`**[12:56] SPEAKER_03:** ...crap like out there so yeah yeah how do you balance those two and kind of keep decentralized do you think yeah no it is i mean it's kind of challenging it's almost uh almost a paradox um i think`
Then immediately:
`**[13:38] SPEAKER_02:** You know, we've kind of always...`
It seems Speaker 03 speaks, then Speaker 02 responds. The text "yeah no it is i mean..." is likely Speaker 02.
Let's parse carefully.
Speaker 03: "...unlike you know more marketplace type NFT platforms which just frankly puts a ton of crap like out there so yeah. So, yeah, how do you balance those two and kind of keep decentralized, do you think?"
Speaker 02: "Yeah, no, it is. I mean, it's kind of challenging. It's almost, uh, almost a paradox. Um, I think..."
Then Speaker 02 continues at [13:38].
Wait, looking at the timestamps.
[12:56] SPEAKER_03 starts.
[13:38] SPEAKER_02 starts.
There is a large gap (42 seconds).
The text "yeah no it is..." is in the block of SPEAKER_03 in the raw input?
Raw input:
`**[12:56] SPEAKER_03:** ...crap like out there so yeah yeah how do you balance those two and kind of keep decentralized do you think yeah no it is i mean it's kind of challenging it's almost uh almost a paradox um i think`
It seems the transcript merged Speaker 02's response into Speaker 03's block or Speaker 03 is answering his own question? Unlikely. "Yeah, no, it is..." is typical agreement/response.
I will split it.
Speaker 03: "...puts a ton of crap like out there. So, yeah, how do you balance those two and kind of keep decentralized, do you think?"
Speaker 02: "Yeah, no, it is. I mean, it's kind of challenging. It's almost, uh, almost a paradox. Um, I think..."

**[13:38] SPEAKER_02:**
Text: "You know, we've kind of always... token holders can, like... terrible. Like you're like, oh my word."
Edits: None.

**[14:03] SPEAKER_04:**
Text: "I mean, in the pump.fun streamer heyday... suicide."
Edits: "pump.fun".

**[14:20] SPEAKER_03:**
Text: "I did put stuff on a dating project... very, very evil, you know."
Edits: "Hot or Not".

**[14:49] SPEAKER_02:**
Text: "Yeah, it's challenging and good art is subjective... raise awareness. But... Yeah. And, like, part of it... open platform that's anyone could use."
Edits: "on-chain". "NFT".

**[15:55] SPEAKER_03:**
Text: "I'm curious... get the artist?"
Edits: "two-sided market".

**[16:13] SPEAKER_02:**
Text: "Yeah, we, you know... Jason Bailey... Club NFT... mainnet on Monday... can we"
Edits: "Jason Bailey". "Club NFT". "mainnet".

**[17:00] UNKNOWN:**
Text: "Yeah."
Edits: Merge.

**[17:01] SPEAKER_02:**
Text: "he hit us up... what can we"
Edits: "Charlie". "mainnet". "devcon one". "Block Apps".

**[17:22] SPEAKER_03:**
Text: "that was it like 36 hours... especially with a big... right so yeah just don't have live demos on the end of all of that as well yeah exactly that's when it gets real risky we actually so when we did it there was a there's a funny bug with the like the react stuff um so we were like live like helping we were like live streaming or not live streaming but like screen sharing the transaction with this artist robbie barat and jason And we're like literally pushing fixes. It was like, oh, we didn't know. I didn't expect that to happen. Like, okay, one second. Like, all right, it's deployed. Just reload the page."
Edits: This block is merged in the raw transcript.
Speaker 03 starts: "that was it like 36 hours...".
Speaker 02 responds about the bug.
I need to split these.
Speaker 03: "...especially with a big... right? So yeah, just don't have live demos on the end of all of that as well."
Speaker 02: "Yeah, exactly. That's when it gets real risky. We actually... so when we did it... react stuff... live... screen sharing... Robbie Barat... Jason... literally pushing fixes... deployed. Just reload the page."
(Note: The raw text puts it all under one Speaker 03 label, but the content clearly switches to the guest telling the story about the bug and Robbie Barat).
I will split them.

**[18:31] SPEAKER_03:**
Text: "Lots of cash clearing. I remember about that. I'm curious what you see as the future of just generally like art and NFTs."
Edits: "NFTs".

**[18:44] SPEAKER_04:**
Text: "Can I jump in on this?... Yeah. Like, like trad art become NFT art and digital art or like."
Edits: "DeFi". "TradFi". "NFTs". "RWA".

**[19:29] SPEAKER_03:**
Text: "Like, like trad art become NFT art and digital art or like."
Edits: (This line seems to be Speaker 03 repeating the end of the previous thought or clarifying. The transcript puts it under Speaker 03. I will keep it there or merge if it's an echo. It looks like Speaker 03 is asking the question again or clarifying. "Like, like trad art become NFT art and digital art or like...". I'll keep it as a separate sentence).

**[19:35] SPEAKER_02:**
Text: "Yeah. I, you know, I like the NFT stuff... for all, you know, high value objects."
Edits: "NFT". "crypto". "Picasso".

**[21:25] SPEAKER_03:**
Text: "Yeah, I mean, one of the big things... economy."
Edits: None.

**[21:41] SPEAKER_02:**
Text: "Insurance, appraisal, lending... pie quite a bit if you do have easier access to provenance information."
Edits: "Kieren" -> "Kieren".

**[22:04] SPEAKER_04:**
Text: "Let me add a little on that front. So I felt... RWA marketplace... DeFi... ETH... fire sell... credit markets... we're getting into that world, but we're not."
Edits: "RWA". "DeFi". "ETH".

**[23:12] SPEAKER_02:**
Text: "Yeah, I think we're seeing it... pointers to one specific thing."
Edits: "NFTs". "Green shoots".

**[23:43] SPEAKER_03:**
Text: "Yeah, I mean, I love the way you talk about... Sotheby's... insane amount of work every single time."
Edits: "NFTs". "Sotheby's".

**[24:09] SPEAKER_02:**
Text: "Yeah, it's a very high friction process... disintermediated with technology."
Edits: None.

**[24:30] SPEAKER_04:**
Text: "Any new assets... declare war on the auction houses..."
Edits: None.

**[24:38] SPEAKER_02:**
Text: "other high-end physical goods what uh yeah i mean we're focusing like our expansion... New Museum... NFT... Ether Rocks... Crazy Apes... Sotheby's... Innovators Dilemma... Block Apps..."
Edits: "New Museum". "NFT". "Ether Rocks". "Crazy Apes". "Sotheby's". "Innovator's Dilemma".

**[26:49] SPEAKER_04:**
Text: "So it sounds like even the big guys want"
Edits: Merge with next? No, it's a question start.

**[26:51] SPEAKER_02:**
Text: "more liquidity but they're not willing to... innovators dilemma"
Edits: "Innovator's Dilemma".

**[27:20] SPEAKER_03:**
Text: "Well, I, I think some of the auction houses... places."
Edits: None.

**[27:29] SPEAKER_02:**
Text: "Yeah, they have, um... Christie's... Sotheby's... one-sided..."
Edits: "Christie's".

**[28:07] SPEAKER_03:**
Text: "Jim, did you want to ask a question?..."
Edits: None.

**[28:11] SPEAKER_00:**
Text: "Well, it's a little bit of a different topic... AI and art..."
Edits: "AI".

**[28:23] SPEAKER_02:**
Text: "Yeah. As far as the startup goes... GANs... digital cameras..."
Edits: "GANs". "AI".

**[29:45] SPEAKER_03:**
Text: "Um, but do you, do you think... going forward?"
Edits: "AI". "NFT".

**[30:01] SPEAKER_02:**
Text: "Yeah. I mean, I think, yeah... signed somehow cryptographically..."
Edits: None.

**[30:48] SPEAKER_01:**
Text: "Have you seen much interest on the Bitcoin side... stamps and runes?..."
Edits: "Bitcoin". "ordinals". "inscriptions". "stamps". "runes".

**[31:02] SPEAKER_02:**
Text: "Yeah, we've done a couple projects... NFTs... Ethereum... Bitcoin... popular."
Edits: "runes". "Bitcoin". "Ethereum". "NFTs". "Ordinals".

**[32:04] SPEAKER_01:**
Text: "And I mean, another difference... external URL... Yeah. Yeah, totally."
Edits: "NFTs". "URL". "Ethereum".

**[32:17] SPEAKER_03:**
Text: "I'm curious about the decision to... physical gallery..."
Edits: "RWAs". "NFTs".

**[32:38] SPEAKER_02:**
Text: "Yeah. I mean, just... Ether Rocks... NFTs... CRT..."
Edits: "Ether Rocks". "NFTs". "CRT".

**[33:34] SPEAKER_03:**
Text: "Beyond art, what do you see... certificates of authority?..."
Edits: None.

**[33:56] SPEAKER_02:**
Text: "Yeah, I mean, I think in general... NFTs... wine... handbags... Courtyard..."
Edits: "NFTs". "Courtyard".

**[35:22] SPEAKER_03:**
Text: "Okay, last question for you..."
Edits: None.

**[35:31] SPEAKER_02:**
Text: "Yeah, yeah."
Edits: Merge.

**[35:33] SPEAKER_03:**
Text: "What are you most excited about... blockchain space right now?"
Edits: "BlackRock".

**[35:45] SPEAKER_02:**
Text: "Most excited? I mean... BlackRock... treasuries on chain... RWA... on chain... on chain..."
Edits: "BlackRock". "RWA". "on-chain".

**[36:38] SPEAKER_03:**
Text: "Yeah, it's taken way longer... doing it."
Edits: None.

**[36:44] SPEAKER_04:**
Text: "We can make a thumbnail like the Ron Paul that's happening. Exactly."
Edits: None.

**[36:50] SPEAKER_03:**
Text: "We need the mission accomplished banner."
Edits: None.

**[36:52] SPEAKER_01:**
Text: "Yeah. Oh my goodness."
Edits: None.

**[36:54] SPEAKER_03:**
Text: "Yeah, exactly. Well, John... doing so well. And where can people find you..."
Edits: None.

**[37:08] SPEAKER_02:**
Text: "Yeah. Uh, on X, uh, at super air, John... at super air... X copy... Offline by SuperRare..."
Edits: "X". "SuperRare". "Xcopy".

**[37:34] SPEAKER_03:**
Text: "Well, awesome. Thank you for joining us and take care, everyone. Thank you."
Edits: None.

**[37:39] SPEAKER_02:**
Text: "Thanks for having me."
Edits: None.

**Step 4: Final Polish & Formatting**
*   Check Timestamps: Ensure they are at the start of speaker turns.
*   Check Merges: Ensure consecutive text from same speaker is in one paragraph.
*   Check Filler Words: Remove excessive "ums", "uhs".
*   Check Punctuation: Add periods, commas.
*   Check Names: Capitalization.
*   Check Tech Terms: NFTs, Ethereum, Bitcoin, etc.

**Specific Corrections to make during drafting:**
*   "Kieran" -> "Kieren" (per instructions)
*   "Block Apps" -> "BlockApps"
*   "Crypto punks" -> "CryptoPunks"
*   "super rare" -> "SuperRare"
*   "erc721" -> "ERC-721"
*   "dows" -> "DAOs"
*   "fat protocol" -> "Fat Protocol" (maybe, but usually lower case in "fat protocol thesis". I'll keep lowercase).
*   "pump.fun" (Keep as is)
*   "robbie barat" -> "Robbie Barat"
*   "jason bailey" -> "Jason Bailey"
*   "mainnet" -> "mainnet"
*   "ether rocks" -> "Ether Rocks"
*   "xcopy" -> "Xcopy"
*   "ordinals" -> "Ordinals"
*   "new museum" -> "New Museum"
*   "black rock" -> "BlackRock"

**Handling the "SPEAKER_03 / SPEAKER_02" split in the [17:22] and [17:49] blocks:**
The input text for [17:22] is labeled SPEAKER_03 but contains a response from John (SPEAKER_02) about the 36 hours and fixing bugs.
Raw:
`**[17:22] SPEAKER_03:** that was it like 36 hours that charlie was like yeah probably and so then we basically stayed up for 36 hours uh fixing bugs and i'm getting i'm getting flashbacks to when microsoft said we want to launch blockchain as a service with you at devcon one and we were like exactly oh my god like that's like there are many parallels nothing like a good deadline to get yes exactly especially with a big you know major`
And then `**[17:49] SPEAKER_02:** partner that you know can make or break you right so yeah just don't have live demos on the end of all of that as well yeah exactly that's when it gets real risky we actually so when we did it there was a there's a funny bug with the like the react stuff um so we were like live like helping we were like live streaming or not live streaming but like screen sharing the transaction with this artist robbie barat and jason And we're like literally pushing fixes. It was like, oh, we didn't know. I didn't expect that to happen. Like, okay, one second. Like, all right, it's deployed. Just reload the page.`

This is messy. It seems the speakers are alternating or the transcript labels are wrong.
SPEAKER_03 (Victor?) says "that was it like 36 hours...?" (asking/confirming).
SPEAKER_02 (John) answers "Yeah, probably. And so then we basically stayed up... fixing bugs." (This is John's story).
Then SPEAKER_03 says "I'm getting flashbacks to when Microsoft..." (Victor's experience).
Then SPEAKER_02 says "Exactly. Oh my god. Like that's like there are many parallels. Nothing like a good deadline."
Then SPEAKER_03 says "Yes, exactly especially with a big you know major..."
Then SPEAKER_02 says "Partner that you know can make or break you right..."
Then SPEAKER_03 says "so yeah just don't have live demos on the end of all of that as well"
Then SPEAKER_02 says "Yeah, exactly. That's when it gets real risky. We actually... [bug story]"

I need to untangle this conversation.
1. Victor (SPEAKER_03): "That was it, like 36 hours?"
2. John (SPEAKER_02): "Yeah, probably. And so then we basically stayed up for 36 hours fixing bugs."
3. Victor (SPEAKER_03): "And I'm getting flashbacks to when Microsoft said we want to launch blockchain as a service with you at DevCon one."
4. John (SPEAKER_02): "Exactly. Oh my god. Like that's like there are many parallels. Nothing like a good deadline."
5. Victor (SPEAKER_03): "Yes, exactly, especially with a big, you know, major partner that you know can make or break you, right? So yeah, just don't have live demos on the end of all of that as well."
6. John (SPEAKER_02): "Yeah, exactly. That's when it gets real risky. We actually, so when we did it... [bug story]"

I will format it this way, ensuring timestamps are preserved as much as possible or attributed to the correct block. Since I can't create new timestamps, I will group them by speaker.

Block [17:22] SPEAKER_03 (Victor) starts.
Block [17:49] SPEAKER_02 (John) starts.
The dialogue alternates rapidly. I will split the text in [17:22] between Victor and John based on content.

**Handling the [12:56] block:**
SPEAKER_03: "...crap like out there. So, yeah, how do you balance those two and kind of keep decentralized, do you think?"
SPEAKER_02: "Yeah, no, it is. I mean, it's kind of challenging. It's almost, uh, almost a paradox. Um, I think..."
Then [13:38] SPEAKER_02 continues.

**Word Count Check:**
Input is roughly 2500 words. I need to keep it high.

**Formatting:**
**[MM:SS] SPEAKER_XX:** Text.
Multi-paragraph: Keep speaker label only on first paragraph.

Let's go.**[00:01] SPEAKER_03:** Okay, we are live, and we have a very special episode today. We are talking about the future of art and NFTs, and we're joined by special guest and very old friend, John Crane. Welcome, John Crane.

**[00:19] SPEAKER_02:** Hey, Victor. Hey, everyone. Hey. Good to see you guys. Thanks for having me.

**[00:22] SPEAKER_03:** John Crane, of course, as everyone knows, is the founder of SuperRare. But do you want to give a quick intro for anyone who is not intimately familiar with all the amazing things you've done over the past couple of years?

**[00:35] SPEAKER_02:** Yeah, sure. So, yeah, my crypto journey started in around 2015, going to the Consensus hackathon where I met, at least, you know, three of the other folks on this call there. Yeah, I was, you know, before that, my background was kind of in art and technology. I worked in advertising. I studied architecture and structural engineering for undergrad. And, yeah, I was always really interested in when crypto and blockchain were going to intersect more with kind of consumer tech and just, you know, things that were a little bit past, you know, finance and trading. And so, yeah, when I saw NFTs, it was an instant win for digital art. So I doubled down immediately.

**[01:24] SPEAKER_04:** Do you remember how you heard about the hackathon or Ethereum generally? Obviously, we met there, but what was that? Yeah.

**[01:34] SPEAKER_02:** No, so I was kind of hanging out with the New York Bitcoin crowd. Yeah, I had actually met, I think, John Lillicrap, which I forgot, but I met him at the like the New York Bitcoin Center. I don't know if you guys remember that.

**[01:44] SPEAKER_04:** Yeah, we do.

**[01:45] SPEAKER_02:** Yeah, so I was hanging around and actually, I was like, I was super into Counterparty. So I was very much like Ethereum's too complicated, you know, Vitalik's full of it, it's not going to work. Um, and then the network launched and I was like, okay, I was wrong, like this is actually super cool. Like, you know, I have no problem changing. I was like, I was totally wrong, this is amazing. And I was just like Googling "Ethereum blockchain hacker". I was like trying to find, like, get deeper involved, you know. I was trying to like quit my day job and go full-time crypto. And so then I, I think I just Googled it and it was like, oh, there's this hackathon in two weeks. And I applied with Charles and then, yeah, met you guys.

**[02:34] SPEAKER_03:** Yeah, and to be clear, to let everyone know that we were blown away by you and your brother Charles' project. And we gave you, I think, your first job, both of you in Web3, right?

**[02:46] SPEAKER_02:** Yeah, yeah, yeah, for sure. Exactly. Yeah, I think the Monday after, I feel like I immediately quit and started working with you guys full-time on BlockApps.

**[02:58] SPEAKER_03:** Yeah, I think we tried to give you a job on the spot because you guys were— Yeah, yeah. Exactly. Exactly.

**[03:04] SPEAKER_02:** I remember there was like a couple week consulting transition period while, you know, yeah, I think that's true. Yeah. Maybe it was like, we started like hourly, like, you know, getting to know each other a little bit and then, um, full time.

**[03:17] SPEAKER_01:** Yeah. So with Counterparty, you, you could have been on Kraken. Yeah, exactly. If only.

**[03:27] SPEAKER_03:** So what inspired SuperRare? Like, you know, I know you when you were working with us, you kind of became our head of product and you were working on a bunch of those enterprise implementations. But what triggered you to kind of create SuperRare, which is for anyone who doesn't know, one of the first NFT platforms really out there?

**[03:49] SPEAKER_02:** Yeah, I, well, I mean, it was super interesting, right? You know, like we were all kind of on the ground floor at the Consensus office or like, you know, at least me and Kieren are hanging out there and like watching the ICO boom happen was fascinating. Because I was like, I remember me and Kieren talked a bunch about, you know, ERC-20 tokens and like, I found it was super interesting that it was this very small bit of standard. It's a super simple protocol, very simple code. But the adoption created this massive wealth generation. And even if there were also lots of scams, I'd say generally net positive for humans and the economy. It was incredible to see that happen.

And so then I saw some of the standards conversations around ERC-721 and like I saw the CryptoPunks launch. Um, and I was like, well, this is pretty crazy. If you think about the consumer web, it's all, you know, an image and a title tag and some metadata. So like it could be that like the entire consumer web turns into like NFTs and that, you know, like I don't know exactly what the business model is going to look like, but the total addressable market is probably pretty large. So that got me into NFTs. And then on the flip side of that, I was also kind of in and around the New York art scene, like going to the art fairs. I had friends who were looking for gallery representation and kind of part of the business of art. And it's just seemed obvious. I was like, oh, there's now a way to kind of like truly own digital assets. And this is obviously going to apply to digital art. So it's kind of like the marriage of, you know, like my interest in the tech side, but then also my interests and passions around art.

**[05:40] SPEAKER_03:** And like, what was it like to be at the forefront of like the NFT explosion? Because you guys, like, I know for a long time you were building and it was like, oh, you know, like, how's it going? And, you know, like no one is really paying attention. And all of a sudden, you know, next day, everyone's talking about NFTs.

**[06:02] SPEAKER_02:** It was absolutely crazy. It was hard to be like, it was just like completely surreal the whole time. Like it felt like a dream. Like we, you know, we started in 2018. We, you know, we were, we tried to raise money. It never really worked. Like by the time we raised, we were already, you know, cashflow positive and like making more than we were paying ourselves.

**[06:24] SPEAKER_03:** So that's the best situation to possibly be in.

**[06:26] SPEAKER_02:** Yeah. It was like, it was much easier to raise then than when I was like, I have this really cool idea. Um, so it was, yeah, it was like, you know, it was, it was a grind. It was super volatile. Many times I was just like, what am I doing with my life? Um, but, uh, yeah, then it just, it just really started. Like, I remember the numbers were like doubling every month for a while. And like, I remember it was October, 2020 was our first million dollar month in volume. And I was just like, this is wild, you know, because, but 12 months ago, we were like, all right. So the volume was like $5,000. We made a couple hundred bucks. Okay. Yeah.

**[07:10] SPEAKER_03:** And were you guys the first self minting NFT platform? I think like we're, we're trying to talk about that.

**[07:17] SPEAKER_02:** Yeah. We, yeah, we were the first to come like, I think there were maybe a couple other minting tools, but like we were the first to combine like the minting and the marketplace experience. So it was like, um, there weren't like great minting tools then. So we like, we started with the minting tool and then we're like, all right, I guess people need a place to sell this. So we'll like, we'll build the marketplace too. And you know, it's partially just out of necessity. Cause like the tooling sucked at the time.

**[07:47] SPEAKER_03:** Yeah, it's funny because I remember, if you recall, what later became the Flow guys doing CryptoKitties. They were based in Vancouver and I was talking to them about running it on our blockchain and doing that kind of stuff too at the time. And, I mean, you've done so much. One of the amazing things, it's the launch of the RARE token. And you guys seem to be one of the first projects that was really committed to sort of figuring out DAO governance in reality. Like, you know, what led to that and how did that go? Like, you know, what did you figure out there?

**[08:26] SPEAKER_02:** Yeah, I mean... You know, early on, I was like, part of like, what got me excited about Bitcoin and Ethereum is just the idea of these networks where, you know, if users of the networks also participate in upside of the network, you know, like there, there's the, you know, like the fat protocol article, um, that was super popular, like 2016. So just like thinking about like, okay, what does monetization look like? And can you build platforms that are, they're more like collaborative than extractive, where it's like, if you're Meta, you're just like, I'm just gonna extract as much metadata and sell ads, which is a great business, but partially for me, it was almost like a, a thought experiment of like, is it possible to build a network where you don't have to sell ads? And it could be like, maybe it's a marketplace as the business model. And then, you know, kind of, it's like collective ownership via the token. Um, so yeah, I was, you know, drinking, drinking a lot of the crypto Kool-Aid at the time.

**[09:32] SPEAKER_04:** Did you do it like classic ICO style? Was there like fixed price auction? How, how did the rare get in there?

**[09:40] UNKNOWN:** Yeah.

**[09:41] SPEAKER_02:** Yeah, we actually just did a huge airdrop, probably one of our mistakes. Yeah. So like we should have probably, you know, sold a bunch of tokens, but we actually just gave them away. Um, and yeah, I mean, yeah, there's plenty of challenges to like, you know, DAOs are hard to manage and run. Um, but you know, it's cool to see the current administration kind of like change tack and actually seem like they're interested in like building and pushing forward, um.

**[10:10] SPEAKER_03:** So what do you think the biggest challenge was in what do you think, you know, the biggest challenge was in running a DAO? Because I think all of us had that sort of as an ideal state with the crypto Kool-Aid, you know, running things completely decentralized. What do you think are, you know, the challenges you faced when you did it and that are still out there, do you think?

**[10:32] SPEAKER_02:** Yeah. I mean, I think still one of the bigger challenges is regulatory. Like you have, you know, like you're kind of like trying to read the tea leaves and then rather than just making like the bet, you're like, okay, well, this is the simplest, best decision. You're like, okay, well, this is not clear what this means. So maybe we should do this. And like, how do we, you know, not get in trouble for trying to experiment, um. And it's obviously, you know, the position is friendlier, but there's still no clear like rules. You know, it's like the obviously like the Gensler era of, you know, enforcement, uh, the dark, the dark ages, you know, Gary's gonna be turning up for a job somewhere soon.

**[11:14] SPEAKER_01:** Isn't it?

**[11:15] SPEAKER_03:** You know, yeah, man. Do you have any advice?

**[11:23] SPEAKER_04:** Do you think of it more like it should be like a representative democracy? Like should it be like passing bills in there? I think they're like, they're proposals and there's like delegation usually is the model.

**[11:36] SPEAKER_01:** Yeah.

**[11:37] SPEAKER_04:** It could also be like, just like you got a couple of leaders, but the stake could call a confidence vote or something. Or like people like futarchy too. I haven't tried it yet, but what's that? Like MetaDAO is trying to do that sort of thing.

**[11:51] UNKNOWN:** Yeah.

**[11:52] SPEAKER_02:** I think, I think it kind of depends on like specifically what you're doing. You know, if it's something like, you know, I mean, Bitcoin and Ethereum are obviously not DAOs, but just like, you know, where it's like if small changes can have potentially like catastrophic impact, I think that's one thing. If, you know, it's, you know, like SuperRare where it's like, if there's a, there's a low level protocol and there's application and like, you know, other than like the escrow contracts for auctions and things like the stakes are like fairly low. I do kind of like the idea of like you sort of like if you can empower like a team or a few individuals to kind of just keep going and then the token holders can say like tell people to stop versus like having to approve everything like that's a very silly arduous process and I feel like it should be more like okay if you're it's like veering off in the wrong direction you can like there's a way to kind of like raise your voice and have influence it but like, you know, having a vote on like what color the button should be or something is very absurd.

**[12:56] SPEAKER_03:** I'm curious, like, you know, given that you're a decentralization advocate, how do you balance like being a curated kind of platform and being open? You know, like how do you think about those two? Because I think one of the advantages of SuperRare with the curation side in art, you keep the quality very, very high. And, yeah, um, unlike, you know, more marketplace type NFT platforms which just frankly puts a ton of crap like out there. So, yeah, how do you balance those two and kind of keep decentralized, do you think?

**[13:38] SPEAKER_02:** Yeah, no, it is. I mean, it's kind of challenging. It's almost, uh, almost a paradox. Um, I think you know, we've kind of always taken the like minimal decentralization. So it's like you have it where it's useful. And then you're like, one example is like, we were like talking about like token models early on. It was like, maybe we'll have token holders vote on artists. And I was just like, that sounds like the most dramatic, terrible thing I could ever imagine. You know, it's like people voting, like your art's terrible. Like you're like, oh my word.

**[14:03] SPEAKER_04:** I mean, in the pump.fun streamer heyday, I think that it could have really worked during that period of time. Yeah, you know, maybe we could have people streaming. Yeah, it's like live voting, like, is the art good or bad? Watch this artist threaten to commit suicide.

**[14:20] SPEAKER_03:** I did put stuff on a dating project once where you basically had to be voted in based on your looks, which just seems horrible. Yeah. Very, very evil, you know.

**[14:33] SPEAKER_01:** But there's writing out a ton of pages, remember those?

**[14:35] SPEAKER_03:** Yes, yes, or Hot or Not or all of those. Oh, yeah, yeah. It's, yeah, just brutal. But, yeah, especially in places, you know, the art industry can be quite vicious.

**[14:49] SPEAKER_02:** Yeah, it's challenging and good art is subjective. I feel like the on-chain auctions, escrow on-chain, that makes a lot of sense. On-chain voting for which artists are good, that's kind of like let people who are, like, making decisions, like, do their thing. And then if it starts to be, you know, like, if things get out of hand, maybe, like, the token holders can, like, you know, raise awareness. But... Yeah. And, like, part of it, too, I mean, actually, early on, we were, like, thought we would be more of an open platform. And then as things progressed, there were more tools. Like, you know, we were just trying... It was, like, we were building things, trying to add value. And... there's a ton of open tooling. So like early on, we kind of thought we might have like SuperRare as like the ultra curated view into the market. And then maybe you have like, you know, another kind of like open platform that's anyone could use.

**[15:55] SPEAKER_03:** I'm curious, like what was the, like, what, like, you know, it's a two-sided market with market artists and art buyers. Like, what do you think, like, did you have to get the artist first to convince them? And how did you do that? Or did you have to get the artist?

**[16:13] SPEAKER_02:** Yeah, we, you know, you kind of had to get both first. So, I mean, we started, like, just, you know, out of, like, it really started as just me kind of, like, experimenting and building. And so we were, like, you know, started with the minting tools. I was going around, like, demoing, talking to people. And... I guess it first kind of piqued interest of the artists. We were talking about how it would work. And then when we first launched that, we kind of had... So there's Jason Bailey, who was kind of like an early digital art advocate, big writer. He runs a company called Club NFT that does NFT art backups.

**[17:00] UNKNOWN:** Yeah.

**[17:01] SPEAKER_02:** He hit us up and was like, hey guys, like, we've been talking to him and he was like, I know you're getting close with your product like, I want to buy this art on Monday. Um, can I, can I do it on SuperRare? And I like looked at Charlie and I was like, dude, Jason wants to, you know, buy something on mainnet on Monday. Like, what can we?

**[17:22] SPEAKER_03:** That was it, like 36 hours?

**[17:24] SPEAKER_02:** That Charlie was like, yeah, probably. And so then we basically stayed up for 36 hours, uh, fixing bugs.

**[17:30] SPEAKER_03:** And I'm getting flashbacks to when Microsoft said we want to launch blockchain as a service with you at DevCon one and we were like—

**[17:36] SPEAKER_02:** Exactly. Oh my god. Like that's like there are many parallels. Nothing like a good deadline.

**[17:39] SPEAKER_03:** Yes, exactly. Especially with a big, you know, major partner that you know can make or break you, right? So yeah, just don't have live demos on the end of all of that as well.

**[17:49] SPEAKER_02:** Yeah, exactly. That's when it gets real risky. We actually, so when we did it, there was a there's a funny bug with the like the React stuff. Um, so we were like live like helping. We were like live streaming or not live streaming but like screen sharing the transaction with this artist Robbie Barat and Jason. And we're like literally pushing fixes. It was like, oh, we didn't know. I didn't expect that to happen. Like, okay, one second. Like, all right, it's deployed. Just reload the page.

**[18:31] SPEAKER_03:** Lots of cash clearing. I remember about that. I'm curious what you see as the future of just generally like art and NFTs.

**[18:44] SPEAKER_04:** Can I jump in on this? Yeah, please. Take on it. So in DeFi, we're starting to see, like as the administration has cleared the way to some extent. It seems like, you know, there was a pent up demand for something like a TradFi DeFi merger. It's not all the way there yet, but it's, you know, getting to just be five. Like I see the path to that happening. Do you think like it's NFTs really stay sort of like a distinct asset class forever? I know, you know, maybe you could talk about your gallery. I know you started to do a lot of like physical sales. Yeah. Et cetera. Like, does it kind of, or, you know, do they merge? Do they not? Do they? Yeah.

**[19:29] SPEAKER_03:** Like, like trad art become NFT art and digital art or like.

**[19:35] SPEAKER_02:** Yeah. I, you know, I like the NFT stuff. I do think kind of just like eventually fades into the background. Like the real zero to one is, you know, cryptographically secure provenance. So, you know, you could use that for physical art. You could use it for digital. I think it was like, more of a breakthrough with digital because you can kind of argue the token is the art. You now have this, you know, more liquid asset. Um, so for art specifically, yeah, it's kind of just becoming part of the market and I think you'll see NFTs, you know, used with digital art obviously but also with physical art. Like no one's really if you like, the lack of good data on provenance in the art market and collectibles in general is kind of amazing. It's still like, oh, there's a sticker on the back that says it was from this gallery. Probably it was. Probably it was? Nobody knows. And also I think, you know, like a lot of people are like really trying to tie the physical asset to the digital asset, which I think is a waste of time personally. It's like, if you have the physical asset and you also have custody of the certificate of authenticity, like that's kind of good enough. You don't really need some complicated tech solution there. And it's hard to imagine a world in which, you know, like collectors and like customers that you just want, like, I personally have like a higher perceived value for physical art that also has an NFT with it. Yeah. Um, and I think in general, that trend continues. So I think digital art will kind of just become a bigger part of the contemporary art market. And then eventually we'll see NFTs used as certificates of authenticity, um, you know, for all, you know, high value objects.

**[21:25] SPEAKER_03:** Yeah, I mean, one of the big things I didn't realize is that a friend of mine is an artist and she often gets a request for the value that was paid for it because someone wants to insure it, right? And there's this whole downstream kind of economy.

**[21:41] SPEAKER_02:** Insurance, appraisal, lending, you need much better. And so it's like, I mean, Kieren, you and I have talked about the lending stuff a little bit. I think the lending market for these types of assets is small just because there's not good information. You could probably really grow that pie quite a bit if you do have easier access to provenance information.

**[22:04] SPEAKER_04:** Let me add a little on that front. So I felt having been more of an NFT style RWA marketplace for a while and gone more DeFi, I thought that people wanted to tokenize to sell things at first, and this is true, but I think it is better that they tokenize to unlock liquidity in selling could be one way, but people kind of want to hold on to stuff. Like, I don't want to sell my ETH. I don't want to sell my, you know, et cetera. Yeah. You would know better than us. At the very high end of the market, you know, if you get like a wealth manager, they might extend some credit against your Picasso, right? But for everybody else, and you probably have to have a lot of separate money for that, too. You can't really, like... I don't know if people fire sell their art, but tends to sit there. And I used to think that was bad, but maybe it should sit there. But the credit markets actually just make it liquid, you know, as we've as we've discussed before, which I think would be super cool. Like, yeah, I'm surprised we're getting into that world, but we're not.

**[23:12] SPEAKER_02:** Yeah, I think we're seeing it. I feel like there's the green shoots of like, OK, here's what's possible. It totally makes sense. I think just like NFTs almost, this is like, they're a great, you know, like we've talked, a lot of people in crypto love talking about identity and stuff. And like, to me, it's like NFTs are like a beautiful, very simple digital identity for whatever. You can pack anything you want in that metadata. It's just like a packet full of stuff. It's very simple. They're unique. They're pointers to one specific thing.

**[23:43] SPEAKER_03:** Yeah, I mean, I love the way you talk about, you know, NFTs as certificates of authenticity, because I didn't realize this. We looked into like the physical art market for a while and like every auction at Sotheby's when they have a big piece, like they have to research it effectively from scratch, right? Like they have to build that entire chain of provenance with every piece that they do, which is an insane amount of work every single time.

**[24:09] SPEAKER_02:** Yeah, it's a very high friction process. Like the transactions are very, very high friction, which is good. You know, like depending on where your position is in the market, like obviously Sotheby's loves being the, you know, the keeper of all secrets and information. But I think that's clearly going to be disintermediated with technology.

**[24:30] SPEAKER_04:** Any new assets or maybe are you guys, you know, just to declare war on the auction houses, houses, you know,

**[24:38] SPEAKER_02:** other high-end physical goods? What, uh, yeah, I mean we're focusing like our expansion like, you know, we launched the gallery earlier this year. Um, offline gallery, it's on the Bowery, um, right next to New Museum. And, you know, we're showing physical digital art, you know, installations, you know, projections, all sorts of different things. And, yeah, I think like, you know, our view like, if you look at the models, the galleries are not doing great business-wise. The auction houses are hurting. I think everyone's trying to find a more sustainable model.

**[25:17] SPEAKER_04:** Stuff is so illiquid, right? I don't mean to interrupt, right? I think the norm is stuff sitting five years, 10 years. It's feast or famine. If we print a bunch of money, probably get a bunch of transactions.

**[25:30] SPEAKER_02:** Just wait. 2021, people were just buying Picassos on their phones online. And Crazy Apes, right? So everything, every year like Ether Rocks. I remember when Ether Rocks were like the price is exploding and I was like this is truly amazing. Yeah. Um, but yeah, I think like the models have to change. And, you know, just as like, if you think what the internet's done as far as like shopping, right? It's like, you can price compare easily on your phone in any stores, right? There's no kind of like price arbitrage. You're like, you're going to look up the price of something. You can scan something, figuring it like ask ChatGPT, what is, you know, what is this? How much should it cost? And so I think like, the art world has really, it has been like an insider's game of who knows who and like, what's the real price, like the marketed price versus like what was actually paid. And I think that's gonna like, it's kind of slowly like unwinding and we'll see, we'll end up with a market structure where pricing is just much more transparent. You can see things on chain. And I mean, I think that's, you know, like that's kind of like part of the opportunity is as the market becomes more efficient, we'll have the best tools to to service the new structure.

**[26:49] SPEAKER_04:** So it sounds like even the big guys want

**[26:51] SPEAKER_02:** more liquidity but they're not willing to like let go of their proprietary information advantage, I guess.

**[26:55] SPEAKER_04:** Yeah, yeah. Exactly. And I, but it's a nice. Like that's a kind of also the paradox. It's like you'll have more liquidity if it's better access to information but like, you know, it's the classic, uh, what's the, the Innovator's Dilemma?

**[27:14] SPEAKER_02:** The Innovator's Dilemma.

**[27:15] SPEAKER_04:** Let me, tip my time. Yeah, classic Innovator's Dilemma.

**[27:20] SPEAKER_03:** Well, I, I think some of the auction houses are even trying to offer loans to try and lock people up even longer. Right. To, to their places.

**[27:29] SPEAKER_02:** Yeah, they have, um, I mean, I, like they're all Christie's inside of it. Like a lot of the big, or most of the auction houses are private. So I don't know how big their businesses are, but they do have, um, yeah. There's like you know people will like inherit art and it's like they don't really care necessarily and their advisor was like don't sell that you should just take out a loan and so they do have them but that seems like a classic conflict of interest to your point right like, like oh we'll tell you how much it's worth and we'll loan you based on that. Yeah, it's very one-sided and you can't really shop it around. It's like ultra specialized information.

**[28:07] SPEAKER_03:** Jim, did you want to ask a question? You look like you came off mute.

**[28:11] SPEAKER_00:** Well, it's a little bit of a different topic, but I'll throw it in right now anyway. What has been the effect for good or bad of AI and art on what you're doing?

**[28:23] SPEAKER_02:** Yeah. As far as the startup goes, it's been great. We had a little robot in our Slack you can talk to that does things for you. As far as the art market goes, I think it's all, I mean, it's also been kind of great. Like in my mind, this is just like, you know, it's a new tool that unlocks creative, you know, like you can kind of like do different creative things. You're encouraging it then.

**[28:43] UNKNOWN:** Yeah. Oh yeah.

**[28:44] SPEAKER_02:** We have like tons of artists use AI. I mean, you know, there's also tons of artists we work with who hate it and, you know, think it's the end of all creativity. I think just like, you know, if you look, I think like what it really enables is like somebody to do more complex things. You know, it's like where you can like all the grunt work you don't have to do. So now maybe it's instead of making one still image, you're going to do insane world building where it's like you can go in, you can, you know, like the art's just more interactive and. And actually the first art we ever sold on SuperRare was kind of like generated via like GANs, like adversarial networks, like voting on outcomes. So I think, you know, it's inevitable, it's going to happen. It's kind of like, you know, digital cameras were the end of photography and they obviously were not.

**[29:45] SPEAKER_03:** Um, but do you, do you think like, you know, going back to the metadata and certificates of authority that proving some part was based, you know, done by a human will be valued into art or, or any kind of creation going forward?

**[30:01] SPEAKER_02:** Yeah. I mean, I think, yeah, just like if you, you know, it's like, it's super amazing to see like the rate at which content's being created and like, you know, people, it's like you can watch a video of like, that person didn't actually say that, but it looks like they did. I think that's where you're like, nobody ever answers a random phone number. If someone's calling you and it's not in your phone, you're like, I literally never answer this. Like, I don't know who does that. You'd have to be like pretty insane. It's sort of like you've kind of certified like the numbers, you know, and I think it'll end up being the same with like content and like art and stuff where it's like, if it isn't, you know, signed somehow cryptographically, you'll probably just assume it's fake because there's no real way to know.

**[30:48] SPEAKER_01:** Have you seen much interest on the Bitcoin side in terms of Ordinals and inscriptions and stamps and runes? Like how is that looking?

**[31:02] SPEAKER_02:** Yeah, we've done a couple projects on Runes with artists. And yeah, it's super interesting. You know, we're... Yeah, I think there's going to be art on many blockchains. Obviously, Bitcoin and Ethereum being the most secure probably have the highest likelihood of it lasting. But yeah, it's actually people really like Ordinals. It's funny. One of the sort of paradoxes that are like the funny things we ran into is like early on, we would talk to like investors and they're like, you need to get rid of the wallet. It's too complicated, but actually it kind of ends up being this, like, you gotta know all the right terms. It's almost like you get the secret incantation, you get inducted into the club and you know how it works. And so like, um, I think people really like that. Ordinals are a little more complex and like harder to understand than, uh, NFTs on Ethereum. Um, which is just, yeah, it's sort of, that's a funny anecdote, but, uh, yeah, they're quite popular. I, you know, I think they'll be around for a while.

**[32:04] SPEAKER_01:** And I mean, another difference you have there, right, is that they're doing the data carrying on chain as well versus an external URL, which is another interesting difference. Yeah. Yeah, totally.

**[32:17] SPEAKER_03:** I'm curious about the decision to, you know, you mentioned starting the gallery and like everyone's talking about RWAs and kind of bringing real world stuff into the blockchain, but you're kind of doing the opposite. Like what was the decision to start a physical gallery and why did you decide that was a logical next step for you guys?

**[32:38] SPEAKER_02:** Yeah. I mean, just. You know, it's part, it's kind of part of like how, you know, like the, the market works. So like, you know, people like getting together and like, a lot of the art, you know, it's like you can look at it on your phone but if you see it, you know, on the huge projector there's like, you know, a 10 by 10, uh, CRT like TV wall, um, it really looks different. So I think, you know, part of it is like, it's community building. It's a space people can show up. And then part of it's like, you know, like the art really does just look different. So I think, you know, as far as like NFT is still, you know, people are like, okay, these are just nonsense. JPEGs there, you know, like it's, you know, it's Ether Rocks 2.0 or like, and so like, it's kind of like telling the story to everyone else. Because at the end of the day, it's still like, you know, it's, it's a demand constrained market and we're, you know, we're trying to grow the collector base.

**[33:34] SPEAKER_03:** Beyond art, what do you see as like the next area? Like, you know, what's the next areas that are kind of going to need these kind of provenance or these kind of certificates of authority? I mean, I can think of a million, but I'm just curious from your point of view, where do you see the next elements kind of getting into it first?

**[33:56] SPEAKER_02:** Yeah, I mean, I think in general it's like, you know, like luxury assets with like NFTs are still more expensive to create than like not having one, you know, like you just print one out and then the ID lives in your database. Yeah. And I think but it's going to be like the customers are going to have to demand it because a lot of the brokers and folks, they do their information advantage. And so they don't really want this to exist. But I think it just makes so much sense. It's just hard to imagine that it doesn't happen. There's people taking wine very seriously, issuing NFTs and building secondary markets. I think part of it's like... an asset that's kind of fun to speculate on but also you do, you know, there's, you know, a high likelihood you might, you know, have somebody send you the NFT. It's like kind of like wine. Watches, um, yeah. Handbags, I think are a big one.

**[35:03] SPEAKER_03:** Like, exactly. Yeah, one of the really popular ones right now is, uh, trading cards. So they're like, um, you know, what people like is like Courtyard is still going, right?

**[35:11] SPEAKER_02:** Yeah, they're doing great. Yeah, it's, uh, you know, kind of like you have the speculative aspect but also like, if you're a serious collector you can, you know, get, get real, get real things.

**[35:22] SPEAKER_03:** Okay, last question for you, because unless anyone else has one, but...

**[35:31] SPEAKER_02:** Yeah, yeah.

**[35:33] SPEAKER_03:** What are you most excited about in any aspect of the blockchain space right now?

**[35:45] SPEAKER_02:** Most excited? I mean, it's like... it's obviously like, we, you know, like we've all been working on this for like a super long time, but I do think like, if you look at even just like, you know, BlackRock putting treasuries on chain with different partners, like art's moving on chain, like, like, everything literally is going to become is moving on chain. Like, I think it's like, that's actually finally, it used to just be like a mantra people would say to like, you know, help themselves feel important. But like, I think we're finally getting there. We're like, holy fuck, like, everything is moving on chain, like that's actually happening. So it's like, you know, real world assets, digital assets. I think just like, yeah, liquidity is increasing. I think it's generally net positive for everyone. It feels actually like it's finally happening.

**[36:38] SPEAKER_03:** Yeah, it's taken way longer, 10 years, but we're still here and we're still doing it.

**[36:44] SPEAKER_04:** We can make a thumbnail like the Ron Paul that's happening. Exactly.

**[36:50] SPEAKER_03:** We need the mission accomplished banner.

**[36:52] SPEAKER_01:** Yeah. Oh my goodness.

**[36:54] SPEAKER_03:** Yeah, exactly. Well, John, thank you for your time. And as always— Um, we're really glad that you're doing so well. And where can people find you and, um, learn more about all the stuff you do?

**[37:08] SPEAKER_02:** Yeah. Uh, on X, uh, at SuperRare John, um, at SuperRare. Uh, yeah, we're, uh, yeah, you should also, there's currently a show at the gallery that's wrapping up, but we have a new, there's an Xcopy show December 10th. So if anyone's in town. Awesome. You said the manual at the gallery one more time. I missed it. Oh, yeah. Offline by SuperRare. Offline by SuperRare.

**[37:34] SPEAKER_03:** Well, awesome. Thank you for joining us and take care, everyone. Thank you.

**[37:39] SPEAKER_02:** Thanks for having me.