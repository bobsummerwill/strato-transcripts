**[00:02] SPEAKER_00:** Test. Hello, can you hear me?

**[00:05] SPEAKER_01:** Hello? Hello?

**[00:13] SPEAKER_00:** We good? We’re both good, yeah. So, hello, I’m Bob Summerwill here with *Early Days of Ethereum*, and talking to Martin Baxter. Hello. Or is it Bexe?

**[00:29] SPEAKER_01:** We say “Bixby,” but “busy,” “busy,” you know, Bexy—that works.

**[00:34] SPEAKER_00:** Okay. So yeah, thanks for talking to us. You are a very OG OG. You are more OG than I am, by a couple of years maybe. Even so, what were you doing prior to Ethereum that led you to Ethereum?

**[00:54] SPEAKER_01:** Yeah, that’s a good question. Prior to Ethereum, I had gotten into Bitcoin for a bit. So I was actually at Occupy Wall Street, and I set up the Bitcoin donation address for OWS, and started doing some development—just regular Web2 development. But as my projects developed, I started wondering how to decentralize them, as you naturally do if you’ve played around with crypto. I was highly influenced by Bitcoin and BitTorrent, and this is around the time of Namecoin also.

**[01:45] SPEAKER_00:** Right, right.

**[01:47] SPEAKER_01:** So I sort of wanted to extend the concepts of Namecoin for my own project, which at the time was a geospatial map thing that displayed what was happening around you. It was supposed to be federated, and I wanted to have a DNS system where we could resolve a location to these servers. So I called it GoDNS. And I was looking at how Namecoin implemented it, and I was like, “Ah, this is going to be a pain. I’m going to have to fork it, rebuild everything, get people to mine it. This is a lot of work.” And then, as you naturally do, you’re like, “Well, this could just be generalized,” right?

**[02:52] SPEAKER_00:** Yes.

**[02:52] SPEAKER_01:** So, you know, this is around the time that Vitalik—he had written some articles, I believe in *Bitcoin Magazine*, but maybe not—on DAOs and DAX.

**[03:16] SPEAKER_00:** Right.

**[03:17] SPEAKER_01:** And I was very interested in that too, and I was following that work. And then, yeah, I saw the white paper drop, and as soon as I saw the white paper drop, I was like, “Yeah, I need that. That’s what I need. That makes a lot of sense.” So then I started hacking on it, because that was before any code, I think, was really operable.

**[03:16] SPEAKER_00:** Right.

**[03:17] SPEAKER_01:** And I wanted to get my hands onto it. I think AlethZero was up, but it was really rough. Yeah, it was up on GitHub. And I was a JavaScript programmer, right? So I was like, “Well, I better implement this in JavaScript, because that’s what I know.” And I really just wanted to get my hands on it and really understand how it worked.

**[03:41] SPEAKER_00:** Right, right. So, yeah, we were just looking at some first commit dates. So we saw that Joseph Chow had had a first commit on Node Ethereum in February, and then we found March 2014 is probably the first commit on your side. So, yeah, I mean, the white paper had come out in November of the previous year. But I was looking: the C and Go clients started in very late December. So, yeah, a couple of months in, as you say, it’s all going to be a bit rough. And yeah, I mean it wasn’t until April that you had the Yellow Paper. That came a little later, I think. I think maybe April-ish was when Geth and cpp-ethereum were maybe kind of working.

**[04:42] SPEAKER_01:** Talking to each other.

**[04:43] SPEAKER_00:** Yes. Yeah, yeah, yeah. I’ll have to find the date. I did see a tweet of when that was, and I think it was Charles sent a transaction to Gav, or the other way around.

**[04:58] SPEAKER_01:** Was it GavCoin maybe? Well, here’s an interesting—GavCoin came later.

**[05:04] SPEAKER_00:** Well, there was a meetup in London in October 2014 where both Gav and Jeff were basically doing “Hey, here’s the status of Ethereum and roadmap,” kind of thing—like an hour-long big thorough thing. But what they did at that was: Gav had GavCoin, which was written in LLL.

**[05:26] SPEAKER_01:** Yeah.

**[05:27] SPEAKER_00:** And Jeff had JeffCoin, which was written in Mutan. And they had an on-chain DEX. It was an on-chain order book. Really clunky, like: “Here, I’m offering three GavCoin for 10 JeffCoin,” or what have you. But they demonstrated it there, and did a transaction to put an offer into the order book, and then Jeff’s pressing the button to mine a block. And that really funny exchange happened. But, I mean, were there many people where you were living that were regularly having meetups and being involved with Ethereum?

**[06:10] SPEAKER_01:** No, not at all. I was living in Indiana, so very rural. It was completely—I only connected online.

**[06:20] SPEAKER_00:** Right, right.

**[06:21] SPEAKER_01:** And I remained that way for some time.

**[06:25] SPEAKER_00:** Right.

**[06:28] SPEAKER_01:** And it wasn’t until, I don’t know, a few months later—I was trying to get a job at Ripple.

**[06:36] SPEAKER_00:** Oh, yes.

**[06:39] SPEAKER_01:** Ripple also. So they had a—I don’t remember what it was called—but they were working on a VM.

**[06:46] SPEAKER_00:** Yeah. I can’t remember—CodeCodex or something. It wasn’t like that.

**[06:52] SPEAKER_01:** Maybe.

**[06:53] SPEAKER_00:** Yeah.

**[06:56] SPEAKER_01:** So I was interested in that, and I had been working on implementing the Ethereum Virtual Machine in JavaScript. So they thought that was pretty cool, and they flew me out for an interview at their office. And that is when I met Vitalik, because—

**[07:18] SPEAKER_00:** Right.

**[07:18] SPEAKER_01:** Not at Ripple—he just happened to be in San Francisco at the same time. And also Joseph Chow for the first time.

**[07:26] SPEAKER_00:** Do you know when that might have been?

**[07:28] SPEAKER_01:** Unfortunately, no. I’m really bad at this. But it was definitely past March, sometime in the summer. And then that’s when I met up with everyone proper. And Vitalik’s like, “Nah, just come work on Ethereum.” So, yeah, that’s what I did.

**[07:48] SPEAKER_00:** So was that working for ETH Dev as a contractor?

**[07:53] SPEAKER_01:** So yes, I was working for ETH Dev as a contractor at that point.

**[07:58] SPEAKER_00:** Right, right. And yeah, Vitalik notoriously also nearly worked for Ripple but could not get his work permit. So, yeah, the world might have looked very, very different if Vitalik had joined Ripple as an intern back then, rather than Ethereum.

**[08:17] SPEAKER_01:** Sort of like they failed to get everyone. But if they had, Ripple also may have looked a lot different.

**[08:24] SPEAKER_00:** Yeah, yeah, yeah. Well, some of my very earliest meetups I went to at the start of 2014, it was like, “Here’s a demo of Ripple,” because it really was a lot less of a tribal setup, right? Everyone was Bitcoiners because that’s all there was. And then it’s like, “Oh, there are these other things appearing.” And, “Oh yeah, it’s a different form of consensus. Here’s a different flavor.”

**[08:45] SPEAKER_01:** And I was actually interested in—there was an early version of Ripple made by this guy in Canada.

**[08:53] SPEAKER_00:** Yeah, Ryan Fugger.

**[08:54] SPEAKER_01:** Yes. Yeah.

**[08:55] SPEAKER_00:** Who lives in Vancouver, same as me.

**[08:58] SPEAKER_01:** Oh, nice.

**[08:58] SPEAKER_00:** I’ve not met him ever, though.

**[09:00] SPEAKER_01:** So I was interested in that version. You were able—you were able—yeah, I’m not sure if I’m going to be able to actually recall, but you were able to—It was like debt. You were able to open debt lines to various people, you know.

**[09:14] SPEAKER_00:** Yeah.

**[09:15] SPEAKER_01:** And then debt would flow through the people.

**[09:17] SPEAKER_00:** That’s right. It would ripple through.

**[09:19] SPEAKER_01:** Yeah, ripple through. And this was pre-blockchain. It was built in PHP. They had a demo in PHP. I had signed up on it, playing around. I was offering my services on it. But yeah, then that’s how I got interested in Ripple. But yeah, then they ended up moving in a slightly different direction.

**[09:42] SPEAKER_00:** Slightly different, yes. I think it was 2004, Ryan’s work. Yeah, around then.

**[09:47] SPEAKER_01:** Very early.

**[09:48] SPEAKER_00:** Absolutely. So when you were then working full time on Ethereum, did you have many collaborators? Were many people working on the code together with you?

**[10:02] SPEAKER_01:** It was like me and Joseph Chow to start with. And then Joseph Chow eventually went off and he started working on BTC Relay.

**[10:14] SPEAKER_00:** Yeah, I don’t know if that’s a very interesting project.

**[10:17] SPEAKER_01:** Yeah. So he did that next. But yeah, there was a bunch of people coming in and out. Kumavis Davis helped out quite a bit.

**[10:26] SPEAKER_00:** Right.

**[10:30] SPEAKER_01:** I was actually looking through the commits and saw he actually committed quite a few things. And then Alex Beregszaszi became involved, and there were several other people that I don’t remember anymore, but those, I think, were the main characters back then.

**[10:47] SPEAKER_00:** Yeah, yeah. So, I mean, for Kumavis, was that before he was doing MetaMask?

**[10:54] SPEAKER_01:** Yeah, yeah. So we met—I met Kumavis at, like, it was MailChimp, may have been MailChimp, at a party in SF or a hangout. And he started just asking me a ton of questions about Ethereum, and we ended up chatting for a very long time. And then, yeah, he was very proficient at JavaScript as well, so he started hacking a bit on Ethereum.js.

**[11:26] SPEAKER_00:** Right. Something I think some people have asked, and I didn’t know the answer to, is: was there ever a fully syncing JavaScript node? Were you able to keep up at any point?

**[11:43] SPEAKER_01:** Yes. So, yes, we did have a syncing full node that worked for a little bit, but yeah, it was difficult. I still think it’s doable today. It’s actually not that bad. I think the thing that didn’t become our focus, though, was that there was not a huge demand for that.

**[12:15] SPEAKER_00:** Right.

**[12:16] SPEAKER_01:** Everything else was going to go a lot faster. We were interested at the time in trying to embed a client in a browser.

**[12:27] SPEAKER_00:** Yeah, yeah.

**[12:29] SPEAKER_01:** Which is now possible.

**[12:30] SPEAKER_00:** Right.

**[12:30] SPEAKER_01:** But through the Helios project.

**[12:33] SPEAKER_00:** Right, yeah. So what’s that? I’m sorry, I don’t know about Helios.

**[12:38] SPEAKER_01:** Oh, it’s a light client from a16z.

**[12:42] SPEAKER_00:** Oh, right. Right.

**[12:43] SPEAKER_01:** They funded it. It’s in Rust.

**[12:44] SPEAKER_00:** Okay.

**[12:45] SPEAKER_01:** And they compile it to WASM. And it, you know—okay, it’s kind of “cheesy,” right? It just makes RPC requests, but it verifies the Merkle proofs and it verifies consensus.

**[12:58] SPEAKER_00:** Right, right, right.

**[12:58] SPEAKER_01:** So, yeah, it doesn’t do the full thing, right? But since I would say it’s like a light client, it’s definitely a light client where you have proof the consensus is correct, and then you pull state that’s verified from third-party RPCs. It’s all right.

**[13:22] SPEAKER_00:** Yeah, yeah, yeah. And so you attended Devcon 0 in Berlin in November 2014.

**[13:30] SPEAKER_01:** Yes. Yeah.

**[13:31] SPEAKER_00:** So how was that?

**[13:32] SPEAKER_01:** That was really cool. It was my first time leaving the US. No, not quite. It was my first time flying over the ocean.

**[13:40] SPEAKER_00:** Right.

**[13:41] SPEAKER_01:** I’d been in Canada—

**[13:42] SPEAKER_00:** Oh, yes. Nice.

**[13:44] SPEAKER_01:** Right—and saw Niagara Falls and stuff. But yeah, first time in Europe, so I was super excited. And yeah, I stayed in a big Airbnb with Juan Benet and Vitalik.

**[13:58] SPEAKER_00:** Right.

**[13:59] SPEAKER_01:** I think Vlad was in the Airbnb as well. It was super cool. Just, you know, see everyone for the first time. Meet up and, yeah.

**[14:10] SPEAKER_00:** Right. Because there are a good chunk of people there. I was trying to count—I think 40 to 50 is about the number that were there. Pretty much everyone who was working on things, I was looking through. I don’t think I could spot really anyone who was still involved who wasn’t there, with maybe—yeah, Anthony Di Iorio wasn’t there. And he didn’t technically leave until the end of 2015, but he was a little involved.

**[14:44] SPEAKER_01:** Yeah, I don’t have—well, actually I had a small contact with Anthony, but yeah, I never met him. I don’t think I’ve ever met him in real life. I know what he looks like, though, right?

**[14:54] SPEAKER_00:** Yeah, I have a few times. Hoping to talk to him soon.

**[14:57] SPEAKER_01:** Oh, nice.

**[14:59] SPEAKER_00:** But yeah, there are missing videos from Devcon 0, which I’m still looking for. There’s 10 of them on the playlist on YouTube. There’s one further which didn’t go in the playlist, but is on there. But there seem to be about 10 missing sessions in there. Can you remember—sorry—did you talk at Devcon 0?

**[15:22] SPEAKER_01:** I did, yeah. And I gave a big presentation—well, big. I had my slides printed off. I gave a talk on Ethereum.js and how I architected it. Yeah.

**[15:39] SPEAKER_00:** So I think that video is currently lost, and I hope to recover it.

**[15:44] SPEAKER_01:** May have never got recorded. I don’t know.

**[15:46] SPEAKER_00:** I think they all did.

**[15:48] SPEAKER_01:** Okay.

**[15:49] SPEAKER_00:** And the other thing Tex was saying was that he did interviews with nearly everyone as well. Can you remember, did you talk to Tex? Did he go off into some back room and do an interview with him?

**[15:59] SPEAKER_01:** I do not remember that. I remember Tex though. Yeah. And he’s still around.

**[16:05] SPEAKER_00:** Absolutely. Yeah. So, yeah, he was one of the earlier interviewees. I’ve known Tex for a long time, and it was funny because he had the water cooler channel—the Skype water cooler.

**[16:18] SPEAKER_01:** Yes.

**[16:19] SPEAKER_00:** So when I joined the EF, I joined the EF channel and the water cooler, and I thought they were both foundation things, but it wasn’t. It was basically Tex’s control room. So then you got a bunch of people outside—it was a broader group. Skype are about to delete all their data, by the way. But you can request a download. So if you want to do that, do it fast.

**[16:51] SPEAKER_01:** I don’t have access to my Skype account anymore.

**[16:55] SPEAKER_00:** Well, I didn’t—I mean, you can just log in and do a password recovery thing, and then you can request it anyway. So I’m hoping to recover mine, and maybe there’s some interesting tidbits in that water cooler channel.

**[17:09] SPEAKER_01:** Yeah, definitely. That’d be interesting.

**[17:11] SPEAKER_00:** Yeah. So then, you know, I guess on into 2015 and through all the PoCs, were you generally just continuing to maintain that as new features and changes came in through the PoCs?

**[17:28] SPEAKER_01:** Yeah. So a lot of time was spent on the virtual machine, as you can imagine. That’s one of the larger components. I also was working on networking. Ethereum.js was a smaller team than everyone else, so we always lagged behind a bit. But yep, the networking protocols—RLPx went through several iterations, and then the virtual machine went through several iterations. We contributed to the testing. And yeah, that was our main focus.

**[18:16] SPEAKER_00:** Right. So, yeah, more about tooling use versus straight consensus client, because there are many Ethereum.js repos and components.

**[18:30] SPEAKER_01:** Yeah. So the original architecture—it doesn’t exist this way anymore; it’s been merged into a monorepo. But originally it was a bunch of small modules. It still is a bunch of small modules, but it’s a monorepo. It’s much more sensible.

**[18:44] SPEAKER_00:** Yes, yes.

**[18:45] SPEAKER_01:** But at that time, yeah, small repos for everything. And yeah, the focus was on building reusable components. So the most widely used component, or most widely used module, was ethereumjs-tx, used for creating and signing transactions.

**[19:04] SPEAKER_00:** Right.

**[19:04] SPEAKER_01:** So wallets such as MetaMask would use that internally to construct and sign a transaction. Then we had everything broken out: so RLP for serialization, the networking libraries, the virtual machine proper. Some of the high-level ones. The fun thing about Ethereum.js was that I tried to make these modules very approachable and easy to use. So people did stuff like write a DHT scraper with it to see all the nodes, see what version they’re running, and things of that nature.

**[19:54] SPEAKER_00:** Yeah, great, great. So do you have memories of launch day? Where were you on that day? How did that play out?

**[20:05] SPEAKER_01:** Yeah, that was just like—I think I was hacking away somewhere. I don’t think I was anywhere special though. It was just sort of another day for me.

**[20:13] SPEAKER_00:** Right. You weren’t in a room with people watching the screen with bated breath?

**[20:19] SPEAKER_01:** No, no, I wasn’t. It wasn’t really—yeah, I was just like, “Yeah, I’ll just keep coding,” you know.

**[20:25] SPEAKER_00:** Because there were a bunch of them were in the Berlin office together. There’s a few photos of that.

**[20:31] SPEAKER_01:** Yeah, I wasn’t there in the Berlin office for that, unfortunately. I don’t remember where I was, but yeah.

**[20:38] SPEAKER_00:** Did you do any mining at any point?

**[20:44] SPEAKER_01:** No, no. I was too nomadic.

**[20:48] SPEAKER_00:** You haven’t got the place to put the hardware.

**[20:50] SPEAKER_01:** Yes. I never had a storage place for it.

**[20:54] SPEAKER_00:** No, no. So then I guess, you know, through 2015, probably the next big piece was Devcon 1. Did you attend Devcon 1 in London?

**[21:03] SPEAKER_01:** Yeah, London. I slept in a closet.

**[21:05] SPEAKER_00:** That’s my big Harry Potter.

**[21:07] SPEAKER_01:** Yeah, that’s my memory from Devcon 1. I also gave a talk at Devcon 1.

**[21:14] SPEAKER_00:** Right.

**[21:15] SPEAKER_01:** Also on Ethereum.js, surprisingly.

**[21:17] SPEAKER_00:** Right. Something somebody pointed out recently was: if you look at the talks at Devcon 1, it’s like everything. There were so many different talks on so many different ideas and concepts, many of which foreshadowing things which are pretty big today, but probably nearly all of it was like 10 years too early.

**[21:39] SPEAKER_01:** Yeah, exactly. We had a lot of—there’s just so many layers that needed to be built. Obviously when you start off, you see this thing, “I can do this.” You don’t fully understand all the layers that need to be created for that. That’s a hard problem, though. And I think we’re still probably catching up to some of the original use cases that were envisioned.

**[22:03] SPEAKER_00:** I was mentioning this to someone last night and he was saying, “I think it’s maybe another five or 10 years from here before all of this stuff is in a viable kind of state.” It’s a lot more work than perhaps we envisaged at the start.

**[22:23] SPEAKER_01:** Yeah, it sounds so easy when you start, but yeah, it is hard.

**[22:27] SPEAKER_00:** Zsolt was saying, I think when he joined the Geth team, he was thinking this would be six months, 12 months kind of thing to work on. Slightly longer, I guess. And yeah, he asked Jeff, “So how long do you think for all of these pieces? AlethZero and Mix and Mist and Proof of Stake and sharding?” And Jeff said, “Maybe about seven months, or a little more.”

**[23:00] SPEAKER_01:** That’s hilarious.

**[23:01] SPEAKER_00:** So it was a little more.

**[23:03] SPEAKER_01:** Yeah, slightly. A little bit more.

**[23:06] SPEAKER_00:** I mean, I had that same delusion, because the very first thing I was doing was doing ARM Linux cross-builds of the C client to try and run it on my smartwatch, really with the thought that a light client was close, right? So just do the porting of the full clients, and then the LES support will drop in in a few months, and we can run a full node or a good-enough light node on a watch, or everywhere. It’s just like, “This is going to be everywhere,” right? Every computing device, every router—it’ll just pop in. It’ll just be another protocol like TCP/IP. It’ll be in the Linux kernel. Just be like another thing, another service.

**[23:50] SPEAKER_01:** It definitely has a ways to go before Linus merges that.

**[23:54] SPEAKER_00:** Yes, yes, I think. Yep.

**[23:58] SPEAKER_01:** So I would still like—I think it would be really cool though if someone built a filesystem interface for Ethereum where, you know, you could `cd` into a folder with all the blocks, and `cd` into a particular block and see a list of transactions, etc. Kind of like a Plan 9—

**[24:26] SPEAKER_00:** So you did a talk on this theme in Seattle. There was a meetup with yourselves—like Kenny Rowe, some of the Dappsis people. I think Kumavis as well.

**[24:41] SPEAKER_01:** Yeah, I think Kumavis was there. Juan from IPFS was definitely there. I think David Diaz was there.

**[24:49] SPEAKER_00:** Yeah, “Into the Merkle Forest” was one of the talks, and I think yours was like “Interplanetary OS.”

**[24:54] SPEAKER_01:** Yeah. Interplanetary Operating System.

**[24:58] SPEAKER_00:** There we go. There we go.

**[24:59] SPEAKER_01:** It was a fun talk.

**[25:01] SPEAKER_00:** That’s it. Merkle computing.

**[25:02] SPEAKER_01:** Yeah.

**[25:02] SPEAKER_00:** Can still happen.

**[25:04] SPEAKER_01:** Yeah, yeah. And there’s no technical reason you can’t do those things. It’s just, you know, layers. Layers need to be built.

**[25:15] SPEAKER_00:** Yeah, absolutely. So we’re getting the Oscars-style music coming on. I’m going to have to wrap up. I did intend to talk about eWASM and things, but maybe that’s for another time.

**[25:28] SPEAKER_01:** Sounds good.

**[25:29] SPEAKER_00:** Okay, so, yeah, we’re up to the end of 2015.

**[25:32] SPEAKER_01:** Nice.

**[25:33] SPEAKER_00:** Okay, thanks so much, man.

**[25:34] SPEAKER_01:** Yep. Thank you, bub. Oh, wow.