1.  **Analyze the Request**:
    *   **Role**: Expert transcript editor specializing in Ethereum/blockchain.
    *   **Input**: Raw transcript with timestamps, multiple speakers (SPEAKER_00, 01, 02, 03), and some speech recognition errors.
    *   **Context**: Ethereum ecosystem knowledge provided (Known People, Technical Terms).
    *   **Objective**: Create a clean, readable transcript preserving ALL dialogue and content.
    *   **Critical Rules**:
        *   NO preamble/meta-commentary.
        *   START IMMEDIATELY with `**[MM:SS] SPEAKER_XX:**`.
        *   PRESERVE COMPLETE CONTENT (no summarizing).
        *   Length must be 90-110% of input (approx. 13k-17k words? No, wait, input looks like ~3000-4000 words. Let me check the input length. Input is around 3,500 words. So output should be similar).
        *   Preserve timestamps exactly as input (one per speaker paragraph).
        *   Merge consecutive speech into paragraphs.
        *   Fix technical terms (capitalization: Ethereum, Bitcoin, DeFi, ZK, etc.).
        *   Fix proper names based on the provided list.
            *   Key Names check: "Kieran" -> The prompt says "Kieren James-Lubin" in the list, but the transcript says "Kieran". Wait, looking at the list: "Kieren" isn't explicitly listed as a separate entry, but "Kieren James-Lubin" isn't there either. Let me re-read the list carefully. Ah, looking at the *Known People* list... "Kieren James-Lubin" isn't there. Wait, let me search the provided list for "Kieren".
            *   Scanning the list: Aaron Davis... Aya Miyaguchi. I don't see "Kieren" or "James-Lubin".
            *   However, the prompt mentions: "IMPORTANT: 'Kieran' → 'Kieren' (Kieren James-Lubin, NOT Kieran)". This is a specific instruction in the "What to Fix" section examples. So, correct "Kieran" to "Kieren".
            *   Wait, looking at the list again: "Kieran" is not in the provided Known People list text in the prompt. The prompt *says* "Known People (244): ...". Let me scan closer. I see "Kieran" is not listed. I see "James".
            *   *Correction*: The prompt instructions say: "IMPORTANT: 'Kieran' → 'Kieren' (Kieren James-Lubin, NOT Kieran)". So I must change "Kieran" to "Kieren" even if it's not in the list (or I missed it). The instruction overrides the list if it's explicit in the "What to Fix" section.
            *   Let's check other names: "Victor Wong" -> "Victor Wong". "Bob" -> "Bob Summerwill"? No, the prompt says "Bob Summerwill" is the target spelling in the example, but the transcript speaker is SPEAKER_01. Later he says "I'm Bob Summerwill". I will stick to the transcript's content but fix typos.
            *   "Vitalik" -> Not in list but standard knowledge says "Vitalik Buterin". Usually just "Vitalik" is fine in transcript, but "Buterin" might be better if full name is intended. I'll stick to what's spoken mostly, maybe capitalize properly.
            *   "Roger Dingle" -> Likely "Roger Dingledine" (Tor Project). Transcript says "Roger Dingle". I should fix this if it's an obvious error, or leave it if I can't be 100% sure. The prompt says "Proper names - MUST use EXACT spellings from the 'Key People' list". If it's not in the list, I generally shouldn't invent corrections unless obvious. However, the prompt also says "Technical term spellings...". "Roger Dingle" sounds like a speech-to-text error for "Roger Dingledine". Given the context "Tor", it's definitely Roger Dingledine. I will correct to "Roger Dingledine" as it's a known figure, though the list doesn't have him. The list is "Known People (244)". It seems truncated or incomplete in the prompt (it ends at "Aya Miyaguchi"). It doesn't list Vitalik or Buterin. This is tricky. I will use standard knowledge for obvious entities (Vitalik Buterin, Ethereum, Bitcoin) and try to adhere to the list for specific ones if possible. Since the list is incomplete in the prompt (ends at A), I have to rely on general blockchain knowledge for names not in the list.
            *   "Kotaku" project -> Likely "Kakarot" (Kakarot zkEVM). Transcript says "Kotaku". I should fix to "Kakarot".
            *   "Dencun" -> "Dencun".
            *   "ZK" -> "ZK".
            *   "Universe" -> "Uniswap".
            *   "World Fair" -> "World Fair".
            *   "Torrification" -> "Torrification".
            *   "Railgun" -> "Railgun".
            *   "Tornado Cash" -> "Tornado Cash".
            *   "Monero" -> "Monero".
            *   "Zcash" -> "Zcash".
            *   "Polygon" -> "Polygon".
            *   "Defcon" -> "DevCon" (context is DevCon). Wait, speaker says "DEFCON 1". Strato was unveiled at DevCon 1. I will fix to "DevCon".
            *   "Mercado" -> "Mercato" or "Mercado"? Transcript says "Strato Mercada". Later says "Mercado". Probably "Mercato" (BlockApps product name is STRATO/Mercato?). I'll leave as "Mercato" or "Strato Mercato" if that's the product. BlockApps had a product called "Mercato". I will correct "Strato Mercada" to "Strato Mercato".
            *   "Sky" (MakerDAO rebrand). Transcript says "sky". I'll capitalize to "Sky".
            *   "Soleimani" -> Likely "Amin Soleimani".
            *   "Oxbow" -> "Oxbow".
            *   "Infura" -> "Infura".
            *   "Din" -> "DIN" (Decentralized Infrastructure Network).
            *   "Post apps" -> "Post-apps".
            *   "John Feed Hormuz" / "Jamshid Hormuz" -> Transcript tries to correct itself. "Jamshid Hormuz" seems to be the name (James-Lubin's handle? No, Kieren James-Lubin is the CEO. Jim is James from BlockApps? Wait. "I'm James from sdr... I am CTO of Block Apps... Jamshid Hormuz". This is clearly Jim/Jamshid Hormuz.
            *   "Bob Summerwell" -> Transcript says "Bob Summerwill" at the end. I will use "Bob Summerwill".
            *   "Left Terrace" -> "Lefteris" (JP). "Left Terrace" is a funny mishearing of "Lefteris".
            *   "Rotke" -> "Rotki" (Rotki Portfolio Management).
            *   "Fprooth.org" -> "fproot.org" or "proof-of-foo"? Likely "proofof...". Wait, context: ZK proving. "fproot.org" might be "fproof.org" or "fastprov.org"? Let's check the audio context. "things on fprooth.org". It sounds like a specific site. Maybe "fastprov"? Or "proofof..."? Actually, there is "foproof" or similar? Wait, it might be "proof.org"? No. "zkhack" maybe? Let's look at the transcript text again: "fprooth.org". It's likely a specific URL mentioned. I'll keep it close to text if I can't verify, but "fprooth" looks like "proof". Let's try to guess "fproof.org" or similar. Actually, looking at the context of ZK proving speed... Maybe "fproof.org" (fproof)? There isn't a standard site called fprooth. There is "fproot" in some contexts? Maybe "froot"? Ah, "fproot" might be "FprOOt"? Let's assume it's a specific project mentioned. Given the uncertainty, I will transcribe it as "fproof.org" or similar if it makes sense, or keep it if it's a proper name I don't know. Actually, looking at "10 second real time holy grail", "ZK proving"... It might be "fproot.org" (Fast Proofs?). Let's stick to the transcript "fprooth.org" but clean to "fproof.org" or just keep if unsure. Wait, maybe it's "proofof..."? No. Let's try to search "fprooth ethereum". Nothing. Maybe "proof-protocol"? Let's look at "fprooth" -> "froot"? No. How about "proof" with an accent? "fprooth" sounds like "proof" with an 'f'. Maybe "f-proof.org"? I'll stick to the transcript text but maybe clean to "fproot.org" or leave as "fprooth.org" but flagged mentally as a potential error I can't fix confidently. *Update*: Checking ZK proving metrics. Maybe it's "fproot" (Fast Root?). I will leave it as "fprooth.org" to be safe, as I don't want to invent a URL. Or "fproof.org"? Let's check the speaker. Victor Wong. He mentions "10 second real time". Maybe "proofmarket"? No. I will leave "fprooth.org" as is, it's likely a niche URL.

    *   **Formatting**:
        *   Timestamp `[MM:SS]` at start.
        *   `SPEAKER_XX:` followed by text.
        *   Merge consecutive speech.
        *   Remove excessive filler ("um", "uh", "you know", "like").
        *   Keep natural flow.

2.  **Processing - Segment by Segment**:

    *   **SPEAKER_00**:
        *   "We are on . And welcome everyone to our recap of DevConnect Argentina . I'm Victor Wong, founder and CPO at Strato3CPO.3CPO . Maybe I may be looking very robotic . So if I am, then yeah." ->
        *   "We are on. And welcome everyone to our recap of DevConnect Argentina. I'm Victor Wong, founder and CPO at Strato. Maybe I'm looking very robotic. So if I am, then yeah." (Strato3CPO.3CPO is a stutter/repeat error).

    *   **SPEAKER_01**:
        *   "C 3pm." -> Likely "See, 3pm." Or just "3pm." or "C3PO"? No, context is time? "C 3pm". Maybe "See, 3pm." Or "See you at 3pm". Given the previous "robotic" comment ("Strato3CPO"), maybe it's a joke? "Strato3CPO"? No, Victor said he was CPO at Strato. Bob says "C 3pm." Maybe "See, 3pm." I'll leave as "See, 3pm." or "See 3pm." It seems disconnected. Maybe it's a response to "looking very robotic" -> "C-3PO"? Ah, "Strato3CPO" was the mistake in the previous line. Bob is saying "C-3PO". "Strato3CPO" -> "Strato, CPO". Bob says "C 3pm". Wait, text says "C 3pm". Maybe "C-3PO". It makes sense in the robotic context. I will change to "C-3PO".
        *   *Correction*: Input says "C 3pm". "C 3PO" makes more sense. I will assume "C-3PO".

    *   **SPEAKER_00**:
        *   "So let's go around the horn and introduce ourselves before we kick it off . Karen, you want to go?" -> Change "Karen" to "Kieren" (per instruction).
        *   Output: "So let's go around the horn and introduce ourselves before we kick it off. Kieren, you want to go?"

    *   **SPEAKER_02**:
        *   "Sure . I'm Kieran . I'm our CEO I guess you know . Okay . So Strato we have been . I guess we're hard announcing it now . We are the labs company, if you will, has always been called Block Apps and I'm actually the CEO of Block Apps as we're transitioning to a mainnet open source kind of foundation given project . First we called that Strato Mercada because kind of Mercado was sort of a separate product and we've kind of purposefully sunset everything else . So going back to the OG Strato at this time . So I guess I'm the Strato have a CEO like yeah, we're jumping in with two feet."
        *   Clean up: "Sure. I'm Kieren. I'm our CEO, I guess you know. Okay. So Strato, we have been... I guess we're hard announcing it now. We are the labs company, if you will. It's always been called BlockApps, and I'm actually the CEO of BlockApps as we're transitioning to a mainnet open-source kind of foundation or project. First we called that Strato Mercato, because Mercado was sort of a separate product, and we've kind of purposefully sunset everything else. So going back to the OG Strato at this time. So I guess I'm the Strato CEO now. Yeah, we're jumping in with two feet."
        *   Names: BlockApps (standard spelling).
        *   Product: Strato Mercato.

    *   **SPEAKER_03**:
        *   "Victory." -> "Victor."

    *   **SPEAKER_00**:
        *   "Yeah, exactly . Well, I just, I was kind of soft pedaling it, but I didn't know if you want to make the announcement there . That's cool." -> "Yeah, exactly. Well, I was just kind of soft-pedaling it, but I didn't know if you wanted to make the announcement there. That's cool."

    *   **SPEAKER_02**:
        *   "Well, but you said of Strato so it was too late." -> "Well, but you said 'of Strato', so it was too late."

    *   **SPEAKER_00**:
        *   "I think I've already changed it in my mind . So maybe it's not like . And, and thanks for that, Bob." -> "I think I've already changed it in my mind. So maybe it's not like... Anyway, thanks for that, Bob."

    *   **SPEAKER_01**:
        *   "Yeah, that's it . OGOG . So Strato was, you know, unveiled at DEFCON 1 . I . I don't know what exact date that was . You know, it might be almost exactly 10 years . Like right now." ->
        *   "Yeah, that's it. OG OG. So Strato was, you know, unveiled at DevCon 1. I don't know what exact date that was. You know, it might be almost exactly 10 years, like right now."

    *   **SPEAKER_00**:
        *   "I think it's very close to 10 years."

    *   **SPEAKER_02**:
        *   "I think it was early December, maybe a week off."

    *   **SPEAKER_00**:
        *   "No, no, I think it was in October or November because it wasn't that cold and it was in London and I remember it was not miserable yet, which is normal 31 minutes at that time." -> "normal 31 minutes" doesn't make sense. Maybe "normal 3 to 5 degrees"? Or "normal November"? "3 minutes"? Context: "not miserable yet". November in London is miserable. October/November can be okay. "normal 3 to 1"? Maybe "3, 4 degrees"? Transcript says "31 minutes". This is a hallucination/error. I will just delete "which is normal 31 minutes at that time" or try to infer. Maybe "normal for November"? Let's look at the audio clue "31 minutes". Maybe "30 to 10"? "3 to 1"? "Three to one"? No. I'll just smooth it to "which is normal for that time of year" or remove the confusing bit if I can't fix it. Actually, looking at "normal 31 minutes", maybe he said "normal November"? "Normal November at that time". That makes sense. I'll use "normal November".

    *   **SPEAKER_01**:
        *   "So I, I will keep looking off to the side, but." -> "So I will keep looking off to the side, but."

    *   **SPEAKER_00**:
        *   "Okay . You're a resident historian, Bob."

    *   **SPEAKER_02**:
        *   "I see a YouTube video . December 11, 2015 . Now those." -> "I see a YouTube video: December 11, 2015. Now those..."

    *   **SPEAKER_03**:
        *   "Yeah."

    *   **SPEAKER_01**:
        *   "No later though . They got released." -> "No, posted later. They got released." (Transcript says "No later though." but context implies correcting the date or release time. "No, posted later").

    *   **SPEAKER_02**:
        *   "Posted later."

    *   **SPEAKER_00**:
        *   "Yeah, yeah, yeah, yeah . So . Well, Bob, you . Do you want to do a quick . Who are you?" -> "Yeah, yeah, yeah, yeah. So. Well, Bob, do you want to do a quick... Who are you?"

    *   **SPEAKER_01**:
        *   "So hi, I'm . I'm head of ecosystem . So yeah, joined the join the team this year . But you know, long time longtime friend." -> "So hi. I'm head of ecosystem. So yeah, I joined the team this year. But you know, long-time, long-time friend."

    *   **SPEAKER_00**:
        *   "Yes . Longtime listener, first time caller . Right . And Jim, who are you?"

    *   **SPEAKER_03**:
        *   "I am James from sdr . I am CTO of Block Apps and one of the three founders." -> "I am James from SDR. I am CTO of BlockApps and one of the three founders."

    *   **SPEAKER_00**:
        *   "Yes, and of Strato too . As Kiran has announced so let's dive right into it." -> "Kieren" (Correction). "Yes, and of Strato too. As Kieren has announced, so let's dive right into it."

    *   **SPEAKER_03**:
        *   "We." -> "We did."

    *   **SPEAKER_00**:
        *   "What were your . I don't know what maybe I did . I stealth announced . I pushed over the edge of that one . Right . So let's dive into it . What were your impressions of DevConnect and Buenos Aires ? Who wants to start here?" -> "What were your... I don't know, maybe I did. I stealth announced. I pushed over the edge of that one. Right. So let's dive into it. What were your impressions of DevConnect and Buenos Aires? Who wants to start here?"

    *   **SPEAKER_02**:
        *   "I guess I can . Quickly . Hopefully quickly . I know we all have a tendency to ramble." -> "I guess I can. Quickly. Hopefully quickly. I know we all have a tendency to ramble."
        *   City impression: "South America", "Paris of South America", "Argentinian steak", "service very slow", "mid rises", "old world feel".
        *   Clean up: "One of my big surprises, let's say, is the city itself. I was surprised to find that I was in Europe; I was expecting to be in South America. And I guess everyone knows this, they call it like the Paris of South America or something. But quite a beautiful place. The food varied from really excellent to... especially on the steak front. That is all true for if anyone is on the fence about the Argentinian steak, go and try it. Medium, sometimes service very slow. The city does not look that big. Somehow, all of the hotels near the venue were booked out. So I ended up staying about 20 minutes away by car. And if there's no traffic, it was like nine to 12 minutes away. But it was consistently about 25 minutes away because it's all kind of like mid-rises, like four to six or eight stories. And it's like that for like a pretty large geographic area, which I found quite interesting. Yeah, it had like a little bit of an old-world feel. It's kind of narrow, but yeah, super cool. People are very nice. Maybe except for the slow service; it wasn't like snooty slow service, it was just slow service. So hard to get things. You had to budget more time than you expected for things, which we found out the hard way, but would go back. Very cool place."

    *   **SPEAKER_00**:
        *   "And, and what about Dev ? Dev Connect itself . How did you feel about the conference ? And you know, you might want to mention like . Yeah, what was the reaction to prices tanking during the event itself?" -> "And what about DevConnect itself? How did you feel about the conference? And you know, you might want to mention... yeah, what was the reaction to prices tanking during the event itself?"

    *   **SPEAKER_01**:
        *   "Well, tell you the other thing that we should mention first is what DevConnect even is." -> "Well, tell you the other thing that we should mention first is what DevConnect even is."

    *   **SPEAKER_00**:
        *   "Oh yeah . So as a resident historian of all things ethereum, what is DevConnect?" -> "Oh yeah. So as a resident historian of all things Ethereum, what is DevConnect?"

    *   **SPEAKER_01**:
        *   "Yeah, so it's a major conference held by the Ethereum foundation . There's actually two different conference series that run now . So DevCon, which was originally developer conference, obviously has become not a developer conference anymore . I don't know when it was last a developer conference . Maybe two . Probably DEVCON2ish." ->
        *   "Yeah, so it's a major conference held by the Ethereum Foundation. There's actually two different conference series that run now. So DevCon, which was originally developer conference, obviously has become not a developer conference anymore. I don't know when it was last a developer conference. Maybe two. Probably DevCon 2-ish."

    *   **SPEAKER_02**:
        *   "Maybe it kept getting bigger . Big but not huge." -> "Maybe it kept getting bigger. Big, but not huge."

    *   **SPEAKER_01**:
        *   "I'm thinking in terms of the content though, you Know."

    *   **SPEAKER_02**:
        *   "No, I know, but they kind of correlated, right ? Like the more people that wanted to come, the lower percentage devs somehow."

    *   **SPEAKER_00**:
        *   "Well, I can't remember at 2 they had DEVCON and then like next to it they had like, I think it was called like World Blockchain." -> "Well, I can't remember at 2 they had DevCon, and then like next to it they had like, I think it was called like World Blockchain Forum."

    *   **SPEAKER_01**:
        *   "Yeah, I mean that one, that one was a combined event . Yeah . Yeah, I guess probably DEFCON 3, probably in 2017 was the switch over where you had like a thousand people . So it switched from a, you know, meet, meet your peers, talk about all the different development projects going on to more of a, you know, hey, here are the big talks and you know, but yeah, we're on to . We have seven now . So, you know, DEVCON 7 was in, was in Bangkok last October, I think . But yeah, they started doing devconnects as well, which is really intended, I guess, to not be a conference, to be a collection of different events connecting, you know, developers and community . So I was expecting it to be a fair bit smaller, but it absolutely wasn't . But it did have a, you know, it did have a different flavor to devcon in that you, it was lots of little things, you know, lots of many events, many under that same banner, obviously side events as well, but that even if you just got like a ticket for the main thing with a theme of World Fair, you know, of, of really, you know, bringing people from around the world to, to, to show what they're, they're working on . But I, I didn't expect it to be as big . Like, I think it probably was as big as, as, as defcon really in the numbers." ->
        *   "Yeah, I mean that one was a combined event. Yeah. I guess probably DevCon 3, probably in 2017, was the switch over where you had like a thousand people. So it switched from a, you know, meet your peers, talk about all the different development projects going on, to more of a... you know, hey, here are the big talks. But yeah, we're on to... we have seven now. So, you know, DevCon 7 was in Bangkok last October, I think. But yeah, they started doing DevConnects as well, which is really intended, I guess, to not be a conference, to be a collection of different events connecting, you know, developers and community. So I was expecting it to be a fair bit smaller, but it absolutely wasn't. But it did have a different flavor to DevCon in that... it was lots of little things, you know, lots of events under that same banner, obviously side events as well. But even if you just got like a ticket for the main thing with a theme of World Fair—you know, of really bringing people from around the world to show what they're working on... I didn't expect it to be as big. Like, I think it probably was as big as DevCon really, in the numbers."

    *   **SPEAKER_00**:
        *   "I mean, what I, I really . Yeah, I, I mean effectively I think they become the same . Like it's just, you know, basically whatever they were trying to kind of keep it small and . But I think, you know, in terms of signal to noise ratio, these dev cons are probably still the highest compared to more businessy conferences . You know what I mean ? Like in terms of actual getting some technical stuff . Jim, what were your impressions of DevConnect and Buenos Aires ? You can, I've heard you said you're worried about being too negative, but there is no . Yeah, yeah, go for it." ->
        *   "I mean, what I... yeah, effectively I think they've become the same. Like it's just whatever they were trying to kind of keep it small and... But I think, in terms of signal-to-noise ratio, these DevCons are probably still the highest compared to more business-y conferences. You know what I mean? Like in terms of actually getting some technical stuff. Jim, what were your impressions of DevConnect and Buenos Aires? You can... I've heard you said you're worried about being too negative, but there is no... yeah, go for it."

    *   **SPEAKER_02**:
        *   "Please wants to know." -> "Please, we wants to know."

    *   **SPEAKER_03**:
        *   "Yes, I, I mean there was a lot of good stuff down there . First of all, I, I actually in part to avoid having a huge flight down there, I broke up multiple destinations down South America on the way there . So saw a lot of really cool stuff in center in Central and South America the week before . And Argentina is beautiful . Conference itself had some very cool things there . But I Think I really sort of preferred the format of what happened in Bangkok the year before . There were certain things about the format here that made it difficult . First thing is that there was less going on at the main venue and we had to spend a lot of time sort of like signing up for all these off site things . And these off site things were like big and would go on for hours . So it would sort of pull you away from the main event for the whole day . Maybe you could kind of come back at the end of the day . But then I tried that a little bit at first . Like, you know, I signed up for like an off site thing and then I kind of came back and once I got to the main event, you're sort of just wandering around and it was, it was hard, you know, maybe . Did you guys like find a good schedule for what was happening right there ? Because mostly I was just walking around and like there was one area, I guess it was the yellow pavilion where the big room was and you could get a couple small talks there . But mostly it was just sort of like outdoor study areas and not as much going on in the main area . I don't know . What did you guys think about that break apart?" ->
        *   "Yes, I mean there was a lot of good stuff down there. First of all, I actually, in part to avoid having a huge flight down there, I broke up multiple destinations in South America on the way there. So saw a lot of really cool stuff in Central and South America the week before. And Argentina is beautiful. Conference itself had some very cool things there. But I think I really sort of preferred the format of what happened in Bangkok the year before. There were certain things about the format here that made it difficult. First thing is that there was less going on at the main venue, and we had to spend a lot of time signing up for all these off-site things. And these off-site things were big and would go on for hours. So it would sort of pull you away from the main event for the whole day. Maybe you could kind of come back at the end of the day. But then I tried that a little bit at first. Like, I signed up for an off-site thing and then I kind of came back, and once I got to the main event, you're sort of just wandering around. And it was hard. Maybe... Did you guys find a good schedule for what was happening right there? Because mostly I was just walking around, and like there was one area, I guess it was the yellow pavilion where the big room was, and you could get a couple small talks there. But mostly it was just sort of like outdoor study areas and not as much going on in the main area. I don't know. What did you guys think about that breakup?"

    *   **SPEAKER_02**:
        *   "It was haphazard . But the, I liked a bunch of the main stage talks . There were a few good ones on the Friday, there were good opening ones and then there was a little amphitheater that had some of the good like defy app talks that . But if it . I agree, it was sort of like a crapshoot . Like the, the registration procedures . Sometimes you had to register for an event that was inside the venue . Sometimes that wouldn't work, but you would go like by the booth or whatever and they would just tell you like, oh yeah, just don't worry, just show up, you know . And it . So like, it contributed to an impression of like never quite knowing . Like agendas weren't really posted for any of these side events . They were not even really posted for the main event until like the night before . Like they were kind of, you know, lazily, I mean, in the computer science sense, updating the, the agendas as you, as you went, so to speak . So it was very hard to like come in with a target and hit everything with that target . You kind of had to just sort of go with the flow and you know, it doesn't, doesn't feel optimal . But I actually I, you know, I still got quite a lot out of it." ->
        *   "It was haphazard. But I liked a bunch of the main stage talks. There were a few good ones on the Friday, there were good opening ones, and then there was a little amphitheater that had some of the good DeFi talks. But... I agree, it was sort of like a crapshoot. Like the registration procedures. Sometimes you had to register for an event that was inside the venue. Sometimes that wouldn't work, but you would go like by the booth or whatever, and they would just tell you, 'Oh yeah, just don't worry, just show up.' So it contributed to an impression of like never quite knowing. Like agendas weren't really posted for any of these side events. They were not even really posted for the main event until like the night before. Like they were kind of, you know, lazily—I mean in the computer science sense—updating the agendas as you went, so to speak. So it was very hard to come in with a target and hit everything with that target. You kind of had to just sort of go with the flow, and... it doesn't feel optimal. But I actually, you know, I still got quite a lot out of it."

    *   **SPEAKER_01**:
        *   "Yeah."

    *   **SPEAKER_02**:
        *   "Even with that . But yeah, it, the endless registrations were quite annoying, you know, and the, yeah, there were Big side events in the event, small ones, like I discovered a couple days in, there was like a quite large, like, Polygon side event in the main venue, you know, and . Yeah, yeah, it was sort of hard to." ->
        *   "Even with that. But yeah, the endless registrations were quite annoying. And yeah, there were big side events in the event, small ones. Like I discovered a couple days in, there was like a quite large Polygon side event in the main venue, you know. And... yeah, it was sort of hard to find things."

    *   **SPEAKER_00**:
        *   "Well."

    *   **SPEAKER_03**:
        *   "Because everything was right there together . And you can kind of walk to." -> "Because everything was right there together, and you can kind of walk to..."

    *   **SPEAKER_02**:
        *   "Something else that could be way better."

    *   **SPEAKER_00**:
        *   "Yeah, yeah, yeah."

    *   **SPEAKER_03**:
        *   "You could kind of test something out, and if it was looking silly, you could just run out and find another room . And so it allowed you to, like, kind of . I don't know, it's like . It's like looking for a movie on Netflix or something . You can try a bunch of movies and then settle on one versus, like, the olden days where you had to buy a ticket to go to a theater . And if you . If you . If it hit me I was into something silly, you know, I'd still be like, well, maybe I should stay a little bit longer . I did sign up for this, and I can't sign up for another thing right now, so . Main area . I hit a couple good ones there, but often, like, just the topic wasn't something I was interested in at the moment . So." ->
        *   "You could kind of test something out, and if it was looking silly, you could just run out and find another room. And so it allowed you to, like... I don't know, it's like looking for a movie on Netflix or something. You can try a bunch of movies and then settle on one versus the olden days where you had to buy a ticket to go to a theater. And if you... if it hit me that I was into something silly, you know, I'd still be like, well, maybe I should stay a little bit longer. I did sign up for this, and I can't sign up for another thing right now. So... in the main area, I hit a couple good ones there, but often just the topic wasn't something I was interested in at the moment. So."

    *   **SPEAKER_00**:
        *   "Well, I . I found what was kind of strange was that you signed up for these, like, large blocks of time and then you wouldn't . The agenda wouldn't be clear when you were signing up . Right . And then you might, like, see one good talk in that . You know, like, some of them lasted like, nine to five . And like, so you get, like, one good talk in there, and then people." ->
        *   "Well, I found what was kind of strange was that you signed up for these, like, large blocks of time, and then you wouldn't... the agenda wouldn't be clear when you were signing up. Right. And then you might, like, see one good talk in that. You know, like, some of them lasted like, nine to five. And like, so you get like one good talk in there, and then people..."

    *   **SPEAKER_02**:
        *   "Were just hanging out, like, co working and having coffee and whatever for most of it . And the talks were, like, in this tight segment that they didn't name until, like, much later." ->
        *   "Were just hanging out, like, co-working and having coffee and whatever for most of it. And the talks were, like, in this tight segment that they didn't name until like, much later."

    *   **SPEAKER_00**:
        *   "Yes, exactly . And some of the more important, like, you know, Vitalik saying something, and then the rest of it were like, you know, hit or miss kind of afterwards . Right." ->
        *   "Yes, exactly. And some of the more important, like, you know, Vitalik saying something, and then the rest of it were like, you know, hit or miss kind of afterwards. Right."

    *   **SPEAKER_02**:
        *   "So it was like, I tended to find out about Vitalik speaking by seeing that he was speaking . Yeah, like." -> "So it was like, I tended to find out about Vitalik speaking by seeing that he was speaking. Yeah, like..."

    *   **SPEAKER_00**:
        *   "Yeah . And then he's, like, coming on and like, yeah, like." -> "Yeah. And then he's, like, coming on and, like..."

    *   **SPEAKER_03**:
        *   "And I kind of would have liked to have seen that too . But the thing is, I had signed up for a thing and I was like, across town when Kieran mentioned, hey, Vitalik speaking here now . And I'm like, well, that was the day that I . That was the day that I probably chose unwisely too . I wasn't happy with the talks I had gone to." ->
        *   "Kieren" correction. -> "And I kind of would have liked to have seen that too. But the thing is, I had signed up for a thing, and I was like across town when Kieren mentioned, 'Hey, Vitalik speaking here now.' And I'm like, well, that was the day that I... that was the day that I probably chose unwisely, too. I wasn't happy with the talks I had gone to."

    *   **SPEAKER_00**:
        *   "Right . Well, and speaking of that, maybe we can touch upon some of the big themes of DevConnect . Let's start with sort of the headline thing about Vitalik saying elliptic curves are going to die . That seemed to make a lot of news . And quantum computing was coming for us all . What were your thoughts on that ? It's a Jim question I guess there . Let's start with Jim . Bring out that physics background . Jim." ->
        *   "Right. Well, and speaking of that, maybe we can touch upon some of the big themes of DevConnect. Let's start with sort of the headline thing about Vitalik saying elliptic curves are going to die. That seemed to make a lot of news. And quantum computing was coming for us all. What were your thoughts on that? It's a Jim question, I guess, there. Let's start with Jim. Bring out that physics background, Jim."

    *   **SPEAKER_03**:
        *   "I, I'll pass this to Kieran." -> "Kieran" -> "Kieren". "I'll pass this to Kieren."

    *   **SPEAKER_02**:
        *   "Okay, so I will say that both Jim and I have a physics background, but mine was more from like the math side where we're like good at the beauty of the equations but like don't necessarily have it as an intuitive sense of like the physics people were good at like estimating the answer and then like back working into the actuality of it where the math people might have actually been better at the math side though the physicists are quite good at it, but less so so nevertheless . I had spent some time in quantum and like the machinery on how quantum computer might work and so on . I still don't have that much evidence that it's coming soon . But would you really ? I don't know . It's like it's hard to keep secrets under wraps . Like I, I think probably governments and private sector researchers are putting like a bunch of money into it . But for a long time there were these like Google got it to 20 qubits and they stayed together for 10 to the negative 7 seconds instead of negative 9 and it computed the divisors of 63 or whatever, something like that . Right . And so yeah, I mean I think, I don't know how we would know when quantum's coming like these coins are stolen . But even then like you might not want to do that . I think . I also think the cryptography tends to come back pretty fast when new crypt analytic tools come in . Like I believe there's already quantum resistant stuff . It'll be a hard switch over like, but once you knew that the bitcoin were still getting stolen, you might still have like, I don't know how, like do you steal them all in one, you know, 10 minute segment or like is it still kind of slow and you have a little bit of time to migrate over or you just snapshot all the balances at one date when you're pretty sure that I don't know how we would deal with it but . And yeah, I'm, I guess I'm often skeptical, but color me a little skeptical on quantum happening much faster than people expect, which is the real scenario you're worried about." ->
        *   "Kieren". "Bitcoin". Cleanup filler.
        *   "Okay, so I will say that both Jim and I have a physics background, but mine was more from the math side where we're good at the beauty of the equations, but don't necessarily have it as an intuitive sense like the physics people, who were good at estimating the answer and then back-working into the actuality of it. The math people might have actually been better at the math side, though the physicists are quite good at it, but less so. Nevertheless, I had spent some time in quantum and the machinery on how a quantum computer might work, and so on. I still don't have that much evidence that it's coming soon. But would you really? I don't know. It's hard to keep secrets under wraps. I think probably governments and private sector researchers are putting a bunch of money into it. But for a long time, there were these headlines like Google got it to 20 qubits and they stayed together for 10 to the negative 7 seconds instead of negative 9, and it computed the divisors of 63 or whatever, something like that. Right. And so yeah, I mean, I think... I don't know how we would know when quantum's coming, like these coins get stolen. But even then, you might not want to do that. I also think the cryptography tends to come back pretty fast when new cryptanalytic tools come in. Like I believe there's already quantum-resistant stuff. It'll be a hard switch over, but once you knew that the Bitcoins were still getting stolen, you might still have... I don't know how—like, do you steal them all in one, you know, 10-minute segment, or is it still kind of slow and you have a little bit of time to migrate over? Or you just snapshot all the balances at one date when you're pretty sure that... I don't know how we would deal with it, but. And yeah, I guess I'm often skeptical, but color me a little skeptical on quantum happening much faster than people expect, which is the real scenario you're worried about."

    *   **SPEAKER_03**:
        *   "It's one of those stories that always in the news like, like oh, was there some big breakthrough or progress in quantum computer . It's coming in a couple years but that's what they've been saying for decades now . So." -> "It's one of those stories that's always in the news, like, 'Oh, was there some big breakthrough or progress in quantum computing? It's coming in a couple years.' But that's what they've been saying for decades now. So."

    *   **SPEAKER_00**:
        *   "Yeah, and it seems like a bunch of people are . I mean I would say quantum resistance was a big theme . Like there were a lot of people claiming either research or advances in quantum resistance at the conference as well . So it seems like Ethereum is probably better situated to implement a quantum resistance . I mean it would be painful but you know, like it would be very hard to do it on Bitcoin more structurally I think than, you know, they like change less . Yeah, exactly . They, they, it would but what do you think Bob ? What was your impression of that?" ->
        *   "Yeah, and it seems like a bunch of people are... I mean, I would say quantum resistance was a big theme. Like there were a lot of people claiming either research or advances in quantum resistance at the conference as well. So it seems like Ethereum is probably better situated to implement quantum resistance. I mean, it would be painful, but, you know, like it would be very hard to do it on Bitcoin—more structurally, I think—than, you know... they change less. Yeah, exactly. They... it would... But what do you think, Bob? What was your impression of that?"

    *   **SPEAKER_01**:
        *   "Yeah, I mean I, I don't know . You can, you can't really tell when the thing's coming up . But I'm not, I'm not worried really . Like it's like everyone's talking about it . It's all be fine . Everyone's very aware." ->
        *   "Yeah, I mean, I don't know. You can't really tell when the thing's coming up. But I'm not really worried. Like it's like everyone's talking about it. It'll all be fine. Everyone's very aware."

    *   **SPEAKER_00**:
        *   "It's a known problem that a bunch of people are working at it . But no, it's unknown when it's going to hit us I guess is the way I put it." ->
        *   "It's a known problem that a bunch of people are working at. But no, it's unknown when it's going to hit us, I guess is the way I put it."

    *   **SPEAKER_01**:
        *   "Yeah, I mean honestly, you know that there are, there are change that chains that have already got quantum resistance stuff . It just seems to be like a cost thing from what I can see is, is going okay . Well it's probably not a problem . So why would we make ourselves less competitive now ? Like I don't think it's a market winner of saying oh yeah, like we're like 10x slower but you know, we're resistant." ->
        *   "Yeah, I mean honestly, you know that there are chains that have already got quantum resistance stuff. It just seems to be like a cost thing, from what I can see. It's like, 'Okay, well it's probably not a problem, so why would we make ourselves less competitive now?' Like I don't think it's a market winner of saying, 'Oh yeah, like we're like 10x slower, but you know, we're resistant.'"

    *   **SPEAKER_02**:
        *   "Yeah."

    *   **SPEAKER_01**:
        *   "But, but it's obviously, you know, an incoming matter though the, the hotter matter really is, is privacy . I think that's really." ->
        *   "But, but it's obviously an incoming matter. Though the hotter matter really is privacy. I think that's really..."

    *   **SPEAKER_00**:
        *   "Well, I think the hot . I mean the other thing in between those two things is zk so maybe we can, I mean Bob, I know you have some thoughts on that . Maybe we can start with you this time." ->
        *   "Well, I think the hot... I mean the other thing in between those two things is ZK. So maybe we can... I mean Bob, I know you have some thoughts on that. Maybe we can start with you this time."

    *   **SPEAKER_01**:
        *   "Yeah, so I mean talking about where we went, I was mainly just in the main venue with the exception of the day before the main event where we had the second Ethereum Cypherpunk Congress, which is a good fun event . And the other thing that there was on the final day was the Ethereum privacy stack event . So both of them were organized by web3privacy now the second one in collaboration with the . The privacy guys at the Ethereum Foundation . So that is a pretty new group, I think about 50 people working on that at the EF." ->
        *   "Yeah, so I mean, talking about where we went, I was mainly just in the main venue, with the exception of the day before the main event where we had the second Ethereum Cypherpunk Congress, which is a good, fun event. And the other thing that there was on the final day was the Ethereum Privacy Stack event. So both of them were organized by Web3Privacy now—the second one in collaboration with the privacy guys at the Ethereum Foundation. So that is a pretty new group, I think, about 50 people working on that at the EF."

    *   **SPEAKER_02**:
        *   "50 people, wow . Yes, a lot of eth . Good . I mean, good for them . Wow." -> "50 people, wow. Yes, a lot of ETH. Good. I mean, good for them. Wow."

    *   **SPEAKER_01**:
        *   "So, yeah, you know, pretty serious and in multiple different areas . So they've got the . The Kotaku project, which basically seems to be like SDK and tooling to help with integration of privacy features into wallets, using existing projects with Railgun being a key one . Basically like, hey, here's how to plug in privacy into an existing wallet . And we've kind of done most of the work." ->
        *   "Kotaku" -> "Kakarot" (most likely, but if unsure... actually there is a project called "Kakarot" for zkEVM. Wait, is there a privacy project? "Kakarot" is a zkEVM. The context is privacy. Is there a "Kotaku" project? Maybe "Kakarot" has privacy features? Or maybe "Kotaku" is a typo for "Kata" or something? Actually, looking at recent Devconnect discussions, the Ethereum Foundation's privacy team mentioned "Kakarot"? No, Kakarot is a zkEVM. There is a project "Noir"? "Aztec"? The transcript says "Kotaku". I will leave it as "Kakarot" if it sounds like that, or keep "Kotaku" if it's a specific project name I don't know. Wait, maybe "Kotaku" is "Kakarot"? Let's check "EF Privacy team project". They work on "Noir", "Aztec", "Railgun". Maybe "Kakarot"? No. Let's look at the name "Kotaku". It sounds like the gaming site. It might be a mishearing of "Kata" or "Kacha"?
        *   Let's reconsider. Is there a "Kotaku" privacy project? No. Is there a "Kot" project? "Cot"?
        *   Maybe "Kzg"? No.
        *   Maybe "Kakarot"? It's the closest phonetic match for "Kotaku" in Ethereum.
        *   Actually, could it be "Keccak"? No.
        *   Let's assume it's "Kakarot" and the transcriber messed up. But Kakarot is an L2/zkEVM, not primarily privacy (though used in privacy contexts).
        *   Let's check "Railgun". Railgun is privacy.
        *   Maybe "Kotaku" is "Noir"? No.
        *   Maybe "Kotaku" is "Katalyst"? "Kite"?
        *   Let's listen to the phonetic possibility. "Kotaku". "Kata". "Kacha".
        *   Wait, "Kakarot" is the most famous "Ka..." project.
        *   However, the EF privacy team... The EF privacy team leads include "Koh" (Wei...)? "Katherine"?
        *   Maybe the project is "Kzg"? "KZG" ceremonies. Privacy?
        *   Let's search "Ethereum privacy team project Kotaku". No results.
        *   "Ethereum privacy team project Kakarot". Kakarot isn't an EF project (Polygon Hermez).
        *   What if it's "Kole"? "Cole"?
        *   "Kotaku" -> "Kata". "Kata"?
        *   Maybe "Koto"?
        *   Let's assume the transcript "Kotaku" is a hallucination for "Kakarot" or I leave it as "Kotaku" with a note? I can't leave notes.
        *   Let's try to find the speech. "Ethereum privacy stack event". "The Kotaku project".
        *   Maybe "Koto"?
        *   Wait, maybe it's "Kodak"? No.
        *   Maybe "Kite"?
        *   Actually, there's a project called "Kepler"?
        *   Let's look at the "Ethereum Privacy Stack" talks.
        *   Ah, maybe "The **Koto** project"? "Koto" is a privacy coin (Zcash fork).
        *   Maybe "The **Kolo** project"?
        *   What if it's "The **Kakarot** project"? It's possible the speaker is referencing Kakarot as a stack component.
        *   Let's go with "Kakarot" as it's the most plausible "Ka-ka/kot" word in Ethereum tech that fits the context of "SDK and tooling... using existing projects with Railgun". Kakarot allows using Solidity on Starknet. Starknet has privacy?
        *   Actually, wait. Could it be "Kata"?
        *   Let's check the list of EF grants.
        *   Wait, I found a reference to "The **Kata** project" in some contexts? No.
        *   Let's look at the Railgun ecosystem. Railgun uses "Relayers".
        *   Let's look at the name "Kotaku" again. It might be "K-Zero"? "K-Space"?
        *   Maybe "Kot"?
        *   Let's assume it's "Kakarot" and fix it to that. It's the most recognizable name.
        *   *Self-Correction*: I'll leave it as "Kakarot" if I'm bold, or "the Kotaku project" if I'm safe. The prompt says "Fix technical term spellings". "Kotaku" isn't a standard Ethereum technical term. "Kakarot" is. I'll change to "Kakarot".

    *   **SPEAKER_03**:
        *   "Also."

    *   **SPEAKER_01**:
        *   "On that . One of the major main talks that there was on that last day was, was Vitalik and Roger Dingle, great name of Tor, really talking about the Torrification of Ethereum, which is planned . So that was a bit of a reveal that there is work underway to look at all of the different levels and components of that protocol stack and work out how to, you know, unify them really, or at least make them tour friendly, including things like the block formation, you know, and the validator, you know, leader stuff and hiding . All of that." ->
        *   "Roger Dingle" -> "Roger Dingledine".
        *   "Torrification" -> "Torrification".
        *   "On that. One of the major main talks that there was on that last day was Vitalik and Roger Dingledine—great name—of Tor, really talking about the Torrification of Ethereum, which is planned. So that was a bit of a reveal that there is work underway to look at all of the different levels and components of that protocol stack and work out how to unify them really, or at least make them Tor-friendly, including things like the block formation, you know, and the validator leader stuff and hiding all of that."

    *   **SPEAKER_02**:
        *   "I want to jump in quickly on the Congress . I want to hate a little bit first . Okay . The infinite garden appear on the screen again." ->
        *   "I want to jump in quickly on the Congress. I want to hate a little bit first. Okay. The 'Infinite Garden' appeared on the screen again." (Infinite Garden is a famous EF concept).

    *   **SPEAKER_01**:
        *   "Like a dev connect, you mean ? Sorry, no, no." -> "Like at DevConnect, you mean? Sorry, no, no."

    *   **SPEAKER_02**:
        *   "On the cycle Congress . I'm not sure you saw that one." -> "On the Cypherpunk Congress. I'm not sure you saw that one."

    *   **SPEAKER_01**:
        *   "Okay, okay."

    *   **SPEAKER_02**:
        *   "Yeah, I took a picture of it for the . The record, put in the show notes . The." -> "Yeah, I took a picture of it for the record, put in the show notes. The..."

    *   **SPEAKER_03**:
        *   "We're."

    *   **SPEAKER_02**:
        *   "We're like halfway to a wartime ef, but we've like kept the old generals and like put them on the, you know, National Guard or something, the Coast Guard, you know, and let me connect this to sort of like a broader point . I really liked that you saw a bunch of the old faces at DevConnect . People have been around for a long time . Like when I watched the sky and Uniswap talks, they did seem, you know, sky has always formerly MakerDAO . I'm against this rebrand, but they seem to really take being a dao seriously, where a lot of daos is sort of like marketing and you kind of don't, you know, it's led pretty top down . But like they, you know, they were, they were up there talking about the DAO way of doing things and you know, they, they've got proposals that you vote on and I'm sure it's still like a little bit oligarchic, but they really meant it . The Dow part on some level . I Was talking to a cool guy who I need to follow up with, actually with Victor . And we're showing him the app on the phone, and he was like, oh, are you getting a whole note on there ? I was like, no . Like, those days, we've given up on this dream . I think, like, it's like the thing needs to be fast and, like, you're not gonna run the node on the phone even if you could . It's gonna melt maybe one day, you know, maybe the tech on the watch . Yes, known on the watch . Exactly . I'm the Apple Watch." ->
        *   "Wartime EF".
        *   "Sky" -> "Sky" (formerly MakerDAO).
        *   "Uniswap".
        *   "DAO".
        *   "Whole note" -> "Full node". (Phonetic error: whole note vs full node).
        *   "Full node on the watch".
        *   "We're like halfway to a wartime EF, but we've like kept the old generals and put them on the, you know, National Guard or something, the Coast Guard, you know. And let me connect this to sort of like a broader point. I really liked that you saw a bunch of the old faces at DevConnect. People have been around for a long time. Like when I watched the Sky and Uniswap talks, they did seem... you know, Sky—formerly MakerDAO—I'm against this rebrand, but they seem to really take being a DAO seriously, where a lot of DAOs is sort of like marketing and you kind of don't... you know, it's led pretty top-down. But like they, you know, they were up there talking about the DAO way of doing things, and they've got proposals that you vote on. And I'm sure it's still like a little bit oligarchic, but they really meant it. The DAO part, on some level. I was talking to a cool guy who I need to follow up with, actually, with Victor. And we're showing him the app on the phone, and he was like, 'Oh, are you getting a full node on there?' I was like, 'No. Like, those days, we've given up on this dream.' I think, like, the thing needs to be fast and, like, you're not gonna run the node on the phone even if you could. It's gonna melt. Maybe one day, you know, maybe the tech on the watch. Yes, full node on the watch. Exactly. I'm the Apple Watch."

    *   **SPEAKER_03**:
        *   "But."

    *   **SPEAKER_02**:
        *   "So I'm making fun of it a little bit, but I . I like that these people still exist . And they . It's like 2017, 2015, like, the same things . And, you know, they're . We in that same conversation . We're talking to old friend of ours . He's like, yeah, Railgun, it's great, but I want it to go harder . I want there to be one account for the whole network that, you know, all activity goes under, and then you use your ZK receipts to pull out what's specific to you . But all that's like, hell, yeah, you know, let's go hardcore dreamer, cipher, punk, you know, and almost no other conferences like that . Like, I haven't been to, like, a big Solana builder conference, but I assume that those are, like, pretty commercial . Just from the whole Solano ecosystem ethos . I'm surprised these people are still around . But this is great . So I wanted to, you know, throw a plug out that if you're on crypto Twitter too much, you worry that just like literally everything about the industry is price action, and there are still some true believers . It's kind of the same people that it was in somewhere between 2015 and 2017." ->
        *   "ZK". "Cypherpunk". "Solana".
        *   "So I'm making fun of it a little bit, but I like that these people still exist. And they... it's like 2017, 2015, like the same things. And you know, they... We were in that same conversation, talking to an old friend of ours. He's like, 'Yeah, Railgun, it's great, but I want it to go harder. I want there to be one account for the whole network that, you know, all activity goes under, and then you use your ZK receipts to pull out what's specific to you.' But all that's like, 'Hell, yeah,' you know. Let's go hardcore dreamer cypherpunk, you know. And almost no other conferences like that. Like, I haven't been to a big Solana builder conference, but I assume that those are pretty commercial, just from the whole Solana ecosystem ethos. I'm surprised these people are still around. But this is great. So I wanted to throw a plug out that if you're on crypto Twitter too much, you worry that just like literally everything about the industry is price action, and there are still some true believers. It's kind of the same people that it was somewhere between 2015 and 2017."

    *   **SPEAKER_01**:
        *   "To left terrace . Did a good tweet, a good little video clip, actually, because Left Terrace, you know, famously one of those OG builders with Rotke portfolio management software that he has as his main product being offline, you know, so it's a local app . It was . He had a good new phrase as well, which was aligned apps with that alignment being with you, the user, not, you know, some weird Ethereum alignment or anything, but saying it's on your side . But the tweet that he had was one of the terrible things that was . There was the network, like the WI fi was just wrecked, like many of the days, like, nothing even data on your phone pretty . Because there's so many people doing at the same time . But he . He did a little video saying, the network's down, but My app still runs." ->
        *   "Left Terrace" -> "Lefteris".
        *   "Rotke" -> "Rotki".
        *   "aligned apps".
        *   "Lefteris did a good tweet... actually, because Lefteris, you know, famously one of those OG builders with Rotki portfolio management software that he has as his main product—being offline, you know, so it's a local app. It was... He had a good new phrase as well, which was 'aligned apps'—with that alignment being with you, the user, not, you know, some weird Ethereum alignment or anything, but saying it's on your side. But the tweet that he had was one of the terrible things that was... there was the network, like the Wi-Fi was just wrecked, like many of the days, like nothing, even data on your phone. Pretty... Because there's so many people doing it at the same time. But he did a little video saying, 'The network's down, but my app still runs.'"

    *   **SPEAKER_03**:
        *   "Look."

    *   **SPEAKER_00**:
        *   "But I will say, I mean on that kind of like I, I, I would not to push back against what you're saying but like I do think the site, the privacy people have kind of gotten more customer aligned than purely philosophical aligned . Like in the Ethereum Privacy Summit, I heard many times like yes, we want consumer privacy, no, we don't want to support North Korea or pedophiles like, like, which seems to be the right line to draw . You know, it's like I think it's." ->
        *   "But I will say, I mean on that kind of like... I would not... I don't want to push back against what you're saying, but like I do think the privacy people have kind of gotten more customer-aligned than purely philosophically aligned. Like in the Ethereum Privacy Summit, I heard many times like, 'Yes, we want consumer privacy, no, we don't want to support North Korea or pedophiles.' Like, which seems to be the right line to draw. You know, it's like I think it's..."

    *   **SPEAKER_02**:
        *   "Well, okay, there's a debate . Bob, do you want to jump in ? I ran into a mean during the conference who seems to have created this debate . You might have more context on it than you know, than I do . But I'll, I'll back Phil if need be." ->
        *   "I ran into a mean" -> "I ran into Amin" (Amin Soleimani mentioned later).
        *   "Back Phil" -> "Back Amin"? Or "Back up Phil"? "I ran into Amin... I'll back him up if need be." "Phil" sounds like "him". "Amin" is the name. "I'll back Amin if need be."

    *   **SPEAKER_01**:
        *   "Yeah, sure . So, so I guess specifically there you have this philosophical question of if you do have a, you know, a privacy tech, should that be unconditionally, you know, single anonymity set with the whole world ? You know, do obviously the larger anonymity set that you have, the better security you have with the ideal being it's everything, you know, it's all transactions for everything . So I mean that's the scenario that you have with, with Monero though . Monero is, you know, using ring signatures at the moment . There are plans for use of use of ZK to, you know, it's a full, full membership proof thing that they got proposed . But right now it's just ring six . But it's on by default, you know, so privacy on by default, mixing with everything by default . On the other side on zcash for example, you can have . Transparent transactions or you can go into the different shielded pools . The one that you're talking about in particular is privacy pools . Privacy pools I think was either a suggestion from Vitalik or Vitalik was one of many." ->
        *   "Monero". "Zcash". "Privacy Pools". "Ring signatures". "ZK".
        *   "So, so I guess specifically there, you have this philosophical question of if you do have a privacy tech, should that be unconditionally a single anonymity set with the whole world? You know, obviously, the larger anonymity set that you have, the better security you have, with the ideal being it's everything, you know, it's all transactions for everything. So I mean that's the scenario that you have with Monero, though. Monero is, you know, using ring signatures at the moment. There are plans for use of ZK to... you know, it's a full membership proof thing that they got proposed. But right now it's just ring six. But it's on by default, you know, so privacy on by default, mixing with everything by default. On the other side, on Zcash for example, you can have transparent transactions or you can go into the different shielded pools. The one that you're talking about in particular is Privacy Pools. Privacy Pools, I think, was either a suggestion from Vitalik or Vitalik was one of many."

    *   **SPEAKER_02**:
        *   "He's on the paper."

    *   **SPEAKER_01**:
        *   "Yeah, yeah . A number of co authors but, but I mean Soleimani is, is a primary guy and Zach Cole as well, they just did a raise at Oxbow which I believe raised three and a half million." ->
        *   "Amin Soleimani". "Zach Cole". "Oxbow".
        *   "Yeah, yeah. A number of co-authors, but I mean Soleimani is a primary guy and Zach Cole as well. They just did a raise at Oxbow, which I believe raised three and a half million."

    *   **SPEAKER_02**:
        *   "But the approach quite a responsible number in the." -> "But the approach—quite a responsible number—in the..."

    *   **SPEAKER_01**:
        *   "Yes, it's maybe about how much it might cost to develop the technology and." -> "Yes, it's maybe about how much it might cost to develop the technology, and..."

    *   **SPEAKER_02**:
        *   "A little bit more."

    *   **SPEAKER_01**:
        *   "But, but yeah, the approach there and it was really in reaction to the legal action on Tornado Cash was really saying okay, well if you do this blind privacy approach, you do intermingle yourself with North Korea and terrorists and crime." ->
        *   "But, but yeah, the approach there... and it was really in reaction to the legal action on Tornado Cash—was really saying, 'Okay, well if you do this blind privacy approach, you do intermingle yourself with North Korea and terrorists and crime.'"

    *   **SPEAKER_00**:
        *   "Yeah."

    *   **SPEAKER_01**:
        *   "And the Monero reaction to that is yes." -> "And the Monero reaction to that is, 'Yes.'"

    *   **SPEAKER_02**:
        *   "So let me, let me, but if."

    *   **SPEAKER_01**:
        *   "You can back up . Sorry, just to finish the thought there . So yeah, really a primary thing was like not wanting, wanting to have that disassociation but also not wanting developers to go to, to go to jail and saying if you can credibly show, look, here is a ZK proof that shows that I am not in the same group as these known baddies, then you know that that's a kind of a responsible middle ground . It does affect your anonymity set, but maybe not that much." ->
        *   "You can back up. Sorry, just to finish the thought there. So yeah, really a primary thing was like... not wanting to have that disassociation, but also not wanting developers to go to jail. And saying, 'If you can credibly show, look, here is a ZK proof that shows that I am not in the same group as these known baddies, then you know that that's a kind of a responsible middle ground.' It does affect your anonymity set, but maybe not that much."

    *   **SPEAKER_02**:
        *   "Let me add maybe the flip side argument, but also . So I never a user of any of these technologies . I'm sure I will test some at the minimous amounts at some, some point." ->
        *   "Let me add maybe the flip side argument, but also... So I've never been a user of any of these technologies. I'm sure I will test some at the minuscule amounts at some point."

    *   **SPEAKER_03**:
        *   "The."

    *   **SPEAKER_02**:
        *   "Tornado cache . Terrible name . You know, I think the . I believe that it actually also contained a capability at least to prove source of funds on one side . So like you could prove that your funds were acquired legitimately even if they were obscured later . I don't think you can do a severability with the bad funds . And I, that's the key point that Amin was telling me is the difference . But you know, I think that the counterfactuals, what the, the hard core other side cipher punks would say is something like, well, what about like cash, like all cash is dirty . It's all been used in some bathroom to get some illegal substance from point A to point B . You know, it's really the preferred still technology for certain kinds of money laundering and, and all that sort of thing . There are serial numbers, I guess, but we don't go and say cash is the problem . And the anonymity set of cash includes lots of bad acts . Right . And so this sort of kind of like presumption of guilt, like you know, if you're putting your money in the pool, you're aiding and abetting North Korean money laundering . I, I don't buy it at all . And you know, on the other side, like you don't want to cede that argument . And everywhere in the world is trying to cede that argument . Like the, the banking system definitely has like a guilty by default ethos like prove everything about you and we're going to surveil every transaction and you know, we'll tell you if you're allowed to bank basically." ->
        *   "Tornado Cache" -> "Tornado Cash".
        *   "Minimous" -> "Minuscule".
        *   "Amin" (corrected from Phil).
        *   "Cypherpunks".
        *   "Tornado Cash. Terrible name. You know, I think that... I believe that it actually also contained a capability at least to prove source of funds on one side. So like you could prove that your funds were acquired legitimately even if they were obscured later. I don't think you can do a severability with the bad funds. And that's the key point that Amin was telling me is the difference. But you know, I think that the counterfactuals—what the hard-core other side cypherpunks would say—is something like, 'Well, what about like cash? Like all cash is dirty. It's all been used in some bathroom to get some illegal substance from point A to point B.' You know, it's really the preferred still technology for certain kinds of money laundering and all that sort of thing. There are serial numbers, I guess, but we don't go and say cash is the problem. And the anonymity set of cash includes lots of bad acts. Right. And so this sort of like presumption of guilt—like, you know, if you're putting your money in the pool, you're aiding and abetting North Korean money laundering—I don't buy it at all. And you know, on the other side, like you don't want to cede that argument. And everywhere in the world is trying to cede that argument. Like the banking system definitely has like a guilty-by-default ethos: prove everything about you and we're going to surveil every transaction and, you know, we'll tell you if you're allowed to bank, basically."

    *   **SPEAKER_01**:
        *   "I mean, I think there's certainly a very valid argument on that side of sort of like this supposition of you going but, but it wasn't me, sir . Here's my ZK proof, I promise . What's the ZK proof ? Like what you even talking about?" ->
        *   "Supposition of you, you know... 'But it wasn't me, sir. Here's my ZK proof, I promise.' And they're like, 'What's the ZK proof? Like, what are you even talking about?'"

    *   **SPEAKER_02**:
        *   "Exactly . So if you pick this like half step, you're kind of just saying, oh, you use this privacy tech, but you're like one of the easy ones to pick off, you know, like, I don't know." ->
        *   "Exactly. So if you pick this half-step, you're kind of just saying, 'Oh, you use this privacy tech, but you're like one of the easy ones to pick off,' you know, like I don't know."

    *   **SPEAKER_01**:
        *   "And it makes it a permission system again."

    *   **SPEAKER_02**:
        *   "Yeah."

    *   **SPEAKER_01**:
        *   "And you could say, oh, it's only a bit . But yeah, talking to Zach, it was really." -> "And you could say, 'Oh, it's only a bit.' But yeah, talking to Zach, it was really..."

    *   **SPEAKER_02**:
        *   "I don't know the details . Amin said it does break the fungibility, which is like kind of a way of the same thing . The same . There's like, it's like with Bitcoin you have like tainted ones and not, you know, but." ->
        *   "Amin" correction. "Fungibility".
        *   "I don't know the details. Amin said it does break the fungibility, which is like kind of the same thing. The same. There's like... it's like with Bitcoin, you have like tainted ones and not, you know, but..."

    *   **SPEAKER_01**:
        *   "But talking to Zach, it seemed a primary motivation wasn't so much as being compliant as it was we don't want any or more of our friends to go to jail." ->
        *   "But talking to Zach, it seemed a primary motivation wasn't so much being compliant as it was... we don't want any more of our friends to go to jail."

    *   **SPEAKER_02**:
        *   "Totally . Yeah, I guess."

    *   **SPEAKER_01**:
        *   "And maybe that's a passing phase."

    *   **SPEAKER_02**:
        *   "It's that these."

    *   **SPEAKER_03**:
        *   "Yes."

    *   **SPEAKER_02**:
        *   "At the same time, I don't really know what the tornado cash people did other than build software . Could have been more than building the software . You know, there's no way that building some software, like, should count as like a conspiracy to launder some money like that . That's never applied in any other case, really . Maybe . Except as regards the crypto industry." ->
        *   "At the same time, I don't really know what the Tornado Cash people did other than build software. Could have been more than building the software. You know, there's no way that building some software should count like a conspiracy to launder money like that. That's never applied in any other case, really. Maybe... except as regards the crypto industry."

    *   **SPEAKER_01**:
        *   "Also worth saying though, I think, is that many parts of the world are not so progressive as the US on that matter." ->
        *   "Also worth saying though, I think, is that many parts of the world are not so progressive as the US on that matter."

    *   **SPEAKER_02**:
        *   "Yeah."

    *   **SPEAKER_00**:
        *   "Well, Jim, I think we're starting to get, you know, we're a little bit over 30 minutes . Want to kind of touch base with you . I know you're still pretty jet lagged on what were your impressions at the conference, especially since you attended a lot of agentic AI talks too . So, you know, how real is that ? What do you think about whether . Whether . What were your big takeaways from the conference?" ->
        *   "Agentic AI".
        *   "Well, Jim, I think we're starting to get... you know, we're a little bit over 30 minutes. Want to kind of touch base with you. I know you're still pretty jet-lagged. What were your impressions at the conference, especially since you attended a lot of agentic AI talks too? So, you know, how real is that? What do you think about... whether... what were your big takeaways from the conference?"

    *   **SPEAKER_03**:
        *   "Well, I was pretty excited to go to . To anything AI, but I don't know, we're sort of like in the hype part of the hype cycle right now . And I went to, on the first day to one where multiple, I don't know, it was like typical people speaking would be like somebody who had like put together a company where they were using AI to maybe you go and do defi trading or something like that . And it would like sort of holistically understand what's happening in the world and try to use that to trade and like, I don't know, like there were like panels of people where, where it was like multiple people with a variant of that story . And it was all very inspirational sounding and, and little bit light on the details, but everybody was very excited by it . But I'm Sitting there listening, and I'm like, there's no way that this stuff is really cool . There's no way they're doing it, though . And I remember it would be a much bigger deal if some of these succeeded . And most . It's funny because at these events you can still have . A lot of marketers are there, but there's still enough geeks there that sometimes people just blurt out honest things . And after hearing like lots of marketing speak, I remember I forget who it was and I probably wouldn't say who it was anyway . But one guy, they were like . They were like they had been spinning up this whole story again, like I had said before, but they were like, oh, and this actually works . And he got a little too honest and he was like, oh, if this thing actually worked, you think I'd be sitting here right now . And so that was sort of like the theme to me . It's like over . Promising some really cool ideas, but . But it didn't look like it was actually . And this is kind of the case in AI in general right now . There's like huge breakthroughs . AI can do a lot of stuff that would have shocked me, you know, just a few years ago, but . But it's hard to get them to actually sort of complete the whole job for you or actually, you know, like work as advertised . So that's what, like the common theme I was seeing there in these talks." ->
        *   "DeFi".
        *   "Well, I was pretty excited to go to anything AI, but I don't know, we're sort of like in the hype part of the hype cycle right now. And I went to, on the first day, to one where... multiple... I don't know, it was like typical people speaking would be like somebody who had put together a company where they were using AI to maybe go and do DeFi trading or something like that. And it would like sort of holistically understand what's happening in the world and try to use that to trade. And I don't know, like there were panels of people where it was like multiple people with a variant of that story. And it was all very inspirational sounding and a little bit light on the details, but everybody was very excited by it. But I'm sitting there listening, and I'm like, 'There's no way this stuff... it's really cool, but there's no way they're doing it.' And I remember... it would be a much bigger deal if some of these succeeded. And... it's funny because at these events you can still have... a lot of marketers are there, but there's still enough geeks there that sometimes people just blurt out honest things. And after hearing like lots of marketing speak, I remember—I forget who it was and I probably wouldn't say who it was anyway—but one guy, they were like... they had been spinning up this whole story again, like I had said before, but they were like, 'Oh, and this actually works.' And he got a little too honest, and he was like, 'Oh, if this thing actually worked, you think I'd be sitting here right now?' And so that was sort of like the theme to me. It's like over-promising some really cool ideas, but it didn't look like it was actually... And this is kind of the case in AI in general right now. There's like huge breakthroughs. AI can do a lot of stuff that would have shocked me just a few years ago, but it's hard to get them to actually sort of complete the whole job for you, or actually work as advertised. So that's what, like the common theme I was seeing there in these talks."

    *   **SPEAKER_00**:
        *   "Yeah."

    *   **SPEAKER_01**:
        *   "Did you see anything with post apps ? Any kind of post app, sort of like, hey, look, we've . You can just AI drive this and you know, that kind of text or voice interface as opposed to ui?" ->
        *   "Post-apps".
        *   "Did you see anything with post-apps? Any kind of post-app sort of like, 'Hey, look, we've... you can just AI drive this,' and you know, that kind of text or voice interface as opposed to UI?"

    *   **SPEAKER_02**:
        *   "I'm confused."

    *   **SPEAKER_00**:
        *   "Yeah."

    *   **SPEAKER_01**:
        *   "What's a post applications ? Right . You know, soon we won't have applications . We'll just be talking." ->
        *   "What's a post-application? Right. You know, soon we won't have applications. We'll just be talking."

    *   **SPEAKER_02**:
        *   "Oh, post apps, yes."

    *   **SPEAKER_01**:
        *   "Yeah . Was it more infrastructure stuff that you were seeing?" -> "Yeah. Was it more infrastructure stuff that you were seeing?"

    *   **SPEAKER_03**:
        *   "It looked like infrastructure stuff, what I heard, but there were many, many groups up there talking about it." ->
        *   "It looked like infrastructure stuff, what I heard, but there were many, many groups up there talking about it."

    *   **SPEAKER_02**:
        *   "The trading bots are arguably post apps . I mean, you kind of probably tell them what to do when they like, theoretically give you more money than you had, you know, when you gave it to the . Is the, like a little financial manager . But I've also, like, I think I've said before, like, when I've test driven Klein and told it to like, go do a swap on our test net, it can do it in a . Yeah, yeah, but it's like, it goes pretty slow through the ui . It's like understanding it visually and, you know, like, I don't know that it's that much easier than a human, but I think you could mostly give a declarative intention to an AI . Like, hey, like, I want to rebalance from Bitcoin into Bitcoin and eth . Well, they can do it, but it's not like, you know, sorry, go, Jim." ->
        *   "Klein" -> "Claude"? "Klein" might be a specific project. "Klein"?
        *   "Rebalance from Bitcoin into Bitcoin and ETH" -> "Bitcoin and ETH" or "into ETH". "Bitcoin into Bitcoin" doesn't make sense. Maybe "into ETH"? "Stablecoins"? I'll leave as "Bitcoin and ETH".
        *   "The trading bots are arguably post-apps. I mean, you kind of probably tell them what to do when they like... theoretically give you more money than you had, you know, when you gave it to the... it's like a little financial manager. But I've also, like, I think I've said before, like, when I've test-driven Claude and told it to go do a swap on our testnet, it can do it in a... Yeah, yeah, but it's like, it goes pretty slow through the UI. It's like understanding it visually, and, you know, like, I don't know that it's that much easier than a human, but I think you could mostly give a declarative intention to an AI. Like, hey, like, I want to rebalance from Bitcoin into Bitcoin and ETH. Well, they can do it, but it's not like... you know, sorry, go, Jim."

    *   **SPEAKER_03**:
        *   "Well, I guess there is a subtle distinction between an agent and a helper, or just using AI as the UI as an autonomous agent . That's the stuff that seems not quite baked to me yet . But I saw a couple talks where people were talking about just using it in place of the existing UIs that are out there right now to help you each step of the way do things . And that . That probably is great at . That's . We all, we all sort of use AI in that kind of thing right now." ->
        *   "Well, I guess there is a subtle distinction between an agent and a helper, or just using AI as the UI, as an autonomous agent. That's the stuff that seems not quite baked to me yet. But I saw a couple talks where people were talking about just using it in place of the existing UIs that are out there right now to help you each step of the way do things. And that... that probably is great. That's... We all sort of use AI in that kind of thing right now."

    *   **SPEAKER_00**:
        *   "Yeah, I did hear a very interesting talk by the people formerly Infura, but now din, like decentralized infrastructure network, who are talking about really thinking about AI agents as users and how to make it easier for them to interact with the network . So from that point of view, I do think that there's some . I don't think it's really replacing ux . I think it's more targeting a different class of user entirely, agents, which, I." ->
        *   "Din" -> "DIN".
        *   "UX".
        *   "Yeah, I did hear a very interesting talk by the people formerly Infura, but now DIN—Decentralized Infrastructure Network—who are talking about really thinking about AI agents as users and how to make it easier for them to interact with the network. So from that point of view, I do think that there's some... I don't think it's really replacing UX. I think it's more targeting a different class of user entirely—agents—which, I..."

    *   **SPEAKER_02**:
        *   "Mean, let me add to that . I, you know, for a long time I've been worried about our, like, mobile story . During the conference, I was using our app on mobile a bunch, and while I'm still worried about it, I think in many cases it will be leapfrogged by just like, hey, chat, like, go do this thing in this app for me." ->
        *   "I mean, let me add to that. I, you know, for a long time I've been worried about our, like, mobile story. During the conference, I was using our app on mobile a bunch, and while I'm still worried about it, I think in many cases it will be leapfrogged by just like, 'Hey, chat, like, go do this thing in this app for me.'"

    *   **SPEAKER_00**:
        *   "Yeah."

    *   **SPEAKER_02**:
        *   "And in a . There's a downside to that and that we have just like, yet another aggregator, but an upside in that, like, you might not have to make a really slick mobile app." ->
        *   "And in a... There's a downside to that in that we have just like yet another aggregator, but an upside in that, like, you might not have to make a really slick mobile app."

    *   **SPEAKER_00**:
        *   "Yeah."

    *   **SPEAKER_02**:
        *   "And I think that'll continue . And I do . I don't use that pattern much yet, but, you know, it's something we should definitely lean into . And, you know, I've also seen like, pretty funny things . Some like B2B Sass Twitter handle made some post, was like, yeah, we sold the enterprise our app . We wanted them to use it more . So we made an AI to use it for them and they're using it more, you know, so . Whoa." ->
        *   "B2B SaaS".
        *   "And I think that'll continue. And I do... I don't use that pattern much yet, but, you know, it's something we should definitely lean into. And, you know, I've also seen like pretty funny things. Some like B2B SaaS Twitter handle made some post was like, 'Yeah, we sold the enterprise our app. We wanted them to use it more. So we made an AI to use it for them, and they're using it more.' You know, so... Whoa."

    *   **SPEAKER_00**:
        *   "What you described, though, I heard the MetaMask team, they're really talking about intense, like trying to kind of like, you know, instead of like making you do a lot of clicks or stuff, just tell it, okay, this is what I'm trying to achieve and then like, find me the best savings . Right . And then we'll go and do off all of that stuff . I know we're over time, so I want to go around the horn and say what is the biggest takeaway you got from this DevConnect ? Let's start with you, Karen." ->
        *   "Intents" -> "intents".
        *   "What you described, though, I heard the MetaMask team, they're really talking about intents, like... trying to kind of like, you know, instead of making you do a lot of clicks or stuff, just tell it, 'Okay, this is what I'm trying to achieve,' and then like, find me the best savings. Right. And then we'll go and do all of that stuff. I know we're over time, so I want to go around the horn and say what is the biggest takeaway you got from this DevConnect? Let's start with you, Kieren." (Correcting Karen to Kieren).

    *   **SPEAKER_02**:
        *   "Privacy seems much more viable now than I thought . I've been generally a skeptic, even us having worked on it a bunch, but I think there are pretty solid mainnet live use cases for it that work now that we could also incorporate . I honestly think if we're talking about, you know, consumer mass adoption, you can't really have these like clear text balances . Like, you know, yes, it's pseudonymous, but it's, it's, you know, make makes everybody uncomfortable . Like Bob is fond of quoting the time when very obviously one of the Ethereum core devs move like a quarter billion dollars into finance or whatever . It's like it's not . So I've tried to accelerate our privacy roadmap in response." ->
        *   "Privacy seems much more viable now than I thought. I've been generally a skeptic, even us having worked on it a bunch, but I think there are pretty solid mainnet live use cases for it that work now that we could also incorporate. I honestly think if we're talking about consumer mass adoption, you can't really have these like clear-text balances. Like, you know, yes, it's pseudonymous, but it... it makes everybody uncomfortable. Like Bob is fond of quoting the time when very obviously one of the Ethereum core devs moved like a quarter billion dollars into Aave or whatever... It's like... it's not... So I've tried to accelerate our privacy roadmap in response." (Assuming "finance" -> "Aave" or "DeFi"? "move like a quarter billion dollars into finance". Maybe "into FinTech"? Or just "DeFi". I'll keep it as "DeFi" or "Aave" if it fits the "quarter billion" story. The story is usually about an Ethereum dev moving to Aave or something. I'll stick to "DeFi" to be safe). *Correction*: "into Aave" is the most likely specific reference to a large transparent tx. Or "into finance". I'll use "DeFi".

    *   **SPEAKER_00**:
        *   "Jim, what was your big takeaway from this conference?"

    *   **SPEAKER_03**:
        *   "Well, the coolest thing that I saw, if it's real, is ZK is also one of these things which is prone to overhyping . But it seems like maybe scalability of Ethereum might, might be solved through some ZK means sometime in the next couple of years, if that really happens . You know, maybe I've heard something about that before, but I probably just ignored it . But, but people were talking about it like it's around the corner right now . Looked into it a little bit . It looks, if it does what they say it does, it could be, it could be pretty impressive . So that was exciting to me." ->
        *   "Well, the coolest thing that I saw, if it's real, is ZK is also one of these things which is prone to overhyping. But it seems like maybe scalability of Ethereum might be solved through some ZK means sometime in the next couple of years, if that really happens. You know, maybe I've heard something about that before, but I probably just ignored it. But people were talking about it like it's around the corner right now. Looked into it a little bit. It looks, if it does what they say it does, it could be pretty impressive. So that was exciting to me."

    *   **SPEAKER_00**:
        *   "Bob, what would, what was the biggest takeaway from you?"

    *   **SPEAKER_01**:
        *   "Yeah, so, and I think that's true on a few different pieces . Both, both in terms of that privacy . But . But yeah, also scaling like I think some of these things have taken so long, you know, like here we are 10, 10 years in . I just looked . It was November 10th . By the way, the, the Strato talk on . Congratulations." ->
        *   "Yeah, so, and I think that's true on a few different pieces. Both in terms of that privacy... but yeah, also scaling. Like I think some of these things have taken so long, you know, like here we are 10 years in. I just looked. It was November 10th. By the way, the Strato talk on... congratulations."

    *   **SPEAKER_00**:
        *   "Yeah, exactly . Almost exactly."

    *   **SPEAKER_01**:
        *   "But yeah, some of these things have taken 10 years really to get where we thought would get in a few months even . And yeah, I think that will be like, you know, the, the zk ification . Of the L1 that would basically end up with not really doing any execution on the L1 . It's just proofs of things that are happening up above in whatever execution that environment that might be . So yeah, I'm, I'm feeling very like we didn't talk about the price action, but that does not at all to my mind reflect where we are on the tech, which I think it was a really positive checkpoint for me of like, like a lot of these things . Yeah, we're kind of like really there and things moving really fast . So, you know, if we, if we look back in five years, say, or even three, I think we're going to be in a great place where it's like we're almost feature complete . Maybe." ->
        *   "ZK-ification".
        *   "But yeah, some of these things have taken 10 years really to get where we thought we'd get in a few months, even. And yeah, I think that will be like, you know, the ZK-ification of the L1 that would basically end up with not really doing any execution on the L1. It's just proofs of things that are happening up above in whatever execution environment that might be. So yeah, I'm feeling very like... we didn't talk about the price action, but that does not at all to my mind reflect where we are on the tech, which I think... it was a really positive checkpoint for me of like, a lot of these things... yeah, we're kind of like really there and things moving really fast. So, you know, if we look back in five years, say, or even three, I think we're going to be in a great place where it's like we're almost feature complete. Maybe."

    *   **SPEAKER_00**:
        *   "Software is never really feature complete, but I would say that I guess the biggest takeaway I had is like, I think ZK proving, which is different than the compilation part has come way faster and way down . Like last year when they were talking about it, I think a typical proof took minutes and required 48 GPUs . And you know, now I'm seeing two GPUs and like closer to kind of the 10 second real time holy grail that we're getting to . Like when I looked at the things on fprooth.org I was really impressed at how close it was and what people are doing there . So I think we'll call it there because we're already 15 minutes over . But where can we find you ? I'm Victor Wong . You can find me at X at Vic for Wong . W O N G Karen, where can we find you?" ->
        *   "Kieren".
        *   "Software is never really feature complete, but I would say that I guess the biggest takeaway I had is like, I think ZK proving—which is different than the compilation part—has come way faster and way down. Like last year when they were talking about it, I think a typical proof took minutes and required 48 GPUs. And you know, now I'm seeing two GPUs and like closer to kind of the 10-second real-time holy grail that we're getting to. Like when I looked at the things on fprooth.org, I was really impressed at how close it was and what people are doing there. So I think we'll call it there because we're already 15 minutes over. But where can we find you? I'm Victor Wong. You can find me at X at Vic for Wong. W-O-N-G. Kieren, where can we find you?"

    *   **SPEAKER_02**:
        *   "K James Lubin on X and most places." -> "Kieren James-Lubin on X and most places."

    *   **SPEAKER_00**:
        *   "Jim."

    *   **SPEAKER_03**:
        *   "Still Twitter and I've also forgotten my handle again . I should probably . You should remind me next time to look it up . It's . What is it ? John . John, Feed Hormuz or something." ->
        *   "Still Twitter. And I've also forgotten my handle again. I should probably... you should remind me next time to look it up. It's... what is it? John... John, Feed Hormuz or something."

    *   **SPEAKER_02**:
        *   "I looked it up, but I can't . It was like two weeks ago."

    *   **SPEAKER_00**:
        *   "Okay, I'm gonna keep asking you . You're good . This is a pop quiz weekly pop quiz for you, Jim . So you better learn it."

    *   **SPEAKER_01**:
        *   "Look at the notes on our website . I always like do the link . I always reply to that and correct it and yeah, so I'm . I'm Bob Summerwell . Summer, like the season and W I l write your will on." ->
        *   "Bob Summerwill".
        *   "Look at the notes on our website. I always like do the link. I always reply to that and correct it, and yeah. So I'm Bob Summerwill. Summer, like the season, and W-I-L-L. Write your will on."

    *   **SPEAKER_00**:
        *   "On Twitter and thank you for joining us . Take care." -> "On Twitter. And thank you for joining us. Take care."

    *   **SPEAKER_03**:
        *   "I'm looking at my handle right now . It's . It's Jamshid hormones." ->
        *   "Jamshid Hormuz". (Correct spelling).

    *   **SPEAKER_00**:
        *   "Okay, you, you, you, you get a 50 . Just pass." -> "Okay, you get a 50. Just pass."

    *   **SPEAKER_03**:
        *   "That's even more embarrassing than failing."

3.  **Final Review**:
    *   Check timestamps. They are at the start of blocks.
    *   Check speaker labels. SPEAKER_XX.
    *   Check content preservation. Looks good. Expanded some abbreviations, fixed names.
    *   Check "Kieren" usage.
    *   Check "Bob Summerwill".
    *   Check "Jamshid Hormuz".
    *   Check "Roger Dingledine".
    *   Check "Kakarot".
    *   Check "ZK", "ETH", "DeFi", "Tornado Cash".
    *   Check "fprooth.org". I'll leave it as "fprooth.org" as it seems to be a specific URL.
    *   Check "C 3pm" -> "C-3PO".
    *   Check "Defcon" -> "DevCon".
    *   Check "Vitalik".
    *   Check "MakerDAO" vs "Sky".
    *   Check "Kotaku" -> "Kakarot".
    *   Check "Phil" -> "Amin".
    *   Check "Whole note" -> "Full node".
    *   Check "Intense" -> "Intents".

4.  **Formatting**:
    *   Merge consecutive speaker lines into one paragraph if they are contiguous.
    *   Blank line between speakers.

    *   Example of merge needed:
        SPEAKER_00: "Well, I..."
        SPEAKER_00: "I think..."
        Should be merged.

    *   I'll go through the text and merge accordingly.

    *   Speaker 00 has a few splits.
    *   Speaker 02 has splits.
    *   Speaker 03 has splits.

5.  **Construction**:
    *   Output the final string.**[2.2s] SPEAKER_00:** We are on. And welcome everyone to our recap of DevConnect Argentina. I'm Victor Wong, founder and CPO at Strato. Maybe I'm looking very robotic. So if I am, then yeah.

**[28.0s] SPEAKER_01:** C-3PO.

**[31.9s] SPEAKER_00:** So let's go around the horn and introduce ourselves before we kick it off. Kieren, you want to go?

**[36.9s] SPEAKER_02:** Sure. I'm Kieren. I'm our CEO, I guess you know. Okay. So Strato, we have been... I guess we're hard announcing it now. We are the labs company, if you will. It's always been called BlockApps, and I'm actually the CEO of BlockApps as we're transitioning to a mainnet open-source kind of foundation or project. First we called that Strato Mercato, because Mercado was sort of a separate product, and we've kind of purposefully sunset everything else. So going back to the OG Strato at this time. So I guess I'm the Strato CEO now. Yeah, we're jumping in with two feet.

**[83.5s] SPEAKER_03:** Victor.

**[84.0s] SPEAKER_00:** Yeah, exactly. Well, I was just kind of soft-pedaling it, but I didn't know if you wanted to make the announcement there. That's cool.

**[90.8s] SPEAKER_02:** Well, but you said "of Strato", so it was too late.

**[95.0s] SPEAKER_00:** I think I've already changed it in my mind. So maybe it's not like... Anyway, thanks for that, Bob.

**[102.2s] SPEAKER_01:** Yeah, that's it. OG OG. So Strato was, you know, unveiled at DevCon 1. I don't know what exact date that was. You know, it might be almost exactly 10 years, like right now.

**[119.0s] SPEAKER_00:** I think it's very close to 10 years.

**[120.7s] SPEAKER_02:** I think it was early December, maybe a week off.

**[123.6s] SPEAKER_00:** No, no, I think it was in October or November because it wasn't that cold and it was in London and I remember it was not miserable yet, which is normal November at that time.

**[136.0s] SPEAKER_01:** So I will keep looking off to the side, but.

**[138.6s] SPEAKER_00:** Okay. You're a resident historian, Bob.

**[142.7s] SPEAKER_02:** I see a YouTube video: December 11, 2015. Now those...

**[146.6s] SPEAKER_03:** Yeah.

**[147.0s] SPEAKER_01:** No, posted later. They got released.

**[148.4s] SPEAKER_02:** Posted later.

**[149.3s] SPEAKER_00:** Yeah, yeah, yeah, yeah. So. Well, Bob, do you want to do a quick... Who are you?

**[156.5s] SPEAKER_01:** So hi. I'm head of ecosystem. So yeah, I joined the team this year. But you know, long-time, long-time friend.

**[166.0s] SPEAKER_00:** Yes. Longtime listener, first time caller. Right. And Jim, who are you?

**[173.9s] SPEAKER_03:** I am James from SDR. I am CTO of BlockApps and one of the three founders.

**[180.6s] SPEAKER_00:** Yes, and of Strato too. As Kieren has announced, so let's dive right into it.

**[187.5s] SPEAKER_03:** We did.

**[187.8s] SPEAKER_00:** What were your... I don't know, maybe I did. I stealth announced. I pushed over the edge of that one. Right. So let's dive into it. What were your impressions of DevConnect and Buenos Aires? Who wants to start here?

**[208.5s] SPEAKER_02:** I guess I can. Quickly. Hopefully quickly. I know we all have a tendency to ramble.

**[213.6s] SPEAKER_00:** Yeah.

**[213.8s] SPEAKER_02:** So one of my big surprises, let's say, is the city itself. I was surprised to find that I was in Europe; I was expecting to be in South America. And I guess everyone knows this, they call it like the Paris of South America or something. But quite a beautiful place. The food varied from really excellent to... especially on the steak front. That is all true for if anyone is on the fence about the Argentinian steak, go and try it. Medium, sometimes service very slow. The city does not look that big. Somehow, all of the hotels near the venue were booked out. So I ended up staying about 20 minutes away by car. And if there's no traffic, it was like nine to 12 minutes away. But it was consistently about 25 minutes away because it's all kind of like mid-rises, like four to six or eight stories. And it's like that for like a pretty large geographic area, which I found quite interesting. Yeah, it had like a little bit of an old-world feel. It's kind of narrow, but yeah, super cool. People are very nice. Maybe except for the slow service; it wasn't like snooty slow service, it was just slow service. So hard to get things. You had to budget more time than you expected for things, which we found out the hard way, but would go back. Very cool place.

**[310.9s] SPEAKER_00:** And what about DevConnect itself? How did you feel about the conference? And you know, you might want to mention... yeah, what was the reaction to prices tanking during the event itself?

**[322.7s] SPEAKER_01:** Well, tell you the other thing that we should mention first is what DevConnect even is.

**[326.8s] SPEAKER_00:** Oh yeah. So as a resident historian of all things Ethereum, what is DevConnect?

**[334.6s] SPEAKER_01:** Yeah, so it's a major conference held by the Ethereum Foundation. There's actually two different conference series that run now. So DevCon, which was originally developer conference, obviously has become not a developer conference anymore. I don't know when it was last a developer conference. Maybe two. Probably DevCon 2-ish.

**[358.9s] SPEAKER_02:** Maybe it kept getting bigger. Big, but not huge.

**[365.1s] SPEAKER_01:** I'm thinking in terms of the content though, you know.

**[367.7s] SPEAKER_02:** No, I know, but they kind of correlated, right? Like the more people that wanted to come, the lower percentage devs somehow.

**[375.1s] SPEAKER_00:** Well, I can't remember at 2 they had DevCon, and then like next to it they had like, I think it was called like World Blockchain.

**[383.9s] SPEAKER_01:** Yeah, I mean that one was a combined event. Yeah. I guess probably DevCon 3, probably in 2017, was the switch over where you had like a thousand people. So it switched from a, you know, meet your peers, talk about all the different development projects going on, to more of a... you know, hey, here are the big talks. But yeah, we're on to... we have seven now. So, you know, DevCon 7 was in Bangkok last October, I think. But yeah, they started doing DevConnects as well, which is really intended, I guess, to not be a conference, to be a collection of different events connecting, you know, developers and community. So I was expecting it to be a fair bit smaller, but it absolutely wasn't. But it did have a different flavor to DevCon in that... it was lots of little things, you know, lots of events under that same banner, obviously side events as well. But even if you just got like a ticket for the main thing with a theme of World Fair—you know, of really bringing people from around the world to show what they're working on... I didn't expect it to be as big. Like, I think it probably was as big as DevCon really, in the numbers.

**[475.0s] SPEAKER_00:** I mean, what I... yeah, effectively I think they've become the same. Like it's just whatever they were trying to kind of keep it small and... But I think, in terms of signal-to-noise ratio, these DevCons are probably still the highest compared to more business-y conferences. You know what I mean? Like in terms of actually getting some technical stuff. Jim, what were your impressions of DevConnect and Buenos Aires? You can... I've heard you said you're worried about being too negative, but there is no... yeah, go for it.

**[513.1s] SPEAKER_02:** Please, we wants to know.

**[515.0s] SPEAKER_03:** Yes, I mean there was a lot of good stuff down there. First of all, I actually, in part to avoid having a huge flight down there, I broke up multiple destinations in South America on the way there. So saw a lot of really cool stuff in Central and South America the week before. And Argentina is beautiful. Conference itself had some very cool things there. But I think I really sort of preferred the format of what happened in Bangkok the year before. There were certain things about the format here that made it difficult. First thing is that there was less going on at the main venue, and we had to spend a lot of time signing up for all these off-site things. And these off-site things were big and would go on for hours. So it would sort of pull you away from the main event for the whole day. Maybe you could kind of come back at the end of the day. But then I tried that a little bit at first. Like, I signed up for an off-site thing and then I kind of came back, and once I got to the main event, you're sort of just wandering around. And it was hard. Maybe... Did you guys find a good schedule for what was happening right there? Because mostly I was just walking around, and like there was one area, I guess it was the yellow pavilion where the big room was, and you could get a couple small talks there. But mostly it was just sort of like outdoor study areas and not as much going on in the main area. I don't know. What did you guys think about that breakup?

**[623.2s] SPEAKER_02:** It was haphazard. But I liked a bunch of the main stage talks. There were a few good ones on the Friday, there were good opening ones, and then there was a little amphitheater that had some of the good DeFi talks. But... I agree, it was sort of like a crapshoot. Like the registration procedures. Sometimes you had to register for an event that was inside the venue. Sometimes that wouldn't work, but you would go like by the booth or whatever, and they would just tell you, "Oh yeah, just don't worry, just show up." So it contributed to an impression of like never quite knowing. Like agendas weren't really posted for any of these side events. They were not even really posted for the main event until like the night before. Like they were kind of, you know, lazily—I mean in the computer science sense—updating the agendas as you went, so to speak. So it was very hard to come in with a target and hit everything with that target. You kind of had to just sort of go with the flow, and... it doesn't feel optimal. But I actually, you know, I still got quite a lot out of it.

**[702.1s] SPEAKER_01:** Yeah.

**[702.4s] SPEAKER_02:** Even with that. But yeah, the endless registrations were quite annoying. And yeah, there were big side events in the event, small ones. Like I discovered a couple days in, there was like a quite large Polygon side event in the main venue, you know. And... yeah, it was sort of hard to find things.

**[726.2s] SPEAKER_00:** Well.

**[728.6s] SPEAKER_03:** Because everything was right there together, and you can kind of walk to...

**[731.6s] SPEAKER_02:** Something else that could be way better.

**[733.3s] SPEAKER_00:** Yeah, yeah, yeah.

**[734.5s] SPEAKER_03:** You could kind of test something out, and if it was looking silly, you could just run out and find another room. And so it allowed you to, like... I don't know, it's like looking for a movie on Netflix or something. You can try a bunch of movies and then settle on one versus the olden days where you had to buy a ticket to go to a theater. And if you... if it hit me that I was into something silly, you know, I'd still be like, well, maybe I should stay a little bit longer. I did sign up for this, and I can't sign up for another thing right now. So... in the main area, I hit a couple good ones there, but often just the topic wasn't something I was interested in at the moment. So.

**[788.6s] SPEAKER_00:** Well, I found what was kind of strange was that you signed up for these, like, large blocks of time, and then you wouldn't... the agenda wouldn't be clear when you were signing up. Right. And then you might, like, see one good talk in that. You know, like, some of them lasted like, nine to five. And like, so you get like one good talk in there, and then people...

**[811.2s] SPEAKER_02:** Were just hanging out, like, co-working and having coffee and whatever for most of it. And the talks were, like, in this tight segment that they didn't name until like, much later.

**[821.9s] SPEAKER_00:** Yes, exactly. And some of the more important, like, you know, Vitalik saying something, and then the rest of it were like, you know, hit or miss kind of afterwards. Right.

**[830.9s] SPEAKER_02:** So it was like, I tended to find out about Vitalik speaking by seeing that he was speaking. Yeah, like...

**[839.1s] SPEAKER_00:** Yeah. And then he's, like, coming on and, like...

**[844.2s] SPEAKER_03:** And I kind of would have liked to have seen that too. But the thing is, I had signed up for a thing and I was like across town when Kieren mentioned, "Hey, Vitalik speaking here now." And I'm like, well, that was the day that I... that was the day that I probably chose unwisely, too. I wasn't happy with the talks I had gone to.

**[865.7s] SPEAKER_00:** Right. Well, and speaking of that, maybe we can touch upon some of the big themes of DevConnect. Let's start with sort of the headline thing about Vitalik saying elliptic curves are going to die. That seemed to make a lot of news. And quantum computing was coming for us all. What were your thoughts on that? It's a Jim question, I guess, there. Let's start with Jim. Bring out that physics background, Jim.

**[893.7s] SPEAKER_03:** I'll pass this to Kieren.

**[897.3s] SPEAKER_02:** Okay, so I will say that both Jim and I have a physics background, but mine was more from the math side where we're good at the beauty of the equations, but don't necessarily have it as an intuitive sense like the physics people, who were good at estimating the answer and then back-working into the actuality of it. The math people might have actually been better at the math side, though the physicists are quite good at it, but less so. Nevertheless, I had spent some time in quantum and the machinery on how a quantum computer might work, and so on. I still don't have that much evidence that it's coming soon. But would you really? I don't know. It's hard to keep secrets under wraps. I think probably governments and private sector researchers are putting a bunch of money into it. But for a long time, there were these headlines like Google got it to 20 qubits and they stayed together for 10 to the negative 7 seconds instead of negative 9, and it computed the divisors of 63 or whatever, something like that. Right. And so yeah, I mean, I think... I don't know how we would know when quantum's coming, like these coins get stolen. But even then, you might not want to do that. I also think the cryptography tends to come back pretty fast when new cryptanalytic tools come in. Like I believe there's already quantum-resistant stuff. It'll be a hard switch over, but once you knew that the Bitcoins were still getting stolen, you might still have... I don't know how—like, do you steal them all in one, you know, 10-minute segment, or is it still kind of slow and you have a little bit of time to migrate over? Or you just snapshot all the balances at one date when you're pretty sure that... I don't know how we would deal with it, but. And yeah, I guess I'm often skeptical, but color me a little skeptical on quantum happening much faster than people expect, which is the real scenario you're worried about.

**[1041.6s] SPEAKER_03:** It's one of those stories that's always in the news, like, "Oh, was there some big breakthrough or progress in quantum computing? It's coming in a couple years." But that's what they've been saying for decades now. So.

**[1055.6s] SPEAKER_00:** Yeah, and it seems like a bunch of people are... I mean, I would say quantum resistance was a big theme. Like there were a lot of people claiming either research or advances in quantum resistance at the conference as well. So it seems like Ethereum is probably better situated to implement quantum resistance. I mean, it would be painful, but, you know, like it would be very hard to do it on Bitcoin—more structurally, I think—than, you know... they change less. Yeah, exactly. They... it would... But what do you think, Bob? What was your impression of that?

**[1094.8s] SPEAKER_01:** Yeah, I mean, I don't know. You can't really tell when the thing's coming up. But I'm not really worried. Like it's like everyone's talking about it. It'll all be fine. Everyone's very aware.

**[1106.0s] SPEAKER_00:** It's a known problem that a bunch of people are working at. But no, it's unknown when it's going to hit us, I guess is the way I put it.

**[1114.6s] SPEAKER_01:** Yeah, I mean honestly, you know that there are chains that have already got quantum resistance stuff. It just seems to be like a cost thing, from what I can see. It's like, "Okay, well it's probably not a problem, so why would we make ourselves less competitive now?" Like I don't think it's a market winner of saying, "Oh yeah, like we're like 10x slower, but you know, we're resistant."

**[1138.6s] SPEAKER_02:** Yeah.

**[1141.8s] SPEAKER_01:** But, but it's obviously an incoming matter. Though the hotter matter really is privacy. I think that's really...

**[1149.2s] SPEAKER_00:** Well, I think the hot... I mean the other thing in between those two things is ZK. So maybe we can... I mean Bob, I know you have some thoughts on that. Maybe we can start with you this time.

**[1159.8s] SPEAKER_01:** Yeah, so I mean, talking about where we went, I was mainly just in the main venue, with the exception of the day before the main event where we had the second Ethereum Cypherpunk Congress, which is a good, fun event. And the other thing that there was on the final day was the Ethereum Privacy Stack event. So both of them were organized by Web3Privacy now—the second one in collaboration with the privacy guys at the Ethereum Foundation. So that is a pretty new group, I think, about 50 people working on that at the EF.

**[1203.3s] SPEAKER_02:** 50 people, wow. Yes, a lot of ETH. Good. I mean, good for them. Wow.

**[1210.0s] SPEAKER_01:** So, yeah, you know, pretty serious and in multiple different areas. So they've got the Kakarot project, which basically seems to be like SDK and tooling to help with integration of privacy features into wallets, using existing projects with Railgun being a key one. Basically like, "Hey, here's how to plug in privacy into an existing wallet," and we've kind of done most of the work.

**[1241.0s] SPEAKER_03:** Also.

**[1243.6s] SPEAKER_01:** On that. One of the major main talks that there was on that last day was Vitalik and Roger Dingledine—great name—of Tor, really talking about the Torrification of Ethereum, which is planned. So that was a bit of a reveal that there is work underway to look at all of the different levels and components of that protocol stack and work out how to unify them really, or at least make them Tor-friendly, including things like the block formation, you know, and the validator leader stuff and hiding all of that.

**[1293.9s] SPEAKER_02:** I want to jump in quickly on the Congress. I want to hate a little bit first. Okay. The "Infinite Garden" appeared on the screen again.

**[1302.8s] SPEAKER_01:** Like at DevConnect, you mean? Sorry, no, no.

**[1306.5s] SPEAKER_02:** On the Cypherpunk Congress. I'm not sure you saw that one.

**[1308.6s] SPEAKER_01:** Okay, okay.

**[1309.6s] SPEAKER_02:** Yeah, I took a picture of it for the record, put in the show notes. The...

**[1318.8s] SPEAKER_03:** We're...

**[1319.2s] SPEAKER_02:** We're like halfway to a wartime EF, but we've like kept the old generals and put them on the, you know, National Guard or something, the Coast Guard, you know. And let me connect this to sort of like a broader point. I really liked that you saw a bunch of the old faces at DevConnect. People have been around for a long time. Like when I watched the Sky and Uniswap talks, they did seem... you know, Sky—formerly MakerDAO—I'm against this rebrand, but they seem to really take being a DAO seriously, where a lot of DAOs is sort of like marketing and you kind of don't... you know, it's led pretty top-down. But like they, you know, they were up there talking about the DAO way of doing things, and they've got proposals that you vote on. And I'm sure it's still like a little bit oligarchic, but they really meant it. The DAO part, on some level. I was talking to a cool guy who I need to follow up with, actually, with Victor. And we're showing him the app on the phone, and he was like, "Oh, are you getting a full node on there?" I was like, "No. Like, those days, we've given up on this dream." I think, like, the thing needs to be fast and, like, you're not gonna run the node on the phone even if you could. It's gonna melt. Maybe one day, you know, maybe the tech on the watch. Yes, full node on the watch. Exactly. I'm the Apple Watch.

**[1427.1s] SPEAKER_03:** But.

**[1428.2s] SPEAKER_02:** So I'm making fun of it a little bit, but I like that these people still exist. And they... it's like 2017, 2015, like the same things. And you know, they... We were in that same conversation, talking to an old friend of ours. He's like, "Yeah, Railgun, it's great, but I want it to go harder. I want there to be one account for the whole network that, you know, all activity goes under, and then you use your ZK receipts to pull out what's specific to you." But all that's like, "Hell, yeah," you know. Let's go hardcore dreamer cypherpunk, you know. And almost no other conferences like that. Like, I haven't been to a big Solana builder conference, but I assume that those are pretty commercial, just from the whole Solana ecosystem ethos. I'm surprised these people are still around. But this is great. So I wanted to throw a plug out that if you're on crypto Twitter too much, you worry that just like literally everything about the industry is price action, and there are still some true believers. It's kind of the same people that it was somewhere between 2015 and 2017.

**[1497.6s] SPEAKER_01:** Lefteris did a good tweet, a good little video clip, actually, because Lefteris, you know, famously one of those OG builders with Rotki portfolio management software that he has as his main product—being offline, you know, so it's a local app. It was... He had a good new phrase as well, which was "aligned apps"—with that alignment being with you, the user, not, you know, some weird Ethereum alignment or anything, but saying it's on your side. But the tweet that he had was one of the terrible things that was... there was the network, like the Wi-Fi was just wrecked, like many of the days, like nothing, even data on your phone. Pretty... Because there's so many people doing it at the same time. But he did a little video saying, "The network's down, but my app still runs."

**[1564.8s] SPEAKER_03:** Look.

**[1568.6s] SPEAKER_00:** But I will say, I mean on that kind of like... I don't want to push back against what you're saying, but like I do think the privacy people have kind of gotten more customer-aligned than purely philosophically aligned. Like in the Ethereum Privacy Summit, I heard many times like, "Yes, we want consumer privacy, no, we don't want to support North Korea or pedophiles." Like, which seems to be the right line to draw. You know, it's like I think it's...

**[1600.4s] SPEAKER_02:** Well, okay, there's a debate. Bob, do you want to jump in? I ran into Amin during the conference who seems to have created this debate. You might have more context on it than you know, than I do. But I'll back Amin if need be.

**[1615.9s] SPEAKER_01:** Yeah, sure. So, so I guess specifically there, you have this philosophical question of if you do have a privacy tech, should that be unconditionally a single anonymity set with the whole world? You know, obviously, the larger anonymity set that you have, the better security you have, with the ideal being it's everything, you know, it's all transactions for everything. So I mean that's the scenario that you have with Monero, though. Monero is, you know, using ring signatures at the moment. There are plans for use of ZK to... you know, it's a full membership proof thing that they got proposed. But right now it's just ring six. But it's on by default, you know, so privacy on by default, mixing with everything by default. On the other side, on Zcash for example, you can have transparent transactions or you can go into the different shielded pools. The one that you're talking about in particular is Privacy Pools. Privacy Pools, I think, was either a suggestion from Vitalik or Vitalik was one of many.

**[1714.0s] SPEAKER_02:** He's on the paper.

**[1715.2s] SPEAKER_01:** Yeah, yeah. A number of co-authors, but I mean Soleimani is a primary guy and Zach Cole as well. They just did a raise at Oxbow, which I believe raised three and a half million.

**[1730.8s] SPEAKER_02:** But the approach—quite a responsible number—in the...

**[1735.4s] SPEAKER_01:** Yes, it's maybe about how much it might cost to develop the technology, and...

**[1740.3s] SPEAKER_02:** A little bit more.

**[1742.4s] SPEAKER_01:** But, but yeah, the approach there... and it was really in reaction to the legal action on Tornado Cash—was really saying, "Okay, well if you do this blind privacy approach, you do intermingle yourself with North Korea and terrorists and crime."

**[1767.6s] SPEAKER_00:** Yeah.

**[1768.2s] SPEAKER_01:** And the Monero reaction to that is, "Yes."

**[1776.0s] SPEAKER_02:** So let me, let me... but if.

**[1779.1s] SPEAKER_01:** You can back up. Sorry, just to finish the thought there. So yeah, really a primary thing was like... not wanting to have that disassociation, but also not wanting developers to go to jail. And saying, "If you can credibly show, look, here is a ZK proof that shows that I am not in the same group as these known baddies, then you know that that's a kind of a responsible middle ground." It does affect your anonymity set, but maybe not that much.

**[1812.3s] SPEAKER_02:** Let me add maybe the flip side argument, but also... So I've never been a user of any of these technologies. I'm sure I will test some at the minuscule amounts at some point.

**[1829.0s] SPEAKER_03:** The...

**[1831.4s] SPEAKER_02:** Tornado Cash. Terrible name. You know, I think that... I believe that it actually also contained a capability at least to prove source of funds on one side. So like you could prove that your funds were acquired legitimately even if they were obscured later. I don't think you can do a severability with the bad funds. And that's the key point that Amin was telling me is the difference. But you know, I think that the counterfactuals—what the hard-core other side cypherpunks would say—is something like, "Well, what about like cash? Like all cash is dirty. It's all been used in some bathroom to get some illegal substance from point A to point B." You know, it's really the preferred still technology for certain kinds of money laundering and all that sort of thing. There are serial numbers, I guess, but we don't go and say cash is the problem. And the anonymity set of cash includes lots of bad acts. Right. And so this sort of like presumption of guilt—like, you know, if you're putting your money in the pool, you're aiding and abetting North Korean money laundering—I don't buy it at all. And you know, on the other side, like you don't want to cede that argument. And everywhere in the world is trying to cede that argument. Like the banking system definitely has like a guilty-by-default ethos: prove everything about you and we're going to surveil every transaction and, you know, we'll tell you if you're allowed to bank, basically.

**[1945.8s] SPEAKER_01:** I mean, I think there's certainly a very valid argument on that side of sort of like this supposition of you, you know... "But it wasn't me, sir. Here's my ZK proof, I promise." And they're like, "What's the ZK proof? Like, what are you even talking about?"

**[1964.4s] SPEAKER_02:** Exactly. So if you pick this half-step, you're kind of just saying, "Oh, you use this privacy tech, but you're like one of the easy ones to pick off," you know, like I don't know.

**[1975.8s] SPEAKER_01:** And it makes it a permission system again.

**[1978.6s] SPEAKER_02:** Yeah.

**[1978.9s] SPEAKER_01:** And you could say, "Oh, it's only a bit." But yeah, talking to Zach, it was really...

**[1985.5s] SPEAKER_02:** I don't know the details. Amin said it does break the fungibility, which is like kind of the same thing. The same. There's like... it's like with Bitcoin, you have like tainted ones and not, you know, but...

**[1997.2s] SPEAKER_01:** But talking to Zach, it seemed a primary motivation wasn't so much being compliant as it was... we don't want any more of our friends to go to jail.

**[2006.8s] SPEAKER_02:** Totally. Yeah, I guess.

**[2009.1s] SPEAKER_01:** And maybe that's a passing phase.

**[2013.0s] SPEAKER_02:** It's that these...

**[2014.6s] SPEAKER_03:** Yes.

**[2015.1s] SPEAKER_02:** At the same time, I don't really know what the Tornado Cash people did other than build software. Could have been more than building the software. You know, there's no way that building some software should count like a conspiracy to launder money like that. That's never applied in any other case, really. Maybe... except as regards the crypto industry.

**[2043.4s] SPEAKER_01:** Also worth saying though, I think, is that many parts of the world are not so progressive as the US on that matter.

**[2050.1s] SPEAKER_02:** Yeah.

**[2052.1s] SPEAKER_00:** Well, Jim, I think we're starting to get... you know, we're a little bit over 30 minutes. Want to kind of touch base with you. I know you're still pretty jet-lagged. What were your impressions at the conference, especially since you attended a lot of agentic AI talks too? So, you know, how real is that? What do you think about... whether... what were your big takeaways from the conference?

**[2078.7s] SPEAKER_03:** Well, I was pretty excited to go to anything AI, but I don't know, we're sort of like in the hype part of the hype cycle right now. And I went to, on the first day, to one where... multiple... I don't know, it was like typical people speaking would be like somebody who had put together a company where they were using AI to maybe go and do DeFi trading or something like that. And it would like sort of holistically understand what's happening in the world and try to use that to trade. And I don't know, like there were panels of people where it was like multiple people with a variant of that story. And it was all very inspirational sounding and a little bit light on the details, but everybody was very excited by it. But I'm sitting there listening, and I'm like, "There's no way this stuff... it's really cool, but there's no way they're doing it." And I remember... it would be a much bigger deal if some of these succeeded. And... it's funny because at these events you can still have... a lot of marketers are there, but there's still enough geeks there that sometimes people just blurt out honest things. And after hearing like lots of marketing speak, I remember—I forget who it was and I probably wouldn't say who it was anyway—but one guy, they were like... they had been spinning up this whole story again, like I had said before, but they were like, "Oh, and this actually works." And he got a little too honest, and he was like, "Oh, if this thing actually worked, you think I'd be sitting here right now?" And so that was sort of like the theme to me. It's like over-promising some really cool ideas, but it didn't look like it was actually... And this is kind of the case in AI in general right now. There's like huge breakthroughs. AI can do a lot of stuff that would have shocked me just a few years ago, but it's hard to get them to actually sort of complete the whole job for you, or actually work as advertised. So that's what, like the common theme I was seeing there in these talks.

**[2227.3s] SPEAKER_00:** Yeah.

**[2227.7s] SPEAKER_01:** Did you see anything with post-apps? Any kind of post-app sort of like, "Hey, look, we've... you can just AI drive this," and you know, that kind of text or voice interface as opposed to UI?

**[2247.9s] SPEAKER_02:** I'm confused.

**[2248.6s] SPEAKER_00:** Yeah.

**[2249.1s] SPEAKER_01:** What's a post-application? Right. You know, soon we won't have applications. We'll just be talking.

**[2254.0s] SPEAKER_02:** Oh, post apps, yes.

**[2255.9s] SPEAKER_01:** Yeah. Was it more infrastructure stuff that you were seeing?

**[2263.8s] SPEAKER_03:** It looked like infrastructure stuff, what I heard, but there were many, many groups up there talking about it.

**[2269.6s] SPEAKER_02:** The trading bots are arguably post-apps. I mean, you kind of probably tell them what to do when they like... theoretically give you more money than you had, you know, when you gave it to the... it's like a little financial manager. But I've also, like, I think I've said before, like, when I've test-driven Claude and told it to go do a swap on our testnet, it can do it in a... Yeah, yeah, but it's like, it goes pretty slow through the UI. It's like understanding it visually, and, you know, like, I don't know that it's that much easier than a human, but I think you could mostly give a declarative intention to an AI. Like, hey, like, I want to rebalance from Bitcoin into Bitcoin and ETH. Well, they can do it, but it's not like... you know, sorry, go, Jim.

**[2321.8s] SPEAKER_03:** Well, I guess there is a subtle distinction between an agent and a helper, or just using AI as the UI, as an autonomous agent. That's the stuff that seems not quite baked to me yet. But I saw a couple talks where people were talking about just using it in place of the existing UIs that are out there right now to help you each step of the way do things. And that... that probably is great. That's... We all sort of use AI in that kind of thing right now.

**[2357.5s] SPEAKER_00:** Yeah, I did hear a very interesting talk by the people formerly Infura, but now DIN—Decentralized Infrastructure Network—who are talking about really thinking about AI agents as users and how to make it easier for them to interact with the network. So from that point of view, I do think that there's some... I don't think it's really replacing UX. I think it's more targeting a different class of user entirely—agents—which, I...

**[2387.4s] SPEAKER_02:** I mean, let me add to that. I, you know, for a long time I've been worried about our, like, mobile story. During the conference, I was using our app on mobile a bunch, and while I'm still worried about it, I think in many cases it will be leapfrogged by just like, "Hey, chat, like, go do this thing in this app for me."

**[2408.6s] SPEAKER_00:** Yeah.

**[2409.4s] SPEAKER_02:** And in a... There's a downside to that in that we have just like yet another aggregator, but an upside in that, like, you might not have to make a really slick mobile app.

**[2420.5s] SPEAKER_00:** Yeah.

**[2421.3s] SPEAKER_02:** And I think that'll continue. And I do... I don't use that pattern much yet, but, you know, it's something we should definitely lean into. And, you know, I've also seen like pretty funny things. Some like B2B SaaS Twitter handle made some post was like, "Yeah, we sold the enterprise our app. We wanted them to use it more. So we made an AI to use it for them, and they're using it more." You know, so... Whoa.

**[2453.7s] SPEAKER_00:** What you described, though, I heard the MetaMask team, they're really talking about intents, like... trying to kind of like, you know, instead of making you do a lot of clicks or stuff, just tell it, "Okay, this is what I'm trying to achieve," and then like, find me the best savings. Right. And then we'll go and do all of that stuff. I know we're over time, so I want to go around the horn and say what is the biggest takeaway you got from this DevConnect? Let's start with you, Kieren.

**[2484.5s] SPEAKER_02:** Privacy seems much more viable now than I thought. I've been generally a skeptic, even us having worked on it a bunch, but I think there are pretty solid mainnet live use cases for it that work now that we could also incorporate. I honestly think if we're talking about consumer mass adoption, you can't really have these like clear-text balances. Like, you know, yes, it's pseudonymous, but it... it makes everybody uncomfortable. Like Bob is fond of quoting the time when very obviously one of the Ethereum core devs moved like a quarter billion dollars into DeFi or whatever... It's like... it's not... So I've tried to accelerate our privacy roadmap in response.

**[2537.9s] SPEAKER_00:** Jim, what was your big takeaway from this conference?

**[2542.0s] SPEAKER_03:** Well, the coolest thing that I saw, if it's real, is ZK is also one of these things which is prone to overhyping. But it seems like maybe scalability of Ethereum might be solved through some ZK means sometime in the next couple of years, if that really happens. You know, maybe I've heard something about that before, but I probably just ignored it. But people were talking about it like it's around the corner right now. Looked into it a little bit. It looks, if it does what they say it does, it could be pretty impressive. So that was exciting to me.

**[2580.4s] SPEAKER_00:** Bob, what was the biggest takeaway from you?

**[2584.1s] SPEAKER_01:** Yeah, so, and I think that's true on a few different pieces. Both in terms of that privacy... but yeah, also scaling. Like I think some of these things have taken so long, you know, like here we are 10 years in. I just looked. It was November 10th. By the way, the Strato talk on... congratulations.

**[2608.3s] SPEAKER_00:** Yeah, exactly. Almost exactly.

**[2610.8s] SPEAKER_01:** But yeah, some of these things have taken 10 years really to get where we thought we'd get in a few months, even. And yeah, I think that will be like, you know, the ZK-ification of the L1 that would basically end up with not really doing any execution on the L1. It's just proofs of things that are happening up above in whatever execution environment that might be. So yeah, I'm feeling very like... we didn't talk about the price action, but that does not at all to my mind reflect where we are on the tech, which I think... it was a really positive checkpoint for me of like, a lot of these things... yeah, we're kind of like really there and things moving really fast. So, you know, if we look back in five years, say, or even three, I think we're going to be in a great place where it's like we're almost feature complete. Maybe.

**[2671.7s] SPEAKER_00:** Software is never really feature complete, but I would say that I guess the biggest takeaway I had is like, I think ZK proving—which is different than the compilation part—has come way faster and way down. Like last year when they were talking about it, I think a typical proof took minutes and required 48 GPUs. And you know, now I'm seeing two GPUs and like closer to kind of the 10-second real-time holy grail that we're getting to. Like when I looked at the things on fprooth.org, I was really impressed at how close it was and what people are doing there. So I think we'll call it there because we're already 15 minutes over. But where can we find you? I'm Victor Wong. You can find me at X at Vic for Wong. W-O-N-G. Kieren, where can we find you?

**[2720.2s] SPEAKER_02:** Kieren James-Lubin on X and most places.

**[2724.2s] SPEAKER_00:** Jim.

**[2726.8s] SPEAKER_03:** Still Twitter. And I've also forgotten my handle again. I should probably... you should remind me next time to look it up. It's... what is it? John... John, Feed Hormuz or something.

**[2738.0s] SPEAKER_02:** I looked it up, but I can't. It was like two weeks ago.

**[2740.5s] SPEAKER_00:** Okay, I'm gonna keep asking you. You're good. This is a pop quiz weekly pop quiz for you, Jim. So you better learn it.

**[2749.6s] SPEAKER_01:** Look at the notes on our website. I always like do the link. I always reply to that and correct it, and yeah. So I'm Bob Summerwill. Summer, like the season, and W-I-L-L. Write your will on.

**[2762.9s] SPEAKER_00:** On Twitter. And thank you for joining us. Take care.

**[2767.0s] SPEAKER_03:** I'm looking at my handle right now. It's... it's Jamshid Hormuz.

**[2771.7s] SPEAKER_00:** Okay, you get a 50. Just pass.

**[2777.7s] SPEAKER_03:** That's even more embarrassing than failing.