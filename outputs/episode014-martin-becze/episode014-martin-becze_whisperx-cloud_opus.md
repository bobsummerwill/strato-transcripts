**[00:02] SPEAKER_01:** Test. Hello, can you hear me? Hello, hello. We're good. We're both good. Yeah, so hello, I'm Bob Summerwill here with Early Days of Ethereum, and talking to Martin Becze. Hello. Was it Becze? We say Becze? Becze? Becze? That works. Okay, so yeah, thanks for talking to us. You are a very OG OG. You're more OG than I am by a couple of years maybe even. So I mean, what were you doing prior to Ethereum that led you to Ethereum?

**[00:54] SPEAKER_00:** Yeah, that's a good question. So prior to Ethereum, I had gotten into Bitcoin for a bit. So I was actually at Occupy Wall Street and I set up the Bitcoin donation address for OWS and started doing some development, just regular web2 development. But as my projects developed, I started wondering how to decentralize them, as you naturally do if you've played around with crypto. I was highly influenced by Bitcoin and BitTorrent. And this is around the time Namecoin also, right?

**[01:34] SPEAKER_01:** Right, right.

**[01:35] SPEAKER_00:** So I was sort of like wanting to extend the concepts of Namecoin for my own project, which at the time was a geospatial map thing that displayed what was happening around you. And it was supposed to be federated, and I wanted to have a DNS system that we could resolve like a location to these servers. So I called it GoDNS. And looking at how Namecoin implemented it, it's like, ah, this is going to be a pain. I'm going to have to fork it, rebuild everything, get people to mine it. This is a lot of work. And then as you naturally do, you're like, well, this could just be generalized, right?

Yeah, so this is around the time that Vitalik had written some articles, I believe in Bitcoin Magazine.

**[02:18] SPEAKER_01:** Yeah, yeah, maybe not on DAOs and DACs?

**[02:22] SPEAKER_00:** Yes, I was very interested in that too. And I was following that work. And then yeah, I saw the white paper drop. And as soon as I saw the white paper drop, I was like, yeah, that's what I need. That makes a lot of sense. So then I started hacking on it because that was before any code was really operable, right? And I wanted to get my hands on it. I think Aleth Zero was up but it was really rough.

**[02:50] SPEAKER_01:** Yeah.

**[02:51] SPEAKER_00:** It was up on GitHub. And I was a JavaScript programmer, right? So I was like, well, I better implement this in JavaScript because that's what I know. And I really just wanted to get my hands on it and really understand how it worked, right?

**[03:41] SPEAKER_01:** Right, right. So yeah, we were just looking at some commit first commit dates. So we saw that Joseph Chow had a first commit on node Ethereum in February, and then we found March 2014 as probably the first commit on your side. So yeah, I mean the white paper had come out in November of the previous year, but the C++ and Go clients started in very late December. So yeah, a couple of months in, as you say, it's all going to be a bit rough. And it wasn't until April that you had the Yellow Paper. That came a little later. I think maybe April-ish was when Geth and cpp-ethereum were maybe kind of working, talking to each other.

**[04:30] SPEAKER_00:** Yes, yeah, yeah. I'll have to find the date. I did see a tweet of when that was, and I think it was Charles sent a transaction to Gav or the other way around.

**[04:42] SPEAKER_01:** Was it GavCoin maybe? Well, here's an interesting one. GavCoin came later. There was a meetup in London in October 2014 where both Gavin and Jeff were basically doing, "Hey, here's the status of Ethereum and roadmap," kind of thing. Like an hour-long big thorough thing. But what they did at that was Gavin had GavCoin, which was written in LLL. And Jeff had JeffCoin, which was written in Mutan. And they had an on-chain DEX. It was an on-chain order book, really clunky. Like, "Here, I'm offering three GavCoin for ten JeffCoin," or what have you. But they demonstrated it there and did a transaction to put an offer into the order book. And then Jeff's pressing the button to mine a block and...

**[05:35] SPEAKER_00:** That's really funny, yeah.

**[05:37] SPEAKER_01:** The exchange happened. But so I mean, were there many people where you were living that were regularly having meetups and being involved?

**[06:09] SPEAKER_00:** No, no, no, not at all. I was living in Indiana, so very rural. And yeah, it was completely — I only connected online, right? And I remained that way for some time. And it wasn't till, I don't know, a few months later. I was trying to get a job at Ripple.

**[06:40] SPEAKER_01:** Oh yes, Ripple also.

**[06:42] SPEAKER_00:** So they had a — I don't remember what it was called, but they were working on a VM.

**[06:47] SPEAKER_01:** Yeah, not — yeah, I can't remember. Codex or something? It wasn't — maybe, yeah.

**[06:54] SPEAKER_00:** Well, I was interested in that, and I had been working on implementing the Ethereum Virtual Machine in JavaScript. So they thought that was pretty cool and they flew me out for an interview at their office. And that is when I met Vitalik, because — not at Ripple. He just happened to be in San Francisco at the same time, right? And also Joseph Chow for the first time.

**[07:22] SPEAKER_01:** Do you know when that might have been?

**[07:24] SPEAKER_00:** Unfortunately no, I'm really bad with dates, but it was probably — it was definitely past March, like sometime in the summer, right? And then yeah, it's when I met up with everyone proper. And Vitalik's like, "No, just come work on Ethereum," right? So yeah, that's what I did.

**[07:48] SPEAKER_01:** So was that working for Ēth Dev as a contractor?

**[07:52] SPEAKER_00:** Yes, I was working for Ēth Dev as a contractor at that point.

**[07:57] SPEAKER_01:** Right, right. And Vitalik notoriously also nearly worked for Ripple but could not get his work permit. So yeah, the world might have looked very, very different if Vitalik had joined Ripple as an intern back then rather than sort of like —

**[08:18] SPEAKER_00:** They failed to get everyone. But if they had, Ripple also may have looked a lot different.

**[08:23] SPEAKER_01:** Yeah, yeah, yeah. Well, some of my very earliest meetups I went to at the start of 2014, it was like, "Here's a demo of Ripple," because it really was a lot less of a tribal setup, right? Like everyone was Bitcoiners because that's all there was. And then it's like, oh, there are these other things appearing. And oh yeah, it's a different form of consensus, here's a different flavor.

**[08:45] SPEAKER_00:** And I was actually interested in — there was an early version of Ripple made by this guy in Canada.

**[08:53] SPEAKER_01:** Ryan Fugger. Yes, yeah, who lives in Vancouver, same as me.

**[08:58] SPEAKER_00:** Oh, nice.

**[08:59] SPEAKER_01:** I've not met him ever though.

**[09:01] SPEAKER_00:** So I was interested in that version. You were able to — yeah, I'm not sure if I'm going to be able to actually recall, but you were able to — it was like debt. You were able to open debt lines to various people, and then debt would flow through the people.

**[09:16] SPEAKER_01:** That's right.

**[09:17] SPEAKER_00:** It would ripple through. And this was pre-blockchain. It was built in like PHP. They had a demo in PHP. I had signed up on it. I was playing around, I was offering my services on it, right? But yeah, then that's how I got interested in Ripple. But yeah, then they ended up moving in a slightly different direction.

**[09:43] SPEAKER_01:** Slightly different, yes. I think it was 2004, Ryan's work, yeah, around then. Very early, absolutely. So when you were then working full-time on Ethereum, did you have many collaborators? Were many people working on the code together with you?

**[09:58] SPEAKER_00:** So it was me and Joseph Chow to start with. And then Joseph Chow eventually went off and he started working on BTC Relay.

**[10:09] SPEAKER_01:** Yeah, I know. That's a very interesting project, yeah.

**[10:12] SPEAKER_00:** So he did that next. But yeah, there was a bunch of people coming in and out. Kumavis — yeah, Davis, right — helped out quite a bit. I was actually looking through the commits and saw he actually committed quite a few things. And then Alex Beregszaszi became involved. And there were several other people that I don't remember anymore, but those I think were the main characters back then.

**[10:49] SPEAKER_01:** Yeah. So I mean, for Kumavis, was that before he was doing MetaMask?

**[10:55] SPEAKER_00:** Yeah, yeah. So I met Kumavis at — it was a Mailchimp, may have been Mailchimp, at a party in SF or hangout. And he started just asking me a ton of questions about Ethereum, and we ended up chatting for a very long time. And then yeah, he was very proficient in JavaScript as well. So he started hacking a bit on EthereumJS, right?

**[11:23] SPEAKER_01:** Right, right. Something I think some people have asked, and I didn't know the answer to, is was there ever a fully syncing JavaScript node? Were you able to keep up at any point?

**[11:41] SPEAKER_00:** Yes. So yes, we did have a syncing full node that worked for a little bit. But yeah, it was difficult. It's still — it's — I think it's doable today. It's actually not that bad. I think the thing that didn't become our focus though, because it was just not a huge demand for that, right? Like Geth and everything else is going to go a lot faster. We were interested at the time in trying to embed a client in a browser.

**[12:17] SPEAKER_01:** Yeah, yeah. Which is now possible through the Helios project, right?

**[12:23] SPEAKER_00:** Yeah, so — what's that? I'm sorry, I don't know about Helios.

**[12:30] SPEAKER_01:** Oh, it's a light client from a16z.

**[12:34] SPEAKER_00:** Oh right, they funded it. It's in Rust, okay. And they compile it to Wasm, right? And it kind of cheats, right? It just makes RPC requests, RPCs, but it verifies the Merkle proofs and it verifies consensus, right? So yeah, it doesn't do the full thing, right. But since it — I would say it's a light client. It's definitely a light client where you have proof that the consensus is correct, and then you pull state that's verified from third-party RPCs.

**[13:18] SPEAKER_01:** Right, yeah, yeah, yeah. And so you attended DevCon Zero in Berlin in November 2014?

**[13:28] SPEAKER_00:** Yes.

**[13:29] SPEAKER_01:** Yeah, so how was that?

**[13:32] SPEAKER_00:** That was really cool. It was my first time — not quite leaving the U.S. It was my first time flying over the ocean, right? I'd been to Canada.

**[13:42] SPEAKER_01:** Oh yes, nice.

**[13:43] SPEAKER_00:** Right, it's like Niagara Falls and stuff. But yeah, so first time in Europe. So it's super exciting. And yeah, I stayed in a big Airbnb with Juan Benet and Vitalik, right? I think Vlad was in the Airbnb as well. It was super cool, just seeing everyone for the first time, right? Meet up and yeah.

**[14:06] SPEAKER_01:** Because there were a good chunk of people there. I was trying to count. I think 40 to 50 is about the number that were there. Pretty much everyone who was working on things. I was looking through — I don't think I could spot really anyone who was still involved who wasn't there, with maybe the — yeah, Anthony Di Iorio wasn't there, and he didn't technically leave until the end of 2015, but he was little involved.

**[14:40] SPEAKER_00:** Yeah, I don't have — well, actually, I had a small contact with Anthony, but yeah, I never met him. I don't think I've ever met him in real life. I know what he looks like though, right.

**[14:51] SPEAKER_01:** Yeah, I have a few times. Hoping to talk to him soon.

**[14:55] SPEAKER_00:** Oh nice.

**[14:56] SPEAKER_01:** But yeah, from there — there are missing videos from DevCon Zero which I'm still looking for. There's ten of them on the playlist on YouTube. There's one further which didn't go in the playlist but is on there, but there seemed to be about ten missing sessions in there. Can you remember — did you talk at DevCon Zero? Was there —

**[15:18] SPEAKER_00:** I did, yeah. And I gave a big presentation — all big — I had my slides printed off. I gave a talk on the EthereumJS, right, and how I architected it.

**[15:35] SPEAKER_01:** Yeah, so I think that video is currently lost, and I hope to recover it. May have never got recorded, I don't know.

**[15:42] SPEAKER_00:** I think they all did.

**[15:43] SPEAKER_01:** Oh, okay. And the other thing Taylor was saying was that he did interviews with nearly everyone as well. Can you remember? Did you talk to Taylor? Did he go off into some back room and do an interview with him?

**[16:00] SPEAKER_00:** I do not remember that, no. I remember Taylor though, yeah. And he's still around.

**[16:07] SPEAKER_01:** Absolutely, yeah. So yeah, he was one of the earlier interviewees. Yeah, I've known Taylor a long time. And it was funny because he had the Water Cooler channel, the Skype Water Cooler.

**[16:18] SPEAKER_00:** Yes.

**[16:19] SPEAKER_01:** So when I joined the EF, I joined the EF channel and the Water Cooler, and I thought they were both foundation things. But it wasn't — it's basically Taylor's troll room. So then you've got a bunch of sort of ex or people outside. It was a broader group. Skype are about to delete all their data, by the way.

**[16:38] SPEAKER_00:** Oh, okay.

**[16:39] SPEAKER_01:** So but you can request a download. So if you want to do that, do it fast.

**[16:44] SPEAKER_00:** I don't have access to my Skype account anymore.

**[16:47] SPEAKER_01:** Well, I didn't — I mean, you can just log in and do a password recovery thing and then you can request it. Anyway, so I'm hoping to recover mine and maybe there's some interesting tidbits in that Water Cooler channel.

**[16:59] SPEAKER_00:** Yeah, definitely, that'd be interesting.

**[17:02] SPEAKER_01:** Yeah. So then, I guess on into 2015 and through all the POCs, were you generally just continuing to maintain that as new features and changes came in through the POCs?

**[17:24] SPEAKER_00:** Yeah. So we did a lot — a lot of time was spent on the virtual machine, as you can imagine. That's sort of one of the larger components. And I also was working on networking, right? So EthereumJS was a smaller team than everyone else. So yeah, we always lagged behind a bit. But the networking protocols, RLPx, went through several iterations. And then the virtual machine went through several iterations. We contributed to the testing, right? And yeah, that was our main focus.

**[18:14] SPEAKER_01:** Right. So yeah, more about tooling use versus straight consensus client, because there are many EthereumJS repos and components.

**[18:29] SPEAKER_00:** Yeah, so the original architecture — and it doesn't exist this way anymore, it's been merged into a monorepo — but originally it was a bunch of small modules.

**[18:38] SPEAKER_01:** It still is a bunch of small modules, but it's a monorepo.

**[18:41] SPEAKER_00:** Yes, it's much more sensible, yes. But at that time, yeah, small repos for everything. And the focus was on building reusable components. So the most widely used component or most widely used module was ethereumjs-tx, right? Used for creating and signing transactions, right? For wallets such as MetaMask, would use that internally to construct and sign a transaction. And then yeah, we had everything broken out. So RLP for serialization, the networking libraries, the virtual machine proper, some of the higher-level ones. And yeah, so the fun thing about EthereumJS was that I tried to make these modules very approachable and easy to use, right? So people did stuff like write a DHT scraper with it to see all the nodes, right, what version they're running, and things of that nature.

**[19:53] SPEAKER_01:** Yeah, great, great. So do you have memories of launch day? Where were you on that day? How did that play out?

**[20:02] SPEAKER_00:** Yeah, that was just like — I think I was hacking away somewhere. I don't think I was anywhere special though. It was just sort of like another day for me, right.

**[20:15] SPEAKER_01:** You weren't in a room with people, watching the screen with bated breath?

**[20:21] SPEAKER_00:** No, no, I wasn't. It wasn't really — yeah, I was just like, yeah, I'll just keep coding, type of thing.

**[20:27] SPEAKER_01:** Because there were a bunch of them in the Berlin office together. There's a few photos of that.

**[20:33] SPEAKER_00:** Yeah, I wasn't there in the Berlin office for that, unfortunately. I don't remember where I was. But yeah. Did you do any mining at any point? No, no. I was too nomadic. You got no place to put the hardware?

**[20:49] SPEAKER_01:** Yes.

**[20:50] SPEAKER_00:** I never had a storage place for — no, no.

**[20:53] SPEAKER_01:** So then I guess through 2015, probably the next big piece was DevCon One. Did you attend DevCon One in London?

**[21:02] SPEAKER_00:** Yeah, yeah. London. I slept in a closet. That's my big Harry Potter memory from DevCon One. Yep. So I gave a talk at DevCon One.

**[21:13] SPEAKER_01:** Right, also on EthereumJS, right? Surprisingly, right. So I mean, something somebody pointed out recently was like, if you look at the talks at DevCon One, it's like everything — like there were so many different talks on so many different ideas and concepts, many of which foreshadowing things which are pretty big today. But probably nearly all of it was like ten years too early.

**[21:38] SPEAKER_00:** Yeah, exactly. Yeah, we had — there's just so many layers that needed to be built. Obviously when you start off you see this thing, "I can do this," you don't fully understand all the layers that need to be created for that. That's a hard problem though. And I think we're still probably catching up to some of the original use cases that were envisioned.

**[22:04] SPEAKER_01:** I was mentioning this to someone last night and he was saying, I think it's maybe another five or ten years from here before all of this stuff is in a viable kind of state.

**[22:14] SPEAKER_00:** Yeah, it's a lot more work than perhaps we envisaged at the start.

**[22:18] SPEAKER_01:** Yeah, it sounds so easy when you start, but yeah, it is hard. Zsolt was saying, I think when he joined the Geth team, he was thinking this would be six months, twelve months kind of thing to work on. Slightly longer, I guess. And yeah, he asked Jeff, "So how long do you think for all of these pieces?" Like Aleth Zero and Mix and Mist and proof of stake and sharding. And Jeff said, "Maybe about seven months or a little more."

**[22:52] SPEAKER_00:** That's hilarious.

**[22:54] SPEAKER_01:** So it was a little more, yeah, slightly. A little bit more. Yeah, I mean, I had that same delusion because the very first thing I was doing was doing ARM Linux cross-builds of the C++ client to try and run it on my smartwatch. Okay, really? With the thought that like, the client was close, right? So we'll just do the porting of the full clients and then the LES support will drop in in a few months and we can run a full node or a good enough light-load node on a watch or everywhere. It's just like, this is going to be everywhere, right? Every computing device, every router, it'll just pop in. It'll just be another protocol like TCP/IP. It'll be in the Linux kernel, it'll just be like another thing, another service.

**[23:40] SPEAKER_00:** Hey, it definitely has a ways to go before Linus merges that.

**[23:44] SPEAKER_01:** Yes, yes, I think, yeah.

**[24:00] SPEAKER_00:** I would — I think it would be really cool though if someone built a filesystem interface for Ethereum, where you could cd into a folder with all the blocks and ls into a particular block and see a list of transactions, etc. Kind of like a Plan Nine — like —

**[24:22] SPEAKER_01:** So you did a talk on this theme in Seattle. There was a meetup with yourselves, like Kenny Rowe, some of the DAPPS-is people, I think Kumavis as well.

**[24:39] SPEAKER_00:** Yeah, I think Kumavis was there. Juan from IPFS was definitely there.

**[24:46] SPEAKER_01:** Yes, he was. I think David Diaz was there. "Into the Merkle Forest" was one of the talks. And I think yours was like "Planetary OS."

**[24:56] SPEAKER_00:** Yeah, it was Interplanetary Operating System. There we go. It was a fun talk. That's it. Miracle computing. Yeah, can still happen. Yeah. And there's no technical reason you can't do those things. It's just layers need to be built.

**[25:14] SPEAKER_01:** Yeah, absolutely. So we're getting the Oscars-style music coming on. I'm going to have to wrap up. All right. I did intend to talk about eWASM and things, but maybe that's for another time.

**[25:28] SPEAKER_00:** Sounds good.

**[25:29] SPEAKER_01:** Okay, so yeah, we're up to the end of 2015. Nice. Okay, thanks so much, man.

**[25:34] SPEAKER_00:** Yep, thank you, Bob.