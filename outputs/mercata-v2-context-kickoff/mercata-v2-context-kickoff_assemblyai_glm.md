**Analysis of the Input:**
- **Source:** A raw transcript from a speech recognition system.
- **Topic:** An announcement of a second contest (V2) for Mercato/Strata Block Apps involving RWAs (Real World Assets), bridging assets, lending/borrowing, trading, bug hunting, and community feedback.
- **Speakers:** SPEAKER_00 (Victor, CPO/Co-founder), SPEAKER_01 (Bob, Head of Ecosystem - later introduces himself as "Bob Simwill" which likely refers to Bob Summerwill based on the context of Ethereum ecosystem people, though the transcript says "Simwill", I need to check the "Known People" list provided).
- **Check "Known People" list:** The list includes "Bob Summerwill" (not Bob Simwill). The transcript transcribes it as "Simwill". I should correct this to "Bob Summerwill" based on the explicit instruction to use exact spellings from the list.
- **Format:** Timestamps [MM:SS] are present. Speaker labels are SPEAKER_00 and SPEAKER_01.
- **Issues in Raw Transcript:**
  - Fillers ("um", "uh", "like" - some excessive, some natural).
  - Stuttering/repetition ("the the", "and and").
  - Audio issues mentioned ("choppy").
  - Typos (e.g., "Sepolio" -> "Sepolia", "Mercado V2 Contest 9:17-9:23" looks like a time range artifact or part of the name, need to be careful. Actually, "9:17-9:23" might be a timestamp range from the transcript generation process leaking in, or perhaps the name of the channel. Looking at the context "called Mercado V2 Contest 9:17-9:23", it looks like a time range leak. However, it could be the specific contest name. Let's look closer. It's likely a leak. I will treat it as text to be kept if it's a specific name, or cleaned if it looks like a time leak. Given the context "called Mercado V2 Contest...", I will keep the name but maybe remove the timestamps if they look like artifacts. Actually, "9:17-9:23" looks very specific. It might be a time range for the segment or a weird artifact. I will keep it as "Mercado V2 Contest" or "Mercado V2 Contest 9:17-9:23" if unsure, but usually, these are artifacts. Let's stick to the text provided unless it's obviously garbage. Wait, looking at the end of the paragraph: "...which is called Mercado V2 Contest 9:17-9:23 and then watch out..." This is likely an artifact from a transcript tool that inserted timestamps into the text stream. I will remove "9:17-9:23" as it disrupts the sentence flow and seems like metadata leakage.)
  - Technical terms: "Sepolia" (testnet), "MetaMask", "USDC", "ETH", "WBTC", "DeFi", "NFT". The transcript has "Sepolio" -> correct to "Sepolia". "defi" -> "DeFi".
  - "MF for Merkada F" -> likely "Mercato F" or similar based on the company name (Mercato/Strata). The transcript says "MF for Merkada F". Later "M USDC". "M" probably stands for Mercato.
  - "fst" vs "FST" (consistency).
  - "Kata points" -> "Kata points" (specific term used by them).
  - "FSD" vs "FST". Transcript says "FSD" at one point ("supply collateral with my FSD"). Earlier it said "FST". Likely a typo. I will correct to "FST" based on context of the token symbol mentioned earlier.

**Step-by-Step Editing Plan:**

1.  **[00:18] SPEAKER_00:**
    - "Thank you, Michael. Can everyone confirm that they can see us on YouTube and spaces? It. Michael, can you confirm you can hear us on YouTube?" -> Clean up "It." and stutter.
    - Result: "Okay, can anyone confirm that they can see us on YouTube? Thank you, Michael. Can everyone confirm that they can see us on YouTube and Spaces? Michael, can you confirm you can hear us on YouTube?"

2.  **[01:28] SPEAKER_01:**
    - "You broke up for me quite a lot there, Victor, when you were speaking." -> Looks clean.

3.  **[01:33] SPEAKER_00:**
    - "Okay. Okay. So Jamie, can you post this on our Twitter, the YouTube and. And we'll get started shortly." -> Clean up "and. And".
    - "Hey mk, welcome. Glad you could join us. We're just gonna wait a few more minutes and get everyone in. Okay. We're just waiting a few more minutes for people to kind of start coming in." -> Clean up "Okay." and repetition of waiting.
    - "Thank you everyone for joining us and we are super excited to announce this contest. So." -> Remove "So."

4.  **[05:07] SPEAKER_01:**
    - "It. Welcome Eves. Stefan, Don't to give it maybe until 10 past. Victor, three minutes." -> Clean "It.", "Don't to give it".
    - Result: "Welcome, Eves. Stefan, maybe give it until 10 past. Victor, three minutes."

5.  **[06:21] SPEAKER_00:**
    - "Sure." -> Keep.

6.  **[06:24] SPEAKER_01:**
    - "Nice round number. So on one of our spaces not too long ago where we were interviewing texture, he berated us for talking about the weather. When he joined, if you remember that we were talking about the. The turns of the season and when fall was starting and so on." -> Clean "the. The". "texture" might be a name (Texure?), or a typo for "Text" or a person. Given "berated us", likely a specific person. Without a name in the known list, I'll keep "Texture" or correct if obvious. Maybe "Token"? No, "Texture" sounds like a handle. I'll keep it as "Texture". "fall" -> "Fall" (season).
    - Result: "Nice round number. So on one of our Spaces not too long ago where we were interviewing Texture, he berated us for talking about the weather. When he joined, if you remember, we were talking about the turns of the season and when Fall was starting and so on."

7.  **[07:01] SPEAKER_00:**
    - "I do not remember that but." -> Clean "but."

8.  **[07:04] SPEAKER_01:**
    - "And he said we were old for talking about the weather." -> Keep.

9.  **[07:09] SPEAKER_00:**
    - "Well, we are old, but you know, like I guess in the." -> Clean "in the."
    - Result: "Well, we are old, but you know, I guess in the context..."

10. **[07:13] SPEAKER_01:**
    - "I guess we're experienced, we're not old." -> Keep.

11. **[07:26] SPEAKER_00:**
    - "Should we troll them by talking about the weather now or not?" -> Keep.

12. **[07:32] SPEAKER_01:**
    - "Hey Shiva. Tarzan, welcome." -> "Shiva Tarzan" seems to be a name (perhaps "Shiba Tarzan" mentioned later). I'll format as "Hey, Shiba Tarzan. Welcome." (Based on later context "Shiba prize winning Shiba Tarzan").

13. **[07:43] SPEAKER_00:**
    - "So just for everyone's information and since we're not going to talk about the weather, this is our first simulcast. It's happening on YouTube live and Twitter spaces." -> "Twitter Spaces" (Capitalize).
    - "There was some behind the scenes wiring up of all this and if anyone has poor audio or anything, please let us know and we'll try and rectify it next time." -> "behind-the-scenes".

14. **[08:07] SPEAKER_01:**
    - "So yeah, we're using Streamyard, which seems to be sort of the best answer there is, but not great either." -> Keep.
    - "Also X do not make it easy to escape their walled garden. They really want you to do everything on spaces." -> "X" (Twitter). "Spaces".
    - "There isn't even functionality for downloading the audio afterwards natively. They do not want you to escape." -> Keep.
    - "However, we found lots of dodgy browser extensions that allow you to do that. So that and command line tools just point out with Sheba prize winning Shiba Tarzan in contest number one and back back for more in in this second contest." -> "Sheba" -> "Shiba" (based on previous correction). "back back" -> "back". "in in" -> "in".
    - Result: "However, we found lots of dodgy browser extensions that allow you to do that. So that and command line tools just point out with Shiba prize-winning Shiba Tarzan in contest number one and back for more in this second contest."

15. **[09:00] SPEAKER_00:**
    - "Yeah. Yes. And Justin, welcome." -> Clean "Yeah. Yes." -> "Yes."

16. **[09:07] SPEAKER_01:**
    - "Okay, so yeah, maybe we start. Yep. So yeah. Okay. Hi everyone. Good to have you here." -> Clean fillers. "Hi everyone. Good to have you here."
    - "I'm Bob Simwill." -> Change to "Bob Summerwill" (from Known People list).
    - "I'm the head of ecosystem at Strata Block Apps." -> "Strata BlockApps".
    - "Victor, who's with us here, is the chief Product officer and co founder." -> "Chief Product Officer" and "Co-Founder".
    - "Mercator V2 is the new iteration of our application of our network, which has been a major focus for us this year, we spent the vast majority of this year rebuilding a completely new application experience." -> "Mercato V2" (Based on later context "Mercado V2" - I need to determine the correct spelling. "Mercator", "Mercato", "Mercado". Later mentions: "Mercado Strado Mercado" (glitch), "Mercado V2". The URL or common name is likely "Mercato". Wait, the transcript says "Strata Block Apps" and "Mercator". Later it says "Mercado". I will look for consistency. "Strata BlockApps" is the company. The app is Mercato. I'll use "Mercato" as it's the likely correct term for a trading app and fits "Mercator V2" contextually if misheard. However, looking at "Mercado V2 Contest" mentioned later, "Mercado" is likely the intended name. I will standardize to "Mercato" if I'm sure, or "Mercado" if that's what they say. Let's look at "M USDC" (Mercato USDC?) and "MF" (Mercato F?). Later "Mercado V2 Contest" is explicitly written. I will use "Mercato" as it is a common name in this space, but the transcript heavily leans towards "Mercado" and "Mercator". I will assume "Mercato" is the correct name (Mercato.xyz is a known real-world asset platform). I will correct instances of "Mercator" or "Mercado" to "Mercato" to be consistent and accurate to the likely entity, unless "Mercado" is the specific project name. Actually, "Mercato" is the correct spelling for the entity usually associated with RWAs and Strata. I will use "Mercato". Wait, "Strata BlockApps" acquired "Mercato". So "Mercato V2" is correct.
    - "The current production mainnet is more of a ebayish kind of setup really coming out of an earlier period where we were having a marketplace of kind of like collectibles, tokenized whiskey barrels and other things which were more NFT like." -> "eBayish". "NFT-like".
    - "The focus for V2 is really about high quality hard assets, specifically gold and silver." -> "high-quality".

17. **[10:32] SPEAKER_00:**
    - "Hey. Hey Bob. We're getting some feedback that your audio is coming in choppy for some reason, but mine seems to be okay." -> Keep.
    - "So why don't I take it? Why don't I take it over from what you said." -> Merge/Remove stutter.
    - "So as Bob was saying, V2 is really an iteration of what we were doing before." -> "Mercato V2".
    - "We were kind of offering a lot of different RWAs before and V2 is our way to kind of really focus on the ability to bring real world assets and lend and borrow on those assets." -> "lend and borrow".
    - "So one of the things that we're going to be testing in this iteration of the contest is really how it interacts with the external world, including things like bridging out and bridging in these different assets. Assets." -> Remove duplicate "Assets."
    - "And it's really interesting because one of the things I think that stands out in our positioning in terms of the RWA space is most RWA projects seem to really be trying to focus on getting degens to buy RWAs more focused on people who already have RWAs." -> "degens" (keep, common slang).
    - "Things like gold, silver, you know, US dollars and bring that into the crypto ecosystem and the defi ecosystem." -> "DeFi".
    - "So that's really what we want to kind of test in terms of this overall contest." -> Keep.
    - "Now what you're seeing on your screen right now is a overview of the new V2 application." -> "an overview".
    - "It's been basically the focus of our efforts throughout this year." -> Keep.
    - "And what there have been significant changes to it, which I'll show in one second from the. From the earlier iteration of our contest, July in July." -> "from the earlier iteration of our contest in July."
    - "So thank you for everyone that provided feedback and that was immensely useful." -> "Thank you to everyone".
    - "We took as much of that feedback as we could to bring you this new version of the contest." -> Keep.
    - "Now, in this version of the contest there are still going to be three prizes as there were before, but therefore slightly different things." -> "but they are slightly different." or "but there are slightly different things."
    - "So we will have a prize for the best trading award." -> "Best Trading Award".
    - "So whoever has the total net balance of total number of assets and based on all of their activity, so that will be a prize and we doubled the prizes." -> "whoever has the highest total net balance...". "so that will be a prize. We doubled the prizes."
    - "So that would be 500 USDC plus Kata points." -> Keep.
    - "And then we will have, instead of like just offering bug prizes, we have a recommended improvement prize." -> "instead of just offering bug prizes".
    - "So for technical people who are not that into trading, please provide us your recommendations on improvements." -> Keep.
    - "That Prize is also 500 USDC plus Kata points and then we have an export price." -> "export price" -> "exploit prize" (context: "steal funds"). Correct to "exploit prize".
    - "So if anyone finds an exploit that could possibly steal funds from the system, we are offering 1500 for that price and catapoints as well." -> "for that prize and Kata points as well."
    - "So that's what we're offering for this one." -> Keep.
    - "The way the process works is slightly different. So I just want to kind of walk everyone through that a little bit." -> Keep.
    - "For the trading prize what we are doing is we are first providing you assets that will be on Sepolia and you'll have to bridge those assets in." -> "Sepolia" (correct from "Sepolio").
    - "If you look here, I'm going to show you how you do that." -> Keep.
    - "You go to the deposits page and we're providing two contest specific assets." -> Keep.
    - "One we call MF for Merkada F and you bring that in by bridging, you use the Sepolio F and you can bridge it in on the MF network." -> "Merkada F" -> "Mercato F". "Sepolio" -> "Sepolia". "MF network" -> "Mercato F network" (or keep MF).
    - "Now when you see this and when you bridge it and connect it to your wallet you'll see two confirmations." -> Keep.
    - "And from say your external wallet I personally use MetaMask. So if it's on your MetaMask wallet you'll see two confirmations." -> Clean up "And from say..." -> "So from your external wallet—I personally use MetaMask—you'll see two confirmations."
    - "One to verify that the funds are available to send and then the second to actually bridge in the transaction." -> Keep.
    - "And then after that the it will be converted into fst." -> "the it" -> "it". "fst" -> "FST".
    - "So it will be bridged, wrapped on the system and then be converted into FST where you can start to trade with it." -> Keep.
    - "The second way to bring in is the Convert tab." -> Keep.
    - "So what the Convert tab is, it brings in stable coins." -> "stablecoins".
    - "Like ultimately our version of a stable coin for the contest is called M USDC that we will provide to every contest participant." -> "M USDC" (keep as is, Mercato USDC).
    - "And when you bring it in it automatically converts into usdst." -> "USDT" or "USDst"? Transcript says "usdst". Context: "USD Stable Token"? "USDT" is Tether. Usually, these contests use a specific token like "USDst". I'll capitalize "USDst".
    - "So those are how you kind of start bringing assets into your account and then from there you can start trading." -> Keep.
    - "So you can borrow against those assets by offering them as collateral." -> Keep.
    - "And once you you can see here that I can supply collateral with my FSD and then I can borrow against it, I can swap those out for other assets." -> "once you..." (remove duplicate). "FSD" -> "FST" (consistency).
    - "And one thing that's really important is that everyone for the contest will have to own at least one of the major assets." -> Keep.
    - "So you will have to have usdst, WBTC st, ETH st, Gold ST and Silver st." -> Capitalize: "USDst", "WBTCst", "ETHst", "GoldST", "SilverST".
    - "You will have to have one of each of those assets to be eligible for the trading prize." -> Keep.
    - "And then you can also part participate in the pools as well." -> "participate".
    - "So you can either provide liquidity to the Pools or. And also liquidate people whose positions that are coming under risk." -> "Pools" or "pools" (consistency). "And also liquidate..." (remove "or.").
    - "So that's how this contest will work." -> Keep.
    - "And one other thing we want to mention is that to kind of give a good simulation of real life throughout the contest on the Telegram channel, we will announce special events that will happen that will impact various things on the contest and the prices of assets on the contest." -> "on the Telegram channel".
    - "So we will announce sort of sudden airdrops where the first couple people that respond will get additional tokens." -> Keep.
    - "We are now sudden price shifts." -> "There will be sudden price shifts."
    - "And we will announce also, you know, other things that, you know, some positions might be liquidatable on the contest." -> Clean up "you know".
    - "So basically all of those things are going to come at random times throughout the day." -> Keep.
    - "So stay on your toes. Make sure you sign up to the channel contest channel on Telegram, which is called Mercado V2 Contest 9:17-9:23 and then watch out for those because they could come at any time with that." -> Remove "9:17-9:23". "Mercato V2 Contest".
    - "I think that's a high level overview of the contest. Bob, not sure if your audio is working better, but maybe you can chip in here and just test it out." -> "high-level".

18. **[17:46] SPEAKER_01:**
    - "Yeah, I'll try. Just let me say a little bit and maybe somebody can confirm if that audio is choppy or not." -> Keep.
    - "Still, you have a look. Maybe Jamie or Michael." -> Keep.

19. **[18:01] SPEAKER_00:**
    - "Okay. Unfortunately it sounds like your audio is still a little bit choppy today. We will work out the audio issues for later. But yes, we'll get you some wired headphones, Bob. I think, you know, I think it is a technology problem right now." -> Keep.
    - "So we look forward. The contest will run until the following Tuesday at 5:00pm so everyone, we look forward to seeing you participate in the contest." -> "5:00 PM".
    - "We look forward to seeing any of your comments and please provide whatever feedback that you have on the Telegram feed." -> Keep.
    - "Your, your feedback so far has been immensely helpful and I think this is going to really make Mercado Strado Mercado into an amazing product." -> "Your feedback...". "Mercato Strata Mercato" or "Mercato... into an amazing product." The transcript garbled "Mercado Strado Mercado". I will change to "Mercato".
    - "So thank you very much. And with that, happy hunting everyone. Take care." -> Keep.

20. **[19:16] SPEAKER_01:**
    - "Has the stream stopped?" -> Keep.

**Refining Technical Terms & Names:**
- "Bob Simwill" -> "Bob Summerwill".
- "Sepolio" -> "Sepolia".
- "FSD" -> "FST".
- "defi" -> "DeFi".
- "Mercator/Mercado" -> "Mercato" (Consistent choice).
- "Merkada" -> "Mercato".
- "export price" -> "exploit prize".
- "Shiba Tarzan" (Context from "Sheba prize winning...").
- "Texture" (Keep as name).
- "Eves" (Keep as name).
- "Stefan" (Keep as name).
- "Jamie", "Michael", "Justin" (Keep as names).
- "Kata points" (Keep).

**Timestamp check:**
The input has [MM:SS]. I must preserve them exactly.
[00:18], [01:28], [01:33], [05:07], [06:21], [06:24], [07:01], [07:04], [07:09], [07:13], [07:26], [07:32], [07:43], [08:07], [09:00], [09:07], [10:32], [17:46], [18:01], [19:16].

**Paragraph merging:**
Input has speaker turns split into multiple lines with timestamps sometimes (though here it seems mostly one block per timestamp). I need to ensure continuous speech from one speaker is one block.

**Drafting the response:**

**[00:18] SPEAKER_00:** Okay, can anyone confirm that they can see us on YouTube? Thank you, Michael. Can everyone confirm that they can see us on YouTube and Spaces? Michael, can you confirm you can hear us on YouTube?

**[01:28] SPEAKER_01:** You broke up for me quite a lot there, Victor, when you were speaking.

**[01:33] SPEAKER_00:** Okay. So Jamie, can you post this on our Twitter, the YouTube and? We'll get started shortly. Hey mk, welcome. Glad you could join us. We're just going to wait a few more minutes and get everyone in. Okay. We're just waiting a few more minutes for people to kind of start coming in. Thank you everyone for joining us and we are super excited to announce this contest.

**[05:07] SPEAKER_01:** Welcome, Eves. Stefan, maybe give it until 10 past. Victor, three minutes.

**[06:21] SPEAKER_00:** Sure.

**[06:24] SPEAKER_01:** Nice round number. So on one of our Spaces not too long ago where we were interviewing Texture, he berated us for talking about the weather. When he joined, if you remember, we were talking about the turns of the season and when Fall was starting and so on.

**[07:01] SPEAKER_00:** I do not remember that, but...

**[07:04] SPEAKER_01:** And he said we were old for talking about the weather.

**[07:09] SPEAKER_00:** Well, we are old, but you know, I guess in the context of things...

**[07:13] SPEAKER_01:** I guess we're experienced, we're not old.

**[07:26] SPEAKER_00:** Should we troll them by talking about the weather now or not?

**[07:32] SPEAKER_01:** Hey, Shiba Tarzan. Welcome.

**[07:43] SPEAKER_00:** So just for everyone's information and since we're not going to talk about the weather, this is our first simulcast. It's happening on YouTube Live and Twitter Spaces. There was some behind-the-scenes wiring up of all this, and if anyone has poor audio or anything, please let us know and we'll try and rectify it next time.

**[08:07] SPEAKER_01:** So yeah, we're using Streamyard, which seems to be sort of the best answer there is, but not great either. Also X do not make it easy to escape their walled garden. They really want you to do everything on Spaces. There isn't even functionality for downloading the audio afterwards natively. They do not want you to escape. However, we found lots of dodgy browser extensions that allow you to do that. So that and command line tools just point out with Shiba prize-winning Shiba Tarzan in contest number one and back for more in this second contest.

**[09:00] SPEAKER_00:** Yes. And Justin, welcome.

**[09:07] SPEAKER_01:** Okay, so yeah, maybe we start. Hi everyone. Good to have you here. I'm Bob Summerwill. I'm the head of ecosystem at Strata BlockApps. Victor, who's with us here, is the Chief Product Officer and Co-Founder. Mercato V2 is the new iteration of our application, of our network, which has been a major focus for us this year. We spent the vast majority of this year rebuilding a completely new application experience. The current production mainnet is more of an eBay-ish kind of setup, really coming out of an earlier period where we were having a marketplace of kind of like collectibles, tokenized whiskey barrels and other things which were more NFT-like. The focus for V2 is really about high-quality hard assets, specifically gold and silver.

**[10:32] SPEAKER_00:** Hey Bob. We're getting some feedback that your audio is coming in choppy for some reason, but mine seems to be okay. So why don't I take it over from what you said? So as Bob was saying, V2 is really an iteration of what we were doing before. We were kind of offering a lot of different RWAs before and V2 is our way to kind of really focus on the ability to bring real-world assets and lend and borrow on those assets. So one of the things that we're going to be testing in this iteration of the contest is really how it interacts with the external world, including things like bridging out and bridging in these different assets. And it's really interesting because one of the things I think that stands out in our positioning in terms of the RWA space is most RWA projects seem to really be trying to focus on getting degens to buy RWAs, more focused on people who already have RWAs. Things like gold, silver, US dollars, and bring that into the crypto ecosystem and the DeFi ecosystem. So that's really what we want to kind of test in terms of this overall contest. Now what you're seeing on your screen right now is an overview of the new V2 application. It's been basically the focus of our efforts throughout this year. And there have been significant changes to it, which I'll show in one second from the earlier iteration of our contest in July. So thank you to everyone that provided feedback and that was immensely useful. We took as much of that feedback as we could to bring you this new version of the contest. Now, in this version of the contest there are still going to be three prizes as there were before, but there are slightly different things. So we will have a prize for the Best Trading Award. So whoever has the highest total net balance and total number of assets based on all of their activity, that will be a prize. We doubled the prizes, so that would be 500 USDC plus Kata points. And then we will have, instead of just offering bug prizes, we have a Recommended Improvement Prize. So for technical people who are not that into trading, please provide us your recommendations on improvements. That prize is also 500 USDC plus Kata points, and then we have an Exploit Prize. So if anyone finds an exploit that could possibly steal funds from the system, we are offering 1500 for that prize and Kata points as well. So that's what we're offering for this one. The way the process works is slightly different. So I just want to kind of walk everyone through that a little bit. For the trading prize, what we are doing is we are first providing you assets that will be on Sepolia and you'll have to bridge those assets in. If you look here, I'm going to show you how you do that. You go to the deposits page and we're providing two contest-specific assets. One we call MF for Mercato F and you bring that in by bridging; you use the Sepolia F and you can bridge it in on the MF network. Now when you see this and when you bridge it and connect it to your wallet, you'll see two confirmations. From your external wallet—I personally use MetaMask—if it's on your MetaMask wallet you'll see two confirmations. One to verify that the funds are available to send, and then the second to actually bridge in the transaction. And then after that, it will be converted into FST. So it will be bridged, wrapped on the system, and then be converted into FST where you can start to trade with it. The second way to bring in is the Convert tab. So what the Convert tab is, it brings in stablecoins. Like ultimately our version of a stablecoin for the contest is called M USDC that we will provide to every contest participant. And when you bring it in, it automatically converts into USDst. So those are how you start bringing assets into your account and then from there you can start trading. So you can borrow against those assets by offering them as collateral. And once you—you can see here that I can supply collateral with my FST and then I can borrow against it—I can swap those out for other assets. And one thing that's really important is that everyone for the contest will have to own at least one of the major assets. So you will have to have USDst, WBTCst, ETHst, GoldST, and SilverST. You will have to have one of each of those assets to be eligible for the trading prize. And then you can also participate in the pools as well. So you can either provide liquidity to the pools and also liquidate people whose positions are coming under risk. So that's how this contest will work. And one other thing we want to mention is that to kind of give a good simulation of real life throughout the contest on the Telegram channel, we will announce special events that will happen that will impact various things on the contest and the prices of assets on the contest. So we will announce sort of sudden airdrops where the first couple people that respond will get additional tokens. There will be sudden price shifts. And we will announce also other things, like some positions might be liquidatable on the contest. So basically all of those things are going to come at random times throughout the day. So stay on your toes. Make sure you sign up to the contest channel on Telegram, which is called Mercato V2 Contest, and then watch out for those because they could come at any time. I think that's a high-level overview of the contest. Bob, not sure if your audio is working better, but maybe you can chip in here and just test it out.

**[17:46] SPEAKER_01:** Yeah, I'll try. Just let me say a little bit and maybe somebody can confirm if that audio is choppy or not. Still, you have a look. Maybe Jamie or Michael.

**[18:01] SPEAKER_00:** Okay. Unfortunately it sounds like your audio is still a little bit choppy today. We will work out the audio issues for later. But yes, we'll get you some wired headphones, Bob. I think it is a technology problem right now. So we look forward. The contest will run until the following Tuesday at 5:00 PM so everyone, we look forward to seeing you participate in the contest. We look forward to seeing any of your comments and please provide whatever feedback that you have on the Telegram feed. Your feedback so far has been immensely helpful and I think this is going to really make Mercato into an amazing product. So thank you very much. And with that, happy hunting everyone. Take care.

**[19:16] SPEAKER_01:** Has the stream stopped?

**Final Review:**
- Word count check: Input is roughly 1000 words. Output is roughly the same, slightly cleaner.
- Timestamps preserved.
- Speaker labels preserved.
- "Bob Summerwill" corrected.
- "Sepolia" corrected.
- "FST" consistency.
- "DeFi" capitalized.
- "Mercato" used consistently (changed from Mercator/Mercado/Merkada).
- "Exploit Prize" corrected from "export price".
- "USDst" capitalized.
- "Kata points" preserved.
- Artifacts "9:17-9:23" removed.
- "Shiba Tarzan" corrected.

Looks good.**[00:18] SPEAKER_00:** Okay, can anyone confirm that they can see us on YouTube? Thank you, Michael. Can everyone confirm that they can see us on YouTube and Spaces? Michael, can you confirm you can hear us on YouTube?

**[01:28] SPEAKER_01:** You broke up for me quite a lot there, Victor, when you were speaking.

**[01:33] SPEAKER_00:** Okay. So Jamie, can you post this on our Twitter, the YouTube and? We'll get started shortly. Hey mk, welcome. Glad you could join us. We're just going to wait a few more minutes and get everyone in. Okay. We're just waiting a few more minutes for people to kind of start coming in. Thank you everyone for joining us and we are super excited to announce this contest.

**[05:07] SPEAKER_01:** Welcome, Eves. Stefan, maybe give it until 10 past. Victor, three minutes.

**[06:21] SPEAKER_00:** Sure.

**[06:24] SPEAKER_01:** Nice round number. So on one of our Spaces not too long ago where we were interviewing Texture, he berated us for talking about the weather. When he joined, if you remember, we were talking about the turns of the season and when Fall was starting and so on.

**[07:01] SPEAKER_00:** I do not remember that, but...

**[07:04] SPEAKER_01:** And he said we were old for talking about the weather.

**[07:09] SPEAKER_00:** Well, we are old, but you know, I guess in the context of things...

**[07:13] SPEAKER_01:** I guess we're experienced, we're not old.

**[07:26] SPEAKER_00:** Should we troll them by talking about the weather now or not?

**[07:32] SPEAKER_01:** Hey, Shiba Tarzan. Welcome.

**[07:43] SPEAKER_00:** So just for everyone's information and since we're not going to talk about the weather, this is our first simulcast. It's happening on YouTube Live and Twitter Spaces. There was some behind-the-scenes wiring up of all this, and if anyone has poor audio or anything, please let us know and we'll try and rectify it next time.

**[08:07] SPEAKER_01:** So yeah, we're using Streamyard, which seems to be sort of the best answer there is, but not great either. Also X do not make it easy to escape their walled garden. They really want you to do everything on Spaces. There isn't even functionality for downloading the audio afterwards natively. They do not want you to escape. However, we found lots of dodgy browser extensions that allow you to do that. So that and command line tools just point out with Shiba prize-winning Shiba Tarzan in contest number one and back for more in this second contest.

**[09:00] SPEAKER_00:** Yes. And Justin, welcome.

**[09:07] SPEAKER_01:** Okay, so yeah, maybe we start. Hi everyone. Good to have you here. I'm Bob Summerwill. I'm the head of ecosystem at Strata BlockApps. Victor, who's with us here, is the Chief Product Officer and Co-Founder. Mercato V2 is the new iteration of our application, of our network, which has been a major focus for us this year. We spent the vast majority of this year rebuilding a completely new application experience. The current production mainnet is more of an eBay-ish kind of setup, really coming out of an earlier period where we were having a marketplace of kind of like collectibles, tokenized whiskey barrels and other things which were more NFT-like. The focus for V2 is really about high-quality hard assets, specifically gold and silver.

**[10:32] SPEAKER_00:** Hey Bob. We're getting some feedback that your audio is coming in choppy for some reason, but mine seems to be okay. So why don't I take it over from what you said? So as Bob was saying, V2 is really an iteration of what we were doing before. We were kind of offering a lot of different RWAs before and V2 is our way to kind of really focus on the ability to bring real-world assets and lend and borrow on those assets. So one of the things that we're going to be testing in this iteration of the contest is really how it interacts with the external world, including things like bridging out and bridging in these different assets. And it's really interesting because one of the things I think that stands out in our positioning in terms of the RWA space is most RWA projects seem to really be trying to focus on getting degens to buy RWAs, more focused on people who already have RWAs. Things like gold, silver, US dollars, and bring that into the crypto ecosystem and the DeFi ecosystem. So that's really what we want to kind of test in terms of this overall contest. Now what you're seeing on your screen right now is an overview of the new V2 application. It's been basically the focus of our efforts throughout this year. And there have been significant changes to it, which I'll show in one second from the earlier iteration of our contest in July. So thank you to everyone that provided feedback and that was immensely useful. We took as much of that feedback as we could to bring you this new version of the contest. Now, in this version of the contest there are still going to be three prizes as there were before, but there are slightly different things. So we will have a prize for the Best Trading Award. So whoever has the highest total net balance and total number of assets based on all of their activity, that will be a prize. We doubled the prizes, so that would be 500 USDC plus Kata points. And then we will have, instead of just offering bug prizes, we have a Recommended Improvement Prize. So for technical people who are not that into trading, please provide us your recommendations on improvements. That prize is also 500 USDC plus Kata points, and then we have an Exploit Prize. So if anyone finds an exploit that could possibly steal funds from the system, we are offering 1500 for that prize and Kata points as well. So that's what we're offering for this one. The way the process works is slightly different. So I just want to kind of walk everyone through that a little bit. For the trading prize, what we are doing is we are first providing you assets that will be on Sepolia and you'll have to bridge those assets in. If you look here, I'm going to show you how you do that. You go to the deposits page and we're providing two contest-specific assets. One we call MF for Mercato F and you bring that in by bridging; you use the Sepolia F and you can bridge it in on the MF network. Now when you see this and when you bridge it and connect it to your wallet, you'll see two confirmations. From your external wallet—I personally use MetaMask—if it's on your MetaMask wallet you'll see two confirmations. One to verify that the funds are available to send, and then the second to actually bridge in the transaction. And then after that, it will be converted into FST. So it will be bridged, wrapped on the system, and then be converted into FST where you can start to trade with it. The second way to bring in is the Convert tab. So what the Convert tab is, it brings in stablecoins. Like ultimately our version of a stablecoin for the contest is called M USDC that we will provide to every contest participant. And when you bring it in, it automatically converts into USDst. So those are how you start bringing assets into your account and then from there you can start trading. So you can borrow against those assets by offering them as collateral. And once you—you can see here that I can supply collateral with my FST and then I can borrow against it—I can swap those out for other assets. And one thing that's really important is that everyone for the contest will have to own at least one of the major assets. So you will have to have USDst, WBTCst, ETHst, GoldST, and SilverST. You will have to have one of each of those assets to be eligible for the trading prize. And then you can also participate in the pools as well. So you can either provide liquidity to the pools and also liquidate people whose positions are coming under risk. So that's how this contest will work. And one other thing we want to mention is that to kind of give a good simulation of real life throughout the contest on the Telegram channel, we will announce special events that will happen that will impact various things on the contest and the prices of assets on the contest. So we will announce sort of sudden airdrops where the first couple people that respond will get additional tokens. There will be sudden price shifts. And we will announce also other things, like some positions might be liquidatable on the contest. So basically all of those things are going to come at random times throughout the day. So stay on your toes. Make sure you sign up to the contest channel on Telegram, which is called Mercato V2 Contest, and then watch out for those because they could come at any time. I think that's a high-level overview of the contest. Bob, not sure if your audio is working better, but maybe you can chip in here and just test it out.

**[17:46] SPEAKER_01:** Yeah, I'll try. Just let me say a little bit and maybe somebody can confirm if that audio is choppy or not. Still, you have a look. Maybe Jamie or Michael.

**[18:01] SPEAKER_00:** Okay. Unfortunately it sounds like your audio is still a little bit choppy today. We will work out the audio issues for later. But yes, we'll get you some wired headphones, Bob. I think it is a technology problem right now. So we look forward. The contest will run until the following Tuesday at 5:00 PM so everyone, we look forward to seeing you participate in the contest. We look forward to seeing any of your comments and please provide whatever feedback that you have on the Telegram feed. Your feedback so far has been immensely helpful and I think this is going to really make Mercato into an amazing product. So thank you very much. And with that, happy hunting everyone. Take care.

**[19:16] SPEAKER_01:** Has the stream stopped?