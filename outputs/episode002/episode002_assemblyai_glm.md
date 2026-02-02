**Plan:**

1.  **Analyze the Request:**
    *   **Role:** Expert transcript editor specializing in Ethereum and blockchain.
    *   **Input:** Raw transcript of a podcast/video discussion about the early days of Ethereum (post-launch, hackathons, Microsoft partnership, DAO, Devcon 1 & 2, EEA).
    *   **Context:** Known People list, Technical Terms list provided.
    *   **Objective:** Create a clean, readable transcript preserving *all* dialogue and content.
    *   **Constraints:**
        *   NO preamble, intro, or meta-commentary.
        *   Start immediately with `[MM:SS] SPEAKER_XX:`.
        *   Output length ~90-110% of input.
        *   Preserve timestamps EXACTLY as they appear in the input.
        *   Merge consecutive speech from one speaker into paragraphs.
        *   Fix spellings/capitalization (names, technical terms).
        *   Fix punctuation/sentence structure.
        *   Remove excessive filler words, false starts, obvious repetitions.
        *   PRESERVE all substantive content, technical details, anecdotes.

2.  **Input Analysis:**
    *   **Speakers:** SPEAKER_00 (Kieren James-Lubin - CEO BlockApps), SPEAKER_01 (Victor Wong - CPO BlockApps), SPEAKER_02 (Jim/James Hermos - CTO BlockApps). Note: The speaker identifies himself as "KIERAN James Lubin" in the text, but the context list says "Kieren James-Lubin". I should use the spelling from the context list "Kieren" if the speaker says it, but here he says "KIERAN". I will leave his self-introduction as spoken "KIERAN" but keep standard Ethereum terms consistent.
    *   **Timestamps:** Present in the input (e.g., `[00:01]`). I must keep them exactly.
    *   **Key Names to Check:**
        *   Kieren James-Lubin (Input says KIERAN James Lubin).
        *   Victor Wong.
        *   James Hermos / Jim.
        *   ConsenSys (Input says Consensus).
        *   Andrew Keys.
        *   Vitalik (Not in Known People list explicitly, but obvious. List has "Aya Miyaguchi" etc. Wait, "Vitalik" is *not* in the Known People list provided in the prompt context? That's odd for an Ethereum context, but I must stick to the provided list for spelling rules. The list has 244 names. I'll check it. Ah, the list provided in the prompt is truncated or specific. It lists "Aaron Davis" to "Aya Miyaguchi". It does *not* list Vitalik. However, standard capitalization applies. I will assume standard spelling for names not explicitly in the list if they are widely known, but strictly follow the list for those present. Wait, the prompt says "Known People (244): ...". It seems I have a partial list or the user provided a sample list. I will use standard spellings for names like Vitalik, Joey Krug, Jack Peterson, Jeremy Gardner, Matt Liston, Marley Gray, John Wolpert, Matt Spoke, Jeremy Miller, Tyler Smith.
        *   *Correction*: The list provided seems to be a subset (A-A). I will proceed with standard capitalization for names not in the provided fragment, and standard technical terms.
    *   **Key Terms to Check:**
        *   Ethereum (input has Ethereum).
        *   dapps vs dapps (Decentralized apps).
        *   Ether vs ETH (Input uses both, will keep context-appropriate).
        *   Dappathon.
        *   Consensus vs ConsenSys. The speaker keeps saying "Consensus" referring to the company ConsenSys. The prompt list includes "ConsenSys". In the transcript, the speakers say "Consensus". I should probably correct this to "ConsenSys" if they are referring to the company, or keep it if they mean general consensus, but here they mean the company. I will correct "Consensus office" to "ConsenSys office" if the context clearly indicates the company, but the speakers consistently say "Consensus". I will stick to the transcript's speech pattern but maybe capitalize it properly as a proper noun if it refers to the company, or keep as "ConsenSys" if it's clearly the entity. Actually, looking at the text: "the first consensus office", "Consensus at this point". They are referring to ConsenSys. I will correct to ConsenSys for accuracy as per the "expert editor" persona, or at least capitalize "Consensus" if they insist on saying it that way, but the prompt list has "ConsenSys". I will change "consensus" (the company) to "ConsenSys" to match the technical term list provided.
        *   "ethercap" -> "Ether.Camp" (likely).
        *   "gamefi" -> "GameFi".
        *   "Truther" -> "TruthCoin" or "Trucoin"? Speaker says "Truther or something. Some. Something like that." and later mentions "Truthcoin". The project was likely Truthcoin or similar. I'll leave as "Truther" if he's guessing, but capitalize.
        *   "Crypto castle".
        *   "Crypto Economicon".
        *   "Augur".
        *   "Poloniex" -> "Poloniex" (Speaker says "Poloniac", will correct).
        *   "Devcon" -> "Devcon" (Input says "DEFCON 1" which is a hacking conference, Devcon is the Ethereum conference. The text says "DEFCON 1" but context is "launching Blockchain as a service" and "Devcon 1". Speaker says "That conference, DEFCON 1" regarding Microsoft handing out passes. It seems he means Devcon. Later he says "Devcon 1" correctly. I will correct "DEFCON 1" to "Devcon 1" where contextually appropriate, as DEFCON is a security conference, Devcon is the Ethereum developer conference. Wait, he says "That conference, DEFCON 1" after discussing the Microsoft launch. I will assume he means Devcon 1 and correct it for clarity, or if he implies the *hacker* conference, keep it? Context: "It was that conference, DEFCON 1. Yeah, they were handing it out and that's why they wanted to make sure we were on their marketplace." Devcon 1 was in London. The Microsoft announcement was at Devcon 1. It is definitely Devcon. I will correct "DEFCON 1" to "Devcon 1".
        *   "Dencun" (in list) - not mentioned in text.
        *   "Slocket" -> "Slock.it".
        *   "The DAO".
        *   "BVVA" -> "BBVA" (Spanish bank).
        *   "Hyperledger".
        *   "EAA" -> "EEA" (Enterprise Ethereum Alliance).
        *   "BHP Billiton".
        *   "Quorum".

3.  **Editing Process (Section by Section):**

    *   **[00:01] SPEAKER_00:**
        *   Speaker: "KIERAN James Lubin". (Context list says Kieren. I will fix to Kieren).
        *   "BlockApps".
        *   "co founders, Victor".
        *   Clean up fillers ("you know", "um", "like" where excessive).

    *   **[00:48] SPEAKER_01:**
        *   Intro Victor Wong.
        *   Clean up.

    *   **[00:54] SPEAKER_02:**
        *   Intro James Hermos (or Jim).

    *   **[01:02] SPEAKER_00:**
        *   Discussion on where they left off (Ethereum launch).
        *   Handing to Victor for Dappathon.

    *   **[01:38] SPEAKER_01:**
        *   First consensus Dappathon. Correct "Consensus" to "ConsenSys" (the company) where appropriate.
        *   "Greenpoint", "Green desks" -> "Green Desk".
        *   "Domino park".

    *   **[02:12] SPEAKER_00:**
        *   "Green desks, maybe green ducks." -> "Green Desk".
        *   Domino park history.

    *   **[02:21] SPEAKER_01:**
        *   Agreement.

    *   **[02:22] SPEAKER_02:**
        *   Location details.

    *   **[02:27] SPEAKER_00:**
        *   Park details.

    *   **[02:40] SPEAKER_02:**
        *   Park construction.

    *   **[02:53] SPEAKER_01:**
        *   Event details. Interns. ConsenSys size (20 people).
        *   Difficulty building dapps (reading variables).

    *   **[04:59] SPEAKER_00:**
        *   Clarification on which Dappathon (second one).
        *   Office move to Bushwick.
        *   "Horse Lineage app". "Truther".
        *   Air conditioning issues.

    *   **[05:59] SPEAKER_01:**
        *   Air conditioning story. Move to new space.
        *   Furniture assembly.

    *   **[06:30] SPEAKER_00:**
        *   Air conditioning memory.

    *   **[06:32] SPEAKER_01:**
        *   Frantic AC setup.

    *   **[06:44] SPEAKER_00:**
        *   "Scrappy days".

    *   **[06:46] SPEAKER_01:**
        *   Furniture assembly as startup proxy.

    *   **[07:09] SPEAKER_00:**
        *   Date of hackathon vs launch.

    *   **[07:15] SPEAKER_01:**
        *   Uncertain launch dates. Synchronizing. Arbitrarily choosing date.

    *   **[07:55] SPEAKER_00:**
        *   Asking Jim about launch prediction and mechanism.

    *   **[08:13] SPEAKER_02:**
        *   Git commits plot. Slack discussion.

    *   **[08:22] SPEAKER_00:**
        *   Git commits plot. How first block clock was set.

    *   **[08:44] SPEAKER_02:**
        *   Slack history.

    *   **[08:54] SPEAKER_00:**
        *   Slack treasure trove.

    *   **[09:32] SPEAKER_01:**
        *   "Jim."

    *   **[09:33] SPEAKER_02:**
        *   Presale ether expectations. Price disappointment (20 cents). "Flop".

    *   **[09:58] SPEAKER_00:**
        *   Expectations. "Day one dapps". "Land grab". Price action.
        *   First ICO (Augur). Pre-sale ether vs Bitcoin.
        *   Crypto Economicon conference.
        *   Meeting Augur guys (Jeremy Gardner, Joey Krug, Jack Peterson).
        *   Crypto castle.

    *   **[12:59] SPEAKER_01:**
        *   Crypto castle imagery.

    *   **[13:09] SPEAKER_00:**
        *   Description of Crypto castle.
        *   Vitalik staying there.
        *   Assassination markets on Wikipedia entry.

    *   **[15:17] SPEAKER_01:**
        *   "Of".

    *   **[15:20] SPEAKER_00:**
        *   Truthcoin meeting. Math/theoretical properties.

    *   **[16:06] SPEAKER_01:**
        *   Day one dap goal.

    *   **[16:15] SPEAKER_00:**
        *   Augur live date vs crowd sale.

    *   **[16:19] SPEAKER_01:**
        *   "Right, right, yeah."

    *   **[16:24] SPEAKER_00:**
        *   Transition to Devcon 1.
        *   ConsenSys BD team. Enterprise interest. Microsoft.
        *   "Ethercap" -> Likely "Ether.Camp".
        *   Java client.

    *   **[18:33] SPEAKER_01:**
        *   Microsoft interest. Java client vs Haskell.
        *   Devcon 1 almost didn't happen (money issues).
        *   Andrew Keys.
        *   Microsoft launch opportunity (Blockchain as a Service).
        *   Java guys faded.
        *   Difficulty getting Ether -> Private Ethereum.

    *   **[21:31] SPEAKER_00:**
        *   Coinbase listing date (May 2016). Kraken.
        *   Poloniex chat (troll box). Circle bought it.

    *   **[21:48] SPEAKER_01:**
        *   Poloniex chat (pre-Discord).

    *   **[21:54] SPEAKER_00:**
        *   Poloniex status. Sketchy exchanges. Difficulty getting Ether.

    *   **[22:33] SPEAKER_02:**
        *   Java client situation. Microsoft mad?
        *   Jim: "No, you're not... they were mad."

    *   **[22:49] SPEAKER_01:**
        *   Microsoft wanted Java. BlockApps worked hard. Internal mantra: "Write a DAP in 30 seconds".

    *   **[23:23] SPEAKER_02:**
        *   Pre-announcement. Java guys disappeared.

    *   **[23:28] SPEAKER_01:**
        *   BlockApps was the runner up/backup.

    *   **[23:50] SPEAKER_02:**
        *   Microsoft internal tension (Azure vs Blockchain). Marley Gray, KO Teeter.

    *   **[24:15] SPEAKER_01:**
        *   Microsoft NY office visits.

    *   **[24:46] SPEAKER_00:**
        *   Azure vs AWS. Azure launch dates (2010 is wrong for Azure? Speaker says 2010. I'll leave it. Azure was 2010 actually. AWS 2006).

    *   **[25:04] SPEAKER_02:**
        *   Free passes at conference.

    *   **[25:11] SPEAKER_01:**
        *   Devcon 1. Microsoft marketplace strategy.

    *   **[25:41] SPEAKER_02:**
        *   Free passes -> paid customers later.

    *   **[25:51] SPEAKER_01:**
        *   Price spike after announcement.

    *   **[26:05] SPEAKER_00:**
        *   Price (ETH or MSFT stock)? Both ticked up.

    *   **[26:10] SPEAKER_01:**
        *   ETH price spike.

    *   **[26:15] SPEAKER_00:**
        *   MSFT stock price memory.

    *   **[26:19] SPEAKER_01:**
        *   MSFT stock up.

    *   **[26:23] SPEAKER_02:**
        *   ETH from 20c to 30c.

    *   **[26:32] SPEAKER_01:**
        *   ETH $1 to $1.80.

    *   **[26:40] SPEAKER_00:**
        *   Devcon timeframe (December). Price around $1.
        *   Calls after announcement.

    *   **[27:02] SPEAKER_01:**
        *   Agreement.

    *   **[27:04] SPEAKER_00:**
        *   Enterprise customers. Vic took calls.

    *   **[28:01] SPEAKER_01:**
        *   Phone calls. Companies struggling to build before. Now able to build.

    *   **[28:59] SPEAKER_00:**
        *   Slock.it project at Devcon 1.
        *   Relation to The DAO.

    *   **[29:26] SPEAKER_01:**
        *   Slock.it weird. DAO concept. Slock.it people realized DAO was more important.

    *   **[30:04] SPEAKER_00:**
        *   What was The DAO?

    *   **[30:15] SPEAKER_01:**
        *   Investment fund. Locked up huge % of ETH supply (14-25%).

    *   **[30:50] SPEAKER_00:**
        *   Wikipedia check. Crowd sale amounts ($34m, $50m, $100m, $150m).
        *   Virality. Collaboration. Pooling capital.

    *   **[32:27] SPEAKER_01:**
        *   Agreement.

    *   **[32:27] SPEAKER_00:**
        *   Meeting with BBVA (Scarlet and Carlos). Operational use cases vs Future. Cautionary tale.
        *   Hack discovered. Recounting the event.

    *   **[33:41] SPEAKER_01:**
        *   The hack. Race between attacker and DAO creators.
        *   Immutable contract flaw.
        *   Funds pulled but transparent and stuck.

    *   **[34:26] SPEAKER_00:**
        *   Agreement.

    *   **[34:26] SPEAKER_01:**
        *   Funds stolen and left on the street.

    *   **[34:54] SPEAKER_00:**
        *   Hard fork debate. Immutability vs Refund.
        *   Jim coding the fork.
        *   Ethereum Classic.

    *   **[35:47] SPEAKER_01:**
        *   "In".

    *   **[35:47] SPEAKER_00:**
        *   Bitcoin forks. Barry Silbert.
        *   Ethereum Classic later hard fork (PoS switch mentioned, but specific fork mentioned later).

    *   **[37:40] SPEAKER_01:**
        *   "No, no."

    *   **[37:43] SPEAKER_00:**
        *   ETC hard fork controversy. Bob Summerwill (corrected from Summarial if needed, speaker says Summarial, list says Summerwill. I will use Summerwill if I'm correcting, or keep Summarial if it's a phonetic attempt? Prompt says "Bob Sumersall" -> "Bob Summerwill". Speaker says "Bob Summarial". I will correct to Bob Summerwill).
        *   Tax treatment of forks.

    *   **[38:45] SPEAKER_01:**
        *   "Yeah."

    *   **[38:45] SPEAKER_00:**
        *   Mining ETC vs ETH.
        *   Cointelegraph article on ETC hard fork.
        *   Tax comments.

    *   **[40:28] SPEAKER_01:**
        *   Current price comparison ($30 billion equivalent).

    *   **[40:44] SPEAKER_00:**
        *   Agreement. Second CoinDesk Consensus Hackathon.

    *   **[41:02] SPEAKER_01:**
        *   Hackathon details. CoinDesk Consensus event (Times Square).
        *   Microsoft (hackathon) -> Ritz (conference).
        *   Hyperledger.
        *   BlockApps room crowded. Co-opted another room.
        *   Winner (built before hackathon).

    *   **[43:18] SPEAKER_00:**
        *   Joke about losing/cheating.

    *   **[43:22] SPEAKER_01:**
        *   Subjective memory.

    *   **[43:27] SPEAKER_00:**
        *   Rest of the conference.

    *   **[43:39] SPEAKER_01:**
        *   First "shiny" conference.
        *   Vitalik speaking. Hyperledger app launch.
        *   Meeting with John Wolpert (Hyperledger) and Vitalik.
        *   "Muscle shirt" incident.

    *   **[45:32] SPEAKER_00:**
        *   Vitalik vs Wolpert size comparison.
        *   John Wolpert later joined ConsenSys. IBM Linux analogy.

    *   **[47:57] SPEAKER_01:**
        *   Picture from hackathon.

    *   **[48:15] SPEAKER_00:**
        *   "Yep."

    *   **[48:18] SPEAKER_01:**
        *   Picture description.

    *   **[48:30] SPEAKER_00:**
        *   Moving on. Devcon 2 (Shanghai, Sept 2016).
        *   Visa stuff. Raising seed money.
        *   Impressions?

    *   **[49:46] SPEAKER_02:**
        *   Big attack on Ethereum. Morning of. Digging in with Haskell client.

    *   **[50:07] SPEAKER_01:**
        *   "So I do remember..."

    *   **[50:10] SPEAKER_00:**
        *   Transactions slowing clients. Data structure issues.

    *   **[50:35] SPEAKER_02:**
        *   EAA (EEA) formed. Vic had meetings, Jim coded.
        *   Vic: "We just formed the EEA."

    *   **[51:09] SPEAKER_01:**
        *   Jeremy Miller drove it. Matt Spoke previous attempt (Deloitte).
        *   Deloitte early in blockchain (Toronto).

    *   **[51:32] SPEAKER_00:**
        *   No memory of Spoke attempt. Spoke at Deloitte.

    *   **[51:46] SPEAKER_01:**
        *   Deloitte/Spoke consortium.
        *   BlockApps/Microsoft organic work.
        *   Coffee shop meeting (Starbucks). Jeremy, John Wolpert (Santander? No, Wolpert was IBM/Consensys later? Speaker says Wolpert was there from Santander. Wait, Wolpert worked for IBM. Maybe he meant someone else from Santander. Actually, speaker says "John Woolpert [sic] and Vitalik... John Wheeling [sic] was there from Santander". I will correct spelling to Wolpert. James Lazarus.
        *   Formation of EEA.

    *   **[53:30] SPEAKER_00:**
        *   Shanghai details. "Aliens" (foreigners) registration.
        *   Flight to hotel. Old stock exchange hotel.

    *   **[54:39] SPEAKER_01:**
        *   Downtown location. The Bund. Pudong.
        *   Registration rules. Chinese breakfast.

    *   **[55:42] SPEAKER_00:**
        *   Hole in the wall food.

    *   **[55:45] SPEAKER_01:**
        *   Food algorithm. WSJ quote about China blockchain market.

    *   **[56:29] SPEAKER_00:**
        *   BHP Billiton project announcement. Tyler Smith.
        *   Fabric market suits. Algorithm: follow locals.

    *   **[57:26] SPEAKER_01:**
        *   Suits. Taxi driver food algorithm.

    *   **[58:08] SPEAKER_00:**
        *   Tyler Smith travel stories (silk blankets).
        *   High speed rail.

    *   **[58:56] SPEAKER_01:**
        *   Train travel improvements. Global feel.

    *   **[59:30] SPEAKER_00:**
        *   Business development in China.
        *   EEA launch lead-up.
        *   Starbucks napkin idea.
        *   "Every innovation lab is using Ethereum."
        *   JP Morgan mention.

    *   **[01:01:55] SPEAKER_01:**
        *   Structuring meetings. Small to 40 people.
        *   Membership fees? Tech vs Company side.
        *   Launch early 2017. Logo wall.

    *   **[01:03:26] SPEAKER_00:**
        *   EEA launch details. JP Morgan office Brooklyn.
        *   Quorum announcement date?

    *   **[01:04:14] SPEAKER_01:**
        *   Quorum timing. Go Ethereum client. Privacy. Haskell team at JP Morgan.

    *   **[01:04:41] SPEAKER_00:**
        *   Demo at launch? 2/2017?
        *   Quorum description (privacy, messaging, no token).
        *   EEA membership peak (100-500?).
        *   End of the beginning. Price trend (Feb 2017 upwards).
        *   Flippening (ETH vs BTC market cap). Litecoin #2. XRP #3.

    *   **[01:06:46] SPEAKER_01:**
        *   "Also".

    *   **[01:06:48] SPEAKER_00:**
        *   Closing thoughts on survivorship bias and coordinated effort.

    *   **[01:09:06] SPEAKER_01:**
        *   Success not predetermined. Contributions of many.

    *   **[01:09:33] SPEAKER_00:**
        *   Tossed in a wave vs willing reality.

    *   **[01:09:41] SPEAKER_02:**
        *   Not just hot air. Live tech.

    *   **[01:09:46] SPEAKER_01:**
        *   "So."

    *   **[01:09:46] SPEAKER_00:**
        *   Closing. Thanks listeners. Future series/guests.

    *   **[01:11:11] SPEAKER_01:**
        *   Thanks.

    *   **[01:11:13] SPEAKER_02:**
        *   Thank you.

4.  **Refining the Text:**
    *   *Self-Correction on Names:*
        *   "KIERAN" -> "Kieren" (per context list).
        *   "Consensus" (company) -> "ConsenSys" (per context list).
        *   "Ethercap" -> "Ether.Camp" (historical context).
        *   "Slocket" -> "Slock.it".
        *   "Poloniac" -> "Poloniex".
        *   "DEFCON 1" -> "Devcon 1" (Context: Ethereum conference).
        *   "BVVA" -> "BBVA".
        *   "Woolpert" -> "Wolpert".
        *   "Bob Summarial" -> "Bob Summerwill".
        *   "Marley Gray" / "KO Teeter" -> Keep.
        *   "Matt Spoke" -> Keep.
        *   "Jeremy Miller" -> Keep.
        *   "James Lazarus" -> Keep.
        *   "Tyler Smith" -> Keep.
    *   *Filler Removal:* Remove "um", "uh", excessive "like", "you know" where it disrupts flow.
    *   *Formatting:* Ensure bold timestamps and speaker labels. Merge paragraphs.

5.  **Final Review against Constraints:**
    *   No preamble? Yes.
    *   Start with `[00:01] SPEAKER_00:`? Yes.
    *   Same length? Yes, I will be careful not to cut content.
    *   Timestamps preserved? Yes.
    *   Merged paragraphs? Yes.
    *   Spelling corrected? Yes.

**(Self-Correction during drafting):**
*   Input: "The first consensus Dapathon" -> "The first ConsenSys Dappathon".
*   Input: "Ethercap" -> The speaker says "Ethercap". I will correct to "Ether.Camp" as it is the correct name of the Java client from that era, assuming the ASR heard "cap".
*   Input: "green desks, maybe green ducks" -> "Green Desk".
*   Input: "Crypto Economicon" -> "Crypto Economicon".
*   Input: "Crypto castle" -> "Crypto Castle".
*   Input: "Poloniac" -> "Poloniex".
*   Input: "DEFCON 1" -> The context implies Devcon 1. The speaker says "That conference, DEFCON 1" regarding Microsoft handing out passes. It seems he means Devcon 1. Later he says "Devcon 1" correctly. I will correct "DEFCON 1" to "Devcon 1" where contextually appropriate, as DEFCON is a security conference, Devcon is the Ethereum developer conference. Wait, he says "That conference, DEFCON 1" after discussing the Microsoft launch. I will assume he means Devcon 1 and correct it for clarity, or if he implies the *hacker* conference, keep it? Context: "It was that conference, DEFCON 1. Yeah, they were handing it out and that's why they wanted to make sure we were on their marketplace." Devcon 1 was in London. The Microsoft announcement was at Devcon 1. It is definitely Devcon. I will correct "DEFCON 1" to "Devcon 1".

*   Input: "EAA" -> "EEA" (Enterprise Ethereum Alliance).
*   Input: "BVVA" -> "BBVA".
*   Input: "Bob Summarial" -> "Bob Summerwill".

Let's generate the transcript.**[00:01] SPEAKER_00:** All right, well, welcome back, everybody. The first episode of the early days of Ethereum actually got quite good critical reception on LinkedIn and Twitter. I have a total of nine YouTube subscribers now, which I think is not so bad for a first video. And there have been a few people who reached out, who we've known a long time who really appreciated the content. One of them called it essential viewing. So anyway, we're back for another episode, so remind everybody. I'm Kieren James-Lubin, CEO of BlockApps, here with my co-founders, Victor. Do you want to introduce yourself quickly?

**[00:48] SPEAKER_01:** Oh, okay. I'm Victor Wong, co-founder and chief product officer of BlockApps.

**[00:54] SPEAKER_02:** I'm James Hermos or Jim, CTO and co-founder of BlockApps.

**[01:02] SPEAKER_00:** All right, thank you. And so I believe where we left off. So I can't watch video of myself, so I forget exactly how we ended the last episode, but I believe we pretty much ended with the Ethereum launch. And there were some things we left out even prior to launch that we can kind of backtrack to a little bit and then go forward to all of the kind of after-launch activity. So with that said, maybe I'll hand it to Victor to talk about the first ConsenSys Dappathon, which was June 2015, I believe.

**[01:38] SPEAKER_01:** Yeah, so that was, I think, the first actual hackathon building. You know, what, in those days, were known as dapps, I guess some people still call it, but that seems to have gone out of favor with blockchain applications. So the first idea was to really try to build blockchain applications directly on Ethereum. And that was in the first ConsenSys office, which was like a very small co-working space in like Greenpoint, I.

**[02:12] SPEAKER_00:** Think it was Water Street. It was called Green Desk, maybe.

**[02:21] SPEAKER_01:** Yeah, that's right.

**[02:22] SPEAKER_02:** Yeah, it's right next to the modern day Domino Park, maybe a block away from there or so.

**[02:27] SPEAKER_00:** Exactly. Yeah, that's right. So and it, of course, Domino Park did not exist at that time. In fact, Domino Park went up really quickly and took me by surprise. I like looked up one day and there was like a big, kind of well-manicured park there.

**[02:40] SPEAKER_02:** Yeah, well, they kind of walled it off and so it just was like, I don't know, I thought it was like an abandoned site. And then one day all of a sudden the wall was gone and there was a beautiful park.

**[02:53] SPEAKER_01:** So at that event, you know, which was I think two months, two to three months before the actual launch of Ethereum, I will say not. The concepts were really interesting. People were coming up, and it was mostly, I think, interns that were interning at ConsenSys over that summer. And ConsenSys at this point was only like, maybe 20 people at max.

**[03:16] SPEAKER_00:** 20 or 30.

**[03:17] SPEAKER_01:** Yeah, it was really, really small. And, you know, some great concepts came up. But, like, even with the stuff we built, we realized pretty quickly that no one could build anything in a short period of time. Like, it was just impossible. Like, very basic stuff, like reading a variable off the blockchain was kind of impossible. Like, you could read the state off the blockchain, all this kind of stuff. So that kind of led into. Yeah, like, everything building in those days was incredibly hard. And that led into. So we decided at that event we were going to, at the launch of Ethereum, we were going to do a bigger hackathon. And that became the second ConsenSys Dappathon, which kind of coincided with the launch of Ethereum. And it was us, you know, the Java client, which I think was called Ether.Camp at that time, and, like, other tools that were kind of combined together. But what was really interesting about that one was, you know, it was bigger. Like, I think the first one we had like six participants. The other one we had, like, I think close to 30. And. But it introduced, like, a lot of ideas that would become more developed pretty quickly. Like, the winner was a GameFi app. Like, it really had that element of tokenized gameplay. There was a decentralized social app, I think, called Truther or something. Something like that. And then there was like a traceability supply chain app in those early days. And that kind of all coincided with, like, the launch of Ethereum.

**[04:59] SPEAKER_00:** Yeah. So, okay, and this. So. So you're talking about the second one.

**[05:03] SPEAKER_01:** I'm talking about the second one.

**[05:04] SPEAKER_00:** Yeah, the second one. Also, the offices had shifted. So we had our ConsenSys, which we were kind of working as a part of at that time, had moved to a much larger office in Bushwick, which I believe they still have a presence there, though they've gone mostly remote. I remember there was like a. There's like a horse lineage app. Yeah, pretty interesting, you know, and we ended up actually hiring a couple people who participated in the hackathon. But that one was open to externals. Right. So that was the big difference. And it actually was, you know, quite well attended. The room, I think, never had the greatest air conditioning, but it was really quite hot in there, if I recall. And you think that one was like 24 hours or it was two days. I can't remember.

**[05:59] SPEAKER_01:** I think it was two days. And yeah, like the air conditioning thing. So we moved into that space to have the hackathon, like, you know, ConsenSys was playing because they had outgrown that co-working space already. And so we moved into that space, which can, you know, was a reasonably sized room. Like, you could probably get 80 to 100 people in that room. Right. But yes, the air conditioning was terrible and we had to frantically. We only realized this after we got into the room, so we had to like, frantically buy some and set them up.

**[06:30] SPEAKER_00:** Okay, I do have a memory of that.

**[06:32] SPEAKER_01:** Yeah, I don't know if you recall that, but yeah, we were like, trying to like, get those air conditioning units in place before a ton of people showed up because, yeah, like, we were sweating when there were only like five people in the room.

**[06:44] SPEAKER_00:** These were the scrappy days.

**[06:46] SPEAKER_01:** Yeah.

**[06:46] SPEAKER_00:** Manually configuring air conditioning. I think the amount of like, furniture assembly that you do is like a good proxy for you are in your startup journey.

**[06:56] SPEAKER_01:** There was a lot of furniture. I mean, we, we like. It was basically an empty room when we moved in there. And I think we moved in there a day or two before the hackathon actually started. So get everything running.

**[07:09] SPEAKER_00:** And was this to like, sort of commemorate the launch, I think, or was it like right before the launch?

**[07:15] SPEAKER_01:** It was, it was, it was right. It actually, you know, if you recall, at the time, we didn't know when the launch would be. Like, the dates were always shifting. Right. And we just said we kind of arbitrarily chose, like, we wanted to actually synchronize it with the launch, but because it was. Because we couldn't know exactly when the launch was, and even when they declared the date, it was still a little bit vague. Like, we were like, is that going to actually happen? So we. We kind of at some point had to arbitrarily chose the date and they. They more or less. What was the right date? Like, I think it was off by maybe a day or two.

**[07:55] SPEAKER_00:** Jim, I might have asked you this last episode, but I'll ask again. Do you remember one, trying to predict the launch and could you explain how. And two, there was some complicated mechanism for how the launch would actually happen because it's hard for, like, a decentralized group to decide on a launch time. I can't remember that at all.

**[08:13] SPEAKER_02:** You were mentioning it in the last video, and I didn't remember this, but I don't doubt it. It sounds correct. You were saying we were looking through the Git commits at the time we were.

**[08:22] SPEAKER_00:** Yes, you made this plot. It was like commits by day and as like the commits and you like extrapolated it forward. I think probably got within a couple days of the launch date but. Okay, so I have to. Yeah, I still don't know how they like set the clock on the first block so to speak. Maybe we can like dig this up. There was something they did and that.

**[08:44] SPEAKER_02:** We had probably in our DMs. I wish I thought to look between the first and second video to find the actual discussion that we had. Maybe the graph is in there.

**[08:54] SPEAKER_00:** Yeah, yeah, that's very funny. The Slack is a treasure trove of interesting things. All right, so yeah, so it launched and I kind of felt like there was a sort of. And then what going on. You know it took a little time for things to get going and you know this, it obviously it's been a smashing success. Right. It's just sort of the reality of a new platform. You sort of get it out there, you see what people do, you learn from it and you know it took a minute for the activity to kick in.

**[09:32] SPEAKER_01:** Jim.

**[09:33] SPEAKER_02:** I remember like, like a lot of people around us at the time had been buying a lot of presale ether beforehand and so the day it came out I think they were expecting it to like have a huge jump in value immediately. And when, like, you know, a couple weeks had gone by and it was only still like 20 cents an ether or so I remember people around us were kind of like some of the people there were like oh this thing was a flop. It's never going to go anywhere.

**[09:58] SPEAKER_00:** Yeah, yeah, yeah. And it's just psychologically, yeah, the expectations were super high. There was this concept floating around ConsenSys of day one dapps like you had to be ready right for the launch because you know it was a land grab and things were going to the moon and it turned out to not quite be obviously again smashing success. But yeah, the price is like under a dollar for a little bit and then around a dollar for like a while I believe. And I did want to mention so I had to look this up. So the first ICO, whatever you want to call it that was on Ethereum obviously Ethereum did its own crowd sale but it was like, you know, they took in Bitcoin and there was, it was something like 2000 ether to one Bitcoin at the time which I believe at the time was like 20 or 30 cents and then it had gone up to a dollar on launch which is already A pretty good return, you know, but that is what it is. The first ICO apparently was Augur. And I knew the Augur guys a little bit. I was digging through the Crypto Economicon videos. I believe one or two of them presented or run panels at Crypto Economicon for folks who are listening to this. Crypto Economicon was a conference that we had in January 2015 that involved a lot of the people who then, including Vitalik and some of the other Ethereum folks, then subsequently created really big and interesting, mostly layer 1 projects in the Ethereum space, but others as well. So the videos are actually up. I tweeted a couple of them, but there was a. Apparently, I think I created a YouTube channel like in 2015 and uploaded all those. I definitely remember getting them recorded. So check those out if that's of interest. So Augur was the first, I guess of the prediction markets platforms. There since have been a couple new ones that have popped up that seem to be popular. There was also this sort of competing project called Truthcoin. And I was kind of confused about how the two related to each other. I think there was no formal relation, though. I remember meeting up this guy named Matt Liston I met who. I checked his LinkedIn. He's been at a couple different places. So I think Augur. Maybe we should look up who actually founded Augur. So Jeremy Gardner I've known over the years and he. I met him in San Francisco with Vitalik because Vitalik was staying at what was termed at the time the Crypto Castle. And, you know, it's kind of what you would imagine, sort of like a co-working co-living crypto space for. And not everyone there was working on Augur. They were all working on different things. Kind of common thing to do.

**[12:59] SPEAKER_01:** I think if you hear the term Crypto Castle now, people would imagine an actual castle, say, you know, what you're describing, which is more like a dormitory.

**[13:09] SPEAKER_00:** Yes, it was more like a dorm. I mean, it was nice, nice little house. I can't remember. It might have been like, adjacent to the Mission in San Francisco. And so Vitalik would stay there sometimes. Joey Krug probably met two or three times over the years. I'm not even sure if I ever met Jack Peterson. So those are the three founders of Augur. So I guess they had, you know, they were good friends with Vitalik and. Or just sort of had realized early on that would be easier to develop on Ethereum than it would be to try to do something with Bitcoin, which was kind of the predominant suggestion at the time, but they did the first on Ethereum, Crowdfund, like I guess right after launch, the Wikipedia is saying August 2015, which is really, really early. I don't know if I believe this Wikipedia page. It says soon after the platform launched, users had created death pools or assassination markets on famous people. So back in 2015, every discussion about blockchain eventually led both to prediction markets and then this sort of uncensorability, you can't shut it down, would lead then to assassination markets. Assassination markets being you predict, you bet on the day someone dies and then someone takes the other side of that bet, kills them and collects on it. So apparently there actually were assassination markets created on Augur, according to this Wikipedia page. I'm. Yeah, I have to look into that. I'm a little bit dubious. But in any case, I guess Augur then blazed the trail sort of after Ethereum did with its successful crowd sale for the wave of ICOs that. That came later. But yeah, so Truthcoin was also this competing project. I just remember meeting up with Matt at like a Berkeley coffee shop and talking about. Both Augur and Truthcoin had some sort.

**[15:17] SPEAKER_01:** Of.

**[15:20] SPEAKER_00:** Machine learning, slightly computer science, graph theoretic way of determining what the truth was. So you take a bunch of votes from a bunch of people, but then determine the principal components of how the voting is, then extract the truth from there. So it sounded like very high end math mechanistic, which is very common of the space. Every, you know, the crypto has a lot of these like. And I was in the math department at Berkeley, a lot of these like mathematician types who like kind of came in and wanted to create like really complicated schemes and mechanisms and all that sort of stuff that had provable theoretical properties for something interesting about, you know, this space. But yeah, so, so they must have launched it like right away. That's very interesting.

**[16:06] SPEAKER_01:** I remember us talking to them at some point and they were developing that like they did want to be a day one dapp. I remember. And they were, I think the first.

**[16:15] SPEAKER_00:** One went live 2018, the Wikipedia page says. But they did the crowd sale like basically right away.

**[16:19] SPEAKER_01:** Right, right, yeah.

**[16:24] SPEAKER_00:** So should we go on to Devcon 1? Which I guess I can talk about. So kind of concurrently while all this is happening, we started to work a bunch. So ConsenSys had a business development team, a little bit of a mix of marketing, BD, actual sales, you know, etc. That was starting to generate interest from big companies in the technology. So you know, for us ourselves, we definitely Worked with companies far more than sort of the crypto public for most of the history of the company. Still don't really work with the crypto public today. But ConsenSys was kind of conflicted on this front. So they had sort of pure blockchain native project and eventually in big numbers. They also had an enterprise arm which is really more consulting oriented, although they kind of ended up sort of backfilling what they saw demand for with products at times. But in any case, the BD folks were reaching out to everybody and they actually got a fair bit of interest from Microsoft. And I think Microsoft had already been kind of watching the Ethereum revolution and seeing it as something interesting, the new front of the cloud war perhaps. And so know, we got to working with them and actually maybe for the technical part of this I could kind of transition, but basically. So ConsenSys had a couple, you know, preferred projects which had the low level, you know, like low level. I mean, like the blockchain client itself infrastructure that could be deployed on cloud platforms and maybe. Yeah, so that ended up being basically us and the, you know, the Java folks. Vic, do you want to, you know, take any, I think you were saying before.

**[18:33] SPEAKER_01:** Yeah, sure. So, like, like they. So they were interested in kind of being able to deploy a. One of the clients that we had. You know, we had the Haskell client and then the Java folks, they were actually more interested in the Java folks. Wait, I should take a step back here. Just mentioning that Devcon 1 almost didn't happen, if you recall, right. Because it was in this low period and the Ethereum Foundation was kind of running out of money because this is why the launch had to happen when it happened. And in that low period they were still trying to preserve a lot of cash. And so it almost didn't happen. And I remember a lot of people inside ConsenSys were like, no, like we have to like bring this. To kind of bring this up and make an event out of this, you know, like, I think Andrew Keys was leading the charge in that, really saying, like, we got to do this and then this Microsoft thing kind of bundled into that. Right. So it was us and the Java client. And my background was like, you know, in my previous company I had tried to work with Microsoft in building apps, like when they had their first mobile platform. And it took me like six months to get a meeting. And I had a cousin who was like a VP at Microsoft. So it was really hard. So it was amazing to me that they were just coming to us and they wanted to launch something with us in Two months. And I think at that point we decided, okay, this is a huge opportunity. We're going to drop everything and focus on that launch, which turned out to be the launch of Blockchain as a Service. But oddly enough, the Java guys started and then they just kind of faded away. Like they, they weren't really interested in kind of pursuing it. They just had other things going on. So we, we like went over it. So by the time Devcon 1 happened, the only thing that was working was, you know, our client on it was ready on the cloud. You could download it and you could start building on it right away. And I remember like we, we started to get like downloads immediately. People started to get, you know, people using it immediately. But that's also in that run up. That was like when kind of we realized, and Microsoft realized, like, if we're going to make this as a developer tool, it can't, you know, connect to the public Ethereum network because people wouldn't be able to get Ether. Like it was quite hard to get Ether at that point. There weren't really that many exchanges or anything to go on. So we were, that's kind of how we have created like private Ethereum, you know, and private enterprise, what, what became known as private Ethereum or enterprise Ethereum. So that, that kind of all led up and then the launch itself in London when we got up with Microsoft, I think people were shocked that Microsoft.

**[21:31] SPEAKER_00:** Was into it, you know, so I just looked that up and didn't have in our little outline, but I, I had forgotten about this. So I think Coinbase listed ether like mid-2016. Right. I'm seeing May 24, 2016.

**[21:48] SPEAKER_01:** So.

**[21:48] SPEAKER_00:** And I guess like Kraken was the popular exchange at the time, you know.

**[21:52] SPEAKER_01:** I think it was Poloniex.

**[21:54] SPEAKER_00:** Sorry, you're right. Yeah, Poloniex still exists.

**[21:59] SPEAKER_01:** And I just remember there was like the chat function on Poloniex. Like, man, like that was like crazy. Like that was Discord before there was Discord.

**[22:08] SPEAKER_00:** Oh wait, hold on. Circle bought it maybe and then it seems to have shut it down anyway. I'm confused by all this, but yeah, so it was like, it was sketchy for sure. There was like a whale chat box. I never really used it, but I would like to see it on people's computers and all that sort of thing. It was, it was difficult to get it in and out of Ether for a while. Jim, are you gonna say something?

**[22:33] SPEAKER_02:** I'm just kind of remembering back then. Remind me because I'm sort of like not sure if I've got this right, But I sort of, I think maybe you're, you're downplaying the Java thing a little bit. I think if I remember right, Microsoft guys were pretty mad at that time. Am I misremembering that?

**[22:49] SPEAKER_01:** No, you're not. They, they. Well the thing is they really want something that they could pitch to companies and you know, like just, you know, companies use Java, right? So they were like really like. And so like when we kind of like were like, like we just dropped everything and just focused on that. And I remember like we sort of had the internal mantra like we gotta get on stage and be able to write a DAP in like 30 seconds. Like that was our internal mantra.

**[23:23] SPEAKER_02:** They had like pre announced something or something and then the Java guys sort of disappeared or something.

**[23:28] SPEAKER_01:** Yeah, they pre announced that, you know, they were going to show like the Java client and the Haskell client and we were like this, we were like the runner up. Like they were like, I think they kind of accepted us because we were willing to work really hard and the Java got like. I think they knew that they needed a backup.

**[23:50] SPEAKER_02:** The other thing I, I remember about Microsoft is that there was a little bit of like tension within there because there were the, they were just launching Azure at that time and at the same time they had blockchain people and the blockchain people really wanted to focus on the blockchain side of it and the Azure people wanted to like use this as a way to, to promote the new platform. So. So there was always a little bit of friction within.

**[24:15] SPEAKER_01:** Yeah, I mean like I remember like, I think there, you know, Marley Gray was really driving those efforts inside Microsoft at the time and KO Teeter like they were like really, really pushing it. And I remember like they were trying to get people in the room to talk to us and some of them wouldn't even go in the room. I mean it was probably like you said, they were launching Azure, so that's a huge project. I'm sure they were just busy with other stuff, but we spent a lot of time in their New York office. I remember we were like going there all the time.

**[24:46] SPEAKER_00:** Yeah, I'm seeing The Azure launches 2010, I checked it. But it did feel much more nascent than it is today. Like Amazon got out, AWS got out there and like took the whole market and then Azure was kind of like in a catch up mode. But I think it might have even like exceeded AWS revenues at some point.

**[25:04] SPEAKER_02:** They were running around one of the conferences. I Can't remember which one. Handing out free passes to or to everyone.

**[25:11] SPEAKER_01:** It was that conference, Devcon 1.

**[25:13] SPEAKER_02:** Okay.

**[25:14] SPEAKER_01:** Yeah, they were, they were handing it out and that's why they wanted to make sure we were on their marketplace. So, like, they could hand out this free pass and you could get the, you know, you could get the. Our client up and running and start building something right away. And that was like a revelation to a lot of people. I remember, like, dozens of companies were like, starting in that first week, their.

**[25:41] SPEAKER_02:** Devious plan worked on us that we grabbed a whole bunch of free passes, and then a year later, we were like giving them like $10,000 a month to stay on.

**[25:51] SPEAKER_01:** It definitely works, but I get you.

**[25:54] SPEAKER_00:** Yeah.

**[25:54] SPEAKER_01:** But I don't know if you remember, like, the day after the Microsoft announcement, there was a spike in the price and we were like, I think we just did that.

**[26:05] SPEAKER_00:** The price? You mean the Microsoft stock price?

**[26:07] SPEAKER_01:** No, no, no. I meant the Ethereum price.

**[26:10] SPEAKER_00:** I think it was both, actually. Yeah, I think memory of the Microsoft stock price, like, slightly ticking.

**[26:15] SPEAKER_01:** Yeah, I think they up and we were like, hey, I think we actually did that.

**[26:19] SPEAKER_02:** So, like, either went from $0.20 to $0.30.

**[26:23] SPEAKER_01:** No, I think it actually went significantly up. I. I remember like. Like, it was. I think it might have like doubled for a day or something like that.

**[26:32] SPEAKER_02:** 20 cents to 40 cents, maybe.

**[26:35] SPEAKER_01:** I think it was like a dollar to a dollar eighty or. I. I don't remember the price.

**[26:40] SPEAKER_00:** Check it out. It's hard to see. It's funny. The price range is like, so.

**[26:45] SPEAKER_01:** Yeah, because the prices.

**[26:46] SPEAKER_00:** Oh, okay. So it's interesting, right? So. So Devcon's like December, right? Yeah, something like that. It's around a dollar. Yeah, there it is ticking up like. And I think we definitely got calls related to the Microsoft announcement into January.

**[27:02] SPEAKER_01:** Yeah, for sure.

**[27:04] SPEAKER_00:** So we probably had something to do with it. Yeah, you never know really what's causing price action.

**[27:10] SPEAKER_02:** But I, I'm joking, but I just remember, like, sort of the mentality within was that until it was up to $20, people thought it was a flop. And somehow when it hit $20, everybody around me all of a sudden got really excited then.

**[27:25] SPEAKER_00:** Yeah, the average person, you know, buys high, sells low. So, yeah.

**[27:32] SPEAKER_01:** That's.

**[27:32] SPEAKER_00:** That's pretty successful at 20 and it was still low. Okay. So moving along, kind of on the back of the enterprise announcement. Sorry, the Microsoft announcement, we started to get customers and a lot of it was like enterprises that were fairly early in their journey and, you know, wanted just some advice on on blockchain technology. Some of them were actually ready to implement something. I don't know. Vic, you took a whole lot of phone calls, you know.

**[28:01] SPEAKER_01:** Oh, man. Yeah, you know.

**[28:03] SPEAKER_00:** Do you want to comment on any of that?

**[28:05] SPEAKER_01:** I mean, it was kind of amazing. Now the numbers in relative size seem pretty small, but in the first couple months we went from zero to dozens of companies calling us. And the amazing thing to me was they had actually tried our software, they had played around and I remember over and over people were like, oh, you know, like we've been working on a blockchain project for the last two years and haven't been able to build anything and now we can do something. Right. So I remember like we were getting them from financial companies and like, you know, resource company and mining companies and like it was like all across the spectrum of people trying things because I don't think they really knew what they wanted to do, but they wanted an easy way to get in and for the first time they had that.

**[28:59] SPEAKER_00:** Gotcha. Do you remember? So I believe I'm trying to keep this straight. So I remember the, the Project Slock.it was sort of being marketed at Devcon 1, but I believe it's a lot of the same people as the DAO. And do you remember? Like, I think they. But I can't. I'm having a hard time keeping it straight.

**[29:26] SPEAKER_01:** So Slock.it was this sort of IoT, kind of strange thing that you could unlock a lock. But they, it was structured around what actually became the DAO. Like they. I think they invented the concept. Not the concept, but I think they practically created a DAO in order to fund this lock. And then they realized, well, you know, I think they realized, well, we don't actually need the lock. Like the DAO is the most important thing and the lock, the actual lock thing is not that interesting. So yeah, it was 100% the same people like they were introducing both ideas at the same time.

**[30:04] SPEAKER_00:** So let me transition into the DAO part. I'm going to go slightly out of order here. So Victor, what was the DAO?

**[30:15] SPEAKER_01:** So the DAO was basically, it was kind of like a investment fund on the Ethereum blockchain. Right. So basically people would put like money into this contract and this contract would basically fund the. The goal of it was it would fund different projects, but it started to like consume a huge amount of, you know, the overall ether supply. I think it was as high as like 20 or 25% of the entire ether supply got locked up into this contract.

**[30:50] SPEAKER_00:** Yeah, I'm looking on the Wikipedia right now. So the part of the reason I thought of it in this sequence is like looking at the price action. Part of it is that the supply, the extant ether supply went down because. Okay, so as of May 2016, the DAO had attracted nearly 14% of all ether tokens issued to date. So they ran a crowd sale and crowd sale raised $34 million, 34 million by May 10, 2016, more than 50 by May 12, over 100 by May 15. So sometimes the dynamics of these ICOs, this is one thing. It's kind of crazy, but like one thing that blockchain seem to do that are. It's really difficult to do with other technologies is to have this sort of really large scale collaboration and in this case to pool capital, basically. So I suppose the. There was a. Some sort of virality going on. People are talking about the DAO and you just see this like enormous movement of funds sort of overnight and you know, so okay, by the. They end up holding by May 21, 2016, over $150 million in ether from over 10,000 people. Which is about. It says, according to the article, about 14% of all ether tokens issued at that time.

**[32:27] SPEAKER_01:** Yeah.

**[32:27] SPEAKER_00:** Okay, so it was really fast, right? Like it took everybody's surprise. I remember, I think I had a meeting that the enterprise folks at ConsenSys had set up with, I'm gonna say the people at BBVA forgetting last names, but I think it was with like Scarlet and Carlos. I don't think you went to this one, Vic. I think you were in town. But they were just like, it just caught everyone's attention. It was crazy, you know, and they were, we were talking a bit about like operational use cases for the bank. But then it was also like, you know, there was a sense that like this is where the future is. Like the money just moved, you know, like there were no really, you know, there's heavy subscription agreements and you know, all that sort of thing. And you know, it was also a cautionary tale of what was to come over the next couple years. Yeah. So by, by June, the people discovered that you could exploit the DAO to siphon off the funds. Do you remember anything about that beyond, you know, it was crazy.

**[33:41] SPEAKER_01:** So, so there were. So you had all the supply locked into this contract and I think the hack was like. Yeah, so there was this massive race between. There was a flaw in the contract logic and because it's immutable, the smart contract couldn't be changed. Right. And when people realized There was this massive race between the people who were trying to extract the money out of the contract and the people who actually worked on the DAO itself. So it was like this. But the people who were successful at kind of extracting the money pulled out a lot of it. Like, I think, I don't remember the number, but I think it was like a huge amount of the value. They were able to pull that out.

**[34:26] SPEAKER_00:** Yeah.

**[34:26] SPEAKER_01:** Now the, the, the ironic thing was that it got pulled out and put into an account and everyone knew where it went because, you know, everything on the blockchain is completely transparent, but no one could do anything about it. Like they couldn't take the money out. And so the money was just sitting there, basically that got like. It was like it got stolen and left on the side of the street or something. And no one knew what to do about this situation.

**[34:54] SPEAKER_00:** Yeah, yeah. And so, okay, I'm kind of looking back on it. So it was, yeah, it blew up and it also caused the creation to. I remember there was a, at this time and we had to implement this in our software, a hard fork debate because. So it's pretty early. It's like less than a year after Ethereum launched. Probably a lot of the, you know, big ether holders participated in this. You know, they've lost significant funds, maybe all of their funds. And the question was like, do you make people whole or do you stick true to the absolute, you know, immutability of, you know, in, in the.

**[35:47] SPEAKER_01:** In.

**[35:47] SPEAKER_00:** The classic blockchain sense where, you know, it's totally buyer beware. Shouldn't have put your Ether in this contract if you weren't going to, you know, if you weren't prepared to lose it. And the refund group one. So in a sense, I mean both, like Ethereum, Bitcoin, really all the projects are governed to an extent. Right. By the people who develop the software and kind of on an ongoing basis, discuss additions to the protocol, et cetera, et cetera. Right. And even in the early days of Bitcoin, I was not really around for this, but supposedly they had to be extremely creative about having, about keeping the protocol running while not ever reverting any of the history. Right. So I don't believe they did. They've ever done a hard fork of the nature described here, though there have been maybe not sponsored by the founders. Obviously there are forks of Bitcoin now, Bitcoin Cash, you know, all that sort of thing. And so the Ethereum community elected to, or the foundation or whatever that is, elected to sort of forcibly revert the funds. There's just like a credit as of a certain block number. So everyone got their funds back. Jim had to code it. Maybe I helped a little bit. Now I was not coding anymore at this point. And so then Ethereum Classic was like the hard line. Like we're sticking the immutability. Sorry, Jim, are you going to say something? Oh no, Victor, you're going to say something.

**[37:40] SPEAKER_01:** No, no.

**[37:43] SPEAKER_00:** And so Ethereum Classic got some backers, I think maybe famously, I think Barry Silbert was in their Ethereum Classic, maybe still is. And eventually it was, I think someday. Victor, you told me this, right? Someday later it had a hard fork itself. Right. When some issue was discovered with the protocol. Is that correct?

**[38:07] SPEAKER_01:** I think, I don't know if it was a hard fork or a soft fork, but yeah, there have been like, you know, there have been debates inside. There have been debates inside the Ethereum Classic community too on how to implement different changes into the protocol. Right. It's not just running like there's constantly. I think Bob Summerwill of the Ethereum Classic Collective knows more about this stuff than I do.

**[38:34] SPEAKER_00:** Interesting. Yeah. Maybe I could follow up on exactly how this went down. But I think also I think Ethereum Classic maybe was mining forever philosophically.

**[38:45] SPEAKER_01:** Yeah.

**[38:45] SPEAKER_00:** Whereas Ethereum switched over to proof of stake like a year ago. Yeah. You know, you're now.

**[38:53] SPEAKER_01:** So.

**[38:53] SPEAKER_00:** Yeah, they were more kind of. Although there was. Okay, yeah. I just googled it. Here's a June 28th Cointelegraph article that says Ethereum Classic devs announce upcoming hard fork, yada yada. So they at least subsequently did some amount of hard forking. But you know, interesting nonetheless. Funny thing also when this, this hard fork happens, right. It's, you know, you don't. This is a silly comment from someone who's, you know, fairly compliance focused. Right. Like, what's the tax treatment of a hard fork? Like you had some say you had some tokens on one chain and then they morph and now you have tokens on both chains. I think it's like airdrops too are like ordinary income, which means whether or not you wanted those hard fork coins, you know, you, you probably have to pay taxes on them if you can access and liquidate them. But you have to pay them whether or not you liquidate. It's not just capital gains, you know, so interesting. Quite a, quite a strange test of our system that we've seen with Blockchain because, you know, they fork all the time. There's lots of airdrops Et cetera. And you might not even be aware. All right, so that was the DAO. I want to. Yeah, this was crazy. Like I still kind of can't believe this happened and it's happened way bigger and differently later. But you know, it, it's, yeah, it was quite a moment, you know, all of this.

**[40:28] SPEAKER_01:** Well, I, I, I, I looked up the current price and in current dollars it would be roughly the equivalent of $30 billion if you think about it. So yeah, it'd be huge, you know, like because just Ethereum was so small at the time.

**[40:44] SPEAKER_00:** Right, yeah. Okay, I want to take you to the second CoinDesk Consensus Hackathon and again hand it to Victor for everything you recall. Also we have some pictures from that time. Do you just show some of that on screen?

**[41:02] SPEAKER_01:** Yeah, I found, I found it from CoinDesk. Let me see if I can still find them. But so what I remember of it is that it was, I think it was one of the first CoinDesk consensus events which you know, subsequently became huge. And then so they, they kind of had two events around it. One was a hackathon which we were part of and then, and we were running, we were like one of the main platforms forms that was participating in it and then there was the event itself which was I think at the Ritz. Like both events were in Times Square. Like the hackathon came first at Microsoft in Times Square and then the event was kind of, you know, a couple blocks away in the hotel. And I remember that like during the hackathon itself we were in all in these like different conference rooms that, and there was you know, like early Hyperledger and some other, I can't remember who the other clients were, but there were like competing clients that were not Ethereum based. And there was a pretty good turnout I think like over a hundred people showed up. Like a lot of people kind of showed up and our room got so crowded we had to like co opt another boardroom in order to kind of like build. So like I think we got like a significant majority of the developers building stuff on our platform which was super exciting. And I remember kind of walking by the rooms that like Hyperledger had had or I'm trying to remember what the other client had and like you know there weren't very many people in there. It seemed like the people that were in there were like people who were working for them. So that was really, really exciting though at the end we didn't win. At least someone building on our stack didn't win. Because I think the winner was actually something that was getting built way before that hackathon existed, which was, you know, technically against the rules, but we didn't, we didn't hold any window. This is.

**[43:18] SPEAKER_00:** Victor asserts, if we lost, it's because someone else cheated. So.

**[43:22] SPEAKER_01:** Exactly.

**[43:24] SPEAKER_00:** That's, that's how we feel.

**[43:27] SPEAKER_01:** That's at least how I felt at the time. Whether or not that's completely true, it's, you know, that memory is subjective. That's all I say. Right.

**[43:39] SPEAKER_00:** And the, the, the rest of the conference.

**[43:44] SPEAKER_01:** Oh, and then the rest of the conference. So that I think was like the first shiny big blockchain conference, right? Like, you know, you had, I remember Vitalik speaking. They launched, I think the first Hyperledger app there. And a bunch of, you know, there was a bunch of activity. Like it was a really interesting combination because most of the other conferences like Devcon are really developer focused, but this, you could really see a lot of businesses becoming interested in. And the thing I most remember about that conference is that we were like pulled into a room at one point and that room was basically in the room was the head of Hyperledger. John Wolpert and Vitalik were in that room and they were like, hey, we heard that you guys have an enterprise ready version of Ethereum that you know, can switch between the public net and like private blockchains, right? And, and like I remember Wolpert at the time was like, my engineers claim that this is completely impossible. Like, and Jim, I think you like pulled off your laptop and you're like, here it is. Like, I'm gonna show you like, this is, this is how it works. And you know, like you can start building on it and everything. And there was this conversation going back and forth between Wolpert and Vitalik about I think Hyperledger supporting Ethereum. And it kind of ended. What I remember of it was it ended with, I think Vitalik was, you know, he always wears an Ethereum T shirt, right? And Wolpert is about three size larger than Vitalik. But interesting.

**[45:32] SPEAKER_00:** I think Vitalik is very tall, stockier, substantial. If they had a bench press competition, I expect there would be a pretty big differentiation, you know, in what John could venture what Vitalik venture.

**[45:49] SPEAKER_01:** Yeah, I, I think you're right. Like, it's not, we're not talking that John is unfit. He's just like much larger. And Vitalic is what at, you know, still quite skinny, right? So like John was like three sizes before and I think it was Andrew Keys that like pointed to The T shirt and like Vitalik, take that shirt off and give it to John because he was about to walk on stage and like it was like a muscle shirt on him. It was like so tight, you know, it was like a compression shirt. And he went on stage and that was like, you know, people were kind of shocked that like hey, what's going on? Like this. I had a Viper ledger and now he's wearing an Ethereum T shirt. And it's interesting because what. Eventually that led to Hyperledger actually supporting Ethereum type clients like Burrow.

**[46:38] SPEAKER_00:** Yeah I would add in talking to. Obviously we, we spoke to John occasionally over the years and he actually went on to join ConsenSys later. I don't really know what he's up to today. I don't think he's there anymore. But he had sort of a sense of like not wanting to be on the wrong side of history. Like he always wanted to talk about, he was always talking about like IBM's embrace of Linux as a. Instead of like pushing really hard on a continual basis with its own operating system. So they just put a ton of open source software development in Linux and of course it probably helped them, you know, have something to run on their mainframes which is still actually a big business for them today. And so he was always like debating back and forth like should we do our own thing? And it is, it was at least mostly open source. Should we go the, you know, the Ethereum way? What do we do? And I think this was you know, like perhaps the best illustration of that, that conflict I think IBM has since, you know, it's, it's. It was formidable for a while and sort of scary as a competitor and all that sort of thing. And I don't hear that much blockchain noise out of them anymore. I think they've shifted resources and all that sort of thing.

**[47:57] SPEAKER_01:** By the way, I did find the picture from that first hackathon. So you know this is off of Coindesk but here's the picture, you know, at the mic and this was one of the rooms and there was, we had to co op another room like this was very early in the process.

**[48:15] SPEAKER_00:** Y. Yep, I remember this one and.

**[48:18] SPEAKER_01:** Here I am sitting in the middle of it over here. But yes, but yeah, it grew really, really rapidly.

**[48:30] SPEAKER_00:** Alrighty. Close to rounding up here but got a couple more things. So things are moving along. 2016, there's some kind of organic momentum. I know like we hired a lot of people during this period of time we're delivering, you know, Our software has been used in enterprise projects. We're kind of like ramping up headcount because people are using our software more. And so I'm looking at this and like I can't believe that the timeframe were this tight. So Devcon 2 is September 2016 and so it's in Shanghai. Right. So I do remember having to deal with all the Visa stuff. The, you know, thankfully ConsenSys dealt with that. We were kind of doing a capital raise, sort of our first sort of seedish one at that time. But it was, it felt like a coming out party. I don't know, I think, what do you guys recall? What are some of your impressions from Devcon 2? Kind of, Etc.

**[49:46] SPEAKER_02:** There was some big attack on Ethereum. I'm trying to remember the details right now, but I remember in the morning and lots of stuff was happening on the business front there. But I remember waking up and suddenly I was just completely involved in like digging in with the Haskell client and, and figuring out what was going on and what changes we had to make.

**[50:07] SPEAKER_01:** So I do remember it was like.

**[50:10] SPEAKER_00:** Transactions that slowed the clients down being created. Right. And yeah, I, I think like, I guess it was like due to the way the data structures worked to some extent, it was like hard to make them process fast. I, I, I can't recall. But yeah, it was funny that it was right around that time also. Okay, so good.

**[50:35] SPEAKER_02:** Well, the funny thing that I sort of remember is like, and maybe you're about to talk about this, but, but the EAA was sort of formed during that conference and Victor somehow in the morning grabbed me and he's like, I've got all these meetings and I'd like you to come along too. But I was like, I had my laptop and I was like trying to dig into the tech with all this stuff that was going on there. So I sort of sat in the corner in this coffee shop and I was like programming all day and then at the end of the day I kind of was like, what were all those meetings you had? And Victor essentially is like, oh yeah, we just formed the EEA.

**[51:09] SPEAKER_01:** Well, I, yeah, it was funny. I, I think really it was Jeremy Miller, who I think later went on to become chief of staff for ConsenSys, who really kind of drove that. Like there had been a previous attempt, I think by Matt Spoke to create some sort of group of enterprises to work together on standards and that never kind of went anywhere.

**[51:32] SPEAKER_00:** But then I have no memory of this, so could you, you know, Matt was at Deloitte, Matt was at Deloitte at the time.

**[51:46] SPEAKER_01:** And Deloitte was early into blockchain, like, so they were@Devcon1. They were really early into blockchain. Blockchain and kind of building up a practice, ironically in the Toronto office. Right? So, like, they're really focused on it. And so they were quite early and quite knowledgeable. And so they were trying to kind of, at some point they had started this effectively a consortium of companies who want to use Ethereum, right? And then there was us where we were working with Microsoft, that was happening sort of organically and. But we realized that there was the need for companies to kind of collaborate, to work together on this kind of stuff. And Jeremy Miller just thought, like, this is in working. Like, what's happening now isn't working. We gotta get some proper structure. Because I think it was just an announcement on the Ethereum Foundation site, but no one was really driving it. So during that day, we like kind of aggregated a bunch of people in that coffee shop. Like, it was like literally happening beside you. And there was like, Jeremy, you know, John Wolpert was there from Santander. Like, Matt spoke came in, I think Marley came in at one point and, you know, like James Lazarus came in and we were all kind of saying, okay, we need this organization, we need to get this together. And it was all happening at this coffee shop that was at the Starbucks that was just like, just literally outside the conference center. And it really kind of all came together and it was amazing to me because it was like, right, like, so by the end of the day we were like, yes, we're going to form this group that eventually became the EEA.

**[53:30] SPEAKER_00:** So I want to add some peripheral details. So we get to Shanghai, right? You get this. We're jet lagged. It's a, it's a hefty flight. You know, you get this card and the card says something like, aliens not going to hotels. Aliens being like, you know, people who are not Chinese who are in the country must report to the police within 72 hours or something. I was like, does that mean, like, the hotels are like part of the police? Like, like, I don't know. I assume plenty of listeners will not have been to mainland China. And then you kind of gets to the hotel. So it's like it was like an hour drive whenever the main airport is to the hotel. Shanghai is vast. Like, there are high rises along the highway the whole way and they just get denser as you get close to where we do. You know, is there a name for the neighborhood? We were, we're staying in like the old stock exchange, I believe, which had been converted to a hotel.

**[54:39] SPEAKER_01:** Yeah, we were, we were right downtown. I'm trying to remember where we stayed at the time. The conference was right downtown along I think close to the Bund. That's the area next to the river and.

**[54:50] SPEAKER_00:** Yeah, that's right. So the Bund hand side and then the other side is like brand new.

**[54:57] SPEAKER_01:** Yeah, that, that's Pudong. Like that's like sort of, you know, originally was the suburbs basically. And you know, like I've founded two companies in China. So I, I, I think I was like the China expert there and like taking people around and yeah, like, I mean you, well if you're not staying in a hotel, the government wants to know how to reach you. And so if you're like staying in the Airbnb and stuff, you need to like, if you stay in a hotel, the hotel takes care of all of that stuff for you. Basically. They just, but like if you're staying in a hotel and we were all staying in a service hotel. But I remember like taking you guys for like a Chinese breakfast and like you guys loved it. Like we went back to that same place. Like I was like, they're all really good.

**[55:42] SPEAKER_00:** I think we went to like a couple holes in the wall too.

**[55:45] SPEAKER_01:** Yeah, exactly, exactly. So, so it was like this hole in the wall place and I was just kind of trying to give you the flavor and you guys really liked it. So we kept that. The other thing I remember about that conference is that the Wall Street Journal was there and I remember I got quoted from them as saying, I think China is going to be one of the biggest blockchain markets in the world. You know, this is before they started their own digital currency and really kind of went in on creating their own blockchain. But I remember people thought it was absolutely bonkers when I said that because they, they hadn't done anything like they was like so early in the journey. But as you said, this all happened really fast.

**[56:29] SPEAKER_00:** Yeah, I'd also mention. So we announced a project we were working on and was getting close to completion with BHP Billiton. Just a big time project and kind of the first of our supply chain work. Our kind of champion at BHP is a guy named Tyler Smith. Very smart guy, geophysicist, blockchain enthusiast. And so the announcement was great. It definitely got everyone excited about the technology, helped us close the financing at that time, et cetera. So we're all on stage. But also I want to mention that Tyler, I Think he'd been to Shanghai before and as one does when one's in Asia, you try to get some suits for lower cost. And he kind of told me his algorithm, there's something nearby called I believe the fabric market. Is that very big.

**[57:26] SPEAKER_01:** Yeah, that's right.

**[57:26] SPEAKER_00:** And he sort of hung out there for a little bit. He told me and he watched where the Chinese business people went and they all went up to the third floor to this pool particular guy. So he, he kind of showed us where that was. I think you got some too, right?

**[57:43] SPEAKER_01:** I did, I did. And, and that that algorithm worked out really well. That that is also my algorithm for finding good places to eat. Like I follow taxi like the way I found that hole in the wall. Like you know, I, I lived in Beijing so I've been to Shanghai plenty of times, but I didn't know near the hotel where they eat and I just got follow where taxi driver wind up stopping. And if that's the place, you know, they probably have pretty good food there.

**[58:08] SPEAKER_00:** Yeah, yeah. And he told me also the last time he had done a China trip, he, he went like 10 hours by buses, trains, boats to get like the best silk blankets which were somewhere near Shanghai. I was never able to look into this and get them back. So similarly he kind of, you know, followed the, just the local knowledge will get you a long way. I, I guess.

**[58:32] SPEAKER_01:** Well, nowadays it's all high speed rail. Like, like I remember, like I, I remember at various times traveling through China and being like, you know, having like 18 hour train rides and stuff like that, which were brutal because like in many times I just had to stand during that entire time in a crowded thing. But yeah, now it's high speed rail. It's, it's, it's amazing. Like it's, it's faster than planes in most cases.

**[58:56] SPEAKER_00:** Yeah, in any case it was, it was an experience. Right. So we also, we, you know, we did some business development there, had a lot of meetings with prospective customers, investors, all that sort of thing. It's definitely tough to do business in China for, for listeners considering it and not from China. I don't recommend it unless you really know what you're doing. But it was quite the trip. Like I actually had to leave a little bit early for some events. I was doing I with Intel actually.

**[59:30] SPEAKER_01:** Yeah, that's right.

**[59:32] SPEAKER_00:** But it was you know, crazy. It, it made, you know, it made things for, for a tech project. Ethereum was actually kind of Europe centric, but I think Asia, you know, almost bigger uptake there so it made it feel really global and it was just kind of funny, you know, just to, to see all of this happening, you know, at the same time, like the Internet kind of worked, you know, it was, it was cool to hang out in, in Shanghai as well and just totally different planet felt like. All right, I think with that segue we could probably wrap it up with the EEA leading up to the EEA launch. So the, the idea had been hatched in a Starbucks in Shanghai. And basically kind of the quote, I guess Jeremy was fond of saying is that like every innovation lab is using Ethereum now. They're watching us and they're each hacking it their own way to be something they can actually use. Right. So no one wanted to connect to the public net at that time. It's definitely changed some over the years, especially with the NFT revolution, etc. And you know, so there was not a lot of technological reuse going on in, you know, the, the duct tape that, you know, various enterprises were putting on the software to make it work for, for their needs. Probably most notable in that set of enterprises was JP Morgan, which we can, you know, talk about in more detail. Um, but a lot of them were doing it. The folks at the Innovation Lab at Santander who we know pretty well, we're doing their own thing. You know, it was quite a, quite interesting to observe the goings on. And Vic, do you remember? Okay, so there were like a couple face to face meetings that were like very hush hush. I think Microsoft's hosted some of them around the launch of the EEA. So you've kind of napkinned out the idea in Starbucks. But then what was the next thing that happened?

**[1:01:55] SPEAKER_01:** So then there were a bunch, there were a series of meetings that were kind of really about structuring. So like how did we want to structure this organization and you know, what composition should be? Like, should it be all big companies? Should it be, you know, like how much of the tech should be involved, how much of the, you know, company side should be involved and how it should work. Like, you know, should it be a free organization, should we charge membership? Should, you know, and all of that was on the table. But the, the amazing thing about those meetings is they did start small, but they eventually like wound up to be like 40 people in the room, like all the major clients, you know, like all of these things. Because I think at the time really where the interest was in terms of real world applications of the Ethereum blockchain was in the enterprise space. Like they were willing to kind of make investments into that. So, like, everyone was kind of participating into that. And so there were like, these, like, really, really active discussions. And ultimately we just kind of had to set a line in the sand and make a launch, basically. And that kind of led to it launching in sort of early 2017. But, yeah, in terms of timeframe, you gotta think that, like, it was only a little over a year when we launched with a single big company. And then at the launch of EEA, it was like 40 companies that were.

**[1:03:26] SPEAKER_00:** Yeah, I remember 28 or something like that. There was a logo wall that was nice. They showed, you know, it was really substantial.

**[1:03:34] SPEAKER_01:** And it was in the Brooklyn JPM office. And, you know, like, it was like, a lot of big players. And this really kind of told the world, like, hey, this is serious. Like, this is something that should happen. So I, I, you know, it was really, really exciting. But, yeah, the negotiations around it were really complicated. And in some cases he did. I remember, like, one of the biggest negotiations was between the different clients. Right. Like, there was us and there were other clients who were trying to figure out, like, how do we share information between us?

**[1:04:07] SPEAKER_00:** Yeah. I'd also add. Okay, so J.P. Morgan, when did they announce Quorum?

**[1:04:14] SPEAKER_01:** That's a good question. I. I don't. I think it was probably before the.

**[1:04:19] SPEAKER_00:** EEA launch, but I'm not sure.

**[1:04:21] SPEAKER_01:** Yeah, I know they were. I know they had a blockchain team that ironically also were working in Haskell. So they were. And, you know, eventually we wound up doing work on Quorum too. So there was, like, we had been talking to them a while and. But I can't remember when the official launch of Quorum was.

**[1:04:41] SPEAKER_00:** I have some memory that they demoed something at, and ConsenSys might have helped, like the front end of the demo. I can't, I can't quite recall, but I believe that they demoed something at the launch, which was what? Like it was either 2-2-2017, something like that.

**[1:05:02] SPEAKER_01:** Yeah.

**[1:05:03] SPEAKER_00:** So I think they must have announced it by then. So Quorum is. Was a flavor of Ethereum or a flavor of enterprise Ethereum, where they'd taken the Go Ethereum client and done things like ADD privacy and so that it was easier to obscure data. And there was like a messaging layer. It had, you know, et cetera, and similar things we developed over the years, just as we. In response to the, you know, privacy preferences and needs of big, big enterprises, basically. So they all wanted to use the technology, didn't want a native token. They didn't want too much detail Leaking to, you know, potentially competitors or even trading counterparties, etc. So they, you know, a lot of people at the same time developed kind of similar features to service. You know, the enterprise need the. But yeah, so the event, 30 big enterprises there, you know, or 30 companies, a few startups, a lot of big enterprises. I think the membership of the EEA peaked at like 500 companies or something really large. Right.

**[1:06:20] SPEAKER_01:** Like it was in the hundreds, like.

**[1:06:22] SPEAKER_00:** I, I don't remember 100 or something like that. So like on the back of this announcement, the business side, you know, got pretty excited and you know, as later in that year, there's also crypto run ups. Kind of everyone wanted to be involved. But I think of the EEA launch as sort of the end of the beginning. If you look back at the price trend.

**[1:06:46] SPEAKER_01:** Also.

**[1:06:48] SPEAKER_00:** On bringing it back up, I closed it. So let's say it's February here. It does start to really tick up and hit into kind of a fever pitch. 2017, 2018. Right. So yeah, you know, it's, it's already at this time, you know, around 10 bucks. But you know, it really goes dramatically up and then, you know, kind of the next phase is the, the heyday of the ICO era, which probably won't, won't talk about today, but in my mind that was when it was a new but established platform and technology. Ethereum kind of generally acknowledged by some of the public, but big businesses as well and had sort of transitioned. It was almost in the position of incumbent at that point. Now I also, I don't quite recall, like what, you know, maybe if I flip this to market cap, like when did a bit Ethereum, you know, move up the ranks? You know, it'd be good to know the, like what was the big ranks, Crypto coins or however you want to call them at that time. Like for a while, Litecoin was number two, right?

**[1:08:07] SPEAKER_01:** Yeah, and I think Ripple was up there.

**[1:08:10] SPEAKER_00:** XRP was usually three or something. And I don't even know where Litecoin is today, but it. I'd have to check when the actual crossover happened. Ethereum would be solidly number two for a long time. But maybe we should, you know, maybe I'll figure that out. Right now I forget how to overlay the prices on coin market cap or the market caps rather. So we've never seen the flip just yet, but it got close at different times in this, this journey. So anyway, I think we could probably leave it there. Slightly shorter than the last episode it appears, but I don't know Any final words? Big Gym from, you know, this interesting time period in many people's lives, our lives.

**[1:09:06] SPEAKER_01:** I, I, I think it was just like, you know, looking back, it seems that, you know, I think if you look back on successful projects, there's sort of that survivorship bias that, you know, all the elements were just there and you can see a lot of the elements there. But I don't think in any way that success was predetermined. Like, I think there was a lot.

**[1:09:33] SPEAKER_00:** A lot of coordinated effort. Right. A lot of working hard on it together, getting the pieces to make it happen, so to speak.

**[1:09:41] SPEAKER_02:** I mean it's dangerous to look back in time and say, like, I knew that was going to happen. But I will say that even before the launch, I remember feeling that I'd never seen such a large group of people so excited about a particular project as that one. So I, yeah, it felt like it was going to be successful.

**[1:10:04] SPEAKER_01:** Yeah. I just mean that, you know, we've mentioned a bunch of the people that, like, I think they all contributed to the success of the key point, even though they weren't, you know, the founders of Ethereum, like they, they made something happen that wouldn't have happened otherwise. Life.

**[1:10:21] SPEAKER_00:** Yeah, it's an interesting thing. It's like, are you, are you being tossed in a great wave or can you will reality into existence? And it's like, I tend to think of it as a little bit of both. Right.

**[1:10:33] SPEAKER_02:** I mean it's not all hot air from us because we literally, we do, we did some of it lives, successful technology.

**[1:10:41] SPEAKER_01:** So.

**[1:10:42] SPEAKER_00:** Yeah. Anyways, all right, let's, let's close it there. Thanks everybody for listening this far, if you make it this far on the second one. And yeah, it'd be interesting to, you know, we might continue this series. We could also kind of delve in on any particular part of it. Maybe we'll get a guest, maybe we'll, we'll do something. So if anyone wants us to cover anything particular, please do let us know.

**[1:11:11] SPEAKER_01:** Thanks everyone. Have a great day.

**[1:11:13] SPEAKER_02:** Thank you.