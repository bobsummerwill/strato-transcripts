1.  **Analyze the Request:**
    *   **Role:** Expert transcript editor specializing in Ethereum and blockchain.
    *   **Input:** A raw transcript from a simulcast (YouTube Live and Twitter Spaces) featuring Bob Summerwill (SPEAKER_00 - inferred based on self-introduction in text "I'm Bob Summerwill") and likely Victor Trón or someone else (SPEAKER_01) discussing a contest related to "Strata Mercado" and "MK2" (Mercado V2).
    *   **Context:** A list of known people (Ethereum ecosystem) and technical terms is provided to check spellings.
    *   **Objective:** Create a clean, readable transcript preserving *all* dialogue.
    *   **Constraints:**
        *   No preamble/meta-commentary.
        *   Start immediately with the first speaker label.
        *   Output length must be ~90-110% of input length.
        *   Timestamps: Keep exact if present (Input has them). One per speaker turn.
        *   Format: `**[MM:SS] SPEAKER_XX:** Text...` with paragraph breaks for natural flow.
        *   Fixes: Technical terms, proper names (from context list), grammar, punctuation.
        *   Remove: Excessive filler words, false starts, obvious repetitions.
        *   Preserve: Substantive content, flow, context.

2.  **Analyze the Source Text:**
    *   **Speakers:**
        *   SPEAKER_01 (Host? Victor?): Asks for confirmation on audio, introduces Bob.
        *   SPEAKER_00 (Bob Summerwill): Introduces himself ("Bob Summerwill"), mentions "Strata Block Apps", "MK2" (Mercado V2). Discusses the contest, prizes (USDC, Catapult points), mechanics (bridging, collateral, trading, liquidations), and specific assets (MF, SepoliaETH, USDC, MUSDC, USDST, WBTCST, ETHST, GOLDST, SILVST).
    *   **Entities to verify/correct:**
        *   "Strata Block Apps" -> Context says "Strata Block apps" but actually refers to "Strata Block apps" or just the ecosystem around "Mercado". Let's look at the text: "Strata Block apps". Bob Summerwill is Executive Director at "Ethereum Classic Cooperative" historically, but here he says "Head of Ecosystem at Strata Block Apps". I will respect the transcript text unless the context list says otherwise. The list doesn't have "Strata Block Apps". It has "Strata" maybe? No. But "Bob Summerwill" is in the list.
        *   "McCarter v2" -> Phonetically matches "Mercado V2". The speaker says "McCarter v2". Later in the text, "Mercada F" and "Mercado" appear. I should probably correct "McCarter" to "Mercado" based on "Mercada F" later in the text and general knowledge of the project (Strata Mercado). The text says "Mercado F" later. Let's look at the text flow. "McCarter v2... Mercada F... Mercado". Yes, "McCarter" is a transcription error for "Mercado".
        *   "Sheba Tarzan" -> "Sheba Tarzan" sounds like "Shiba Tankan" or something similar? No, looking at the text later: "Cata points" and "Catapult points". Ah, "Cata" likely refers to "Catapult". "Sheba Tarzan" might be "Cata Tankan"? Or a specific person. Wait, the text says "point out with Sheba prize winning Sheba Tarzan in contest number one". Maybe "SHEba" -> "Cata"? "Sheba Tarzan" -> "Cata Tankan"? Let's re-read carefully. "Sheba prize winning Sheba Tarzan". Later it mentions "Catapult points". It's likely "Catapult". But "Sheba Tarzan"? Maybe "Shiba Tankan"? Or maybe "Cata Tankan"? Actually, looking at the context of "Catapult points", "Sheba" is almost certainly a transcription error for "Cata". "Tarzan" is likely "Tankan" (a pseudonym). Or maybe "Catalan"? I will stick to what is intelligible or generic if uncertain, but "Catapult" is the clear token name. Let's look at the text again: "point out with Sheba prize winning Sheba Tarzan... Catapult points". I will change "Sheba Tarzan" to "Catapult Tankan" if I'm confident, but since "Catapult" is mentioned later, I'll assume "Catapult" is the ecosystem.
        *   "Texture" -> A person interviewed previously.
        *   "StreamYard" -> Software name.
        *   "Sepolia F" -> "Sepolia ETH"? "MF network"? The text says "Sepolia F" and "MF for Mercada F". "Mercada F" -> "Mercada Finance"? Or just "Mercada". The asset is "MF". It seems they are on a testnet or a specific chain.
        *   "FST" -> Token name.
        *   "MUSDC" -> Mock USDC.
        *   "USDST" -> USDC Stable Token? Or similar.
        *   "WBTCST", "ETHST", "GOLDST", "SILVST" -> Wrapped BTC, ETH, Gold, Silver (ST likely stands for Strata/Mercado Token).
        *   "Jeremy or Michael" -> People in the chat.

3.  **Step-by-Step Editing:**

    *   **[00:18] SPEAKER_01:** "Okay, can anyone confirm that they can see us on YouTube? Thank you, Michael. Can everyone confirm that they can see us on YouTube and spaces? Michael, can you confirm you can hear us on YouTube?" -> Keep.
    *   **[01:28] SPEAKER_00:** "You broke up for me quite a lot there, Victor, when you were speaking." -> Keep. (Adds name "Victor").
    *   **[01:33] SPEAKER_01:** "Okay. OK. So Jamie, can you post this on our Twitter, the YouTube, and we'll get started shortly. Hey, MK, welcome. Glad you could join us. We're just gonna wait a few more minutes and get everyone in. So Okay, we're just waiting a few more minutes for people to kind of start coming in. Thank you everyone for joining us. And we are super excited to announce this contest. So" -> Clean filler: "kind of", "So Okay" -> "So,".
    *   **[05:43] SPEAKER_00:** "Welcome, Yves. Stefan. Do you want to give it maybe until 10 past, Victor, three minutes?" -> Keep.
    *   **[06:21] SPEAKER_01:** "Sure." -> Keep.
    *   **[06:24] SPEAKER_00:** "Nice round number. So on one of our spaces not too long ago where we were interviewing Texture, he berated us for talking about the weather when he joined. Do you remember that? We were talking about the turns of the season and when fall was starting and so on." -> Keep.
    *   **[07:02] SPEAKER_01:** "I do not remember that." -> Keep.
    *   **[07:04] SPEAKER_00:** "And he said we were old for talking about the weather." -> Keep.
    *   **[07:09] SPEAKER_01:** "Well, we are old, but you know, like I guess in the, I guess." -> Clean up: "Well, we are old, but I guess..."
    *   **[07:17] SPEAKER_00:** "We're experienced. We're not old." -> Keep.
    *   **[07:25] SPEAKER_01:** "Should, should we troll them by talking about the weather now or, or not?" -> Remove stutter: "Should we troll them..."
    *   **[07:33] SPEAKER_00:** "Welcome." -> Keep.
    *   **[07:43] SPEAKER_01:** "So just for everyone's information, and since we're not going to talk about the weather, this is our first simulcast. It's happening on YouTube Live and Twitter Spaces. There was some behind-the-scenes wiring up of all this. And if anyone has poor audio or anything, please let us know, and we'll try to rectify it next time." -> Keep.
    *   **[08:07] SPEAKER_00:** "So yeah, we're using StreamYard, which seems to be sort of the best answer there is. not great either. Also, X do not make it easy to escape their walled garden. They really want you to do everything on spaces. There isn't even functionality for downloading the audio afterwards natively. They do not want you to escape. However, we found lots of dodgy browser extensions that allow you to do that. that and command line tools. Just point out with Sheba prize winning Sheba Tarzan in contest number one and back for more in this second contest." -> Fix "X do not" to "X does not". The end of this paragraph "Just point out with Sheba..." seems disconnected or a sentence fragment. I will try to smooth it but keep the meaning. "Just point out with [Sheba] prize winning [Sheba] Tarzan..." is confusing. Later text mentions "Cata points". It's likely "Catapult". "Sheba" -> "Cata". "Tarzan" -> "Tankan" (likely a username). I will use "Catapult" and "Tankan" if it fits, otherwise keep close to text if unsure. Let's look at "Sheba Tarzan". Maybe "Cata Tankan"? "Sheba" is very similar to "Cata" phonetically in some accents or if muffled. "Tarzan" is likely "Tankan". I will change to "Cata Tankan" and "Catapult". The text says "Sheba prize winning Sheba Tarzan". I'll correct to "Catapult prize-winning Cata Tankan" or similar if the context allows, but "Sheba" is repeated. Given the "Catapult points" later, I'm 95% sure it's "Catapult". I'll use "Catapult" for "Sheba". "Tarzan" -> "Tankan".
    *   **[09:00] SPEAKER_01:** "Yes. And Justin, welcome." -> Keep.
    *   **[09:08] SPEAKER_00:** "Okay. So yeah, maybe we start. So yeah. okay hi everyone um good to have you here i'm i'm bob simwell i'm the head of ecosystem at uh at um at strata block apps uh victor who's with us here is the uh chief product officer and co-founder um mccarter v2 um is the new iteration uh of our application of our network um which is has been a major focus for us this year you know we spent the vast majority of this year rebuilding a completely new um application experience um the current production mainnet is more of a sort of ebay-ish kind of uh setup um really coming out of an earlier period where we were having a marketplace of kind of like collectibles, tokenized whiskey barrels, and other things which were more NFT-like. The focus for V2 is really about high-quality, hard assets, specifically gold and silver." -> Major cleanup needed here.
        *   Remove fillers: "um", "uh", "you know".
        *   Fix names: "Bob Simwell" -> "Bob Summerwill" (from list).
        *   Fix project name: "Mccarter v2" -> "Mercado V2" (Contextual).
        *   "Ebay-ish" -> "eBay-ish".
        *   "NFT-like" -> "NFT-like".
    *   **[10:33] SPEAKER_01:** "Hey, Bob. We're getting some feedback that your audio is coming in choppy for some reason, but... mine seems to be okay. So why don't I take it over from what you said? So as Bob was saying, V2 is really an iteration of what we were doing before. We were kind of offering a lot of different RWAs before, and V2 is our way to kind of really focus on the ability to bring real-world assets and lend and borrow on those assets. So one of the things that we're going to be testing in this iteration of the contest is really how it interacts with the external world, including things like bridging out and bridging in these different assets. And it's really interesting because One of the things I think that stands out in our positioning in terms of the RWA space is most RWA projects seem to really be trying to focus on getting degensed by RWAs. We're focused on people who already have RWAs, things like gold, silver, US dollars, and bring that into the crypto ecosystem and the DeFi ecosystem. That's really what we want to test in terms of this overall contest. What you're seeing on your screen right now is a overview of the new V2 application. It's been basically the focus of our efforts throughout this year. And what There have been significant changes to it, which I'll show in one second, from the earlier duration of our contest in July. So thank you for everyone that provided feedback. And that was immensely useful. We took as much of that feedback as we could to bring you this new version of the contest. Now, in this version of the contest, There are still going to be three prizes since they were before, but they're for slightly different things. So we will have a prize for the best trading award. So whoever has the total net balance of total number of assets and based on all of their activities. So that will be a prize and we've doubled the prizes. So that would be 500 USDC plus Cata points. And then we will have, instead of like just offering the bug prices, we have a recommended improvement price. So for technical people who are not that into trading please provide us your recommendations on improvements. That price is also a 500 USDC plus color points. And then we have an export price. So if anyone finds an exploit that could possibly steal funds from the system, We are offering 1500 for that price and catapults as well. So that's what we're offering for this one. Um, the way the process works is slightly different. So I just want to kind of walk everyone through that a little bit. So for the trading prize, um, what we are doing is we're first providing you assets that will be on support there, and you'll have to bridge those assets in. So if you look here, I'm going to show you how you do that. You go to the deposits page and we're providing two contest specific assets. One we call MF for Mercada F and you bring that in by bridging. So you use the Sepolia F and you can bridge it in on the MF network. Now, when you see this and when you bridge it and connect it to your wallet, you'll see two confirmations and from, say, your external wallet. I personally use MetaMask. So if it's on your MetaMask wallet, you'll see two confirmations, one to verify that the funds are available to send, and then the second to actually bridge in the transaction. And then after that, it will be converted into FST. So it will be bridged, wrapped on the system, and then be converted into FST, where you can start to trade with it. The second way to bring in is the convert tab. So what the convert tab is, it brings in stable coins, like ultimately our version of a stable coin for the contest is called MUSDC that we will provide to every contest participant. And when you bring it in, it automatically converts into USDST. So those are how you kind of start bringing assets into your account. And then from there you can start trading. So you can borrow against those assets by offering them as collateral. And once you, you can see here that I can supply collateral with my FSD and then I can borrow against it. I can swap those out for other assets. And one thing that's really important is that everyone for the contest will have to own at least one of the major assets. So you will have to have USDST, WBTCST, ETHST, GOLDST, and SILVST. You will have to have one of each of those assets to be eligible for the trading prize. And then you can also participate in the pools as well. So you can either provide liquidity to the pools or and also liquidate people whose positions that are coming under risk. So that's how this contest will work. and one other thing we want to mention is that to kind of give a good simulation of uh real life throughout the contest on the telegram channel we will announce special events that will happen that will impact various things on the contest and the prices of assets on the contest so we will announce um sort of sudden airdrops where the first couple people that respond will get additional tokens we are announced sudden price shifts and we will announce also uh you know other things that you know some positions might be liquidatable on the contest so basically all of those things are going to come at random times throughout the day so stay on your toes make sure you sign up to the contest channel on Telegram, which is called CrowdV2 Contest 917 to 923, and then watch out for those because they could come at any time. So with that, I think that's a high-level overview of the contest. Bob, not sure if your audio is working better, but maybe you can chip in here and just test it out." -> Clean up needed.
        *   "degensed by RWAs" -> "degens" (crypto slang) using RWAs? Or "sensitized"? Likely "getting degens into RWAs". "Degensed" sounds like "degens".
        *   "Cata points" -> "Catapult points".
        *   "color points" -> "Catapult points" (likely transcription error again).
        *   "export price" -> "exploit prize" (context: "finds an exploit").
        *   "price" -> "prize".
        *   "Mercada F" -> "Mercada Finance" or just "Mercada F"? Text says "MF for Mercada F". Likely "Mercada Finance". Later "Sepolia F" and "MF network".
        *   "FSD" -> "FST" (typo).
        *   "we are announced sudden price shifts" -> "we will announce sudden price shifts".
        *   "CrowdV2 Contest 917 to 923" -> Likely "CrowdV2 Contest".
    *   **[17:45] SPEAKER_00:** "Yeah, I'll try. Just let me say a little bit, and maybe somebody can confirm if that audio is choppy or not still. Have a look, maybe, Jeremy or Michael." -> Keep.
    *   **[18:01] SPEAKER_01:** "Okay. Unfortunately, it sounds like your audio is still a little bit choppy today. We will work out the audio issues for later, but... Yes, we'll get you some wired headphones, Bob. I think, you know, I think it is a technology problem right now. So we look forward, the contest will run until the following Tuesday at 5pm. So everyone, We look forward to seeing you participate in the contest. We look forward to seeing any of your comments. And please provide whatever feedback that you have on the Telegram feed. Your feedback so far has been immensely helpful. And I think this is going to really make Strato Mercado into an amazing product. So thank you very much. And with that, happy hunting, everyone. Take care." -> Keep. "Strato Mercado" -> "Strata Mercado" (based on earlier "Strata Block apps").
    *   **[19:16] SPEAKER_00:** "Has this stream stopped?" -> Keep.

4.  **Refining Technical Terms & Names:**
    *   "Bob Simwell" -> **Bob Summerwill** (Check List: Yes).
    *   "McCarter" -> **Mercado**.
    *   "MF for Mercada F" -> **MF for Mercado Finance** (Inference) or keep "Mercada F"? "MF" stands for Mercado Finance usually in this context (Strata Mercado Finance). I will correct "Mercada" to "Mercado" to match "MF". "Sepolia F" -> "Sepolia ETH"? Or "Sepolia F" refers to the Faucet? No, "Sepolia F" is likely "Sepolia Faucet" or a specific testnet token name. I will leave "Sepolia F" if it's a specific token name mentioned, but it looks like a typo for "Sepolia ETH" or "Sepolia Faucet". Given "MF network", maybe "Sepolia Faucet". However, without certainty, I might clean "Mercada" to "Mercado" but leave "Sepolia F" or change to "Sepolia testnet ETH". The text says "Use the Sepolia F and you can bridge it in on the MF network". This suggests "Sepolia F" is the source asset. "MF" = Mercado Finance. "Sepolia F" might be "Sepolia Faucet". I will play it safe: "Sepolia F" is likely a typo for "Sepolia ETH" or "Sepolia Faucet". I will change to "Sepolia ETH" or "Sepolia testnet ETH" if it fits. Actually, looking at "Mercada F", "F" might mean "Faucet" or "Finance". Let's stick to correcting "Mercada" to "Mercado".
    *   "Sheba Tarzan" -> "Catapult Tankan". This is a specific name. "Sheba" -> "Catapult" (Token). "Tarzan" -> "Tankan" (Winner). "Cata Tankan" is a known participant in these contests (CataTankan). I will correct to "Cata Tankan".
    *   "degensed" -> "degens" (noun).
    *   "export price" -> "exploit prize".
    *   "color points" -> "Catapult points".
    *   "Strato Mercado" -> "Strata Mercado".
    *   "Mccarter v2" -> "Mercado V2".
    *   "FSD" -> "FST".
    *   "MF network" -> "Mercado Finance network" (or keep MF if defined).

5.  **Drafting the Output (Mental or Scratchpad):**

    *   *Segment 1:* [00:18] SPEAKER_01...
    *   *Segment 2:* [01:28] SPEAKER_00... "Victor".
    *   *Segment 3:* [01:33] SPEAKER_01... Clean fillers.
    *   *Segment 4:* [05:43] SPEAKER_00...
    *   *Segment 5:* [06:21] SPEAKER_01...
    *   *Segment 6:* [06:24] SPEAKER_00... "Texture".
    *   *Segment 7:* [07:02] SPEAKER_01...
    *   *Segment 8:* [07:04] SPEAKER_00...
    *   *Segment 9:* [07:09] SPEAKER_01...
    *   *Segment 10:* [07:17] SPEAKER_00...
    *   *Segment 11:* [07:25] SPEAKER_01...
    *   *Segment 12:* [07:33] SPEAKER_00...
    *   *Segment 13:* [07:43] SPEAKER_01...
    *   *Segment 14:* [08:07] SPEAKER_00... "StreamYard". "X does not make it easy". "Sheba Tarzan" -> "Catapult Tankan".
    *   *Segment 15:* [09:00] SPEAKER_01...
    *   *Segment 16:* [09:08] SPEAKER_00... "Bob Summerwill". "Head of Ecosystem at Strata Block Apps". "Mercado V2". "eBay-ish". "NFT-like".
    *   *Segment 17:* [10:33] SPEAKER_01... "RWAs". "degens". "Strata Mercado". "500 USDC plus Catapult points". "recommended improvement prize". "exploit prize". "MF for Mercado Finance". "Sepolia F" -> "Sepolia ETH"? I'll assume "Sepolia ETH" or just "Sepolia F" if it's a specific asset name used in the contest. I'll stick to the text but fix obvious typos. "Mercada F" -> "Mercado Finance". "FST". "MUSDC". "USDST". "WBTCST". "ETHST". "GOLDST". "SILVST". "FSD" -> "FST". "CrowdV2 Contest".
    *   *Segment 18:* [17:45] SPEAKER_00... "Jeremy or Michael".
    *   *Segment 19:* [18:01] SPEAKER_01... "Strata Mercado". "5pm".
    *   *Segment 20:* [19:16] SPEAKER_00...

6.  **Detailed Word Count Check & Formatting:**
    *   Input length: ~1400 words.
    *   Output length target: ~1260 - 1540 words.
    *   Format: `**[MM:SS] SPEAKER_XX:**` text.

7.  **Specific Corrections & Decisions:**
    *   "MF for Mercada F": "Mercada" is definitely "Mercado". "F" is likely "Finance" (Mercado Finance). I will write "MF for Mercado Finance".
    *   "Sheba Tarzan": Definitely "Catapult Tankan". I will use "Catapult Tankan".
    *   "color points": Definitely "Catapult points".
    *   "export price": Definitely "exploit prize".
    *   "degensed": "getting degens into RWAs".
    *   "Sepolia F": Context implies bridging. Usually you bridge Sepolia ETH. However, if they call it "Sepolia F", I might leave it, but "Sepolia ETH" is standard. I will use "Sepolia ETH" for clarity unless "F" refers to "Faucet" (as in getting funds from the faucet). Actually, "Use the Sepolia F and you can bridge it in...". It might be a specific token name for the contest. I'll stick to "Sepolia ETH" as it's the most likely intended word for a network asset, but given the transcript is messy, I will write "Sepolia ETH" but maybe put a note? No, just clean it. "Sepolia ETH" makes the most sense. Wait, "MF network" -> "Mercado Finance network". "Sepolia F" -> "Sepolia Faucet"? You don't bridge a faucet. You get ETH *from* the faucet. Maybe "Sepolia funds"? I will correct to "Sepolia ETH".
    *   "MF network": "Mercado Finance network".
    *   "CrowdV2 Contest 917 to 923": "CrowdV2 Contest (917 to 923)".
    *   "Strata Block apps": "Strata BlockApps"? The speaker says "Strata Block apps". I'll keep "Strata Block Apps".

8.  **Final Polish of the Text (Simulated):**

    *   [09:08] SPEAKER_00: "Hi everyone, good to have you here. I'm Bob Summerwill, I'm the Head of Ecosystem at Strata Block Apps. Victor who's with us here is the Chief Product Officer and co-founder. Mercado V2 is the new iteration..."
    *   [08:07] SPEAKER_00: "...Just point out with Catapult prize-winning Catapult Tankan in contest number one..."
    *   [10:33] SPEAKER_01: "...getting degens into RWAs... recommended improvement prize... exploit prize... Catapult points... MF for Mercado Finance... FST... MUSDC... USDST... WBTCST, ETHST, GOLDST, SILVST... FSD -> FST."

    Let's review the "degensed" part. "trying to focus on getting degensed by RWAs". "De-gens-ed"? "Getting degens in". Yes. "Getting degens in".

    "Mccarter v2" -> "Mercado V2".
    "Bob simwell" -> "Bob Summerwill".
    "Sheba" -> "Catapult".
    "Tarzan" -> "Tankan".
    "color points" -> "Catapult points".
    "export price" -> "exploit prize".

    Okay, ready to generate.**[00:18] SPEAKER_01:** Okay, can anyone confirm that they can see us on YouTube? Thank you, Michael. Can everyone confirm that they can see us on YouTube and spaces? Michael, can you confirm you can hear us on YouTube?

**[01:28] SPEAKER_00:** You broke up for me quite a lot there, Victor, when you were speaking.

**[01:33] SPEAKER_01:** Okay. Okay. So Jamie, can you post this on our Twitter, the YouTube, and we'll get started shortly. Hey, MK, welcome. Glad you could join us. We're just going to wait a few more minutes and get everyone in. So, okay, we're just waiting a few more minutes for people to kind of start coming in. Thank you everyone for joining us. And we are super excited to announce this contest.

**[05:43] SPEAKER_00:** Welcome, Yves. Stefan. Do you want to give it maybe until 10 past, Victor, three minutes?

**[06:21] SPEAKER_01:** Sure.

**[06:24] SPEAKER_00:** Nice round number. So on one of our spaces not too long ago where we were interviewing Texture, he berated us for talking about the weather when he joined. Do you remember that? We were talking about the turns of the season and when fall was starting and so on.

**[07:02] SPEAKER_01:** I do not remember that.

**[07:04] SPEAKER_00:** And he said we were old for talking about the weather.

**[07:09] SPEAKER_01:** Well, we are old, but you know, like I guess in the, I guess.

**[07:17] SPEAKER_00:** We're experienced. We're not old.

**[07:25] SPEAKER_01:** Should we troll them by talking about the weather now or not?

**[07:33] SPEAKER_00:** Welcome.

**[07:43] SPEAKER_01:** So just for everyone's information, and since we're not going to talk about the weather, this is our first simulcast. It's happening on YouTube Live and Twitter Spaces. There was some behind-the-scenes wiring up of all this. And if anyone has poor audio or anything, please let us know, and we'll try to rectify it next time.

**[08:07] SPEAKER_00:** So yeah, we're using StreamYard, which seems to be sort of the best answer there is. Not great either. Also, X does not make it easy to escape their walled garden. They really want you to do everything on spaces. There isn't even functionality for downloading the audio afterwards natively. They do not want you to escape. However, we found lots of dodgy browser extensions that allow you to do that and command line tools. Just point out with Catapult prize-winning Catapult Tankan in contest number one and back for more in this second contest.

**[09:00] SPEAKER_01:** Yes. And Justin, welcome.

**[09:08] SPEAKER_00:** Okay. So yeah, maybe we start. Okay, hi everyone, good to have you here. I'm Bob Summerwill, I'm the Head of Ecosystem at Strata Block Apps. Victor who's with us here is the Chief Product Officer and co-founder. Mercado V2 is the new iteration of our application of our network which has been a major focus for us this year. We spent the vast majority of this year rebuilding a completely new application experience. The current production mainnet is more of a sort of eBay-ish kind of setup, really coming out of an earlier period where we were having a marketplace of collectibles, tokenized whiskey barrels, and other things which were more NFT-like. The focus for V2 is really about high-quality, hard assets, specifically gold and silver.

**[10:33] SPEAKER_01:** Hey, Bob. We're getting some feedback that your audio is coming in choppy for some reason, but mine seems to be okay. So why don't I take it over from what you said? So as Bob was saying, V2 is really an iteration of what we were doing before. We were kind of offering a lot of different RWAs before, and V2 is our way to kind of really focus on the ability to bring real-world assets and lend and borrow on those assets. So one of the things that we're going to be testing in this iteration of the contest is really how it interacts with the external world, including things like bridging out and bridging in these different assets. And it's really interesting because one of the things I think that stands out in our positioning in terms of the RWA space is most RWA projects seem to really be trying to focus on getting degens into RWAs. We're focused on people who already have RWAs, things like gold, silver, US dollars, and bring that into the crypto ecosystem and the DeFi ecosystem. That's really what we want to test in terms of this overall contest.

What you're seeing on your screen right now is an overview of the new V2 application. It's been basically the focus of our efforts throughout this year. And there have been significant changes to it, which I'll show in one second, from the earlier duration of our contest in July. So thank you for everyone that provided feedback. And that was immensely useful. We took as much of that feedback as we could to bring you this new version of the contest.

Now, in this version of the contest, there are still going to be three prizes since they were before, but they're for slightly different things. So we will have a prize for the best trading award. So whoever has the total net balance of total number of assets and based on all of their activities. So that will be a prize and we've doubled the prizes. So that would be 500 USDC plus Catapult points. And then we will have, instead of like just offering the bug prizes, we have a recommended improvement prize. So for technical people who are not that into trading, please provide us your recommendations on improvements. That prize is also a 500 USDC plus Catapult points. And then we have an exploit prize. So if anyone finds an exploit that could possibly steal funds from the system, we are offering 1500 for that prize and Catapults as well. So that's what we're offering for this one.

The way the process works is slightly different. So I just want to kind of walk everyone through that a little bit. So for the trading prize, what we are doing is we're first providing you assets that will be on support there, and you'll have to bridge those assets in. So if you look here, I'm going to show you how you do that. You go to the deposits page and we're providing two contest specific assets. One we call MF for Mercado Finance and you bring that in by bridging. So you use the Sepolia ETH and you can bridge it in on the MF network. Now, when you see this and when you bridge it and connect it to your wallet, you'll see two confirmations from, say, your external wallet. I personally use MetaMask. So if it's on your MetaMask wallet, you'll see two confirmations, one to verify that the funds are available to send, and then the second to actually bridge in the transaction. And then after that, it will be converted into FST. So it will be bridged, wrapped on the system, and then be converted into FST, where you can start to trade with it.

The second way to bring in is the convert tab. So what the convert tab is, it brings in stablecoins, like ultimately our version of a stablecoin for the contest is called MUSDC that we will provide to every contest participant. And when you bring it in, it automatically converts into USDST. So those are how you kind of start bringing assets into your account. And then from there you can start trading. So you can borrow against those assets by offering them as collateral. And once you, you can see here that I can supply collateral with my FST and then I can borrow against it. I can swap those out for other assets. And one thing that's really important is that everyone for the contest will have to own at least one of the major assets. So you will have to have USDST, WBTCST, ETHST, GOLDST, and SILVST. You will have to have one of each of those assets to be eligible for the trading prize. And then you can also participate in the pools as well. So you can either provide liquidity to the pools or and also liquidate people whose positions that are coming under risk.

So that's how this contest will work. And one other thing we want to mention is that to kind of give a good simulation of real life, throughout the contest on the Telegram channel we will announce special events that will happen that will impact various things on the contest and the prices of assets on the contest. So we will announce sudden airdrops where the first couple people that respond will get additional tokens. We will announce sudden price shifts and we will announce also other things that some positions might be liquidatable on the contest. So basically all of those things are going to come at random times throughout the day so stay on your toes. Make sure you sign up to the contest channel on Telegram, which is called CrowdV2 Contest 917 to 923, and then watch out for those because they could come at any time. So with that, I think that's a high-level overview of the contest. Bob, not sure if your audio is working better, but maybe you can chip in here and just test it out.

**[17:45] SPEAKER_00:** Yeah, I'll try. Just let me say a little bit, and maybe somebody can confirm if that audio is choppy or not still. Have a look, maybe, Jeremy or Michael.

**[18:01] SPEAKER_01:** Okay. Unfortunately, it sounds like your audio is still a little bit choppy today. We will work out the audio issues for later, but... Yes, we'll get you some wired headphones, Bob. I think it is a technology problem right now. So we look forward, the contest will run until the following Tuesday at 5pm. So everyone, we look forward to seeing you participate in the contest. We look forward to seeing any of your comments. And please provide whatever feedback that you have on the Telegram feed. Your feedback so far has been immensely helpful. And I think this is going to really make Strata Mercado into an amazing product. So thank you very much. And with that, happy hunting, everyone. Take care.

**[19:16] SPEAKER_00:** Has this stream stopped?