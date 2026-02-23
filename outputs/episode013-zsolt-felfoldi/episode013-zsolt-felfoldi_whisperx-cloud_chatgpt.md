**[00:01] SPEAKER_03:** So, hello and welcome to ETHDenver 2026. Recording here for Early Days of Ethereum with Zsolt Felföldi. How do you pronounce your name? Zsolt? Zsolt, there you go. Anyway, I was working out when we recently reconnected at Devconnect that you’re the third longest-serving person at the Ethereum Foundation, right? You’ve got Vitalik, and then…

**[00:34] SPEAKER_01:** Felix, and then you. Yeah, I haven’t really checked this fact yet, but honestly, yeah.

**[00:44] SPEAKER_03:** Sounds great, that’s it. You’re a very long-time member of the Geth team, yes, but what were you doing before you started at the Foundation? What was your background? How did you find your way into the blockchain world?

**[00:58] SPEAKER_01:** Well, before Ethereum I was working on really different types of projects. I first started at a Hungarian software company, like a really classic software company. We actually sold software in boxes, like put on a shelf—discs, like floppy disks—put in a box on a shelf, and you can buy the software. Like classic software.

Five-and-a-quarter-inch floppies, yeah. Actually, three-and-a-half was… oh okay, three-and-a-half, modern floppies. But maybe also, like I said, in ’97, so maybe I was exaggerating a little. By that time it was mostly CDs. We still used a lot of floppies anyway.

At that company I did things related to—first I did things related to computer graphics. I built a ray tracing engine for some architectural software. And then I also did a lot of work on electronic circuit simulation and circuit design. Really different things.

It was around 2011 when I first heard about Bitcoin, and around 2012 when I started to realize that, as weird as it sounds, it really is probably a big thing.

Actually, I first heard about Ethereum early 2014, a few months after the initial paper had been published. I started contributing, I think, around November, and officially joined EF in 2015 March.

**[03:02] SPEAKER_03:** Did you hear about it through Danny and Viktor, or some other way?

**[03:10] SPEAKER_01:** I did hear about it from Danny and Viktor’s friend circle. But then Viktor was already… actually, I never knew Viktor before. I heard about this thing through one of his friends, and then Viktor was also in that wider circle. He came to Hungary and said, “Oh, I’m already working on this.” Then I started with my ideas and started to explain to him why this thing probably will never work. And he was like, “Okay, you seem to have a good understanding of this. Why don’t you come to work?”

**[03:52] SPEAKER_03:** Right, right, right. Am I right in thinking that you said it was Swarm that you started with?

**[03:59] SPEAKER_01:** Well, yeah. Swarm was part of this initial trinity of base technologies of Ethereum. It was supposed to be the storage layer for dApps. It was kind of a naive way of how people imagined decentralized applications back then, but honestly it made sense at the time. I will say that nothing ever turned out exactly the way that people imagined, but we are still making a lot of progress.

Swarm was how we initially imagined the storage layer for Ethereum. This project still has merits, but this whole problem space is just a bit more complex.

I started contributing to Swarm first, and actually I wrote the first like 500 lines of Swarm.

**[05:02] SPEAKER_03:** There you go. If I remember rightly, Viktor mentioned around May 2014 was when he first heard the trinity concept: Ethereum as your compute and expensive database, Swarm as your decentralized storage, and then Whisper as your messaging. There’s that famous diagram, right, with the circle and the things coming in, and Whisper going around the edge.

But I guess it was Devcon 0 where Danny really presented a fleshed-out vision of what decentralized storage would be.

**[05:51] SPEAKER_01:** That’s correct. I wasn’t there at Devcon 0 yet. I heard about this idea even before I heard about Ethereum. Danny already told me about this idea: he wants to do this kind of hash-based chunk storage. It made total sense that he pitched that, and it could fit in. At the time it was a perfect fit.

So he pitched this idea at Devcon 0, and when they accepted it and hired Danny, Danny called me and said—because he already knew that I knew of this project—let’s do it together.

**[06:40] SPEAKER_03:** There you go. And then you were hired into FDEV?

**[06:40] SPEAKER_01:** Yes.

**[06:40] SPEAKER_03:** I did have a date for that, I’ve forgotten. I guess it was shortly after Devcon 0, right, that you started there?

**[06:40] SPEAKER_01:** Yes, correct.

**[06:40] SPEAKER_03:** Did you go to Berlin or Amsterdam? When did you first meet other people? How did it work?

**[07:07] SPEAKER_01:** It was Amsterdam in February ’15. That’s where I met Jeffrey Wilcke, the creator of Go Ethereum, and the Go Ethereum team back then. I don’t say “Geth” because that abbreviation was invented later. So yeah, that’s where I met the Go Ethereum people.

I already had these contributions to Swarm, and it was kind of an implied thing that maybe I might be hired, but there was really no official hiring process back then.

Jeff was this really laid-back guy. He just said, “Okay man, I saw your contributions, and let’s talk sometime this week.” I waited the whole week and waited for some serious interview—like, it was a dream job for me. By that time I was really enthusiastic about this whole thing. Even though I felt that this whole initial design… I couldn’t really imagine how it would scale and everything, and yeah, it is a hard problem. That was true. But it was still worth starting it, and I was really enthusiastic. I really wanted to get hired.

The whole week I just waited, and at the end of the week, like the last half an hour before we all left home, Jeff just said, “Oh yeah, when I wanted to talk to you—you’re hired.” Okay, that’s a good talk. So yeah, this is how the hiring process went back then.

**[08:47] SPEAKER_03:** Excellent. That’s easy, we like that. So that was before you went to Amsterdam, I assume? I assume you went to Amsterdam after you had been hired?

**[09:07] SPEAKER_01:** No, it happened in Amsterdam.

**[09:07] SPEAKER_03:** Oh, so you were there, unhired, on site?

**[09:07] SPEAKER_01:** Yeah. Jeff agreed that—I bought my own plane ticket—but I could stay at the Airbnb where the whole team stayed. I just worked with them and showed my contributions. So I went to Amsterdam unhired, but… yeah.

**[09:29] SPEAKER_03:** Right, that plane ticket was a good investment. Did they not have office space at that point, even?

**[09:35] SPEAKER_01:** They did. Back then there was an Amsterdam office. It was mostly for Jeff, because Jeff lived in Amsterdam. When Jeff left—or maybe before that, I’m not sure exactly—the office was closed. It was a really small office. Last time I checked, now I think it’s a dentist. It doesn’t exist, but it was really just a small place.

Later I went to Berlin a lot after I was hired. For the Geth team it was really centered in Berlin.

**[10:27] SPEAKER_03:** Right, because as well as Jeff you’ve got Bas, right? He was another Amsterdam person, right? Bas van…

**[10:41] SPEAKER_01:** Sorry, not “in Amsterdam.” I mean, yeah, no one else was—quite distributed. Bas was there for a relatively short time, and Jeffrey also left after a while and started his own…

**[10:57] SPEAKER_03:** Company, right—develop games or something. He did have… “EF Labs” was another one. Do you know anything about EF Labs? Because when Jeff worked with JPMorgan to do Quorum, that was announced under the label “EF Labs.”

**[11:20] SPEAKER_01:** Never heard of that. I think I heard the name, but I didn’t really know what it does. But I knew that Jeff started working with JPMorgan back then. And in that time big banks really, really wanted to talk to us at every Devcon. We were always invited to fancy dinners by some people. Banks really wanted to learn about the technology.

Jeff went for a while to work on Quorum, yes.

**[11:56] SPEAKER_03:** Unless I can somehow get in contact with Jeff, I guess it’s a little bit of a mystery what exactly EF Labs was—though I suspect it might be a little bit like “Ethosphere,” sort of being a name, a banner for activities rather than a legal entity.

Another thing I don’t know there, but I suspect, is: I don’t think Jeff told Ming that he was doing that stuff with JPM. I suspect he completely just did that on his own without any communication with Ming, or with the EF.

**[12:34] SPEAKER_01:** Well, actually he never really told a lot to us about that. We knew that he’s working with JPMorgan, but probably it’s a big bank—probably he had to sign a contract, a non-disclosure agreement—so he probably couldn’t share all the details.

**[12:54] SPEAKER_03:** I remember at some point, and I can’t remember the context, him saying he found it interesting because the consensus for that was on-chain. The consensus for that was happening as smart contracts. So it was kind of almost like this pluggable consensus—consensus pulled up into the app layer. He found that quite interesting. The initial Quorum consensus, it didn’t last long.

But I think Gav also was doing that sort of stuff on the C++ side. He did some proof-of-authority stuff before that happened on the Geth side, before Clique. There was this… he actually made a different C++ client. So you’ve got Eth, but he made another one that was called like “Fluidity” or something, which was like pulling all the libraries in the same, but with a proof-of-authority consensus. He did that, that was one of the last things he did before he went out to Parity. I think both him and Jeff were interested in that thought of, “Well, how can you formulate these pieces in different ways,” right, for those kinds of use cases.

Interesting. But he left, I think it was probably very early in 2017. I did find a period but it was certainly ahead of Devcon 3. Let me see if I can find the date. I don’t remember the exact date.

**[14:44] SPEAKER_01:** There maybe wasn’t even a really exact date when Jeff left. Basically, a month after I joined, Péter Szilágyi joined, and he was the team lead for a very long time. Jeff kind of handed it on to Péter, and for a while he was officially still team lead, but not really. We haven’t seen him on the calls for…

**[15:13] SPEAKER_03:** No. The date I found there was February 2017, but I think I got that from GitHub. I think that was like his final commit, but he probably tailed off.

**[15:29] SPEAKER_01:** Yeah, he already started focusing on other stuff, like this Quorum stuff, and then his own things sometime in ’16.

**[15:37] SPEAKER_03:** He started a company called Grid Games with his brother, building a particular game, but that also seems to have ceased. So yeah, he’s unknown off in the world somewhere.

**[15:52] SPEAKER_01:** That’s pretty much all I know about him. We tried to invite him a few times to come to some event and meet up, but I think for some reasons he really had enough of—maybe not us—but things going on in the EF.

**[16:09] SPEAKER_03:** I think that would be the case that when Ming came in, she both did legal tidy-up but also cut the spending a lot. You’d had the crowdsale in July/August/September 2014, but coming up to the mainnet release a year later, nearly all the money was gone. So Defcon 1 was a postponed one because of that.

**[16:36] SPEAKER_01:** Yes, they spent it very fast. We didn’t really feel a lot of this, actually. Jeff just said that now that the ether price is so low—actually I think the low point was $0.42—and for a full year it didn’t really move. Jeff said, “Okay, we all have to take a pay cut,” but the pay cut was really just 10%, and I think maybe he took a bigger one.

For us it was really not that bad. The idea was that when the ether price reaches $2, then we do have some time, some money to go forward. Then our salaries went back. That wasn’t a lot of time.

I don’t really remember the price history, and maybe it’s not the most important thing, but I think ETH reached something like $10 pretty soon, like in 2016, the start of 2016. We went even a little bit higher, but then we had the DAO fork, and the Shanghai attacks. Given how turbulent those times were, the markets held up pretty well. With $10 ETH, we could survive further.

**[18:18] SPEAKER_03:** Yeah, that was quite a jump up. I heard that at the worst point there was only four months of runway left. That was how close it was to running out of money.

There were those big cuts which really resulted in: Gav, Gavin, the C++ team were the main victims of those cuts. Then into 2016—pardon me—I was hired in February 2016, same time as Greg Colvin came in, and also Pavel was rehired. He was working through Imapp, working on that JIT. That contract stopped, but then he came back at that time as well. So late 2015 to early 2016 was the absolute bottom of: are we even going to ship this thing? Are we going to run out of money before we get to mainnet? But then some of us were coming in as backfill for that C++ team.

Defcon 1 was sort of what you were mentioning, in that series that had got cancelled, but then ConsenSys came in and paid for that and said, “Hey, we’ll mainly organize it,” so the thing can happen. That was the big first public event.

What are your memories of Defcon 1?

**[19:55] SPEAKER_01:** My subjective impression was that it’s really amazing. Compared to today’s Devcons, it was small—I think 300-something people, maybe. But I’m not sure; less than a thousand.

It was in a really prestigious venue—some old bank building on Threadneedle Street, in the City of London. I really felt like, okay, so now this is really a serious thing. Probably that was the reason why ConsenSys stepped in and funded the event: so we really could step up in terms of public appearance and appear something really serious.

I remember all the big banks having a presence—like booths—at Defcon 1.

**[20:59] SPEAKER_03:** And then Microsoft is headline sponsor. It’s like, wow, right? Recognition, right, that you’re like, wow, Microsoft are interested and supportive.

I think for a lot of people it was a real kind of wow: this is for real. Sadly, I could not afford to go. I watched the livestream. I was not quite in and working yet—I was an enthusiastic contributor—but yeah.

**[21:34] SPEAKER_01:** Actually it was also the first time for me when I met a larger number of Ethereum people. I first met the Go Ethereum team in early ’15, and I went to Amsterdam one more time, I think in May. But Defcon 1 was the place where I really realized how big this thing is, and it’s really not just about client developers. Even back then people presented about formal verification and all this stuff. I realized this is really big, and probably everyone wants to be a part of it, at least a little bit.

**[22:20] SPEAKER_03:** Looking back at Devcon 1 videos, it’s like everything—any kind of use case you could think of, there was somebody presenting about it. So early, more than 10 years ago, but many concepts which were probably massively too early to do, but maybe you can do them all now, seem to be presented. You had Nick Szabo as well—Nick Szabo doing a keynote.

Was that maybe the first time that you’d met a number of the people in Berlin, like Christoph Jentzsch and Lefteris, and maybe even Gav?

**[23:00] SPEAKER_01:** I think I met some of these people already in London, and I think first time I went to the Berlin office—back then it was like the old office. Some people I met at Defcon 1, some people I met in Berlin.

**[23:24] SPEAKER_03:** Was Defcon 1 the first time that you’d been to do Ethereum things in London, or did you go to any sort of London meetups, or meet any of those comms people earlier?

**[23:39] SPEAKER_01:** I didn’t go to any meetups in London before, but actually I did… Viktor was in London at the time, and I went to London around the time of doing some event with my old software company, the Hungarian software company. We went to London to sell our software and everything. I was still working there. After that I met up with Viktor and talked about things.

**[24:23] SPEAKER_03:** From what Viktor was describing, and then I was looking at videos later, he had seen Gav talk in London in very early February—I think it was February the 6th—almost immediately after they’d had the Miami, like B2C Miami launch: Vitalik’s first public talk, and Anthony Di Iorio’s mansion where a lot of them met for the first time.

Gav had been back in London, I think it was like a week after, and did a talk there that Viktor had gone to. That was Viktor’s first in-person meeting with any of these, and then Gav pulled him on board. Those are the very, very early days.

**[25:22] SPEAKER_01:** The very, very early days—I wasn’t there. When I first heard about Ethereum that was, I think, March or April ’14. I first heard about the presale. That’s where I first heard about this thing. But yeah, I know that Gavin was one of the very early founders of this, and he wrote the Yellow Paper.

**[25:51] SPEAKER_03:** Full of Greek letters, yes.

**[25:51] SPEAKER_01:** Yes.

**[25:51] SPEAKER_03:** Very confusing. And the C++ client, of course.

The first time I think I saw your name or was in contact with you was about light client. I’d been trying to get Ethereum ARM Linux cross-builds running on my smartwatch. My thought there was: get the thing running, and then this light client stuff is just kind of starting, and scaling will be solved, right? We’re going to be able to run these nodes on anything. You’ll have them on your phone, smartwatch, router. They’ll be in every operating system. We’ll solve that scaling and that lightness.

You were plunged right into that problem, right?

**[26:38] SPEAKER_01:** Yeah. When Jeff hired me, he put me on this project. He just said, “Okay, it’s great that you contributed to Swarm, but if you join the Geth team, you will have to start working on the light client because it’s a very important thing and it hasn’t been started yet.”

I felt really good about it. Back then it really felt like: we do these few things, we have a working light client protocol, and the whole Ethereum base layer, and then we’re all good. But it wasn’t that easy. Still, those were the first steps.

So I designed the LES protocol. In retrospect it didn’t make a lot of sense to build it over the devp2p layer, because it wasn’t easy to access from web browsers and stuff. Also it was a proof-of-work-based light client, and that project ended after a while.

But I’m still very much into trustless chain access. That has usually been one of my focuses all the time. Right now I’m also working on something called the Trustless Execution Layer API, which is similar to the Beacon REST API but works on the execution layer and provides everything with proofs.

I’m still very much into this, because I think this is where it really makes sense if even normal users access chain data with proofs.

**[28:36] SPEAKER_03:** Right, right. And there was a project called Portal as well—were you involved with Portal? That was a later kind of light client.

**[28:42] SPEAKER_01:** No, I wasn’t. Portal was Piper Merriam’s brainchild.

By the time we kind of realized that LES was a nice first experiment but maybe not the best approach, he started something different that was UDP-based, and also used different topologies. It was kind of a DHT approach to storing the chain and the state.

Actually I think it’s a bad thing that it’s been completely canceled, because—to be honest—I never really believed that it will be an easily solvable problem to store the Merkle Patricia trie of the state on a DHT. But for the chain data, yeah, it made perfect sense.

Maybe the state would have been possible with a lot of work. Piper told me a few times how he imagines solving all the unsolvable problems, and I felt like, yeah, it sounds good, but he just made a lot of really hard assumptions about DHTs.

By the time I already worked on Discovery v5, there was also this discovery protocol that basically we designed in 2016 in Berlin with Felix, and I released the original version. So I already knew that it’s never so easy to imagine a DHT that’s efficiently formed, that all the nodes are working.

But for the chain data, especially with EIP-4444—that lets the main protocol nodes processing main protocol forget all chain history—it made perfect sense to at least put the chain history on a DHT. But it was an EF decision that it was discontinued at some point.

**[31:06] SPEAKER_03:** I guess the thing is, Merkle Patricia tries are not great for the number of accesses anyway, let alone if you’re making each of those steps over a networked DHT kind of setup. There’s so much transactional change. The state trie suffers from a lot of issues, especially the Merkle Patricia state trie.

**[31:32] SPEAKER_01:** Yeah, the Merkle Patricia state trie. It’s a huge dataset that keeps changing all the time, and keeps changing in completely random places. It’s not an easy task to distribute it. Actually it’s getting harder to even synchronize it between the full nodes, or the entire state.

**[31:59] SPEAKER_03:** Do you think that proofs are going to be a magic silver bullet here, where by having local proofs versus massive, really redundant state machines—do you think there’s a path here where…?

**[32:24] SPEAKER_01:** Oh yeah, no, it’s not a silver bullet.

I assume you mean what people call statelessness. It’s a good thing. It definitely allows a higher degree of scaling, but the state trie still has to be processed and maintained by someone. Especially if most of the nodes have no incentive to process it.

Now we are talking about a 100x and 1000x scaling. Then even if we also do state expiry—which is currently imagined in a way that we basically reset the state trie every year or something, and have multiple state tries—that helps somewhat. But if we scale 1000x then it will be a huge infrastructural centralization issue.

By the way, this is not an unsolvable problem. The state as it works today unfortunately makes it really hard to do any fundamental improvements over these properties, but people are considering different storage architectures. Of course we have to keep the existing contracts workable because that was our main promise from the beginning. We will not just shut down anything. Everything has 100% uptime.

But it is a viable way to come up with more efficient storage methods and use it as an opt-in alternative that over time will be available for much less, and new contracts can be designed using those more efficient storage architectures.

**[34:26] SPEAKER_03:** Verkle trees seemed to be the first sort of thought on that, but then those… that’s kind of come and gone. Maybe it’s a binary tree, or actually does it…?

**[34:40] SPEAKER_01:** It’s not so important either. I mean, both are better than the Merkle Patricia trie in some ways, but they don’t solve this fundamental issue by themselves.

Still, the thing is that the state is a permanent key-value store. In order to avoid it growing forever, there are all these ideas about state expiry. But still, it’s going to be a huge dataset, and the method of hashing, or consensus representation, doesn’t fundamentally change this.

Verkle was supposed to provide more efficient Merkle proofs, but also I guess somewhat more expensive state processing because it’s more expensive cryptography. Also, if I’m correct, it’s not quantum secure. That was also a thing where I always felt like, yeah, I’m not sure if it’s a good idea to start working on now, and I just saw it in front of my eyes how it’s going to be canceled.

**[36:04] SPEAKER_03:** For running nodes in general, there’s not a lot of incentive for people to run any kind of node software themselves unless they are a validator, or you’re running an exchange or a business and you need your backend.

The vision at the start was like, well, everyone will be running their own node, and you’ve got Mist on top of it, and it’s local apps, and then that can have Swarm for the smart contracts. It’s almost like you won’t have server architecture because everyone’s running a server stack. That did not happen.

**[36:47] SPEAKER_01:** That’s why we are also stuck with the JSON-RPC API, which doesn’t provide proofs—except eth_getProof—but doesn’t provide proofs for a lot of things, because it was never meant to be used remotely. It was always imagined that it’s used locally, in a trusted setup, on your own machine.

I remember all those good old days when I just synced up a full node. It was a few gigabytes of disk space, and ran Mist on top of it. It was magic. But unfortunately it didn’t scale.

**[37:29] SPEAKER_03:** In the Museum of Ethereum here, I’ve got laptops running Geth 1.3.6—Homestead Geth—and I mined Homestead back to life. Any hard fork that happens, the old one doesn’t go away. It doesn’t disappear; it’s just people don’t associate any economic value with it and it kind of gets abandoned.

What I’ve done is first GPU and then down to CPU mine that Homestead difficulty down to the level that you can CPU mine it again. I have Mist running on those, so we can go and transact. We can send a transaction between those, and it should be possible to run Aleth0 and Aleth1 and Mix on that as well. I haven’t had time to do that.

ERC-20 tokens existed. You could have DAO tokens or MistCoin at that time. But the assumption that people would run their own node and it would all be self-sovereign local apps certainly did not come to fruition.

**[38:56] SPEAKER_01:** That’s when the light client came in, and then we assumed that, okay, then we do the light client and it will be all solved.

**[39:00] SPEAKER_03:** That’s it, yeah. That’s what I was thinking: I’ve got a full node running on my smartwatch that works, and I’ll just wait for you and the other guys to sort out light client and just turn that on, and there we go.

**[39:11] SPEAKER_01:** Well, actually the light client protocol worked fine. It’s just… I spent a really crazy amount of time figuring out how it could be decently incentivized in a truly decentralized way.

I remember this idealism that now we are almost done with everything, so we just have to find a real proper way for incentivizing things, but not in a way that there’s a few companies where you can buy tokens—truly in a decentralized way, which is much harder. Then we have to somehow build decentralized trust and figure out market mechanisms that work without initial trust.

This is something I spent years with. Honestly I think I came up with some nice theoretical models and a lot of really complex code, but yeah, it was just the wrong approach, maybe also at the wrong time. We were just not there, really.

**[40:29] SPEAKER_03:** BitTorrent has obviously worked for distributing content for many years, but you do have this tragedy of the commons, right? The latest Hollywood movie—someone has ripped it—people want that, so that’s going to get shared around no problem. But things which are only of interest to a smaller number of people, without incentives, it’s just a leeching problem. Good full node runners would contribute; they would turn on LES as well; they would help supply that. But the incentives and economics are not easy.

**[41:16] SPEAKER_01:** Actually with BitTorrent, usually if you really want to use it, it requires trackers where you buy some priority access. There are these private trackers and everything. So yeah, those are also not completely decentralized. But it does work; it’s definitely better than nothing.

For LES it wasn’t really this easy, because downloading movies was an application that everyone understood, that everybody used. With Ethereum it was always: everyone felt the importance, but we were nowhere near close to a really mature ecosystem. So I don’t think there would have been a big enough market really for these services to work out in a market-based way.

But as we scale and accessing the whole dataset becomes more and more difficult, at a certain point I think we are going to have something like we imagined several years ago. It’s just timing and specifics. I was right about everything except timing and specifics.

**[42:51] SPEAKER_03:** There’s a number of things that seemed like they would be easy and quick and obvious, and have taken so many years. Like proof of stake: it was in the white paper; there was an assumption later in 2015 that’ll happen within six months, maybe three to six months, and then it’s eight years before it actually went live.

On storage: Filecoin, their first white paper was in 2014 as well. Filecoin was not a new thing. IPFS was around before Ethereum as well. Whisper kind of went for a while, and then now there’s… and you’ve had Status driving a lot of those texts for a lot of those years as well—Jarrad Hope and team—who were also doing Android version of the Java client, same kind of time as I was looking at smartwatches.

**[44:06] SPEAKER_01:** Yeah, Jarrad Hope was also very eagerly waiting for the fully functional light client.

**[44:12] SPEAKER_03:** Yeah, because they were building a decentralized “we work” super app. I guess kind of a competitor to Mist—really similar kind of thing—wanting to have a container for running dApps sitting on top of a local client, again having this completely self-sovereign server-app stack.

I can’t remember who it was that was telling me that when they first saw MetaMask—which was at Devcon 1, one of the grantee winners—it was MetaMask; them thinking, “No, that’s not what we want. We don’t want some browser extension thing talking to a trusted endpoint. That’s absolutely the opposite. What are these guys doing?” And then that’s become the standard flow, right?

**[45:18] SPEAKER_01:** Well, yeah. This is still kind of an unsolved problem: to access everything in a truly decentralized way. But I think we are getting there over time. It’s just: nothing is as simple as we initially imagined, and also there’s a time for everything.

I think decentralized infrastructure will be forced by scaling. Sometimes it just doesn’t happen if they are not forced by some circumstance—some external factor. As long as it works in a lazy way to just connect MetaMask to Infura, until then it’s the standard way.

**[46:15] SPEAKER_03:** I found two different talks of yours at Devcons talking really about light clients. Do you remember—did you talk in London, or was Shanghai your first?

**[46:22] SPEAKER_01:** I talked at London, also Shanghai, and also in Cancún. Those were the first two Devcons that were mostly about the light client. The first release of the light client protocol was in ’16, so it was around that time.

Later, I already started to invent all the next chapters of decentralized technology. It was really naive of me, but I also had this project back then where I started to try to make logs provable efficiently.

The initial attempt for that was in 2017, and now I’m back at it. Now I also have this trustless log index project. All the approaches in 2017 were just a more efficient way to organize the bloom filters, but it didn’t really solve the problem of bloom filters not adapting to the number of events. And I never even proposed putting it into consensus, which would have allowed the actual trustless proofs through the chain. That also proved to be a hard problem, but this is one of the things I presented in Cancún.

Also, some kind of my ideas of state channels. Back then we didn’t have L2s in a way. Back then, layer two just meant something that happens off-chain, not necessarily another blockchain. I had these ideas about individual nodes all running their own blockchains and somehow organizing some off-chain calculations through that, but it also assumed a lot about how those would operate and probably would have never worked.

**[48:50] SPEAKER_03:** Yeah, I suspect, right. We had state channels, and then we had Plasma, and then eventually coming into optimistic rollups, and then zk later. Just many, many different attempts.

Hello, see you sir, great to see you. Okay.

So, in terms of the Geth team: has that been similar over the years, or have you had larger and smaller amounts of people? Has it been a similar kind of flow through that time?

**[49:36] SPEAKER_01:** I would say it was pretty consistently around 10 people throughout all these years. Sometimes eight, nine; sometimes 11, 12; but really in this range.

We did improve our internal processes during the years. Now we do have all this issue and pull request triage and… yeah. But really, it’s mostly been— the team was always small enough so that we didn’t need a lot of processes.

Honestly the team culture did obviously change, especially with certain people coming and going, but I would say it was always a good team culture. I always liked the Geth team. That’s also why I never really looked into moving to other teams or other projects, because I felt that team is the best place to do meaningful things.

**[50:54] SPEAKER_03:** It’s funny because from the very start of Ethereum, the intention was to have multiple clients, right? That was a very basic decision: we want a separation between the specification and the implementation, because we don’t want it to be like Bitcoin where you’ve got one codebase and then there’s no competition.

**[51:21] SPEAKER_01:** For Bitcoin’s complexity that approach worked, but for Ethereum’s complexity I would say this was one of the best decisions. It also contributed to almost running out of money by the time we launched mainnet, but I would say it was money well wasted.

**[51:43] SPEAKER_03:** I would agree. It was not efficient, but the outcome was very much worthwhile. When we switched to proof of stake…

**[51:52] SPEAKER_01:** We again successfully applied this pattern by funding multiple CL implementations, and then testing every EL against every CL.

**[52:08] SPEAKER_03:** And then all the combinations. Five, is it? Five different primary consensus clients there are—I think it’s five. Notably none of those were within the Foundation either; they were all independent companies and teams.

On the execution side there have been a good number of different alternative execution clients over the years. How do you tend to work and interact in that kind of environment where you’ve got all these different… starting with Parity, and then Besu and Nethermind, Erigon—how do you work with other teams?

**[52:58] SPEAKER_01:** We have now all the ACD calls and testing calls. Mostly, I mean, we all do have working clients all the time, so by default we don’t need to interact a lot. We have to interact when we are testing out new features. There are the proper forums for that.

Some people keep more contacts outside of the Geth team; some people are more turning inwards and then just focusing on Geth issues. But actually I think in the first years communication was really not organized as well. We really just tried to figure out things, and some people knew some people from the other teams.

These days we have much better processes for this. Also it’s a much, much bigger challenge because there’s so many more people.

This is also something I realized during the time we really started working on proof of stake. In 2017 it was the first time the ether price went to several thousand dollars, and the Foundation had money to hire new teams and fund external teams.

I remember that until 2017 I mostly met non-Go-Ethereum people at Devcons. Maybe those people who lived in Berlin or one of those cities where there were multiple people met more people, but I was always in Hungary and worked remotely, and I mostly met most of the people at Devcons.

Around, I think, 2018—when so many researchers and CR teams had been hired—I remember Devcon 4 in Prague. Until then it was mostly, I don’t know how many people exactly, but I do remember maybe 30 or 40 people. After every Devcon we stood up at the main stage and the group photo: “Oh yeah, we are the Ethereum Foundation.” It was that many people.

In ’18, I was just shocked: who the hell are all these people? The whole Ethereum Foundation? So it became a much bigger challenge. But also now we do have all these official forums, and I try to go to more events, not just Devcons, in order to keep all the contacts live.

**[56:00] SPEAKER_03:** Looking back to when you first started working on Ethereum, did you have any kind of thought or vision of what things might have looked like 10 years later? Has it worked out as you expected, or differently? Looking back on these 10 years, what’s your thought?

**[56:24] SPEAKER_01:** I always had a lot of visions. Maybe I was too focused on vision sometimes.

The thing is that we all kind of have to imagine the future at every point, even though we know we can’t imagine it as it will turn out. It never turns out exactly the way we want, but we always have to have some kind of direction, and we have to have ideas of how things can turn out.

Around 2017 I also realized that scaling will not happen just with L1. I also had these ideas about how we could solve problems more efficiently with—not even rollups—just application-specific state channels and stuff like that.

But there was this really great project…

**[58:08] SPEAKER_03:** Raiden?

**[58:08] SPEAKER_01:** Oh, okay, right—then Raiden. So yeah, they properly implemented the protocol and everything. I think it has always struggled with not many people using it.

It’s a pain that transactions are expensive, but still somehow maybe we just missed some organizing force to really move to some kind of layer two solutions.

**[58:44] SPEAKER_03:** It was meant to be Lightning for Ethereum, right? That was the thought.

**[58:44] SPEAKER_01:** Well, yeah, it was pretty much that idea. But then Lightning’s kind of failed, so maybe not surprising if an Ethereum version of that has not really got… because you’ve got routing issues, right? It’s really complicated.

The channels seem to work great for consistent, static topographies—if you want to do merchant-to-merchant, channels work great. But opening those channels is still costly and non-trivial.

I installed it, I tried it, okay this is interesting, but I never really made a payment through Raiden because there was just no occasion where the other party really wanted a Raiden transfer.

**[59:11] SPEAKER_03:** No, no. Well, thank you very much. I think we can wrap it up there.

So thanks for your time, and thanks for all of your work on Geth over these very many years. Geth has always really been the backbone of Ethereum. New clients come and go, but Geth remains. So thank you.

Thank you for having me here.

**[59:41] SPEAKER_00:** Thank you.

**[59:41] SPEAKER_03:** You, you.

**[59:41] SPEAKER_UNKNOWN:** You, you, you, you, you.