The user wants a clean, readable transcript of an Ethereum-themed discussion.
I need to follow specific formatting and content preservation rules.

**Key Constraints & Rules:**
1.  **No preamble/meta-commentary:** Start immediately with the first speaker.
2.  **Preserve ALL content:** No summarizing or condensing. The output length should be 90-110% of the input.
3.  **Timestamps:** The input has timestamps (e.g., [01:19]). I must preserve them exactly as they appear at the beginning of each speaker's turn. If a speaker speaks multiple paragraphs, only the first one gets the timestamp.
4.  **Formatting:**
    *   `**[MM:SS] SPEAKER_XX:**` followed by the speech.
    *   Merge consecutive speech from one speaker into one turn/paragraph unless there's a natural break in the input or if the speaker switches topics significantly within their turn, but the prompt says "All speech from one speaker before another speaks = ONE paragraph". Wait, let me re-read. "All speech from one speaker before another speaks = ONE paragraph". Okay, but then it says "Each speaker turn can be multiple paragraphs (natural breaks) with: - Bold speaker label with timestamp... - First paragraph... - Subsequent paragraphs have blank lines between them but omit the speaker prefix". This seems contradictory. Let's look at the example.
    *   Example provided:
        ```
        **[00:03] SPEAKER_00:** So, yes, I'm Bob Summerwill...

        We did meet in Bogota...

        **[00:38] SPEAKER_01:** ...
        ```
        The example shows Speaker 00 has two paragraphs, but only the first has the timestamp. The second is just text.
    *   However, the instruction "All speech from one speaker before another speaks = ONE paragraph" is in the "MERGE CONSECUTIVE SPEECH INTO PARAGRAPHS" section. The example shows multiple paragraphs.
    *   Looking at the input, the speech is often broken up by newlines arbitrarily by the ASR. I should group sentences into paragraphs if they flow together, but if there is a distinct topic shift or a long pause, I can use a new paragraph without the speaker label. The prompt says "Separate sentences with spaces, NOT line breaks" under the "MERGE CONSECUTIVE SPEECH INTO PARAGRAPHS" section. This suggests one big block per speaker turn. But the "REQUIRED OUTPUT FORMAT" allows for multiple paragraphs.
    *   Let's stick to the "One big paragraph" rule primarily, as that's under the "MERGE" section which is usually specific to ASR cleanup. The "REQUIRED OUTPUT FORMAT" example shows multiple paragraphs, but that might be for pre-formatted content. Given the raw transcript is very choppy, merging into one paragraph per speaker turn is usually the safest way to make it readable while strictly following the "Separate sentences with spaces, NOT line breaks" rule. I will treat "multiple paragraphs" as an option only if the input clearly has distinct separated thoughts within the same speaker block (like reading a list), but I'll prioritize merging lines into a single flow.

5.  **Corrections:**
    *   Technical terms: Ethereum, Bitcoin, NFT, Dapp, etc.
    *   Proper Names: Use the provided list.
        *   Adam B Levine
        *   Andreas Antonopoulos
        *   Anthony Di Iorio (mentioned as Anthony D'Orio / Anthony Diorio in transcript -> correct to Anthony Di Iorio based on list? The list says "Anthony D'Onofrio", wait. The list provided in context says: "Anthony D Onofrio, Anthony D'Onofrio, Anthony Di Iorio". Okay, the transcript says "Anthony D'Orio" and "Diorio". The correct spelling from the list is "Anthony Di Iorio".
        *   Vitalik (Not in list? Let me check. Ah, the list provided is "Known People (244)" but the list cuts off after "Aya Miyaguchi". It's an A-Z list that stops at A. Okay, I have to rely on general knowledge for names not in the list, but the list *explicitly* mentions: "Anthony D Onofrio, Anthony D'Onofrio, Anthony Di Iorio". Wait, Anthony Di Iorio is a co-founder. Anthony D'Onofrio is a different person? The transcript mentions Anthony Di Iorio ("Anthony D'Orio", "Anthony Diorio"). The transcript mentions "Anthony D'Onofrio" nowhere. Wait, actually the transcript says "Anthony D'Orio" and "Diorio" referring to the Ethereum co-founder. The list has "Anthony Di Iorio". I will use "Anthony Di Iorio".
        *   Charles Hoskinson (The transcript says "Charles").
        *   Gavin Wood (The transcript says "Gav").
        *   Jeff Wilcke (The transcript says "Jeff").
        *   Mihai Alisie (The transcript says "Mihai" or "Ming"? No, "Ming" usually refers to Ming Chan, but the transcript says "Ming" then corrects to "Mihai". Wait. The transcript says "Ming dynasty, where she immediately knocked off all the other directors". This refers to Ming Chan. The transcript also mentions "Mihai" (Alisie). I need to be careful.
        *   Aya Miyaguchi.
        *   Joseph Lubin (Joe Lubin).
        *   Taylor? (Likely Taylor Gerring).
        *   Kieran -> The list says "Kieren James-Lubin"? No, the list only has "Aya Miyaguchi" as the last entry. It doesn't have Kieren. But the instructions say "IMPORTANT: 'Kieran' -> 'Kieren' (Kieren James-Lubin, NOT Kieran)". Okay, so I must correct "Kieran" to "Kieren".
        *   Texture -> The speaker identifies as Texture. I'll leave it as is or check if there's a real name. The user calls him "Texture". He says "IamTexture on Twitter". I will stick to "Texture" as the name reference in text, but the speaker labels are SPEAKER_XX.
    *   Terms: "Ethereum", "Bitcoin", "DAO", "NFT", "DeFi", "white paper".

**Specific Transcripts Analysis & Cleaning:**

*   **[01:19] SPEAKER_03:** "Can you hear me?" -> Keep.
*   **[01:27] SPEAKER_01:** "Can you hear me? Yes, I can. Excellent. Happy straddle spaces..." -> Merge.
*   **[02:25] SPEAKER_03:** "I think technically fall starts..." -> Merge.
*   **[02:56] SPEAKER_01:** "I might have to see that..." -> Merge.
*   **[03:02] SPEAKER_03:** "I may have a photo..." -> Merge.
*   **[03:16] SPEAKER_01:** "Yeah. Text, you're welcome..." -> Merge.
*   **[03:55] SPEAKER_03:** "By the way, for Spaces Resiliency..." -> Merge.
*   **[04:06] SPEAKER_01:** "Yeah, you and Bob are co-hosts."
*   **[04:10] SPEAKER_03:** "Okay, it just appears a speaker to me..." -> Merge.
*   **[04:18] SPEAKER_00:** "It appears so."
*   **[04:20] SPEAKER_03:** "I see it now. Okay, fantastic."
*   **[04:33] SPEAKER_02:** "Can you hear me? All right, cool."
*   **[04:35] SPEAKER_03:** "Wait, very, very kind of cool August..." -> Merge.
*   **[04:57] SPEAKER_01:** "Yeah, completely agree. A lot of long sleeves..." -> Merge.
*   **[05:37] SPEAKER_02:** "Do you own a texture pump?"
*   **[05:40] SPEAKER_01:** "I do not, but I saw a few folks..." -> Merge.
*   **[05:51] SPEAKER_02:** "it was a joke cause I thought punks were ugly..." -> Merge.
*   **[06:15] SPEAKER_01:** "That's some good lore."
*   **[06:16] SPEAKER_02:** "That's some great lore right there..." -> Merge.
*   **[06:26] SPEAKER_00:** "Accidental success. Fantastic."
*   **[06:32] SPEAKER_02:** "Great."
*   **[06:32] SPEAKER_00:** "All right. Well, let's get going..." -> Merge.
*   **[06:39] SPEAKER_02:** "It's been a while..."
*   **[06:44] SPEAKER_00:** "always good when I think of you..." -> Merge. Mentions "peace love Revolution".
*   **[07:05] SPEAKER_02:** "so you know uh i was kind of i wouldn't say a hippie..." -> Merge. "Peace Love Human". "Bitcoin", "Let's Talk Bitcoin podcast", "Adam B. Levine", "Andreas Antonopoulos".
*   **[08:30] UNKNOWN:** "Okay." -> "UNKNOWN" is a speaker label in the source. I should keep it or change it if I know who it is. It sounds like a reaction. Probably SPEAKER_00 or 03? I'll keep it as UNKNOWN to be safe, or map it if obvious. The previous speaker was 02. The next is 02. It's likely a nod. I'll leave it as UNKNOWN.
*   **[08:31] SPEAKER_02:** "But it helped me..." -> Merge.
*   **[08:36] SPEAKER_00:** "Right. Very useful."
*   **[08:38] SPEAKER_02:** "I took into my role in Ethereum..." -> Merge.
*   **[08:43] SPEAKER_00:** "I seem to remember at some point..." -> Merge.
*   **[08:50] SPEAKER_02:** "Oh, a thousand in a day..." -> Merge.
*   **[09:12] SPEAKER_00:** "I mean, I can see why Decentralized Dance Party..." -> Merge.
*   **[09:18] SPEAKER_02:** "Yeah, so DDP, Gary..." -> Merge. "Decentralized Dance Party".
*   **[09:55] SPEAKER_00:** "I'll drop some links on Twitter..." -> Merge.
*   **[10:07] SPEAKER_02:** "It's funny. I had no..."
*   **[10:11] SPEAKER_00:** "didn't really understand the decentralized thing..." -> Merge. This line seems to be a continuation of 00 or a correction of 02? The timestamp [10:11] is under SPEAKER_00 in the text provided. The text starts "didn't really understand...". Wait, looking at context: 02 says "It's funny. I had no...". Then 00 says "didn't really understand...". It looks like 00 is finishing the thought or interrupting. Or maybe it's a misattribution. "didn't really understand the decentralized thing at that point i was not really involved...". This sounds like Texture (SPEAKER_02) referring to himself. However, the transcript assigns it to SPEAKER_00. I will stick to the transcript assignment but clean the text. Actually, reading further: "so that he was kind of ahead of the curve on that with me for sure". This sounds like Texture (SPEAKER_02) speaking. Then "So tell me about the vision..." is SPEAKER_00. The section [10:11] SPEAKER_00 seems mislabeled in the source or it's Bob responding. "So yeah that's gary la chance... gary was in that photo...". That sounds like Texture (SPEAKER_02). Then "So tell me about the vision..." is definitely Bob (SPEAKER_00). The segment [10:11] in the raw text is SPEAKER_00, but the content ("I didn't really understand...") refers to Texture's history with Gary. It's likely a speaker identification error in the raw transcript. However, the prompt says "PRESERVE ALL dialogue... ALL speaker labels (SPEAKER_01, SPEAKER_02, etc. - do not add actual names)". It implies I shouldn't *change* the labels. But if it's clearly an error, do I fix it? The prompt says "do not add actual names". It doesn't explicitly forbid fixing speaker ID errors if obvious, but usually "expert transcript editor" implies fixing flow. However, strictly following "PRESERVE... ALL speaker labels" might mean sticking to the source. But the source has "UNKNOWN" too. Let's look at the specific text at [10:11].
    Raw:
    **[10:11] SPEAKER_00:** didn't really understand the decentralized thing at that point i was not really involved so that he was kind of ahead of the curve on that with me for sure so yeah that's gary la chance who was a fellow vancouverite with me um he was uh funnily enough in in in a photo for the very first item i could find about vancouver decentral know the whole uh decentral toronto vancouver thing gary was in that photo for the first one maybe well known as well now but for doge claren so there is the doge wrapped mclaren which uh travels around many uh many conferences where they can get uh financial support for that um yeah gary's a great guy it's pretty fun So tell me about the vision that you had, which was then the same as the white paper, because on the Twitter thread, I was wrongly saying your mind was blown by the Ethereum white paper, where actually what happened was that you'd had a vision of this about a week before, And then the white paper landed on your lap. So what the hell was that about?

    The first half ("didn't really understand... gary's a great guy it's pretty fun") is clearly Texture. The second half ("So tell me about the vision...") is Bob.
    If I keep it as one block for SPEAKER_00, it attributes Texture's story to Bob.
    However, the prompt says "Merge Consecutive Speech into Paragraphs". If I assume [10:11] SPEAKER_00 is actually Texture, I'm violating the "don't change speaker labels" rule.
    But if I look at the raw format, maybe the line break was missing.
    Let's look at [09:55] SPEAKER_00: "I'll drop some links...".
    [10:07] SPEAKER_02: "It's funny..."
    [10:11] SPEAKER_00: "didn't really understand..."
    If SPEAKER_00 is Bob, he is saying "I didn't really understand...". That doesn't make sense in the flow of Bob interviewing Texture about Texture's history with DDP.
    However, the prompt says "PRESERVE... ALL speaker labels... do not add actual names". I will assume the transcript labels are provided as the ground truth for *who* is speaking, even if the content seems mismatched, OR I will treat the label as a container. Wait, if I'm an "expert transcript editor", part of the job is fixing speaker diarization. The prompt says "PRESERVE... ALL speaker labels (SPEAKER_01... - do not add actual names)". This is an instruction on format (don't replace SPEAKER_01 with "Bob"), but usually editors fix attribution.
    Actually, looking closely at the [10:11] block, it ends with Bob asking a question.
    I will split this. The first part is clearly Texture (SPEAKER_02). The second part is Bob (SPEAKER_00).
    I will assign the first part to SPEAKER_02? No, the input text explicitly writes **[10:11] SPEAKER_00:**.
    If I change the label, I risk violating "PRESERVE ALL speaker labels".
    If I don't change it, the transcript is nonsense.
    Let's look for a pattern. Is it possible the raw transcript just messed up the newlines?
    [10:07] SPEAKER_02 speaks.
    Then [10:11] SPEAKER_00 starts.
    Then [11:40] SPEAKER_02 speaks.
    If I look at [15:23] SPEAKER_00, etc.
    I will stick to the explicit speaker labels in the text to avoid hallucinations, but I will add a note? No, "no meta commentary".
    Okay, I will assume the transcript text under [10:11] SPEAKER_00 is what it is. But wait, "So tell me about the vision..." is definitely Bob asking Texture. If I leave it under SPEAKER_00, the first part of the paragraph (about Gary) is attributed to Bob. This is a classic ASR error where it switches speakers but keeps the previous label or vice versa.
    Given the instruction "expert transcript editor", I should fix obvious diarization errors.
    I will split [10:11].
    Part 1 (about Gary): SPEAKER_02. (Since it continues the DDP conversation).
    Part 2 (So tell me about the vision): SPEAKER_00.
    Wait, [10:11] timestamp is assigned to 00.
    Let's look at the context again.
    SPEAKER_02 (Texture) is talking about DDP and Gary.
    SPEAKER_00 (Bob) interjects or comments?
    Actually, the text "didn't really understand the decentralized thing at that point i was not really involved..." refers to *Texture's* state of mind.
    I will correct this. The speaker labels in the prompt are SPEAKER_00, SPEAKER_01, etc. I must use these IDs.
    I will move the Gary story to SPEAKER_02 and the Question to SPEAKER_00.
    But wait, if I do that, I am changing the input structure significantly.
    Alternative: I will output what is given, assuming the user might have provided the labels as they want them, or the "speaker label preservation" rule is strict.
    However, the rule "PRESERVE... ALL speaker labels" usually means "don't replace ID with Name".
    I will assume the text [10:11] is a continuation of SPEAKER_02 (Texture) answering Bob's prompt from [09:55] about links, or continuing his thought from [10:07], and then Bob (SPEAKER_00) cuts in at the end.
    Actually, looking at the text: "so yeah that's gary la chance... So tell me about the vision".
    This is two people talking.
    I will assign the first part to SPEAKER_02 (Texture) because he is the one who "didn't really understand the decentralized thing at that point" (regarding his early pre-Ethereum days). Bob has been in Ethereum for a long time, so saying "I was not really involved [in decentralized thing at that point]" makes no sense for Bob.
    I will format it as:
    **[10:11] SPEAKER_02:** [Gary story]
    **[10:25] SPEAKER_00:** [Question] (I need to estimate the timestamp for the second part or just use the one provided? "One timestamp per speaker paragraph". I'll keep the start time. If I split, the second part needs a timestamp. The input only gave [10:11]. I'll assign [10:25] (estimate) or just keep [10:11] if I can't calculate. The prompt says "Do NOT modify... timestamps". This is tricky. If I split speakers, I have to generate a timestamp for the new speaker turn.
    To be safe and strictly adhere to "Do NOT modify... timestamps", I should probably NOT split the turn if I have to invent a timestamp.
    But if I don't split, the content is wrong.
    Let's re-read the rule: "IF the input HAS timestamps [MM:SS]: PRESERVE them EXACTLY as they appear... Do NOT modify, recalculate, or regenerate timestamps".
    This strongly suggests I should NOT split turns if it requires generating a new timestamp.
    Therefore, I will keep the [10:11] SPEAKER_00 block as is, even though the first half sounds like Texture. Maybe Bob is saying "I [referring to Texture's story] didn't really understand...". No, that's a stretch.
    Or maybe the transcript labels are just completely wrong and I should correct them.
    "Expert transcript editor" -> Fixing speaker attribution is key.
    But the timestamp rule is "Do NOT regenerate".
    I will compromise: I will keep the speaker label as SPEAKER_00 for the whole block because I cannot generate a valid timestamp for the switch. The user can interpret the context, or maybe Bob is narrating? No, it's an interview.
    Wait, maybe I can check if the text *is* all SPEAKER_00. "I didn't really understand the decentralized thing at that point i was not really involved...". Bob Summerwill is heavily involved. Texture is the one telling the story about the photo and Gary. This is definitely Texture.
    Okay, I will split it. I will duplicate the timestamp [10:11] for the second part or just use [10:11] for both? Or, I will look at the next timestamp. The next one is [11:40] SPEAKER_02. That's a huge gap. The switch happens at "So tell me about the vision".
    I'll just use [10:11] for the first part (Texture) and then a blank line and the second part (Bob) with NO timestamp? No, "ONE timestamp per speaker turn (at the beginning)". If I put text without a timestamp, I break the format.
    Okay, I will interpret the "Do NOT modify... timestamps" as "Don't change the numbers [MM:SS]". If I create a new line, I have to assign a time.
    Given the strict constraint, I will assume the input text block [10:11] is a single turn. I will merge the lines. I will not fix the speaker attribution to avoid violating the timestamp rule. It is safer to keep the label SPEAKER_00 (even if likely wrong) than to invent a timestamp which is explicitly forbidden.

    *Self-Correction*: Actually, looking at the transcript again, [10:11] SPEAKER_00 contains the question "So tell me about the vision...". If I leave it as one block, SPEAKER_00 asks himself a question.
    Let's look at the [15:23] block. SPEAKER_00: "Yep." SPEAKER_02: "Yep."
    Let's look at [16:27]. SPEAKER_00: "I guess it's off-topic...". SPEAKER_02: "Maybe...".
    There are many short turns.
    The [10:11] block is clearly a transcription merge error.
    I will fix it. I will assign the story to SPEAKER_02 (Texture) and the question to SPEAKER_00 (Bob).
    For the timestamp of the new turn (Bob), I will use the same timestamp [10:11] or leave it blank? "One timestamp per speaker turn". If I use [10:11] again, is that "modifying"? It's duplicating.
    Let's look at the "Incorrect Format" section. It forbids multiple timestamps *per speaker turn*.
    Okay, I will output:
    **[10:11] SPEAKER_02:** [Gary story]

    **[10:11] SPEAKER_00:** [Question]
    This seems like the most logical "editorial" decision that respects the content preservation while acknowledging the likely missing timestamp for the switch. Using the same time isn't modifying the *value*.

    *Wait*, I need to verify the "Kieran" -> "Kieren" rule. The prompt explicitly mentions it. The transcript has "Kieran" (Speaker 03/01? No, Speaker 03 is likely Kieren, Speaker 01 is likely Bob? No, Speaker 00 is Bob. Speaker 02 is Texture. Speaker 03 is Kieren? The transcript shows "Speaker_03" early on. Then later "Speaker_03" speaks again and refers to Kieren in the third person? No, "Bob and Kieran" -> Bob (00) and Kieren (03).
    I will replace "Kieran" with "Kieren".

**List of Names/Terms to Fix:**
*   "Kieran" -> "Kieren"
*   "Adam B. Levine" (Check transcript: "Adam B. Levine" -> Keep as is or add periods? List has "Adam B Levine" and "Adam B. Levine". Transcript has "Adam B. Levine". Keep.)
*   "Andreas Antonopoulos" (Keep).
*   "Anthony D'Orio" -> "Anthony Di Iorio" (Correct based on list).
*   "Charles" -> "Charles" (Hoskinson).
*   "DARPA" -> Keep.
*   "D'Oreo" / "Diorio" -> "Di Iorio".
*   "Stefan" -> "Stefan" (George?).
*   "Gavin" -> "Gavin" (Wood).
*   "Jeff" -> "Jeff" (Wilcke).
*   "Mihai" -> "Mihai" (Alisie). Note: The transcript mentions "Ming" referring to Ming Chan later.
*   "Taylor" -> "Taylor" (Gerring).
*   "Aya" -> "Aya" (Miyaguchi).
*   "Vitalik" -> "Vitalik" (Buterin).
*   "Joe" / "Joseph" -> "Joe" (Lubin).
*   "Jerome" -> "Jerome" (de Tychey?).
*   "Greg" -> "Greg" (Colvin).
*   "Hudson" -> "Hudson" (Jameson).
*   "Jamie" -> "Jamie" (Pitts?).
*   "Tomas" -> "Tomas" (Stancaker).
*   "Amir" -> "Amir" (Taaki).
*   "Dogecoin" (transcript says "doge").
*   "McLaren" (transcript says "mclaren").
*   "Water Cooler" (Name of the chat group).
*   "Peace Love Human" (Group).
*   "DDP" -> "Decentralized Dance Party".
*   "Ethereum" (capitalization).
*   "Bitcoin" (capitalization).
*   "white paper" (lowercase usually, or White Paper).
*   "DevCon".
*   "Zug" (Zug, Switzerland).
*   "Zugg" -> "Zug".
*   "Red Wedding" (The event).
*   "Ming" (Ming Chan) vs "Mihai" (Alisie).
*   "Kieren" (James-Lubin).
*   "Texture" (Speaker 02).

**Format Check:**
"Separate sentences with spaces, NOT line breaks".
This is a strict rule. I must merge the lines in the input (which are broken by ASR) into single paragraphs.

**Timestamp Handling:**
The input has timestamps. I must keep them.
Example:
Input:
**[01:19] SPEAKER_03:** Can you hear me?

**[01:27] SPEAKER_01:** Can you hear me? Yes, I can. Excellent. Happy straddle spaces. GM. What's up, guys? How are you? I'm good. First week of September. I'm not sure if it's officially the first week of fall. But nevertheless... Super excited for a new month. I know at Strato we have a very exciting month ahead.

This is already grouped. But some inputs have lines broken.
Example:
**[04:57] SPEAKER_01:** Yeah, completely agree. A lot of long sleeves and sweatshirts during the night. cooler you guys are old been around talking about the weather we're waiting for you well i'm here even better welcome what's up gm yeah great great to kick this off um I'll hand the mic over to Bob, but I just want to pay my compliments to your PFT texture. It's quite a good one. Thanks, man.

This needs punctuation fixes and merging (it is already one block).
But if it was:
**[04:57] SPEAKER_01:** Yeah, completely agree.
A lot of long sleeves...
I would merge it.

**Content Preservation:**
Do not cut the story about Charles and the text message.
Do not cut the story about the Bitcoin vision.
Do not cut the texture punks story.

**Specific Fixes in text:**
*   "straddle spaces" -> "Straddle Spaces"? (Likely a Twitter Space name).
*   "GM" -> "GM" (Good Morning).
*   "PFT" -> "PFP" (Profile Picture). Transcript says "PFT texture". I will correct to "PFP Texture" or "Texture PFP". Context: "pay my compliments to your PFT texture". Texture's name is Texture. "PFT" is likely a typo for "PFP".
*   "texture pump" -> "Texture Pumps" (his NFT project).
*   "Viktor" -> "Vitalik"? No, transcript says "Vitalik". Input says "Viktor Tron" in list, but speaker says "Vitalik".
*   "Gary" -> "Gary" (Lachance).
*   "Doge wrapped mclaren" -> "Dogecoin-wrapped McLaren".
*   "Decentral" -> "Decentral" (Toronto/Vancouver hub).
*   "water cooler" -> "Water Cooler".
*   "Adam B. Levine" -> Adam B. Levine.
*   "Andreas Antonopoulos" -> Andreas Antonopoulos.
*   "blockchain" -> blockchain.
*   "Charles" -> Charles.
*   "DARPA" -> DARPA.
*   "Zug" -> Zug.
*   "Zugg" -> Zug.
*   "Ming" -> Ming.
*   "Mihai" -> Mihai.
*   "Ethereum Swiss" -> Ethereum Switzerland.
*   "Amir" -> Amir.
*   "Joe" -> Joe.
*   "Consensys" -> ConsenSys.
*   "NFT" -> NFT.
*   "L2" -> L2 (Layer 2).
*   "EVM" -> EVM.
*   "FCC" -> DevCon (likely typo in transcript "At the recent FCC" -> context "DevCon" in Cannes? No, DevCon 0 in London. "FCC" might be "EthCC"? Or "DevCon"? Transcript says "FCC". I'll keep "FCC" if I'm unsure, but "DevCon" is the standard Ethereum conference. Wait, "FCC" could be a typo for "DevCon" or "EthCC". Given it's "in Cannes", it's likely "EthCC". I will assume "EthCC" but checking timestamps... no timestamp for that part. "At the recent FCC in Cannes". Cannes is EthCC. I will correct to "EthCC".
*   "Jerome" -> Jerome.
*   "Greg Colvin" -> Greg Colvin.
*   "Tomas" -> Tomas.
*   "Nethermind" -> "nevermind" (transcript says "nevermind", correct to "Nethermind").
*   "CEO" -> CEO.
*   "Bitcoin" -> Bitcoin.
*   "Ethereum" -> Ethereum.
*   "NFTs" -> NFTs.
*   "DAO" -> DAO.
*   "Smart contract" -> smart contract.
*   "Cult" -> cult.

**Paragraph Splitting Strategy:**
The prompt says: "Separate sentences with spaces, NOT line breaks".
But also: "Each speaker turn can be multiple paragraphs...".
I will merge short lines into one paragraph. I will only start a new paragraph if the speaker has a distinct, long pause or topic shift that was already separated in the transcript, OR if the transcript provides a long monologue that looks better split for readability (though the "Separate sentences with spaces" rule suggests merging).
I will prioritize merging into one paragraph per speaker turn unless it's unreadable. The example provided in the prompt shows merging multiple sentences into one paragraph ("So, hello. Hello, Bob.").

**Let's process the text.**

**[01:19] SPEAKER_03:**
"Can you hear me?"

**[01:27] SPEAKER_01:**
"Can you hear me? Yes, I can. Excellent. Happy straddle spaces. GM. What's up, guys? How are you? I'm good. First week of September. I'm not sure if it's officially the first week of fall. But nevertheless... Super excited for a new month. I know at Strato we have a very exciting month ahead."

**[02:25] SPEAKER_03:**
"I think technically fall starts on the 21st or 22nd, but spiritually it starts after Labor Day, of course. I don't know if anyone has a white suit, but I actually sort of have a white suit. And you can no longer wear those already."

**[02:56] SPEAKER_01:**
"I might have to see that. White suit's pretty nice."

**[03:02] SPEAKER_03:**
"I may have a photo. I think it's been worn to two sort of summer weddings, and that's the only time it's been. But I could probably dig one up for you, Jamie."

**[03:16] SPEAKER_01:**
"Yeah. Text, you're welcome. We had him, we lost him. Give it a few more minutes for some more folks to pile in. Yeah, yeah, Spiritually Fall is here along with football to the behest of our European counterparts."

**[03:55] SPEAKER_03:**
"By the way, for Spaces Resiliency, Chat GPT is recommending two co-hosts up front. Now, do we already have the two, or can you add another one?"

**[04:06] SPEAKER_01:**
"Yeah, you and Bob are co-hosts."

**[04:10] SPEAKER_03:**
"Okay, it just appears a speaker to me. Maybe it appears as co-host to Bob on Bob's side. Bob, are you a co-host successfully?"

**[04:18] SPEAKER_00:**
"It appears so."

**[04:20] SPEAKER_03:**
"I see it now. Okay, fantastic."

**[04:33] SPEAKER_02:**
"Can you hear me? All right, cool."

**[04:35] SPEAKER_03:**
"Wait, very, very kind of cool August for those of us who spent some of it in New York. August is supposed to be hot, and it mostly wasn't. There's supposed to be a sharp transition heading into the fall, but it feels like it kind of started early this year. I don't know what's going on."

**[04:57] SPEAKER_01:**
"Yeah, completely agree. A lot of long sleeves and sweatshirts during the night. Cooler, you guys are old? Been around talking about the weather? We're waiting for you. Well, I'm here. Even better. Welcome. What's up? GM. Yeah, great, great to kick this off. Um, I'll hand the mic over to Bob, but I just want to pay my compliments to your PFP Texture. It's quite a good one."

**[05:37] SPEAKER_02:**
"Do you own a Texture Pumps?"

**[05:40] SPEAKER_01:**
"I do not, but I saw a few folks with them and obviously noticed yours, so might have to get one."

**[05:51] SPEAKER_02:**
"It was a joke cause I thought punks were ugly. So I made myself a better one. And then a friend asked me to make her one and then somebody else asked me to make one. And then like 30 people later, I was like, I should just fucking make a little thing where they can make their own. And then, um, uh, then, then my buddy started a Discord and 10,000 people showed up and I was like, look,"

**[06:15] SPEAKER_01:**
"That's some good lore."

**[06:16] SPEAKER_02:**
"That's some great lore right there. I thought it was going to be me and my hundred friends."

**[06:26] SPEAKER_00:**
"Accidental success. Fantastic."

**[06:32] SPEAKER_02:**
"Great."

**[06:32] SPEAKER_00:**
"All right. Well, let's get going. So hi, Texture. How are you?"

**[06:39] SPEAKER_02:**
"It's been a while. It's been a long time."

**[06:44] SPEAKER_00:**
"Always good when I think of you. The first thing I think of is love. Oh, and something I've spotted going through making my notes is your Medium is called Peace Love Revolution. Yes. So what's the story there?"

**[07:05] SPEAKER_02:**
"So you know, uh, I was kind of I wouldn't say a hippie. I didn't dress like a hippie. I didn't really hang out with hippies, but I I took some psychedelics and when I was a kid and I had some experiences and uh, you know, kind of drove my passion for uh, you know, doing good things and spreading love in the world. I know people that probably follow me are like, what the he just calls people retards all day, uh, yeah but I mean, I'm on Twitter. I don't know. It's full of retards. Um, so I started this group called Peace Love Human because uh, I was like sitting in a shitty basement apartment in San Francisco and uh, I was watching the news and I was seeing how religions got all fucked up and I was like, what if there was like a religion that didn't have any beliefs and we just went out and did nice shit? So for like three years of my life I was just like homeless and had no job and wanted to setting up like free hug events and like other stuff just to make people smile because like, you know, making people feel loved or making people happy was not like a quantifiable metric, but making people smile was. So that was that was what I did for my early 20s. So that's what I was doing, the community building. I accidentally started a cult. And when I realized that it was a cult, I shut it down."

**[08:30] UNKNOWN:**
"Okay."

**[08:31] SPEAKER_02:**
"But it helped me. It was my first foray into cult building, which obviously..."

**[08:36] SPEAKER_00:**
"Right. Very useful."

**[08:38] SPEAKER_02:**
"I took into my role in Ethereum, and I feel like the Ethereum cult is going pretty well."

**[08:43] SPEAKER_00:**
"I seem to remember at some point you told me that you've probably hugged a thousand random people on the street."

**[08:50] SPEAKER_02:**
"Oh, a thousand in a day, probably. Probably a hundred thousand more. More. Yeah. It was nice. It was, it was good. I mean, I could waste this entire thing telling that story. That's probably not what people want to hear."

**[09:12] SPEAKER_00:**
"I mean, I can see why Decentralized Dance Party also appealed to you on that score."

**[09:18] SPEAKER_02:**
"Yeah, so DDP, Gary, the guy who runs that, he came and stayed at my apartment in Brooklyn, and we had this three-story loft in a warehouse, and we'd let people come crash, and he came through, and that's how I met him, and I've done three or four of them. I was... What is it? It's Tom. I was Tom. So Tom is like a rotate. I was Tom one time. So that was fun. I had to shave my beard. I had a mustache. I looked funny."

**[09:55] SPEAKER_00:**
"I'll drop some links on Twitter for that for anyone who hasn't seen Decentralized Dance Party or you can go and have a Google on your own. It's quite exceptional."

**[10:07] SPEAKER_02:**
"It's funny. I had no..."

**[10:11] SPEAKER_00:**
"Didn't really understand the decentralized thing at that point. I was not really involved, so that he was kind of ahead of the curve on that with me for sure. So yeah, that's Gary Lachance, who was a fellow Vancouverite with me. Um, he was, uh, funnily enough, in, in, in a photo for the very first item I could find about Vancouver Decentral. Know the whole, uh, Decentral Toronto, Vancouver thing. Gary was in that photo for the first one. Maybe well known as well now, but for Dogecoin. So there is the Dogecoin-wrapped McLaren which, uh, travels around many, uh, many conferences where they can get, uh, financial support for that. Um, yeah, Gary's a great guy. It's pretty fun. So tell me about the vision that you had, which was then the same as the white paper, because on the Twitter thread, I was wrongly saying your mind was blown by the Ethereum white paper, where actually what happened was that you'd had a vision of this about a week before, and then the white paper landed on your lap. So what the hell was that about?"
*(Note: I am keeping this as one block per the timestamp rule, even though the speaker attribution is messy. The content is preserved.)*

**[11:40] SPEAKER_02:**
"Yeah, so what actually happened was I had a roommate for years ago, like years when I lived in New York. And he had tried to get me into Bitcoin when it was a dollar. And I said, this is like internet nerd money. I'm like a love revolutionary. I don't give a shit about this. And then he kept bothering me about it for years. And then it hit $1,400. And I was kind of humble enough to be like, well, if other people think it's worth something, I guess it is. But he had texted me and he said, listen, man, I want you to listen to this podcast. And it was the Let's Talk Bitcoin podcast with Adam B. Levine and Andreas Antonopoulos. And so I had given up working in tech because my arms had given out. I was a programmer and designer for a very long time. And, uh, I had, I started making cannabis edibles in California because it, uh, it seemed like a, uh, an industry that was going to be, um, some pretty easy to get into like the marketing, the production, everything was shit and I was pretty good at it. So, uh, yeah, so I had, I had a girlfriend who was about four hours away, uh, and I would go visit her on the weekends and I, so I threw the Bitcoin podcast on, I ate one of my candies and, uh, Don't drive stoned kids. But yeah, on the way there, I was listening and listening to the podcast and my, my brain is kind of tuned in and I had, I like, what could I, I can only describe as like a biblical vision. I would say like before that, I wouldn't have understood what that meant, but like, just this massive data download into my head where I can see, like basically see the future, like visually, like I just saw the whole thing playing out in front of me. And I was like, Oh shit, you know, Bitcoin, I'm still not particularly fascinated by, but the blockchain, um, this idea has an amazing amount of potential. And I kind of saw how it could help people coordinate. And so it just kind of it struck me so much that I was like, I got to go talk to Adam. I got to go meet the people who did this podcast because at that time it was the only Bitcoin podcast. And I thought anybody who wanted attention for what they were doing would probably contact them. So the buddy that had told me to listen to the podcast randomly came into town three days later. And I said, hey, man, I've been thinking a lot. I listen to the podcast. I have a lot of ideas. I need to meet Adam. I need to meet. And he goes, well, actually, I'm flying out in a couple of days to go meet him. We have a meeting scheduled. He's in Washington celebrating his birthday with his wife. And I said, no, no, no, no. We're getting in my car right now. I'm driving. I'm driving us there. I'm going, I'm going to go talk to him. And he's like, what really? And I'm like, yeah, fucking cancel your ticket. Like we're getting my car right now. So we drove like 20 hours or whatever to like Washington state. I walked in pretty much. I don't know what their meeting was about, but I pretty much just took Adam to the side and we ended up sitting in his hot tub on his balcony for like, nine hours just talking. And it was a really cool discussion. And I said, what I want from you is I want you to tell me anybody you know who's working on anything like this. And he said, well, do you know who Vitalik is? I said, man, I'm not in crypto. I'm not in Bitcoin. I don't know. I don't know anybody. I don't know anything. Um, and he said, uh, well, he just sent me this white paper a few days ago. I can like, I can forward it to you. Um, and can you guys still hear me?"

**[15:23] SPEAKER_00:**
"Yep."

**[15:24] SPEAKER_02:**
"Yep. So then, um, yeah. So he forwarded me the white paper. I looked at it. You know, to me, it wasn't as comprehensive as the vision that I had, but I thought, you know, this is kid's met, you know, right. Like what are the chances that all of this stuff lined up like this? So I said, yeah, make the intro. And so we started a Skype group and, you know, Adam was there. I remember Charles was there. Vitalik was there. I was there. It became the official Ethereum Skype group and just kind of grew from there. So, you know, it was like... Was that water cooler? No, no, no. Water cooler is something I made later because people... That was later. Yeah, so that was just the the literal like main ethereum skype channel that we used to communicate for the first i don't know long time. Right. No, water cooler was something I created later because I actually don't remember why. I guess I was kind of like..."

**[16:27] SPEAKER_00:**
"I guess it's off-topic or whatever, probably. Off-topic chatty thing."

**[16:31] SPEAKER_02:**
"Maybe, but I was kind of like the dude that everybody trusted. And so whenever anybody wanted to talk to somebody, they would come talk to me, which is why I got so much information about what was going on all the time. But yeah, so I think it was just an extension of that. People talk to me all the time when we create a little place for us to shoot the shit."

**[16:51] SPEAKER_00:**
"So when do you think you had that trip to Washington? When do you think that would have been?"

**[16:59] SPEAKER_02:**
"I'm horrible with time and dates, especially during that time, you know, when you're like a free-flowing hippie dude. Yeah. But I would say it was the week after... the week and a half after Vitalik sent the white paper out to his original group of people to get the feedback on."

**[17:22] SPEAKER_00:**
"Yeah, so it might even have been during November still."

**[17:27] SPEAKER_02:**
"Yeah, I mean, it was as early as you could get. I mean, just by happenstance, just by the timing I was there, basically the moment we were coming together."

**[17:38] SPEAKER_00:**
"Yeah, yeah, it's amazing. Cause yeah, so I was able to find that, uh, the video of, of you and Vitalik at the, uh, at the salon, uh, which was, uh, beaming into the Vancouver Decentral there. And that was December the 15th. That was. Yeah. You did that one."

**[18:00] SPEAKER_02:**
"Yeah. So we had been, yeah, I mean, again, the timing, the timing, I don't know, but yeah, obviously by that time we had been doing it for a minute."

**[18:11] SPEAKER_00:**
"Yeah. I mean, the funny thing was looking at that, that's before there was any code, any public code at least. There wasn't even any Python code from Vitalik published at that point. Gav and Jeff were weeks away still."

**[18:25] SPEAKER_02:**
"Yeah. And Jeff, to my understanding, just read the white paper and started coding it up on his own and said, hey, I've got this Go implementation."

**[18:34] SPEAKER_00:**
"Yeah, pretty much. And the same for Gav. They were both at the very tail end of December, basically like a Christmas project kind of deal for them, for the pair of them."

**[18:45] SPEAKER_02:**
"Yeah, no, it was great. You know, and I've been a developer my whole life since I was a kid. Um, and since I had quit coding, I wasn't really sure where I fit in, you know, but I was really happy when all these other people like got in, I guess maybe if I had dropped some code and gotten a lot more ETH, that would have been cool, but whatever."

**[19:08] SPEAKER_00:**
"So, I mean, to you at that point, like, what was Ethereum? Like, what was this vision? And what were you thinking that that could unfold to be? You know, what was the kernel of that?"

**[19:28] SPEAKER_02:**
"Yeah, so, I mean, it's so hard to remember those days. There's so much on top of it now. You know, I remember the general vibe was just, a technology that would allow people to coordinate, to, to encode value to, I mean, you know, like just at all dimensions, things that haven't even come to fruition yet, things that people aren't even thinking about because like, so much of it has gone to scale, just like fundraising, fundraising locally, like just coordinating anything. I mean, it was, it was just the whole world, like just imagining every single system being replaced by this decentralized coordination structure that, that gives the, the, you know, some, some 11 year old kid and, you know, Bangalore could create the next, you know, technical development. And, you know, I think that kind of platform is just something that seemed really empowering. So, you know, a lot of idealism, you know, obviously real life as it's played out is a lot messier and a lot different from how we imagined it. But a lot of idealistic things, a lot of like very much, uh, just, just really coordination. And that's a really shitty description of the vision that I had because it was so deep and so multidimensional and, um, but yeah."

**[21:02] SPEAKER_00:**
"Social operating system is something I've seen you say on a few occasions."

**[21:06] SPEAKER_02:**
"Yeah, I mean, yeah, just there's so many dimensions to it. But yeah, I mean, a social operating system for allowing people to encode their values or encode, yeah, literally their values, anything with value, creating incentive structures, contracts that are enforced at the exact level that they were designed to. Which none of that sounds really technical and unsexy, but to me it was really about the impact. What happens when you empower people to be able to create value in their local communities or encode value in ways they haven't been able to? What happens when you know, the equity in your company can be easily traded, you know, just all these things. Just so what happens when you can do that to houses and local businesses and local communities?"

**[22:09] SPEAKER_00:**
"Yeah. I mean, I'm thinking my own sort of thinking in those early days, it was an awful lot about empowerment and about, you know, giving, giving people the ability to control their own destiny. Right. Yeah. Um, and, and something I repeatedly thought was, was like, um, if you think about the, uh, what's it called? The pyramid of needs. What's it called? I forget the."

**[22:34] SPEAKER_03:**
"Maslow. The hierarchy."

**[22:35] SPEAKER_00:**
"Yeah. Maslow's right. Maslow hierarchy of needs. Know, I remember a number of times saying, you know, it's frankly obscene given all the resources that we have in the world and how, you know, how, how much more there is than was in previous years, it's obscene that people should be like worried about housing or education or health care or, you know, just these basic things, right. Yeah. And how wonderful would it be if you could like yank up that base layer a little bit so that people are not like living in this fearful place of powerlessness but instead can be like not worrying about that and not having to make these compromised bad decisions and everything, yeah. Just if you could do what you love. What, what a world that would be. Yeah. And I'm a lot less idealistic about it now after"

**[23:39] SPEAKER_02:**
"The last decade for a lot of reasons, but you know, the marshmallow test is real and you can create really good technologies and really good user experiences and as many guardrails as you can for people. But at the end of the day, there's motherfuckers that are going to eat the marshmallow before they even hear the rules, you know, and then they'll do it again and again. So, you know, I think there's a lot of, it's not that I think the problems are unsolvable, but they're, you know, the idea that, it's something from above being imposed down. You know, despite the fact that the system seemed to be that way, I think a lot of it is just the, the, the level of complexity of modern life relative to the average intelligence is it's just, it's, it's a wide gap and there's a lot of, I mean, I could talk about that for fucking 10 hours too. So yeah,"

**[24:37] SPEAKER_00:**
"Yeah, well, I mean, something that I saw in those early days of Ethereum as well was a real kind of almost like allergic reaction to anything that looked like organization or hierarchy or structure. You know, just like this total flip to the opposite side, right? Everything's got to be flat and open and, you know, everything, everyone involved with everything, which is just completely impractical for actually organizing or doing anything. Um, yeah. Yeah. It's just, it's just nutty. So, but then it's like, I realized it's like hierarchy. Isn't the problem being tracked in a hierarchy where it's to your detriment and you can't get out is the problem. Yeah."

**[25:25] SPEAKER_02:**
"Yeah. And a lot of, and I think a lot of times what happens in that is smart people, you know? Smart people aren't really, they don't really understand not smart people. And so what happens is we, we are born into a world where these preexisting hierarchies exist and they've, you know, to some degree or another, you know, kind of persisted through, through generation after generation. And then we come in and we're like, why am I at the bottom of this hierarchy? I'm smart. We're all too smart for this. And then they try to like, know they try to create new systems assuming that everyone is approximately like them and then, you know, I've, I've been through so many because again coming through the hippie I was in the bay area for a long time you see so many people think that they're the first person ever think of flat hierarchies and how it's going to be so much better and at the end of the day man like that's fine if you want to talk all the time and you want to argue and you want to get nothing done but at the end of the day you know a hierarchy is an information structure and it's also an accountability structure and so as long as there's accountability at the top and as long as the information is flowing correctly and as long as the outputs are you know optimal to some degree then it's the best you're going to get and it's, it doesn't mean we can't continually improve obviously life gets better and we, we have an obligation, you know, I think when you're creating things, it's not just the creating things. And I think this is a big problem that still exists in crypto. People think if you build it, they will come. You can't just build it. You have to build it and then you have to make it a button, a single button. It has to be so simple your grandma can do it and not destroy her life. And so it is this kind of perpetual attempt to take these complex structures, simplify them so that everyone has access to them. But through that simplification, not creating these kind of hells that no one can get out of. And I think... Just because of the rate of technological development and the nature of economic progress, our opportunities as people trapped in those systems is to build new systems. But ultimately, we're going to come face to face with the reality of why those systems were set up the way they were and understand that. The best we can really hope for in most instances is an optimization of that. We can try to make it simpler, more efficient, better and more adaptable. But those are a lot of dimensions that any one of them out of, how to out of sync is going to is going to create either more problems or the system itself will collapse. Right. And, you know, if the system doesn't exist and nobody gets, nobody gets anything."

**[28:19] SPEAKER_00:**
"Yeah. I mean, I guess it's a little bit analogous to sort of technical death and things in code."

**[28:39] SPEAKER_03:**
"Yeah."

**[28:39] SPEAKER_00:**
"If you've got code and you're like, Jesus, look at this. It's so much like complexity and these conditions. I don't think we need any of that. Let's just take all that out. But, you know, someone did that for a reason."

**[29:15] SPEAKER_02:**
"Yeah, and I, you know, after I became a father, I became really a huge proponent of the idea of if you think a stupid rule exists because the person who made it is stupid, you haven't thought through the problem. It isn't a bunch of people. I'm not saying this has never existed, but it's not like some nefarious guy at the top who wants to just ruin your life. It's some fucking idiot who did some idiot shit. And then now you got to make a stupid rule. You know what I mean? And you got to enforce it with fire. Otherwise, you know, your kids end up dumping plates of food in their closet and you find it six months later. And so, you know, it's, it's just that at scale."

**[29:59] SPEAKER_00:**
"You're gonna have to keep me on topic as much as you want to because I am a meanderer. Yeah. Um, on on this human side something I, I talked about, um, during my, uh, maple syrup peace phase was, was neurodiversity and the fact that, uh, normies would not be involved in the early phases of such a project, right. It's absolutely crazy to go and do what you did. Yeah. It's crazy what most people did. Um, so how does that play out the fact that in these frontier Technologies you don't have normal people? Well, you do, but you have a lot of, uh, of us people who would not fall into that category. So how does that all play out? What do you think is happening there?"

**[30:57] SPEAKER_02:**
"I think it's just the structure of how things have always occurred, right? So you have these kind of people on the front edge. And I was on the internet from, know, I remember reading when the HTML 2.0 spec was about to come out, right. And so the early days of the internet it was that and so I was on the internet all day talking to people and you know there was a technical barrier and and it's just you have these kind of neurodivergent people show up. So in the early days of crypto it was a lot of people who are paranoid, a lot of autistic people and a spattering of sociopaths who kind of could see that they could make money. And so that has a profound effect on how things play out. But I think it seems the way that at least in capitalism, what happens is huge amounts of capital come in and it just becomes this kind of probability matrix of, throw as much energy at this thing as you can on the front end, and then whatever survives is going to play out. But if you look at something like Linux or open source technology in general, it's very autistic. And autistic people have a very specific, I've noticed, differentiation from the average person, which is they, they honestly like believe that the terminal is the greatest interface of all time. It's like, they don't grasp that most people need buttons. And so it's like, you look at Linux, Linux was kind of a fringe thing only tech people used. And then Google came in and, at least had enough sense to hire some designers to turn it into something functional. Steve Jobs did the same thing with OSX. OSX was a previous Unix variant. And so you need those people. You need those people who come in who are on the edge, who are technical enough to be able to communicate with the technical people and understand. But they also need the clout, the money, and the power to overrule those people because... like Linux had like very horrible user interface and user experience for a long time even when they had window managers and you have to understand I was a designer so I would go into these open source spaces and I, I'm going to tell you what man like these people who for sure would not let you comment on their code and for sure not let you tell you how they were going to structure it or for sure not tell them what language they were going to use have no fucking problem stepping outside of their own expertise and driving a designer insane. You know what I mean? Very logical unemotional totally tapped out of any sense of like what a normal person needs and they they just beat the designers into the ground so you really need somebody who has power and the competence and the will and the desire and can put it all together, um, and, and I, I don't think we really see that. You know what I mean? The wallets suck. You, you know, um, you could, I, I don't know now but you know, like a year ago, I clicked a button and emptied my hot wallet, right? And like, that shouldn't be possible. Like how hard is it to throw up a fucking thing that says, hey, are you meaning to send every bit of this? This is a lot of money. You know, like why does it not just say, Hey, it didn't even say it in dollars. Do you know what I mean? It was, it was obfuscated. It didn't even say there should have been a massive fucking pop-up that said, you're about to send a hundred thousand dollars to somebody. Um, are you sure you want to do this? Yeah. Or, or, or I, as soon as I clicked the button, knew what had happened, even if there had been like a fucking five minute, you know, delay, um, right. You think there's, there's but none of this isn't happening. Right. And be the structure of the organizations or, you know, if the designers are having to argue with the tech people, like whatever it is, it's just grandma still can't use this shit. It's ten years in. If I find energy, I could, you know what I mean? I could like within six months we could we could solve these problems. And I just don't see."

**[35:26] SPEAKER_00:**
"And I guess. I, I guess this is the reason why things like the ETFs are so appealing, right? Is just, yeah. Can I just not deal with any of this at all? Uh, but I can just like use my Coinbase account? I've already got and it's just a thing that I buy or sell, right. And, and just, you know, it's a proxy for it but most people don't care. Yeah. But that reduces it to an investment vehicle, right. It does. It does. It does, and then that's really a failure, as you say, on delivery of the holistic platform that you do need something which is absolutely better, right? It's just like a product question, really, right? It's saying, unless the product that you are offering is absolutely better than something existing... or is cheaper or gives you some other benefits or whatever, then normal people are not going to use it. It doesn't matter what your worldview is behind that. You've given them something that's worse than what they have, so they don't care."

**[36:39] SPEAKER_02:**
"Yeah, and so I think exchanges and things like that acting as a buffer, it's a step. Ultimately, how are these things going to be used? The end user is probably not going to know."

**[37:00] SPEAKER_00:**
"what they're using on the back end any more than the average person knows what processor is in their phone so no no I mean I I guess the hope is it's like a layering thing right that you know in the same ways you've got those DeFi primitives that you're going to layer this you know whatever social recovery or buffered amounts or whatever or insurance for up or all this sort of stuff right that you should be able to put together a stack of things that have an equivalent kind of characteristic and experience to existing things, but without that strong dependence on, you know, a single legal entity that's, you've got that customer service provider kind of pattern rather than just it being raw, dangerous as you experienced."

**[37:50] SPEAKER_02:**
"Yeah. And I mean, you know, to this day, I mean, I feel anxious all the time because I hold crypto, you know? Me, I feel anxious all the time. You know what I mean? I think we all do. So it's like that's not an experience that the average person wants. The average person wants to put their money in a bank account. The average person wants to click a button and if something goes wrong, to be able to reverse it. You know, we haven't really addressed any of that. Again, it's a failure because the people who are in charge think like, anyone can do what they're doing and it's not that big of a deal. And like, all you have to do is do this and like, blah, blah, blah. It's like another, if all they have to do is click a button, you've done it. That's, that's your metric for success. Click one button and not worry about anything. You just know the thing's going to happen. And if it doesn't, it'll get fixed."

**[38:45] SPEAKER_00:**
"Yeah. Yeah. So, I mean, when I was looking through, um, sort of different phases of this period that I've been covering in the, um, in the early days of Ethereum, uh, sort of website there I, uh, I was noticing so in, in January in January and February 2014 there's just such a flood of people that came in. I mean, there were a fair chunk in December, uh, but that just really accelerated, uh, through January and February. So, I mean, how did that, like, play out that you've just got, like, tons and tons of people, you know, rocking up and really, like, volunteering?"

**[39:34] SPEAKER_02:**
"It turned everything into Game of Thrones. Yeah. Yeah, that's what happened. It turned everything into Game of Thrones. So, like, I was there day one. I was making sure, like, you know, first thing I did was – um Vitalik posted this website that he made. It was piss yellow. He had stolen some other shitcoin's logo and um, just put Ethereum on it and I was like, please don't post this. Give me till tomorrow. So I like spun up a logo, sent it to him, he was like, oh yeah, this is kind of what I was thinking. I was like thank god please don't put that out. Um, I don't know if I made a website or, and then somebody submitted an image, but the image was like, like, and so just real quick, like what I used to do is I used to be like the dude who, um, dev shops would call when they were six months behind on a project and needed it done in three days. Right. So I was a designer full stack developer. So my, my skill was I could take your idea and I could, I could make it look like it existed forever. And you had $10 million in funding in 24 hours, right. So that was my goal at that point once I realized that that was a massive gap I just inserted myself there and I'm only telling the story to say then when everybody flooded in and especially when the Zug house happened you had all these people kind of going behind other people's backs and um, trying to, um, push people out and take over their roles and it was it was just a very stressful weird time because you just get a different type of person, right? The type of people who show up and are just wanting to build a thing because it's cool. That's the type of person. But when they show up and they're like, yeah, let's fucking let's make sure it's us. Let's make sure we're the ones. Let's like, fuck those people. Let's not communicate with them. So there was a lot of like political maneuvering that was required to survive."

**[41:39] SPEAKER_00:**
"Yeah, and I mean, I guess that Miami house was where that really dug in. Because that was the first time that most people were physically in the same location out of that set of people."

**[41:52] SPEAKER_02:**
"It was pretty fun. The weirdest part about that was meeting Charles. And, you know, Charles, he might have been the first person who was doing kind of the thing that I just said, right? Yeah. He just showed up and kind of inserted himself and was like, I'm going to be CEO. He's just a fucking liar, though, man. He was like 24 or something. 25. Yeah, he presented himself like he was 50 years old and he'd been in tech forever. And here's the thing, man. I actually was probably the most experienced in terms of I'd lived in Silicon Valley. I'd worked in multiple startups. But... like despite my personality on Twitter or even if you meet me in person, like I'm pretty humble when I get into a group of people that I can tell have skills. So I kind of just sat back and didn't try to insert myself. I didn't try to like demand anything. You know, I'd be involved in this or that I just tried to kind of be as helpful as I could um so you know when I when I talked to uh uh charles for the first time i was like all right you know this dude's kind of weird like but well we'll see what's up so like literally the moment i met him in miami i shook his hand and i was like oh god he's a sociopath like okay well maybe he's our sociopath you know like every company has a sociopath like maybe he's like a well-regulated sociopath and then when we got to the miami house i found out no no he's not a well-regulated sociopath he's a fucking compulsive liar manipulative weirdo"

**[43:37] SPEAKER_03:**
"I was just going to say, in Charles' defense, at that time, he did look 50 years old. He'd go away with it."

**[43:46] SPEAKER_02:**
"Bro, when I found out he was like fucking seven years younger than me, I was like, why am I deferring to this kid? He's like, what the hell? Um, so yeah, it was, it was weird, man. Uh, like in the Miami house, I, he just said some of the weirdest shit to me. Um, there was some thing from, I don't know. I won't go into too many details. I've, I've covered them and given interviews to people who have reported on it, but not under my name. So I guess to shield me from any sort of retribution, but I, I, it was weird, man. He just said some weird shit to me. Like he showed me, I'll tell this one cause I've told it publicly a lot of times, but he was like, Texture, come here. And I'm like, what's up? And he's like, check out this text message. And I'm like, okay. And I like just met the dude and he shows me this text message and it's the chick. And she's like, I want to suck your cock so bad. Sorry for any children listening. Um, and, uh, I'm like, why the fuck is he showing me this? And he's like, you know where I met her? I was like, no. He's like, I met her on the front lines of Afghanistan when I was working for DARPA. I'm like, Jesus Christ, dude. Oh my God, shut the fuck up. And so I will say this because it's something that bothers me. Like for some reason, the media all says that the reason that Charles was kicked out was because he wanted to do business and not a nonprofit. And like Charles got kicked out because he was a fucking weirdo sociopath who didn't do anything. Like on above board and like, he couldn't be trusted. He, he didn't, he played games with everybody. Like I was not in his inner circle. Cause I, I did like, he would do, I call him sociopath. That's where like, they say something fucked up to see how you respond. They'll ask you to do unreasonable things to see if you'll do them. And then the people that do them and do them without question end up being in his inner circle. They, they become the people, which is continued on in his Cardano. So like, you know, he he he just operates in such a way that he gets sycophants around him. He lies to them. He gets them into situations where they like loyal to him and they don't question him. And then, you know, just weaves a whole reality around that that isn't real. And that's that that's my assessment of Charles. And he was he was not kicked out because of business. I mean, it was a cluster. Now. Yeah. I mean, no one else was kicked out. Let's just say that. I guess Amir left, but that's another story."

**[46:19] SPEAKER_00:**
"Well, Amir was kind of kicked out from what I saw based on the fact that people thought he wasn't actually doing anything. He wasn't really, like, pulling his weight or doing anything useful."

**[46:30] SPEAKER_02:**
"I liked Amir as a person. I haven't talked to him in a few years. We're still cool to this day. But, yeah, I mean, what was his skill set?"

**[46:40] SPEAKER_00:**
"Yeah, I don't know. Biz Debbie sort of stuff. He said he was... He was talking to people, potential investors sort of thing. But yeah. Yeah. And I mean, in terms of Charles, it took me a lot of years to really understand Charles, shall we say."

**[47:01] SPEAKER_02:**
"Yeah. You know, I defended you on that because I think you're like a really sweet guy and I think I understand your perspective. So whether or not I like Charles, I'm going to come defend you."

**[47:13] SPEAKER_03:**
"Not to dig too much, but Charles is kind of like buddy, assistant, partner guy. Is his name Jeremy? I'm trying, I'm remembering, because I actually thought he was Jeremy Wood. Yeah, and maybe there was more there, but I'm just, to Texture's point, you know, maybe he was just naive, or maybe you guys know more than I do, but that was sort of a strange dichotomy."

**[47:39] SPEAKER_02:**
"Yeah, again, I think it's just whoever would follow him around and not question him. That's how you got to be his right-hand man. The less questions you ask, the closer, better friend you are. The more you listen to his stupid stories, didn't call him on it. You know what I mean? I was on the front lines of Afghanistan for DARPA, and now I'm like, shut the fuck up, Charles."

**[48:01] SPEAKER_00:**
"With Jeremy Wood, he notably called him, boy, come here, boy."

**[48:06] SPEAKER_02:**
"I never saw that. Wow. I'm telling you like I remember some story about him like playing games with people in the Zug house like sending somebody's sending somebody off whose wife was there, a girlfriend, and telling them that they had to go do this thing for him out of town. And then when that person had left, he then tried to convince one of the other dudes to get with the dude's wife. Just weird stuff, man. Why would you do that? You have an opportunity of life. The answer is you're a fucking idiot who lied yourself into a situation you shouldn't be in and you are a compulsive... lying manipulator. I'm sure it makes him feel smart or something. I don't know but like it was just the the stories that when he when he was gone after the red wedding I think everybody breathed a sigh of relief you know the biggest problem for me was um after the fundraiser after the red wedding Stefan who I had introduced or I had welcomed into the organization and again there was a lot of political stuff if you went to Zug you got basically put up in the hierarchy so I ended up under Stefan I couldn't go to Zug because my girlfriend was pregnant and I couldn't leave to go to Zug for a month and yeah I don't know Stefan was I don't know. High energy, high anxiety dude. It was a weird thing."

**[49:44] SPEAKER_03:**
"He was smoking the stereotypical amount of cigarettes at the time."

**[49:49] SPEAKER_02:**
"The stereotypical amount? That dude lived... He had a vape that he puffed. Oh, you're right. It was a vape. It was clouds of smoke. And so I went, you know, with DevCon Zero, I went and spent a week with them in the office in London. And, dude, Stefan, if you weren't having a fucking panic attack, Stefan couldn't tell you were working. It was crazy and he would pace around this co-working space like nobody else was there just the whole place looked like a fucking rave, dude. Like, I think he got kicked out because he was trying to film a TV show and vaping too much and he had bought like fifty thousand dollars worth of camera equipment because his dream was to start a TV show or something on the Ethereum budget."

**[50:47] SPEAKER_00:**
"Yeah, I heard that London location was pretty special."

**[50:53] SPEAKER_02:**
"It was weird, man."

**[50:58] SPEAKER_00:**
"Did you say you were never in Zug?"

**[51:00] SPEAKER_02:**
"No, I never went. My girlfriend at the time was pregnant. I had spent a month in Panama with Eric Voorhees and his team while she was pregnant. Honestly, in retrospect, if I could go to... It's hard to know how things would have played out because of the political stuff. I was not political. I didn't have any strategy. I was not prepared for any of that shit. My... I just tried to be the most authentic, trustworthy, do-what-I-say person, good to everybody. That's how I survived as long as I did. I don't really do politics. All that stuff was really weird."

**[51:47] SPEAKER_00:**
"I mean, all of this was prior to both the crowd sale and... the formation of the Ethereum Foundation, right? So the Red Wedding was 3rd of June 2014, where you had that, I guess, that final decision of the foundation happening versus the for profit because you had, uh, we had people coming notably Anthony Di Iorio coming to, uh, Zug at that point to sign papers, right. You know, it was it was to do with that Swiss, uh, legal entity and then it was like yep no we're not signing the papers the big mess uh, and then the foundation, uh, was, was July that that was, uh, incorporated and you still have the crowd sale ongoing through July and August. So yeah. And that was a hell of a long span of time."

**[52:57] SPEAKER_02:**
"Yeah. We kept saying two weeks. I don't know. That was a meme for a very long time. Two weeks, two weeks, two weeks."

**[53:07] SPEAKER_00:**
"Well, the website that was up at the time of the Miami conference was showing a countdown to the first of February. That was when the sales were going to start."

**[53:17] SPEAKER_02:**
"Yeah. And then, you know, I was with Vitalik when the sale was launched. Uh, we had hung out all day in San Francisco. We were in the Westfield mall in the food court for, uh, uh, he needed WiFi. Um, and he was just sitting there and he just looked up at me and he goes, Oh, the crowd. So I went live. Um, because that wasn't planned. I don't know if Taylor talked to you about that, uh, when you, uh, was an accidental launch was it? It was an accident. I don't know you have to ask Taylor about that but yeah I guess he accidentally accidentally hit the button because you know it was legal like that's what kept happening they kept saying we're waiting on legal we're waiting on legal we're waiting on illegal like legal in retrospect right so you and Kieren must have met each other a little bit, yeah various times, yeah, we've, we've actually hung out more probably in the last five years than we did back then. Um, yeah."

**[54:27] SPEAKER_00:**
"And I guess that Kieren, you saw more of that sort of New York legal side of things."

**[54:35] SPEAKER_03:**
"yeah so okay this is a good good tie-in point so uh and and bob at your request of course i was digging through the emails trying to piece together some pieces of the timeline you know yesterday day before so i had um I think by March I was talking with Vitalik and, you know, I was in academia at that time, and he kind of found it useful to bounce like protocol, economic modeling stuff. Off you know like i was like good at reading the white papers and understand what they were doing i could you know kind of code at that time i could still kind of code today but that's sort of we ended up talking about like how the thing should work at a you know theory protocol level more than an implementation level and that kind of I guess, and this was covered in the Red Wedding time, there was a discussion of the usage of funds that ended up on a whiteboard or something. And a lot of it was theoretically earmarked for a research group that meant to solve hard problems like scalability. In crypto that, you know, like in practice, people have sort of solved today and not by any of the means we imagined exactly. But, you know, they've been solved to some degree at least. Um, like with layer twos for instance. Um, scalability was very much anticipated as a problem and you know it took a couple years but you know we had like 55 dollar fees on NFT transfers at some point. Um, so I think um, Metallic sort of like, uh, talk we talked about this for a little bit and then he kind of like blessed me as like the representative who's currently in academia. I started contacting people and trying to get them interested in Ethereum and then doing like research related to it in general we even like set a legal entity up for a separate research group at some point. And I'm trying to remember, so Texture, we mostly worked together just on the site, basically. Like, I guess you were like, you know, web designer at that time. But I'm trying to remember."

**[57:05] SPEAKER_02:**
"Yeah, I was doing web design. We had talked about the CRG, Cryptocurrency Research Group. And I was like, that's cool. Let me build a website. I remember throwing, you know, faces on it. And then it just kind of puttered out, which, you know, it's... you know, like, um, I, it would have, it would have been a like cool thing, fun thing. I don't know. Um, but also, uh, there's a story about Anthony Di Iorio, not anyways. I like, I didn't know people were getting paid for a long time. And, um, I, uh, was like living on my sister's love seat in her one bedroom apartment with my daughter. Cause I was like fucking homeless, uh, and working on Ethereum as much as I could, uh, like multiple other jobs, uh, to, to try to make money. And, uh, I contact or Anthony Di Iorio contacted me one day cause he was, you know, he was in the earlier days, like the primary contact, um, that I would talk to the most. And he called me and he asked me for a favor. And, uh, I was like, yeah, man, no problem. And I said, Hey, by the way, if you, you know, like, listen, I'm in a bad spot right now. Is there any way I could get like back pay for 10 grand, which, you know, was not much. And this dude just says, Oh no. And I was like, what the fuck? Anyways, I talked to Vitalik. The way it goes back to the CRG is the CRG was supposed to pay me $5,000. So you owe me $5,000, Kieren. I don't know, you know, given that it was so early, if you could just pay me an ETH relative to the price at that time, that'd be sick. Exactly."

**[58:56] SPEAKER_03:**
"20 cents was the presale price. Yeah, something like that. So it'd be like quite the amount of ETH."

**[59:04] SPEAKER_02:**
"Yeah, so just like 15,000 ETH and we'll call it even."

**[59:08] SPEAKER_03:**
"All right."

**[59:08] SPEAKER_02:**
"All right."

**[59:14] SPEAKER_00:**
"But yeah, I mean, I guess, you know, many, that was the case for many people through those months, you know, for some people that was nine, 10 months of unpaid contribution."

**[59:29] SPEAKER_03:**
"My memory is also that Anthony was the main force behind sort of actually not quite stopping, but delaying the funding to the CCRG. So like somehow we got it, some of it way later. Di Iorio. Di Iorio, yeah. Um, and it was like not quite the original amount but it was still some but we were all like working on different things at that time so we ended up returning it I think but yeah it was a strange like the the strange delay that happened I guess like right after the pre-sale. Um, So before people are working, you know, uncompensated or largely uncompensated. And then right after there was, I suppose, like a big cash grab going on. So like maybe, you know, better than us. So there were a bunch of legal entities getting set up like, you know, there was like the Berlin Dev Company and then there was another one like in each. Everyone tried to like pull out as much of the pie as they could."

**[1:00:38] SPEAKER_00:**
"but like yeah i don't know yeah good yeah so so uh anthony the oreo not you yeah uh incorporated um ethereum canada in february actually but it was about it was just a few days before everyone went to Zug so his thought i guess was everything was going to happen out of toronto but that didn't happen You had Ethereum Swiss got formed in Switzerland somewhere in April, I think. You had GAV incorporating Ethereum Dev in Berlin. Jeff in Amsterdam, though, that took quite a few months, more legalities to it. And there was an Ethereum... in London as well. Most of those FDev ones were kind of co-founded by Vitalik and Gav and Jeff and Mihai kind of group. Yeah, it was only the the Toronto one there where it was that I could see Anthony was a director. I don't think he was ever a director on any of the other legal entities. They were basically the, you know, the, the debt people, um, and all Mihai and Taylor. Um, but, but yeah, when, when you'd had the crowd sale and the, the had been formed and then were the recipients of those funds, there was a whole power grab of a mess of how those funds went out and, uh, in, in cryptopians it talks about Gav maybe wanting to like grab all the money straight into dev but then it's like that's probably not legal and it's probably not a good idea either and Joe wanting to do it sort of a milestone based slow delivery which is i think what it sort of ended up being but you did have this sort of weird situation where um You'd say, oh, do you work for the Ethereum Foundation? But very few people actually work for the Ethereum Foundation. Most people were actually working as staff or contractors for these for-profit legal entities, which were sort of doing the work."

**[1:03:02] SPEAKER_03:**
"Yeah, I guess they must have got it kind of like having now run a business for a long time. You've got to set up sensible contracts and IP agreements. Sometimes that looks like an intercompany agreement. And then if you do it in the buttoned-up way, there's a lot of headache associated with such things. I think it was a hell of a lot looser than that."

**[1:03:28] SPEAKER_00:**
"I have a a strong memory yes of like a let's just put all the money in this other legal entity discussion going on like during the whole red week wedding week you know so yes man yes um and and yes the majority of those legal entities have since been shut down um that was something that Ming did over the course of her time was tidy up all of this like corporate mess that was maybe not really even required in the first place but uh um yeah I mean I think yeah good sorry well they could have just worked for the foundation but I guess they didn't they didn't want to be in Switzerland which maybe was part of it and I remember this was yeah it well this was another funny thing right with the uh with the spaceship"

**[1:04:25] SPEAKER_02:**
"was that there was an expectation at the start there that there was going to be a lot of development work happening in Switzerland as well and then that never happened also it it kind of uh goes against the charles was fired for wanting to uh make it corporate when every single person filed their own corporate legal entity in an attempt to divert the funds to their own personal power structure"

**[1:04:54] SPEAKER_03:**
"Yeah, I'll add, because I was in the room for some of this. Gavin immediately started talking about brain drain when there was to be no crypto Google. Um, so I, I guess like they, for, for a long time, they wanted to do hybrid for-profit, uh, nonprofit and, you know, the, the protocol sits in the not-for-profit and, you know, for-profit tries to commercialize and yada, yada, yada. And of course in the end, everyone's like the tokens were worth more than probably any equity would have ever been worth. But, um, but yeah, I think, I think the, it's, it's definitely a mix of factors. I think it's primarily what you said, but also, you know, like the, I think while there's just a grossness to Charles, like, I guess, okay with being on record on, I think there was also a dev guy, business guy divide that to your point on like the autists, right. You know, not that they were great at business like Amir Charles, but there was more of a like, what do you do? And some of what they did was like, try to set up deals with the Canton of Zug and then do like other business developments, etc. That kind of was lost afterwards. I'm not saying it was all that effective. In their hands but, uh, there was this like BD commercialization gap and so, yeah, to your point everyone then started their own companies. ConsenSys being the most successful of them and kind of filling that sort of business guy plus commercialization role from there on. You're saying the guy with the most business experience did the best so it seems like"

**[1:06:43] SPEAKER_02:**
"What's funny when I met your dad, uh, in the Miami house, I just thought he was somebody's dad. I mean, obviously in retrospect, he was yours, but, uh, I didn't know that he would go on to become Joe Lubin. You know, I just remember like shooting shit with them and talking to him about thoughts and stuff. And he was real like quiet and, you know, told me about his time making music videos in Jamaica or whatever."

**[1:07:09] SPEAKER_03:**
"Yeah, that was right after that. He also, for a time, he believed that he would be a software developer for Ethereum. And then I guess he realized... like no one knew anything about business and uh yeah you know he does he doesn't have you know a tour in corporate from the i.t side and then run a hedge fund so he the most understood how things worked I guess yeah much better than everyone else. I knew how to, uh, exist in a early stage startup because I've been doing that for 10 years over and over."

**[1:07:44] SPEAKER_02:**
"So my major contribution was not saying, have you guys ever heard of a four year vesting period? I thought it a bunch and I was like, I don't want to be here for four years. I'm not going to say that shit."

**[1:08:01] SPEAKER_00:**
"Yeah. I mean, it's something which I've seen people comment on a fair bit is, um, you know, the, the early contributor slice of, which was 9.9% of the Ether, which was shared between the people who did contribute over those 10 months or so, is equal to the amount that the Ethereum Foundation received. So all of the developments of everything which happened after that July to the current date has had that same bucket. And, uh, you know, that is not a typical kind of uh setup for you know long-term success talk about the best thing you know that uh as I as I look through a lot of these early people uh you know they they did their part and they moved on yeah but it would be nice if some people hung around some more"

**[1:09:06] SPEAKER_02:**
"Yeah. I mean, I think to some degree, that's why I'm still here in this space, that, and the guilt of learning what people do with the things you create and feeling some sort of like responsibility to kind of try to nudge it in a direction, you know, but balancing that with my desire to be anonymous to the most degree that I can was difficult."

**[1:09:32] SPEAKER_00:**
"Yeah. Yeah, for sure. I mean, it was something which came up, I think, through sort of 2018, 2019 as well was the foundation stiffing developers, essentially."

**[1:09:48] SPEAKER_02:**
"Yeah, I don't know. That didn't happen to me. Praise Vitalik."

**[1:09:53] SPEAKER_00:**
"No, no. It's all right for you early, guys. But... But yeah, what else they have noted? Something which you've spoken about a little bit on Twitter as well is sort of like purges and palace politics and so on. Can you speak a little bit to about the nature of the foundation and the opaque nature of it and these kind of palace politics that you have going on? What's happening there?"

**[1:10:26] SPEAKER_02:**
"You mean in the last 10 years?"

**[1:10:30] SPEAKER_00:**
"Right, right. I mean, because it's quite a contrast, right, in your Coinbase article, you were speaking about the contrast, right, between your open, decentralized, collaborative space and the foundation as an entity."

**[1:10:46] SPEAKER_02:**
"Yeah, so I think that it's difficult because if you look at, you know, this is my personal assessment, how I think about the situation. If you look at the early days and and you take all that political shit seriously and you realize that Vitalik's basically like a 18 year old kid in the middle of this like I was under prepared for the political shit but I wasn't even like the center of it you know Vitalik had to be pushed into this weird situation where all these sharks and snakes were around and where Charles is acting some type of way. Um, and then everyone else around him is, is vying for power and that's a lot of stress. Right. And so if I was thinking of it from Vitalik's perspective, to me, my primary goal for myself would be to insulate myself from the, those political games to, to the greatest degree possible. Right. And so, you know, In some ways, it's kind of like the requirement to stay sane and the requirement to insulate yourself from people playing these games and trying to get to you is that you kind of have to anoint yourself king and do the thing that Charles did, which is surround yourself with people who are going to basically have like fealty to you, right? They're not there because they're trying to manipulate you or get one over on you. They're not there because, you know, they're not playing games behind your back that you're going to have to deal with. And I think that if you're trying to focus on your goal, you know, in this kind of like foundational structure, I just assume that every, every decision that's been made in, in the structure of the foundation is, is, based on kind of two principles, one is kind of the the amorphous notion that, like a decentralized project shouldn't have. Centralized control structure and it, you know there's really some sort of kind of suicide urge that I see in the way that they structure it like it could be an organization that exists for you know. A thousand years if they organize it correctly but they're they're trying as hard as they can it seems to make it disappear and I think that that's like incredibly misguided I don't think there's any historical um examples of anything like that happening and I think that if the foundation disappeared tomorrow then all those power game you know the power vacuum would just create fucking infinity of those power games until somebody stepped up and Ethereum becomes whatever the person who can kind of get that power position. So I think that, unfortunately, from my assessment, Vitalik's need to keep himself sane and protected has not been done in such a way that the Ethereum Foundation necessarily serves the long-term survival of Ethereum. It just, like... that that's a major concern for me. So I don't, I don't, I think a lot of people might criticize the way it's structured for reasons like, but I understand, man, like I'm not Vitalik and I've had to deal with, you know, those power games and they drive you crazy, man. They get in your way. They keep you from being able to focus on what you want to focus on. And I think not coming up through the traditional, um, kind of like Silicon Valley group. When you come up in that, you're surrounded by people who have been in it and have survived for a long time. And they understand how to support founders and they understand how to legally orchestrate these things. And I just don't think that he had those people around him to protect him. So I don't know. Kieren, you got something to say?"

**[1:14:56] SPEAKER_03:**
"I wanted to compare Ethereum with Bitcoin, which I've seen some of the similar governance issues on Bitcoin, but it's different. Right now, it feels pretty technologically stagnant. At a time, I knew a bunch of the core devs. We had a funny meetup once at a Berkeley restaurant and a couple of them showed up. And it's... you know, Bitcoin technologically just doesn't really change, but there was a time where people were kind of, it was a foundation and they were acting in a coordinated manner to popularize Bitcoin and so on. And now it feels like those people are largely gone. Um, there, there's, a, a lot of the work, um, that adds functionality to Bitcoin uses Ethereum or an L2 or an EVM or what have you. And people are just kind of focused on the price action pretty much. And that's been, I think, a benefit to Bitcoin. But I guess like... I think Satoshi kind of went through something similar. And I think he was starting to get pretty irritated from, there's a good book covering his Bitcoin talk posts and how that started to feel over time. And then obviously he disappeared when he disappeared. I'm just thinking like, is the Ethereum way better? I think like probably it is. It's not optimal for sure. Like later projects run much closer to Silicon Valley tech companies and like have the open source part where the open source parses, but are pretty strongly governed so far as I can tell. But no, I think I also say like there's probably some merits to the approach. Like it was so decentralized that lots of people could come in and"

**[1:16:50] SPEAKER_02:**
"try to make it their own and that there was a plus to that too and just the downside being the chaos. I don't know what, what do you think about this question? Yeah, I mean I think, can you hear me? My little thing is not showing. You're good. Okay. Um, yeah no I think you know as far as the foundation being set up in the beginning it's it's whatever what it's become is whatever too because it could they could change into a structure that supports Ethereum for the long term. But yeah, I'm more focused on today. But I do think, you know, I always thank your dad every time I see him for all his work, because I do think he's filling a role. And if there is a power, again, I think if there is a power vacuum, you know, I think he will be standing around to at least mitigate it. Um, without him who knows but the the thing about the Bitcoin thing you said is like that's what I'm concerned is going to happen to Ethereum is you get to a point where it just becomes this kind of like not coordinated thing where everybody's arguing and nothing happens right and nobody can make a decision because at the end of the day like groups don't make decisions you know groups don't create greatness like that's just that's just not what happens you know like you have you have these kind of visionary geniuses and if they manage to like find the right idea and the right group and they're supported and they have the time and energy to do it, um, then then it then it moves forward. You can you can even look at like a more structured version, version like Apple. Um, whereas you know, Steve Jobs had set up a massive corporate structure and it still exists to this day and the vision is gone. Right. So once, once the kind of visionary is separated from the vision and once the, you know, it's, it's going to default back to the level of the organization. And if you're, if the goal of the Ethereum foundation as stated is to make itself irrelevant, like, I mean, that's so frustrating, like, man, we created this technology that could potentially allow you to, it could, it could potentially allow, this technology could potentially allow you to create entire governance systems and corporate structures or whatever that could persist on the blockchain indefinitely with all kinds of mechanisms. And like, what the fuck? Like, is that not what the Ethereum Foundation should be doing? Should they not be like eating their own dog food? Should they not be doing what we said we were going to do? Should they not be funding that? Like, I mean, how many esoteric scaling solutions can you invest in, right?"

**[1:19:46] SPEAKER_00:**
"Yeah, I mean, from my perspective, I think the change of leadership that there was this year with Tomas coming in as a co-ED has made a world of difference, that they have become more transparent than has been the case before. And I think that he, as a Nethermind company CEO because he's the the CEO of of Nethermind as well I think has given him that kind of like product holistic getting done kind of perspective that hasn't before and he's got the credibility of having been in the ecosystem as well right and having gone from hey we're we're a"

**[1:20:37] SPEAKER_02:**
"you know we're a little company doing an Ethereum client to you know a really large kind of player that do all kinds of things yeah and i think there hasn't been that before you know he is a CEO type he uh he was i did a call with him we talked for a bit and he seemed great asked a lot of questions and said he talked to over 100 people and I gave him some of my thoughts and criticisms and I don't know. I've, I've seen a lot of the things that we've talked about kind of playing out. So, you know, I hope, I hope he can be a force that persists again. You know, if you have the palace politics, there's always the people like that. They're always in danger."

**[1:21:25] SPEAKER_00:**
"So there might be another coup."

**[1:21:30] SPEAKER_02:**
"That's what I'm saying. Like, You could be the best guy with the best intentions, with the best ideas, and you're the guy to do it. And if the power structure is designed around placating people who are only concerned about their place in the palace, um, you know it's happened to me multiple times in my life, uh, they kick you, they kick you out because you're a threat to what they're trying to accomplish in their minds, um, they don't understand that you know if you allow the guy the guy who is doing this to to really create something that lasts and is bigger than you're going to get a bigger piece of a bigger slice from a bigger pie but if you completely undermine everybody who's trying to do that then you're going to end up with a nothing you know"

**[1:22:30] SPEAKER_03:**
"there's a mechanism for a coup I assume like in practice the foundation is like you know kind of doing whatever the people who work for it want to do but in the end is a dictatorship of Vitalik at the end of the day like yeah so yeah the only mechanism I see is the people who have Vitalik's ear get in his ear long enough that"

**[1:23:00] SPEAKER_02:**
"it's not working. So to some degree, there might be a community capacity to be a louder voice consistently to ensure that there will be backlash if anything like that happens."

**[1:23:21] SPEAKER_00:**
"Yeah, I make this the sick epoch that there's been. So we had white paper to web red red wedding where it's essentially you know just no formal structures really you know emergent then you have the the period of the uh of the Ethereum Foundation and FDev so that was July 2014 through February 2015. Then he had the interregnum where you you were whopped which was between March 2015 and June 2015, where you had Kelly... Becker. Kelly Becker overseeing the installation of the new professional, in quotes, board that began the Ming dynasty, where she immediately knocked off all the other directors, and then she had her Three years of tyranny. And then you had the Infinite Garden with Aya coming in in another coup there in February 2018. And then it seems this last one was maybe not so much of a coup as an evolution in that Aya's still around as the president, that you have new executive leadership."

**[1:24:48] SPEAKER_02:**
"Yeah. So yeah I don't know what this period comes to be called but it's it's it's definitely better and more coherent you know I, I'm, I'm prescient a lot of the time and you know I had my encounters with Aya that clued me into the fact that she was not really um qualified or even coherently involved in a way that I would assume somebody uh in her position will be so i was you know i was applying pressure years ago years and years ago and um yeah five years ago six years ago so i think you know eventually the community kind of uh came around to what i've been saying this whole time which is wait like she should be doing like there's things that need to be done and we all see that they're not being done and what the fuck and we can't even this woman is doesn't seem to care and she keeps talking about esoteric poetry and fucking infinite gardens what is this shit you know like fucking do your job. Like, you know, for me, the, you know, I've talked about it before, but you know, their website, the website was like the same website for three years. I had, it was just an informational website. It was a brochure website. And I just messaged her and said, Hey man, we, uh, we need to update this website. I'll do it for free. And she said, oh yeah, I think we have a team working on that. Let me get back to you. So I like kept in contact with her it took her six months, six months to figure out who was working on the website Bob I mean, yeah, like are you kidding me like what are you doing are you sitting and at the beach like sipping mai tais? I legitimately don't know what you're doing because you clearly have no Active. This is how this is what it should be. You should have an org chart. You should fucking know the person to call. You know, you should actually know who's building your website. Yeah. So that was that was just insane to me that you could be the ostensible. Yeah. Running an organization and not even know who to contact to to see who is building the website. And then it ultimately was Josh Stark. I messaged him, said, hey, man, I'd love to help. I'll do it for free. I can have it done in a week. He was like, no, I'm good. I was like, what do you mean? You're good. You're not doing it. Like nothing has happened. It's been six months. It's not something that takes six months or a year. Anyways, it was like a year later, they finally launched a year and a half later."

**[1:27:23] SPEAKER_00:**
"So there was a longer tweet thread, um, of me ranting a little bit. Well, it wasn't very ranty actually. It was quite polite in, in late, uh, in late, it was December, 2017. And Hudson tweeted out something like, hey, what could the Ethereum be doing better? It was something like that. It's like, ah, well. Oh, my God. But my list was very simple. It was like, yeah, the website, shit, useless, doesn't do anything. There's no information, nothing there. You know, nothing useful there. Also, there's no public information on the Ethereum Foundation. Like, you know, who... Who are the board members? How does voting work? Who are advisors to the foundation? What teams are there? Who works on these teams? There wasn't even a grants program at that point either. It was just basically, you just have Ming and Vitalik and she had hired on Jamie Pitts and Hudson. So there was a little bit of extra help. But essentially it was that thin little bit of overhead and a bunch of devs. And that was what there was. And she couldn't delegate either, Ming. So just nothing got done. Like really just nothing got done at all."

**[1:28:52] SPEAKER_02:**
"Um, yeah, I mean, I don't know in retrospect if I had known that I mean I know you said she was a nightmare but she did offer to hire me back into the Ethereum Foundation but I, uh, I didn't feel I don't know it was a time where I didn't really feel like uh working I'd been a little burnt out from the previous few years so um yeah you know maybe if I'd accepted that"

**[1:29:19] SPEAKER_00:**
"She should have Minged you. Don't worry, you wouldn't have lasted long if she came back."

**[1:29:24] SPEAKER_02:**
"Maybe, maybe, maybe. Everyone got Minged. If she was like Stefan, then yeah, that high energy, like stress stuff. But I don't know. I was a little bit more."

**[1:29:35] SPEAKER_00:**
"But yeah, I mean, you know, so I think that was the problem, like that. You hadn't got enough people to get anything done, you know, like what you talked about with AYA. That was a case in that earlier era as well. There wasn't really no organizational structure and nothing really much was happening beyond the developers doing their development. Oh, and, you know, we'll do a DevCon now and then."

**[1:29:58] SPEAKER_02:**
"Yeah. Well, you asked about the palace politics thing and I just had a memory, you know, people it's, it's much less now than it used to be, but to some degree people still keep me in the loop when, you know, they know things. So I think maybe the biggest problem with the, with the way that things are structured right now is that there's nobody to give pushback. And there's no dissenting voices and there's a, like a, very homogenous group of people, homogeneous, whatever the word is, a group of people who aren't going to step out of the party line for any reason because they're going to be afraid of being pushed out. And I think that's not necessarily good. Obviously, you can't have people following you around who think their only job is to undermine anything you say but really I mean you need you need voices that will speak the truth um even when it's uncomfortable because you know decisions may they have they have outcomes and having a bunch of people who see the world in the same way and um aren't really thinking of of things holistically or from different perspectives you know it's going to create issues"

**[1:31:24] SPEAKER_00:**
"At the recent FCC in Cannes, there was a slide which Jerome had on there, which was talking about dissenting voices. And both myself and Greg Colvin were up there as Ethereum dissidents."

**[1:31:43] SPEAKER_02:**
"I didn't get it. It's all right. Nobody remembers me. Congrats, though."

**[1:31:47] SPEAKER_00:**
"No, sorry. You're not being loud enough. I don't know. Oh, no. You're not being loud enough."

**[1:31:55] SPEAKER_02:**
"No, it's all right. I only have the number of followers I do because of a couple of jokes I made, one of them being Texture Punks. I very much don't mind being lost to history if it means I'm not on someone's let's rob the sky list."

**[1:32:14] SPEAKER_00:**
"Well, I think that's maybe a good kind of place to wrap up. Yeah, don't worry. So I wish you all the very best and enjoy your life."

**[1:32:29] SPEAKER_02:**
"Yeah. Well, Bob, thanks for having me on. If you want to have me on again, I'm more than happy to always give you my time. Good to talk to you, Kieren."

**[1:32:39] SPEAKER_03:**
"It's been not too long. Great to chat again and we'll do it again soon."

**[1:32:48] SPEAKER_02:**
"Maybe so. Maybe we'll see you soon. Thanks for everybody who's come to listen. Don't follow me."

**[1:33:00] SPEAKER_00:**
"Thanks a lot. Texture is IamTexture on Twitter. Have you got any other questions?"

**[1:33:07] SPEAKER_02:**
"Websites or anything places that you'd like to point people? No, I'm not. No, just okay have a nice night have a nice day whatever you're at morning thanks so much. Okay cheers everyone bye"**[01:19] SPEAKER_03:** Can you hear me?

**[01:27] SPEAKER_01:** Can you hear me? Yes, I can. Excellent. Happy Straddle Spaces. GM. What's up, guys? How are you? I'm good. First week of September. I'm not sure if it's officially the first week of fall. But nevertheless... Super excited for a new month. I know at Strato we have a very exciting month ahead.

**[02:25] SPEAKER_03:** I think technically fall starts on the 21st or 22nd, but spiritually it starts after Labor Day, of course. I don't know if anyone has a white suit, but I actually sort of have a white suit. And you can no longer wear those already.

**[02:56] SPEAKER_01:** I might have to see that. White suit's pretty nice.

**[03:02] SPEAKER_03:** I may have a photo. I think it's been worn to two sort of summer weddings, and that's the only time it's been. But I could probably dig one up for you, Jamie.

**[03:16] SPEAKER_01:** Yeah. Text, you're welcome. We had him, we lost him. Give it a few more minutes for some more folks to pile in. Yeah, yeah, Spiritually Fall is here along with football to the behest of our European counterparts.

**[03:55] SPEAKER_03:** By the way, for Spaces Resiliency, ChatGPT is recommending two co-hosts up front. Now, do we already have the two, or can you add another one?

**[04:06] SPEAKER_01:** Yeah, you and Bob are co-hosts.

**[04:10] SPEAKER_03:** Okay, it just appears a speaker to me. Maybe it appears as co-host to Bob on Bob's side. Bob, are you a co-host successfully?

**[04:18] SPEAKER_00:** It appears so.

**[04:20] SPEAKER_03:** I see it now. Okay, fantastic.

**[04:33] SPEAKER_02:** Can you hear me? All right, cool.

**[04:35] SPEAKER_03:** Wait, very, very kind of cool August for those of us who spent some of it in New York. August is supposed to be hot, and it mostly wasn't. There's supposed to be a sharp transition heading into the fall, but it feels like it kind of started early this year. I don't know what's going on.

**[04:57] SPEAKER_01:** Yeah, completely agree. A lot of long sleeves and sweatshirts during the night. Cooler, you guys are old? Been around talking about the weather? We're waiting for you. Well, I'm here. Even better. Welcome. What's up? GM. Yeah, great, great to kick this off. Um, I'll hand the mic over to Bob, but I just want to pay my compliments to your PFP Texture. It's quite a good one.

**[05:37] SPEAKER_02:** Do you own a Texture Pumps?

**[05:40] SPEAKER_01:** I do not, but I saw a few folks with them and obviously noticed yours, so might have to get one.

**[05:51] SPEAKER_02:** It was a joke cause I thought punks were ugly. So I made myself a better one. And then a friend asked me to make her one and then somebody else asked me to make one. And then like 30 people later, I was like, I should just fucking make a little thing where they can make their own. And then, um, uh, then, then my buddy started a Discord and 10,000 people showed up and I was like, look,

**[06:15] SPEAKER_01:** That's some good lore.

**[06:16] SPEAKER_02:** That's some great lore right there. I thought it was going to be me and my hundred friends.

**[06:26] SPEAKER_00:** Accidental success. Fantastic.

**[06:32] SPEAKER_02:** Great.

**[06:32] SPEAKER_00:** All right. Well, let's get going. So hi, Texture. How are you?

**[06:39] SPEAKER_02:** It's been a while. It's been a long time.

**[06:44] SPEAKER_00:** Always good when I think of you. The first thing I think of is love. Oh, and something I've spotted going through making my notes is your Medium is called Peace Love Revolution. Yes. So what's the story there?

**[07:05] SPEAKER_02:** So you know, uh, I was kind of I wouldn't say a hippie. I didn't dress like a hippie. I didn't really hang out with hippies, but I I took some psychedelics and when I was a kid and I had some experiences and uh, you know, kind of drove my passion for uh, you know, doing good things and spreading love in the world. I know people that probably follow me are like, what the he just calls people retards all day, uh, yeah but I mean, I'm on Twitter. I don't know. It's full of retards. Um, so I started this group called Peace Love Human because uh, I was like sitting in a shitty basement apartment in San Francisco and uh, I was watching the news and I was seeing how religions got all fucked up and I was like, what if there was like a religion that didn't have any beliefs and we just went out and did nice shit? So for like three years of my life I was just like homeless and had no job and wanted to setting up like free hug events and like other stuff just to make people smile because like, you know, making people feel loved or making people happy was not like a quantifiable metric, but making people smile was. So that was that was what I did for my early 20s. So that's what I was doing, the community building. I accidentally started a cult. And when I realized that it was a cult, I shut it down.

**[08:30] UNKNOWN:** Okay.

**[08:31] SPEAKER_02:** But it helped me. It was my first foray into cult building, which obviously...

**[08:36] SPEAKER_00:** Right. Very useful.

**[08:38] SPEAKER_02:** I took into my role in Ethereum, and I feel like the Ethereum cult is going pretty well.

**[08:43] SPEAKER_00:** I seem to remember at some point you told me that you've probably hugged a thousand random people on the street.

**[08:50] SPEAKER_02:** Oh, a thousand in a day, probably. Probably a hundred thousand more. More. Yeah. It was nice. It was, it was good. I mean, I could waste this entire thing telling that story. That's probably not what people want to hear.

**[09:12] SPEAKER_00:** I mean, I can see why Decentralized Dance Party also appealed to you on that score.

**[09:18] SPEAKER_02:** Yeah, so DDP, Gary, the guy who runs that, he came and stayed at my apartment in Brooklyn, and we had this three-story loft in a warehouse, and we'd let people come crash, and he came through, and that's how I met him, and I've done three or four of them. I was... What is it? It's Tom. I was Tom. So Tom is like a rotate. I was Tom one time. So that was fun. I had to shave my beard. I had a mustache. I looked funny.

**[09:55] SPEAKER_00:** I'll drop some links on Twitter for that for anyone who hasn't seen Decentralized Dance Party or you can go and have a Google on your own. It's quite exceptional.

**[10:07] SPEAKER_02:** It's funny. I had no...

**[10:11] SPEAKER_00:** Didn't really understand the decentralized thing at that point. I was not really involved, so that he was kind of ahead of the curve on that with me for sure. So yeah, that's Gary Lachance, who was a fellow Vancouverite with me. Um, he was, uh, funnily enough, in, in, in a photo for the very first item I could find about Vancouver Decentral. Know the whole, uh, Decentral Toronto, Vancouver thing. Gary was in that photo for the first one. Maybe well known as well now, but for Dogecoin. So there is the Dogecoin-wrapped McLaren which, uh, travels around many, uh, many conferences where they can get, uh, financial support for that. Um, yeah, Gary's a great guy. It's pretty fun. So tell me about the vision that you had, which was then the same as the white paper, because on the Twitter thread, I was wrongly saying your mind was blown by the Ethereum white paper, where actually what happened was that you'd had a vision of this about a week before, and then the white paper landed on your lap. So what the hell was that about?

**[11:40] SPEAKER_02:** Yeah, so what actually happened was I had a roommate for years ago, like years when I lived in New York. And he had tried to get me into Bitcoin when it was a dollar. And I said, this is like internet nerd money. I'm like a love revolutionary. I don't give a shit about this. And then he kept bothering me about it for years. And then it hit $1,400. And I was kind of humble enough to be like, well, if other people think it's worth something, I guess it is. But he had texted me and he said, listen, man, I want you to listen to this podcast. And it was the Let's Talk Bitcoin podcast with Adam B. Levine and Andreas Antonopoulos. And so I had given up working in tech because my arms had given out. I was a programmer and designer for a very long time. And, uh, I had, I started making cannabis edibles in California because it, uh, it seemed like a, uh, an industry that was going to be, um, some pretty easy to get into like the marketing, the production, everything was shit and I was pretty good at it. So, uh, yeah, so I had, I had a girlfriend who was about four hours away, uh, and I would go visit her on the weekends and I, so I threw the Bitcoin podcast on, I ate one of my candies and, uh, Don't drive stoned kids. But yeah, on the way there, I was listening and listening to the podcast and my, my brain is kind of tuned in and I had, I like, what could I, I can only describe as like a biblical vision. I would say like before that, I wouldn't have understood what that meant, but like, just this massive data download into my head where I can see, like basically see the future, like visually, like I just saw the whole thing playing out in front of me. And I was like, Oh shit, you know, Bitcoin, I'm still not particularly fascinated by, but the blockchain, um, this idea has an amazing amount of potential. And I kind of saw how it could help people coordinate. And so it just kind of it struck me so much that I was like, I got to go talk to Adam. I got to go meet the people who did this podcast because at that time it was the only Bitcoin podcast. And I thought anybody who wanted attention for what they were doing would probably contact them. So the buddy that had told me to listen to the podcast randomly came into town three days later. And I said, hey, man, I've been thinking a lot. I listen to the podcast. I have a lot of ideas. I need to meet Adam. I need to meet. And he goes, well, actually, I'm flying out in a couple of days to go meet him. We have a meeting scheduled. He's in Washington celebrating his birthday with his wife. And I said, no, no, no, no. We're getting in my car right now. I'm driving. I'm driving us there. I'm going, I'm going to go talk to him. And he's like, what really? And I'm like, yeah, fucking cancel your ticket. Like we're getting my car right now. So we drove like 20 hours or whatever to like Washington state. I walked in pretty much. I don't know what their meeting was about, but I pretty much just took Adam to the side and we ended up sitting in his hot tub on his balcony for like, nine hours just talking. And it was a really cool discussion. And I said, what I want from you is I want you to tell me anybody you know who's working on anything like this. And he said, well, do you know who Vitalik is? I said, man, I'm not in crypto. I'm not in Bitcoin. I don't know. I don't know anybody. I don't know anything. Um, and he said, uh, well, he just sent me this white paper a few days ago. I can like, I can forward it to you. Um, and can you guys still hear me?

**[15:23] SPEAKER_00:** Yep.

**[15:24] SPEAKER_02:** Yep. So then, um, yeah. So he forwarded me the white paper. I looked at it. You know, to me, it wasn't as comprehensive as the vision that I had, but I thought, you know, this is kids met, you know, right. Like what are the chances that all of this stuff lined up like this? So I said, yeah, make the intro. And so we started a Skype group and, you know, Adam was there. I remember Charles was there. Vitalik was there. I was there. It became the official Ethereum Skype group and just kind of grew from there. So, you know, it was like... Was that water cooler? No, no, no. Water cooler is something I made later because people... That was later. Yeah, so that was just the the literal like main ethereum skype channel that we used to communicate for the first i don't know long time. Right. No, water cooler was something I created later because I actually don't remember why. I guess I was kind of like...

**[16:27] SPEAKER_00:** I guess it's off-topic or whatever, probably. Off-topic chatty thing.

**[16:31] SPEAKER_02:** Maybe, but I was kind of like the dude that everybody trusted. And so whenever anybody wanted to talk to somebody, they would come talk to me, which is why I got so much information about what was going on all the time. But yeah, so I think it was just an extension of that. People talk to me all the time when we create a little place for us to shoot the shit.

**[16:51] SPEAKER_00:** So when do you think you had that trip to Washington? When do you think that would have been?

**[16:59] SPEAKER_02:** I'm horrible with time and dates, especially during that time, you know, when you're like a free-flowing hippie dude. Yeah. But I would say it was the week after... the week and a half after Vitalik sent the white paper out to his original group of people to get the feedback on.

**[17:22] SPEAKER_00:** Yeah, so it might even have been during November still.

**[17:27] SPEAKER_02:** Yeah, I mean, it was as early as you could get. I mean, just by happenstance, just by the timing I was there, basically the moment we were coming together.

**[17:38] SPEAKER_00:** Yeah, yeah, it's amazing. Cause yeah, so I was able to find that, uh, the video of, of you and Vitalik at the, uh, at the salon, uh, which was, uh, beaming into the Vancouver Decentral there. And that was December the 15th. That was. Yeah. You did that one.

**[18:00] SPEAKER_02:** Yeah. So we had been, yeah, I mean, again, the timing, the timing, I don't know, but yeah, obviously by that time we had been doing it for a minute.

**[18:11] SPEAKER_00:** Yeah. I mean, the funny thing was looking at that, that's before there was any code, any public code at least. There wasn't even any Python code from Vitalik published at that point. Gav and Jeff were weeks away still.

**[18:25] SPEAKER_02:** Yeah. And Jeff, to my understanding, just read the white paper and started coding it up on his own and said, hey, I've got this Go implementation.

**[18:34] SPEAKER_00:** Yeah, pretty much. And the same for Gav. They were both at the very tail end of December, basically like a Christmas project kind of deal for them, for the pair of them.

**[18:45] SPEAKER_02:** Yeah, no, it was great. You know, and I've been a developer my whole life since I was a kid. Um, and since I had quit coding, I wasn't really sure where I fit in, you know, but I was really happy when all these other people like got in, I guess maybe if I had dropped some code and gotten a lot more ETH, that would have been cool, but whatever.

**[19:08] SPEAKER_00:** So, I mean, to you at that point, like, what was Ethereum? Like, what was this vision? And what were you thinking that that could unfold to be? You know, what was the kernel of that?

**[19:28] SPEAKER_02:** Yeah, so, I mean, it's so hard to remember those days. There's so much on top of it now. You know, I remember the general vibe was just, a technology that would allow people to coordinate, to, to encode value to, I mean, you know, like just at all dimensions, things that haven't even come to fruition yet, things that people aren't even thinking about because like, so much of it has gone to scale, just like fundraising, fundraising locally, like just coordinating anything. I mean, it was, it was just the whole world, like just imagining every single system being replaced by this decentralized coordination structure that, that gives the, the, you know, some, some 11 year old kid and, you know, Bangalore could create the next, you know, technical development. And, you know, I think that kind of platform is just something that seemed really empowering. So, you know, a lot of idealism, you know, obviously real life as it's played out is a lot messier and a lot different from how we imagined it. But a lot of idealistic things, a lot of like very much, uh, just, just really coordination. And that's a really shitty description of the vision that I had because it was so deep and so multidimensional and, um, but yeah.

**[21:02] SPEAKER_00:** Social operating system is something I've seen you say on a few occasions.

**[21:06] SPEAKER_02:** Yeah, I mean, yeah, just there's so many dimensions to it. But yeah, I mean, a social operating system for allowing people to encode their values or encode, yeah, literally their values, anything with value, creating incentive structures, contracts that are enforced at the exact level that they were designed to. Which none of that sounds really technical and unsexy, but to me it was really about the impact. What happens when you empower people to be able to create value in their local communities or encode value in ways they haven't been able to? What happens when you know, the equity in your company can be easily traded, you know, just all these things. Just so what happens when you can do that to houses and local businesses and local communities?

**[22:09] SPEAKER_00:** Yeah. I mean, I'm thinking my own sort of thinking in those early days, it was an awful lot about empowerment and about, you know, giving, giving people the ability to control their own destiny. Right. Yeah. Um, and, and something I repeatedly thought was, was like, um, if you think about the, uh, what's it called? The pyramid of needs. What's it called? I forget the.

**[22:34] SPEAKER_03:** Maslow. The hierarchy.

**[22:35] SPEAKER_00:** Yeah. Maslow's right. Maslow hierarchy of needs. Know, I remember a number of times saying, you know, it's frankly obscene given all the resources that we have in the world and how, you know, how, how much more there is than was in previous years, it's obscene that people should be like worried about housing or education or health care or, you know, just these basic things, right. Yeah. And how wonderful would it be if you could like yank up that base layer a little bit so that people are not like living in this fearful place of powerlessness but instead can be like not worrying about that and not having to make these compromised bad decisions and everything, yeah. Just if you could do what you love. What, what a world that would be. Yeah. And I'm a lot less idealistic about it now after

**[23:39] SPEAKER_02:** The last decade for a lot of reasons, but you know, the marshmallow test is real and you can create really good technologies and really good user experiences and as many guardrails as you can for people. But at the end of the day, there's motherfuckers that are going to eat the marshmallow before they even hear the rules, you know, and then they'll do it again and again. So, you know, I think there's a lot of, it's not that I think the problems are unsolvable, but they're, you know, the idea that, it's something from above being imposed down. You know, despite the fact that the system seemed to be that way, I think a lot of it is just the, the, the level of complexity of modern life relative to the average intelligence is it's just, it's, it's a wide gap and there's a lot of, I mean, I could talk about that for fucking 10 hours too. So yeah,

**[24:37] SPEAKER_00:** Yeah, well, I mean, something that I saw in those early days of Ethereum as well was a real kind of almost like allergic reaction to anything that looked like organization or hierarchy or structure. You know, just like this total flip to the opposite side, right? Everything's got to be flat and open and, you know, everything, everyone involved with everything, which is just completely impractical for actually organizing or doing anything. Um, yeah. Yeah. It's just, it's just nutty. So, but then it's like, I realized it's like hierarchy. Isn't the problem being tracked in a hierarchy where it's to your detriment and you can't get out is the problem. Yeah.

**[25:25] SPEAKER_02:** Yeah. And a lot of, and I think a lot of times what happens in that is smart people, you know? Smart people aren't really, they don't really understand not smart people. And so what happens is we, we are born into a world where these preexisting hierarchies exist and they've, you know, to some degree or another, you know, kind of persisted through, through generation after generation. And then we come in and we're like, why am I at the bottom of this hierarchy? I'm smart. We're all too smart for this. And then they try to like, know they try to create new systems assuming that everyone is approximately like them and then, you know, I've, I've been through so many because again coming through the hippie I was in the bay area for a long time you see so many people think that they're the first person ever think of flat hierarchies and how it's going to be so much better and at the end of the day man like that's fine if you want to talk all the time and you want to argue and you want to get nothing done but at the end of the day you know a hierarchy is an information structure and it's also an accountability structure and so as long as there's accountability at the top and as long as the information is flowing correctly and as long as the outputs are you know optimal to some degree then it's the best you're going to get and it's, it doesn't mean we can't continually improve obviously life gets better and we, we have an obligation, you know, I think when you're creating things, it's not just the creating things. And I think this is a big problem that still exists in crypto. People think if you build it, they will come. You can't just build it. You have to build it and then you have to make it a button, a single button. It has to be so simple your grandma can do it and not destroy her life. And so it is this kind of perpetual attempt to take these complex structures, simplify them so that everyone has access to them. But through that simplification, not creating these kind of hells that no one can get out of. And I think... Just because of the rate of technological development and the nature of economic progress, our opportunities as people trapped in those systems is to build new systems. But ultimately, we're going to come face to face with the reality of why those systems were set up the way they were and understand that. The best we can really hope for in most instances is an optimization of that. We can try to make it simpler, more efficient, better and more adaptable. But those are a lot of dimensions that any one of them out of, how to out of sync is going to is going to create either more problems or the system itself will collapse. Right. And, you know, if the system doesn't exist and nobody gets, nobody gets anything.

**[28:19] SPEAKER_00:** Yeah. I mean, I guess it's a little bit analogous to sort of technical death and things in code.

**[28:39] SPEAKER_03:** Yeah.

**[28:39] SPEAKER_00:** If you've got code and you're like, Jesus, look at this. It's so much like complexity and these conditions. I don't think we need any of that. Let's just take all that out. But, you know, someone did that for a reason.

**[29:15] SPEAKER_02:** Yeah, and I, you know, after I became a father, I became really a huge proponent of the idea of if you think a stupid rule exists because the person who made it is stupid, you haven't thought through the problem. It isn't a bunch of people. I'm not saying this has never existed, but it's not like some nefarious guy at the top who wants to just ruin your life. It's some fucking idiot who did some idiot shit. And then now you got to make a stupid rule. You know what I mean? And you got to enforce it with fire. Otherwise, you know, your kids end up dumping plates of food in their closet and you find it six months later. And so, you know, it's, it's just that at scale.

**[29:59] SPEAKER_00:** You're gonna have to keep me on topic as much as you want to because I am a meanderer. Yeah. Um, on on this human side something I, I talked about, um, during my, uh, maple syrup peace phase was, was neurodiversity and the fact that, uh, normies would not be involved in the early phases of such a project, right. It's absolutely crazy to go and do what you did. Yeah. It's crazy what most people did. Um, so how does that play out the fact that in these frontier Technologies you don't have normal people? Well, you do, but you have a lot of, uh, of us people who would not fall into that category. So how does that all play out? What do you think is happening there?

**[30:57] SPEAKER_02:** I think it's just the structure of how things have always occurred, right? So you have these kind of people on the front edge. And I was on the internet from, know, I remember reading when the HTML 2.0 spec was about to come out, right. And so the early days of the internet it was that and so I was on the internet all day talking to people and you know there was a technical barrier and and it's just you have these kind of neurodivergent people show up. So in the early days of crypto it was a lot of people who are paranoid, a lot of autistic people and a spattering of sociopaths who kind of could see that they could make money. And so that has a profound effect on how things play out. But I think it seems the way that at least in capitalism, what happens is huge amounts of capital come in and it just becomes this kind of probability matrix of, throw as much energy at this thing as you can on the front end, and then whatever survives is going to play out. But if you look at something like Linux or open source technology in general, it's very autistic. And autistic people have a very specific, I've noticed, differentiation from the average person, which is they, they honestly like believe that the terminal is the greatest interface of all time. It's like, they don't grasp that most people need buttons. And so it's like, you look at Linux, Linux was kind of a fringe thing only tech people used. And then Google came in and, at least had enough sense to hire some designers to turn it into something functional. Steve Jobs did the same thing with OSX. OSX was a previous Unix variant. And so you need those people. You need those people who come in who are on the edge, who are technical enough to be able to communicate with the technical people and understand. But they also need the clout, the money, and the power to overrule those people because... like Linux had like very horrible user interface and user experience for a long time even when they had window managers and you have to understand I was a designer so I would go into these open source spaces and I, I'm going to tell you what man like these people who for sure would not let you comment on their code and for sure not let you tell you how they were going to structure it or for sure not tell them what language they were going to use have no fucking problem stepping outside of their own expertise and driving a designer insane. You know what I mean? Very logical unemotional totally tapped out of any sense of like what a normal person needs and they they just beat the designers into the ground so you really need somebody who has power and the competence and the will and the desire and can put it all together, um, and, and I, I don't think we really see that. You know what I mean? The wallets suck. You, you know, um, you could, I, I don't know now but you know, like a year ago, I clicked a button and emptied my hot wallet, right? And like, that shouldn't be possible. Like how hard is it to throw up a fucking thing that says, hey, are you meaning to send every bit of this? This is a lot of money. You know, like why does it not just say, Hey, it didn't even say it in dollars. Do you know what I mean? It was, it was obfuscated. It didn't even say there should have been a massive fucking pop-up that said, you're about to send a hundred thousand dollars to somebody. Um, are you sure you want to do this? Yeah. Or, or, or I, as soon as I clicked the button, knew what had happened, even if there had been like a fucking five minute, you know, delay, um, right. You think there's, there's but none of this isn't happening. Right. And be the structure of the organizations or, you know, if the designers are having to argue with the tech people, like whatever it is, it's just grandma still can't use this shit. It's ten years in. If I find energy, I could, you know what I mean? I could like within six months we could we could solve these problems. And I just don't see.

**[35:26] SPEAKER_00:** And I guess. I, I guess this is the reason why things like the ETFs are so appealing, right? Is just, yeah. Can I just not deal with any of this at all? Uh, but I can just like use my Coinbase account? I've already got and it's just a thing that I buy or sell, right. And, and just, you know, it's a proxy for it but most people don't care. Yeah. But that reduces it to an investment vehicle, right. It does. It does. It does, and then that's really a failure, as you say, on delivery of the holistic platform that you do need something which is absolutely better, right? It's just like a product question, really, right? It's saying, unless the product that you are offering is absolutely better than something existing... or is cheaper or gives you some other benefits or whatever, then normal people are not going to use it. It doesn't matter what your worldview is behind that. You've given them something that's worse than what they have, so they don't care.

**[36:39] SPEAKER_02:** Yeah, and so I think exchanges and things like that acting as a buffer, it's a step. Ultimately, how are these things going to be used? The end user is probably not going to know.

**[37:00] SPEAKER_00:** What they're using on the back end any more than the average person knows what processor is in their phone so no no I mean I I guess the hope is it's like a layering thing right that you know in the same ways you've got those DeFi primitives that you're going to layer this you know whatever social recovery or buffered amounts or whatever or insurance for up or all this sort of stuff right that you should be able to put together a stack of things that have an equivalent kind of characteristic and experience to existing things, but without that strong dependence on, you know, a single legal entity that's, you've got that customer service provider kind of pattern rather than just it being raw, dangerous as you experienced.

**[37:50] SPEAKER_02:** Yeah. And I mean, you know, to this day, I mean, I feel anxious all the time because I hold crypto, you know? Me, I feel anxious all the time. You know what I mean? I think we all do. So it's like that's not an experience that the average person wants. The average person wants to put their money in a bank account. The average person wants to click a button and if something goes wrong, to be able to reverse it. You know, we haven't really addressed any of that. Again, it's a failure because the people who are in charge think like, anyone can do what they're doing and it's not that big of a deal. And like, all you have to do is do this and like, blah, blah, blah. It's like another, if all they have to do is click a button, you've done it. That's, that's your metric for success. Click one button and not worry about anything. You just know the thing's going to happen. And if it doesn't, it'll get fixed.

**[38:45] SPEAKER_00:** Yeah. Yeah. So, I mean, when I was looking through, um, sort of different phases of this period that I've been covering in the, um, in the early days of Ethereum, uh, sort of website there I, uh, I was noticing so in, in January in January and February 2014 there's just such a flood of people that came in. I mean, there were a fair chunk in December, uh, but that just really accelerated, uh, through January and February. So, I mean, how did that, like, play out that you've just got, like, tons and tons of people, you know, rocking up and really, like, volunteering?

**[39:34] SPEAKER_02:** It turned everything into Game of Thrones. Yeah. Yeah, that's what happened. It turned everything into Game of Thrones. So, like, I was there day one. I was making sure, like, you know, first thing I did was – um Vitalik posted this website that he made. It was piss yellow. He had stolen some other shitcoin's logo and um, just put Ethereum on it and I was like, please don't post this. Give me till tomorrow. So I like spun up a logo, sent it to him, he was like, oh yeah, this is kind of what I was thinking. I was like thank god please don't put that out. Um, I don't know if I made a website or, and then somebody submitted an image, but the image was like, like, and so just real quick, like what I used to do is I used to be like the dude who, um, dev shops would call when they were six months behind on a project and needed it done in three days. Right. So I was a designer full stack developer. So my, my skill was I could take your idea and I could, I could make it look like it existed forever. And you had $10 million in funding in 24 hours, right. So that was my goal at that point once I realized that that was a massive gap I just inserted myself there and I'm only telling the story to say then when everybody flooded in and especially when the Zug house happened you had all these people kind of going behind other people's backs and um, trying to, um, push people out and take over their roles and it was it was just a very stressful weird time because you just get a different type of person, right? The type of people who show up and are just wanting to build a thing because it's cool. That's the type of person. But when they show up and they're like, yeah, let's fucking let's make sure it's us. Let's make sure we're the ones. Let's like, fuck those people. Let's not communicate with them. So there was a lot of like political maneuvering that was required to survive.

**[41:39] SPEAKER_00:** Yeah, and I mean, I guess that Miami house was where that really dug in. Because that was the first time that most people were physically in the same location out of that set of people.

**[41:52] SPEAKER_02:** It was pretty fun. The weirdest part about that was meeting Charles. And, you know, Charles, he might have been the first person who was doing kind of the thing that I just said, right? Yeah. He just showed up and kind of inserted himself and was like, I'm going to be CEO. He's just a fucking liar, though, man. He was like 24 or something. 25. Yeah, he presented himself like he was 50 years old and he'd been in tech forever. And here's the thing, man. I actually was probably the most experienced in terms of I'd lived in Silicon Valley. I'd worked in multiple startups. But... like despite my personality on Twitter or even if you meet me in person, like I'm pretty humble when I get into a group of people that I can tell have skills. So I kind of just sat back and didn't try to insert myself. I didn't try to like demand anything. You know, I'd be involved in this or that I just tried to kind of be as helpful as I could um so you know when I when I talked to uh uh charles for the first time i was like all right you know this dude's kind of weird like but well we'll see what's up so like literally the moment i met him in miami i shook his hand and i was like oh god he's a sociopath like okay well maybe he's our sociopath you know like every company has a sociopath like maybe he's like a well-regulated sociopath and then when we got to the miami house i found out no no he's not a well-regulated sociopath he's a fucking compulsive liar manipulative weirdo

**[43:37] SPEAKER_03:** I was just going to say, in Charles' defense, at that time, he did look 50 years old. He'd go away with it.

**[43:46] SPEAKER_02:** Bro, when I found out he was like fucking seven years younger than me, I was like, why am I deferring to this kid? He's like, what the hell? Um, so yeah, it was, it was weird, man. Uh, like in the Miami house, I, he just said some of the weirdest shit to me. Um, there was some thing from, I don't know. I won't go into too many details. I've, I've covered them and given interviews to people who have reported on it, but not under my name. So I guess to shield me from any sort of retribution, but I, I, it was weird, man. He just said some weird shit to me. Like he showed me, I'll tell this one cause I've told it publicly a lot of times, but he was like, Texture, come here. And I'm like, what's up? And he's like, check out this text message. And I'm like, okay. And I like just met the dude and he shows me this text message and it's the chick. And she's like, I want to suck your cock so bad. Sorry for any children listening. Um, and, uh, I'm like, why the fuck is he showing me this? And he's like, you know where I met her? I was like, no. He's like, I met her on the front lines of Afghanistan when I was working for DARPA. I'm like, Jesus Christ, dude. Oh my God, shut the fuck up. And so I will say this because it's something that bothers me. Like for some reason, the media all says that the reason that Charles was kicked out was because he wanted to do business and not a nonprofit. And like Charles got kicked out because he was a fucking weirdo sociopath who didn't do anything. Like on above board and like, he couldn't be trusted. He, he didn't, he played games with everybody. Like I was not in his inner circle. Cause I, I did like, he would do, I call him sociopath. That's where like, they say something fucked up to see how you respond. They'll ask you to do unreasonable things to see if you'll do them. And then the people that do them and do them without question end up being in his inner circle. They, they become the people, which is continued on in his Cardano. So like, you know, he he he just operates in such a way that he gets sycophants around him. He lies to them. He gets them into situations where they like loyal to him and they don't question him. And then, you know, just weaves a whole reality around that that isn't real. And that's that that's my assessment of Charles. And he was he was not kicked out because of business. I mean, it was a cluster. Now. Yeah. I mean, no one else was kicked out. Let's just say that. I guess Amir left, but that's another story.

**[46:19] SPEAKER_00:** Well, Amir was kind of kicked out from what I saw based on the fact that people thought he wasn't actually doing anything. He wasn't really, like, pulling his weight or doing anything useful.

**[46:30] SPEAKER_02:** I liked Amir as a person. I haven't talked to him in a few years. We're still cool to this day. But, yeah, I mean, what was his skill set?

**[46:40] SPEAKER_00:** Yeah, I don't know. Biz dev sort of stuff. He said he was... He was talking to people, potential investors sort of thing. But yeah. Yeah. And I mean, in terms of Charles, it took me a lot of years to really understand Charles, shall we say.

**[47:01] SPEAKER_02:** Yeah. You know, I defended you on that because I think you're like a really sweet guy and I think I understand your perspective. So whether or not I like Charles, I'm going to come defend you.

**[47:13] SPEAKER_03:** Not to dig too much, but Charles is kind of like buddy, assistant, partner guy. Is his name Jeremy? I'm trying, I'm remembering, because I actually thought he was Jeremy Wood. Yeah, and maybe there was more there, but I'm just, to Texture's point, you know, maybe he was just naive, or maybe you guys know more than I do, but that was sort of a strange dichotomy.

**[47:39] SPEAKER_02:** Yeah, again, I think it's just whoever would follow him around and not question him. That's how you got to be his right-hand man. The less questions you ask, the closer, better friend you are. The more you listen to his stupid stories, didn't call him on it. You know what I mean? I was on the front lines of Afghanistan for DARPA, and now I'm like, shut the fuck up, Charles.

**[48:01] SPEAKER_00:** With Jeremy Wood, he notably called him, boy, come here, boy.

**[48:06] SPEAKER_02:** I never saw that. Wow. I'm telling you like I remember some story about him like playing games with people in the Zug house like sending somebody's sending somebody off whose wife was there, a girlfriend, and telling them that they had to go do this thing for him out of town. And then when that person had left, he then tried to convince one of the other dudes to get with the dude's wife. Just weird stuff, man. Why would you do that? You have an opportunity of life. The answer is you're a fucking idiot who lied yourself into a situation you shouldn't be in and you are a compulsive... lying manipulator. I'm sure it makes him feel smart or something. I don't know but like it was just the the stories that when he when he was gone after the red wedding I think everybody breathed a sigh of relief you know the biggest problem for me was um after the fundraiser after the red wedding Stefan who I had introduced or I had welcomed into the organization and again there was a lot of political stuff if you went to Zug you got basically put up in the hierarchy so I ended up under Stefan I couldn't go to Zug because my girlfriend was pregnant and I couldn't leave to go to Zug for a month and yeah I don't know Stefan was I don't know. High energy, high anxiety dude. It was a weird thing.

**[49:44] SPEAKER_03:** He was smoking the stereotypical amount of cigarettes at the time.

**[49:49] SPEAKER_02:** The stereotypical amount? That dude lived... He had a vape that he puffed. Oh, you're right. It was a vape. It was clouds of smoke. And so I went, you know, with DevCon Zero, I went and spent a week with them in the office in London. And, dude, Stefan, if you weren't having a fucking panic attack, Stefan couldn't tell you were working. It was crazy and he would pace around this co-working space like nobody else was there just the whole place looked like a fucking rave, dude. Like, I think he got kicked out because he was trying to film a TV show and vaping too much and he had bought like fifty thousand dollars worth of camera equipment because his dream was to start a TV show or something on the Ethereum budget.

**[50:47] SPEAKER_00:** Yeah, I heard that London location was pretty special.

**[50:53] SPEAKER_02:** It was weird, man.

**[50:58] SPEAKER_00:** Did you say you were never in Zug?

**[51:00] SPEAKER_02:** No, I never went. My girlfriend at the time was pregnant. I had spent a month in Panama with Eric Voorhees and his team while she was pregnant. Honestly, in retrospect, if I could go to... It's hard to know how things would have played out because of the political stuff. I was not political. I didn't have any strategy. I was not prepared for any of that shit. My... I just tried to be the most authentic, trustworthy, do-what-I-say person, good to everybody. That's how I survived as long as I did. I don't really do politics. All that stuff was really weird.

**[51:47] SPEAKER_00:** I mean, all of this was prior to both the crowd sale and... the formation of the Ethereum Foundation, right? So the Red Wedding was 3rd of June 2014, where you had that, I guess, that final decision of the foundation happening versus the for profit because you had, uh, we had people coming notably Anthony Di Iorio coming to, uh, Zug at that point to sign papers, right. You know, it was it was to do with that Swiss, uh, legal entity and then it was like yep no we're not signing the papers the big mess uh, and then the foundation, uh, was, was July that that was, uh, incorporated and you still have the crowd sale ongoing through July and August. So yeah. And that was a hell of a long span of time.

**[52:57] SPEAKER_02:** Yeah. We kept saying two weeks. I don't know. That was a meme for a very long time. Two weeks, two weeks, two weeks.

**[53:07] SPEAKER_00:** Well, the website that was up at the time of the Miami conference was showing a countdown to the first of February. That was when the sales were going to start.

**[53:17] SPEAKER_02:** Yeah. And then, you know, I was with Vitalik when the sale was launched. Uh, we had hung out all day in San Francisco. We were in the Westfield mall in the food court for, uh, uh, he needed WiFi. Um, and he was just sitting there and he just looked up at me and he goes, Oh, the crowd. So I went live. Um, because that wasn't planned. I don't know if Taylor talked to you about that, uh, when you, uh, was an accidental launch was it? It was an accident. I don't know you have to ask Taylor about that but yeah I guess he accidentally accidentally hit the button because you know it was legal like that's what kept happening they kept saying we're waiting on legal we're waiting on legal we're waiting on illegal like legal in retrospect right so you and Kieren must have met each other a little bit, yeah various times, yeah, we've, we've actually hung out more probably in the last five years than we did back then. Um, yeah.

**[54:27] SPEAKER_00:** And I guess that Kieren, you saw more of that sort of New York legal side of things.

**[54:35] SPEAKER_03:** Yeah so okay this is a good good tie-in point so uh and and bob at your request of course i was digging through the emails trying to piece together some pieces of the timeline you know yesterday day before so i had um I think by March I was talking with Vitalik and, you know, I was in academia at that time, and he kind of found it useful to bounce like protocol, economic modeling stuff. Off you know like i was like good at reading the white papers and understand what they were doing i could you know kind of code at that time i could still kind of code today but that's sort of we ended up talking about like how the thing should work at a you know theory protocol level more than an implementation level and that kind of I guess, and this was covered in the Red Wedding time, there was a discussion of the usage of funds that ended up on a whiteboard or something. And a lot of it was theoretically earmarked for a research group that meant to solve hard problems like scalability. In crypto that, you know, like in practice, people have sort of solved today and not by any of the means we imagined exactly. But, you know, they've been solved to some degree at least. Um, like with layer twos for instance. Um, scalability was very much anticipated as a problem and you know it took a couple years but you know we had like 55 dollar fees on NFT transfers at some point. Um, so I think um, Metallic sort of like, uh, talk we talked about this for a little bit and then he kind of like blessed me as like the representative who's currently in academia. I started contacting people and trying to get them interested in Ethereum and then doing like research related to it in general we even like set a legal entity up for a separate research group at some point. And I'm trying to remember, so Texture, we mostly worked together just on the site, basically. Like, I guess you were like, you know, web designer at that time. But I'm trying to remember.

**[57:05] SPEAKER_02:** Yeah, I was doing web design. We had talked about the CRG, Cryptocurrency Research Group. And I was like, that's cool. Let me build a website. I remember throwing, you know, faces on it. And then it just kind of puttered out, which, you know, it's... you know, like, um, I, it would have, it would have been a like cool thing, fun thing. I don't know. Um, but also, uh, there's a story about Anthony Di Iorio, not anyways. I like, I didn't know people were getting paid for a long time. And, um, I, uh, was like living on my sister's love seat in her one bedroom apartment with my daughter. Cause I was like fucking homeless, uh, and working on Ethereum as much as I could, uh, like multiple other jobs, uh, to, to try to make money. And, uh, I contact or Anthony Di Iorio contacted me one day cause he was, you know, he was in the earlier days, like the primary contact, um, that I would talk to the most. And he called me and he asked me for a favor. And, uh, I was like, yeah, man, no problem. And I said, Hey, by the way, if you, you know, like, listen, I'm in a bad spot right now. Is there any way I could get like back pay for 10 grand, which, you know, was not much. And this dude just says, Oh no. And I was like, what the fuck? Anyways, I talked to Vitalik. The way it goes back to the CRG is the CRG was supposed to pay me $5,000. So you owe me $5,000, Kieren. I don't know, you know, given that it was so early, if you could just pay me an ETH relative to the price at that time, that'd be sick. Exactly.

**[58:56] SPEAKER_03:** 20 cents was the presale price. Yeah, something like that. So it'd be like quite the amount of ETH.

**[59:04] SPEAKER_02:** Yeah, so just like 15,000 ETH and we'll call it even.

**[59:08] SPEAKER_03:** All right.

**[59:08] SPEAKER_02:** All right.

**[59:14] SPEAKER_00:** But yeah, I mean, I guess, you know, many, that was the case for many people through those months, you know, for some people that was nine, 10 months of unpaid contribution.

**[59:29] SPEAKER_03:** My memory is also that Anthony was the main force behind sort of actually not quite stopping, but delaying the funding to the CCRG. So like somehow we got it, some of it way later. Di Iorio. Di Iorio, yeah. Um, and it was like not quite the original amount but it was still some but we were all like working on different things at that time so we ended up returning it I think but yeah it was a strange like the the strange delay that happened I guess like right after the pre-sale. Um, So before people are working, you know, uncompensated or largely uncompensated. And then right after there was, I suppose, like a big cash grab going on. So like maybe, you know, better than us. So there were a bunch of legal entities getting set up like, you know, there was like the Berlin Dev Company and then there was another one like in each. Everyone tried to like pull out as much of the pie as they could.

**[1:00:38] SPEAKER_00:** But like yeah i don't know yeah good yeah so so uh anthony the oreo not you yeah uh incorporated um ethereum canada in february actually but it was about it was just a few days before everyone went to Zug so his thought i guess was everything was going to happen out of toronto but that didn't happen You had Ethereum Swiss got formed in Switzerland somewhere in April, I think. You had GAV incorporating Ethereum Dev in Berlin. Jeff in Amsterdam, though, that took quite a few months, more legalities to it. And there was an Ethereum... in London as well. Most of those FDev ones were kind of co-founded by Vitalik and Gav and Jeff and Mihai kind of group. Yeah, it was only the the Toronto one there where it was that I could see Anthony was a director. I don't think he was ever a director on any of the other legal entities. They were basically the, you know, the, the debt people, um, and all Mihai and Taylor. Um, but, but yeah, when, when you'd had the crowd sale and the, the had been formed and then were the recipients of those funds, there was a whole power grab of a mess of how those funds went out and, uh, in, in cryptopians it talks about Gav maybe wanting to like grab all the money straight into dev but then it's like that's probably not legal and it's probably not a good idea either and Joe wanting to do it sort of a milestone based slow delivery which is i think what it sort of ended up being but you did have this sort of weird situation where um You'd say, oh, do you work for the Ethereum Foundation? But very few people actually work for the Ethereum Foundation. Most people were actually working as staff or contractors for these for-profit legal entities, which were sort of doing the work.

**[1:03:02] SPEAKER_03:** Yeah, I guess they must have got it kind of like having now run a business for a long time. You've got to set up sensible contracts and IP agreements. Sometimes that looks like an intercompany agreement. And then if you do it in the buttoned-up way, there's a lot of headache associated with such things. I think it was a hell of a lot looser than that.

**[1:03:28] SPEAKER_00:** I have a a strong memory yes of like a let's just put all the money in this other legal entity discussion going on like during the whole red week wedding week you know so yes man yes um and and yes the majority of those legal entities have since been shut down um that was something that Ming did over the course of her time was tidy up all of this like corporate mess that was maybe not really even required in the first place but uh um yeah I mean I think yeah good sorry well they could have just worked for the foundation but I guess they didn't they didn't want to be in Switzerland which maybe was part of it and I remember this was yeah it well this was another funny thing right with the uh with the spaceship

**[1:04:25] SPEAKER_02:** Was that there was an expectation at the start there that there was going to be a lot of development work happening in Switzerland as well and then that never happened also it it kind of uh goes against the charles was fired for wanting to uh make it corporate when every single person filed their own corporate legal entity in an attempt to divert the funds to their own personal power structure

**[1:04:54] SPEAKER_03:** Yeah, I'll add, because I was in the room for some of this. Gavin immediately started talking about brain drain when there was to be no crypto Google. Um, so I, I guess like they, for, for a long time, they wanted to do hybrid for-profit, uh, nonprofit and, you know, the, the protocol sits in the not-for-profit and, you know, for-profit tries to commercialize and yada, yada, yada. And of course in the end, everyone's like the tokens were worth more than probably any equity would have ever been worth. But, um, but yeah, I think, I think the, it's, it's definitely a mix of factors. I think it's primarily what you said, but also, you know, like the, I think while there's just a grossness to Charles, like, I guess, okay with being on record on, I think there was also a dev guy, business guy divide that to your point on like the autists, right. You know, not that they were great at business like Amir Charles, but there was more of a like, what do you do? And some of what they did was like, try to set up deals with the Canton of Zug and then do like other business developments, etc. That kind of was lost afterwards. I'm not saying it was all that effective. In their hands but, uh, there was this like BD commercialization gap and so, yeah, to your point everyone then started their own companies. ConsenSys being the most successful of them and kind of filling that sort of business guy plus commercialization role from there on. You're saying the guy with the most business experience did the best so it seems like

**[1:06:43] SPEAKER_02:** What's funny when I met your dad, uh, in the Miami house, I just thought he was somebody's dad. I mean, obviously in retrospect, he was yours, but, uh, I didn't know that he would go on to become Joe Lubin. You know, I just remember like shooting shit with them and talking to him about thoughts and stuff. And he was real like quiet and, you know, told me about his time making music videos in Jamaica or whatever.

**[1:07:09] SPEAKER_03:** Yeah, that was right after that. He also, for a time, he believed that he would be a software developer for Ethereum. And then I guess he realized... like no one knew anything about business and uh yeah you know he does he doesn't have you know a tour in corporate from the i.t side and then run a hedge fund so he the most understood how things worked I guess yeah much better than everyone else. I knew how to, uh, exist in a early stage startup because I've been doing that for 10 years over and over.

**[1:07:44] SPEAKER_02:** So my major contribution was not saying, have you guys ever heard of a four year vesting period? I thought it a bunch and I was like, I don't want to be here for four years. I'm not going to say that shit.

**[1:08:01] SPEAKER_00:** Yeah. I mean, it's something which I've seen people comment on a fair bit is, um, you know, the, the early contributor slice of, which was 9.9% of the Ether, which was shared between the people who did contribute over those 10 months or so, is equal to the amount that the Ethereum Foundation received. So all of the developments of everything which happened after that July to the current date has had that same bucket. And, uh, you know, that is not a typical kind of uh setup for you know long-term success talk about the best thing you know that uh as I as I look through a lot of these early people uh you know they they did their part and they moved on yeah but it would be nice if some people hung around some more

**[1:09:06] SPEAKER_02:** Yeah. I mean, I think to some degree, that's why I'm still here in this space, that, and the guilt of learning what people do with the things you create and feeling some sort of like responsibility to kind of try to nudge it in a direction, you know, but balancing that with my desire to be anonymous to the most degree that I can was difficult.

**[1:09:32] SPEAKER_00:** Yeah. Yeah, for sure. I mean, it was something which came up, I think, through sort of 2018, 2019 as well was the foundation stiffing developers, essentially.

**[1:09:48] SPEAKER_02:** Yeah, I don't know. That didn't happen to me. Praise Vitalik.

**[1:09:53] SPEAKER_00:** No, no. It's all right for you early, guys. But... But yeah, what else they have noted? Something which you've spoken about a little bit on Twitter as well is sort of like purges and palace politics and so on. Can you speak a little bit to about the nature of the foundation and the opaque nature of it and these kind of palace politics that you have going on? What's happening there?

**[1:10:26] SPEAKER_02:** You mean in the last 10 years?

**[1:10:30] SPEAKER_00:** Right, right. I mean, because it's quite a contrast, right, in your Coinbase article, you were speaking about the contrast, right, between your open, decentralized, collaborative space and the foundation as an entity.

**[1:10:46] SPEAKER_02:** Yeah, so I think that it's difficult because if you look at, you know, this is my personal assessment, how I think about the situation. If you look at the early days and and you take all that political shit seriously and you realize that Vitalik's basically like a 18 year old kid in the middle of this like I was under prepared for the political shit but I wasn't even like the center of it you know Vitalik had to be pushed into this weird situation where all these sharks and snakes were around and where Charles is acting some type of way. Um, and then everyone else around him is, is vying for power and that's a lot of stress. Right. And so if I was thinking of it from Vitalik's perspective, to me, my primary goal for myself would be to insulate myself from the, those political games to, to the greatest degree possible. Right. And so, you know, In some ways, it's kind of like the requirement to stay sane and the requirement to insulate yourself from people playing these games and trying to get to you is that you kind of have to anoint yourself king and do the thing that Charles did, which is surround yourself with people who are going to basically have like fealty to you, right? They're not there because they're trying to manipulate you or get one over on you. They're not there because, you know, they're not playing games behind your back that you're going to have to deal with. And I think that if you're trying to focus on your goal, you know, in this kind of like foundational structure, I just assume that every, every decision that's been made in, in the structure of the foundation is, is, based on kind of two principles, one is kind of the the amorphous notion that, like a decentralized project shouldn't have. Centralized control structure and it, you know there's really some sort of kind of suicide urge that I see in the way that they structure it like it could be an organization that exists for you know. A thousand years if they organize it correctly but they're they're trying as hard as they can it seems to make it disappear and I think that that's like incredibly misguided I don't think there's any historical um examples of anything like that happening and I think that if the foundation disappeared tomorrow then all those power game you know the power vacuum would just create fucking infinity of those power games until somebody stepped up and Ethereum becomes whatever the person who can kind of get that power position. So I think that, unfortunately, from my assessment, Vitalik's need to keep himself sane and protected has not been done in such a way that the Ethereum Foundation necessarily serves the long-term survival of Ethereum. It just, like... that that's a major concern for me. So I don't, I don't, I think a lot of people might criticize the way it's structured for reasons like, but I understand, man, like I'm not Vitalik and I've had to deal with, you know, those power games and they drive you crazy, man. They get in your way. They keep you from being able to focus on what you want to focus on. And I think not coming up through the traditional, um, kind of like Silicon Valley group. When you come up in that, you're surrounded by people who have been in it and have survived for a long time. And they understand how to support founders and they understand how to legally orchestrate these things. And I just don't think that he had those people around him to protect him. So I don't know. Kieren, you got something to say?

**[1:14:56] SPEAKER_03:** I wanted to compare Ethereum with Bitcoin, which I've seen some of the similar governance issues on Bitcoin, but it's different. Right now, it feels pretty technologically stagnant. At a time, I knew a bunch of the core devs. We had a funny meetup once at a Berkeley restaurant and a couple of them showed up. And it's... you know, Bitcoin technologically just doesn't really change, but there was a time where people were kind of, it was a foundation and they were acting in a coordinated manner to popularize Bitcoin and so on. And now it feels like those people are largely gone. Um, there, there's, a, a lot of the work, um, that adds functionality to Bitcoin uses Ethereum or an L2 or an EVM or what have you. And people are just kind of focused on the price action pretty much. And that's been, I think, a benefit to Bitcoin. But I guess like... I think Satoshi kind of went through something similar. And I think he was starting to get pretty irritated from, there's a good book covering his Bitcoin talk posts and how that started to feel over time. And then obviously he disappeared when he disappeared. I'm just thinking like, is the Ethereum way better? I think like probably it is. It's not optimal for sure. Like later projects run much closer to Silicon Valley tech companies and like have the open source part where the open source parses, but are pretty strongly governed so far as I can tell. But no, I think I also say like there's probably some merits to the approach. Like it was so decentralized that lots of people could come in and

**[1:16:50] SPEAKER_02:** Try to make it their own and that there was a plus to that too and just the downside being the chaos. I don't know what, what do you think about this question? Yeah, I mean I think, can you hear me? My little thing is not showing. You're good. Okay. Um, yeah no I think you know as far as the foundation being set up in the beginning it's it's whatever what it's become is whatever too because it could they could change into a structure that supports Ethereum for the long term. But yeah, I'm more focused on today. But I do think, you know, I always thank your dad every time I see him for all his work, because I do think he's filling a role. And if there is a power, again, I think if there is a power vacuum, you know, I think he will be standing around to at least mitigate it. Um, without him who knows but the the thing about the Bitcoin thing you said is like that's what I'm concerned is going to happen to Ethereum is you get to a point where it just becomes this kind of like not coordinated thing where everybody's arguing and nothing happens right and nobody can make a decision because at the end of the day like groups don't make decisions you know groups don't create greatness like that's just that's just not what happens you know like you have you have these kind of visionary geniuses and if they manage to like find the right idea and the right group and they're supported and they have the time and energy to do it, um, then then it then it moves forward. You can you can even look at like a more structured version, version like Apple. Um, whereas you know, Steve Jobs had set up a massive corporate structure and it still exists to this day and the vision is gone. Right. So once, once the kind of visionary is separated from the vision and once the, you know, it's, it's going to default back to the level of the organization. And if you're, if the goal of the Ethereum foundation as stated is to make itself irrelevant, like, I mean, that's so frustrating, like, man, we created this technology that could potentially allow you to, it could, it could potentially allow, this technology could potentially allow you to create entire governance systems and corporate structures or whatever that could persist on the blockchain indefinitely with all kinds of mechanisms. And like, what the fuck? Like, is that not what the Ethereum Foundation should be doing? Should they not be like eating their own dog food? Should they not be doing what we said we were going to do? Should they not be funding that? Like, I mean, how many esoteric scaling solutions can you invest in, right?

**[1:19:46] SPEAKER_00:** Yeah, I mean, from my perspective, I think the change of leadership that there was this year with Tomas coming in as a co-ED has made a world of difference, that they have become more transparent than has been the case before. And I think that he, as a Nethermind company CEO because he's the the CEO of of Nethermind as well I think has given him that kind of like product holistic getting done kind of perspective that hasn't before and he's got the credibility of having been in the ecosystem as well right and having gone from hey we're we're a

**[1:20:37] SPEAKER_02:** You know we're a little company doing an Ethereum client to you know a really large kind of player that do all kinds of things yeah and i think there hasn't been that before you know he is a CEO type he uh he was i did a call with him we talked for a bit and he seemed great asked a lot of questions and said he talked to over 100 people and I gave him some of my thoughts and criticisms and I don't know. I've, I've seen a lot of the things that we've talked about kind of playing out. So, you know, I hope, I hope he can be a force that persists again. You know, if you have the palace politics, there's always the people like that. They're always in danger.

**[1:21:25] SPEAKER_00:** So there might be another coup.

**[1:21:30] SPEAKER_02:** That's what I'm saying. Like, You could be the best guy with the best intentions, with the best ideas, and you're the guy to do it. And if the power structure is designed around placating people who are only concerned about their place in the palace, um, you know it's happened to me multiple times in my life, uh, they kick you, they kick you out because you're a threat to what they're trying to accomplish in their minds, um, they don't understand that you know if you allow the guy the guy who is doing this to to really create something that lasts and is bigger than you're going to get a bigger piece of a bigger slice from a bigger pie but if you completely undermine everybody who's trying to do that then you're going to end up with a nothing you know

**[1:22:30] SPEAKER_03:** There's a mechanism for a coup I assume like in practice the foundation is like you know kind of doing whatever the people who work for it want to do but in the end is a dictatorship of Vitalik at the end of the day like yeah so yeah the only mechanism I see is the people who have Vitalik's ear get in his ear long enough that

**[1:23:00] SPEAKER_02:** It's not working. So to some degree, there might be a community capacity to be a louder voice consistently to ensure that there will be backlash if anything like that happens.

**[1:23:21] SPEAKER_00:** Yeah, I make this the sick epoch that there's been. So we had white paper to web red red wedding where it's essentially you know just no formal structures really you know emergent then you have the the period of the uh of the Ethereum Foundation and FDev so that was July 2014 through February 2015. Then he had the interregnum where you you were whopped which was between March 2015 and June 2015, where you had Kelly... Becker. Kelly Becker overseeing the installation of the new professional, in quotes, board that began the Ming dynasty, where she immediately knocked off all the other directors, and then she had her Three years of tyranny. And then you had the Infinite Garden with Aya coming in in another coup there in February 2018. And then it seems this last one was maybe not so much of a coup as an evolution in that Aya's still around as the president, that you have new executive leadership.

**[1:24:48] SPEAKER_02:** Yeah. So yeah I don't know what this period comes to be called but it's it's it's definitely better and more coherent you know I, I'm, I'm prescient a lot of the time and you know I had my encounters with Aya that clued me into the fact that she was not really um qualified or even coherently involved in a way that I would assume somebody uh in her position will be so i was you know i was applying pressure years ago years and years ago and um yeah five years ago six years ago so i think you know eventually the community kind of uh came around to what i've been saying this whole time which is wait like she should be doing like there's things that need to be done and we all see that they're not being done and what the fuck and we can't even this woman is doesn't seem to care and she keeps talking about esoteric poetry and fucking infinite gardens what is this shit you know like fucking do your job. Like, you know, for me, the, you know, I've talked about it before, but you know, their website, the website was like the same website for three years. I had, it was just an informational website. It was a brochure website. And I just messaged her and said, Hey man, we, uh, we need to update this website. I'll do it for free. And she said, oh yeah, I think we have a team working on that. Let me get back to you. So I like kept in contact with her it took her six months, six months to figure out who was working on the website Bob I mean, yeah, like are you kidding me like what are you doing are you sitting and at the beach like sipping mai tais? I legitimately don't know what you're doing because you clearly have no Active. This is how this is what it should be. You should have an org chart. You should fucking know the person to call. You know, you should actually know who's building your website. Yeah. So that was that was just insane to me that you could be the ostensible. Yeah. Running an organization and not even know who to contact to to see who is building the website. And then it ultimately was Josh Stark. I messaged him, said, hey, man, I'd love to help. I'll do it for free. I can have it done in a week. He was like, no, I'm good. I was like, what do you mean? You're good. You're not doing it. Like nothing has happened. It's been six months. It's not something that takes six months or a year. Anyways, it was like a year later, they finally launched a year and a half later.

**[1:27:23] SPEAKER_00:** So there was a longer tweet thread, um, of me ranting a little bit. Well, it wasn't very ranty actually. It was quite polite in, in late, uh, in late, it was December, 2017. And Hudson tweeted out something like, hey, what could the Ethereum be doing better? It was something like that. It's like, ah, well. Oh, my God. But my list was very simple. It was like, yeah, the website, shit, useless, doesn't do anything. There's no information, nothing there. You know, nothing useful there. Also, there's no public information on the Ethereum Foundation. Like, you know, who... Who are the board members? How does voting work? Who are advisors to the foundation? What teams are there? Who works on these teams? There wasn't even a grants program at that point either. It was just basically, you just have Ming and Vitalik and she had hired on Jamie Pitts and Hudson. So there was a little bit of extra help. But essentially it was that thin little bit of overhead and a bunch of devs. And that was what there was. And she couldn't delegate either, Ming. So just nothing got done. Like really just nothing got done at all.

**[1:28:52] SPEAKER_02:** Um, yeah, I mean, I don't know in retrospect if I had known that I mean I know you said she was a nightmare but she did offer to hire me back into the Ethereum Foundation but I, uh, I didn't feel I don't know it was a time where I didn't really feel like uh working I'd been a little burnt out from the previous few years so um yeah you know maybe if I'd accepted that

**[1:29:19] SPEAKER_00:** She should have Minged you. Don't worry, you wouldn't have lasted long if she came back.

**[1:29:24] SPEAKER_02:** Maybe, maybe, maybe. Everyone got Minged. If she was like Stefan, then yeah, that high energy, like stress stuff. But I don't know. I was a little bit more.

**[1:29:35] SPEAKER_00:** But yeah, I mean, you know, so I think that was the problem, like that. You hadn't got enough people to get anything done, you know, like what you talked about with AYA. That was a case in that earlier era as well. There wasn't really no organizational structure and nothing really much was happening beyond the developers doing their development. Oh, and, you know, we'll do a DevCon now and then.

**[1:29:58] SPEAKER_02:** Yeah. Well, you asked about the palace politics thing and I just had a memory, you know, people it's, it's much less now than it used to be, but to some degree people still keep me in the loop when, you know, they know things. So I think maybe the biggest problem with the, with the way that things are structured right now is that there's nobody to give pushback. And there's no dissenting voices and there's a, like a, very homogenous group of people, homogeneous, whatever the word is, a group of people who aren't going to step out of the party line for any reason because they're going to be afraid of being pushed out. And I think that's not necessarily good. Obviously, you can't have people following you around who think their only job is to undermine anything you say but really I mean you need you need voices that will speak the truth um even when it's uncomfortable because you know decisions may they have they have outcomes and having a bunch of people who see the world in the same way and um aren't really thinking of of things holistically or from different perspectives you know it's going to create issues

**[1:31:24] SPEAKER_00:** At the recent EthCC in Cannes, there was a slide which Jerome had on there, which was talking about dissenting voices. And both myself and Greg Colvin were up there as Ethereum dissidents.

**[1:31:43] SPEAKER_02:** I didn't get it. It's all right. Nobody remembers me. Congrats, though.

**[1:31:47] SPEAKER_00:** No, sorry. You're not being loud enough. I don't know. Oh, no. You're not being loud enough.

**[1:31:55] SPEAKER_02:** No, it's all right. I only have the number of followers I do because of a couple of jokes I made, one of them being Texture Punks. I very much don't mind being lost to history if it means I'm not on someone's let's rob the sky list.

**[1:32:14] SPEAKER_00:** Well, I think that's maybe a good kind of place to wrap up. Yeah, don't worry. So I wish you all the very best and enjoy your life.

**[1:32:29] SPEAKER_02:** Yeah. Well, Bob, thanks for having me on. If you want to have me on again, I'm more than happy to always give you my time. Good to talk to you, Kieren.

**[1:32:39] SPEAKER_03:** It's been not too long. Great to chat again and we'll do it again soon.

**[1:32:48] SPEAKER_02:** Maybe so. Maybe we'll see you soon. Thanks for everybody who's come to listen. Don't follow me.

**[1:33:00] SPEAKER_00:** Thanks a lot. Texture is IamTexture on Twitter. Have you got any other questions?

**[1:33:07] SPEAKER_02:** Websites or anything places that you'd like to point people? No, I'm not. No, just okay have a nice night have a nice day whatever you're at morning thanks so much. Okay cheers everyone bye