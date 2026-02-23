**[00:02] SPEAKER_00:** So, hello and welcome to ETHDenver 2026. I'm here recording for Early Days of Ethereum with Zsolt Felföldi. How do you pronounce your name?

**[00:14] SPEAKER_01:** Zsolt Felföldi.

**[00:16] SPEAKER_00:** There you go. Anyway, so yeah, I was working out when we recently reconnected at DevConnect and I was working it out that you're the third longest-serving person at the Ethereum Foundation. Right. You've got Vitalik and then Felix Lange and then you.

**[00:38] SPEAKER_01:** Yeah, I haven't really checked this fact yet, but honestly, yeah, it sounds great.

**[00:46] SPEAKER_00:** That's it. So, I mean, you're a very long-time member of the Geth team.

**[00:52] SPEAKER_01:** Yes.

**[00:52] SPEAKER_00:** But what were you doing before you started at the foundation? What was your background? How did you find your way into the blockchain world?

**[01:02] SPEAKER_01:** Well, before Ethereum, I was working on really different types of projects. I first started at a Hungarian software company, like a really classic software company. We actually sold software in boxes, put on a shelf, like floppy disks. Put in a box on a shelf and you can buy the software. So this type of classic software.

**[01:35] SPEAKER_00:** Five and a quarter inch floppies.

**[01:38] SPEAKER_01:** Yeah, actually three and a half.

**[01:42] SPEAKER_00:** Oh, okay. Three and a half. We're on to modern floppies.

**[01:46] SPEAKER_01:** Yeah, I started in '97, so maybe I was exaggerating a little. By that time it was mostly CDs. We still used a lot of floppies anyway. At that company I did things related to computer graphics. I wrote a ray tracing engine for some architectural software. And then I also did a lot of work on electronic circuit simulation and circuit design.

**[02:20] SPEAKER_00:** Right.

**[02:21] SPEAKER_01:** So yeah, really different things. It was around 2011 when I first heard about Bitcoin, and around 2012 when I started to realize that, as weird as it sounds, it really is probably a big thing. Actually, I first heard about Ethereum early 2014, a few months after the initial paper had been published.

**[02:53] SPEAKER_00:** Yeah.

**[02:54] SPEAKER_01:** And yeah, I started contributing I think around November and officially joined EF in March 2015.

**[03:05] SPEAKER_00:** And did you hear about it, do you think, through Dani and Viktor or some other way?

**[03:14] SPEAKER_01:** Well, I did hear about it from Dani and Viktor's friend circle.

**[03:22] SPEAKER_00:** Right.

**[03:22] SPEAKER_01:** Actually, I didn't know Viktor before. So I heard about this thing through one of Dani's friends and then Viktor was also in that wider circle, and he came to Hungary and said, "Oh, I'm already working on this." And then I started with my ideas and started to explain to him why this thing will probably never work. And he was like, "Okay, you seem to have a good understanding of this. Why don't you come to work?"

**[03:52] SPEAKER_00:** Right, right. And am I right in thinking that you said it was Swarm that you started with?

**[04:00] SPEAKER_01:** Well, yeah. So Swarm was part of this initial trinity of base technologies of Ethereum, supposed to be the storage layer for dapps. I mean, it was kind of a naive way of how people imagined decentralized applications back then, but honestly, it made sense at the time. I will say that nothing ever turned out exactly the way that people imagined it, but we are still making a lot of progress. So yeah, Swarm was how we initially imagined this storage layer for Ethereum. This project still has merits, but this whole problem space is just a bit more complex. But yeah, I started contributing to Swarm first, and actually, I wrote the first 500 lines of Swarm.

**[05:02] SPEAKER_00:** There you go. Yeah, I think if I remember rightly, Viktor mentioned around May 2014 was when he first heard about the trinity. This concept that you could have Ethereum as your compute and expensive database, Swarm as your decentralized storage, and then Whisper as your messaging. There was that famous diagram, right? There's a circle and the things coming in and Whisper going around the edge. But yeah, I guess it was Devcon 0 where Dani really presented a fleshed-out vision of what that decentralized storage was.

**[05:54] SPEAKER_01:** Yes, that's correct. I wasn't there at Devcon 0 yet. I heard about this idea even before I heard about Ethereum. So Dani already told me about this idea that he wants to do this kind of hash-based chunk storage. So it made total sense that he just pitched that.

**[06:14] SPEAKER_00:** That it could fit in.

**[06:16] SPEAKER_01:** Yeah, at the time it was a perfect fit. So he pitched this idea at Devcon 0, and when they accepted it and hired Dani, he called me and said—because he already knew that I knew of this project—he said, "Let's do it together."

**[06:38] SPEAKER_00:** There you go. And then you were hired into ethdev? I did have a date for that, but I've forgotten. I guess it was shortly after Devcon 0, right, that you started there?

**[06:51] SPEAKER_01:** Yes, correct.

**[06:53] SPEAKER_00:** Did you go to Berlin or Amsterdam? When did you first meet other people?

**[07:01] SPEAKER_01:** It was Amsterdam in February '15. That's where I met Jeffrey Wilcke, the creator of Go Ethereum, and the Go Ethereum team. Back then, I didn't say Geth because that abbreviation was invented later. So yeah, that's where I met the Go Ethereum people. I already had these contributions to Swarm, and it was kind of an implied thing that maybe I might be hired, but there was really no official hiring process back then. Jeff was this really laid-back guy, and he just said, "Okay man, I saw your contributions, let's talk sometime this week." And I waited the whole week and waited for some serious interview. It was a dream job for me, and I was really enthusiastic about this whole thing. Even though I felt that this whole initial design was a hard problem and I really couldn't imagine how it would scale, it was still worth starting it. I really wanted to get hired. The whole week I just waited. And at the end of the week, like the last half an hour before we all left for home, Jeff just said, "Oh yeah, man, I wanted to talk to you. You're hired." So, yeah, this is how the hiring process went back then.

**[08:50] SPEAKER_00:** Excellent. Well, that's easy. We like that. And that was before you went to Amsterdam? I assume you went to Amsterdam after you had been hired.

**[09:04] SPEAKER_01:** No, no, no, it happened in Amsterdam.

**[09:06] SPEAKER_00:** Oh, I see. So you were there unhired on site.

**[09:10] SPEAKER_01:** Yeah, Jeff agreed that if I bought my own plane ticket, I could stay at the Airbnb where the team stayed. I just worked with them and showed my contributions. So I went to Amsterdam unhired.

**[09:27] SPEAKER_00:** Right, right.

**[09:29] SPEAKER_01:** That plane ticket was a good investment.

**[09:31] SPEAKER_00:** Yeah. So did they not have office space at that point even?

**[09:36] SPEAKER_01:** Well, they did. Back then there was an Amsterdam office.

**[09:40] SPEAKER_00:** Right.

**[09:41] SPEAKER_01:** It was mostly for Jeff because Jeff lived in Amsterdam. But when Jeff left EF, or maybe before that, this office was closed. It was a really small office. Last time I checked, I think a dentist works there now. It doesn't exist, but it was really just a small place. Later, I went to Berlin a lot after I was hired. For the Geth team, work was somehow centered in Berlin.

**[10:24] SPEAKER_00:** Right, right. Because as well as Jeff, you've got Bas. He was another Amsterdam person, right? Bas van Kervel. But then maybe most of the other team members weren't in Amsterdam.

**[10:43] SPEAKER_01:** Yeah, no one else was in Amsterdam. Bas was there for a relatively short time. And Jeffrey also left after a while and started his own company to develop games or something.

**[11:01] SPEAKER_00:** Though he did have... EthLab was another one. Do you know anything about EthLab? Because when Jeff worked with JP Morgan to do Quorum, that was announced under the label EthLab.

**[11:18] SPEAKER_01:** I think I heard the name, but I didn't really know what it did. I knew that Jeff started working with JP Morgan at that time. Big banks really wanted to talk to us at every Devcon, and we were always invited to fancy dinners by main people. So banks really wanted to learn about the technology, and Jeff went for a while to work on Quorum, yes.

**[11:52] SPEAKER_00:** Yeah. Unless I can somehow get in contact with Jeff, I guess it's a little bit of a mystery what exactly EthLab was. Though I suspect it might be a little bit like Ethersphere, just sort of being a name, a banner for activities rather than a legal entity. And another thing I don't know there, but I suspect is, I don't think Jeff told Ming Chan that he was doing that stuff with JP Morgan. I suspect that he completely just did that on his own without any communication with Ming or with the EF. He just went and did it.

**[12:35] SPEAKER_01:** He never really told a lot to us about that. We knew that he was working with JP Morgan, but probably it's a big bank, and he had to sign non-disclosure agreements, so he probably couldn't share all the details.

**[12:51] SPEAKER_00:** No. I remember at some point, and I can't remember the context, him saying he found it interesting because the consensus for that was on-chain. The consensus for that was happening as smart contracts. So it was almost like this pluggable consensus that was pulled up into the app layer. He found the initial Quorum consensus quite interesting. It didn't last long, but I think Gav also was doing that sort of stuff on the C++ side. He did some Proof of Authority stuff before that happened on the Geth side with Clique. He actually made a different C++ client, so you've got eth, but he made another one that was called Fluidity or something, which was pulling all the libraries in the same way, but with a Proof of Authority consensus. That was one of the last things Gav did before he went out to Parity. So I think both him and Jeff were interested in how you formulate these pieces in different ways for those kinds of use cases. But yeah, Jeff left. I think it was probably very early in 2017. I did find a period, but it was certainly ahead of Devcon 3. Let me see if I can find the date.

**[14:42] SPEAKER_01:** I don't remember the exact date. Actually, maybe there wasn't even a really exact date when Jeff left, because basically a month after I joined, Péter Szilágyi joined, and he was the team lead for a very long time. Jeff basically kind of handed it over to Péter. For a while, he was officially still team lead, but not really. We hadn't seen him on the calls for a while.

**[15:14] SPEAKER_00:** No. The date I found there was February 2017, but I think I got that from GitHub. I think that was his final commit. But he probably tailed off a long time before that.

**[15:28] SPEAKER_01:** He already started focusing on other stuff, like this Quorum stuff and his own things, sometime in '16.

**[15:35] SPEAKER_00:** Yeah, he started a company called Grid Games with his brother, building a particular game. That also seems to have ceased. So he's now unknown, off in the world somewhere.

**[15:51] SPEAKER_01:** That's pretty much all I know about him. We tried to invite him a few times to come to some events and meet up, but I think for some reason he really had enough of, maybe not us, but things going on in the EF.

**[16:13] SPEAKER_00:** Yeah, I think that would be the case. When Ming came in, she both did legal tidy-up but also cut the spending a lot. You'd had the crowdsale in July, August, September 2014, but coming up to the mainnet release a year later, nearly all the money was gone. They spent it very fast.

**[16:40] SPEAKER_01:** So Devcon 1 was postponed because of that. We didn't really feel a lot of this. Actually, Jeff just said that now that the ether price is so low—I think the lowest point was 42 cents—

**[17:00] SPEAKER_00:** Yeah. And for a full year it didn't really move.

**[17:04] SPEAKER_01:** Jeff just said, "We all have to take a pay cut." But the pay cut was really just 10%, and I think maybe he took a bigger one. For us, it was really not that bad. The idea was that when the ether price reaches $2, then we do have some money to go forward. Then our salaries went back up. And that wasn't a lot of time. I don't really remember the exact price history, but I think the ether price reached something like $10 pretty soon.

**[17:56] SPEAKER_00:** Just around the start of 2016.

**[17:58] SPEAKER_01:** Yeah. And we went even a little bit higher. But then we had the DAO fork and the Shanghai attacks. Given how turbulent those times were, the market held up pretty well, and with a $10 ether price, we could survive further.

**[18:17] SPEAKER_00:** Yeah, that was quite a jump up. I heard that at the worst point there were only four months of runway left. That was how close it was to running out of money. But there were those big cuts which resulted in Gav and the C++ team being the main victims of those cuts. But then just into 2016... pardon me, I was hired in February 2016, the same time as Greg Colvin came in. Pavel was rehired; he was working through IMAP, working on EVMJIT, but that contract stopped and then he came back at that time as well. So this period through late 2015 to early 2016 was the absolute bottom of, "Are we even going to ship this thing? Are we going to run out of money before we get to mainnet?" Some of us were really coming in as backfill for that C++ team. And Devcon 1 had been canceled, but ConsenSys came in and actually paid for that. They said, "Hey, we'll mainly organize it so that the thing can happen." So that was the first public event. What are your memories of Devcon 1?

**[20:00] SPEAKER_01:** My subjective impression was that it was really amazing. Compared to today's Devcons, it was small. I think around 300, maybe less than a thousand people definitely. It was at a really prestigious venue, some old bank building on Threadneedle Street, right in the City of London. I really felt like, "Okay, now this is really a serious thing." Probably that was the reason why ConsenSys stepped in and funded the event so we could step up in terms of public appearance and appear as something really serious. I remember all the big banks having booths at Devcon 1.

**[20:56] SPEAKER_00:** Right? Yeah. And then Microsoft as headline sponsor. Recognition, right? Wow, Microsoft is interested and supportive. I think for a lot of people it was a real, "Wow, this is for real." Sadly, I could not afford to go. I watched the livestream. I was not quite in and working yet. I was an enthusiastic contributor.

**[21:34] SPEAKER_01:** Actually, it was the first time for me when I met a larger number of Ethereum people. I first met the Go Ethereum team in early '15, and I went to Amsterdam one more time, I think in May. But Devcon 1 was the place where I really realized how big this thing is, and that it's really not just about client developers. Even back then people presented about formal verification and all this stuff. I realized that this is really big, and everyone wants to be a part of it, at least a little bit.

**[22:22] SPEAKER_00:** Looking back at Devcon 1 videos, any kind of use case you could think of, there was somebody presenting about it, so early, more than 10 years ago. Many concepts which were probably massively too early to do, but seem more viable now, were presented. You had Nick Szabo as well doing a keynote.

**[22:49] SPEAKER_01:** Yeah, Nick Szabo was also there.

**[22:53] SPEAKER_00:** So was that maybe the first time that you'd met a number of the people from Berlin like Christoph Jentzsch and Lefteris Karapetsas, and maybe even Gav?

**[23:03] SPEAKER_01:** I think I met some of these people already in London. The first time I went to the Berlin office back then, it was the old office. So some people I met at Devcon 1, some people I met in Berlin.

**[23:22] SPEAKER_00:** So was Devcon 1 the first time that you'd been to do Ethereum things in London, or did you go to any London meetups or meet any of those comms people earlier?

**[23:41] SPEAKER_01:** I didn't go to any meetups in London before, but actually Viktor was in London at the time. I went to London around that time doing an event with my old Hungarian software company. We went to London to sell our software, as I was still working there.

**[24:17] SPEAKER_00:** Right.

**[24:17] SPEAKER_01:** And after that, I met up with Viktor and talked about Ethereum-related things.

**[24:21] SPEAKER_00:** Nice. From what he was describing, and looking at videos later, he had seen Gav talk in London in very early February. I think it was February 6th, almost immediately after they'd had the BTC Miami launch, Vitalik's first public talk, and Anthony Di Iorio's mansion where a lot of them met for the first time. Gav had been back in London a week after and did a talk there that Viktor had gone to. That was Viktor's first in-person meeting with any of them. And then Gav pulled him on board.

**[25:19] SPEAKER_01:** Those were the very early days, and I wasn't there. I first heard about Ethereum in March or April '14, which was around the presale. But yeah, I know that Gavin was one of the very early founders, and he wrote the yellow paper full of Greek letters.

**[25:51] SPEAKER_00:** Very confusing, yes. And the C++ client, of course. The first time I think I saw your name or was in contact with you was about the Light Client. I had been trying to get Ethereum ARM Linux cross-builds running on my smartwatch, and my thought was, "Get the thing running, and then this Light Client stuff is just starting, and scaling will be solved. We're going to be able to run these nodes on anything. You'll have them on your phone, smartwatch, router. They'll be in every operating system." So you were plunged right into that problem, right?

**[26:38] SPEAKER_01:** Yeah, when Jeff hired me, he put me on this project. He just said, "Okay, it's great that you contributed to Swarm, but if you join the Geth team, you will have to start working on the Light Client because it's a very important thing and hasn't been started yet." I felt really good about it. I felt like this is a big thing. Back then, it really felt like we just do these few things—have a working Light Client protocol and the whole trinity base layer—and then we're all good. It wasn't that easy, but those were the first steps. So I designed the LES protocol. In retrospect, it didn't make a lot of sense to build it over the devp2p layer because it wasn't easy to access from web browsers, and it was a Proof of Work based light client.

**[27:51] SPEAKER_00:** Right.

**[27:52] SPEAKER_01:** That project ended after a while, but I'm still very much into trustless chain access. That has usually been one of my focuses all the time. Right now, I'm working on something called the Trustless Execution Layer API, which is similar to the Beacon REST API but works on the execution layer and provides everything with proofs. I think this is where Ethereum really makes sense; if even normal users access chain data with proofs.

**[28:36] SPEAKER_00:** Right. And there was a project called Portal as well. Were you involved with Portal? That was a later Light Client.

**[28:44] SPEAKER_01:** No, I wasn't. Portal was Piper Merriam's brainchild. By the time we realized that LES was a nice first experiment but maybe not the best approach, he started something different that was UDP-based and used different topologies. It was kind of a DHT approach to storing the chain and the state. I think it's a bad thing that it's been completely canceled. Honestly, I never really believed that it would be an easily solvable problem to store the Merkle Patricia Trie of the state on a DHT, but for the chain data it made perfect sense. Maybe the state would have been possible with a lot of work. Piper told me a few times how he imagines to solve all the unsolvable problems, and it sounded good, but he made a lot of really hard assumptions about DHTs. By that time, I had already worked on Discovery V5, which we designed in 2016 in Berlin with Felix Lange.

**[30:20] SPEAKER_00:** Right.

**[30:20] SPEAKER_01:** I released the original version of that. I already knew that it's never easy to imagine a DHT that's efficiently formed and where all the nodes are working. But for the chain data...

**[30:37] SPEAKER_00:** Right.

**[30:37] SPEAKER_01:** Especially with EIP-4444, which lets the nodes running the main protocol forget the old chain history. It made perfect sense to at least put the chain history on a DHT. But it was an EF decision that it was discontinued at a point.

**[31:05] SPEAKER_00:** Well, I guess the thing is, Merkle Patricia Tries are not great for the number of accesses anyway. Let alone if you're making each of those steps over a networked DHT setup. There's so much transactional change complexity.

**[31:31] SPEAKER_01:** The state trie suffers from a lot of issues, especially the Merkle Patricia state trie. It's a huge data set that keeps changing all the time at completely random places, and it's not an easy task to distribute it. It's getting harder to even synchronize it between full nodes storing the entire stuff.

**[32:00] SPEAKER_00:** Do you think that proofs are going to be a magic silver bullet here? By having local proofs versus massively redundant state machines, do you think there's a path there?

**[32:19] SPEAKER_01:** Oh, no, it's not a silver bullet. I assume you mean what people call statelessness. It's a good thing, and it definitely allows a higher degree of scaling, but the state trie still has to be processed and maintained by someone. Especially if most nodes have no incentive to process it. If we are talking about 100x and 1000x scaling, even if we do state expiry—currently imagined in a way that we reset the state trie every year or something and have multiple state tries—it will be a huge infrastructural centralization issue.

**[33:21] SPEAKER_00:** Right.

**[33:21] SPEAKER_01:** This thing is not an unsolvable problem. The state as it works today unfortunately makes it really hard to do fundamental improvements, but people are considering different storage architectures. Of course, we have to keep existing contracts workable because that was our main promise from the beginning: that we will not just shut down anything and everything has 100% uptime. But it is a viable way to come up with more efficient storage methods as an opt-in alternative, which will over time be available for much less, and new contracts can be designed using those more efficient architectures.

**[34:28] SPEAKER_00:** Yeah, because Verkle trees seemed to be the first sort of thought on that, but then that's kind of come and gone, and maybe it's a binary tree.

**[34:37] SPEAKER_01:** Actually, it does either.

**[34:40] SPEAKER_00:** You don't think it's so important either?

**[34:42] SPEAKER_01:** Both are better than the Merkle Patricia Trie in some ways, but they don't solve this fundamental issue by themselves. The state is still a permanent key-value store, and in order to avoid it growing forever, there's all these ideas about state expiry, but it's still going to be a huge data set. The method of hashing or consensus protocol representation doesn't fundamentally change this. Verkle was supposed to provide more efficient Merkle proofs, but also somewhat more expensive state processing because of more expensive cryptography. Also, if I'm correct, it's not quantum secure. That was a thing that I always felt like, maybe it's not a good idea to start working on, and I just saw it canceled in front of my eyes.

**[36:00] SPEAKER_00:** I guess for running nodes in general, there's not a lot of incentive for people to run any kind of node software themselves unless they are a validator or running an exchange or a business and need a node back-end. The vision at the start was, "Well yeah, everyone will be running their own node." You had Mist on top of it for local apps, generating Swarm for the smart contracts, and it was almost like you wouldn't have server architecture because everyone's running their own server stack.

**[36:46] SPEAKER_01:** That did not happen. That's why we are also stuck with the JSON-RPC API, which doesn't provide proofs except for eth_getProof. It doesn't provide proofs for a lot of things because it was never meant to be used remotely. It was always imagined that it's used locally in a trusted setup on your own machine. And yeah, I remember all those good old days when I just synced up a full node, it was a few gigabytes of disk space, and ran Mist on top of it. It was magic, but unfortunately, it didn't scale.

**[37:26] SPEAKER_00:** No. At the Museum of Ethereum here, I've got laptops running Geth 1.3.6, so Homestead Geth, and I mined Homestead back to life. Any hard fork that happens doesn't go away, right? It doesn't disappear; it's just people don't associate economic value with it and it kind of gets abandoned. What I've done is first GPU and then CPU mined that Homestead difficulty down to the level that you can CPU mine it again. So I have Mist running on those so we can go and transact locally. We can send a transaction between those, and it should be possible to run AlethZero and AlethOne and Mix on that as well. ERC-20 tokens existed; you could have DAO tokens or Mistcoin at that time. But the assumption that people would run their own node and it would all be a self-sovereign local app stack certainly did not come to fruition.

**[38:54] SPEAKER_01:** Well, that's when the Light client came in, and we assumed we'd do the Light client and it would all be solved.

**[39:01] SPEAKER_00:** That's what I was thinking: "I've got a full node running on my smartwatch that works, I'll just wait for you and the other guys to sort out the Light Client, turn that on, and there we go."

**[39:15] SPEAKER_01:** Actually, the Light Client protocol worked fine. I just spent a really crazy amount of time figuring out how it could be incentivized in a truly decentralized way. I remember there was this idealism that we are almost done with everything, so we just have to find a proper way to incentivize things, not through buying tokens from companies, but in a truly decentralized way. Which is much harder because you have to somehow build decentralized trust and figure out market mechanisms that work without initial trust. I spent years with this and I think I came up with some nice theoretical models and a lot of complex code, but it was just the wrong approach, maybe at the wrong time. We were simply not there.

**[40:27] SPEAKER_00:** Because BitTorrent has obviously worked for distributing content for many years, but you do have this tragedy of the commons. The latest Hollywood movie that someone has ripped off will get shared around no problem because people want that. But things which are only of interest to a smaller number of people, without incentives, it's just a leeching problem.

**[41:00] SPEAKER_01:** Exactly.

**[41:00] SPEAKER_00:** Full node runners would contribute, they'd turn on LES as well, and help supply that. But the incentives and economics of that were not easy.

**[41:14] SPEAKER_01:** Actually, with BitTorrent, if you really want to use it, it often requires private trackers where you buy some priority access. So it's not completely decentralized, but it does work and is better than nothing. But for LES, it wasn't this easy. Downloading movies was an application everybody understood and used. With Ethereum, everyone felt the importance, but we were nowhere near a mature ecosystem. There just wasn't a big enough market for these services to work out in a market-based way. As we scale and accessing the whole data set becomes more difficult, at a certain point I think we are going to have something like what we imagined several years ago. I was right about everything except timing and specifics.

**[42:46] SPEAKER_00:** Yes. There are a number of things that seemed like they would be easy, quick, and obvious, and have taken many years. Like Proof of Stake; it was in the white paper with an assumption later in 2015 that it will happen within six months. It took eight years before it actually went live. And on storage, Filecoin's first white paper was in 2014, and IPFS was around before Ethereum as well. Whisper kind of went for a while, and now there's Waku. You've had Status driving a lot of those techs for years as well. Jarrad Hope and the team were doing an Android version of the Java client around the same time I was looking at smartwatches.

**[44:04] SPEAKER_01:** Jarrad Hope was also very eagerly waiting for a fully functional light client.

**[44:10] SPEAKER_00:** Yeah. Because they were building a kind of super app, a competitor to Mist really, wanting a container for running dapps sitting on top of a local client, having this completely self-sovereign server app stack. Not easy. I can't remember who was telling me that when they first saw MetaMask at Devcon 1—MetaMask was a grantee winner—they thought, "No, that's not what we want. We don't want some browser extension talking to a trusted endpoint. That's absolutely the opposite. What are these guys doing?" And then that became the standard flow, right?

**[45:15] SPEAKER_01:** Well, this is still an unsolved problem to access everything in a truly decentralized way, but I think we are getting there over time. Nothing is as simple as we initially imagined, and there's a time for everything. True decentralized infrastructure will be forced by scaling constraints. Things sometimes just don't happen if they are not forced by external factors. As long as it works conceptually in a lazy way to just connect MetaMask to Infura, until then, it remains the standard way.

**[46:12] SPEAKER_00:** Yeah. So I think I found two different talks of yours at Devcons talking mainly about the Light Client. Do you remember? Did you talk in London, or was Shanghai your first?

**[46:26] SPEAKER_01:** I talked in London, also Shanghai, and also in Cancun. The first two Devcons were mostly about the Light Client. The first release of the Light Client protocol was in '16. Later, I started to invent all the next chapters of decentralized technology. It was really naive of me, but I also had a project where I tried to make logs provable efficiently. That initial attempt was in 2017, and now I'm back at it. Now I have this trustless log index project. That old 2017 approach was just a more efficient way to organize Bloom filters, but it didn't solve the problem of Bloom filters not adapting to the number of events, and I never proposed putting it into consensus, which would have allowed actual trustless proofs through the chain.

**[47:58] SPEAKER_00:** Right.

**[47:58] SPEAKER_01:** That also proved to be a hard problem, but this is one of the things I presented in Cancun.

**[48:08] SPEAKER_00:** Right, right.

**[48:10] SPEAKER_01:** Also, I presented some ideas on state channels. Back then, we didn't have L2s the way we do now. Layer 2 just meant something happening off-chain, not necessarily another blockchain. I had ideas about individual nodes running their own blockchains and organizing off-chain calculations. It assumed a lot about how nodes would operate and probably would have never worked in retrospect.

**[48:53] SPEAKER_00:** We had state channels, and then we had Plasma, eventually coming into Optimistic Rollups, and then ZK later. Just many different attempts.

**[49:06] SPEAKER_01:** Hello.

**[49:07] SPEAKER_00:** See you, sir.

**[49:07] SPEAKER_01:** Great to see you.

**[49:10] SPEAKER_00:** There's an awful lot of learning, right? Ten years' worth of lots of people trying lots of different things. In terms of the Geth team, has that been similar over the years regarding size? Have you had larger and smaller amounts of people? Has it been a consistent flow through that time?

**[49:36] SPEAKER_01:** I would say it was pretty consistently around 10 people throughout all these years. Sometimes 8 or 9, sometimes 11 or 12, but really in this range. We did improve our internal processes during the years; now we do issue and pull request triages. The team was always small enough so that we didn't need a lot of processes. The team culture did obviously change with certain people coming and going, but I would say it was always a good culture. I always liked the Geth team. That's why I never really looked into moving to other teams or projects because I felt that the team is the best place to do meaningful things.

**[50:56] SPEAKER_00:** It's funny because from the very start of Ethereum, the intention was to have multiple clients. That was a very basic decision to say we want a separation between the specification and the implementation. We didn't want it to be like Bitcoin where you've got one codebase and there's no competition.

**[51:20] SPEAKER_01:** For Bitcoin's complexity that approach worked, but for Ethereum's complexity, I would say this was one of the best decisions. It also contributed to almost running out of money by the time we launched Mainnet, but I would say it was money well wasted.

**[51:40] SPEAKER_00:** Yes, I would agree it was not efficient, but the outcome was very much worthwhile.

**[51:48] SPEAKER_01:** When we switched to Proof of Stake, we again successfully applied this pattern by funding multiple Consensus Layer implementations and then testing every Execution Layer against every Consensus Layer, and running testnets with all five.

**[52:09] SPEAKER_00:** Are there five different primary consensus clients? I think it's five, and notably none of those were within the foundation either. They were all independent companies and teams. On the execution side, there have been a good number of alternative execution clients over the years. Starting with Parity and then Besu, Nethermind, and Erigon. How do you work with other teams in that kind of environment?

**[52:53] SPEAKER_01:** Now we have all the ACD calls and testing calls. We all have working clients all the time, so by default, we don't need to interact a lot. We have to interact when we are testing out new features, and there are proper forums for that. Some people keep more contacts outside the Geth team, and some turn inwards focusing on Geth issues. In the first years, communication was not really organized well; we just tried to figure things out. Now we have much better processes. It's also a much bigger challenge because there are so many more people. I realized this during the time we really started working on Proof of Stake. In 2017, the ether price went to several thousand dollars and the foundation had money to hire new teams and fund external teams. Until 2017, I mostly met non-Go Ethereum people only at Devcons.

**[54:37] SPEAKER_00:** Right.

**[54:37] SPEAKER_01:** Maybe those who lived in Berlin or cities where there were multiple people met more, but I mainly lived in Hungary and worked remotely. I mostly met people at Devcons. Until Devcon 4 in Prague, it was maybe 30 or 40 people. After every Devcon, we stood up at the main stage and did a group photo.

**[55:28] SPEAKER_00:** Oh yeah, yeah.

**[55:28] SPEAKER_01:** "We are the Ethereum Foundation."

**[55:30] SPEAKER_00:** Yes.

**[55:30] SPEAKER_01:** It was that many people. In '18, I was just shocked. "Who the hell are all these people?" It was the whole Ethereum Foundation. It became a much bigger challenge, but now we do have official forums, and I try to go to more events to stay connected.

**[56:00] SPEAKER_00:** Looking back to when you first started working on Ethereum, did you have any kind of thought or vision of what things might have looked like 10 years later? Has it worked out as you expected or differently?

**[56:25] SPEAKER_01:** I always had a lot of visions. Maybe I was too focused on visions sometimes, yeah. We all kind of have to imagine the future at every point, even though we know we can't imagine it exactly as it will turn out. It never turns out exactly the way we want, but we always have to have some direction and ideas of how things can go. Around 2017, I realized that scaling would not happen just with L1. I had these ideas about solving problems more efficiently with application-specific state channels rather than rollups. There was also this really great project...

**[57:34] SPEAKER_00:** Raiden.

**[57:35] SPEAKER_01:** Raiden. Yeah, thank you. They properly implemented the protocol and everything.

**[57:41] SPEAKER_00:** Yeah.

**[57:41] SPEAKER_01:** I think it always struggled with not many people using it. Transactions are expensive, but somehow we just missed an organizing force to really move to Layer 2 solutions back then.

**[58:10] SPEAKER_00:** Well, it was meant to be Lightning for Ethereum, right? That was the thought.

**[58:16] SPEAKER_01:** Yeah, it was pretty much that idea.

**[58:18] SPEAKER_00:** But then Lightning's kind of failed, so maybe it's not surprising if an Ethereum version of that hasn't really caught on. You've got routing issues. Channels seem to work perfectly for consistent static topographies. If you want to do merchant-to-merchant, channels work great.

**[58:46] SPEAKER_01:** Yeah. But opening those channels is still costly and nontrivial. I installed it and tried it, and I thought, "Okay, this is interesting," but I never really made a payment through Raiden because there was just no occasion where the other party really wanted a Raiden transfer.

**[59:14] SPEAKER_00:** No. Well, thank you very much. I think we can wrap it up there. Thanks for your time and thanks for all of your work on Geth over these very many years. Geth has always really been the backbone of Ethereum. New clients come and go, but Geth remains. So thank you.

**[59:39] SPEAKER_01:** Thank you for having me here.

**[59:40] SPEAKER_00:** Thank you so much.