```
**[00:00] SPEAKER_03:** All right, well, welcome back, everybody. The first episode of the Early Days of Ethereum actually got quite good critical reception on LinkedIn and Twitter. I have a total of nine YouTube subscribers now, which I think is not so bad for a first video. And there have been a few people who reached out who we've known a long time who really appreciated the content. One of them called it, you know, essential viewing. So anyway, we're back for another episode. So, to remind everybody, I'm Kieren James-Lubin, CEO of BlockApps, here with my co-founders. Victor, do you want to introduce yourself quickly?

**[00:34] SPEAKER_00:** Oh, okay. I'm Victor Wong, co-founder and Chief Product Officer of BlockApps.

**[00:39] SPEAKER_01:** I'm James from OSD Hour—Jim, CTO and co-founder of BlockApps.

**[00:45] SPEAKER_03:** All right, thank you. So I believe where we left off—so I can't watch video of myself, so I forget exactly how we ended the last episode—but I believe we pretty much ended with the Ethereum launch. And there were some things we left out even prior to launch that we can kind of backtrack to a little bit and then go forward to all of the kind of after-launch activity. So with that said, maybe I'll hand it to Victor to talk about the first ConsenSys Dappathon, which was June 2015, I believe.

**[01:12] SPEAKER_00:** Yeah, so that was, I think, the first actual hackathon building, you know, what in those days were known as dapps. I guess some people still call them that, but that seems to have gone out of favor in favor of "blockchain applications." So the first idea was to really try to build blockchain applications directly on Ethereum, and that was in the first ConsenSys office, which was like a very small co-working space in Greenpoint, I think. I would say it was on Water Street.

**[01:39] SPEAKER_01:** Yeah, it was called Green Desk, maybe?

**[01:41] SPEAKER_00:** Green Desk, yeah, that's right. It's right next to the modern-day Domino Park, maybe a block away from there or so.

**[01:48] SPEAKER_01:** Exactly, yeah, that's right. And of course, Domino Park did not exist at that time. In fact, Domino Park went up really quickly and took me by surprise. I looked up one day and there was a big, kind of well-manicured park there.

**[01:59] SPEAKER_00:** Yeah, well, they kind of walled it off, and so it just was like—I don't know, I thought it was like an abandoned site. And then one day, all of a sudden, the wall was gone and there was a beautiful park there. So at that event, which was, I think, two to three months before the actual launch of Ethereum, I will say the concepts were really interesting. People were coming up, and it was mostly, I think, interns that were interning at ConsenSys over that summer. And ConsenSys at this point was only like maybe 20 people at max.

**[02:28] SPEAKER_01:** 20 or 30, yeah.

**[02:29] SPEAKER_00:** That's interesting. It was really, really small. And you know, some great concepts came up, but even with the stuff we built, we realized pretty quickly that no one could build anything in a short period of time. Like, it was just impossible. Very basic stuff like reading a variable off the blockchain was kind of impossible. Like, you couldn't read the state off the blockchain and all this kind of stuff. So that kind of led into—yeah, like everything building in those days was incredibly hard. And that led into—so we decided at that event we were going to, at the launch of Ethereum, do a bigger hackathon. And that became the second ConsenSys Dappathon, which coincided with the launch of Ethereum. And it was us, the Java client, which I think was called Ether.Camp at that time, and other tools that were kind of combined together. But what was really interesting about that one was it was bigger. I think the first one we had like six participants. The other one we had like, I think, close to 30. And it introduced a lot of ideas that would become more developed pretty quickly. Like, the winner was a GameFi app. It really had that element of tokenized gameplay. There was a decentralized social app, I think called Truther or something like that. And then there was a traceability supply chain app in those early days. And that kind of all coincided with the launch of Ethereum.

**[03:42] SPEAKER_03:** Yeah, so okay, you're talking about the second one?

**[03:45] SPEAKER_00:** I'm talking about the second one, yeah.

**[03:46] SPEAKER_03:** The second one, also the offices had shifted. So we had—our ConsenSys, which we were kind of working as a part of at that time—had moved to a much larger office in Bushwick, which is, I believe they still have a presence there, though they've gone mostly remote. I remember there was like a horse lineage app.

**[04:03] SPEAKER_01:** Yeah, yeah, interesting.

**[04:04] SPEAKER_03:** And we ended up actually hiring a couple people who participated in the hackathon. But that one was open to externals, right? So that was the big difference. And it actually was quite well attended. The room, I think, never had the greatest air conditioning, but it was really quite hot in there, if I recall. Do you think that one was like 24 hours or it was two days? I can't remember.

**[04:24] SPEAKER_00:** I think it was two days. And yeah, like the air conditioning thing—so we moved into that space to have the hackathon. ConsenSys was planning because they had outgrown that co-working space already. And so we moved into that space, which was a reasonably sized room. You could probably get 80 to 100 people in that room. But yes, the air conditioning was terrible. And we had to frantically—we only realized this after we got into the room—so we had to frantically buy some and set them up.

**[04:52] SPEAKER_03:** Okay, I do have a memory of that.

**[04:54] SPEAKER_00:** Yeah, I don't know if you recall that. But yeah, we were trying to get those air conditioning units in place before a ton of people showed up. Because yeah, we were sweating when there were only like five people in the room.

**[05:04] SPEAKER_03:** These were the scrappy days in manually configuring air conditioning. I think the amount of furniture assembly that you do is a good proxy for how scrappy you are in your startup journey.

**[05:14] SPEAKER_00:** There was a lot of furniture. It was basically an empty room when we moved in there. And I think we moved in there a day or two before the hackathon actually started. So we had to get everything up and running. And it was to sort of commemorate the launch, I think. Or was it like right before the launch?

**[05:30] SPEAKER_03:** It was right—actually, you know, if you recall at the time, we didn't know when the launch would be. The dates were always shifting, right? And we just said—we kind of arbitrarily chose—we wanted to actually synchronize it with the launch. But because we couldn't know exactly when the launch was, and even when they declared the date, it was still a little bit vague, like exactly what actually happened. So we at some point had to arbitrarily choose the date. And they more or less—it was the right date. I think it was off by maybe a day or two.

**[05:57] SPEAKER_03:** Jim, I might have asked you this last episode, but I'll ask again. Do you remember, one, trying to predict the launch and could you explain how? And two, there was some complicated mechanism for how the launch would actually happen because it's hard for a decentralized group to decide on a launch time. I can't remember that at all.

**[06:13] SPEAKER_01:** You were mentioning it in the last video and I didn't remember this, but I don't doubt it. It sounds correct. You were saying we were looking through the Git commits at the time.

**[06:21] SPEAKER_03:** We were, yes. You made this plot. It was like commits by day, and you extrapolated it forward. I think it probably got within a couple of days of the launch date. Okay, so I still don't know how they set the clock on the first block, so to speak. Maybe we can dig this up. There was something they did, and we had probably in our DMs—I wish I thought to look between the first and second video to find the actual discussion that we had. Maybe the graph is in there. That's very funny. The Slack is the treasure trove of interesting things. All right, so yeah, so it launched. And I kind of felt like there was a sort of "and then what" going on. You know, it took a little time for things to get going. And then, you know, obviously it's been a smashing success, right? It's just sort of the reality of a new platform. You sort of get it out there, you see what people do, you learn from it. And it took a minute for the activity to kick in.
```