**[00:02] SPEAKER_01:** Test, hello. Can you hear me? Hello. Hello. We good? We both good? Yeah. So hello, I'm Bob Summerwill here with Early Days of Ethereum and talking to Martin Becze. Hello. Or is it Becze? We say Becze. Becze? Yeah, Becze. That works. Okay. So, yeah, thanks for talking to us. You are a very OG OG. You're more OG than I am by a couple of years maybe even. So, I mean, when...

**[00:48] SPEAKER_00:** What were you doing prior to Ethereum that led you to Ethereum? Yeah, that's a good question. So like prior to Ethereum I had gotten into Bitcoin for a bit. So I was actually at Occupy Wall Street, and I set up the Bitcoin donation address for OWS and started doing some development, just regular Web2 development. But as my projects developed, I started wondering how to decentralize them, as you naturally do if you've played around with crypto. And I was highly influenced by Bitcoin and BitTorrent. And this is around the time Namecoin also moved out. So I wanted to extend the concepts of Namecoin for my own project, which at the time was a geospatial map thing that displayed what was happening around you. And it was supposed to be federated. And I wanted to have a DNS system that we could resolve, like, a location to these servers. So I called it GeoDNS. And I was looking at how Namecoin implemented it, and I was like, ah, this is going to be a pain, I'm going to have to fork it, rebuild everything, get people to mine it, this is a lot of work. And then, as you naturally do, you're like, well, this could just be generalized.

**[01:50] SPEAKER_01:** Right, right.

**[01:51] SPEAKER_00:** Yeah, so this is around the time that Vitalik, he had written some articles, I believe, in Bitcoin Magazine, but maybe not on DAOs and DACs.

**[02:01] SPEAKER_01:** Yes.

**[02:02] SPEAKER_00:** I was very interested in that, too. And I was following that work. And then, yeah, I saw the white paper drop. And as soon as I saw the white paper drop, I was like, yeah, that's what I need. That makes a lot of sense. So then I started hacking on it because that was before any code, I think, was really operable. And I wanted to get my hands onto it. I think AlethZero is up, but it was really rough.

**[02:28] SPEAKER_01:** Yeah. It was up on GitHub.

**[02:30] SPEAKER_00:** And I was a JavaScript programmer. Right. So I was like, well, I better implement this in JavaScript because that's what I know. And I really just wanted to get my hands on it and really understand how it worked.

**[03:41] SPEAKER_01:** Right, right. So yeah, we were just looking at some commit, first commit dates. So we saw that Joseph Chow had had a first commit on Node Ethereum in February, and then we found March 2014 as probably the first commit on your side. So yeah, I mean, the white paper had come out in November of the previous year, but I was looking, you know, the C++ and Go clients started in very late December. But so yeah, you know, a couple of months in, as you say, it's all going to be a bit rough.

**[04:15] SPEAKER_00:** Yeah.

**[04:16] SPEAKER_01:** And yeah, I mean, it wasn't until April that you had the yellow paper. You know, that came a little later. I think maybe April-ish was when Geth and cpp-ethereum were maybe, you know, kind of working, talking to each other.

**[04:30] SPEAKER_00:** Yes. Yeah. Yeah. Yeah.

**[04:32] SPEAKER_01:** I'll have to find the date. There is that, I did see like, you know, maybe a tweet of when that was. And I think it was Charles sent a transaction to Gav or the other way around. Was it Gavcoin? Maybe.

**[04:45] SPEAKER_00:** Well, here's an interesting one. Gavcoin came later.

**[04:48] SPEAKER_01:** Well, there was a meetup in London in October 2014 where both Gav and Jeff were basically doing, hey, here's the status of Ethereum and roadmap kind of thing. You know, like an hour long, big, thorough thing. But what they did at that was Gav had got Gavcoin, which was written in LLL. And Jeff had JeffCoin, which was written in Mutan. And they had an on-chain DEX. It was an on-chain order book, really clunky, you know, like here I'm offering, you know, three Gavcoin for 10 JeffCoin or what have you. But they demonstrated it there and, you know, did a transaction to put an offer into the order book. And then Jeff's like pressing the button to mine a block. And the exchange happened.

**[05:35] SPEAKER_00:** That's really funny, yeah.

**[05:37] SPEAKER_01:** But so, I mean, were there many people where you were living that were regularly having meetups and being involved with Ethereum?

**[05:45] SPEAKER_00:** No, not at all. I was living in Indiana, so very rural.

**[05:50] SPEAKER_01:** Right.

**[05:51] SPEAKER_00:** And it was just... Yeah, it was completely... I only connected online.

**[05:57] SPEAKER_01:** Right, right.

**[05:58] SPEAKER_00:** And I remained that way for, you know, some time.

**[06:01] SPEAKER_01:** Right.

**[06:02] SPEAKER_00:** And it wasn't until, I don't know, a few months later, I was trying to get a job at Ripple.

**[06:08] SPEAKER_01:** Oh, yes.

**[06:09] SPEAKER_00:** Ripple also, so they had a, I don't remember what it was called, but they were working on a VM.

**[06:16] SPEAKER_01:** Yeah. I can't remember. Codex or something.

**[06:20] SPEAKER_00:** It wasn't like that. Maybe. Yeah. I was interested in that and I had been working on implementing the Ethereum Virtual Machine in JavaScript. They thought that was pretty cool, and they flew me out for an interview at their office. And that is when I met Vitalik, because not at Ripple. He just happened to be in San Francisco at the same time. And also Joseph Chow for the first time.

**[06:48] SPEAKER_01:** Do you know when that might have been?

**[06:50] SPEAKER_00:** Unfortunately, no. I'm really bad with dates. But it was definitely past March. It was sometime in the summer. And then that's when I met up with everyone proper. And Vitalik's like, no, just come work on Ethereum. So yeah, that's what I did.

**[07:10] SPEAKER_01:** So was that working for EthDev as a contractor?

**[07:14] SPEAKER_00:** So, yes, I was working for EthDev as a contractor at that point.

**[07:18] SPEAKER_01:** Right, right. And yeah, Vitalik notoriously also nearly worked for Ripple, but could not get his work permit. So yeah, the world might have looked very, very different if Vitalik had joined Ripple as an intern back then, rather than Ethereum. Ripple sort of like, they failed to get everyone. But if they had Ripple, it also may have looked a lot different.

**[07:42] SPEAKER_00:** Yeah, yeah.

**[07:43] SPEAKER_01:** Well, some of my very earliest meetups I went to at the start of 2014, it was like, here's a demo of Ripple. Because it really was a lot less of a tribal setup, right? Like everyone was Bitcoiners because that's all there was. And then it's like, oh, there are these other things appearing. And oh, here's a different form of consensus. Here's a different flavor. And I was actually interested in, there was an early version of Ripple.

**[08:10] SPEAKER_00:** Made by this guy in Canada.

**[08:12] SPEAKER_01:** Yeah, Ryan Fugger.

**[08:13] SPEAKER_00:** Yes, yeah. Who lives in Vancouver, same as me.

**[08:16] SPEAKER_01:** Oh, nice. I've not met him ever though.

**[08:18] SPEAKER_00:** So I was interested in that version. Like you were able, yeah, I'm not sure if I'm going to be able to actually recall, but you were like able to, it was like debt. You were able to open debt lines to various people you know.

**[08:32] SPEAKER_01:** Yeah.

**[08:33] SPEAKER_00:** And then you know debt would flow through the people.

**[08:36] SPEAKER_01:** That's right. It would ripple through.

**[08:38] SPEAKER_00:** Yeah, ripple through. And this was pre-blockchain. It was built in PHP. They had a demo in PHP. I had signed up on it. I was playing around. I was offering my services on it.

**[08:50] SPEAKER_01:** Right, right. But yeah, that's how I got interested in Ripple. But yeah, then they ended up moving in a slightly different direction.

**[08:58] SPEAKER_00:** Slightly different, yes.

**[09:00] SPEAKER_01:** I think it was 2004, Ryan's work.

**[09:02] SPEAKER_00:** Yeah, around then, very early, absolutely.

**[09:06] SPEAKER_01:** So when, you know, you were then working full-time on Ethereum, did you have many collaborators? Were many people working on the code together with you?

**[09:18] SPEAKER_00:** So it was like me and Joseph Chow to start with, and then Joseph Chow eventually went off. And he started working on BTC Relay.

**[09:28] SPEAKER_01:** Yeah, that's a very interesting project.

**[09:30] SPEAKER_00:** Yeah. So he did that next. But yeah, there was a bunch of people coming in and out. Kumavis helped out quite a bit.

**[09:38] SPEAKER_01:** Right. I was actually looking through the commits and saw he actually committed quite a few things.

**[09:43] SPEAKER_00:** Alex Beregszaszi, axic, became involved. And there were several other people that I don't remember anymore. But those, I think, were the main characters back then.

**[09:55] SPEAKER_01:** Yeah, yeah. So, I mean, for Kumavis, was that before he was doing MetaMask?

**[10:00] SPEAKER_00:** Yeah, yeah. So, you know, I met Kumavis at, like, it was at MailChimp. May have been MailChimp at a party in SF for a hangout. And he started just asking me a ton of questions about Ethereum. And we ended up chatting for a very long time. And then, yeah, he was, you know, he was very proficient in JavaScript as well. So he, you know, started hacking a bit on Ethereum.js.

**[10:28] SPEAKER_01:** Right, right. Something I think some people have asked, and I didn't know the answer to, is was there ever a fully syncing JavaScript node? Were you able to keep up at any point?

**[10:42] SPEAKER_00:** Yes. Yes, we did have a syncing full node that worked for a little bit. But yeah, it was difficult. I think it's doable today. It's actually not that bad. I think the thing that... That sort of didn't become our focus, though, because it was just, like, not a huge demand for that.

**[11:02] SPEAKER_01:** Right.

**[11:03] SPEAKER_00:** Like, you know, Geth and everything else is going to go a lot faster. We were interested in the time of trying to embed a client in a browser.

**[11:12] SPEAKER_01:** Yeah, yeah.

**[11:13] SPEAKER_00:** Which is now possible.

**[11:15] SPEAKER_01:** Right.

**[11:16] SPEAKER_00:** But through the Helios project.

**[11:18] SPEAKER_01:** Right. Yeah. So, what's that? I'm sorry, I don't know about Helios.

**[11:22] SPEAKER_00:** Oh, it's a light client from a]16z.

**[11:25] SPEAKER_01:** Oh, right, right. They funded it.

**[11:27] SPEAKER_00:** It's in Rust.

**[11:28] SPEAKER_01:** Okay.

**[11:29] SPEAKER_00:** And they compile it to Wasm.

**[11:31] SPEAKER_01:** To Wasm, right.

**[11:32] SPEAKER_00:** And it, you know, okay, it kind of cheats, right? It just makes RPC requests, RPCs, but it verifies the Merkle proofs and it verifies consensus.

**[11:42] SPEAKER_01:** Right, right, right.

**[11:43] SPEAKER_00:** So, yeah, it doesn't do the full thing, right? But, you know, I would say it's like a light client. It's definitely a light client that, you know, you have proof that the consensus is correct and then you have, you know, you pull state that's verified from third-party RPCs. It's all right.

**[12:02] SPEAKER_01:** Yeah, yeah, yeah. And so you attended DEVCON Zero in Berlin in November 2014?

**[12:10] SPEAKER_00:** Yes, yeah.

**[12:11] SPEAKER_01:** So how was that?

**[12:13] SPEAKER_00:** That was really cool. It was my first time leaving the U.S. No, not quite. It was my first time flying over the ocean.

**[12:22] SPEAKER_01:** Right.

**[12:23] SPEAKER_00:** I'd been to Canada.

**[12:24] SPEAKER_01:** Oh, yes, nice.

**[12:25] SPEAKER_00:** Right. Saw the Niagara Falls and stuff. But yeah, so it's the first time in Europe. So it was super exciting. And yeah, I stayed in a big Airbnb with Juan Benet and Vitalik.

**[12:38] SPEAKER_01:** Right.

**[12:39] SPEAKER_00:** I think Vlad was in the Airbnb as well. It was super cool just to see everyone for the first time.

**[12:46] SPEAKER_01:** Right.

**[12:47] SPEAKER_00:** Meet up and yeah.

**[12:49] SPEAKER_01:** Because there were a good chunk of people there. I was trying to count. I think, you know, 40 to 50, I think, is about the number that were there. Pretty much everyone who was working on things. I was looking through. I don't think I could spot really anyone who was still involved, who wasn't there. Anthony Di Iorio wasn't there and he didn't technically leave until the end of 2015, but he was little involved.

**[13:18] SPEAKER_00:** Yeah, I don't have... Well, actually, I had a small contact with Anthony, but I never met him in... I don't think I've ever met him in real life. I know what he looks like, though.

**[13:30] SPEAKER_01:** Right, yeah, I have a few times. Hoping to talk to him soon.

**[13:34] SPEAKER_00:** Oh, nice.

**[13:35] SPEAKER_01:** But, yeah, from... There are missing videos from DEVCON 0 which I'm still looking for. There's 10 of them on the playlist on YouTube. There's one further which didn't go in the playlist but is on there. But there seem to be about 10 missing sessions in there. Can you remember? Did you talk at DEVCON 0?

**[13:58] SPEAKER_00:** I did, yeah. I gave a big presentation. Well, big. I had my slides printed off. I gave a talk on the Ethereum.js and how I architected it. So I think that video is currently lost, and I hope to recover it.

**[14:16] SPEAKER_01:** It may have never got recorded. I don't know.

**[14:18] SPEAKER_00:** I think they all did.

**[14:19] SPEAKER_01:** Oh, okay. And the other thing Texture was saying was that he did interviews with nearly everyone as well. Can you remember? Did you talk to Texture? Did he go off into some back room and do an interview with him?

**[14:33] SPEAKER_00:** I do not remember that. No. I remember Texture, though, yeah, and he's still around.

**[14:38] SPEAKER_01:** Absolutely, yeah. So, yeah, he was one of the earlier interviewees. Yeah, I've known Texture a long time. And it was funny because, you know, he had the water cooler channel, the Skype water cooler?

**[14:51] SPEAKER_00:** Yes.

**[14:52] SPEAKER_01:** So... When I joined the EF, you know, I joined the EF channel and the water cooler. And I thought they were both, you know, like foundation things. But it wasn't. It's basically Texture's troll room.

**[15:06] SPEAKER_00:** So then you've got a bunch of sort of ex or people outside. It was a broader group.

**[15:12] SPEAKER_01:** Skype are about to delete all their data, by the way.

**[15:15] SPEAKER_00:** Oh, OK.

**[15:16] SPEAKER_01:** But you can request a download. So if you want to do that, do it fast.

**[15:20] SPEAKER_00:** I don't have access to my Skype account anymore.

**[15:22] SPEAKER_01:** Well, I didn't. I mean, you can just log in and do a password recovery thing, and then you can request it anyway. So I'm hoping to recover mine, and maybe there's some interesting tidbits in that water cooler channel.

**[15:35] SPEAKER_00:** Yeah, definitely. That'd be interesting.

**[15:38] SPEAKER_01:** Yeah. So then, you know, I guess on into 2015 and through all the POCs, were you generally just, you know, continuing to maintain that as new features and changes came in through the POCs?

**[15:52] SPEAKER_00:** Yeah. So we did a lot of time was spent on the virtual machine. As you can imagine, that's sort of the largest, one of the larger components. And I also was working on networking.

**[16:05] SPEAKER_01:** Right.

**[16:06] SPEAKER_00:** So Ethereum.js has a smaller team than everyone else.

**[16:10] SPEAKER_01:** Yes.

**[16:11] SPEAKER_00:** So, yeah, we always lagged behind a bit. But yeah, the networking protocols, RLPx went through several iterations and then the virtual machine went through several iterations. We contributed to the testing.

**[16:26] SPEAKER_01:** Right.

**[16:27] SPEAKER_00:** And yeah, that was our main focus.

**[16:30] SPEAKER_01:** Right. So yeah, more about tooling use versus straight consensus client, because there are many Ethereum.js repos and components.

**[16:40] SPEAKER_00:** Yeah, so the original architecture, and it doesn't exist this way anymore, it's been merged into a monorepo, but originally it was a bunch of small modules. It still has a bunch of small modules, but it's a monorepo, which is much more sensible.

**[16:56] SPEAKER_01:** Yes, yes.

**[16:57] SPEAKER_00:** But at that time, yeah, small repos for everything. And yeah, the focus was on building reusable components. The most widely used module was ethereumjs-tx, which is used for creating and signing transactions. Wallets such as MetaMask would use that internally to construct and sign a transaction. Then we had everything broken out, so RLP for serialization, the networking libraries, the virtual machine proper, some of the high-level ones. So the fun thing about Ethereum.js was that I tried to make these modules very approachable and easy to use. So people did stuff like write a DHT scraper with it to see all the nodes, see what version they're running, and things of that nature.

**[17:48] SPEAKER_01:** Yeah, great, great. So do you have memories of launch day? Where were you on that day? How did that play out?

**[17:56] SPEAKER_00:** Yeah, that was just like, I think I was hacking away somewhere. I don't think I was anywhere special, though. It was just sort of like another day for me.

**[18:06] SPEAKER_01:** Right. You weren't in a room with people watching the screen with bated breath.

**[18:10] SPEAKER_00:** No, no, I wasn't really. Yeah, I was just like, yeah, I'll just keep coding, you know, type of thing.

**[18:16] SPEAKER_01:** Because a bunch of them were in the Berlin office together. There's a few photos of that.

**[18:20] SPEAKER_00:** Yeah, I wasn't there in the Berlin office for that, unfortunately. I don't remember where I was, but yeah.

**[18:26] SPEAKER_01:** Did you do any mining at any point?

**[18:28] SPEAKER_00:** No. No. I was too nomadic.

**[18:32] SPEAKER_01:** Right, you haven't got the place to put the hardware.

**[18:35] SPEAKER_00:** Yes, I never had a storage place for... No, no. So then, I guess, you know, through 2015, probably the next big piece was DEVCON 1. Did you attend DEVCON 1 in London?

**[18:48] SPEAKER_01:** Yeah, London.

**[18:49] SPEAKER_00:** I slept in a closet. That's my big memory.

**[18:52] SPEAKER_01:** Yeah.

**[18:53] SPEAKER_00:** Memory from DEVCON 1. Yeah.

**[18:55] SPEAKER_01:** I also gave a talk at DEVCON 1.

**[18:58] SPEAKER_00:** Right. Also on Ethereum.js, not surprisingly.

**[19:01] SPEAKER_01:** Right, right. So, I mean, something somebody pointed out recently was like, if you look at the talks at DEVCON 1, it's like everything. There were so many different talks on so many different ideas and concepts, many of which foreshadowing things which are pretty big today. But probably nearly all of it was like 10 years too early.

**[19:22] SPEAKER_00:** Yeah, exactly. There's just so many layers that needed to be built. Obviously, when you start off, you see this thing, I can do this. You don't fully understand all the layers that need to be created for that. That's a hard problem, though.

**[19:38] SPEAKER_01:** And I think we're still probably catching up to some of the original use cases that were envisioned. I was mentioning this to someone last night and he was saying, I think it's maybe another five or ten years from here before all of this stuff is in a viable kind of state. It's a lot more work than perhaps we envisaged at the start.

**[19:58] SPEAKER_00:** Yeah, it sounds so easy when you start, but yeah, it is hard.

**[20:02] SPEAKER_01:** Zsolt was saying, I think when he joined the Geth team, he was thinking this would be six months, 12 months kind of thing to work on. Slightly longer, I guess. And yeah, he asked Jeff, so, you know, how long do you think, you know, for all of these pieces, you know, AlethZero and Mix and Mist and proof of stake and sharding?

**[20:22] SPEAKER_00:** Yeah.

**[20:23] SPEAKER_01:** And Jeff said maybe about seven months or a little more.

**[20:27] SPEAKER_00:** That's hilarious.

**[20:28] SPEAKER_01:** So it was a little more. Yeah, slightly a little bit more. I mean, I had that same delusion because the very first thing I was doing was doing ARM Linux cross builds of the C++ client to try and run it on my smartwatch. Really with the thought that light client was close, right? So we'll just do the porting of the full clients and then the LES support will drop in in a few months and we can run a full node or a good enough light client node on a watch or everywhere. It's just like this is going to be everywhere, right? Every computing device, every router, it will just pop in. It'll just be another protocol like TCP/IP, you know, it'll be in the Linux kernel. It'll just be like another thing, another service.

**[21:08] SPEAKER_00:** It definitely has ways to go before Linus merges that.

**[21:12] SPEAKER_01:** Yes, yes. I think.

**[21:14] SPEAKER_00:** Yeah. So... I would still like... I think it would be really cool, though, if someone built a file system interface for Ethereum where like, you know, you could like CD into a folder with all the blocks and, you know, CD into a particular block and see a list of transactions, etc. You know, kind of like a Plan 9.

**[21:38] SPEAKER_01:** So you did a talk on this theme in Seattle. There was a meetup with yourselves, like Kenny Rowe, some of the DAOhub people, I think Kumavis as well.

**[21:48] SPEAKER_00:** Yeah, I think Kumavis was there.

**[21:50] SPEAKER_01:** Juan from IPFS was definitely there.

**[21:52] SPEAKER_00:** Yes, he was.

**[21:53] SPEAKER_01:** I think David Dias was there.

**[21:55] SPEAKER_00:** Yeah.

**[21:56] SPEAKER_01:** Into the Merkle Forest was one of the talks, and I think yours was, like, Planetary OS.

**[22:02] SPEAKER_00:** Yeah, it was Interplanetary Operating System.

**[22:05] SPEAKER_01:** There we go, there we go. It was a fun talk.

**[22:08] SPEAKER_00:** That's it, Merkle Computing.

**[22:10] SPEAKER_01:** Yeah. Can still happen.

**[22:12] SPEAKER_00:** Yeah, yeah, and there's no, like, technical reason, like, you can't do those things. It's just, you know, layers. Layers need to be built.

**[22:20] SPEAKER_01:** Yeah, absolutely. So we're getting the Oscars-style music coming on. I'm going to have to have a wrap-up. I did intend to talk about eWASM and things, but maybe that's for another time.

**[22:32] SPEAKER_00:** Sounds good.

**[22:33] SPEAKER_01:** Okay, so yeah, we're up to the end of 2015.

**[22:36] SPEAKER_00:** Nice, we made it.

**[22:37] SPEAKER_01:** Thanks so much, Martin.

**[22:38] SPEAKER_00:** Yep, thank you, Bob.