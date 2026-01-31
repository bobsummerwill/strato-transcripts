1.  **Analyze the Request:**
    *   **Role:** Expert transcript editor specializing in Ethereum and blockchain technology.
    *   **Context:** Provided lists of Known People (244) and Technical Terms (163).
    *   **Input:** A raw transcript with timestamps (MM:SS format) and speaker labels (SPEAKER_00, SPEAKER_01, etc.).
    *   **Primary Objective:** Clean, readable transcript preserving *ALL* dialogue and content.
    *   **Critical Rules:**
        *   NO preamble, meta-commentary, or introduction.
        *   Start IMMEDIATELY with the first speaker label.
        *   Preserve COMPLETE content (no summarizing/condensing).
        *   Output length ~90-110% of input length.
        *   Preserve timestamps EXACTLY as they appear (one per speaker turn/paragraph block).
        *   Merge consecutive speech from the same speaker into paragraphs.
        *   Fix technical terms (capitalization, spelling).
        *   Fix proper names using the EXACT spellings from the provided list.
        *   Remove excessive filler words (um, uh, like, you know - but keep natural flow).
        *   Remove false starts/stammering and obvious repetitions.
        *   Preserve all substantive dialogue, technical explanations, questions, reactions.
    *   **Output Format:** `**[MM:SS] SPEAKER_XX:** First paragraph. [Blank line] Second paragraph (if natural break). [Blank line] **[MM:SS] SPEAKER_XX:** ...`

2.  **Analyze the Input Transcript:**
    *   **Speakers:**
        *   SPEAKER_00: Seems to be Redwan Meslen (identified later as "Redwan Meslen"). He talks about EA (Enterprise Ethereum Alliance), Sibos, Swift, CBDCs, etc.
        *   SPEAKER_01: Identified as "Bob Summerwill" later ("I'm Bob Summerwill..."). Talks about ConsenSys, EA history, Hyperledger, etc.
        *   SPEAKER_02: Identified as "Kieren James-Lubin" later ("Kieren James-Lubin"). Talks about Blockups, history of EA.
        *   SPEAKER_03: Identified as "Victor Wong" later ("Victor Wong"). Talks about Stratum, history of EA.
    *   **Content:** Discussion about streaming tools (Restream, StreamYard), history of the Enterprise Ethereum Alliance (EEA/EA), DevCon 2, Sibos, Swift, ISO 20022, Stablecoins vs CBDCs, Tokenization, RWA (Real World Assets), DTCC, future of institutional adoption, Fabric, Canton, Hyperledger.
    *   **Issues:** Typos ("Jane Jo" -> "J.P. Morgan"? No, "Jane Jo Live" sounds like "J.P. Morgan Live" or a specific event, but looking at context: "all of us for Jane Jo Live" - wait, "J.P. Morgan" is likely. Later "J.P. Morgan office" is mentioned. Actually, "Jane Jo Live" might be "Ethereum Live" or a mishearing. Wait, looking at text "all of us for Jane Jo Live in real life". It might be "J.P. Morgan". Let's check context. SPEAKER_01 says "Redwan Meslen... executive director of the EA". Then SPEAKER_02 says "Chairman James Lubin, CEO of Blockups." SPEAKER_03 is Victor Wong. SPEAKER_01 is Bob Summerwill.
    *   **Names to check against list:**
        *   Redwan Meslen -> Is he on the list? "Redwan Meslen" is NOT in the "Known People" list provided. The list has names like Aaron Davis, Adam B. Levine, etc. Wait, Redwan Meslen isn't there. However, the transcript says "Redwan Meslen". I should trust the transcript for names *not* in the list unless it's an obvious typo of a name *in* the list. Or maybe the list is just a sample of known people? The prompt says: "Known People (244): ... [List]". It seems to imply these are the valid names. Redwan Meslen is a real person (ED of EEA). The list provided might be incomplete or a sample. I will use the spelling from the transcript if it seems correct, or standard spelling if I know it. "Redwan Meslen" or "Redwan Mesli"? It's usually Redwan Mesli. The transcript says "Meslen". I should probably correct to "Mesli" if I'm an expert, but the prompt says "MUST use EXACT spellings from the 'Key People' list above". If he's not there, I should stick to what is likely correct or the transcript. However, looking at the list again: "Adam B. Levine, Adam B Levine". It has variations. It's a specific list. Wait, "Redwan Meslen" is not in the list. "Bob Summerwill" (Bob Summerwill) is not in the list. "Kieren James-Lubin" is not in the list. "Victor Wong" is not in the list.
        *   *Self-Correction*: The list provided in the prompt seems to be a *sample* of "Known People" and "Technical Terms" for context, but the transcript contains people not on that list (e.g., Redwan, Bob, Kieren, Victor). I cannot use the list to correct names if the names aren't there. I will assume the "Known People" list is for reference if those specific names appear (e.g., "Vitalik" is mentioned later).
        *   *Wait, let me re-read the list carefully.*
        *   The list ends with "...Aya Miyaguchi". It seems truncated or specific. It includes "Aaron Davis", "Aaron Wright", "Adam B. Levine"... but not the current speakers.
        *   The prompt says: "Known People (244): ... [List]". It implies the list is exhaustive or a reference.
        *   However, I am an "expert transcript editor". I should know the correct spellings for people like Redwan Mesli (usually Mesli, but transcript says Meslen. I will keep Meslen to be safe based on "PRESERVE COMPLETE CONTENT" and not altering names unless explicitly wrong or on the list. Actually, I will assume the transcript "Meslen" is the phonetic rendering. As an expert, I know it's Redwan Mesli. But the prompt says "MUST use EXACT spellings from the 'Key People' list above". If he's not on the list, I'll stick to the transcript or correct obvious errors? "Meslen" is likely "Mesli". I'll check the transcript again. "Redwan Meslen. Yes. Meslen". It's repeated. I will stick to "Meslen" to avoid guessing against the specific constraint of the list, although Mesli is the real name. Or, since I am an expert, I should probably fix it. But the constraint is strong. "MUST use EXACT spellings from the 'Key People' list". If he's not there, I won't invent a correction. I will fix the transcription errors of people ON the list (like Vitalik, Jeff Wilkie -> Wilcke).
    *   **Technical Terms:** EVM, L1, L2, CBDC, RWA, Swift, Sibos, ISO 20022, Hyperledger, Quorum, Fabric, Canton, Besu, Burrow, ErisDB, Monax, Tendermint, NFT, DAO, AMM, TPS, POC.

3.  **Detailed Editing Plan (Segment by Segment):**

    *   **[00:02] SPEAKER_00:** Mentions Restream, Twitter, YouTube, LinkedIn.
        *   Clean up "stream on Twitter, I think YouTube and LinkedIn" -> "streams on Twitter, YouTube, and LinkedIn at the same time."
    *   **[00:10] SPEAKER_03:** StreamYard mention.
    *   **[00:15] SPEAKER_01:** "screwing around with different tools" -> keep informal. "seems a bit... Not all perfect" -> "seems a bit better, or at least not all perfect." (interpretation of stutter).
    *   **[00:26] SPEAKER_00:** "this one looks pretty cool."
    *   **[00:31] SPEAKER_01:** "there must be good software for this, right? It's such a common need. Isn't there just an answer that just works?"
    *   **[00:39] SPEAKER_00:** "interoperability". "track you in." -> "track you in." "X especially." -> "X, especially." "On X, there isn't even a means to download the bloody audio." "Be able to own your data, you know, in all those platforms. Even own a query or just access..." -> "own a query, or just access to that data." "Google... tracking... what did you do that week?" -> "I can go in and say, what did you do that week?"
    *   **[01:31] SPEAKER_03:** "Yeah, exactly."
    *   **[01:33] SPEAKER_00:** "I find it quite, quite well. 501." -> This looks like a false start or random noise. "501" might be a room number or unrelated. I'll keep "I find it quite, quite well."
    *   **[01:39] SPEAKER_02:** "Oh, yeah."
    *   **[01:40] SPEAKER_03:** "No, no, no, I'm ready. No, but that was a good call-in show, right? So we have a very special guest today, but a special format because all of us for Jane Jo Live in real life."
        *   "Jane Jo Live" is likely "J.P. Morgan Live" or "Ethereum Live"? Later they mention "J.P. Morgan office". Let's look at "all of us for Jane Jo Live". It might be "all of us for J.P. Morgan Live". Or "all of us for [Event Name] Live". Given the context of "In the same room. In the same room. Amazing." and "special format", maybe it's "Zero Knowledge Live"? No. "Jane Jo" is phonetic. "J.P. Morgan" was mentioned earlier as a big player. Let's assume "J.P. Morgan Live" is the intended phrase, or keep it if unsure. However, "J.P. Morgan" fits the context of enterprise/banking later. But wait, "Jane Jo" is spoken twice. Could it be "Genoa Live"? "Ethereal Live"? Let's stick to the transcript or a minimal fix if obvious. Actually, looking at "Jane Jo", maybe it's "Gen Con"? No. "Ethereal"?
        *   Wait, "all of us for J.P. Morgan Live" makes sense if it's a conference. But they are in a room. Maybe it's "Ethereal JPM"? No.
        *   Let's look at "call-in show". Maybe "Jane Jo" is the name of the show? Or "J.P. Morgan"?
        *   Let's assume "J.P. Morgan Live" is the intended meaning but the transcript is poor. Or maybe "Jane Jo" is a person? No.
        *   Actually, maybe it's "all of us for 'Jingle' Live"? No.
        *   Let's look at the flow. They are introducing a guest, Redwan. They are all in the same room. "all of us for Jane Jo Live". Could it be "Gensler Live"? No.
        *   I will transcribe it as "J.P. Morgan Live" if I'm confident, otherwise leave it. Given "J.P. Morgan office" is mentioned later regarding the kickoff meeting. And "Santander". It seems to be a banking theme. I'll try "J.P. Morgan Live" or simply clean it to "all of us for this event live". No, I must preserve content. I'll keep "Jane Jo Live" if I can't be sure. *Correction*: "Jane Jo" -> "J.P. Morgan" is a stretch phonetically ("Jane Jo" vs "Jay Pee"). Maybe "Genzo"? "Ethereal"?
        *   Let's look at "Jane Jo". "Jay-En-Jay-Oh"? J.N.J.O.? "Ethereum" is often pronounced "Ether-ee-um". "Jane Jo" could be "Ethereal"?
        *   Actually, looking at the "Known People" list: "Aya Miyaguchi".
        *   Let's skip the name guess and just clean the text. "Jane Jo Live" is likely a specific proper noun I can't verify 100%. I'll leave it as "Jane Jo Live" or "Ethereal Live" if I want to risk it. Wait, "Jane Jo" sounds like "Zero Knowledge" (ZK)?? No.
        *   Let's look at the context: "special format because all of us for Jane Jo Live in real life." "In the same room."
        *   Maybe it's "Ethereal J.P."?
        *   Let's just fix the grammar around it. "special format because all of us are here for Jane Jo Live in real life."
    *   **[01:57] SPEAKER_01:** "In the same room. In the same room. Amazing."
    *   **[02:00] SPEAKER_03:** "And you are a special guest. Do you want to show?"
    *   **[02:03] SPEAKER_01:** Introduces Redwan Meslen (Executive Director of EA/Enterprise Ethereum Alliance). "Healthy run."
    *   **[02:22] SPEAKER_00:** "Yes, exactly."
    *   **[02:23] SPEAKER_01:** "It's eight years now. Since 2017, yeah. February 2017 was the launch date on the 28th."
    *   **[02:31] SPEAKER_02:** "There was pre-work solidly before, at least three months, maybe more."
    *   **[02:34] SPEAKER_01:** "DevCon 2... Shanghai, October."
    *   **[02:57] SPEAKER_02:** "kickoff meeting at the J.P. Morgan office... closed-door meetings at Microsoft."
    *   **[03:07] SPEAKER_01:** "public launch was February... internal one in December."
    *   **[03:16] SPEAKER_03:** "initial contacts... DevCon 2... group of people... Starbucks... idea formation."
        *   "january 2017 but but yeah like a lot of those initial contacts..." -> "January 2017, but yeah, a lot of those initial contacts..."
    *   **[03:58] SPEAKER_01:** "Matt spoke of NewCo held a little bar side event..." -> "Matt Spoke, of NewCo, held a little bar side event..."
    *   **[04:15] SPEAKER_03:** Technical issue. "push James to tell everybody to go to YouTube." "messed up the Twitter."
    *   **[04:33] SPEAKER_02:** "Space is at 5 a.m."
    *   **[04:36] SPEAKER_01:** "Right." "Yes." (Short confirmations).
    *   **[04:35] SPEAKER_02:** "Yes."
    *   **[04:36] SPEAKER_01:** "But yeah, Matt Spoke... bar upstairs... technical issues." -> Wait, the transcript cuts off and repeats "technical issues" later? No, SPEAKER_03 interrupts.
    *   **[04:45] SPEAKER_03:** "I didn't go to that one... fix this right now on Twitter."
    *   **[05:02] SPEAKER_01:** "If not, I am."
    *   **[05:06] SPEAKER_03:** "I did choose a..."
    *   **[05:08] SPEAKER_01:** "parallel... enterprise Slack set up... Vitalik... dumped the ball in a Slack and ran away."
        *   "Nuka was part of that luca was part of that" -> "Nuka [maybe Nukash?] was part of that, Luca [Luca Prosperi?] was part of that."
        *   "i'm boxing will so i'm head of ecosystem at Stratum Cut." -> "I'm Bob Summerwill. I'm head of ecosystem at Stratum [Stratum? Or 'Ethereum' sounds like Stratum? No, Stratum is a company?]. Later SPEAKER_02 says "Blockups". SPEAKER_03 says "Stratum Recon". Ah, "Blockups" created "Stratum Recon". Wait. SPEAKER_02: "James Lubin, CEO of Blockups. Victor Wong. Creators of Stratum Recon."
        *   SPEAKER_01: "I'm Bob Summerwill... head of ecosystem at Stratum [something]." Transcript says "Stratum Cut". Maybe "Stratum One"? Or "Summerwill" was misheard as "boxing will"?
        *   "boxing will" -> "Bob Summerwill".
        *   "Stratum Cut" -> maybe "Summerwill"? No, he says "head of ecosystem at Stratum..." The transcript says "Stratum Cut". Maybe "Stratum One"? "Stratum One"? Or is he at "Ethereum Foundation" (former)?
        *   Later SPEAKER_03 introduces himself as Victor Wong from Blockups.
        *   Let's look at the company. "Stratum Recon". "Blockups". SPEAKER_01 is Bob Summerwill. Is he at Stratum? Or EEA? He says "head of ecosystem at Stratum Cut". Maybe "Stratis"? Or "Summerwill" works for "Summerwill"?
        *   Actually, Bob Summerwill is the Executive Director of EEA in real life. Wait, SPEAKER_00 is Redwan Meslen, introduced as ED of EA.
        *   Maybe SPEAKER_01 (Bob) is at "Stratis"? "Stratum"? Let's stick to "Stratum Cut" if unsure, or correct to "Summerwill" for the name.
        *   "boxing will" -> "Bob Summerwill".
        *   "Stratum Cut" -> Maybe "Stratis"? Or "Summerwill" was misheard as "boxing will" and he said "I'm Bob Summerwill, head of ecosystem at..."? The transcript has "boxing will so i'm head of ecosystem at Stratum Cut". It's very garbled.
        *   Let's check the "Known People" list. Bob Summerwill is NOT on it.
        *   However, I know Bob Summerwill is the ED of EEA. But here SPEAKER_00 is Redwan Meslen, the ED of EEA.
        *   Maybe SPEAKER_01 is just a guest.
        *   Let's fix the name to "Bob Summerwill" (as he introduces himself later: "I'm on Twitter. Same as my name, Bob at Summerville...").
        *   "Stratum Cut" -> "Stratum One"? Or "Summerwill"?
        *   Actually, in the intro [05:56], he says "boxing will". Later [49:22] he says "Bob at Summerville".
        *   In [05:56], the text is "boxing will so i'm head of ecosystem at Stratum Cut". Maybe "Summerwill" is the name. And "Stratum Cut" is the company. Or maybe "Stratis"?
        *   I'll assume "Bob Summerwill" for the name. I'll try to fix "Stratum Cut" to something plausible or leave if unsure. "Stratum" is mentioned later ("Stratum Recon"). Maybe "Stratum" is the company.
    *   **[05:56] SPEAKER_02:** "Chairman James Lubin, CEO of Blockups. Victor Wong. Creators of Stratum Recon."
        *   "Blockups" -> "BlockApps"? "Blockups" sounds like "BlockApps".
        *   "James Lubin" -> "Kieren James-Lubin" (based on the "Known People" list having "Kieren James-Lubin" or "James Lubin"? The list has "Kieren James-Lubin"). But here he says "Chairman James Lubin". I will use "Kieren James-Lubin" if the prompt allows, but "James Lubin" is what he says. I'll stick to "James Lubin" or "Kieren James-Lubin". The prompt says "MUST use EXACT spellings from the 'Key People' list above". The list has "Kieren James-Lubin". But the speaker introduces himself as "Chairman James Lubin". I will fix to "Kieren James-Lubin" based on the expert knowledge and the list, or stick to the transcript "James Lubin" if it's a self-intro. Usually, transcripts should reflect what is said, but the prompt says "MUST use EXACT spellings...". I'll use "Kieren James-Lubin".
        *   "Blockups" -> "BlockApps" (likely).
        *   "Stratum Recon" -> "Strato Recon"? "Stratum" seems to be the name used here.
        *   Let's check [49:26] "K. James Lubin".
    *   **[06:01] SPEAKER_03:** "Victor Wong, Chief Product Officer of Blockups."
    *   **[06:04] SPEAKER_02:** "That's it. Sorry, back. But yeah, Amos as well. Do you remember that? Yeah. Taiwan. Taiwan. We should check in on. I haven't thought of Amos until, in like several years until the moment."
    *   **[06:16] SPEAKER_01:** "Taiwan bank consortium thing. Chinese cryptography. Master chain... Russia... spare bank thing."
        *   "Master chain" -> "Masterchain".
    *   **[06:42] SPEAKER_00:** "I use Restream... I'm not at the year at that time" -> "I wasn't there at the time". "EA was created like eight years ago?"
        *   "year" -> "there".
        *   "healthy run" -> "pretty big event".
        *   "hopes... atmosphere".
    *   **[07:13] SPEAKER_01:** "ConsenSys were very critical... load of enterprise engagement... momentum... really, really quick."
    *   **[07:48] SPEAKER_02:** "DevCon 2... innovation lab level... forking their own flavor of Ethereum... hacked their own consensus algorithms... Many guests. Many guests, indeed. We learned later that, like... like a lot of JP Morgan's forum was initially built by Jeff Wilkie."
        *   "forum" -> "Quorum" (likely, or "platform"?). Jeff Wilcke built a lot of early stuff. "JP Morgan's Quorum". The transcript says "forum". I will correct to "Quorum".
        *   "Jeff Wilkie" -> "Jeff Wilcke" (on the list? No, but known person. Correct spelling is Wilcke).
    *   **[08:19] SPEAKER_01:** "He had like some kind of... not announced... behind the scenes... Quorum started. ErisDB that became Monax, that became Hyperledger Burrow... permissioned Ethereum client off POC5 pre-mainnet... Tendermint onto an EVF [EVM]."
        *   "smished apart" -> "splintered apart"? "smished" -> "mushed together"? "smashed apart"?
        *   "EVF" -> "EVM".
        *   "ErisDB... Monax... Hyperledger Burrow".
    *   **[09:07] SPEAKER_02:** "Us too. We had our own client... consensus consulting engagements... tuning it for enterprise... standard for all of this new stuff... above and beyond the base standard."
    *   **[09:30] SPEAKER_03:** "even beyond that. technical work... silo... bolting on these things... private everyone... marriage between..."
        *   "private everyone" -> "private Ethereum".
    *   **[10:11] SPEAKER_01:** "customers of these things and builders... vendor locked... Quorum... collaboratively do code bases... Hyperledger... C plus plus relicensing... Apache 2... Hyperledger... EA was kind of a backup... fusion... Commoditize any difference among the startups... vendor locked... IBM nightmares, Oracle nightmares... not going to live through this."
        *   "fucked up" -> "fell apart"? "messed up"? The transcript says "that fucked up". It might be an expletive or "that forked up". I'll clean to "that fell apart" or keep it if it fits the "authentic speaking patterns". "fucked up" is authentic. I'll keep "fucked up" or change to "messed up" if it feels too harsh, but the prompt says "Preserve Natural conversation flow". I'll leave it or use a dash if it's a filler. Actually "that fucked up" sounds like "that didn't work out". I'll stick to the transcript but maybe soften if it's a transcript error for "forked up". "Forked up" makes sense in context. I will use "forked up" or "fell apart".
        *   "commoditize any difference among the startups... existence... vendor locked again... horrific IBM nightmares, Oracle nightmares".
    *   **[12:10] SPEAKER_00:** "Market pressure... Corda coming out, IBM launching Fabric... Nominally open source, but quite proprietary... February 2017... get our shit together... Ethereum product... hope against IBM and R3."
    *   **[12:40] SPEAKER_02:** "EA at that time... call with 300 people... selling into big banks... Ethereum just survived... not paying any attention... competition came in."
    *   **[13:08] SPEAKER_03:** "Parallel thing... DEVCON event... enterprise use cases... Santander... US dollar on chain... stable coin."
    *   **[13:31] SPEAKER_00:** "Very cool parallel... innovation labs... implementing blockchain... executive team... production... get it to market."
    *   **[14:16] SPEAKER_02:** "Thankfully, like they're scared now."
    *   **[14:18] SPEAKER_00:** "move or out... interesting talk... Sibos... Swift conference."
    *   **[14:28] SPEAKER_03:** "ShredFi institutional players... communication... digital asset tokenization... hot topic."
    *   **[14:55] SPEAKER_00:** "less regulatory... Sibos... Swift... messaging system... 11,000 financial institutions... co-op... DAO for Trash Buy [??]... Kudos to Danielle from ConsenSys... DAO."
        *   "DAO for Trash Buy" -> "DAO for Trash Buy"? "DAO for Swift"? "DAO for the banks"?
        *   "Trash Buy" -> "Swiss buy"? "Sibos"? It says "DAO for Trash Buy". Probably "DAO for the banks" or "DAO for the members". "Trash Buy" is nonsense. Maybe "S.W.I.F.T."? "Swift"? Or "Trade Bank"?
        *   "It's a doubt." -> "It's a DAO."
    *   **[15:26] SPEAKER_02:** "can we buy in now? token is having probably a bank license... London Metal Exchange... buy a bunch of shares... annual fee... put someone there."
    *   **[15:49] SPEAKER_01:** "join the trade guild."
    *   **[15:51] SPEAKER_00:** "make-out of payments... global financial institutions... clearing house, settlements... Work Leader [??]... big financial institutions."
        *   "Work Leader" -> "World Bank"? "Clearstream"? "Euroclear"?
    *   **[16:54] SPEAKER_02:** "finance gets cleared through messaging... crypto people... transaction... not really like this."
    *   **[17:06] SPEAKER_00:** "key point... delivery versus payment... complex... receive message, send another... atomic transaction... submit... executed... delivered... give you the can... dense... move here... send the money... efficiencies... t plus one... t plus two... second to less than that... swift"
        *   "give you the can" -> "give you the token"? Or "give you the cash"? "Can" is weird. Maybe "give you the coin"? "give you the can" -> "give you the can" implies moving a physical object. I'll keep "give you the can" or fix to "give you the cash" if context suggests money. "I give you the can, well I know you've been giving me, like, the money".
        *   "Work Leader" -> Maybe "Clearstream"?
    *   **[18:21] SPEAKER_02:** "Swift is a payments mechanism? No, it's not a message... interject... FX... USD... Euro... trade... pair... send my side... Swift checks... matched... charges $7... matched."
        *   "Swift offer type of envelope... format of envelope... paper and ink... corresponding banking... take their share."
        *   "moving the asset... USD on my bank list... Euro on your bank list... talking to each other... compliance... bunch of local jurisdiction-specific handshakes."
    *   **[19:54] SPEAKER_01:** "Yeah, it's like a lot of different handshakes."
    *   **[20:00] SPEAKER_03:** "tracking the transfers... no money actually moving... list of IOUs... send $100 to you in France... I go to my bank, I put in $100... The money doesn't"
    *   **[20:27] SPEAKER_00:** "go anywhere... my debate... write the usd off the net... rtgs... different messaging... deep dive... huge dance... money in your bank account... central bank money... deposit money... M0, M1, M2... complex... payment... securities... financial instruments... blockchain... stablecoin... CBDCs."
        *   "my debate" -> "the bank ledger"? "the day"? "RTGS" (Real Time Gross Settlement).
    *   **[21:26] SPEAKER_03:** "Yeah, yeah, yeah."
    *   **[21:27] SPEAKER_00:** "misconception... stablecoin and CBDCs... exactly the same thing... different context... CBDC is a stablecoin for a central bank... issuer is not the same... money of banks... technical level... copy-paste of the same contract mechanism... whole different language... terminology... CB