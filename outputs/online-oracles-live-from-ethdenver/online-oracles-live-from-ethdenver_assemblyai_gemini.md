**[00:02] SPEAKER_00:** So, hello and welcome to ETHDenver 2026. So here recording for Early Days of Ethereum with Zsolt Felföldi. How do you pronounce your name?

**[00:14] SPEAKER_01:** Zsolt Felföldi.

**[00:16] SPEAKER_00:** There you go. Anyway, so yeah, I was working out when we recently reconnected at Devconnect, and I was working out that you're the third longest person at the Ethereum Foundation. Right? You've got Vitalik, and then Felix, and then you.

**[00:38] SPEAKER_01:** Yeah, I haven't really checked this fact yet, but honestly, yeah, it sounds great.

**[00:46] SPEAKER_00:** That's it. So, I mean, you're a very long-time member of the Geth team.

**[00:52] SPEAKER_01:** Yes.

**[00:52] SPEAKER_00:** But what were you doing before you started at the Foundation? What was your background? How did you find your way into the blockchain world?

**[01:02] SPEAKER_01:** Well, before Ethereum, I was working on really different types of projects. So I first started at a Hungarian software company, like a really classic software company. We actually sold software in boxes, put on a shelf, like floppy disks inside a box on a shelf, and you can buy the software. So, like this type of classic software.

**[01:35] SPEAKER_00:** Five and a quarter-inch floppies.

**[01:38] SPEAKER_01:** Yeah, actually three and a half.

**[01:42] SPEAKER_00:** Oh, okay. Three and a half. We're on to modern floppies.

**[01:46] SPEAKER_01:** Yeah, but I started in '97, so maybe I was exaggerating a little. By that time it was mostly CDs. We still used a lot of floppies anyway. At that company, I did things related first to computer graphics. I wrote a ray-tracing engine for some architectural software. And then I also did a lot of work on electronic circuit simulation and circuit design.

**[02:20] SPEAKER_00:** Right.

**[02:21] SPEAKER_01:** So yeah, really different things. It was around 2011 when I first heard about Bitcoin, and around 2012 when I started to realize that, as weird as it sounds, it really is probably a big thing. Actually, I first heard about Ethereum early 2014, a few months after the initial paper had been published.

**[02:53] SPEAKER_00:** Yeah.

**[02:54] SPEAKER_01:** And yeah, I started contributing, I think, around November, and officially joined the EF in March 2015. So, yeah.

**[03:05] SPEAKER_00:** And did you hear about it through Dani and Viktor, or some other way?

**[03:14] SPEAKER_01:** Well, I did hear about it from Dani and Viktor's friend circle.

**[03:22] SPEAKER_00:** Right.

**[03:22] SPEAKER_01:** But Viktor was already... actually, I didn't know Viktor before. I heard about this thing through one of Dani's friends, and then Viktor was also in that wider circle. He came to Hungary and said, "Oh, I'm already working on this." And then I started with my ideas and started to explain to him why this thing would probably never work. And he was like, "Okay, you seem to have a good understanding of this. Why don't you come to work?"

**[03:52] SPEAKER_00:** Right, right. And was I right in thinking that you said it was Swarm that you started with?

**[04:00] SPEAKER_01:** Well, yeah. Swarm was part of this initial trinity of base technologies of Ethereum. Swarm was supposed to be the storage layer for dapps. I mean, it was kind of a naive way of how people imagined decentralized applications back then. But honestly, it made sense at the time. I will say that nothing ever turned out exactly the way that people imagined it, but we are still making a lot of progress. Swarm was how we initially imagined this storage layer for Ethereum. This project still has merits, but this whole problem space is just a bit more complex. So I started contributing to Swarm first, and actually I wrote the first 500 lines of Swarm.

**[05:02] SPEAKER_00:** There you go. Yeah, I think if I remember rightly, Viktor mentioned around May 2014 was when he first heard this trinity concept—that you could have Ethereum as your compute and expensive database, Swarm as your decentralized storage, and then Whisper as your messaging. That famous diagram, right, with the circle and the things coming in, and Whisper going around the edge. But yeah, I guess it was Devcon 0 where Dani really presented a fleshed-out vision of what that decentralized storage could be.

**[05:54] SPEAKER_01:** Yes, that's correct. I wasn't there at Devcon 0 yet. I heard about this idea even before I heard about Ethereum. Dani already told me about this idea that he wanted to do this kind of hash-based chunk storage. It made total sense that he pitched that.

**[06:14] SPEAKER_00:** That can fit in.

**[06:16] SPEAKER_01:** Yeah, at the time it was a perfect fit. So he pitched this idea at Devcon 0, and when they accepted it and hired Dani, he called me and said—because he already knew that I knew of this project—"Let's do it together."

**[06:38] SPEAKER_00:** There you go. And then, you were hired into ethdev? I did have a date for that, which I've forgotten. I guess it was shortly after Devcon 0 that you started there.

**[06:51] SPEAKER_01:** Yes, correct.

**[06:53] SPEAKER_00:** Did you go to Berlin or Amsterdam? When did you first meet other people?

**[07:01] SPEAKER_01:** It was Amsterdam in February 2015.

**[07:05] SPEAKER_00:** Right.

**[07:06] SPEAKER_01:** That's where I met Jeffrey Wilcke, the creator of Go Ethereum, and the Go Ethereum team. Back then, I didn't say Geth, because that abbreviation was invented later. That's where I met the Go Ethereum people. I already had these contributions to Swarm, and it was kind of an implied thing that maybe I might be hired, but there was really no official hiring process back then. Jeff was this really laid-back guy, and he just said, "Okay, man, I saw your contributions, and let's talk sometime this week." I waited the whole week and waited for some serious interview; it was a dream job for me. I was really enthusiastic about this whole thing. Even though I felt that this initial design... I really couldn't imagine how it would scale, and it is a hard problem. It was still worth starting, and I was really enthusiastic and really wanted to get hired. The whole week I just waited. And at the end of the week, like the last half an hour before we all left for home, Jeff just said, "Oh yeah, man, I wanted to talk to you. You're hired." Okay, that's a good talk. So, this is how the hiring process went back then.

**[08:50] SPEAKER_00:** Excellent. Well, that's easy. We like that. So that was before you went to Amsterdam, I assume. You went to Amsterdam after you had been hired.

**[09:04] SPEAKER_01:** No, no, no, it happened in Amsterdam.

**[09:06] SPEAKER_00:** Oh, I see. So you were there unhired, on site.

**[09:10] SPEAKER_01:** Yeah, Jeff agreed that if I bought my own plane ticket, I could stay at the Airbnb where the team stayed. I just worked with them and showed my contributions. So I went to Amsterdam unhired.

**[09:27] SPEAKER_00:** Right, right.

**[09:29] SPEAKER_01:** That plane ticket was a good investment.

**[09:31] SPEAKER_00:** Yeah. Did they not have office space at that point even?

**[09:36] SPEAKER_01:** They did, actually. Back then there was an Amsterdam office.

**[09:40] SPEAKER_00:** Right.

**[09:41] SPEAKER_01:** It was mostly for Jeff because Jeff lived in Amsterdam. But when Jeff left the EF, or maybe before that, I'm not sure exactly, this office was closed. It was a really small office. Last time I checked, I think a dentist works there now. So it doesn't exist anymore, but it was just a small place. Later, I went to Berlin a lot after I was hired. For the Geth team, it was really centered in Berlin.

**[10:24] SPEAKER_00:** Right, right. Because, as well as Jeff, you've got Bas, right? Bas van Kervel was another Amsterdam person. But maybe most of the other team members weren't in Amsterdam.

**[10:43] SPEAKER_01:** Yeah, no one else was in Amsterdam. Bas was there for a relatively short time. Jeffrey also left after a while and started his own company, developed games or something.

**[11:01] SPEAKER_00:** Though he did have... oh, EthLab was another one. Do you know anything about EthLab? Because when Jeff worked with JP Morgan to do Quorum, that was announced under the label EthLab.

**[11:18] SPEAKER_01:** I think I heard the name, but I didn't really know what it did. I knew that Jeff started working with JP Morgan. Around that time, big banks really wanted to talk to us at every Devcon, and we were always invited to fancy dinners by main people. Banks really wanted to learn about the technology. So Jeff went for a while to work on Quorum.

**[11:52] SPEAKER_00:** Yeah, unless I can somehow get in contact with Jeff, I guess it's a little bit of a mystery what exactly EthLab was. Though I suspect it might be a little bit like Ethersphere, just sort of a name or banner for activities rather than a legal entity. Another thing I don't know for sure, but I suspect, is that I don't think Jeff told Ming Chan that he was doing that stuff with JP Morgan. I suspect he completely just did that on his own without any communication with Ming or with the EF.

**[12:35] SPEAKER_01:** He never really told a lot to us about that. We knew he was working with JP Morgan, but because it's a big bank, he probably had to sign a non-disclosure agreement, so he just couldn't share all the details.

**[12:51] SPEAKER_00:** No, no. I remember at some point, and I can't remember the context, him saying he found it interesting because the consensus for that was on-chain. Like, the consensus for that was happening as smart contracts. So it was kind of almost like this pluggable consensus, pulled up into the app layer. He found the initial Quorum consensus quite interesting. It didn't last long, but I think Gav also was doing that sort of stuff on the C++ side. He did some proof-of-authority stuff before that happened on the Geth side, before Clique. Actually, he made a different C++ client, so you've got C++ Ethereum, but he made another one called Fluidity or something, which was pulling all the libraries in the same, but with a proof-of-authority consensus. That was one of the last things he did before he went out to Parity. Both him and Jeff were interested in how you could formulate these pieces in different ways for those kinds of use cases. But yeah, he left. I think it was probably very early in 2017. I did find a period, but it was certainly ahead of Devcon 3. Let me see if I can find the date.

**[14:42] SPEAKER_01:** I don't remember the exact date. Actually, maybe there wasn't even an exact date when Jeff left, because basically a month after I joined, Péter Szilágyi joined, and he was the team lead for a very long time. So Jeff basically kind of handed it over to Péter. For a while, Jeff was officially still team lead, but not really. We hadn't seen him on the calls for a while.

**[15:14] SPEAKER_00:** The date I found was February 2017. But I think I got that from GitHub. That was like his final commit. But he probably tailed off a long time before that.

**[15:28] SPEAKER_01:** He already started focusing on other stuff, like this Quorum stuff and his own things, sometime in 2016.

**[15:35] SPEAKER_00:** Yeah, so he started a company called Grid Games with his brother, building a particular game, though that also seems to have ceased. He's unknown, off in the world somewhere.

**[15:51] SPEAKER_01:** That's pretty much all I know about him. We tried to invite him a few times to come to some events and meet up. But for some reason, he really had enough of... maybe not us, but things going on at the EF.

**[16:13] SPEAKER_00:** Yeah, I think that would be the case. When Ming came in, she both did a legal tidy-up but also cut the spending a lot. You'd had the crowdsale in July, August, September 2014, but coming up to the mainnet release a year later, nearly all the money was gone. They spent it very fast.

**[16:40] SPEAKER_01:** Devcon 1 was postponed because of that, but we didn't really feel a lot of this. Jeff just said that now that the ether price is so low—actually, I think the lowest point was 42 cents.

**[17:00] SPEAKER_00:** Yeah. And for a full year, it didn't really move.

**[17:04] SPEAKER_01:** And Jeff just said that we all have to take a pay cut. But the pay cut was really just 10%, and I think maybe he took a bigger one. So for us, it was really not that bad. The idea was that when the ether price reaches $2, then we would go back to our forward salaries. And that wasn't a lot of time. I don't really remember the price history, and maybe it's not the most important thing, but I think the ether price reached something like $10 pretty soon.

**[17:56] SPEAKER_00:** Just at the start of 2016.

**[17:58] SPEAKER_01:** Yeah, and it went even a little bit higher. But then we had the DAO fork and the Shanghai attacks. Given how turbulent those times were, the market held pretty well, and with a $10 ether price, we could survive further.

**[18:17] SPEAKER_00:** Yeah, that was quite a jump up. I heard that at the worst point, there was only four months of runway left. That was how close it was to running out of money. There were those big cuts which resulted in Gav and the C++ team being the main victims of those cuts. But then, just into 2016... pardon me, so I was hired in February 2016, same time as Greg Colvin came in, and also Paweł Bylica was rehired. He was working through EVM JIT, but that contract had stopped. Then he came back at that time as well. So it was this period through late 2015 to early 2016 that was the absolute bottom of, "Are we even going to ship this thing? Are we going to run out of money before we get to mainnet?" But then, some of us were really coming in as backfill for that C++ team. Devcon 1 was sort of... you were mentioning it had gotten canceled, but then ConsenSys came in and actually paid for that and said, "Hey, we'll organize it so the thing can happen." So that was the first big public event. What are your memories of Devcon 1?

**[20:00] SPEAKER_01:** My subjective impression was that it was really amazing. Compared to today's Devcon, it was small, I think 300 something people maybe. I'm not sure, but less than a thousand definitely. It was a really prestigious venue, some old bank building on Threadneedle Street, in the City of London. I really felt like, "Okay, so now this is really a serious thing." Probably that was the reason why ConsenSys stepped in and funded the event, so we really could step up in terms of public appearance and appear as something serious. I remember all the big banks having booths at Devcon 1, right?

**[20:58] SPEAKER_00:** Yeah. And then Microsoft as a headline sponsor. It's like, "Wow. Recognition, right?" You're like, "Wow, Microsoft are interested and supportive." I think for a lot of people it was a real, "Wow, this is for real." Sadly, I could not afford to go. I watched the livestream. I was not quite in and working yet. I was an enthusiastic contributor, but...

**[21:34] SPEAKER_01:** It was also the first time for me when I met a larger number of Ethereum people. I first met the Go Ethereum team in early 2015. I went to Amsterdam one more time, I think in May. But Devcon 1 was the place where I really realized how big this thing is. It's really not just about client developers; even back then people presented about formal verification and all this stuff. I realized this is really big, and probably everyone wants to be a part of it.

**[22:22] SPEAKER_00:** Looking back at Devcon 1 videos, it's like any kind of use case you could think of, there was somebody presenting about it, more than 10 years ago. Many concepts which were probably massively too early to do, but maybe you can do them more now, seemed to be presented. You had Nick Szabo as well, doing a keynote.

**[22:49] SPEAKER_01:** Yeah, Nick Szabo was also there.

**[22:53] SPEAKER_00:** So was that maybe the first time that you'd met a number of the people in Berlin, like Christoph Jentzsch and Lefteris Karapetsas, and maybe even Gav?

**[23:03] SPEAKER_01:** I think I met some of these people already in London, and the first time I went to the Berlin office. Back then it was the old office. So some people I met at Devcon 1, some people I met in Berlin.

**[23:22] SPEAKER_00:** Was Devcon 1 the first time that you'd been to do Ethereum things in London, or did you go to any London meetups or meet any of those people earlier?

**[23:41] SPEAKER_01:** I didn't go to any meetups in London before, but actually I did... Viktor was in London at the time, and I went to London around that time doing some event with my old Hungarian software company.

**[24:10] SPEAKER_00:** Right.

**[24:10] SPEAKER_01:** We went to London to sell our software, as I was still working there.

**[24:17] SPEAKER_00:** Right.

**[24:17] SPEAKER_01:** And after that, I met up with Viktor and talked about Ethereum-related things.

**[24:21] SPEAKER_00:** Nice. From what he was describing, and then looking at videos later, he had seen Gav talk in London in very early February, I think February 6th. Almost immediately after they'd had the BTC Miami launch, Vitalik's first public talk, and Anthony Di Iorio's mansion where a lot of them met for the first time. Gav had been back in London a week after and did a talk there that Viktor had gone to. That was Viktor's first in-person meeting with any of them. And then Gav had pulled him on board.

**[25:19] SPEAKER_01:** Yeah, so those are the very early days I wasn't there for. When I first heard about Ethereum, that was March or April 2014. I first heard about the presale, and that's where I first heard about this thing. But I know that Gavin was one of the very early founders of this, and he wrote the Yellow Paper full of Greek letters.

**[25:51] SPEAKER_00:** Very confusing. Yeah. And the C++ client, of course. So the first time I think I saw your name or was in contact with you was about the light client. I'd been trying to get Ethereum ARM Linux cross-builds running on my smartwatch. My thought there was get the thing running, and then this light client stuff is just starting, and scaling will be solved, right? We're going to be able to run these nodes on anything. You'll have them on your phone, smartwatch, router. They'll be in every operating system. It will solve scaling and lightness. So you were plunged right into that problem, right?

**[26:38] SPEAKER_01:** Yeah. When Jeff hired me, he put me on this project. He said it was great that I contributed to Swarm, but if I join the Geth team, I will have to start working on the light client because it's a very important thing and it hadn't been started yet. I felt really good about it. I also felt like this is a big thing. Back then, it really felt like we do these few things, we have a working light client protocol and the whole trinity of the base layer, and then we're all good. It wasn't that easy, but still, those were the first steps. So I designed the LES protocol. In retrospect, it didn't make a lot of sense to build it over the devp2p layer because it wasn't easy to access from web browsers, and also it was a proof-of-work-based light client.

**[27:51] SPEAKER_00:** Right.

**[27:52] SPEAKER_01:** That project ended after a while, but I'm still very much into trustless chain access. That has usually been one of my focuses all the time. Right now, I'm also working on something called the trustless Execution Layer API, which is similar to the Beacon REST API but works on the execution layer and provides everything with proofs. I'm still very much into this because I think this is where Ethereum really makes sense, if even normal users access chain data with proofs.

**[28:36] SPEAKER_00:** Right, right. And there was a project called Portal as well. Were you involved with Portal? That was a later kind of light client.

**[28:44] SPEAKER_01:** No, I wasn't. Portal was Piper Merriam's brainchild. By the time we kind of realized that LES was a nice first experiment but maybe not the best approach, he started something different that was UDP-based and used different topologies. It was kind of a DHT approach to storing the chain and the state. I think it's a bad thing that it's been completely canceled. To be honest, I never really believed that it would be an easily solvable problem to store the Merkle Patricia Trie of the state on a DHT, but for the chain data it made perfect sense. Maybe the state would have been possible with a lot of work. Piper told me a few times about how he imagined solving the unsolvable problems, and I felt like it sounded good, but he just made a lot of really hard assumptions about DHTs. By that time, I had already worked on Discovery v5—this discovery protocol that we designed in 2016 in Berlin with Felix.

**[30:20] SPEAKER_00:** Right.

**[30:20] SPEAKER_01:** I released the original version. So I already knew that it's never so easy to imagine a DHT that's efficiently formed and all the nodes are working. But for the chain data...

**[30:37] SPEAKER_00:** Right.

**[30:37] SPEAKER_01:** Especially with EIP-4444. That lets the nodes processing the main protocol forget the old chain history. So it made perfect sense to at least put the chain history on a DHT. But it was an EF decision that it was discontinued at a point.

**[31:05] SPEAKER_00:** Well, I guess the thing is, Merkle Patricia Trees are not great for the number of accesses and things anyway, let alone if you're making each of those steps over a networked DHT kind of setup. There's a lot of transactional change complexity.

**[31:31] SPEAKER_01:** The state tree suffers from a lot of issues, especially the Merkle Patricia Trie. It's a huge data set that keeps changing all the time and keeps changing at completely random places, and it's not an easy task to distribute it. Actually, it's getting harder to even synchronize it between full nodes storing the entire stuff.

**[32:00] SPEAKER_00:** So do you think that proofs are going to be a magic silver bullet here, where by having local proofs versus massive, really redundant state machines... do you think there's a path here?

**[32:19] SPEAKER_01:** Oh, no, it's not a silver bullet. I assume you mean what people call statelessness. It's a good thing. It definitely allows a higher degree of scaling. But the state tree still has to be processed and maintained by someone, especially if most of the nodes have no incentive to process it. Now we are talking about 100x and 1000x scaling. Even if we also do state expiry, which is currently imagined in a way that we basically reset the state tree every year and have multiple state trees, if we scale a thousand x then it will be a huge infrastructural centralization issue.

**[33:21] SPEAKER_00:** Right.

**[33:21] SPEAKER_01:** By the way, this thing is not an unsolvable problem. The state as it works today unfortunately makes it really hard to do any fundamental improvements over these properties. But people are considering different storage architectures. Of course, we have to keep the existing contracts workable because that was our main promise from the beginning, that we will not just shut down anything. Everything has 100% uptime. But it is a viable way to come up with more efficient storage methods and use it as an opt-in alternative that will over time be available for much less, and new contracts can be designed using those more efficient storage architectures.

**[34:28] SPEAKER_00:** Yeah, because Verkle trees seemed to be the first sort of thought on that. But then that's kind of come and gone, and maybe it's a binary tree.

**[34:37] SPEAKER_01:** Or actually it does either.

**[34:40] SPEAKER_00:** You don't think it's so important either.

**[34:42] SPEAKER_01:** I mean, both are better than the Merkle Patricia Trie in some ways. But they don't solve this fundamental issue by themselves. The state is a permanent key-value store, and in order to avoid it growing forever, there are all these ideas about state expiry, but still, it's going to be a huge data set. The method of hashing or consensus protocol representation doesn't fundamentally change this. Verkle was supposed to provide more efficient Merkle proofs, but also I guess somewhat more expensive state processing because it's more expensive cryptography. Also, if I'm correct, it's not quantum secure. That was also a thing that I always felt like, I'm not sure if it's a good idea to start working from now, and I just saw it in front of my eyes how it's going to be canceled.

**[36:00] SPEAKER_00:** Yeah, I guess for running nodes in general, there's not a lot of incentive for people to run any kind of node software themselves unless they are a validator or you're running an exchange or a business and you need your node backend. I guess the vision at the start was, "Well yeah, everyone will be running their own node and you've got Mist on top of it, and it's local apps." That can have Swarm for the smart contracts, and it's almost like you won't have server architecture because everyone's running a server stack.

**[36:46] SPEAKER_01:** That did not happen, actually. That's why we are also stuck with the JSON-RPC API, which doesn't provide proofs except for eth_getProof, but doesn't provide proofs for a lot of things, because it was never meant to be used remotely. It was always imagined that it's used locally in a trusted setup on your own machine. And yeah, I remember all those good old days when I just synced up a full node—it was a few gigabytes of disk space—and ran Mist on top of it. It was magic, but unfortunately, it didn't scale.

**[37:26] SPEAKER_00:** No, no. At the Museum of Ethereum here, I've got laptops running Geth 1.3.6, so Homestead Geth, and I mined Homestead back to life. Any hard fork that happens, the old one doesn't go away, right? It doesn't disappear. It's just people don't associate any economic value with it, and it kind of gets abandoned. What I've done is, first via GPU and then down to CPU, mined that Homestead difficulty down to the level that you can CPU mine it again. I do have Mist running on those so we can go and transact, we can send a transaction between those. It should be possible to run AlethZero and AlethOne and Mix on that as well. I haven't had time to do that. And ERC-20 tokens existed. You could have DAO tokens or Mist coin at that time. But yeah, the assumption that people would run their own node and it would all be self-sovereign local apps certainly did not come to fruition.

**[38:54] SPEAKER_01:** Well, yeah, that's when the light client came in and then we assumed that, okay, we do the light client and then it will be all solved.

**[39:01] SPEAKER_00:** That's what I was thinking. I've got a full node running on my smartwatch that works, and I'll just wait for you and the other guys to sort out the light client and just turn that on, and there we go.

**[39:15] SPEAKER_01:** Well, actually the light client protocol worked fine. It's just I spent a really crazy amount of time figuring out how it could be incentivized in a truly decentralized way. I remember this idealism that we are almost done with everything, so we just have to find a real proper way for incentivizing things. But not in a way that there's a few companies where you can buy tokens, but truly in a decentralized way, which is much harder. Then we have to somehow build decentralized trust and figure out market mechanisms that work without initial trust. This is something I spent years with. Honestly, I think I came up with some nice theoretical models and a lot of really complex code. But it just again was the wrong approach, maybe also at the wrong time. We were just not there really.

**[40:27] SPEAKER_00:** Yeah, because BitTorrent has obviously worked for distributing content for many, many years. But then you do have this tragedy of the commons, right? As the latest Hollywood movie gets ripped off, people want that, so that's going to get shared around, no problem. But things which are only of interest to a smaller number of people, without incentives, it's just a leeching problem. Right. Full node runners would contribute, they'd turn on LES as well to help supply that. But the incentives and economics of that, not easy.

**[41:14] SPEAKER_01:** Yeah. Actually, with BitTorrent, if you really want to use it, it requires trackers where you buy some priority access. There are these private trackers and everything. So this is also not completely decentralized, but it does work. It's definitely better than nothing. But for LES, it wasn't really this easy, because downloading movies was an application that everyone understood and everybody used. With Ethereum, everyone felt the importance, but we were nowhere near close to a really mature ecosystem. So I don't think there would have been a big enough market really for these services to work out in a market-based way. But as we scale and accessing the whole data set becomes more and more difficult, at a certain point I think we are going to have something reimagined several years ago. It's just both timing and specifics. I was right about everything except timing and specifics.

**[42:46] SPEAKER_00:** Yes, yes. There's a number of things that seemed like they would be easy and quick and obvious, and have taken so many years. Proof of stake, the white paper had an assumption later in 2015 that it will happen within six months, maybe three to six months. And it was eight years before it actually went live. And on storage. Filecoin, their first white paper was in 2014 as well. Filecoin was not a new thing, and IPFS was around before Ethereum as well. Whisper kind of went for a while, and then now there's Waku, and you've had Status driving a lot of those techs for a lot of those years as well. Jarrad Hope and his team, who were also doing an Android version of the Java client around the same time as I was looking at smartwatches.

**[44:04] SPEAKER_01:** Jarrad Hope was also very eagerly waiting for a fully functional light client.

**[44:10] SPEAKER_00:** Yeah, because they were building kind of a decentralized WeChat super app, but I guess kind of a competitor to Mist really. Similar kind of thing, wanting to have a container for running dapps sitting on top of a local client. Again, having this completely self-sovereign server app stack, but not easy. I can't remember who it was who was telling me when they first saw MetaMask, which was at Devcon 1—that was one of the grantee winners—thinking, "No, that's not what we want. We don't want some browser extension thing talking to a trusted endpoint. That's absolutely the opposite. What are these guys doing?" And then that's become the standard flow, right?

**[45:15] SPEAKER_01:** Well yeah, this is still kind of an unsolved problem to access everything in a truly decentralized way, but I think we are getting there over time. It's just nothing is as simple as we initially imagined. Also, there's a time for everything, and I think truly decentralized infrastructure will be forced by scaling. Things sometimes just don't happen if they are not forced by some external factor. As long as it works in a lazy way to just connect MetaMask to Infura, until then it's the standard way.

**[46:12] SPEAKER_00:** Yeah, yeah. So I think I found two different talks of yours at Devcons talking really about the light client. Do you remember, did you talk in London, or was Shanghai your first?

**[46:26] SPEAKER_01:** No, I talked in London, also Shanghai, and also in Cancún. Those were the first ones, and those were mostly about the light client. Actually, the first release of the light client protocol was in 2016. Later I started to invent all the next chapters of decentralized technology. It was really naive of me, but I also had this project back then where I tried to make logs provable efficiently. The initial attempt for that was in 2017, and now I'm back at it. Now I also have this trustless log index project. That old approach from 2017 was just a more efficient way to organize the Bloom filters, but it didn't really solve the problem of the Bloom filters not adapting to the number of events. Also I never even proposed putting it into consensus, which would have allowed actual trustless proofs through the chain.

**[47:58] SPEAKER_00:** Right.

**[47:58] SPEAKER_01:** So yeah, that also proved to be a hard problem. But yeah, this is one of the things I presented in Cancún.

**[48:08] SPEAKER_00:** Right, right, right.

**[48:10] SPEAKER_01:** And also some of my ideas on state channels. Back then we didn't have L2s in a way. Back then, Layer 2 just meant something that happens off-chain, not necessarily another blockchain. So I had these ideas about individual nodes running their own blockchains, somehow organizing some off-chain calculations through that. But it also assumed a lot about how nodes would operate and probably would have never worked in retrospect.

**[48:53] SPEAKER_00:** Yeah, I mean we had state channels and then we had Plasma and then eventually coming into optimistic rollups and then ZK later. Just many, many different attempts. Hello. See you sir.

**[49:07] SPEAKER_01:** Great to see you.

**[49:10] SPEAKER_00:** So yeah, I guess there's an awful lot of learning, right? Ten years' worth of lots of people trying lots of different things. In terms of the Geth team, has that been similar over the years or have you had larger and smaller amounts of people? Has it been a similar kind of flow through that time?

**[49:36] SPEAKER_01:** I would say it was pretty consistently around 10 people throughout all these years. Sometimes 8, 9, sometimes 11, 12. But really in this range. We did improve our internal processes during the years. Now we do have all these issue and pull request triages. But mostly, that team was always small enough so that we didn't need a lot of processes. Honestly, the team culture did change, especially with certain people coming and going. But I would say it was always a good team culture. I always liked the Geth team. That's also why I never really looked into moving to other teams or other projects because I felt that the team is the best place to do meaningful things.

**[50:56] SPEAKER_00:** Yeah, it's funny because from the very start of Ethereum, the intention was to have multiple clients, right? That was a very basic decision of saying we want a separation between the specification and the implementation. We don't want it to be like Bitcoin where you've got one codebase and there's no competition.

**[51:20] SPEAKER_01:** Well yeah, for Bitcoin's complexity that approach worked, but for Ethereum's complexity I would say this was one of the best decisions. Yeah, it also contributed to almost running out of money by the time we launched Mainnet. But I would say it was money well wasted.

**[51:40] SPEAKER_00:** Yes, no, I would agree it was not efficient, but the outcome was very much worthwhile, yeah.

**[51:48] SPEAKER_01:** And when we switched to proof of stake, we again successfully applied this pattern by funding multiple CL implementations and then testing every EL against every CL, and then running testnets with all five.

**[52:09] SPEAKER_00:** Is it five? Five different primary consensus clients. I think it's five. And notably none of those were within the Foundation either. They were all independent companies and teams. On the execution side, there have been a good number of alternative execution clients over the years. I guess starting with Parity and then Besu and Nethermind, Erigon. How have you tended to work and interact in that kind of environment where you've got all these different teams?

**[52:53] SPEAKER_01:** Well, now we have all the ACD calls and testing calls. By default, we don't need to interact a lot. We have to interact when we are testing out new features. There are prepared forums for that. Some people keep more contacts outside of the Geth team, some people are more turning inwards and just focusing on Geth issues. I think in the first years communication was really not organized well, so we really just tried to figure out things. Some people knew people from the other teams. But actually these days we have much better processes for this. It's also a much bigger challenge because there are so many more people. This is something I realized during the time we really started working on proof of stake. In 2017 was the first time the ether price went to several thousand dollars, and the Foundation had money to hire new teams and fund external teams. I remember that until 2017, I mostly met non-Go Ethereum people at Devcons.

**[54:37] SPEAKER_00:** Right, yeah.

**[54:37] SPEAKER_01:** Those people who lived in Berlin or one of those cities where there were multiple people, they met more people. But I was mainly in Hungary and worked remotely, and I mostly met most of the people at Devcons. But around 2018, so many researchers and new hires came in, and there were also the Seattle teams. I remember Devcon 4 in Prague. Until then, it was mostly 30, 40 people. After every Devcon we stood up on the main stage and did a group photo.

**[55:28] SPEAKER_00:** Oh yeah, yeah.

**[55:28] SPEAKER_01:** Like, "We are the Ethereum Foundation."

**[55:30] SPEAKER_00:** Yes.

**[55:30] SPEAKER_01:** And in 2018, I was just shocked. Like, "Who the hell are all these people? The whole Ethereum Foundation?" It became a much bigger challenge. But also now we do have all these official forums, and I try to go to more events, not just Devcons, in order to keep all the contacts live.

**[56:00] SPEAKER_00:** Yeah. Looking back to when you first started working on Ethereum, did you have any kind of thought or vision of what things might have looked like 10 years later? Has it worked out as you expected or differently? What's your thought looking back on these 10 years?

**[56:25] SPEAKER_01:** I always had a lot of visions. Maybe I was too focused on visions sometimes. The thing is that we all kind of have to imagine the future at every point, even though we know we can't imagine it exactly as it will turn out. But we always have to have some kind of direction and have ideas of how things can turn out. Around 2017, I also realized that scaling will not happen just with L1. As I mentioned, I had these ideas about how we could solve problems more efficiently with, not even rollups, just application-specific state channels and stuff like that. There was also this really great project... oh, okay, I don't...

**[57:34] SPEAKER_00:** Raiden.

**[57:35] SPEAKER_01:** Raiden. Yeah, thank you. They properly implemented the protocol and everything. I think it always struggled with not many people using it. It's a pain that transactions are expensive, but somehow maybe we just missed some organizing force to really move to Layer 2 solutions, and it was just...

**[58:10] SPEAKER_00:** Well, it was meant to be Lightning for Ethereum, right? That was the thought.

**[58:16] SPEAKER_01:** Well yeah, it was pretty much that idea.

**[58:18] SPEAKER_00:** But then Lightning's kind of failed, so maybe not surprising if an Ethereum version of that's not really caught on. Because you've got routing issues, right? It's really complicated. Channels seem to work great for consistent, static topographies. If you want to do merchant-to-merchant, channels work great.

**[58:46] SPEAKER_01:** Yeah, but opening those channels is still costly and non-trivial. I also never really... I installed it, I tried it, I thought, "Okay, this is interesting," but I never really made a payment through Raiden because there was just no occasion where the other party really wanted a Raiden transfer.

**[59:14] SPEAKER_00:** No, no. Well, thank you very much. I think we can wrap it up there. So thanks for your time and thanks for all of your work on Geth over these very many years. Geth has always really been the backbone of Ethereum. New clients come and go, but Geth remains. So thank you.

**[59:39] SPEAKER_01:** Thank you for having me here.

**[59:40] SPEAKER_00:** Thank you so much.