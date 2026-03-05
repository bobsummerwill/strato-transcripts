**[00:02] SPEAKER_01:**
Test. Hello, can you hear me? Hello, hello. We're good, we're both good. Yeah. So hello, I'm Bob Summerwill here with Early Days of Ethereum, and talking to Martin Becze. Hello. Was it Becze? We say, busy, busy, busy, you know. Becze, but that works, okay. So yeah, thanks for talking to us. You are a very OG. You're more OG than I am, by a couple of years maybe even. So I mean, what were you doing prior to Ethereum that led you to it?

**[00:54] SPEAKER_00:**
Ethereum, yeah, that's a good question. So prior to Ethereum, I had gotten into Bitcoin for a bit. So I was actually at Occupy Wall Street, and I set up the Bitcoin donation address for OWS, and started doing some development. Just regular, like, Web 2 development. But as my projects developed, I started wondering how to decentralize them, as you naturally do if you've played around with crypto. And you know, I was highly influenced by Bitcoin and BitTorrent.

This is around the time Namecoin also came out. So I wanted to extend the concepts of Namecoin for my own project, which at the time was a geospatial map thing that displayed what was happening around you, and it was supposed to be federated. I wanted to have a DNS system that we could resolve a location to these servers, so I called it GeoDNS. And looking at how Namecoin implemented it, I was like, "Ah, this is going to be a pain. I'm going to have to fork it, rebuild everything, get people to mine it. This is a lot of work." And then, as you naturally do, you're like, "Well, this could just be generalized," right?

Yeah, so this is around the time that Vitalik had written some articles, I believe in Bitcoin Magazine, on DAOs and DACs. Yes, I was very interested in that too, and I was following that work. And then, yeah, I saw the white paper drop. As soon as I saw the white paper drop, I was like, "Yeah, that I need. That's what I need. That makes a lot of sense."

So then I started hacking on it because that was before any code, you know, I think was really operable, right? And I wanted to get my hands onto it. I think AlethZero was up, but it was really rough. It was up on GitHub. And you know, I was a JavaScript programmer, right? So I was like, "Well, I better implement this in JavaScript because that's what I know." And I really just wanted to get my hands on it and really understand how it worked, right?

**[03:41] SPEAKER_01:**
Right, right. So yeah, we were just looking at some first commit dates. So we saw that Joseph Chow had a first commit on Node Ethereum in February. And then we found March 2014 as probably the first commit on your side. So yeah, I mean, the white paper had come out in November of the previous year. But I was looking, you know, the C++ and Go clients started in very late December. But so yeah, a couple of months in, as you say, it's all going to be a bit rough.

And yeah, I mean, it wasn't until April that you had the yellow paper. That came a little later. I think maybe April-ish was when Geth and cpp-ethereum were maybe kind of working, talking to each other. Yes. Yeah, I'll have to find the date there. I did see maybe a tweet of when that was, and I think it was Charles sent a transaction to Gav, or the other way around. Was it GavCoin, maybe?

Well, here's an interesting one, that GavCoin came later. There was a meetup in London in October 2014 where both Gav and Jeff were basically doing, "Hey, here's the status of Ethereum and roadmap" kind of thing, you know, like an hour-long, big, thorough thing. But what they did at that was Gav had GavCoin, which was written in LLL. Yeah. And Jeff had JeffCoin, which was written in Mutan.

And they had an on-chain DEX. It was an on-chain order book, really clunky, you know, like, "Here, I'm offering three GavCoin for 10 JeffCoin," or what have you. But they demonstrated it there and did a transaction to put an offer into the order book, and then Jeff's pressing the button to mine a block, and the exchange happened. But so I mean, were there many people where you were living that were regularly having meetups and being involved?

**[06:09] SPEAKER_00:**
No, no, no, not at all. I was living in Indiana, so very rural. It was completely—I only connected online, right? And I remained that way for some time. And it wasn't till a few months later, I was trying to get a job at Ripple. Oh yes, Ripple also. So they had a, I don't remember what it was called, but they were working...

**[06:44] SPEAKER_01:**
On a VM? Yeah, I can't remember. Codius or something it was, maybe?

**[06:54] SPEAKER_00:**
Well, I was interested in that, and I had been working on implementing the Ethereum Virtual Machine in JavaScript. So they thought that was pretty cool, and they flew me out for an interview at their office. And that is when I met Vitalik. Because, right, not at Ripple, yes, he just happened to be in San Francisco at the same time. Right. And also Joseph Chow for the first time.

Do you know when that might have been? Unfortunately no, I'm really bad with dates, but it was definitely past March. Sometime in the summer. And then I met up with everyone proper, and Vitalik's like, "No, just come work on Ethereum, right." So yeah, that's what I did.

**[07:57] SPEAKER_01:**
So was that working for ethdev as a contractor? So, yes, I was working for ethdev as a contractor at that point. Right, right. And yeah, Vitalik notoriously also nearly worked for Ripple but could not get his work permit. So yeah, the world might have looked very, very different if Vitalik had joined Ripple as an intern back then rather than sort of like...

**[08:18] SPEAKER_00:**
They failed to get everyone. But if they had, Ripple also may have looked a lot different.

**[08:23] SPEAKER_01:**
Yeah. Well, some of my very earliest meetups I went to at the start of 2014, it was like, "Here's a demo of Ripple," because it really was a lot less of a tribal setup. Right? Like everyone was Bitcoiners because that's all there was, and then it's like, "Oh, there are these other things appearing, and oh yeah, it's a different form of consensus. Here's a different flavor." And I...

**[08:45] SPEAKER_00:**
Was actually interested in—there was an early version of Ripple made by this guy in Canada. Yeah.

**[08:53] SPEAKER_01:**
Ryan Fugger, yes. Yeah, who lives in Vancouver, same as me. Oh, nice. I've not met him ever, though. So I was...

**[09:01] SPEAKER_00:**
Interested in that version. Like, you were able—yeah, I'm not sure if I'm going to be able to actually recall—but it was like debt. You were able to open debt lines to various people, you know, and then debt would flow through the people. That's right, it would ripple through. Yeah, ripple through.

And this was pre-blockchain. It was built in like PHP. They had a demo in like PHP. I had signed up on it, I was playing around. I was like offering my services on it. Right, right. But yeah, then they ended up moving in a slightly different direction.

**[09:43] SPEAKER_01:**
Slightly different, yes. I think it was 2004, Ryan's work, yeah, around then. Very early, absolutely. Yeah, so when you were then working full-time on Ethereum, did you have many collaborators? Were...

**[09:58] SPEAKER_00:**
Many people working on the code together with you? So it was like me and Joseph Chow to start with. And then Joseph Chow eventually went off and he started working on BTC Relay. Yeah, I don't know, that's a very interesting project. Yeah, so he did that next.

But yeah, there was a bunch of people coming in and out. Kumavis... yes, Aaron Davis, right? Yeah, helped out quite a bit. Right. I was actually looking through the commits and saw he actually committed quite a few things. And then Alex Beregszaszi, right, yeah, became involved. And there were several other people that I don't remember anymore, but those I think were the main characters back then. Yeah.

**[10:49] SPEAKER_01:**
For Kumavis, was that before he was doing MetaMask? Yeah. Yeah. So you know, we met—I met Kumavis at like...

**[10:57] SPEAKER_00:**
Um, it was at Mailchimp, may have been Mailchimp, at a party in SF or hangout. And he started just asking me a ton of questions about Ethereum, and we ended up chatting for a very long time. And then yeah, he was, you know, very proficient in JavaScript as well, so he started, you know...

**[11:23] SPEAKER_01:**
Hacking a bit on EthereumJS, right, right. Something I think some people have asked and I didn't know the answer to, is was there ever a fully syncing JavaScript node? Were you able to keep up...

**[11:41] SPEAKER_00:**
At any point? Yes. Like, so yes, we did have a syncing full node that worked for a little bit, but yeah, it was difficult. It still is. Like, I think it's doable today, like right now. It's actually not that bad.

I think the thing that, you know, sort of didn't become our focus though, because it was just like not a huge demand for that, right? Like, you know, I mean, Geth and everything else is going to go a lot faster. We were interested at the time in trying to embed a client in a browser. Yeah, yeah. Which is now possible, right?

**[12:30] SPEAKER_01:**
But through the Helios project, right? Yeah. So, what's that? I'm sorry, I don't know about Helios.

**[12:37] SPEAKER_00:**
Oh, it's a light client from a16z. Oh, right. They funded it. It's in Rust. Okay. And they compile it to Wasm. Right. And it, you know, okay, it's kind of cheesed, right? It just makes RPC requests. RPCs. But it verifies the Merkle proofs and it verifies consensus. Right, right, right. So it doesn't do the full thing, right. But you know, I would say it's a light client. It's definitely a light client that, you know, you have proof that the consensus is correct, and then you get back the state you've pulled that's verified.

**[13:18] SPEAKER_01:**
From third-party RPCs, right. It's all right, yeah, yeah, yeah. And so you attended Devcon 0 in Berlin in November 2014. Yes. Yeah. So how was that? That was really cool. It was my first time...

**[13:36] SPEAKER_00:**
Leaving the US. No, not quite. It was my first time flying over the ocean. Right. I'd been to Canada. Oh yes, nice. Right, I saw Niagara Falls and stuff. But yeah, so it was my first time in Europe, so it was super exciting. And yeah, I stayed in a big Airbnb with Juan Benet and Vitalik. Right. I think Vlad was in the Airbnb as well. It was super cool to just see everyone for the first time.

**[14:06] SPEAKER_01:**
Right, meet up and, um, yeah. Because there were a good chunk of people there. I was trying to count, I think, you know, 40 to 50 I think is about the number that were there. Pretty much everyone who was working on things. I was looking through, I don't think I could spot really anyone who was still involved who wasn't there, with maybe the—yeah, Anthony Di Iorio wasn't there. And he didn't technically leave until the end of 2015, but he was little involved. Yeah, I don't have—well, actually...

**[14:46] SPEAKER_00:**
I had a small contact with Anthony, but yeah, I never met him in—I don't think I've ever met him...

**[14:51] SPEAKER_01:**
In real life. I know what he looks like though. Right, yeah, I have a few times. Hoping to talk to him soon. Oh, nice. But yeah, there are missing videos from Devcon 0 which I'm still looking for. There's 10 of them on the playlist on YouTube. There's one further which didn't go in the playlist but is on there, but there seemed to be about 10 missing sessions in there. Okay, can you...

**[15:18] SPEAKER_00:**
Remember, did you—sorry, did you talk at Devcon 0? Was it there? I did, yeah. And I gave a big presentation, all big, I had my slides printed off. I gave a talk on EthereumJS, right, and...

**[15:35] SPEAKER_01:**
How I architected it. Um, yeah, so I think that video is currently lost, and I hope to recover it. It may have never got recorded. I don't know. I think they all did. Oh, okay. And the other thing Texture was saying was that he did interviews with nearly everyone as well. Can you remember, did you talk to Texture? Did he go off into some back room and do an interview with him? I do not remember...

**[16:00] SPEAKER_00:**
That. No. I remember Texture though. Yeah, and he's still around. Absolutely, yeah. So yeah, he was one...

**[16:07] SPEAKER_01:**
Of the earlier interviewees. Yeah, I've known Texture a long time, and it was funny because, you know, he had the water cooler channel, the Skype water cooler. Yes. So when I joined the EF, you know, I joined the EF channel and the water cooler, and I thought they were both, you know, like Foundation things. But it wasn't; it's basically Texture's troll room. So then you've got a bunch of sort of ex- or people outside, it was a broader group.

Skype are about to delete all their data, by the way. Oh, okay. So, but you can request a download. So if you want to do that, like, do it fast. I don't have access to my Skype account anymore. Well, I didn't, I mean, you can just log in and do a password recovery thing and then you can request it anyway. So I'm hoping to recover mine, and maybe there's some interesting, you know, tidbits in that water cooler channel. Yeah, definitely, that'd be interesting. Yeah. So then, you know, I guess on into 2015 and through all the PoCs, were you generally just, you know, continuing to maintain that as new...

**[17:24] SPEAKER_00:**
Features and changes came in through the PoCs? Yeah, um, so we did a lot. Like, a lot of time was spent on the Virtual Machine, as you can imagine, that's sort of the largest, one of the larger components. And I also was working on networking. Right. So EthereumJS was a smaller team than everyone else. Yes.

So yeah, we always lagged behind a bit. But yep, the networking protocols, RLPx, went through several iterations. And then the Virtual Machine went through several iterations. We contributed to the testing, right. And yeah, that was our main focus. Right. So yeah, more...

**[18:18] SPEAKER_01:**
About tooling use versus straight consensus client, because there are many EthereumJS repos and...

**[18:29] SPEAKER_00:**
Components, yeah. So the original architecture—and it doesn't exist this way anymore, it's been merged into a monorepo—but originally it was a bunch of small modules. It still is a bunch of small modules, but it's a monorepo. Yes, it's much more sensible. Yes, yes. But at that time, yeah, small repos for everything. And yeah, the focus was on building reusable components.

So the most widely used component, or most widely used module, was ethereumjs-tx. Right, right. Used for creating and signing transactions. Right, right. For, you know, wallets such as MetaMask would use that internally to, right, you know, construct and sign a transaction.

Then yeah, we had, you know, everything broken out. So RLP for serialization, the networking libraries, the Virtual Machine proper, some of the high-level ones. And yeah, so the fun thing about EthereumJS was that I tried to make these modules very approachable and easy to use. Right. So, you know, people did stuff like write a DHT scraper with it to, you know, see all the nodes, right. Right. What version they're running. Um, you know, and things like that...

**[19:53] SPEAKER_01:**
Of that nature. Yeah. Great, great. So do you have memories of launch day? Where, where were you on that day?

**[20:02] SPEAKER_00:**
How, how did that play out? Yeah, that was just like, I think I was hacking away somewhere. I don't think I was anywhere special, though. It was just sort of like another day for me. Right. You weren't, you weren't in a...

**[20:15] SPEAKER_01:**
Room with people? No. Watching the screen with bated breath? No, no, I wasn't. It wasn't really...

**[20:21] SPEAKER_00:**
Yeah, I was just like, "Yeah, I'll just keep coding," you know, type of thing. Because there were a bunch of...

**[20:27] SPEAKER_01:**
Them were in the Berlin office together. There's a few photos of that. Yeah, I wasn't there in the...

**[20:33] SPEAKER_00:**
Berlin office for that, unfortunately. I don't remember where I was, but yeah. Um, did you do any mining at any point? No, no. I was too nomadic. Nomadic. You got to have a place to put the hardware. Yes. I never...

**[20:51] SPEAKER_01:**
Had a storage place for it. No, no. So then I guess, you know, through 2015, probably the next big piece was Devcon 1. Did you attend Devcon 1 in... Yeah, yeah. London. I slept in a closet.

**[21:05] SPEAKER_00:**
That's my big Harry Potter memory from Devcon 1. Yep, so I gave a talk at Devcon 1.

**[21:13] SPEAKER_01:**
Right, also on EthereumJS. Right, surprisingly, right. So I mean, something somebody pointed out recently was like, if you look at the talks at Devcon 1, it's like everything. Like there were so many different talks on so many different ideas and concepts, you know, many of which foreshadowing things which are, you know, pretty big today, but probably nearly all of it was like 10 years too...

**[21:38] SPEAKER_00:**
Early, yeah, exactly. Yeah, we had a lot of—there's just so many layers that needed to be built. Obviously, when you start off, you see this thing, "I can do this." You don't fully understand all the layers that need to be created for that. That's a hard problem, though. And I think we're still probably catching up to some of the original use cases that were envisioned. I was mentioning...

**[22:04] SPEAKER_01:**
This to someone last night, and he was saying, "I think it's maybe another five or ten years from here before, you know, all of this stuff is in a viable kind of state." Yeah, it's a lot more work than perhaps we envisaged at the start. Yeah. It sounds so easy when you start, but yeah, it is hard.

Zsolt was saying, I think when he joined the Geth team, he was thinking this would be six months, 12 months kind of thing to work on. Slightly longer, I guess. And yeah, he asked Jeff, "So how long do you think for all of these pieces, you know, AlethZero and Mix and Mist and proof of work and proof of stake and sharding?" Yeah. And Jeff said, "Maybe about seven months, or a little more." That's hilarious. So it was a little more, yeah, slightly, a little bit more.

Yeah, I mean, I had that same delusion because the very first thing I was doing was doing ARM Linux cross builds of the C++ client to try and run it on my smartwatch. Okay. Really with the thought that light client was close, right, so we'll just do the porting of the full clients, and then the LES support will drop in in a few months, and you know, we can run a full node or a good enough light node on a watch or everywhere. It's just like, this is going to be everywhere, right? Every computing device, every router, just you know, it'll just pop in. You know, it'll just be another protocol like TCP/IP. You know, it'll be in the Linux kernel. It'll just be like another thing, another service. Hey, it definitely has a ways to go before Linus merges that. Yes, yes. I think, yeah, um, so...

**[24:00] SPEAKER_00:**
I would still like—I think it would be really cool though, if someone built like a file system interface for Ethereum where, like, you know, you could CD into a folder with all the blocks, and you know, tap right into a particular block and see a list of transactions, etc. You know, kind of like Plan 9, like... So you did a talk on this theme in Seattle.

**[24:29] SPEAKER_01:**
Um, there was a meetup with yourselves, like Kenny Rowe, some of the Dappsys...

**[24:39] SPEAKER_00:**
People, I think Kumavis as well. Yeah, I think Kumavis was there. Juan from IPFS was definitely there.

**[24:46] SPEAKER_01:**
Yes, he was. I think David Dias was there. Yeah. Into the Merkle Forest was one of the talks, and I think yours was like Planetary OS? Yeah, it was Interplanetary Operating System. There we go, there...

**[24:59] SPEAKER_00:**
We go. It was a fun talk. That's it. Merkle computing. Yeah, it can still happen. Yeah, yeah, and there's no, like, technical reason you can't do those things. It's just, you know, layers need to be...

**[25:14] SPEAKER_01:**
Built. Um, yeah, absolutely. So we're getting the Oscars-style music coming on. I'm going to have to have a wrap up. All right. I did intend to talk about ewasm and things, but maybe that's for another time. Sounds good. Okay, so yeah, we're up to the end of 2015. Nice. Okay, thanks so much, man. Yep.

**[25:34] SPEAKER_00:**
Thank you, Bob.