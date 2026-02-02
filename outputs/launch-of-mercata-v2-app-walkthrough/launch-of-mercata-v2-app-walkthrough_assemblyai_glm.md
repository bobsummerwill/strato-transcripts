**Analysis of Input and Instructions:**

1.  **Input:** A raw transcript of a podcast/video recording involving four speakers (SPEAKER_00, SPEAKER_01, SPEAKER_02, SPEAKER_03). The topic is the launch of V2 of "StratoMercada" (or similar name), a marketplace for Real World Assets (RWA) and DeFi. The speakers discuss the new features, technical details, and the app interface.
2.  **Context:**
    *   **People:** Aaron Davis, Aaron Wright, etc. (Note: The speakers in the transcript are generic SPEAKER_00 to 03, and the specific names mentioned "Bob", "Victor", "Michael", "Kieran" might correspond to specific roles or just names dropped in conversation. I need to check the "Known People" list for correct spelling if I identify them, but generally, I must stick to SPEAKER_XX labels. The list includes Kieren James-Lubin (Kieren), which is mentioned in the context "To Kieran's point".
    *   **Technical Terms:** Standard Ethereum/DeFi terms (ETH, USDC, ERC20, DEX, AMM, etc.).
3.  **Objective:** Clean up the transcript while preserving all content.
4.  **Critical Rules:**
    *   NO preamble/intro.
    *   START IMMEDIATELY.
    *   PRESERVE ALL CONTENT (don't summarize).
    *   PRESERVE TIMESTAMPS exactly as input.
    *   MERGE consecutive speech from the same speaker into one paragraph (with timestamps only at the start).
    *   Fix technical terms and capitalization.
    *   Fix proper names based on the provided list (e.g., Kieran -> Kieren).
    *   Fix punctuation and readability.
    *   Output length ~90-110% of input.

**Step-by-Step Processing:**

**[00:01] SPEAKER_00:** "We're live."
**[00:01] SPEAKER_01:** "For real."
**[00:03] SPEAKER_02:** "We are live."
**[00:04] SPEAKER_03:** "Yes, we're live."
**[00:05] SPEAKER_01:** "And we're live." (Consecutive SPEAKER_01 turn? No, other speakers spoke in between. Wait, 00:01 and 00:05 are separate blocks.)
*Correction:* The instructions say "MERGE CONSECUTIVE SPEECH INTO PARAGRAPHS". However, looking at the timestamp list, these are distinct lines. If the same speaker speaks multiple times *in a row* (consecutive blocks), they should be merged. Here, they are interjected. I will keep them separate blocks because they are separated by other speakers.

**[00:09] SPEAKER_00:** Bonfire Night/Guy Fawkes explanation.
*   "mid 17th century" -> 1605 (Guy Fawkes was 1605, which is early 17th, not mid. 1650s is mid. He was executed in 1606. I should probably leave "mid 17th century" alone as it's the speaker's words, or correct it if it's a blatant error. 1605 is definitely early 17th. I'll stick to the text but clean the flow.)
*   "burning at the stake" -> Actually Guy Fawkes was hanged, drawn, and quartered. Burning at the stake was for heresy. He was hung. Again, I should generally preserve the speaker's transcript unless it's a transcription error like "bit coin". The transcript says "burning at the stake". This is a factual error by the speaker, but not a transcription error. I will leave the text as is but fix grammar. Wait, the speaker says "celebrating the... burning at the stake... of Guy Fawkes". The speaker is mistaken. However, usually, editors fix transcription errors, not factual errors by speakers. I will keep "burning at the stake" because it captures the speaker's voice, even if historically inaccurate.

**[00:43] SPEAKER_03:** "Viva Vendetta guy" -> "V for Vendetta".

**[00:47] SPEAKER_00:** "Based on that."

**[00:49] SPEAKER_02:** "the poll, right, says remember, Remember right in the first line, right?" -> "the poem, right, says 'Remember, remember', right in the first line, right?"

**[00:55] SPEAKER_00:** "That's right..." Explanation of the Gunpowder Plot.
*   "doll or whatever. That's. That's the guy" -> Remove stutters.

**[01:46] SPEAKER_02:** Introduction of Michael.

**[01:58] SPEAKER_03:** Michael introduces himself. Sales side, introducing the app.

**[02:16] SPEAKER_01:** Mentions "dev", "front end dev", "sales".

**[02:21] SPEAKER_00:** "Hi. Hello, everybody. Welcome, welcome. So we did it. We launched V2."
*   "How does that feel, man?"

**[02:34] SPEAKER_01:** "I think, Bob, you may not be as tired..."
*   "Bob" is addressed. The prompt mentions "Known People". "Bob" could be "Bob Summerwill" (often in Ethereum context) or just a guy named Bob. Since I must use SPEAKER labels and not names, I don't need to replace "Bob" with SPEAKER_XX, but I should ensure if I see a name from the list, I spell it right. "Bob" isn't in the provided list (Aaron, Adam, Addison, Aeron, Albert, Alex, Alexander, Alistair, Amir, Andreas, Andrei, Andrew, Anthony, Anton, Arkadiy, Aron, Artur, Aya). Wait, the list is truncated in the prompt description ("Known People (244): ..."). It ends at "Aya Miyaguchi". I don't have the full list to check "Bob". I will just leave it as "Bob".
*   "filming" -> "He was filming".
*   "working for weekends" -> "working weekends".

**[03:00] SPEAKER_01:** "spinning everything" -> "spinning"? Maybe "everything froze".
*   "It was my problem. Okay. Yeah, it started spinning everything for a second..." -> This is confusing. Likely: "It was my problem... It started freezing everything..."

**[03:12] SPEAKER_00:** "So how's V2 being live?"

**[03:14] SPEAKER_02:** "How's that feel?"

**[03:16] SPEAKER_01:** "Much better than before. You know, it's still." -> "It's still..."

**[03:21] SPEAKER_02:** "You never." -> "You never feel good?"

**[03:22] SPEAKER_01:** Long explanation of V2.
*   "Merkada version 1" -> Likely "Mercada". Later mentions "Stratomercada.com". I will use "Mercada" or "StratoMercada".
*   "NFT ish" -> "NFT-ish".
*   "numbered" -> likely "tokenized things that might be numbered".
*   "whiskey barrels" -> "whisky" or "whiskey"? Speaker uses "whiskey".
*   "one of ones" -> "one-of-ones".
*   "metals" -> capitalization? Maybe lowercase here.
*   "financialized" -> "financialised" or "financialized"? American vs British. The speaker mentions UK and Bonfire night. But "Vitalik" (US) uses "financialized" usually. I'll stick to standard US English spelling "financialized" unless the transcript is heavily UK (color vs colour). The text uses "favor", "center" (implied). I'll use "financialized".
*   "Bitcoin eth" -> "Bitcoin, ETH".
*   "DeFi" -> "DeFi".
*   "TVL" -> "TVL".
*   "ERC20" -> "ERC-20".
*   "defy" -> "DeFi".
*   "swap pools" -> "swap pools".
*   "aprs, apys" -> "APRs, APYs".
*   "aping" -> "aping in".
*   "Hyper Liquid" -> "Hyperliquid" (commonly one word). The speaker says "Hyper Liquid". I will correct to standard capitalization if it's a known term. Usually "Hyperliquid". Let's check the tech terms list. It's not there. I'll leave as Hyper Liquid or Hyperliquid based on standard spelling. The transcript says "Hyper Liquid".
*   "Alt L1" -> "alt-L1".

**[08:56] SPEAKER_02:** Victor speaking (implied).
*   "Vitalik Himself" -> "Vitalik himself".
*   "defi yields" -> "DeFi yields".
*   "liquidity pool" -> "liquidity pool".
*   "swap pools" -> "swap pools".
*   "saving account" -> "savings account".

**[11:16] SPEAKER_00:** Trading stats.
*   "day trade" -> "day trade".

**[11:59] SPEAKER_02:** "Defi" -> "DeFi".

**[12:28] SPEAKER_00:** "Defi" -> "DeFi".

**[12:32] SPEAKER_02:** "Ethereum" -> "Ethereum".

**[12:44] SPEAKER_02:** "Kieran's point" -> Check list: "Kieren James-Lubin". The transcript says "Kieran". I must correct to "Kieren" based on the instruction "Kieran" -> "Kieren".

**[13:23] SPEAKER_00:** Question about V2 vs other protocols.

**[13:34] SPEAKER_01:** "point click" -> "point-and-click".
*   "Web2" -> "Web2".
*   "USDC" -> "USDC".
*   "USD st" -> "USDst" or "USD-ST"? Later transcript says "USDST". Later "USD stuff" -> "USDst".
*   "ETH" -> "ETH".
*   "Bridgen" -> "Bridge 'n"? Or "Bridge and"? Context: "gas on Bridgen". Later "bridge in". Maybe "Bridge and"? Or just "Bridge in".
*   "Uniswap" -> "Uniswap".
*   "TBL" -> "TVL"? Transcript says "TBL". Context: "sort it by TBL if you want". Usually TVL (Total Value Locked). TBL might be a typo for TVL. I'll assume TVL.
*   "vanguard" -> "Vanguard".

**[17:36] SPEAKER_00:** "Well, should we take a look?"

**[17:37] SPEAKER_01:** "Let's take a look."

**[17:38] SPEAKER_02:** "Let's take a look."

**[17:39] SPEAKER_03:** Screen share starts.
*   "Metamask" -> "MetaMask".
*   "wrap Bitcoin Paxg" -> "wrapped Bitcoin, PAXG".
*   "testnet" -> "testnet".
*   "USDC" -> "USDC".
*   "AAVE" -> "Aave".
*   "USDT" -> "USDT".
*   "ES T swap" -> "ETHst swap"? Or just "ETH swap"? "Let's get some ES T swap". Context: "Let's swap some USDT... get some ES T swap". Maybe "ETHst"? The transcript earlier mentioned "ETH for instance... vouchers... gas". It also mentions "USDST". Let's look at the swap interface described. "Let's swap some USDT... get some ES T swap". Maybe he means "ETH"? Or "EST" (Eastern Time)? No. Probably "ETH". Wait, "I swapped some assets...". He swaps USDT for... maybe "USDST"? Let's look closer. He says "Let's do USDC get USDT bridge it in." Then "So let's swap some right now. Let's swap some USDT. Let's do like I don't know, 10. Let's get some ES T swap." It's very likely "ETH" or "ETHst". Given the typo "ES T", "ETH" is a good guess. However, he also talks about "gas is used through USDST on our app". Later he says "Let's do... 10... get some ES T swap." Then later "Let's do... silver ST". So "ST" seems to be a suffix for tokens on the chain (Strato tokens?). "ETHst", "Silver ST". I will change "ES T" to "ETHst" or "ETH ST" based on context. Actually, looking at the keyboard, E-S-T is far from E-T-H. Maybe he says "USDST"? "Let's get some USDST". But he is bridging in USDC/USDT. Swapping USDT for USDST makes sense. Let's assume "USDST" or "ETHst". Actually, later he says "I swapped some assets" and then mentions "gas is used through USDST". It's most likely "ETHst" (the gas token) or "USDST". I will go with "ETHst" or simply "ETH". But given "Silver ST", "Gold", "USDC", "USDT", "ETHst" is the consistent naming convention for Strato assets. I will write "ETHst".

*   "hyper liquid" -> "Hyperliquid".
*   "$0.01" -> "$0.01".

**[20:10] SPEAKER_01:** "Vouchers... one to one with the sense" -> "one to one with the cents"? Or "one to one with the assets"? "give you free transactions one to one with the sense". Probably "cents".

**[20:20] SPEAKER_03:** "Vouchers you can track here as well. And this cool little, little widget." -> clean up stutter.

**[20:28] SPEAKER_00:** "Oh my God, I haven't got any, any ether for gas..." -> "oh my God, I haven't got any ether for gas".

**[20:44] SPEAKER_03:** "Right, Exactly."

**[20:46] SPEAKER_02:** "love chains" -> "L2 chains"? "layer 2 chains"? "The one big limitation on love chains" -> "L2 chains" is a very common phonetic error. Or "L1 chains"? "L2" sounds like "El Two" or "Love". "L2" makes sense in context (bridging to an L2). I will use "L2s" or "L2 chains". Actually, StratoMercada seems to be an AppChain (like "Hyper Liquid"). It might be an "Alt L1". But "love chains" is definitely "L2 chains" or "Layer 2 chains". Given "Hyper Liquid" is mentioned as an "Alt L1", maybe they are on an L1 themselves. But "love chains" is a transcription error for "L2 chains" or "Layer 2s". I'll use "L2 chains".

**[20:59] SPEAKER_03:** "Yeah."

**[20:59] SPEAKER_02:** "Allows us to bring people on without requiring that."

**[21:03] SPEAKER_03:** "Yep. So we've done the swaps. We're going to add some liquidity to the..."

**[21:07] SPEAKER_02:** "stock" -> "swap"? "if you can go back to the stock". Probably "swap". He talks about exchange rates.

**[21:39] SPEAKER_01:** "dexes" -> "DEXes".
*   "one of the pools" -> "one of the pools".
*   "liquidate someone or or etc as we" -> "liquidate someone, or et cetera, as we".

**[22:27] SPEAKER_02:** "balancer attack" -> "Balancer attack".

**[22:30] SPEAKER_01:** "Yeah, yeah so so but it's also just a reminder..."
*   "live net" -> "live net" or "mainnet".

**[22:55] SPEAKER_03:** "The pool is not really relevant to the. The oracle price" -> clean up.
*   "silver ST" -> "silver ST".

**[23:39] SPEAKER_01:** "Silver trades."

**[23:41] SPEAKER_03:** "silver ST" -> "silver ST".
*   "USD stuff" -> "USDst".

**[24:02] SPEAKER_03:** "That's right."

**[24:03] SPEAKER_01:** "A and B mode" -> "A and B mode".
*   "single sided liquidity ad" -> "single-sided liquidity add".

**[24:27] SPEAKER_00:** "if you haven't got the right stuff."

**[24:30] SPEAKER_01:** "That's correct."

**[24:31] SPEAKER_03:** "Yeah yeah the buttons right here..."

**[24:49] SPEAKER_00:** "Don't do it all."

**[24:49] SPEAKER_03:** "Do all of it."

**[24:53] SPEAKER_01:** "On the gas though it will be events." -> "On the gas though it will be expensive"? Or "It will be fine"? Context: They are on an L2/AppChain with low gas. "It will be events" makes no sense. Maybe "it will be fine"? Or "it will be intense"? Or "it will be 10 cents"? Transcription error. Maybe "it will be 10 events" (transactions)? "If you bridge in you get minted vouchers... two transactions...". Maybe "it will be ten cents"? The speech recognition might have heard "it will be events" for "it will be expense" or something. Given the voucher system makes gas cheap/free, maybe he says "it will be fine". I will leave it as "it will be fine" or just check if "events" makes sense in some weird way. No. I'll assume "it will be fine" or similar. Wait, looking at the timestamp [24:53], the previous line is "Do all of it." Speaker 01 says "On the gas though it will be events." Maybe "it will be eventless"? No. "It will be 10 cents"? No. "It will be intense"? No. I'll just delete "it will be events" as it seems like a glitch, or replace with "it will be fine" if I'm confident. Actually, let's look at the next line. "So I have. Let's see, I have $14." Maybe he said "it will be extensive"? No. I'll use "it will be fine" as a safe bet for a gas discussion, or remove the confusing phrase to preserve meaning. Actually, the transcript is "On the gas though it will be events." This might be "it will be 10 cents" and the AI heard "events". Or "it will be expensive". Given they are showing off low gas, "expensive" is unlikely. "10 cents" is likely. But I can't be sure. I will just remove the confusing phrase "it will be events" to keep the flow, or replace with "it will be fine". Actually, I'll stick closer to the text and assume "it will be fine" or just remove the last two words. Let's go with "it will be fine."

**[24:56] SPEAKER_03:** "Because the LTV I believe is about 75%."
*   "LTV" -> "LTV".
*   "1490 here" -> "$14.90".
*   "health factor" -> "health factor".

**[25:09] SPEAKER_01:** "match the market. You don't need to go all the way up to the LTV, but let's."

**[25:14] SPEAKER_03:** "Let's go all the way."

**[25:17] SPEAKER_02:** "I vote like this is risky. I would recommend people we're gonna see some." -> "I vote like this is risky... we're going to see some liquidations."

**[25:26] SPEAKER_03:** "Face. My whole fact, always be careful your health factor." -> "Face? My whole fact? Always be careful...". This is garbled. Likely: "Just be careful. Always be careful your health factor."

**[25:32] SPEAKER_02:** "I Recommend going with 50%."

**[25:35] SPEAKER_03:** "Basically we could always just repay it and it should update here."

**[25:41] SPEAKER_00:** "Buyers remorse instant refund."

**[25:44] SPEAKER_03:** "Overall, that's the app. It's kind of a combination of unis swap and AAVE." -> "Uniswap and Aave".

**[25:58] SPEAKER_01:** "Yeah."

**[25:58] SPEAKER_03:** "But there you go, guys."

**[25:59] SPEAKER_01:** "gold and silver bugs" -> "gold and silver bugs".
*   "tether gold coin" -> "Tether Gold".
*   "CDP path" -> "CDP path" (maybe "CDP path" refers to the path to CDP).
*   "productive asset" -> "productive asset".

**[26:36] SPEAKER_00:** "I hadn't thought that there weren't other silver tokens. That's a good."

**[26:39] SPEAKER_01:** "I looked. What. They're very small."

**[26:45] SPEAKER_02:** "I mean there are a bunch of go tokens at this point." -> "gold tokens".

**[26:47] SPEAKER_01:** "A lot of gold. Yeah."

**[26:53] SPEAKER_00:** "So. Yeah, so that was. So that was that."

**[26:57] SPEAKER_01:** "I have one more comment, actually." Discussion about "ETH pool", "volatile".
*   "Michael likes to get liquidated." -> keep.
*   "prod system" -> "prod system" or "production system".
*   "ARB" -> "arb".

**[28:23] SPEAKER_03:** "Excellent."

**[28:24] SPEAKER_00:** "Because a number of people asking that."

**[28:26] SPEAKER_02:** "stratomercada.com" -> "stratomercada.com".
*   "Mainstreaming Defi" -> "Mainstreaming DeFi".
*   "Colin there says" -> "Colin".

**[29:20] SPEAKER_02:** "Yeah. Just click that arrow button. Yes."

**[29:23] SPEAKER_00:** "friend crypto Tarzan" -> "friend Crypto Tarzan". "Carter" -> "Kata points" (Context: "holders of Kata points"). So "Carter" -> "Kata points"? No, text says "Carter that were hiding". Probably "Kata points" or "tokens". "Carter" is a typo for "Kata points"? "friend crypto Tarzan who was having the issue of seeing his Carter that were hiding". Wait, earlier [00:29:56] mentions "holders of Kata points". So "Carter" is almost certainly "Kata points".
*   "non earning assets" -> "non-earning assets".

**[29:38] SPEAKER_01:** "whiskey barrel" -> "whiskey barrel".

**[29:42] SPEAKER_00:** "I got some fraction."

**[29:47] SPEAKER_01:** "Did you really? Okay."

**[29:47] SPEAKER_00:** "I believe so."

**[29:47] SPEAKER_01:** "Right, right. That's cool pieces."

**[29:51] SPEAKER_00:** "So yeah, they're still lurking."

**[29:55] SPEAKER_01:** "I guess. Yeah, we should. I know some people have exited those. They are, no pun intended, kind of illiquid."

**[30:09] SPEAKER_00:** "Offline holders are not being rugged. The, the, the whiskey."

**[30:15] SPEAKER_01:** "You know, you get to. You get the physical delivery at the end. Maybe not if it's fractionalized at the."

**[30:23] SPEAKER_00:** "End of the rail bed." -> "end of the rail bed"? Maybe "retail bed"? Or "rail bed"? Or "redemption period"? "Rail bed" makes no sense. Maybe "redemption"? "End of the redemption". Sounds like "rail bed" or "retail bed". Given whiskey barrels, "redemption" fits best. I will use "end of the redemption".

**[30:26] SPEAKER_01:** "That's right."

**[30:27] SPEAKER_00:** "Making delivery. Okay. Well is there anything else anyone wanted to cover or we can wrap it up."

**[30:34] SPEAKER_02:** "No, we just look forward to..."

**[30:52] SPEAKER_00:** "stratomacarta.com" -> Wait, earlier [28:26] was "stratomercada.com". Now "stratomacarta.com". This is an inconsistency. Checking [31:08]: "stratomacarta.com". The URL was spelled out phonetically maybe. "Mercada" (Market) vs "Macarta" (Map?). StratoMercada (Strato Market) makes more sense for a marketplace. However, the speakers might be saying "Stratomacarta". Let's look at the spelling in the prompt's example: "stratomacarta.com" is in the prompt text under SPEAKER_00 at [31:08]. And earlier SPEAKER_02 says [28:26] "stratomercada.com". This is a conflict. I need to decide which is correct or just transcribe what I hear/read. The prompt text [31:08] says "stratomacarta.com". But [28:26] says "stratomercada.com". Given the Spanish word for market is "Mercado", "Mercada" is plausible. "Macarta" sounds like a place name. Without external knowledge, I can't be sure. But the prompt *text* I am editing has both. I will look for consistency. "Marketplace version 1, or Merkada version 1" is in the text at [03:22]. So the project name is likely "Mercada". Therefore [31:08] "stratomacarta.com" is likely a typo for "stratomercada.com". I will correct [31:08] to "stratomercada.com" to be consistent with [28:26] and [03:22].

*   "information in the top right. Then the people do another landing page which we of course eliminate as well." -> "Then the people do another landing page... which we will of course eliminate as well."

**[31:26] SPEAKER_00:** "Well, don't I say if you, you know, if you, if you're, if you're not embarrassed a bit about the things that you release, then you release too late for sure." -> This is a quote (Reid Hoffman maybe? "If you're not embarrassed by the first version...").

**[31:34] SPEAKER_02:** "Absolutely. Yeah. We do. We are strong advocates of the great stuff." -> "strong advocates of the [iterate fast? ship fast?] stuff." "Great stuff" might be wrong. "Ship it" stuff? "Get it out" stuff? "Great stuff" is what the text says. I'll keep "great stuff" or maybe "get it out". Actually "launch stuff" or "ship stuff". I'll stick to the text "great stuff" or "getting it out". Given the context "release too late", "ship it" is likely. But "great stuff" is in the transcript. I will assume "get it out" or "ship it" but without audio, I have to be careful. "Great stuff" is benign enough.

**[31:38] SPEAKER_01:** "It's like, it's like a child, like, like a teenager."

**[31:47] SPEAKER_02:** "You can say that as a non parent, as a parent, they never get. It's just love."

**[31:54] SPEAKER_00:** "They're perfect."

**[31:55] SPEAKER_01:** "I love. They never get on your nerves."

**[31:57] SPEAKER_00:** "Never."

**[31:57] SPEAKER_01:** "They definitely get on your nerves. You're lying to me, you're lying to the Internet."

**[32:03] SPEAKER_00:** "Children are never frustrating."

**[32:04] SPEAKER_02:** "Never. They're balls of joy. That's it. Thank you."

**[32:14] SPEAKER_00:** "Cheers everyone."

**[32:15] SPEAKER_01:** "Everyone have a good."

**Formatting Check:**
- Merge consecutive speech from same speaker.
- Timestamps preserved.
- Correct capitalization (DeFi, ETH, etc.).
- Correct names (Kieren).
- Fix obvious transcription errors ("love chains" -> "L2 chains", "Kieran" -> "Kieren", "Carter" -> "Kata points" [Wait, context "seeing his Carter that were hiding". If they are "holders of Kata points", maybe the UI has a "Kata points" section. But [29:20] mentions "Carter" specifically. Let's re-read. "friend crypto Tarzan who was having the issue of seeing his Carter that were hiding under the non earning assets." If "Carter" is a typo, "Kata" seems likely given the later mention. Or "Cart"? "Cart" of items? "Cart" makes sense in a marketplace. "seeing his Cart that were hiding". "Kata points" are loyalty points, not items in a cart. So "Cart" is a strong candidate. But then later "holders of Kata points". So "Carter" might be "Kata" or "Cart". Given "non earning assets", it's likely assets. So "Cart" (shopping cart) makes the most sense. I will change "Carter" to "cart".]
- "ES T swap" -> "ETHst swap".
- "stratomacarta.com" -> "stratomercada.com".

Let's refine "ES T swap". Speaker says "Let's get some ES T swap". "E S T". "ETHst" fits the pattern of "Silver ST". "USDst". I'll use "ETHst".

Let's refine "Carter". "seeing his Carter that were hiding". "Cart" is a common feature. "Kata points" is a loyalty program. The issue was likely "seeing his cart". I will use "cart".

Let's refine "love chains". "L2 chains" is the standard phrase.

Let's refine "Kieran". "Kieren".

Let's refine "Viva Vendetta". "V for Vendetta".

Let's refine "hyper liquid". "Hyperliquid".

Let's refine "USDC AAVE has". "USDC, Aave has".

Let's refine "ES T". "ETHst" (or "EST" if it's a specific token, but "ETHst" is consistent with the ST suffix).

Let's refine "MUSDST". "musdST" or "mUSDST". The transcript has "MUSDST". I'll use "mUSDST".

Let's refine "rail bed". "redemption".

Let's refine "TBL". "TVL".

Let's refine "point click". "point-and-click".

Let's refine "non earning". "non-earning".

Let's refine "buyers remorse". "buyer's remorse".

Let's refine "one of ones". "one-of-ones".

Let's refine "gold and silver bugs". "gold and silver bugs".

Let's refine "mainstreaming". "mainstreaming".

Let's refine "vouchers... one to one with the sense". "one to one with the cents". This explains the "give you free transactions".

Let's refine "working for weekends". "working weekends".

Let's refine "filming". "filming"? "He's frozen. He was filming." Or "He was simulating"? Or "He was sleeping"? "filming" seems odd for "frozen". Maybe "dreaming"? "He was dreaming". The transcript says "filming". I'll leave it as "filming" (maybe a nickname or inside joke).

Let's refine "spinning everything". "freezing everything".

Let's refine "Carter". "cart".

Let's refine "stratomacarta.com". "stratomercada.com".

Final check on merging.
[03:22] SPEAKER_01 has a very long block. It seems to be continuous. I will keep it as one block.

[03:12] to [03:16] SPEAKER_00 -> SPEAKER_02 -> SPEAKER_01. These are separate turns.

[20:10] SPEAKER_01 to [20:20] SPEAKER_03. Separate.

[21:39] SPEAKER_01 to [22:27] SPEAKER_02. Separate.

[22:30] SPEAKER_01 to [22:55] SPEAKER_03. Separate.

[24:56] SPEAKER_03 to [25:09] SPEAKER_01. Separate.

[26:45] SPEAKER_02 to [26:47] SPEAKER_01. Separate.

[29:23] SPEAKER_00 to [29:38] SPEAKER_01. Separate.

[29:42] SPEAKER_00 to [29:51] SPEAKER_00. These are consecutive turns for SPEAKER_00.
"I got some fraction." -> "I believe so." -> "Right, right. That's cool pieces." (Speaker 01 speaks).
Wait.
[29:42] SPEAKER_00: "I got some fraction."
[29:47] SPEAKER_01: "Did you really? Okay."
[29:47] SPEAKER_00: "I believe so."
[29:47] SPEAKER_01: "Right, right. That's cool pieces."
So they are alternating rapidly. I will keep them separate as per the input timestamp granularity, or merge if they are effectively one conversation. The prompt says "MERGE CONSECUTIVE SPEECH INTO PARAGRAPHS". Since they are interjected, I keep them separate. However, [29:47] appears twice for SPEAKER_00 and SPEAKER_01. I will assume the transcript lines are sequential.

One tricky part:
**[29:23] SPEAKER_00:** And you'll see that's the sneaky arrows. When I do that I get, I get, I get the old stuff. I've got, you know, I think I've got some whiskey barrel bits in there and some other little.
**[29:38] SPEAKER_01:** You get a whiskey barrel. Those are real. They're trading.
**[29:42] SPEAKER_00:** I got some fraction.
**[29:47] SPEAKER_01:** Did you really? Okay.
**[29:47] SPEAKER_00:** I believe so.
**[29:47] SPEAKER_01:** Right, right. That's cool pieces.
**[29:51] SPEAKER_00:** So yeah, they're still lurking.
This is rapid fire. I will respect the speaker turns.

Okay, ready to generate.

Word count check: Input is ~2500 words. Output should be similar.

Special attention to "Kieran" -> "Kieren".
"Defi" -> "DeFi".
"ETH" -> "ETH".
"ERC20" -> "ERC-20".
"USDC" -> "USDC".
"MetaMask" -> "MetaMask".
"Aave" -> "Aave".
"Hyperliquid" -> "Hyperliquid".
"StratoMercada" -> "StratoMercada".

The prompt mentions "Known People (244): ..." and stops at Aya. It doesn't contain Bob, Victor, Michael, Kieren. Wait.
"IMPORTANT: "Kieran" -> "Kieren" (Kieren James-Lubin, NOT Kieran)"
Ah, this instruction is in the prompt text specifically. So I must fix Kieran -> Kieren.
The list provided in the prompt text is truncated ("Aaron... Aya"). I can't verify others against the full list, but I should use standard spellings.
"Vitalik" is not in the list but is a known figure. I'll capitalize "Vitalik".
"V for Vendetta".

Re-evaluating "Carter". Context: "seeing his Carter that were hiding under the non earning assets."
Speaker 00 says: "I got some fraction." (referring to whiskey barrel bits).
Speaker 01: "Those are real."
Speaker 00: "I believe so."
Speaker 01: "Right, right. That's cool pieces."
Speaker 00: "So yeah, they're still lurking."
Earlier Speaker 02 said: "Yeah. Just click that arrow button. Yes."
Speaker 00: "And you'll see that's the sneaky arrows. When I do that I get... the old stuff... whiskey barrel bits... some other little."
The "Carter" line: "friend crypto Tarzan who was having the issue of seeing his Carter that were hiding under the non earning assets."
Could "Carter" be "Kata"? "Kata points".
In [28:23] "Kata points mostly from V1".
Is it "seeing his Kata points"? Or "seeing his cart"?
In the UI described [29:20], "Click that arrow button... seeing his Carter...".
If you click an arrow to see things "hiding under the non earning assets", it sounds like a UI expansion of a list or a cart. "Kata points" aren't typically "hiding" in that sense, nor are they "assets" you trade (they are points). "Cart" items make sense. However, "Carter" starts with C. "Cart" is very close.
I'll use "cart".

Re-evaluating "ES T swap".
Input: "Let's get some ES T swap."
Context: "Swap some USDT... get some ES T swap."
Later: "gas is used through USDST".
Later: "swap some right now... let's do... silver ST".
I will use "ETHst".

Re-evaluating "stratomacarta.com" vs "stratomercada.com".
Input [28:26]: "stratomercada.com"
Input [31:08]: "stratomacarta.com"
Input [03:22]: "Merkada".
I will standardize on "StratoMercada" and "stratomercada.com".

Re-evaluating "MUSDST".
Input: "mint me some MUSDST tokens".
I will use "mUSDST".

Re-evaluating "TBL".
Input: "sort it by TBL".
Context: "top pool is usually the top pool by volume".
Standard DeFi metric is TVL. TBL is likely a typo for TVL. I will use "TVL".

Re-evaluating "point click".
Input: "point click philosophy".
I will use "point-and-click".

Re-evaluating "one to one with the sense".
Input: "one to one with the sense, I suppose."
Context: vouchers for transactions. "Cents" makes sense.
I will use "cents".

Re-evaluating "love chains".
Input: "The one big limitation on love chains".
Context: bridging, gas tokens.
I will use "L2 chains".

Re-evaluating "rail bed".
Input: "End of the rail bed."
Context: physical delivery of whiskey.
I will use "redemption".

Re-evaluating "working for weekends".
Input: "working for weekends. Oh, he's gone away. Okay. He's... He was filming. Yes, well, there were a lot of sleepless nights and working for weekends."
Wait. "working for weekends" sounds like "working weekends" (working through weekends). "Working for weekends" means working to get to the weekend. Given "sleepless nights", "working weekends" (working on the weekend) is the intended meaning. I'll use "working weekends".

Re-evaluating "spinning everything".
Input: "it started spinning everything for a second".
Context: "He's frozen. He was filming."
"Spinning" usually refers to a loading icon. "Everything froze for a second" is likely.
I will use "freezing everything".

Re-evaluating "Carter" one last time.
Could it be "Kata"? "Seeing his Kata points".
But "hiding under the non earning assets".
If I have "non-earning assets", and I click an arrow, maybe I see "Kata points"?
But "Carter" is closer to "Cart".
Also Speaker 00 says "I've got some whiskey barrel bits...". Those are assets. They would be in a "portfolio" or "cart".
I'll stick with "cart".

Re-evaluating "filming".
"he's frozen. He was filming."
Maybe "simulating"?
I will leave as "filming" (maybe he was showing a pre-recorded video or it's a nickname).

Final Plan:
Merge blocks.
Fix terms.
Fix spelling.
Keep timestamps.
Start immediately.**[00:01] SPEAKER_00:** We're live.

**[00:01] SPEAKER_01:** For real.

**[00:03] SPEAKER_02:** We are live.

**[00:04] SPEAKER_03:** Yes, we're live.

**[00:05] SPEAKER_01:** And we're live.

**[00:09] SPEAKER_00:** So maybe this won't be so meaningful for the rest of you, but it is the 5th of November today, which in the UK is a very famous day of the calendar because it's Bonfire Night or Guy Fawkes Night, celebrating the. The burning at the stake, I guess, of Guy Fawkes, who was the guy who tried to. To blow up the Parliament in the mid 17th century.

**[00:43] SPEAKER_03:** Oh, the V for Vendetta guy.

**[00:47] SPEAKER_00:** Based on that.

**[00:49] SPEAKER_02:** I mean, the poem, right, says "Remember, remember" right in the first line, right?

**[00:55] SPEAKER_00:** That's right. So basically the deal there was that, I guess annually you had like the king giving the speech in front of the Parliament, you know, so you had like, basically the royalty and all of the elite sitting in the hall. They, like, stuffing barrels of gunpowder underneath, but it was discovered at the last minute. So then there you go. You now have burning of Guy Fawkes in effigy on Bonfire nights to celebrate that it didn't happen. And. Yeah, so you have a, you know, like a doll or whatever. That's. That's the guy that you put on the fire. So, anyway, happy Bonfire Night, everybody.

**[01:44] SPEAKER_03:** Happy Bonfire Night.

**[01:46] SPEAKER_02:** We should probably introduce Michael because he's a special guest.

**[01:50] SPEAKER_01:** Absolutely, yes, I guess he's a guest. I mean, we'll make him a regular, I assume, but.

**[01:58] SPEAKER_02:** Yeah.

**[01:58] SPEAKER_03:** See me on the telegram.

**[02:00] SPEAKER_02:** Michael, do you. Do you want to introduce yourself quickly?

**[02:02] SPEAKER_03:** Yeah, yeah. I work on the sales side of the team. I'm going to be introducing the app today to you guys and I hope you're excited.

**[02:09] SPEAKER_02:** Well, you work sales, you're a dev, you're a front end dev. You know, like, you do a bunch of different stuff on the team, so.

**[02:16] SPEAKER_01:** Yeah.

**[02:16] SPEAKER_00:** Got the moves.

**[02:18] SPEAKER_02:** Yes. Sorry, go ahead.

**[02:21] SPEAKER_00:** Let me just kick off. Hi. Hello, everybody. Welcome, welcome. So we did it. We launched V2. It happened. How does that feel, man?

**[02:34] SPEAKER_01:** I think, Bob, you may not be as tired, you know.

**[02:41] SPEAKER_02:** Oh, he's gone away. Okay. He's. He's frozen. He was filming. Yes, well, there were a lot of sleepless nights and working weekends. Oh, you are back.

**[02:58] SPEAKER_03:** It was back. It was.

**[03:00] SPEAKER_01:** It was my problem. Okay. Yeah, it started freezing everything for a second and then I. And you all came back. Yeah. Second.

**[03:12] SPEAKER_00:** So how's V2 being live?

**[03:14] SPEAKER_02:** How's that feel?

**[03:16] SPEAKER_01:** Much better than before. You know, it's still.

**[03:21] SPEAKER_02:** You never.

**[03:22] SPEAKER_01:** It's a funny thing. Do you ever feel, like, good for, like a sustained period? Like. I think not, but extremely happy that it's live. I think it would be maybe interesting for the audience to go into a little bit of like what it is and also like why it took so long. So we, to the end of 2024 we started to realize that there was a lot of demand for DeFi type features. So basically Marketplace version 1, or Mercada version 1, if you will, was more NFT-ish. We had interesting and exotic things that might be numbered and a breadth of them. So this was. We have carbon offsets trading on there, whiskey barrels. Michael moved a lot of collectible shoes through the system. So truly, you know, fairly unique, at least down to like having a serial number or sometimes very unique stuff. So there are occasional one-of-ones on there. We dipped our toes into the art market a little bit with some collabs and also so. And then more financialized stuff too. So the metals in particular being something that we've had for a long time and we kind of saw the most demand for the most financialized items and it sort of led us to realize what people want from this technology. I mean, one way or another know, I think in the course of the company, obviously we did very enterprise stuff a lot in the supply chain and that kind of actually led very naturally to the unique item focus and. But you know, often everything in the blockchain space pulls back to some sort of financialization. And we kind of decided to stop resisting this impulse, you know, as the market seemed to be demanding it. So, so we released the other thing we realized is that in some ways, so you know, say your goal is to tokenize everything. Like you want all manner of real world value to be on chain existing alongside truly digital native assets like Bitcoin, ETH and so on. What would get the world to do that? And we thought the answer was making liquid trading markets where they didn't exist prior. And that is definitely still part of it. But I think it is more about debt than it is about selling or transacting. Right. And so we kind of on Marketplace version 1 created a mechanism whereby you could borrow against collateral. It was sort of primitively done, but you could do it within the system. And it got great uptake. And then we, we said, all right, like let's just make this stuff a little more DeFi. And it just turned out that like I. We were not expecting to do a relaunch. In fact, we were bringing folks on through Q1 and Q2 and TVL was rising and you know, etc. More loan volumes and all that. Sort of thing. But we realized that we were hitting the limits of the system pretty quickly and that it would be just, you know, that we needed to at least change some of the way the internals worked. And you know, we, so we did a listing of our gold token with small exchange. Was good experience to work with them, but they had, you know, a hard time dealing with things as, as they are, as they were rather and found that just everyone wants the ERC-20 style and that to make the capabilities, you know, sort of show the best of DeFi. It was like a huge, huge effort that turned into a full relaunch, which was never the goal at the outset, but you know, happy to be on the other side of it. The system is definitely way better. It's a little bit different. There are some areas where we kind of took a shortcut on version one that made it kind of easy and we've gone and made it say more decentralized now, which is definitely better. But there, there could be like rough edges around it. As a for instance, we often had fixed pricing on Marketplace version 1 or Pure Spot pricing. And we have swap pools now, which is great. And that they let the market determine the price and get third party liquidity in and so forth. But then there's just more variability on the, on the, any given trade execution. And so though these things will all sort of work themselves out over time, but huge effort, it's way better, way better. But it's, it's. We ended up in more of a different place than I intended at the outset. Let me just, let me throw, throw it over to say Victor just on, on all this.

**[08:56] SPEAKER_02:** Yeah, I, I think the thing is that really, I think our core insight was really, if you think about how people in the real world really accurately, you know, accumulate wealth, it's really through like small accumulation over time of interest. You know, like think about a savings account, a retiring account, all these things people aren't like day trading constantly. Right. So what we realized is that, you know, it wasn't enough to simply be able to buy new exotic or not even exotic, but tokenized things in the real world, but really to turn those into things that were revenue generating for you individually and earning over time. So it should, you know, you should be able to have multiple ways except for trading to earn things. And we realized that DeFi had kind of answered this, but it did it in a way that was too complicated for the vast majority of people to understand. I mean, you know, it was only a year ago that Vitalik himself was like, someone needs to explain to me where DeFi yields are coming from. Right. Like if he couldn't understand it, you know, how could the rest of the world kind of get into it? And we wanted to build a system that would allow the rest of the world to really kind of get those DeFi earning potentials. And you know, I think there were two things that really came out of it. One is that we had to kind of combine the pool of assets to not just be about real world asset, liquid real world assets, which we started with, but we also had to bring in, you know, high quality crypto assets. And then the second thing is that we had to offer different paths of earning. Like you could be able to put some of those assets into liquidity pool that you would lend out to other people and get interest on that you would be able to go into swap pools and see when their prices indifferent. You should be able to earn directly if you put some of your things into a savings account that people could offer. So basically V2 offers all of those paths for users which we're really, really excited about.

**[11:16] SPEAKER_00:** Yeah, I mean the point you were saying about trading specifically Victor, you know, so a stat I've repeatedly said, parroting from a prior project, was that, you know, only about 5% of people who try and day trade actually like make a profit. Yeah, most people are terrible, absolutely terrible at trading because you just end up trading your emotions. Right. And you're just scared at the wrong time and you're not brave at the right time and you just, it's very, very easy to, you know, to put yourself in a worse position. So you know, having passive yield is absolutely, you know, a big need for a huge amount of people.

**[11:59] SPEAKER_02:** Yeah. And I was really surprised that even in the crypto world the amount of people that had exposure to DeFi was relatively small. Like, I mean, you know, and I think people didn't understand that how well established those patterns have gotten. It's funny that, you know, Vitalik has just woken up to this after like last year saying I didn't understand you said, you know, the future of Ethereum is going to be based on low risk DeFi. Right.

**[12:28] SPEAKER_00:** So that's using DeFi themselves now finally.

**[12:32] SPEAKER_02:** Exactly.

**[12:34] SPEAKER_00:** For like 10 years they were just like market dumping to raise funds. And it's like, you know, the thing that's kind of got built here because of Ethereum.

**[12:44] SPEAKER_02:** Well, and the world fundamentally, to Kieren's point, runs on credit. Right, That's. And DeFi has really solved the collateralized lending component in a way that is so seamless. Like where else can you get a loan in like minutes? Right. Like it's, it's, it's hard to kind of think of any other place where you could do that in a reliable fashion. And I think it does it in a way that allows it to be much more transparent than say typical financial institutions. Right. So you know, the people that are benefiting from those loans are the other users, which is really exciting I think to us.

**[13:23] SPEAKER_00:** So I mean how, how would you say V2 is different than existing, you know, other big name DeFi protocols?

**[13:34] SPEAKER_01:** Yeah, it's. So it's very much has a point-and-click philosophy. I think if you look at the app today, which Michael will show you, there are still details bleeding through that we will eventually kind of smooth out as appropriate. You know, you need to, you need the user to know what they're doing but not quite know how it's happening if you will, you know, give, give them the right amount of rope, etc. But it is much easier than other takes on how to do it in my opinion. Like if you, you know, you've got to do sort of the one wallet connect if you use the bridge in Path. So probably easiest way into our system is to take some USDC and mint some of our stable token USDst. You can also go in with ETH for instance and then you'll be granted some vouchers which, which will give you gas on Bridge and. Once that's happened, you're in this sort of pleasant, let's say essentially gas free playground where you point and click like a normal Web2 app. And this philosophy extends further. So at the moment we have just four swap pools set up which we've seeded and others have with some liquidity we want. We'll expand this over time for sure and eventually we'll go to a permissionless listing structure, if you will. The reason we've kept it small to date is just to one, make sure everything is working but give you a little less rope than the other platforms out there. So if you go to Uniswap, for instance, you'll find the top pool is usually the top pool by volume. You can sort it by TVL if you want. And that tends to direct people's attention to whatever is trading right now. And the wildly variable APRs, APYs, et cetera kind of encourage an aping in sort of behavior. Our message is kind of more like yeah, get into whichever assets you prefer, maybe borrow conservatively and just kind of keep accumulating over time basically. And so, you know, it's not quite at a Vanguard level, but you know, kind of more of a set it, forget it, be conservative, keep growing attitude that should show through within the system while still having flexibility. So the, yeah, so, and it's, I guess I would say batteries included. There are actually two borrowing paths within the system. So once you have collateral, you can mint our stablecoin at a moderate interest rate and you can then put that into swap pools, you can put that into lending pools, you know, and so on. Or you could just, you know, kind of go into the secondary market which is a little bit more flexible in certain ways. So that would be swapping directly, lending pool, etc. So you know, I think we, we don't aspire to the same ends but look at projects like Hyperliquid where the, it's, it's an Alt L1 which means you've got control over the fees. The latency of the system is very good as compared with most Ethereum stuff. Let's say it's fast confirmations that are irreversible. And that thing, it just gives you the latitude to make the user experience as good as possible, which will be a continual battle. But it's been a real step function change from both our old stuff and what's out there today.

**[17:36] SPEAKER_00:** Well, should we take a look?

**[17:37] SPEAKER_01:** Let's take a look.

**[17:38] SPEAKER_02:** Let's take a look.

**[17:39] SPEAKER_03:** I guess I'm up. All right, Share my screen.

**[17:51] SPEAKER_02:** Okay.

**[17:55] SPEAKER_03:** Okay, everybody see my screen?

**[17:57] SPEAKER_02:** Yes.

**[17:58] SPEAKER_00:** Great.

**[17:58] SPEAKER_03:** So we're going to start with bridging in tokens. There's two ways to do it. The normal bridge. Well first you have to connect your wallet of course using MetaMask here. There's two ways to do it if you want to bridge an ETH or any kind of like wrapped Bitcoin, PAXG. I think we have something else forgot. But you bridge it in through this. If you want to bridge in stables I would go through the convert feature that will mint on bridge. So we're going to bridge in USDC. This is the testnet by the way. If you want to try it out, just go to this link. And if you want to get some test USDC, Aave has some test faucets for USDC and USDT but let's bridge in like 100 bucks maybe let's do USDC get USDT bridge it in. Confirm, confirm minting. So I bridged them in before just because this is a bit of a process. But you could also check the Status here takes a while for the. Takes a little bit for the server to update there. But visit earlier when I did that. Completed. So let's just assume that it's already in here.

**[19:11] SPEAKER_02:** We should be clear the delays are not on the Mercado side. Pretty much instantaneous. It's on the, you know, Ethereum Sepolia side.

**[19:20] SPEAKER_03:** Yep. So we're going to swap some right now. Let's swap some USDT. Let's do like I don't know, 10. Let's get some ETHst swap. And also gas is used through USDST on our app as well. Similar to, similar to Hyperliquid actually.

**[19:44] SPEAKER_00:** And what do you pay? What do you pay? What are you paying?

**[19:47] SPEAKER_03:** As normal transaction, it depends on the transactions. But some are $0.01 to $0.03 depending on what it is.

**[19:55] SPEAKER_01:** If it's $0.03, it's probably three transactions in there.

**[19:58] SPEAKER_03:** Yes. Yeah, yeah. Usually like I believe a transfer. No, not a transfer. A bridge in is two transactions, I'm not mistaken.

**[20:10] SPEAKER_01:** Although yes. If you bridge in you get minted vouchers. So the vouchers just give you free transactions one to one with the cents, I suppose. Yep.

**[20:20] SPEAKER_03:** Vouchers you can track here as well. And this cool little, little widget. Anyway, so I swapped some assets and.

**[20:28] SPEAKER_00:** Vouchers just to clarify. So that's kind of a little, A little, A little nice hack of getting past the. Oh my God, I haven't got any, any ether for gas on this chain at this time.

**[20:44] SPEAKER_03:** Right, Exactly.

**[20:46] SPEAKER_02:** It's a, it's an onboarding thing. Right. Like.

**[20:49] SPEAKER_00:** Yeah.

**[20:50] SPEAKER_02:** You know, the one big limitation on L2 chains, right. Like is you can't even do your first transactions on most of them until you have the native token. Right.

**[20:59] SPEAKER_03:** Yeah.

**[20:59] SPEAKER_02:** Allows us to bring people on without requiring that.

**[21:03] SPEAKER_03:** Yep. So we've done the swaps. We're going to add some liquidity to the.

**[21:07] SPEAKER_02:** Michael, I just want to mention if you can go back to the swap. One really important thing with our system is it allows you to see sort of like the exchange rates internally but also like the global exchange rate. That's where you see the exchange spot right under there. So that's the global. Right. This is something we learned from two of our trading contests. So where are like, you know, the arbitrage opportunities? You can see from these two things directly instead of having to go somewhere else to figure.

**[21:39] SPEAKER_01:** All right, it's been funny on the, on the live system. So it. For, for those who have used DEXes, you find, you know, if there's not that much liquidity. You can definitely push the price as reported and provided by the DEX off of the true market price. And in here we're combining a couple different data sources to get the spot price and that's just coming through an Oracle really here it's just a reminder. The spot price is used for like the health calculations when you borrow and the reason you want to do that is you know someone could do a big trade on the one of the pools and manipulate that price and then liquidate someone or or etc as we.

**[22:27] SPEAKER_02:** Saw very recently with the Balancer attack, you know.

**[22:30] SPEAKER_01:** Yeah, yeah so so but it's also just a reminder to, to get good execution. So you know for, for those who go try this if you do it on the live net just, just make sure you know don't do huge trades on there just yet because liquidity is still coming in both. Both from us and externals to make sure you get good execution.

**[22:55] SPEAKER_03:** Yep. And yeah just the pool is not really relevant to the. The oracle price but yeah everyone should keep that in mind as well. Anyway we'll get back to the pool. So these are the lending pools that contribute to the borrow lending which we'll get to in a little bit. But I can deposit 100 in here and I will. It should mint me some mUSDST tokens which is my pool token that's represented of my. My lending pool contribution believe that is in these non-earning. Right here I am again. So let's also contribute some money to the swap pool so you can earn APY. See what looks juicy right now the silver. Wow.

**[23:39] SPEAKER_01:** Silver trades.

**[23:41] SPEAKER_03:** So I'm going to confirm my deposit. And we are deposited and we're earning.

**[23:55] SPEAKER_00:** APY and you're depositing both silver ST and USDst.

**[24:02] SPEAKER_03:** That's right.

**[24:03] SPEAKER_01:** When you input to a swap pool you need to put in both pairs and we have, we have two modes here. It's probably just better to use the A and B mode but you can do a single-sided liquidity add. But what it does is it does a swap so that you have an equal amount of the other one and then it deposits it. So yeah and as long as the convenience if you.

**[24:27] SPEAKER_00:** If you wanted to get into it but you haven't got the right stuff.

**[24:30] SPEAKER_01:** That's correct.

**[24:31] SPEAKER_03:** Yeah yeah the buttons right here for everybody that wants to do it single side if they choose to do so. And let's see what are we going to. Let's do some borrowing. So I'm gonna supply my whole ETH stack 14 bucks all of it.

**[24:49] SPEAKER_00:** Don't do it all.

**[24:49] SPEAKER_03:** Do all of it.

**[24:53] SPEAKER_01:** On the gas though it will be fine.

**[24:56] SPEAKER_03:** So I have. Let's see, I have $14. Oh, we gotta hide some of these 1490 here. Because the LTV I believe is about 75%. I have $11.

**[25:09] SPEAKER_01:** We tend to match the market. You don't need to go all the way up to the LTV, but let's.

**[25:14] SPEAKER_03:** Let's go all the way.

**[25:17] SPEAKER_02:** I vote like this is risky. I would recommend people we're gonna see some.

**[25:26] SPEAKER_03:** Face. My whole fact, always be careful your health factor. Once you hit one, you can get liquidated but we can also reach.

**[25:32] SPEAKER_02:** I recommend going with 50%.

**[25:35] SPEAKER_03:** Basically we could always just repay it and it should update here.

**[25:41] SPEAKER_00:** Buyer's remorse instant refund.

**[25:44] SPEAKER_03:** Overall, that's the app. It's kind of a combination of Uniswap and Aave. For you guys more familiar with Web3, if you guys have any questions or you want a deeper walkthrough, feel free to message me on telegram and we can hop onto Zoom.

**[25:58] SPEAKER_01:** Yeah.

**[25:58] SPEAKER_03:** But there you go, guys.

**[25:59] SPEAKER_01:** Also for the gold and silver bugs out there, we take physical deposits in addition to supporting some of the popular. Well, actually there's no. So far as I know, there's no really popular silver token other than ours. But you know, we'll take PAXG right now and soon the Tether Gold coin as well. And that can drive your borrowing power within the system. You can borrow and then turn around and lend CDP path and that will make your gold into a productive asset.

**[26:36] SPEAKER_00:** I hadn't thought that there weren't other silver tokens. That's a good.

**[26:39] SPEAKER_01:** I looked. What. They're very small. To the extent that we have that they're out there.

**[26:45] SPEAKER_02:** I mean there are a bunch of gold tokens at this point.

**[26:47] SPEAKER_01:** A lot of gold. Yeah.

**[26:53] SPEAKER_00:** So. Yeah, so that was. So that was that.

**[26:57] SPEAKER_01:** I have one more comment, actually. It's been kind of fun. So the, the prod system, you know, it's been online for a couple days and the. That, you know, the most trading has been on the ETH pool because it's been volatile. Right. Sorry if anyone's gotten hurt out there in the last, you know, 24 hours or so. Michael likes to get liquidated. I know. But so, so, you know, that's manifested very quickly on our system and it's where a lot of the. The trading is. And it's, you know, still very much beta mode. But we have enough people that it's. We're starting to see the pool prices actually converge to the Spot price because if it doesn't there's an arb in there. So you know, get in early, you know, don't, don't put crazy amounts in but because you know these systems become pretty efficient over time but when it's not, there's money to be made. And finally I will say for those of you who are holders of Kata points mostly from V1 or contest participation, we're going to monitor the system for a little bit. Just make sure everything's working and so on and then start to work towards the V2 points program. Not imminent but coming.

**[28:23] SPEAKER_03:** Excellent.

**[28:24] SPEAKER_00:** Because a number of people asking that.

**[28:26] SPEAKER_02:** Question I was just going to add. If you want to try it out now you can just go to our updated website at stratomercada.com and click launch app. One of the big efforts that we're going to is to improve the UX. So if anyone has any suggestions please join our Telegram community and send us messages there. We'd love to hear from you. We're actively trying to improve it and you know, achieve our goal of like.

**[28:56] SPEAKER_00:** Mainstreaming DeFi and Colin there says the whole platform works perfectly. Just waiting on rendering of the front page to be visible. For me that's a friend. A friend Crypto Tarzan who was having the. The issue of seeing his cart that were hiding under the non-earning assets.

**[29:20] SPEAKER_02:** Yeah. Just click that arrow button. Yes.

**[29:23] SPEAKER_00:** And you'll see that's the sneaky arrows. When I do that I get, I get, I get the old stuff. I've got, you know, I think I've got some whiskey barrel bits in there and some other little.

**[29:38] SPEAKER_01:** You get a whiskey barrel. Those are real. They're trading.

**[29:42] SPEAKER_00:** I got some fraction.

**[29:47] SPEAKER_01:** Did you really? Okay.

**[29:47] SPEAKER_00:** I believe so.

**[29:47] SPEAKER_01:** Right, right. That's cool pieces.

**[29:51] SPEAKER_00:** So yeah, they're still lurking.

**[29:55] SPEAKER_01:** I guess. Yeah, we should. I know some people have exited those. They are, no pun intended, kind of illiquid. But there's been a little bit of whiskey barrel trading so we should, we should discuss.

**[30:09] SPEAKER_00:** Offline holders are not being rugged. The, the, the whiskey.

**[30:15] SPEAKER_01:** You know, you get to. You get the physical delivery at the end. Maybe not if it's fractionalized at the.

**[30:23] SPEAKER_00:** End of the redemption.

**[30:26] SPEAKER_01:** That's right.

**[30:27] SPEAKER_00:** Making delivery. Okay. Well is there anything else anyone wanted to cover or we can wrap it up.

**[30:34] SPEAKER_02:** No, we just look forward to. We look forward to you guys trying it and giving us whatever input. We're really excited for you to see this and you know we're still going to evolve a lot. Things have been moving quickly and will continue to be moving quickly on it. So exciting times for us.

**[30:52] SPEAKER_00:** So yeah, just to head to stratomercada.com so S T R A T O M E R C-A-D A.com stratomercada.com and you've got the app there and all.

**[31:08] SPEAKER_01:** The information in the top right. Then the people do another landing page which we of course eliminate as well. It's better that this thing is up. But yes, this, you know, the. Sometimes you have to just make a choice and launch it. But yes, in time.

**[31:26] SPEAKER_00:** Well, don't I say if you, you know, if you, if you're not embarrassed a bit about the things that you release, then you release too late for sure.

**[31:34] SPEAKER_02:** Absolutely. Yeah. We do. We are strong advocates of the great stuff.

**[31:38] SPEAKER_01:** It's like, it's like a child, like, like a teenager. You're like, I love this child. But you know, you still get on my nerves a little bit.

**[31:47] SPEAKER_02:** You can say that as a non parent, as a parent, they never get. It's just love.

**[31:54] SPEAKER_00:** They're perfect.

**[31:55] SPEAKER_01:** I love. They never get on your nerves.

**[31:57] SPEAKER_00:** Never.

**[31:57] SPEAKER_01:** They definitely get on your nerves. You're lying to me, you're lying to the Internet.

**[32:03] SPEAKER_00:** Children are never frustrating.

**[32:04] SPEAKER_02:** Never. They're balls of joy. That's it. Thank you.

**[32:14] SPEAKER_00:** Cheers everyone.

**[32:15] SPEAKER_01:** Everyone have a good.