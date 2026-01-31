**Step 1: Analyze the Request and Constraints**

*   **Role:** Expert transcript editor specializing in Ethereum and blockchain.
*   **Input:** A raw transcript from speech recognition with speaker labels (SPEAKER_04, SPEAKER_03, SPEAKER_01, SPEAKER_02) and timestamps.
*   **Key People List:** Provided for spellings (e.g., Bob Summerwill, Kieren James-Lubin, Vitalik, etc.).
*   **Technical Terms List:** Provided for spellings (e.g., Ethereum, EVM, DeFi, ConsenSys, etc.).
*   **Primary Objective:** Create a clean, readable transcript preserving ALL dialogue and content.
*   **Critical Output Rules:**
    *   NO preamble, introduction, or meta-commentary. Start immediately with the first speaker label.
    *   Preserve content (no summarizing).
    *   Maintain length (~90-110% of input).
    *   **Timestamps:** Preserve exactly as input. One per speaker paragraph.
    *   **Formatting:** Merge consecutive speech into paragraphs. Bold speaker label + timestamp.
*   **What to Fix:** Technical terms, proper names (using the provided list), punctuation, sentence structure.
*   **What to Remove:** Excessive filler words ("um", "uh", "like"), false starts, repetitions (selectively).
*   **What to Preserve:** All substantive dialogue, technical explanations, speaker labels, natural flow.

**Step 2: Analyze the Input Transcript**

*   **Speakers:**
    *   SPEAKER_04: Host (sounds like Bob Summerwill based on context "head of ecosystem at Stratum..."). *Correction:* Wait, SPEAKER_02 introduces himself as "Bob Summerwill, I'm head of ecosystem at Stratum..." later in the transcript. So SPEAKER_02 is Bob. SPEAKER_04 is likely the one asking questions. SPEAKER_03 is the moderator/host ("In the same room"). SPEAKER_01 introduces the guest "Redwan Meslen". SPEAKER_01 is likely Kieren James-Lubin? Or maybe just another panelist. Let's look for clues. SPEAKER_01 mentions "I'm Pax..." wait, the text says "boxing will". Later it says "So, yeah, I'm on Twitter. Same as my name, Bob at Summerville with a W-I-L-L". That confirms SPEAKER_02 is Bob Summerwill. SPEAKER_03 asks "Bob, where can people find you?". SPEAKER_03 seems to be the host. SPEAKER_01 introduces the guest. Let's check the "Key People" list. "Kieren James-Lubin" is there. "Bob Summerwill" is there.
*   **Content:** Discussion about the Enterprise Ethereum Alliance (EEA), history (DevCon 2, JPMorgan, Quorum, Hyperledger, etc.), current state (Sibos, SWIFT, DTCC, stablecoins), and future (tokenization, regulation).

**Step 3: Segment-by-Segment Editing**

*   **[00:02] SPEAKER_04:** Discussing streaming tools (Restream, StreamYard, X/Twitter, YouTube, LinkedIn).
    *   *Fixing:* "We try to use something and it streams on Twitter, I think YouTube and LinkedIn at the same time. So we're using StreamYard too. ... You want to use it somewhere else? Are you seeing somebody else? Be able to own your data..." -> "Are you seeing somebody else? Be able to own your data."
    *   *Clean up:* Remove "um", "uh", excessive "you know".
    *   *Timestamp:* Keep [00:02].

*   **[01:38] SPEAKER_03:** Technical issues check, intro to guest, "Jane Joe Live".
    *   *Correction:* "Jane Joe" -> Maybe "Bankless"? Or "Just Jane"? The text says "Jane Joe Live". Without external context, I have to keep it phonetically or guess "Bankless" is unlikely given the context "Jane Joe". Let's look at the speakers. SPEAKER_03 says "In the same room." It's likely a podcast name. "Jane Joe" might be "Zero Knowledge" or something similar? Actually, looking at the list "Adam B Levine" is in the list. Maybe it's related? Let's stick to the text "Jane Joe Live" but clean the grammar. Actually, looking later: "Thanks again. It's awesome. Thanks for coming. Take care." -> This sounds like a wrap up.
    *   *Context:* "Jane Joe Live" is likely a transcription error for "Bankless"? Or "Just a bit"? No. Let's leave "Jane Joe Live" or "Jae and Joe". Actually, "Jane Joe" sounds like "ZK" maybe? No. Let's keep "Jane Joe Live" as a proper noun phrase even if it's weird, but clean the surrounding text. Wait, SPEAKER_03 says "No, but that was a good cold intro".
    *   *Timestamp:* [01:38].

*   **[02:04] SPEAKER_01:** Introduces "Redwan Meslen". Executive director of EEA. History: Feb 2017 launch, DevCon 2 (Shanghai), JPMorgan meetings.
    *   *Names:* Redwan Meslen (check list - not in list, but introduced). EEA (Enterprise Ethereum Alliance).
    *   *Timestamp:* [02:04].

*   **[03:16] SPEAKER_03:** JPMorgan meeting Jan 2017. DevCon 2 conversations. Meeting at Starbucks. Matt spoke. Technical issues with Twitter.
    *   *Fixing:* "Matt spoke of NewCo held a little bar side event" -> "Matt Spoke of NewCo" (person).
    *   *Timestamp:* [03:16].

*   **[05:06] SPEAKER_01:** Enterprise Slack started by Vitalik. "dumped the ball in a slack and ran away". Introduction of himself: "boxing will" -> "Bob Summerwill" (later confirmed as SPEAKER_02? No, SPEAKER_02 introduces himself later. Let's check who is who).
    *   *Correction:* "boxing will" -> "Bob Summerwill". Wait. Later at [05:54] SPEAKER_02 says "I'm living CEO of blockups... creators of straddle... Victor Wong...". Wait, "Stratum cut change" -> "Stratum". "I'm Bob Summerwill, I'm head of ecosystem at Stratum". So SPEAKER_02 is Bob.
    *   *Who is SPEAKER_01?* "I'm Pax..." text says "boxing will". It says "boxing will so i'm head of ecosystem at Stratum cut change". Wait. The transcript says: "boxing will so i'm head of ecosystem at Stratum cut change". This seems like a misattributed segment or a bad transcription of "Bob Summerwill". BUT, later SPEAKER_02 introduces himself as "Bob Summerwill, head of ecosystem at Stratum". Let's re-read [05:06]. "I did choose a parallel in that... I was still working for the Ethereum Foundation...". Then [05:54] SPEAKER_02 says "I'm living CEO of blockups...". Actually, looking at the names in the "Key People": Bob Summerwill is listed. Kieren James-Lubin is listed.
    *   *Correction:* In [05:06], SPEAKER_01 says "boxing will so i'm head of ecosystem at Stratum cut change". This is likely Bob Summerwill speaking. But the label is SPEAKER_01.
    *   *Later in [49:09] SPEAKER_01 says "Bob, where can people find you?"*. This implies SPEAKER_01 is NOT Bob.
    *   *Re-evaluating [05:06]:* The text "boxing will so i'm head of ecosystem at Stratum cut change" is extremely corrupted. It looks like the previous speaker (SPEAKER_01) continues or it's a glitch. However, later at [05:54], SPEAKER_02 speaks and introduces themselves. "I'm living CEO of blockups...".
    *   *Hypothesis:* The transcript at [05:06] might be mislabeled or the text belongs to someone else who isn't Bob. Or maybe SPEAKER_01 is Bob, and SPEAKER_02 is Victor? Or vice versa.
    *   *Let's check the end:* [49:35] SPEAKER_03 asks "Vic...". [49:09] SPEAKER_01 asks "Bob, where can people find you?". So SPEAKER_01 is neither Bob nor Vic.
    *   *Let's check [05:54] SPEAKER_02:* "I'm living CEO of blockups, Victor, creators of straddle." -> Likely "I'm Victor Wong, chief product officer of BlockApps". (Key People: "Victor Wong" is in the list). The text says "living CEO" -> likely "Lin" something? Or "I'm Victor Wong"? No, "living CEO" is probably "Victor Wong". Wait, "Victor, creators of straddle". It sounds like the speaker is introducing Victor. "I'm [Name], CEO of BlockApps...". Or maybe "I'm [Name]... Victor is...".
    *   *Let's check [05:54] again:* "I'm living CEO of blockups, Victor, creators of straddle. Yeah. And Victor Wong, uh, chief product officer of blockups." This implies Speaker 02 is introducing himself AND Victor? Or introducing Victor. "I'm [Name], CEO of BlockApps... Victor Wong...". Let's assume Speaker 02 is introducing Victor Wong, or introducing himself as Victor Wong.
    *   *Later at [49:35] SPEAKER_03 asks "Vic, V-I-C..."*. This confirms Vic/Victor is one of the guests.
    *   *Let's check the Key People list for CEO of BlockApps.* "Kieren James-Lubin" is CEO of BlockApps.
    *   *Let's check the text at [05:54]:* "I'm living CEO of blockups". "living" -> "Kieren"? Phonetically "Kieren" sounds a bit like "living" if muffled. Or "I'm Kieren".
    *   *Let's check [49:09]:* SPEAKER_01 asks "Bob, where can people find you?". SPEAKER_02 answers. Then SPEAKER_01 asks "Karen?". "K. James Lubin on X...".
    *   *So:*
        *   SPEAKER_01: Kieren James-Lubin (asks about Bob, then Karen/Kieren).
        *   SPEAKER_02: Bob Summerwill (Head of Ecosystem at Stratum).
        *   SPEAKER_03: Host (asks Vic).
        *   SPEAKER_04: The guest Redwan Meslen? Or another host?
        *   Wait, [02:04] SPEAKER_01 introduces the guest "Redwan Meslen". So SPEAKER_01 is the moderator for that segment? Or SPEAKER_01 is the guest? "So, yeah, we have here today with us Redwan Meslen...". This sounds like the host introducing the guest. But later SPEAKER_01 is Kieren asking Bob. This is confusing.
    *   *Let's look at [01:38] SPEAKER_03:* "So we are live... we have a very special guest today... In the same room... And you are a special guest, do you want to intro?" -> SPEAKER_03 is the host/moderator.
    *   *Then [02:04] SPEAKER_01 speaks:* "Sure. So, yeah, we have here today with us Redwan Meslen...". This suggests SPEAKER_01 is Redwan Meslen? Or SPEAKER_01 is introducing Redwan? "Sure. So, yeah, we have here today with us Redwan Meslen... who is the executive director of the EA...". This sounds like the speaker is the one being introduced or the introducer. "And you are a special guest, do you want to intro?" (SPEAKER_03). SPEAKER_01 responds: "Sure. So, yeah, we have here today with us Redwan Meslen...". This is weird. Usually the guest says "Hi, I'm Redwan". Here the speaker says "We have here today... Redwan". Maybe Redwan is introducing someone else? Or maybe SPEAKER_01 is the host passing the mic?
    *   *Let's assume SPEAKER_01 is Kieren James-Lubin (based on the later "Karen" question and Kieren being CEO of BlockApps, which matches the "blockups" mention).*
    *   *Let's assume SPEAKER_02 is Bob Summerwill.*
    *   *Let's assume SPEAKER_04 is Redwan Meslen?* Let's check [06:23] SPEAKER_01 asks "But then they did work on Chinese cryptography...". [06:42] SPEAKER_04 asks "because you you have uh you know i was not at the year at that time...". This sounds like the guest who wasn't there in the early days asking questions. Redwan wasn't there (joined EEA later, around 2023?). So SPEAKER_04 is likely Redwan Meslen.
    *   *Let's assume SPEAKER_03 is the host.*

*   **Correction Strategy for Names:**
    *   SPEAKER_01: Kieren James-Lubin (Context: "Karen" later, CEO of BlockApps).
    *   SPEAKER_02: Bob Summerwill (Context: "head of ecosystem at Stratum", "Bob at Summerville").
    *   SPEAKER_03: Host (maybe Victor Wong? No, Vic is addressed at the end by SPEAKER_03).
    *   SPEAKER_04: Redwan Meslen (Guest, wasn't there early, asks questions).

*   **Refining the text:**

    *   **[00:02] SPEAKER_04 (Redwan?):** Discussing streaming. "I use Restream...". "Those platforms, they're not built with interoperability in mind...". "On X... there isn't even a means to download the bloody audio.".
    *   **[01:38] SPEAKER_03 (Host):** "501. Oh, yeah. We are live...". "Jane Joe Live" (Keep as is, maybe "Bankless" but text is distinct). "In the same room.".
    *   **[02:04] SPEAKER_01 (Kieren):** Introduces Redwan Meslen. "Redwan Meslen... executive director of the EA...". Mentions history: Feb 2017 launch, DevCon 2, JPMorgan, Microsoft.
    *   **[03:16] SPEAKER_03 (Host):** JPMorgan Jan 2017. Devcon 2 contacts. Meeting at Starbucks. Matt Spoke. Technical glitch. "I messed up the Twitter. You did a bad one."
    *   **[05:06] SPEAKER_01 (Kieren):** Mentions "Enterprise slack started by Vitalik". "Nuka" (Nikola?), "Luca". "I'm boxing will so i'm head of ecosystem at Stratum cut change." -> This line is misplaced in the transcript. It's likely SPEAKER_02's introduction later? No, SPEAKER_02 introduces himself at [05:54]. The line at [05:06] "boxing will" is suspicious. "I did choose a parallel in that because I was still working for the Ethereum Foundation at the time...". This fits Kieren (who worked at EF). "I'm boxing will" might be a hallucination of the transcript where Bob Summerwill's name pops up? Or maybe Kieren says "I'm Kieren" and it got transcribed as "boxing will". Wait, Kieren James-Lubin was CEO of BlockApps. Bob is head of ecosystem at Stratum. The text says "I'm boxing will so i'm head of ecosystem at Stratum". This is definitely Bob Summerwill's intro text, but it appears under SPEAKER_01 at [05:06] *after* Kieren talks about the EF. This is likely a speaker label error in the source or a very garbled edit. However, SPEAKER_02 gives a different intro at [05:54]. Let's look at [05:54] SPEAKER_02. "I'm living CEO of blockups, Victor, creators of straddle...". "living" -> "Kieren"? "I'm Kieren...". If SPEAKER_02 is Kieren, then SPEAKER_01 might be someone else.
    *   *Let's re-evaluate based on [49:09].*
        *   SPEAKER_01: "Cool. And Bob, where can people find you?"
        *   SPEAKER_02: "So, yeah, I'm on Twitter. Same as my name, Bob at Summerville..."
        *   SPEAKER_01: "Karen? K. James Lubin on X..."
    *   *Conclusion:*
        *   SPEAKER_01 is the host/moderator for the wrap-up? Or Kieren? He asks Bob, then answers for "Karen".
        *   SPEAKER_02 is Bob.
    *   *Let's look at [02:04]. SPEAKER_01 says "Sure. So, yeah, we have here today with us Redwan Meslen..."*. This sounds like a host.
    *   *Let's look at [05:54]. SPEAKER_02 says "I'm living CEO of blockups...". If "living" is "Kieren", then SPEAKER_02 is Kieren. But SPEAKER_02 is confirmed as Bob later.
    *   *Conflict:* [05:54] text says "I'm living CEO of blockups". If SPEAKER_02 is Bob, this text is wrong. Bob is not CEO of BlockApps. Kieren is.
    *   *Hypothesis:* The labels 01, 02, 03, 04 are mixed up or the text segments are swapped.
    *   *Let's go by content flow and voice.*
        *   Voice A (Redwan/Guest): SPEAKER_04. (Wasn't at early events, asks questions).
        *   Voice B (Host): SPEAKER_03. (Introduces guest, manages stream).
        *   Voice C (Kieren): CEO of BlockApps, knows history (Devcon 2, EF).
        *   Voice D (Bob): Head of ecosystem at Stratum.
    *   *Mapping to labels:*
        *   [02:04] SPEAKER_01: Knows history (EF, JPMorgan). Likely Kieren.
        *   [03:16] SPEAKER_03: Host.
        *   [05:06] SPEAKER_01: Continues history. "Nuka", "Luca". Mentions "boxing will" (transcription glitch).
        *   [05:54] SPEAKER_02: "I'm living CEO of blockups". If this is Kieren, then the labels are swapped. But at the end, SPEAKER_02 is Bob.
        *   *Maybe the transcript labels shifted.*
        *   Let's check [05:54] again. "I'm living CEO of blockups, Victor, creators of straddle. Yeah. And Victor Wong, uh, chief product officer of blockups. So sorry, but, but yeah. Um, Amos as well. Do you remember that?" This sounds like Kieren (CEO of BlockApps). Victor Wong is CPO.
        *   *But at the end:* SPEAKER_01 asks Bob where to find him. SPEAKER_02 answers as Bob.
        *   *Maybe SPEAKER_01 is Kieren and SPEAKER_02 is Bob, but the intro at [05:54] is mislabeled?* Or maybe SPEAKER_01 is Bob? No, [05:06] talks about EF and "boxing will" (Bob's name?) is there.
        *   *Let's look at [05:06] text again.* "boxing will so i'm head of ecosystem at Stratum cut change". This is clearly Bob's intro. It is inside SPEAKER_01's block.
        *   *Let's look at [05:54] text.* "I'm living CEO of blockups". This is Kieren's intro. It is inside SPEAKER_02's block.
        *   *Let's look at the end.*
            *   [49:09] SPEAKER_01: "Cool. And Bob, where can people find you?"
            *   SPEAKER_02: "So, yeah, I'm on Twitter. Same as my name, Bob at Summerville..." -> SPEAKER_02 is Bob.
            *   SPEAKER_01: "Karen? K. James Lubin on X..." -> SPEAKER_01 is Kieren (answering for himself).
        *   *Mapping:*
            *   SPEAKER_01 = Kieren James-Lubin.
            *   SPEAKER_02 = Bob Summerwill.
            *   SPEAKER_03 = Host (maybe Victor Wong?).
            *   SPEAKER_04 = Redwan Meslen.
    *   *Resolving the Intro Confusion:*
        *   [05:06] SPEAKER_01 (Kieren) is speaking. He mentions the EF, Nuka, Luca. Then the text "boxing will so i'm head of ecosystem at Stratum cut change" appears. This is clearly Bob's text. It's likely a transcript error where the file cut or the speakers switched labels.
        *   [05:54] SPEAKER_02 (Bob) starts speaking. But the text says "I'm living CEO of blockups". This is Kieren's text.
        *   *Hypothesis:* The segments for Kieren and Bob were swapped or mislabeled in the source for the intros.
        *   *Action:* I will correct the *content* to match the speaker identity based on the end of the recording (which is clearer: SPEAKER_01 is Kieren, SPEAKER_02 is Bob).
        *   *However*, I must keep the Speaker Labels (SPEAKER_01, SPEAKER_02) as provided in the input. I cannot change "SPEAKER_01" to "SPEAKER_02". I can only fix the text *inside*.
        *   *Dilemma:* If SPEAKER_01 is Kieren, but the text under SPEAKER_01 at [05:06] contains Bob's intro, and the text under SPEAKER_02 at [05:54] contains Kieren's intro...
        *   *Wait,* let's look closer at [05:06].
            *   SPEAKER_01: "...That was the technique. so that was a not quite the same group it was a larger group that's slightly different uh nuka was part of that luca was part of that um also um by the way we should introduce ourselves yeah i'm boxing will so i'm head of ecosystem at Stratum cut change."
            *   Maybe SPEAKER_01 *is* Bob? No, at the end SPEAKER_01 asks Bob questions.
            *   Maybe SPEAKER_01 is Bob and SPEAKER_02 is Kieren?
            *   Let's re-read the end.
            *   [49:09] SPEAKER_01: "Cool. And Bob, where can people find you?"
            *   [49:15] SPEAKER_02: "So, yeah, I'm on Twitter. Same as my name, Bob at Summerville..."
            *   [49:25] SPEAKER_01: "Karen? K. James Lubin on X..."
            *   Okay, here SPEAKER_02 is clearly Bob (speaking in first person "I'm Bob..."). SPEAKER_01 asks Bob. Then SPEAKER_01 answers for "Karen" (himself).
            *   So SPEAKER_01 is Kieren. SPEAKER_02 is Bob.
        *   *Back to [05:06] and [05:54].*
            *   [05:06] SPEAKER_01 (Kieren) talks about history. Then says "we should introduce ourselves". Then text says "I'm boxing will...". This is a transcript error. Kieren should say "I'm Kieren James-Lubin".
            *   [05:54] SPEAKER_02 (Bob) starts. The text says "I'm living CEO of blockups". This is a transcript error. Bob should say "I'm Bob Summerwill".
            *   *How to handle:* I cannot invent dialogue. I must correct the text.
            *   The text "boxing will so i'm head of ecosystem at Stratum" is Bob's intro. It is in SPEAKER_01's block.
            *   The text "living CEO of blockups" is Kieren's intro. It is in SPEAKER_02's block.
            *   If I fix the names inside the text to match the speaker label (based on end confirmation):
                *   SPEAKER_01 (Kieren): Change "boxing will" to "Kieren James-Lubin"? But the text says "head of ecosystem at Stratum" (Bob's job). This contradicts Kieren's job (CEO BlockApps).
                *   SPEAKER_02 (Bob): Change "living CEO of blockups" to "Bob Summerwill"? But the text says "CEO of blockups" (Kieren's job).
            *   *Alternative:* The speaker labels in the source might be wrong for the middle section. But I am instructed to "PRESERVE ALL speaker labels (SPEAKER_01, SPEAKER_02, etc. - do not add actual names)".
            *   *Constraint:* "Technical term spellings and capitalization... Proper names... MUST use EXACT spellings from the 'Key People' list".
            *   *Constraint:* "Output the corrected transcript... SPEAKER_XX:".
            *   *Decision:* I will assume the transcript labels are correct identifiers (SPEAKER_01, 02, etc.) but the text content (names/titles) is garbled or swapped.
            *   *Actually,* looking at [05:06], "boxing will" is "Bob Summerwill". "Stratum cut change" is "Stratum".
            *   Looking at [05:54], "living CEO of blockups" is likely "I'm Kieren, CEO of BlockApps". "Straddle" is "Stratum"? No, "straddle" might be "Stratum" again or something else. "Creators of straddle" -> "Creators of Stratum"? No, BlockApps created Burrow/Quorum stuff. Bob is at Stratum. Kieren is at BlockApps.
            *   *Let's look at the intro at [05:06] again.* "we should introduce ourselves yeah i'm boxing will so i'm head of ecosystem at Stratum cut change."
            *   *Let's look at [05:54] again.* "I'm living CEO of blockups, Victor, creators of straddle... And Victor Wong, uh, chief product officer of blockups."
            *   *Correction Strategy:* I will correct the garbled names to their canonical forms *if the context is clear*. If the text says "boxing will", I change to "Bob Summerwill". If the text says "living", I change to "Kieren".
            *   *Wait,* if SPEAKER_01 (Kieren) says "I'm Bob Summerwill" in the text, and I fix it to "Bob Summerwill", it makes Kieren say he is Bob. That's a logic error in the transcript.
            *   *Maybe the labels are just 1, 2, 3, 4 in order of appearance, but the people shuffled seats?*
            *   Let's look at [49:35] SPEAKER_03 asks "Vic...". This suggests SPEAKER_03 is the host asking everyone.
            *   If SPEAKER_01 is asking Bob at the end, SPEAKER_01 is not the main host. SPEAKER_03 is likely the host.
            *   Let's look at [01:38] SPEAKER_03. "So we are live... we have a very special guest today... In the same room... And you are a special guest, do you want to intro?" -> SPEAKER_03 is the host asking SPEAKER_01 (or whoever is next).
            *   [02:04] SPEAKER_01 responds "Sure... we have here today with us Redwan Meslen...". This sounds like the host introducing the guest. So maybe SPEAKER_01 is the host?
            *   But at the end, SPEAKER_01 asks "Bob where can people find you?". This implies SPEAKER_01 is a moderator/panelist asking another panelist.
            *   And SPEAKER_02 answers as Bob.
            *   If SPEAKER_01 is the host/moderator, why did he introduce Redwan in 3rd person at [02:04]? "We have here today with us Redwan". Maybe he's introducing him to the *other* panelists? Or the audience?
            *   Let's look at the names again. "Kieren James-Lubin", "Bob Summerwill", "Victor Wong", "Redwan Meslen".
            *   If SPEAKER_01 is the host, then at the end "Bob, where can people find you?" -> "Karen? K. James Lubin on X...". This implies the host (SPEAKER_01) is Kieren James-Lubin.
            *   If SPEAKER_01 is Kieren (host), then at [02:04] he introduced Redwan.
            *   At [05:06] SPEAKER_01 (Kieren) says "we should introduce ourselves... I'm boxing will (Bob)...". This is the error. Kieren says "I'm Bob".
            *   At [05:54] SPEAKER_02 (Bob) says "I'm living (Kieren)... CEO of blockups...". This is the error. Bob says "I'm Kieren".
            *   *Conclusion:* The transcript has the *introductions swapped* between SPEAKER_01 and SPEAKER_02 in the middle section, but the labels are consistent throughout.
            *   *Action:* I will correct the text to reflect the likely reality (SPEAKER_01 = Kieren, SPEAKER_02 = Bob), OR I will just correct the garbled text to what the text *says* (e.g., fix "boxing will" to "Bob Summerwill") even if it's logically wrong for the speaker?
            *   *Better Action:* Fix the names to the correct person based on the *context of the conversation flow* and the *end of the video*.
            *   *However*, strictly speaking, I should only edit the text. If the text has an error where A introduces themselves as B, should I fix it? Yes, "Technical term spellings and capitalization... Proper names...". If the ASR heard "boxing will" (which is Bob's name phonetic) but it was spoken by Kieren, it's a hallucination. But "living CEO" (Kieren) spoken by Bob is also a hallucination.
            *   It is highly probable that in the source audio, the speakers spoke in an order that got mixed up or the transcript editor swapped them.
            *   *Safest bet:* Correct "boxing will" to "Bob Summerwill" and "living" to "Kieren James-Lubin". Even if it makes the speaker label mismatch, I am preserving the text content. *But* the prompt says "PRESERVE ALL dialogue and content".
            *   Let's look at [05:54] again. "I'm living CEO of blockups, Victor, creators of straddle...". "Creators of straddle" -> Maybe "BlockApps"? "Straddle" is likely "Stratum" or "BlockApps".
            *   *Actually,* Bob is Head of Ecosystem at **Stratum**. Kieren is CEO of **BlockApps**.
            *   [05:06] says: "I'm [Bob]... head of ecosystem at Stratum".
            *   [05:54] says: "I'm [Kieren]... CEO of blockups".
            *   It is 100% certain the lines are swapped in the transcript relative to the speaker labels (if we trust the labels at the end).
            *   *My Approach:* I will correct the names and titles to the canonical ones ("Bob Summerwill", "Stratum", "Kieren James-Lubin", "BlockApps") and let the chips fall where they may with the labels. The user asks to fix proper names. "boxing will" -> "Bob Summerwill". "living" -> "Kieren James-Lubin". "blockups" -> "BlockApps". "Stratum cut change" -> "Stratum". "creators of straddle" -> "creators of BlockApps" (or keep "straddle" if uncertain, but "BlockApps" is the company). "Victor Wong" is CPO of BlockApps.
            *   *Note:* SPEAKER_02 says "And Victor Wong, uh, chief product officer of blockups". This fits BlockApps. So SPEAKER_02 *should* be Kieren (Victor's colleague). But at the end, SPEAKER_02 is Bob.
            *   *Is it possible SPEAKER_01 is Bob and SPEAKER_02 is Kieren?*
                *   [49:09] SPEAKER_01: "Bob, where can people find you?" -> If 01 is Bob, he wouldn't ask himself.
                *   [49:15] SPEAKER_02: "So, yeah, I'm on Twitter. Same as my name, Bob..." -> If 02 is Kieren, he wouldn't say "I'm Bob".
            *   *Conclusion:* The labels at the end are definitive. SPEAKER_01 = Kieren, SPEAKER_02 = Bob.
            *   *The text in the middle is swapped.*
            *   *Correction:* I will correct the text content to what the person *should* say if I can infer it, or just correct the garbled words.
            *   *Actually, looking at [05:06]:* "also um by the way we should introduce ourselves yeah i'm boxing will so i'm head of ecosystem at Stratum cut change." -> This paragraph is likely Bob interrupting or speaking out of turn, or the transcript is just messy.
            *   *Let's look at [05:54]:* "Stratum cut change" -> "Stratum". "blockups" -> "BlockApps". "straddle" -> "Stratum"? No, "creators of straddle" -> "creators of BlockApps".
            *   *I will clean the specific name errors based on the words in the text:*
                *   "boxing will" -> "Bob Summerwill"
                *   "Stratum cut change" -> "Stratum"
                *   "living" -> "Kieren James-Lubin" (based on context of CEO of BlockApps)
                *   "blockups" -> "BlockApps"
            *   *Wait,* if I do this, Kieren (01) will say "I'm Bob Summerwill" and Bob (02) will say "I'm Kieren James-Lubin". This is a transcript error I can't fix without swapping speaker labels, which I am not supposed to do ("do not add actual names", use SPEAKER_XX).
            *   *Alternative:* Maybe the prompt implies I should correct the names *if they refer to the speaker*.
            *   "I'm boxing will" -> The speaker identifies as Bob. If the speaker is Kieren, this is wrong.
            *   *Let's check the "Key People" list again.* "Kieren James-Lubin" is the name.
            *   *Maybe I should assume the transcript text is correct about who is speaking and the labels at the end are wrong?* Unlikely. The end conversation is very clear: "Bob where can people find you?" -> "I'm Bob". This is a Q&A. SPEAKER_01 asks, SPEAKER_02 answers.
            *   *Maybe SPEAKER_01 is the Host, SPEAKER_02 is Bob, SPEAKER_03 is Redwan?*
            *   Let's re-verify [02:04]. SPEAKER_01: "Sure. So, yeah, we have here today with us Redwan Meslen...". If 01 is Host/Kieren.
            *   [05:06] SPEAKER_01 (Host/Kieren) talks about history.
            *   [05:54] SPEAKER_02 (Bob) introduces himself? "I'm living CEO...". This text is Kieren's.
            *   *Okay, I will assume the text "I'm boxing will" belongs to SPEAKER_02 (Bob) and the text "I'm living CEO of BlockApps" belongs to SPEAKER_01 (Kieren).*
            *   *But they are placed in the wrong blocks.*
            *   *I will simply correct the transcribed words to their proper forms.* I will change "boxing will" to "Bob Summerwill". I will change "blockups" to "BlockApps". I will change "living" to "Kieren James-Lubin".
            *   *I will not swap the blocks.*
            *   *Wait,* if SPEAKER_01 says "I'm Bob Summerwill", and later SPEAKER_01 asks "Bob, where can people find you?", it's a contradiction.
            *   *Let's look at the text "boxing will".* It's a phonetic match for "Bob Summerwill".
            *   *Let's look at the text "living".* It's a bad phonetic match for "Kieren". "Kieren" -> "Keer-en". "Living" -> "Liv-ing". Not close. "I'm Kieren" -> "I'm living". Maybe.
            *   *Let's look at [05:54] again.* "I'm living CEO of blockups, Victor, creators of straddle." Maybe "I'm living" is "I'm leaving"? No. "I'm living" -> "I'm Kieren".
            *   *Is it possible SPEAKER_02 is Kieren?*
                *   If SPEAKER_02 is Kieren:
                *   [49:15] SPEAKER_02 says "I'm on Twitter. Same as my name, Bob at Summerville...".
                *   This makes SPEAKER_02 Bob.
                *   Contradiction confirmed: The labels are fixed at the end (01=Host/Kieren, 02=Bob). The middle text is swapped.
            *   *Decision:* I will correct the text *as it appears* but fix the names. So SPEAKER_01 will say "I'm Bob Summerwill" (correcting "boxing will") and SPEAKER_02 will say "I'm Kieren James-Lubin" (correcting "living"). This preserves the content of the transcript (garbled as it is) while fixing the specific name spellings requested. Swapping content between speaker blocks is risky if I'm not 100% sure of the audio flow, though I am 90% sure here. However, I will stick to the safer path of "fixing the text in place".
            *   *Actually,* looking at [05:06], the text "also um by the way we should introduce ourselves yeah i'm boxing will..." comes after "Nuka was part of that". Nuka (Nikola) worked with the EF. Kieren worked with the EF. This suggests SPEAKER_01 is indeed Kieren. So why does he say "I'm Bob"? Maybe he says "I'm with Bob"? Or "I'm not Bob"? Or the transcript is just "boxing will" -> "Bob Summerwill" (referring to the next speaker?).
            *   Let's assume the text "boxing will" is a mishearing of "Bob Summerwill" but Kieren is pointing to him? Or maybe Bob interrupted.
            *   *Okay, I'll just clean the text up.*
            *   "boxing will" -> "Bob Summerwill"
            *   "living" -> "Kieren James-Lubin"
            *   "blockups" -> "BlockApps"
            *   "Stratum cut change" -> "Stratum"
            *   "straddle" -> "BlockApps" (context: creators of BlockApps).
            *   "Karen" -> "Kieren".

**Step 4: Detailed Pass on Content**

*   **[00:02] SPEAKER_04:** "I use Restream. We try to use something and it streams on Twitter, I think YouTube and LinkedIn at the same time. So we're using StreamYard too. We're using StreamYard and I'm just double checking. We have been screwing around with different tools trying to find anything that seems a bit... Not all perfect, yeah. Yeah. I'll share the one. I don't know if you've tried this one, but this one is pretty cool. Pretty great. Because you're thinking, there must be good software for this, right? It's such a common need. Isn't there just an answer that just works? But the thing is, those platforms, they're not built with interoperability in mind. They don't like it. They want to track you in. Yeah, exactly. X especially. So that's against our vision. On X, there isn't even a means to download the bloody audio. Yeah, it's... Why would you want to download it? You know, like that's something, you know, I guess the next step in maybe like... You want to use it somewhere else? Are you seeing somebody else? Be able to own your data, you know, in all those platforms. Even own a query or just access, you know. Something I love about Google is like I can go, I can activate, you know, like the tracking, you know. But at least I can go in and say, what did I do that week? I went in front of that restaurant or that store. It was pretty nice. And I can go and see and check. I have access to that. It can be helpful. But most of the things, they have like thousands of data, but they don't even share it with you. Yeah, exactly. I find it quite, quite well."
    *   *Cleanup:* Remove "I think" (if filler). "track you in" -> "lock you in". " bloody audio" (keep). "own a query" -> "own a query" (keep? maybe "own a query" means data request? Keep). "quite, quite well" -> "quite interesting" or keep? Probably "quite well" is fine.

*   **[01:38] SPEAKER_03:** "501. Oh, yeah. We are live. So we are live. No, no, no, I'm ready. No, but that was a good cold intro, right? So we have a very special guest today, but a special format because all of us for Jane Joe Live in real life. In the same room. In the same room. So we're amazing. And you are a special guest, do you want to intro? Yeah."
    *   *Cleanup:* "501" (keep). "Jane Joe Live" (keep). "In real life".

*   **[02:04] SPEAKER_01:** "Sure. So, yeah, we have here today with us Redwan Meslen. Yes, exactly. Meslen, who is the executive director of the EA, the Enterprise Ethereum Alliance, which all of us at this table have had a hand and a part in over the years. The healthy run. Yes, exactly. So, yeah. It's eight years now. Since 2017, yeah. February 2017 was the launch date on the 28th. There was pre-work solidly before, at least three months, maybe more. There were meetings I was part of in December and January. I mean, those were the first big meetings, you know, with whatever, 30, 40 people, crazy amounts. But yeah, it really started probably at DevCon 2, really. It did? Yeah. So that was Shanghai, October. There was the kickoff meeting at the JPMorgan office, which was pretty big. They were the closed-door meetings at Microsoft. Right. So that public launch was February. It was February. But December, there was an internal one, and then JPMorgan..."
    *   *Names:* "Redwan Meslen" (Check list: "Redwan Meslen" is not in list, but "Redwan Meslen" is in transcript. Wait, prompt says "Known People (244)... Redwan Meslen" IS NOT in the list provided. Ah, the list is "Known People (244): Aaron Davis...". It lists "Aya Miyaguchi". It doesn't list Redwan. But SPEAKER_01 introduces him as "Redwan Meslen". I will use the spelling in the transcript as it's the intro, or check if "Redwan Meslen" is standard. It is likely "Redwan Meslen" or "Redwan Mesli"? Google says "Redwan Meslen" or "Redwan Mesli". I'll use "Redwan Meslen" as introduced. Wait, looking at the provided list again. "Redwan Meslen" is NOT there. I will use "Redwan Meslen" as introduced in the text.
    *   *Correction:* "The EA" -> "the EEA". "DevCon 2" -> "Devcon 2". "JPMorgan".

*   **[03:16] SPEAKER_03:** "was in January of 2017. But yeah, like a lot of those initial contacts have happened at DEVCON2 in October the previous year. Well, in the DEVCON2... Oh, yes. Yeah, so like basically, basically, there was a lot of conversations there about figuring out how to bring on enterprises too. And there were a lot of interested parties. And yeah, like, The group of people, which was I think about six people that were interested, met at like a Starbucks just off site. And, you know, that was sort of the idea formation thing about the... And then Matt spoke of NewCo held a little bar side event as well, which... Do we have some technical issues? I don't know. Oh, okay. Hold on a second. We have a technical issue, everybody. I will fix that. Oh, did I? I messed up the Twitter. You did a bad one. I did a bad one. So everyone, please join us on YouTube. Space is at 5 a.m. Right. Matt spoke, held a little event at one of the bars upstairs, which I went to, and there were various others there. I don't know if you went to that one as well. I didn't go to that one. So I think the main thing was that, yeah, so I think the main thing, I'm going to try to fix this right now on Twitter. Live technical support, see if I can resolve it right now. If not, I am."
    *   *Cleanup:* "DEVCON2" -> "Devcon 2". "Matt spoke of NewCo" -> "Matt Spoke of NewCo"? Or "Matt Spoke"? "Matt Spoke" is a name (Key People). Yes, "Matt Spoke" is in the list (or at least common knowledge, but I should stick to list if possible. "Aaron Davis...". Matt Spoke is not in the provided list. I'll correct capitalization). "NewCo" (keep).
    *   *Timestamp:* [03:16].

*   **[05:06] SPEAKER_01:** "I did choose a parallel in that because I was still working for the Ethereum Foundation at the time was that there was like an enterprise slack set up there, which was actually started by Vitalik, who afterwards said people kept badgering him about enterprise stuff. So at some point he just dumped the ball in a slack and ran away. That was the technique. so that was a not quite the same group it was a larger group that's slightly different uh nuka was part of that luca was part of that um also um by the way we should introduce ourselves yeah i'm boxing will so i'm head of ecosystem at
Stratum cut change. I was living CEO of blockups, Victor, creators of straddle. Yeah. And Victor Wong, uh, chief product officer of blockups. So sorry, but, but yeah. Um, Amos as well. Do you remember that? Oh yeah. We should check in on, I, I haven't thought about Amos until in like several years until the moment. So the interesting thing about what they were doing, so that was like some Taiwan bank consortium thing. Yep."
    *   *Major Cleanup:* This block is messy. It mixes Kieren's speech with Bob's intro?
    *   "Nuka" -> "Nuka" (Keep? Maybe "Nikola"? "Nuka" is likely Nukala Bhavani or someone? Not in list. Keep "Nuka").
    *   "Luca" -> "Luca" (Maybe Luca Cosmo? Keep).
    *   "boxing will" -> "Bob Summerwill".
    *   "Stratum cut change" -> "Stratum".
    *   *Wait,* the text continues: "I was living CEO of blockups, Victor...". This text appears right after "Stratum cut change". It looks like Bob interrupted, then maybe Victor or Kieren spoke?
    *   *Actually*, looking at the flow, "I was living CEO of blockups" is likely a different speaker. But the label is still SPEAKER_01.
    *   *Timestamp:* [05:06].
    *   *Hypothesis:* The transcript has merged two speaker turns into one block [05:06] without a label change.
    *   *Constraint:* "One timestamp per speaker paragraph".
    *   *Constraint:* "MERGE CONSECUTIVE SPEECH INTO PARAGRAPHS".
    *   *Conflict:* If two different people speak (SPEAKER_01 and SPEAKER_02) without a label in the raw transcript, but I know it's a new person, what do I do?
    *   The input has a label [05:06] SPEAKER_01: and then text that contains "I'm boxing will... I was living CEO...". This implies the transcript thinks it's one person or failed to split.
    *   However, at [05:54] there is a NEW label SPEAKER_02.
    *   So [05:06] to [05:54] is all under SPEAKER_01.
    *   The text "I'm boxing will... I was living CEO..." is in the middle.
    *   If I assume SPEAKER_01 is Kieren, and the text "I'm boxing will" (Bob) is an error, I should probably remove it or move it? No, I should preserve content.
    *   *Best Guess:* The transcript has the sequence wrong. But I will output it as a single paragraph block under SPEAKER_01 because that's the input structure (one label).
    *   *Wait,* "I was living CEO of blockups, Victor...".
    *   If SPEAKER_01 is Kieren, he might be saying "I'm Kieren... CEO of BlockApps".
    *   And "boxing will" might be a mishearing of "Bob's will"? Or Kieren saying "I'm with Bob"?
    *   Let's try to interpret "boxing will". Kieren says "I'm boxing will". Maybe "I'm Bob Summerwill"? No.
    *   Maybe Kieren says "I'm Kieren James-Lubin" and it got transcribed as "boxing will"? Unlikely phonetically.
    *   Maybe Kieren says "I'm Bob Summerwill" as a joke? Unlikely.
    *   *Let's look at the list again.* "Kieren James-Lubin".
    *   *Let's look at [05:54] SPEAKER_02.* "But then they did work on Chinese cryptography and stuff. They've got differing requirements, right? And Master Chain, which was in Russia, that was like a spare bank thing."
    *   *Wait*, I need to align the text blocks with timestamps correctly.
    *   Input:
        *   [05:06] SPEAKER_01: "I did choose... dumped the ball in a slack and ran away. That was the technique. so that was a not quite the same group it was a larger group that's slightly different uh nuka was part of that luca was part of that um also um by the way we should introduce ourselves yeah i'm boxing will so i'm head of ecosystem at Stratum cut change. I was living CEO of blockups, Victor, creators of straddle. Yeah. And Victor Wong, uh, chief product officer of blockups. So sorry, but, but yeah. Um, Amos as well. Do you remember that? Oh yeah. We should check in on, I, I haven't thought about Amos until in like several years until the moment. So the interesting thing about what they were doing, so that was like some Taiwan bank consortium thing. Yep."
        *   [05:54] SPEAKER_02: "But then they did work on Chinese cryptography and stuff. They've got differing requirements, right? And Master Chain, which was in Russia, that was like a spare bank thing."
    *   *Analysis:* The block at [05:06] ends with "Yep.".
    *   The block at [05:54] starts with "But then they did work...".
    *   Who says "But then they did work on Chinese cryptography"?
    *   Context: "Amos" (Amos is likely Amos Xu? A Taiwan bank?). "Master Chain" (Russia).
    *   This sounds like the conversation continuing.
    *   Is [05:06] SPEAKER_01 or SPEAKER_02? Label is SPEAKER_01.
    *   Is [05:54] SPEAKER_01 or SPEAKER_02? Label is SPEAKER_02.
    *   If SPEAKER_01 is Kieren, and SPEAKER_02 is Bob.
    *   Kieren talks about EF Slack.
    *   Then "I'm boxing will" (Bob).
    *   Then "I was living CEO" (Kieren).
    *   Then "Amos as well".
    *   Then "But then they did work..." (SPEAKER_02).
    *   It seems the [05:06] block contains a dialogue that flips back and forth or is very confused.
    *   *However*, I will treat [05:06] as one speaker turn (SPEAKER_01) and [05:54] as the next (SPEAKER_02).
    *   I will correct "boxing will" to "Bob Summerwill". I will correct "living" to "Kieren James-Lubin". I will correct "blockups" to "BlockApps". I will correct "straddle" to "BlockApps" (or Stratum? "creators of straddle" - Bob is at Stratum, Kieren at BlockApps. If "living" is Kieren, "creators of straddle" should be "creators of BlockApps").
    *   This results in SPEAKER_01 saying "I'm Bob... I'm Kieren...". I will just fix the words.

*   **[05:54] SPEAKER_02:** "because you you have uh you know i was not at the year at that time and so it's very interesting for me to you know what were the hopes and really excitement that you see you know you were part of those early conversations this was rated yeah i think companies it's like a pretty it was a pretty big event you know yeah as you mentioned you know like gp morgan and everything all those big names coming into the ecosystem".
    *   *Wait,* looking at the input provided in the prompt:
        *   The text starting "because you you have..." seems to belong to SPEAKER_04? Or maybe SPEAKER_02?
        *   Let's trace the input provided in the prompt carefully.
        *   Input:
            *   [05:54] SPEAKER_02: "But then they did work on Chinese cryptography and stuff. They've got differing requirements, right? And Master Chain, which was in Russia, that was like a spare bank thing."
            *   *Wait, I missed a block.*
            *   Let's look at the raw input again.
            *   [05:06] SPEAKER_01: ... "Yep."
            *   [06:23] SPEAKER_01: "But then they did work on Chinese cryptography and stuff. They've got differing requirements, right? And Master Chain, which was in Russia, that was like a spare bank thing."
            *   [06:42] SPEAKER_04: "because you you have uh..."
            *   *Correction:* My previous mapping was wrong. I need to look at the Raw Transcript provided in the prompt.
            *   Let's look at the Raw Transcript again.
            *   [05:06] SPEAKER_01: ... "Yep."
            *   [05:54] SPEAKER_02: "Stratum cut change. I was living CEO of blockups..." -> **Wait, this is in the prompt!**
            *   Let's re-read the prompt's Raw Transcript carefully.
            *   [05:06] SPEAKER_01: "I did choose... Nuka... Luca... also um by the way we should introduce ourselves yeah i'm boxing will so i'm head of ecosystem at"
            *   [05:54] SPEAKER_02: "Stratum cut change. I was living CEO of blockups, Victor, creators of straddle..."
            *   **Ah!** The transcript splits the sentence across [05:06] and [05:54]!
            *   SPEAKER_01 says: "also um by the way we should introduce ourselves yeah i'm boxing will so i'm head of ecosystem at"
            *   SPEAKER_02 says: "Stratum cut change. I was living CEO of blockups..."
            *   This implies SPEAKER_01 and SPEAKER_02 are talking over each other or the cut is mid-conversation.
            *   BUT, SPEAKER_01 cuts off at "at". SPEAKER_02 starts with "Stratum". This looks like SPEAKER_01 is Bob (identifying himself) and SPEAKER_02 is Kieren (identifying himself).
            *   If SPEAKER_01 says "I'm boxing will (Bob)...", and SPEAKER_02 says "I'm living (Kieren)...".
            *   This matches the logic that SPEAKER_01=Bob, SPEAKER_02=Kieren.
            *   *But earlier I concluded SPEAKER_01=Kieren, SPEAKER_02=Bob based on the end.*
            *   Let's re-check the end. [49:09] SPEAKER_01: "Bob, where can people find you?". [49:15] SPEAKER_02: "So, yeah, I'm on Twitter... Bob...".
            *   If SPEAKER_01=Bob, he wouldn't ask "Bob where...".
            *   So at the end, SPEAKER_01 is NOT Bob.
            *   Therefore, the split at [05:06]/[05:54] where SPEAKER_01 introduces as Bob is a label error or the labels swap later.
            *   *Or*, maybe SPEAKER_01 introduces *Bob* sitting next to him? "We have here today with us... Bob Summerwill". (Note: In [02:04] he introduces Redwan. Maybe he introduces Bob here).
            *   "by the way we should introduce ourselves yeah i'm boxing will so i'm head of ecosystem at" -> If SPEAKER_01 is Kieren, he might be introducing Bob. "He is Bob...". But it says "I'm".
            *   *Most likely:* The labels 01 and 02 are swapped in the middle section, or consistent but the text is swapped.
            *   *Decision:* I will follow the labels. SPEAKER_01 is the label. SPEAKER_02 is the label.
            *   I will correct the text inside. "boxing will" -> "Bob Summerwill". "living" -> "Kieren James-Lubin".
            *   If this results in SPEAKER_01 saying "I'm Bob", so be it. The user provided labels 01/02. I should stick to them.
            *   *Wait*, if I look at [05:06] in the prompt: "boxing will so i'm head of ecosystem at". This is cut off.
            *   [05:54] in the prompt: "Stratum cut change. I was living CEO of blockups...".
            *   This looks like one continuous speech: "I'm Bob Summerwill, I'm head of ecosystem at Stratum. I was...". But the speaker changes from 01 to 02?
            *   Or maybe SPEAKER_01 says "I'm Bob...", stops. SPEAKER_02 says "Stratum...". (Finishing the sentence?)
            *   Or maybe the labels are just wrong.
            *   *Let's look at the prompt text again.* The prompt text for [05:06] ends with "at". The prompt text for [05:54] starts with "Stratum cut change."
            *   If SPEAKER_01 says "I'm Bob... head of ecosystem at", and SPEAKER_02 continues "Stratum...", that implies 01 is Bob.
            *   If 01 is Bob, then at the end 01 asks "Bob where...". This is a contradiction.
            *   *However*, maybe the end labels are different? [49:09] SPEAKER_01... [49:15] SPEAKER_02...
            *   Maybe the person identified as SPEAKER_01 at the start is different from SPEAKER_01 at the end? (e.g., fixed ID vs dynamic ID). Usually fixed.
            *   *Let's assume the labels are just arbitrary IDs 1, 2, 3, 4 assigned by the diarization system.*
            *   Diarization often splits a single speaker into 1 and 2 if their voice changes or there's noise.
            *   *But* here they are clearly distinct people (Redwan, Host, etc.).
            *   *Let's check the "Key People" list spellings again.*
            *   "Bob Summerwill".
            *   "Kieren James-Lubin".
            *   *Okay, I will just output the text with corrections.*
            *   I will merge [05:06] and [05:54] text if they look like a continuation? No, the timestamps are different. [05:06] and [05:54] is a 48 second gap. It's not a continuation. It's a new speaker.
            *   So SPEAKER_01 says "I'm Bob...". Then silence. Then SPEAKER_02 says "Stratum...". This is disjointed.
            *   Maybe SPEAKER_01 says "I'm Bob..." (referring to himself?).
            *   Maybe SPEAKER_02 says "Stratum..." (referring to Stratum?).
            *   *Actually,* looking at [05:06]: "I'm boxing will so i'm head of ecosystem at". Then [05:54]: "Stratum cut change." -> This is extremely suspicious. It looks like the same sentence split across speakers.
            *   If I edit it, I should probably keep them separate but fix the text.
            *   Let's assume the transcript is garbage there and just fix the words. "Stratum cut change" -> "Stratum". "boxing will" -> "Bob Summerwill".

*   **Technical Terms:**
    *   "ethereum" -> "Ethereum".
    *   "defi" -> "DeFi".
    *   "dapp" -> "dapp".
    *   "blockchain" -> "blockchain".
    *   "consensus" -> "consensus".
    *   "tokenization" -> "tokenization".
    *   "stablecoin" -> "stablecoin".
    *   "CBDCs" -> "CBDCs".
    *   "ISO 222" -> "ISO 20022" (The transcript says "ISO 222", but SWIFT uses ISO 20022. "222" is a clear speech error. I should correct to "ISO 20022").
    *   "RTGS" -> "RTGS".
    *   "M0, M1, M2" -> "M0, M1, M2".
    *   "ZKSync" -> "zkSync".
    *   "L2" -> "Layer 2" or "L2".
    *   "L1" -> "Layer 1" or "L1".
    *   "DTCC" -> "DTCC".
    *   "Swift" -> "SWIFT" (Usually all caps).
    *   "Hyperledger" -> "Hyperledger".
    *   "Fabric" -> "Fabric".
    *   "Burrow" -> "Burrow".
    *   "EVM" -> "EVM".
    *   "DevCon" -> "Devcon".
    *   "Quorum" -> "Quorum".
    *   "Corda" -> "Corda".
    *   "Besu" -> "Besu" (mentioned in list, not sure if in text).

*   **Specific Text Fixes:**
    *   "g p morgan" -> "JPMorgan".
    *   "straddle" -> "BlockApps" (if referring to the company) or keep "Straddle"? Context: "creators of straddle". BlockApps created Burrow. Bob is at Stratum. "Straddle" is likely "BlockApps" or "Stratum". Given "CEO of BlockApps", "Straddle" is likely a mishearing of "BlockApps".
    *   "living" -> "Kieren James-Lubin".
    *   "boxing will" -> "Bob Summerwill".
    *   "stratum cut change" -> "Stratum".
    *   "Jane Joe Live" -> Keep "Jane Joe Live" (phonetic, likely "Bankless" or similar, but "Jane Joe" is distinct). "ZK"?
    *   "genius act" -> "FIT21" (Financial Innovation and Technology for the 21st Century Act)? "Genius" -> "FIT21"? "charity act"? "Genius act was signed in July". FIT21 passed the House in May. There is "Paycheck Protection Program"? No. "Stablecoin Act"? "Genius" sounds like "FIT21"? Or "Genus"? "Stable Act"?
    *   *Check:* "charity act". Maybe "Lummis-Gillibrand"? No.
    *   "Genius act" -> Maybe "MiCA" (EU)? No, US. July 2024?
    *   Maybe "Generative"?
    *   *Wait*, "genius act" sounds like "FIT21" (Fit Twenty-One). "Genius" and "FIT21" are not close.
    *   How about "ETC"?
    *   "charity act" -> "Stablecoin Act"?
    *   Let's look for "July" and "act". "FIT21" passed House in May. Senate in July? No.
    *   "Market Structure"?
    *   "Payment Stablecoin Act"?
    *   "Genius" -> "Jenius"? No.
    *   Maybe "The Genesis Act"?
    *   *Actually*, maybe it's "The Financial Innovation Act"?
    *   Let's stick to "Genius Act" or "charity act" if unsure. Or "FIT21" if I'm confident? "FIT21" is the big one.
    *   "Genius" -> "FIT". "Charity" -> "Twenty-One"? No.
    *   Maybe "The 21st Century Act"? (FIT21).
    *   Let's check "Genius Act" phonetic match. "Jen-nius". "Fit-Twenty-One". Not close.
    *   "Lummis-Gillibrand"? No.
    *   "MiCA" (Europe).
    *   Let's try "SAFE Act"?
    *   *Correction:* I will leave it as "Genius Act" but capitalize "Act". Or maybe "The FIT21 Act". "Genius" is very wrong. Let's search "July act blockchain".
    *   *Result:* "Financial Innovation and Technology for the 21st Century Act" (FIT21). Passed House May 2024. Senate action?
    *   Maybe "The Stablecoin Act"?
    *   I'll stick to "Genius Act" as I can't be sure. Or "financial act".
    *   *Wait*, "charity act". Maybe "Stablecoin" -> "Charity"? No.
    *   "Genius" -> "U.S."?
    *   Let's look at the text: "genius act was signed in July... or something like this charity act."
    *   "charity" sounds like "Stablecoin". "genius" sounds like "Genesis"?
    *   Maybe "The Genesis Act"?
    *   I will transcribe as "the FIT21 Act" if I feel bold, otherwise "the Genus Act".
    *   Actually, let's look at the speaker. "Redwan Meslen". He talks about regulation.
    *   I'll use "the FIT21 Act" (FIT21) as it's the most likely candidate for major legislation in that timeframe. "Genius" might be a hallucination of "FIT". "Charity" -> "Twenty-one"? No.
    *   Let's just correct "genius" to "FIT21" and "charity act" to "or something like this". "or something like this FIT21".
    *   No, I'll play it safe: "the Financial Innovation Act".

*   **Timestamps:** Keep exact.

*   **Formatting:**
    *   **[MM:SS] SPEAKER_XX:** Text.
    *   Merge paragraphs if same speaker.
    *   Timestamp at start of merged block.

Let's do the processing.

**Raw Transcript Analysis:**
- **[00:02] SPEAKER_04:** Streaming issues. "track you in" -> "lock you in".
- **[01:38] SPEAKER_03:** Intro. "Jane Joe Live".
- **[02:04] SPEAKER_01:** Intro Redwan Meslen. EEA history. Devcon 2. JPMorgan.
- **[03:16] SPEAKER_03:** History. Starbucks. Matt Spoke.
- **[05:06] SPEAKER_01:** EF Slack. Vitalik. Nuka, Luca. Intro "boxing will" (Bob).
- **[05:54] SPEAKER_02:** Continuation? "Stratum cut change" (Stratum). "living CEO" (Kieren). "blockups" (BlockApps). "straddle" (BlockApps). Victor Wong. Amos.
- **[06:23] SPEAKER_01:** Chinese cryptography. Master Chain.
- **[06:42] SPEAKER_04:** "because you you have...". (Redwan speaks).
- **[07:07] SPEAKER_01:** "and and what were the hopes...". ConsenSys. Enterprise engagement.
- **[07:53] SPEAKER_02:** Forking Ethereum. Quorum. Jeff Wilkie. ErisDB. Monax. Hyperledger Burrow.
- **[09:01] SPEAKER_02:** Work together. Standard. Client. ConsenSys consulting.
- **[09:30] SPEAKER_03:** Siloed work. Private networks.
- **[10:11] SPEAKER_01:** Customers and builders. Vendor lock. Hyperledger.
- **[11:36] SPEAKER_02:** Shared code base vs standardization. IBM/Oracle nightmares. Corda, Fabric.
- **[12:21] SPEAKER_01:** Proprietary. IBM R3. Corda.
- **[12:49] SPEAKER_02:** Call with 300 people.
- **[13:14] SPEAKER_03:** Santander. USD on chain (stablecoin).
- **[13:38] SPEAKER_04:** Innovation labs. Sibos.
- **[14:30] SPEAKER_03:** Sibos. Digital asset tokenization. ShredFi (TradFi?).
- **[14:55] SPEAKER_04:** Sibos description. SWIFT. ISO 222 -> ISO 20022.
- **[15:21] SPEAKER_02:** SWIFT as coop. Buy shares.
- **[15:51] SPEAKER_04:** Payments. Clearing house.
- **[16:51] SPEAKER_02:** Finance clearing via messaging. Not like crypto.
- **[17:14] SPEAKER_04:** Delivery vs payment. Atomic transaction.
- **[18:21] SPEAKER_02:** SWIFT is not payment mechanism. FX example.
- **[19:07] SPEAKER_04:** SWIFT format. Envelope. Correspondent banking.
- **[19:58] SPEAKER_03:** IOUs. Handshakes.
- **[20:27] SPEAKER_04:** Ledger entry. RTGS. M0, M1, M2. Securities. Stablecoins/CBDCs.
- **[22:52] SPEAKER_04:** Ethereum Foundation protected the baby. Scalability, privacy, composability, interoperability.
- **[25:03] SPEAKER_03:** Knowledge gap.
- **[25:28] SPEAKER_04:** Trillions vs billions. Education. Contract size limit. Stack overflow. L1/L2 explanation.
- **[29:34] SPEAKER_03:** Supply demand.
- **[30:03] SPEAKER_02:** Back office vs top line. Nike NFTs. Digital asset treasuries.
- **[31:45] SPEAKER_04:** Operational optimization. Capital flow. Intermediaries. RWA convergence. Aave, Figure.
- **[34:57] SPEAKER_03:** DeFi + TradFi. Institutions feelings.
- **[35:27] SPEAKER_04:** Ethereum standard. Multi-chain. Circle ARC paper. ZKSync. Wikipedia analogy.
- **[37:32] SPEAKER_01:** EVM vs non-EVM. Canton. Solana. Ripple.
- **[38:01] SPEAKER_04:** Canton network. Quorum B2. Ecosystem size.
- **[39:25] SPEAKER_03:** Solana. Ripple. Sibos story.
- **[40:17] SPEAKER_03:** Ripple conference. Vitalik speaking.
- **[41:32] SPEAKER_01:** Corda Selaena. Fabric.
- **[41:55] SPEAKER_04:** Fabric in central banks. BIS Project Agora.
- **[42:46] SPEAKER_03:** Fabric removal?
- **[43:06] SPEAKER_01:** IBM bridge Fabric X to Ethereum. EVM integration.
- **[44:21] SPEAKER_04:** EVM standard. Sibos panels.
- **[45:32] SPEAKER_01:** Router analogy. Modular codebases. EF Enterprise team.
- **[47:32] SPEAKER_04:** No CEO of Ethereum. Mission of EEA.
- **[49:09] SPEAKER_01:** Wrap up. Where to find EEA. Redwan. Bob.
- **[49:35] SPEAKER_03:** Vic.

**Refining the Text:**
- "Jane Joe Live" -> Keep.
- "Redwan Meslen" -> Keep.
- "boxing will" -> "Bob Summerwill".
- "Stratum cut change" -> "Stratum".
- "living" -> "Kieren James-Lubin".
- "blockups" -> "BlockApps".
- "straddle" -> "BlockApps" (Context: creators of...).
- "ISO 222" -> "ISO 20022".
- "ShredFi" -> "TradFi".
- "genius act" -> "FIT21" (or "the Financial Innovation Act"). I will use "FIT21" as it's the specific term. "charity act" -> "or something like this".
- "down for a trash buy" -> "a co-op" (SWIFT).
- "K. James Lubin" -> "Kieren James-Lubin".
- "Vic, V-I-C" -> "Vic".
- "Summerville" -> "Summerwill".

**Speaker Labels:**
The prompt says "PRESERVE ALL speaker labels (SPEAKER_01, SPEAKER_02, etc. - do not add actual names)".
So I will NOT change SPEAKER_01 to Kieren. I will just fix the text *inside*.

**Final Check of "ISO 222":**
SWIFT migration is to ISO 20022. ISO 22222 is "Personal financial planning". ISO 222 is likely a misrecognition of "20022". I will correct to "ISO 20022".

**Final Check of "Genius Act":**
"Genius act was signed in July".
The "Financial Innovation and Technology for the 21st Century Act" (FIT21) passed the House in May.
In July 2024, the Senate Banking Committee held a hearing on stablecoins?
Maybe "Genius" is "Generative AI"?
Maybe "Genius" is "Jeanius"?
Maybe "The Payment Stablecoin Act"?
Actually, "The FIT21 Act" was signed? No, passed House.
Maybe "The Markets in Crypto-Assets (MiCA)" was fully implemented? MiCA was passed 2023.
Maybe "The Electronic Transactions Act"?
Let's just use "the Financial Innovation Act" to be safe and descriptive, or "the FIT21 Act". I'll go with "the FIT21 Act" as it's the standard industry term people refer to.

**Formatting:**
I will use bold for the speaker labels.
I will merge consecutive paragraphs for the same speaker (e.g. [05:06] and [05:54] if they are the same speaker label? No, they are different labels. I will not merge different speaker labels. But I will merge blocks within the SAME timestamp block if there are line breaks? The input doesn't have line breaks within a speaker block, just one block. The output format says "Each speaker turn can be multiple paragraphs". This implies if the input has multiple paragraphs for one speaker, I merge them. Here, each speaker turn is one block.

Wait, looking at the input:
`**[00:02] SPEAKER_04:** I use Restream. We try to use something and it streams on Twitter, I think YouTube and LinkedIn at the same time. So we're using StreamYard too. We're using StreamYard and I'm just double checking. We have been screwing around with different tools trying to find anything that seems a bit... Not all perfect, yeah. Yeah. I'll share the one. I don't know if you've tried this one, but this one is pretty cool. Pretty great. Because you're thinking, there must be good software for this, right? It's such a common need. Isn't there just an answer that just works? But the thing is, those platforms, they're not built with interoperability in mind. They don't like it. They want to track you in. Yeah, exactly. X especially. So that's against our vision. On X, there isn't even a means to download the bloody audio. Yeah, it's... Why would you want to download it? You know, like that's something, you know, I guess the next step in maybe like... You want to use it somewhere else? Are you seeing somebody else? Be able to own your data, you know, in all those platforms. Even own a query or just access, you know. Something I love about Google is like I can go, I can activate, you know, like the tracking, you know. But at least I can go in and say, what did I do that week? I went in front of that restaurant or that store. It was pretty nice. And I can go and see and check. I have access to that. It can be helpful. But most of the things, they have like thousands of data, but they don't even share it with you. Yeah, exactly. I find it quite, quite well.`

This is one block. I will keep it as one paragraph (or split if natural? "Output should contain ONLY the formatted transcript... Each speaker turn can be multiple paragraphs...").
I will split into paragraphs for readability if the topic shifts.
e.g. "I use Restream... Yeah. I'll share the one... But the thing is..."
I will break it up.

**Double Check: Names.**
"Matt spoke" -> "Matt Spoke".
"Amos" -> "Amos".
"Nuka" -> "Nuka".
"Luca" -> "Luca".
"Jeff Wilkie" -> "Jeff Wilcke" (Ethereum co-founder? Yes. Jeff Wilcke).
"Vitalik" -> "Vitalik".

**Ready.****[00:02] SPEAKER_04:** I use Restream. We try to use something and it streams on Twitter, I think YouTube and LinkedIn at the same time. So we're using StreamYard too. We're using StreamYard and I'm just double checking. We have been screwing around with different tools trying to find anything that seems a bit... Not all perfect, yeah. Yeah. I'll share the one. I don't know if you've tried this one, but this one is pretty cool. Pretty great. Because you're thinking, there must be good software for this, right? It's such a common need. Isn't there just an answer that just works? But the thing is, those platforms, they're not built with interoperability in mind. They don't like it. They want to lock you in. Yeah, exactly. X especially. So that's against our vision. On X, there isn't even a means to download the bloody audio. Yeah, it's... Why would you want to download it? You know, like that's something, you know, I guess the next step in maybe like... You want to use it somewhere else? Are you seeing somebody else? Be able to own your data, you know, in all those platforms. Even own a query or just access, you know. Something I love about Google is like I can go, I can activate, you know, like the tracking, you know. But at least I can go in and say, what did I do that week? I went in front of that restaurant or that store. It was pretty nice. And I can go and see and check. I have access to that. It can be helpful. But most of the things, they have like thousands of data, but they don't even share it with you. Yeah, exactly. I find it quite interesting.

**[01:38] SPEAKER_03:** 501. Oh, yeah. We are live. So we are live. No, no, no, I'm ready. No, but that was a good cold intro, right? So we have a very special guest today, but a special format because all of us for Jane Joe Live in real life. In the same room. In the same room. So we're amazing. And you are a special guest, do you want to intro? Yeah.

**[02:04] SPEAKER_01:** Sure. So, yeah, we have here today with us Redwan Meslen. Yes, exactly. Meslen, who is the executive director of the EEA, the Enterprise Ethereum Alliance, which all of us at this table have had a hand and a part in over the years. The healthy run. Yes, exactly. So, yeah. It's eight years now. Since 2017, yeah. February 2017 was the launch date on the 28th. There was pre-work solidly before, at least three months, maybe more. There were meetings I was part of in December and January. I mean, those were the first big meetings, you know, with whatever, 30, 40 people, crazy amounts. But yeah, it really started probably at Devcon 2, really. It did? Yeah. So that was Shanghai, October. There was the kickoff meeting at the JPMorgan office, which was pretty big. They were the closed-door meetings at Microsoft. Right. So that public launch was February. It was February. But December, there was an internal one, and then JPMorgan...

**[03:16] SPEAKER_03:** was in January of 2017. But yeah, like a lot of those initial contacts have happened at Devcon 2 in October the previous year. Well, in the Devcon 2... Oh, yes. Yeah, so like basically, basically, there was a lot of conversations there about figuring out how to bring on enterprises too. And there were a lot of interested parties. And yeah, like, the group of people, which was I think about six people that were interested, met at like a Starbucks just off site. And, you know, that was sort of the idea formation thing about the... And then Matt Spoke of NewCo held a little bar side event as well, which... Do we have some technical issues? I don't know. Oh, okay. Hold on a second. We have a technical issue, everybody. I will fix that. Oh, did I? I messed up the Twitter. You did a bad one. I did a bad one. So everyone, please join us on YouTube. Space is at 5 a.m. Right. Matt Spoke held a little event at one of the bars upstairs, which I went to, and there were various others there. I don't know if you went to that one as well. I didn't go to that one. So I think the main thing was that, yeah, so I think the main thing, I'm going to try to fix this right now on Twitter. Live technical support, see if I can resolve it right now. If not, I am.

**[05:06] SPEAKER_01:** I did choose a parallel in that because I was still working for the Ethereum Foundation at the time was that there was like an enterprise Slack set up there, which was actually started by Vitalik, who afterwards said people kept badgering him about enterprise stuff. So at some point he just dumped the ball in a Slack and ran away. That was the technique. So that was a not quite the same group it was a larger group that's slightly different. Nuka was part of that. Luca was part of that. Also, um, by the way we should introduce ourselves. Yeah, I'm Bob Summerwill, so I'm head of ecosystem at Stratum.

**[05:54] SPEAKER_02:** I was Kieren James-Lubin, CEO of BlockApps, Victor, creators of BlockApps. Yeah. And Victor Wong, uh, chief product officer of BlockApps. So sorry, but, but yeah. Um, Amos as well. Do you remember that? Oh yeah. We should check in on, I, I haven't thought about Amos until in like several years until the moment. So the interesting thing about what they were doing, so that was like some Taiwan bank consortium thing. Yep.

**[06:23] SPEAKER_01:** But then they did work on Chinese cryptography and stuff. They've got differing requirements, right? And Master Chain, which was in Russia, that was like a spare bank thing.

**[06:42] SPEAKER_04:** Because you, you know, I was not at the year at that time and so it's very interesting for me to, you know, what were the hopes and really excitement that you see, you know, you were part of those early conversations. This was great, yeah. I think companies it's like a pretty, it was a pretty big event, you know. Yeah, as you mentioned, you know, like JPMorgan and everything, all those big names coming into the ecosystem.

**[07:07] SPEAKER_01:** And what were the hopes and and really like the overall like atmosphere you know when the EEA was created like eight years ago? Yeah, well, I mean, so I mean, ConsenSys were very critical as well because, you know, they were doing a load of the enterprise like engagement stuff, right? They've got many, many companies like starting to get interested in hey, you know, we want to do a pilot, we want to get involved. So ConsenSys were doing a lot of those. So they ended up having a lot of those connections and bringing those those in together. But yeah, you, you know, over those months you, you really have like they've got a hell of a lot of momentum. Yeah, really, really quick. So the observation during Devcon 2 when the idea was hatched was basically that...

**[07:53] SPEAKER_02:** At least at the innovation lab level, a lot of the enterprises were just using and forking their own flavor of Ethereum. They had like hacked their own consensus algorithms and security and many guests, many guests. Indeed. We learned later that like...

**[08:13] SPEAKER_01:** Like a lot of JP Morgan's Quorum was initially built by Jeff Wilcke. He had like some kind of, and that was not announced at the time of Devcon 2. That was still behind the scenes for a few months, but happened just before the EEA started. But, yeah, you've got all of this stuff brewing up, I mean, for years earlier. Like, if you think of like ErisDB that became Monax, that became Hyperledger Burrow. So that was a permissioned Ethereum client off POC 5 pre-mainnet, mid-2014, of sticking in Tendermint onto an EVM. So yeah, like, you know, it was all a bit smashed apart.

**[09:01] SPEAKER_02:** But it was like the time is right for us to work together because we've all got the same needs. Us too. We had our own client and they got used in a bunch of the ConsenSys consulting engagements at that time. And we started even then kind of tuning it for enterprise. And so I guess the idea was like, well, maybe enterprises won't adopt if there isn't a standard for all of this new stuff that they need that's above and beyond the base standard.

**[09:30] SPEAKER_03:** Well, I think clients I, I think it was even beyond that. Like there was just tons of technical work going on in each individual company's siloed to get, I think like Ethereum to do what they wanted to do in a private way. Yeah, so everyone was like holding on these things and what came out of that, those early conversations at Devcon was wait, like while doing similar things maybe if we all kind of work together we could do it faster and get this up faster. And that was all around private Ethereum. And I guess also like a marriage between like...

**[10:11] SPEAKER_01:** Kind of customers of these things and builders. Yeah, of saying you've got all these kind of startup kind of companies that are making Ethereum things and you've obviously got big demand from really major enterprises to have this but there's, but yeah, on that standardization side there was like nothing and it's like you're all going to get vendor locked like instantly and it'll all just be arbitrarily different and painful and horrible. So let's try and work out because well at some point as well with with Quorum it was kind of like you know are we going to like collaboratively do code bases as well? Uh, like, you know, Hyperledger was another, was another piece into this. Is that is that a few months earlier I've spent a bunch of time working on C++ relicensing C++ client to get back to Apache 2 so it could have been contributed into Hyperledger and we could have like gathered around that. That fucked up. So the EEA was kind of a backup, I guess, of like, right, we can't have this grand fusion, but there's enough happening on the Ethereum side that we can at least get all the Ethereum, you know, pieces together. And then, yeah, I guess it went quite quickly from, okay, we don't want to straight compete with Hyperledger.

**[11:36] SPEAKER_02:** Having a shared code base also kind of like screws up the companies. So I think, let me, you know, in the spirit of spiciness, I think the enterprise users would have preferred a shared code base and they wanted to commoditize any difference among the startups out of existence so that they could never be vendor locked again. They've had these horrific, you know, IBM nightmares, Oracle nightmares over the years, and they're just like, not this time. We're not going to live through this. I mean, also, you know, you have got that market pressure, right, of Corda coming out, of IBM launching Fabric. They were worried it would end up that kind of...

**[12:21] SPEAKER_01:** Those were nominally open source, but quite proprietary. So those were both shooting for release in February 2017. So it's that kind of timeline is like, right, we've got to get our shit together to be able to do like an Ethereum product thing that can have some hope against IBM, R3, Corda. DA at that time, I remember one of our prominent enterprise user EEA members said...

**[12:49] SPEAKER_02:** They've got a call with you know 300 people on it every week trying to sell into the big banks let's say right. And, um, it's funny that all of the like Ethereum just survived all of this more or less not paying any attention and like you know the this this competition kind of came in. Well, I think there was another parallel thing that was happening at that Devcon.

**[13:14] SPEAKER_03:** Really were like the first, like the kind of enterprise use cases we talked about today. Like for example, Santander talked about, you know, US dollar on chain, which we all recognize as a stablecoin now. But you see, Victor, I think that's a very cool parallel. Like you've set the stage pretty well for like, you know, where it's coming from.

**[13:38] SPEAKER_04:** Yeah. And where it started, you mentioned, you know, innovation labs, like starting to contribute to some codes. We've known like the use cases that blockchain and Ethereum can solve for a long time. But it's only actually now and it's been for probably like for the last year that things have been really changing drastically. And to take, you know, like your words for when you say innovation labs. It's not Innovation Labs anymore looking at how they implement blockchain in their ecosystem. It's really an executive team that say, hey, we want to plan what is the production, like how we get it to market. Thankfully, they're scared now. So they better move. I don't know if it's like... But there was some interesting talk when we were at Sibos, like the SWIFT conference. Yeah, we should mention that because...

**[14:30] SPEAKER_03:** You were just at Sibos and you're dealing with like what we think of as TradFi institutional players and that's, you know, where you have a lot of communication. So like what were your impressions about where they're at with that because that's the other side that we talk about. The digital asset tokenization is definitely a hot topic. Everyone is looking because...

**[14:55] SPEAKER_04:** They know it's happening. They want to be involved. And it's, now especially like there is less, there is less like regulatory, you know, um, the listeners may not know what Sibos is. Oh yeah, so Sibos is the is the big SWIFT conference. SWIFT, if you're not familiar, is uh, it's a messaging system that a lot of 11,000 financial institutions around the world use. It's actually a co-op. It's a doubt.

**[15:21] SPEAKER_02:** Kudos to Danielle from ConsenSys who said that to me once. It is a doubt. Although it's like, can we buy in now? I feel like, you know, it's not. Yeah. The token is having probably a bank license. The London Metal Exchange is like this too. It's like you want to sign up, you got to like buy a bunch of shares and like, you know, then there's an annual fee and whatnot. And you have to like put someone there all the time. You have to join the trade guild.

**[15:51] SPEAKER_04:** Yes. Exactly. And so that big conference is a big meetup of payments, I would say, every year. So you have all the big financial institutions, also global financial institutions like clearing house, settlements, like your work, etc. But also like all the banks. And they gather here and there is a lot of conversation. What is very interesting is actually Sibos and SWIFT is a very kind of standard organization. Because what they do is how we make sure we send messaging across all of us that everyone is sure is going to understand. And so they used to have a different kind of messaging format, and recently now they're migrating to something new, which is ISO 20022. Okay. Which is, if you want to go and dive deeper into this, this is really how every financial institution wants to discuss. They've been working on that spec for a long time, and that's how anything that can touch finance...

**[16:51] SPEAKER_02:** From securities to payment, like they have to be codified. Yeah, I think it's good to explain. So like most of finance gets cleared through messaging. And it's like, so crypto people are used to like putting a transaction in and then it goes everywhere. Yes. It's not really like this. Oh, yes. Thank you. Thank you. Yeah, indeed. That's a very key point is that...

**[17:14] SPEAKER_04:** The process of what we call delivery versus payment in traditional finance. It's a pretty complex thing because how you make sure like when you deliver the money, the money has been received, that you receive the asset, that everything has been, you know, and it's a kind of a lot of dance because you receive message, you send another one. And it's not like how we used to do where in crypto we submit and it's actually an atomic transaction, which is like just one thing. And when the transaction is complete, you know it's been executed, it's been delivered, and all the parties that is actually, you know, I give you the can, well, I know you've been giving me, like, the money exactly, you know, where actually there is, like, a little bit tense, well, I put the can here, like, you see the can that has been moving here, like, you send the money, and so the blockchain here offers such efficiencies because things like where like you know like the T+1 or T+2 for some of some of those different exchanges now. You, you do it like well depending on what chain you're going to deploy. Yeah, between a second to even like less than that. Yeah. And also SWIFT...

**[18:21] SPEAKER_02:** Isn't a payments mechanism, right? No, it's a message. That's another comment. So let me, I think, interject with a specific example. I think they're biggest in FX, right? Yes. So let's say I've got some USD, I want some Euro. And we kind of like agree to a USD Euro trade. And so we like, I guess we look up whatever the pair is trading at. And I think it's like, I send my side of the trade with some unique ID to SWIFT. And you do too. And then SWIFT checks if it matches. It charges $7 either way. If it does match, then it'll tell us that it matched. Well, I don't think it's actually exactly this way.

**[19:07] SPEAKER_04:** It's more a SWIFT offer type of envelope and a format of envelope and paper and ink that we know how to use and how we're supposed to fill up some forms. Then how we trade those forms between different market participants. It's not much, you know, like the people, like they're going to be some, you know, corresponding banking that's going to be like locally taking your cash and they're going to, everyone is going to take their share. It's not moving the asset. It's just, it's like, I have the USD on my bank list. You've got the euro on your bank list. Talking to each other in a secure and compliant way. Because it's also, oh, he sent that. You have to send some specific messaging for compliance. Then I send another one, say, hey, I checked. There's all the information. A bunch of local jurisdiction-specific.

**[19:58] SPEAKER_03:** Yeah, it's like a lot of different handshakes. Yeah, I think the way someone described it to me... It's like a funny TCP handshake. It's sort of like what they're doing is tracking the transfers, but no money is actually moving, and then they have a list of IOUs. So, like, when I send a SWIFT transaction from, like, let's say I send $100 to you in France, and I go to my bank, I put in $100, the money doesn't...

**[20:27] SPEAKER_04:** Go anywhere. I have to write USD off my ledger. The net at the end of the day is what they call RTGS. They're going to do the transfer actually. It's like a different messaging. If you research, and I'm not a SWIFT expert, but I had to learn over the last couple of months. I've done a little bit more deep dive. And it's fascinating because there is such a huge dance between two transfer of money. Because you have the money in your bank account, but then you actually use central bank money, then you have like the deposit money. So like those, like what you call like M0, M1, M2. And so all of that is pretty complex. And then we're just talking about payment here, you know, talking about, you know, securities or like those other like financial instruments that you can exchange also using blockchain in a very efficient way. But that's, you know, using stablecoin, you can make everything super simple. And also one misconception maybe I would love to mention is like, you know, like we talked about stablecoins and CBDCs. Yeah, yeah, yeah. They're actually exactly the same thing, but just in a different context. A CBDC is a stablecoin for a central bank. It's just the issuer. It's just the issuer is not the same. We're never going to really touch CBDCs because this is like the money of banks, if you say. But almost, I think, from a technical level, it's almost like a copy-paste of the same contract, the same mechanism. But we create a whole different language and terminology for that. But they're actually very similar. And funny fact, those CBDCs, they've been doing, you know, like the, I think the baby needed to grow, you know, like you said, Devcon 2. So it was a two years old kid, Ethereum. And we were like, hey, come in here. You can manage like the most critical infrastructure of the planet, which is our money and how we do trade. And you can do all of this. And I think like the Ethereum Foundation, I have to give them credit like this. Yes, for a long time, they were saying, hey, guys, you're not considering the enterprise and everything. But I think they did the right thing because they protected that baby. So it could grow. And now we're at an age of it's more mature. It's more than 10 years. It's still not even a teenager. The analogy with human is going to take some limits. But we are at a point now where we have a technology and Ethereum is really a capacity to answer all the challenges that are facing, you know, that we're blocking institutions without, which is, you know, well, scalability, privacy, composability and interoperability. The four points that you had in the ARC paper from Circle. And now we have this. Just last week, zkSync announced up to 15,000 TPS, and there is a new thing that almost every week is going on. We like now have a technology when it looks at, well, I need to make sure this is private. I need to make sure this is going to be executed in a seamless way. Also, the decentralization, it's more about the way they look at it. It's more like the vendor locking. I would say the best analogy is that you want to make sure the infrastructure you rely on is going to be able to absorb your activity, but also be resilient enough. This, we still have some work because it's definitely, and I understand the perspective of institution to deploy on a like public infrastructure. You know, at first when Wikipedia showed up, like, you know, 20, 25 years ago, something like that, I think. I mean, I remember I was at my, in my college, like my engineering college, was at the board and we were talking about having wiki you know for doing some articles and they were like those very academic guys said this is this is unacceptable this is unacceptable whenever I'm gonna do this this is anyone can put any information this is not trust. To be clear, you are friends. Yeah, I'm like you are allowed to. And so, but they were in French. They were very like, you know, and protecting this. And at that time, I said, well, we cannot trust, you know, something that's being built collectively like this. But now we know you have to take a grain of salt, but it's actually much more accepted, you know, like that those are like reliable source of information and that you can have things that are being built publicly that are actually very resilient.

**[25:03] SPEAKER_03:** Sorry, I was just going to ask, but there's always this gap between what traditional institutions understand about... We all understand what's been capable for a really, really long time, but are there still gaps, or do you think that's been closed now? It's maybe grown up fully, but even when the capability is there, there's still...

**[25:28] SPEAKER_04:** A knowledge gap, I think, sometimes. Well, let me put it this way. There is about, if you combine all the different types of money, $123 trillion of cash around the world. Right, right. $300 billion are on chain. Right. So... The numbers talk for itself. We're very early. So there's people like they can, I think we still have like a lot of work to do in terms of education. But by education, I mean really talking from a product perspective. What business problem I can solve for you, how it's going to be done, what is going to be the maintenance after, how you're going to deal with very specific use cases. And so you can have some teams that already have an understanding of what you can achieve, but we still need to provide, I think, as an ecosystem more structuring who you can work with, the different vendors, what services they can do, where they can help, what's the type of contract you're going to have after, and really giving that overall perspective of a new entrant in the market. And so some of them, they understand very well, and they have already some pretty detailed questions, even asking me, our Redwan we need to increase like the contract size from the 24 to uh 40, 48 kilobytes and uh we have some you know like those those uh Stack Overflow issue like well known. So yeah, the stack limit one that was always a problem. And so there is some of them it's this but but then some other ones in in this small product they're going to ask me okay. Why should I go on an L2? What is the L1? What does it mean? And what about those changes? What are the primitives? Explaining like, well, if you build any L2s, you're actually going to choose maybe one vendor in some way. But you can completely move your assets freely among all the ecosystem. The wallets are going to be the same. A lot of things are going to be equivalent that you don't have to rebuild. Mm-hmm. And so those are things you need to explain. Some other maybe people, they're going to say, well, what is this? This is just some scammy or something like that. I think you can find all the layers. But now people, they also see the potential of what you can do with digital assets, tokenization. And for people who are a little bit looking around, I'm very excited to see what's going to happen in the next six to 12 months because, you know, the FIT21 Act was signed in July, you know, or something like this. The Financial Innovation Act. I think it's still still a bit ongoing. Yeah. So. Now we like they're like and and we we can also hear that like there's really companies from every direction say okay how how are we going to implement this. The fintech is also moving so they're they're they're like the fact that they're building their L1 even if they're building the L1, I wish they would do some L2s and um my door will always be open uh when when you want to consider that there there is a pretty great tool that can help but but that's going to push the market and from like financial institution to really like adopting this. There is an organization like DTCC, you know, like the biggest clearing house in the world. Like all the securities in the world basically are being cleared over there. They released like an incredible product like four months ago in April, like the great collateral where they have a collection of hundreds of smart contracts that allows you to clear and to make some margin call and collateral management from different jurisdictions, which is a fantastic use case when you see... I'm not a collateral management expert, but I understand the value of how this unlocks. You actually have something that you can take from your... your bank in Japan that you're going to post for something in the U.S. because you have a market event. And this is something you would not even imagine before. And now you can do it. And it's compliant. It's actually legal. And that can unlock so much efficiencies.

**[29:34] SPEAKER_03:** And so that's in the next few months, that's going to be a huge game changer. So it sounds like the lid has been lifted off and there's a ton of demand, but it's like walking down the path to supply that demand. That's the part that people are figuring out, right? Is that right? I think it's such a very transformative technology for how those businesses operate. There is also how I'm going to make money. Okay.

**[30:03] SPEAKER_02:** So there's a fear element to it, right? It's like, well, now I can have like, I'm a PSP provider. Let me ask you this. So in the early days, it felt like there was a focus on more like back office use cases. Like, yeah, how do I move the collateral from like my Japan regional branch to my, you know, whatever. Business process improvements. Business process improvements. And I felt that there's eventually became a I think this started like 2020, 2021, a shift for big corporations wanting top line use cases like like Nike was the first to like sell a ton of NFTs. And then you're seeing like I think like the digital asset treasuries are a kind of genius way for a token to like like the company doesn't have to IPO but like there could be a token and there can be something that's had provides the traditional protections of equity that's publicly traded. And then you didn't, you could just leave this part sort of where it was and somehow there's kind of like a merger going on. And, you know, this is a creating good top line revenue for investment banks and, you know, et cetera, et cetera. So like, is your, is your sense that, people want the efficiency to compete or like, are they starting to think about it as like a new revenue line or, you know, like a transformed revenue line or something?

**[31:45] SPEAKER_04:** Well, that's a billion, trillion dollar question right there. I don't have the answer. What I could say is I see how I think if you look at operational optimization, it's more than that. If you capital flow more seamlessly, you make more money in a financial flow. So the more you have a flow of your money easy, the more you're going to be able to make some because you're going to unlock some opportunities, some some capital improvements. Yeah, I think and from like conversation I've seen and and where where like the still don't have like the golden do say hey that's gonna remix a little bit of like all the different people and intermediaries and people working because If you suddenly have something that is being done in a much more efficient way, well, some different intermediates, they might have to rethink the way of doing their business. This is not going to happen from one day to another. What I can say is that because we're going to have those new forms of working with digital assets, that's going to be more like being a golden era for opportunities to build a pretty fantastic product. And the people that understand pretty well the ethos of the Ethereum ecosystem and also like blockchain in general, like some operation in traditional finance and be able to bridge those two, you, you're going to be able to bring like some amazing, amazing product. And that's what we see a little bit more with convergence, you know, of Aave that is that doing like a collateral product with Horizon and, and, and, you know, like you have like Figure, like you have a Spike or you have some, some of like how as, as we're going to have like now some assets that are on chain that maybe you can loan and you can collateralize and you can borrow money and you can have some, liquidity in front of those assets while being the action. And also, I want to stress, we say RWAs, RWAs, RWAs. There is a lot of... We need probably to find some new language because there is... You know how I feel about that. I think the RWA term is so broad. Yeah, we need... This can be an RWA. Yeah, exactly. And and I can also take a picture of my uh I guess my bank account and say hey this is a tokenization of my bank account and and so there is all the ways but most of them they actually kind of elaborate IOUs and not like and now we're moving towards more and more having some standards and like things like it's the legal tent. You want the native issue. The token is the legal claim to the asset. When this happens and when focusing on that, that's going to unlock some pretty incredible things. You connect this with DeFi, you're going to always need some form of AML, KYC and everything. Like the, the, the, the DeFi, like the, like there's none for the last year. It's...

**[34:57] SPEAKER_03:** They're probably going to have like two of those, but once you connect this, I think that's going to be pretty incredible. But how do the institutions feel about like, obviously as the head of the EEA and you feel strongly about Ethereum, right? Like the Ethereum ecosystem broadly of L1s, L2s, like how do they feel about that? Do they see any other, you know, like we know that Ripple has tried to attract that interest for a really long time. Like, are they kind of sold on Ethereum at this point or are they...

**[35:27] SPEAKER_04:** Are they still needing to be convinced? I've heard several executives at Sibos saying, Ethereum is the standard. EVM is the standard. This is the ecosystem. Having said that, and as decision makers, they also want to make sure they keep the door open and not being locked, so they move progressively. You know, 60% of the stablecoin issuance is on Ethereum. I think probably 85% to 90% of all RWAs, it's the same. Some similar statistics about DeFi activities. That's, you know, like Electric Capital, like you can see a graph like three times more like that than any other ecosystem in terms of like builders and everything. So that's the most radiant and advanced, you know, ecosystem in terms of research on every, every facet. And so that's, they know, they recognize. But it doesn't mean that we need to keep educating, to keep like, you know, working with the EF, for instance, like they've been incredible work for the last few months of really packaging the message in a better way that can be more digestible. But there's more like some work, for instance, like, you know, like the protocol team, they're already addressing so many of the fear, like can have some different like, you know, digital asset manager in financial institution. But how we bring that message to the right people, package it in a way that it's easy to understand, that's some of the work that is being done as we speak. And that's going to really help continuing solidifying that dominance position. But to also answer your question, some of those institutions they say hey we want to be multi-chain we want to look at everything which I think it's it's absolutely fair and I would do the same if I were in their shoe so okay well we they have some different assessment, um, you know, criteria and they say wow we're going to take this chain this chain this chain this chain and and then we'll see. I mean, beyond EVM I mean you've obviously got competition between Ethereum and other EVM flavors.

**[37:32] SPEAKER_01:** What is the competition outside of that? Because I know there's, you know, you've obviously got competition within that. But are institutions doing non-EVM things as well? There's like Cantons around. I don't know what they're using. Like do institutions use Solana at all? Well, I know, but does DA still have its own like big proprietary-ish stack?

**[38:01] SPEAKER_04:** It's not proprietary anymore, but it's, yeah. Well, Hedera. No one using Hedera. What are you here? Competitive. Canton is probably the one, the most advanced in terms of like, you know, connection with the rest of the ecosystem. And I would say that not the rest, but the traditional finance. They have, they have like a way it's structured though. It's, It's something I still don't completely understand. You can be a validator, have some tokens that you can exchange on some private market. And so some form of revenue. And then they have already like that. It's a consortium, you know, like it's a Quorum B2, I would say. And they've been able to bring into their governance like a lot of the different financial institutions. So, but then once again, and if you ask me, and I'm biased, of course, but this is an ecosystem. He has a Canton code. He's open source and everything. But, well, you're still building on a technology that is not super very, there's not a lot of people. When are you going to be the CIO of a company and you need to have some maintenance or something? It's going to be, what, like 20 guys in a country that can do some work on this? And so that's the way I look at this.

**[39:25] SPEAKER_03:** But I think Solana, I'm not sure with the institution. I don't hear anything institutional from Solana, but it seems popular nonetheless. Oddly enough, like Ripple has been trying to do this for a long time, but I don't hear them brought up in the conversation that much. Nobody ever used Ripple.

**[39:46] SPEAKER_04:** I've been in blockchain not as long as you guys, but really since 2019. And I spent like almost four years at ChainSafe. Very authentic, like, you know, builders, like crypto native protocol development. And I've been to conferences, you know, with the engineers and I asked them in a very candid way, I said, have you ever built on Ripple or on some other? And I had conversation with the engineers at ChainSafe.

**[40:17] SPEAKER_03:** We had some polls and we had some conversation in the Slack, I remember, and no one really came up with some very... It just got an infinite war chest for marketing and lobbying. I mean, at one point, one of the Sibos I went to years and years ago, Ripple was supposed to have a huge brood. And I guess SWIFT decided, oh, they're too much of a competitor, so they kicked them out. They were calling themselves the SWIFT killer. They decided, like Ripple decided, you know what? We're just going to run our own conference in parallel with Sibos. They put on a parallel conference. And Vitalik was speaking at their conference. At the Ripple one? At the Ripple one. And I remember they had buses in front of the Sibos conference, like taking you to where their new conference was. And I remember, like, seeing Vitalik, like, run across, like, looking for this conference because, like, it was in this new place and, like, we were all trying to, I remember, like, waving him, like, over here, Vitalik. So it's, you know. People still using Corda? Corda?

**[41:32] SPEAKER_01:** Like it's been bought out by Sela, Corda Sela. I don't think they would actually get those terms. I think it's a partnership and a collaboration. So we're not absolutely, they weren't bought by. Not bought out, but yes. I mean, I will say. Anyone using Fabric still? Fabric?

**[41:55] SPEAKER_04:** Well, yes. Behind the scene, the Fabric is still very present in, I think, central banks and those type of more very close environments. Even, I'm not sure, BIS, Bank of International Settlement, which is, for those who don't know, it's like 40 different international banks that work together to optimize, I would say, the collaboration and exchange. But they had like a project Agora that they started a couple of like months ago. Those are like institutions where it takes like much longer time, I think. That's dancing in new projects. That's not the same, the same Agora, but I would imagine like maybe they were having some POCs before. I know some few central banks, they run, you know, like using Fabric, you know, like the...

**[42:46] SPEAKER_03:** It's probably like the asbestos, isn't it? It's just going to take years to sort of check out. You need people in suits to like support us. I will say, I think we're almost at 45 minutes. Redwan's been very generous with his time. I think we asked him.

**[43:06] SPEAKER_01:** Do you have any final thoughts you want to share? Actually, on Fabric, I know IBM is working on a bridge between Fabric to, it's called Fabric X, to Ethereum. So you can see that online. Right. Well, one of their big sell at New York Blockchain Week in 2018 was their EVM integration. They did the... Yeah, they did a channel or something. About 3.js or whatever, that they did do this munching together. And that was using Burrow, right? Because you've got the Burrow. Burrow went into Hyperledger for Besu, uh, and that was the continuation of that Eris DB, Monax, on, you went, that was never made mainnet compatible though, um, but there was that Go EVM within Hyperledger under the same licensing so they couldn't, they could wham those together, um, and I mean that's that's that's seven years ago so yeah I'm sure that they they need to have an even better EVM story these days.

**[44:21] SPEAKER_04:** To answer your question, like EVM and Ethereum is really the standard as everyone, that's what they're saying. You know, like you go through some different stages. You have like the chief innovation officer of like SWIFT and some different institutions. They understand that. They're like, that's what they say. You know, I was really, everywhere I went on all those different panels, you know, we had a panel at 8:30 on like Permissionless, Very Private Network. It was hosted by Applied Blockchain, a member of the EEA. There was like Citibank, Linux Foundation, Decentralized Trust, Ubix, and me. And it was, we were full. There were people standing up. And there was, you know, the SWIFT Innovation Officers and most of the banks that came to talk to us. People, they understand. Ethereum is definitely seen as the standard and the place where you want to build because that's where you have access to the most liquidity, the most users, the most vibrant DeFi ecosystem, which is something that is getting closer, I think, and say, well, maybe there is some way to make some money here. I don't know exactly...

**[45:32] SPEAKER_01:** How, but there is some potential. So I think the future is very bright for us. And I think that ties very nicely back to the start of the conversation and about the thoughts for the EEA and so on, was something that Jeremy Miller said in the opening speech on the opening day was, think of this as being like a router, an internet intranet. There's no reason why suitably modular code bases shouldn't serve all of these use cases, public and private. And what we did not want to happen, and I remember being driven very much by this, was saying, let's not have arbitrarily different code bases for these different things because we can't be asked having that conversation and making the effort to try and bridge those worlds. And that was really coming from that Fabric and Corda competition of of these big enterprises basically sort of being told Ethereum guys have got to get your stuff together or we're going to get mandated to use this other stuff and it doesn't matter what you want it's like the spending will have been spent and it's it's never coming back so I think it's from to my mind it's like really superb to see where we are it's like that's what we were thinking that was kind of the goal right is that this can be a standard for everything and yeah, things were like immature and maybe, you know, you needed to be doing consortium chains and you needed to take these baby steps on the way and wait for the tech to catch up. But really it's like, this can be the answer for everything. So, and I think that's where we are. And we're talking more and more, you know, like Ethereum Foundation has done an incredible job. They have like an enterprise team also like that in conversation with everyone and they can have like, they have access to all the different leaders. And this has been very...

**[47:32] SPEAKER_04:** Pretty fantastic. And so the more we discuss about this and say hey you know there is no CEO of Ethereum it's not a private company there's no CEO of internet you know has that yeah it was Linux right so that's uh that that's something that is like catching up more and more and the more you know we're going that's also like the mission that's what we do at EEA you know like going to have this conversation doing events like bringing some people together from like a few events that we do when we try to remix like DeFi traditional finance institution like pure Ethereum players and have all those people talking together that's how we make that you know moving forward. Well, on that note, I think we'll wrap up. But where can people find more about you and EEA in general? Well, the website, we are present on all the social media. The website is entethalliance.org. We have the same handle on Twitter, on LinkedIn. I'm also on LinkedIn and Twitter and try to post often some few articles and some insights. And there's some more work that I'm going to put together in a couple of weeks around other ways and everything. And also always looking for some large institution that would like to collaborate on some writing pieces. Yeah. So we can really put some like thought leadership and helping, you know, explaining what's being done. And I think bridging, you know, like the Ethereum world with the traditional finance also like something that we're pretty excited to do in a couple of weeks. Yeah, that's awesome. We'll be also in Singapore Fintech Week next month, in Devcon in Argentina, and we'll be also in Abu Dhabi for Finance Week.

**[49:09] SPEAKER_01:** Cool. And Bob, where can people find you? So, yeah, I'm on Twitter. Same as my name, Bob at Summerwill with a W-I-L-L, not Ville, not Summerville. Not the German spelling. No. Yeah. Kieren? Kieren James-Lubin on X, YouTube, et cetera. And you can find me on X at?

**[49:35] SPEAKER_03:** Vic, V-I-C, the number four, W-O-N-G. Thank you for joining us for our first in-person roundtable. Thanks again. It's awesome. Thanks for coming. Take care.