**[00:01] SPEAKER_03:** So hello and welcome to ETHDenver 2026. So here recording for Early Days of Ethereum with Zsolt Felföldi. How do you pronounce your name? Zsolt? Zsolt, there you go. Anyway, so yeah, I was working out when we were recently reconnected at Devconnect, and I was working out that you're the third longest person at the Ethereum Foundation, right? That you've got Vitalik, and then Felix, and then you.

**[00:34] SPEAKER_01:** Yeah, I haven't really checked this fact yet, but honestly yeah, it sounds great.

**[00:44] SPEAKER_03:** That's it. So I mean, you're a very long time member of the Geth team, yes. But what were you doing before you started at the Foundation? What was your background? How did you find your way into the blockchain world?

**[00:58] SPEAKER_01:** Well, before Ethereum I was working on really different types of projects. I first started at a Hungarian software company, like really classic software company. We actually sold softwares in boxes, like put on a shelf, discs. Like floppy disks, put in a box on a shelf and you can buy the software. Like this type of classic software.

**[01:18] SPEAKER_03:** Five and a quarter inch floppies?

**[01:20] SPEAKER_01:** Yeah, actually three and a half.

**[01:22] SPEAKER_03:** Oh okay, three and a half. We're on to modern floppies, yeah.

**[01:25] SPEAKER_01:** But maybe also, like I said, in '97, so maybe I was exaggerating a little. So by that time it was mostly CDs. We still used a lot of floppies anyway. So at that company I did things related to, first did things related to computer graphics. Like I built a ray tracing engine for some architectural software. And then I also did a lot of work on electronic circuit simulation and circuit design. So yeah, really different things.

And it was around 2011 when I first heard about Bitcoin, and around 2012 when I started to realize that, as weird as it sounds, it really is probably a big thing. And yeah, so actually I first heard about Ethereum early 2014, a few months after the initial paper had been published. Yeah, and started contributing I think around November and officially joined EF in 2015 March. So yeah.

**[03:02] SPEAKER_03:** And did you hear about it through like Danny and Viktor, or some other way?

**[03:10] SPEAKER_01:** Well, I did hear about it from like Danny and Viktor's friend circle. Yeah, but then Viktor was already actually — I never, I didn't know Viktor before. So I heard about this thing through one of his friends, and then Viktor was also in that wider circle and he came to Hungary and said, "Oh, I'm already working on this." And then I started with my ideas and started to explain to him why this thing probably will never work. And he was like, "Okay, you seem to have a good understanding of this. Why don't you come to work?"

**[03:52] SPEAKER_03:** Right, right, right. So yeah. And am I right in thinking that you said it was Swarm that you started with?

**[03:59] SPEAKER_01:** Well yeah, so Swarm was like part of this initial trinity of base technologies of Ethereum. So it was supposed to be the storage layer for dapps. Yeah, I mean it was kind of a naive way of how people imagined the decentralized applications back then, but honestly it made sense at the time. So I will say that nothing ever turned out exactly the way that people imagined it, but we are still making a lot of progress.

So yeah, Swarm was how we initially imagined the storage layer for Ethereum. And I mean, this project still has merits, but yeah, this whole problem space is just a bit more complex. Yeah, so I started contributing to Swarm first and actually I wrote the first like 500 lines of Swarm.

**[05:02] SPEAKER_03:** There you go. Yeah, I mean I think if I remember rightly that Viktor mentioned around May 2014 was when he first heard the trinity, this concept that you could have Ethereum as your sort of compute, an expensive database, Swarm as your decentralized storage, and then Whisper as your messaging. There's that famous diagram, right, with the circle and the things coming in and Whisper going around the edge. And there's another one of those. But yeah, I mean I guess it was Devcon Zero where Danny really presented a fleshed out vision of what that decentralized storage could be.

**[05:51] SPEAKER_01:** Yes, that's correct. I wasn't there at Devcon Zero yet. So I've heard about this idea even before I heard about Ethereum. So Danny already told me about this idea that he wants to do this kind of hash-based chunk storage. Yeah, and it made total sense that he just pitched that it can fit in. At the time it was a perfect fit.

So he pitched this idea at Devcon Zero, and when they accepted it and hired Danny, then Danny called me and said, because he already knew that I know of this project, yeah, then let's do it together.

**[06:40] SPEAKER_03:** So there you go. And then so you were hired into EF Dev. Yes, I did have a date for that, I've forgotten. I guess it was shortly after Devcon Zero, right, that you started there? Yes, correct. Did you go to Berlin or Amsterdam? Well, when did you first meet other people? How did it...

**[07:07] SPEAKER_01:** It was Amsterdam in February '15, right. That's where I met Jeffrey Wilcke, the creator of Go Ethereum, and the Go Ethereum team back then. I don't say Geth because Geth was like this abbreviation was invented later. But so yeah, that's where I met the Go Ethereum people.

Yeah, and I already had these contributions to Swarm and it was kind of an implied thing that maybe I might be hired, but there was really no official hiring process back then. So yeah, it was really just — Jeff was this really laid back guy and he just said, "Okay, okay man, I saw your contributions and let's talk sometime this week." And yeah, I waited the whole week and waited for some serious interview. Like, it was a dream job for me. Yeah, but by that time I was really enthusiastic about this whole thing. And I felt like, even though I felt that this whole initial design was — yeah, I couldn't really imagine how it would scale and everything. And yeah, it is a hard problem, so it was true. But it was still worth starting it.

And I was really enthusiastic and I really wanted to get hired. And yeah, the whole week I just waited, and at the end of the week, like the last half an hour before we all left home, Jeff just said, "Oh yeah, when I wanted to talk to you — you're hired." Okay, that's a good talk.

**[08:47] SPEAKER_03:** So yeah, this is how the hiring process went back then. Excellent, well that's easy, we like that. And so you — that was before you went to Amsterdam, I assume? I assume you went to Amsterdam after you had been hired? No, no, no, it happened in Amsterdam. Oh, so I see, so you were there unhired on site?

**[09:07] SPEAKER_01:** Yeah, so like Jeff agreed that, I mean, I bought my own plane ticket, but I could stay at the Airbnb where the whole team stayed. And yeah, I just worked with them and showed my contributions. And yeah, so I went to Amsterdam unhired but...

**[09:29] SPEAKER_03:** Right, right. That plane ticket was a good investment. So yeah. So did they not have office space at that point even?

**[09:35] SPEAKER_01:** Well, they did. They actually, back then there was an Amsterdam office. It was mostly for Jeff because Jeff lived in Amsterdam. Yeah, but when Jeff left, or maybe before that, I'm not sure exactly, but so this office was closed. And actually it was a really small office. Last time I checked, now I think it's a dentist. Like, oh yeah, works there. Yeah, it doesn't exist. But it was really just a small place.

But I later went to Berlin a lot after I was hired, and yeah, it was, for the Geth team, it was really centered somehow in Berlin.

**[10:27] SPEAKER_03:** Right, right. Because yeah, I mean I guess as well as Jeff, you've got Bas, right? He was another Amsterdam person, right? Bas van Kervel. Yeah. But then maybe most of the other team members weren't in Amsterdam.

**[10:41] SPEAKER_01:** I mean, yeah, no one else was. Quite distributed. Bas was there for a short time, relatively short time. And Jeffrey also left after a while. Yeah, and started his own company.

**[10:57] SPEAKER_03:** Right. Develop games or something. Yeah, so though he did have — oh, EthLabs was another one. Do you know anything about EthLabs? Because when Jeff worked with JP Morgan to do Quorum, that was announced under the label EthLabs. Never heard of that.

**[11:20] SPEAKER_01:** Yeah, I think I heard the name, but I didn't really know what it does. But yeah, this is something I knew, that Jeff started working with JP Morgan back then. And then in that time, big banks really wanted to just talk to us at every Devcon. And we were always invited to fancy dinners by some main people. And yeah, so banks really wanted to learn about the technology. Yeah, so Jeff went for a while to work on Quorum. Yes, true.

**[11:56] SPEAKER_03:** Yeah. I mean, unless I can somehow get in contact with Jeff, I guess it's a little bit of a mystery what exactly EthLabs was. Though I suspect it might be a little bit like Ethersphere, of just sort of being a name, a banner for activities rather than a legal entity. And another thing I don't know there but I suspect is I don't think Jeff told Ming that he was doing that stuff with JPM. I suspect that he completely just did that on his own without any communication with Ming or with the EF. It's just —

**[12:34] SPEAKER_01:** Well, actually he never really told a lot to us about that. So we knew that yeah, he's working with JP Morgan, but probably like it's a big bank, probably he had to sign a non-disclosure agreement. So he just probably couldn't share all the details.

**[12:54] SPEAKER_03:** No, no. I mean, I remember at some point, and I can't remember the context, him saying he found it interesting because the consensus for that was on-chain. Like the consensus for that was happening as smart contracts. So it was kind of almost like this pluggable consensus but consensus pulled up into the app layer. So he found that quite interesting. The initial one called Quorum consensus, it didn't last long.

But I think Gav also was doing that sort of stuff on the C++ side, that he did some proof of authority stuff before that happened on the Geth side, before Clique. The was this — okay, well he actually made a different C++ client. So you've got eth, but he made another one that was called like Fluidity or something, which was like pulling all the libraries in the same but it was with a proof of authority consensus. But he did that — that was one of the last things he did before he went out to Parity.

So I think both him and Jeff were interested at that thought of, well, how can you formulate these pieces in different ways for those kind of use cases? Interesting. But yeah, he left. I think it was, I think it was probably very early in 2017. I did find a period but it was certainly ahead of Devcon Three. Let me see if I can find the date.

**[14:44] SPEAKER_01:** Yeah, I don't remember the exact date. And actually, there was maybe there wasn't even a really exact date when Jeff left. No, because basically a month after I joined, Peter Szilágyi joined. And he was the team lead for a very long time. So Jeff basically handed it on to Peter. And for a while he was officially still team lead but not really. We haven't seen him on the calls for...

**[15:13] SPEAKER_03:** No. So the date I found there was February 2017, but I think I got that from GitHub. I think that was like his final commit, but he probably tailed off. Yeah, a long time.

**[15:29] SPEAKER_01:** Yeah, he already started focusing on other stuff like this Quorum stuff and then his own things sometime in '16. So yeah.

**[15:37] SPEAKER_03:** Yeah, so started a company called Grid Games with his brother, just building a particular game, but that also seems to have ceased. So yeah, he's unknown, off in the world somewhere.

**[15:52] SPEAKER_01:** Yeah, that's pretty much all I know about him. We try to invite him a few times to just come to some event and meet up. But yeah, I think for some reasons he really had enough of maybe not us, but things going on in the EF. And yeah.

**[16:09] SPEAKER_03:** I mean yeah, I think that would be the case that when Ming came in she both did legal tidy-up but also cut the spending a lot. You'd had the crowd sale in July, August, September 2014, but coming up to the mainnet release a year later, like nearly all the money was gone.

**[16:36] SPEAKER_01:** Yes, they spent it very fast. Yeah, so Devcon One was a postponed one because of that. Yeah. So and we didn't really feel a lot of this actually. Jeff just said that now that ether price is so low — actually I think the lower point was 42 cents. Yeah, and for a year it didn't really move. And Jeff just said that, okay, we all have to take a pay cut. But the pay cut was really just 10 percent. And I think maybe he took a bigger one. So yeah, for us it was really not that bad.

And the idea was that when ether price reaches two dollars then yeah, we do have some — go back, some time, some money to go forward. So yeah, then our salaries went back. And that wasn't a lot of time. So yeah, actually I don't really remember the price history and maybe it's not the most important thing, but I think ether reached something like $10 pretty soon, like in the start of 2016. Yeah, and we went even a little bit higher, but then we had the DAO fork and the Shanghai attacks. And well, given how turbulent those times were, the markets held pretty well. So yeah, and with $10 ether we could survive further. And yeah.

**[18:18] SPEAKER_03:** Yeah, I mean that was quite a jump up. I mean, I heard that at the worst point there was only four months of runway left. That was how close it was to running out of money. But yeah, there were those big cuts which really resulted in like Gav, Gavin, the C++ team were the main victims of those cuts.

But then yeah, just into 2016 — pardon me, so I was hired in February 2016, same time as Greg Colvin came in. And also Pavel was rehired. He was working through IMAPP, working on that JIT, but that contract stopped, but then he came back at that time as well. So it was this period through late 2015 to early 2016 was like the absolute bottom of, are we even going to ship this thing? Are we going to run out of money before we get to mainnet?

But then yeah, some of us were really coming in as backfill for that C++ team. Yeah. So I mean, Devcon One was sort of, you were mentioning in that series that had got cancelled, but then ConsenSys came in and actually paid for that and said, "Hey, we'll mainly organize it," and kind of so that the thing can happen. So that was the big first public event. So what are your memories of Devcon One?

**[19:55] SPEAKER_01:** Well, my subjective impression was that it's really amazing. Yeah, compared to today's Devcons it was small. I think 300-something people maybe, but I'm not sure about less than a thousand. Yeah. And it was in a really prestigious venue, some old bank building.

**[20:14] SPEAKER_03:** Threadneedle Street, yeah. It's like City of London.

**[20:18] SPEAKER_01:** And yeah, I really felt like, okay, so now this is really a serious thing. And probably that was the reason why ConsenSys stepped in and funded the event, so we really could step up in terms of public appearance and appear something really serious. And yeah, I remember all the big banks having a presence, like booths at Devcon One. Right.

**[20:59] SPEAKER_03:** Yeah, so yeah, and then Microsoft is headline sponsor. It's like, wow, right? Like recognition, right? That you're like, wow, Microsoft are interested and supportive. And yeah, I mean I think for a lot of people it was a real kind of, wow, like this is for real. You know, sadly I could not afford to go. I watched the live stream. I was not quite in and working yet. I was an enthusiastic contributor, but yeah.

**[21:34] SPEAKER_01:** So actually it was also like the first time for me when I met a larger number of Ethereum people. Yeah, I first met the Go Ethereum team in like early '15, and yeah, I went to Amsterdam one more time I think in May. But Devcon One was the place where I really realized how big this thing is. And it's really not just about client developers, but also even back then people presented about formal verification and all this stuff. So yeah, I realized that this is really big and probably everyone wants to be a part of it, at least a little bit.

**[22:20] SPEAKER_03:** Yeah, yeah. I mean, looking back at Devcon One videos, it's like everything — like any kind of use case you could think of, there was somebody presenting about it, so early, more than 10 years ago. But many concepts which were probably like massively too early to do, but maybe you can do them all now seem to be presented. You had Nick Szabo as well, Nick Szabo doing a keynote.

**[22:48] SPEAKER_01:** Yeah, yeah, Nick Szabo was also there.

**[22:52] SPEAKER_03:** So was that maybe the first time that you'd met a number of the people in Berlin, like Christoph Jentzsch and Lefteris Karapetsas and maybe even Gav?

**[23:00] SPEAKER_01:** I think I met some of these people already in London. And I think first time I went to Berlin office, back then it was like the old office. Yeah, right. But so yeah, some people I met at Devcon One, some people I met in Berlin. But yeah.

**[23:24] SPEAKER_03:** Yeah, so no. Was Devcon One the first time that you'd been to do Ethereum things in London, or did you go to any sort of London meetups or meet any of those comms people earlier?

**[23:39] SPEAKER_01:** I didn't go to any meetups in London before. But actually I did — so Viktor Trón was in London at the time, and I went to London around the time, actually if you're doing some event with my old software company, the Hungarian software company. Oh, right. Yeah, so we went to London to sell our software and everything. So I was still working there. And after that, yeah, I met up with Viktor and talked about things.

**[24:23] SPEAKER_03:** Because yeah, he, from what he was describing and then I was looking at videos and things later, he had seen Gav talk in London in very, very early February. I think it was February the 6th. So almost immediately after they'd had the Miami, like BTC Miami launch, Vitalik's first public talk. And Anthony Di Iorio's like mansion where a lot of them met for the first time. Gav had been back in London, I think it was like a week after, and did a talk there that Viktor had gone to. That was Viktor's first in-person meeting with any of these. And then Gav had pulled him on board. Yeah, so those are like the very, very early days.

**[25:22] SPEAKER_01:** I wasn't there. So when I first heard about Ethereum, that was I think March or April '14. So I first heard about the pre-sale. And yeah, that's where I first heard about this thing. But yeah, I know that Gavin was like one of the very early founders of this, and he wrote the Yellow Paper. Yeah, full of Greek letters.

**[25:51] SPEAKER_03:** Yes, very confusing. Yeah, and the C++ client of course. So the first time I think I saw your name or was in contact with you was about light client. Because I'd been trying to get Ethereum ARM Linux cross-builds running on my smartwatch. And my thought there was, get the thing running, and then this light client stuff is just kind of starting. And scaling will be solved, right? We're going to be able to run these nodes on anything. You'll have them on your phone, smartwatch, router. They'll be in every operating system. We'll solve that scaling and that lightness. So you were plunged right into that problem, right?

**[26:38] SPEAKER_01:** Yeah, so when Jeff hired me, actually he put me on this project. So he just said that, okay, it's great that I contributed to Swarm, but if I joined the Geth team, I will have to start working on the light client because it's a very important thing and it hasn't been started yet. Yeah, so I felt really good about it. Like, I also felt like this is a big thing.

And yeah, back then it really felt like we do these few things, we have a working light client protocol and the whole eternity of a base layer and then we're all good. Yeah, but it wasn't that easy. But still those were the first steps. And so I designed the LES protocol. Yeah, in retrospect it didn't make a lot of sense to build it over the devp2p layer, because yeah, it wasn't easy to access from web browsers and stuff. But also it was a proof of work based light client. So yeah, that project ended after a while.

But I'm still very much into trustless chain access. So that has usually been one of my focuses all the time. Right now I'm also working on something called the trustless execution layer API, which is similar to the Beacon REST API but works on the execution layer and provides everything with proofs. So yeah, I'm still very much into this because I think this is where it really makes sense, if even normal users access chain data with proofs.

**[28:36] SPEAKER_03:** Right, right. And there was a project called Portal as well. Were you involved with Portal? That was a later kind of like client?

**[28:42] SPEAKER_01:** No, I wasn't. So Portal was Piper Merriam's brainchild. And yeah, so by the time we kind of realized that LES was a nice first experiment but maybe not the best approach, he started something different that was UDP-based and also used different topologies. So it was kind of a DHT approach to storing the chain and the state.

And yeah, actually I think it's a bad thing that it's been completely canceled. Because well, actually to be honest, I never really believed that it will be an easily solvable problem to store the Merkle Patricia trie of the state on the DHT. But for the chain data, yeah, it made perfect sense.

So yeah, maybe the state would have been possible with a lot of work. But yeah, I mean, Piper told me a few times about how he imagines the order to solve all the unsolvable problems, and I felt like, yeah, it sounds good, but he just made a lot of really hard assumptions about DHTs. That I — by that time I already worked on Discovery v5. So there was also this discovery protocol that basically we designed it in 2016 in Berlin with Felix, and I released the original version.

And yeah, so I already knew that it's never so easy to imagine a DHT that's efficiently formed, that all the nodes are working. And yeah, so but for the chain data, right, especially with EIP-4444, so that lets the main protocol nodes processing main protocol forget the old chain history, right? So it made perfect sense to at least put the chain history on a DHT. But yeah, it was an EF decision that it was discontinued at a point.

**[31:06] SPEAKER_03:** Well, I mean I guess the thing is, Patricia Merkle tries are not great for the number of accesses and things anyway, let alone if you're making each of those steps over a networked DHT kind of setup. That's, yeah, there's a lot of... it's so much transactional change.

**[31:32] SPEAKER_01:** Yeah, complexity. State trie suffers from a lot of issues, especially in a Merkle Patricia state trie. Yeah, and it's a huge data set that keeps changing all the time and keeps changing at completely random places. Yeah, and it's not as easy a task to distribute it. So actually it's getting harder to even synchronize it between the full nodes, the entire state. Yeah.

**[31:59] SPEAKER_03:** So do you think that proofs are going to be a magic silver bullet here? Where by having local proofs versus massive, really redundant state machines — do you think there's a path here where...

**[32:24] SPEAKER_01:** Oh yeah, no, it's not a silver bullet. So I assume you mean what people call statelessness. So it's a good thing. It definitely allows a higher degree of scaling. But the state tree still has to be processed and maintained by someone. And especially if most of the nodes have no incentive to process it. Yeah.

And it — and yeah, now we are talking about 100x and 1000x scaling, then even if we also do state expiry, which is currently imagined in a way that we basically reset the state tree every year or something, and have multiple state trees — so yeah, that helps somewhat. But if we scale a thousand x, then it will be a huge infrastructural centralization issue.

And yeah, by the way, this thing is not an unsolvable problem. I mean, the state as it works today, yeah, unfortunately somehow makes it really hard to do any fundamental improvements over these properties. But people are considering different storage architectures. Yeah, of course we have to keep the existing contracts workable because that was our main promise from the beginning, right? But we will not just shut down anything. Yeah, everything has 100% uptime. But it is a viable way to come up with more efficient storage methods and use it as an opt-in alternative that will over time be available for much less. And new contracts can be designed using those more efficient storage architectures.

**[34:26] SPEAKER_03:** Yeah, because Verkle trees seem to be the first sort of thought on that, but then those, yeah, that's kind of come and gone. And maybe it's a binary tree or actually it does — either...

**[34:40] SPEAKER_01:** I mean, both are better than the Merkle Patricia trie, yeah. But in some ways. But they don't solve this fundamental issue by themselves. So still the thing is that the state is a permanent key-value store, and in order to avoid it growing forever, yeah, there's all these ideas about state expiry. But still it's going to be a huge data set. And the method of hashing or consensus, protocol representation doesn't fundamentally change this.

So Verkle was supposed to provide more efficient Merkle proofs, but also I guess somewhat more expensive state processing because it's more expensive cryptography. Right. Also, if I'm correct, it's not quantum secure. So, right, right. And that was also a thing where I always felt like, yeah, I'm not sure if it's a good idea to start working on now. And I just saw it in front of my eyes how it's going to be cancelled. And yeah, so yeah.

**[36:04] SPEAKER_03:** I mean, I guess for running nodes in general, there's not a lot of incentive for people to run any kind of node software themselves unless they are a validator or they're running an exchange or a business and they need their back end to that. I guess the vision that there was at the start of, like, well, yeah, everyone will be running their own node, and you've got Mist on top of it and it's local apps. And then that can have Swarm for the smart contracts, and it's almost like you won't have server architecture because everyone's running a server stack. And then yeah, that did not happen.

**[36:47] SPEAKER_01:** Actually, actually, that's so that's why we are also stuck with the JSON-RPC API which doesn't provide proofs, except for eth_getProof, but doesn't provide proofs for a lot of things. Because it was never meant to be used remotely. It was always imagined that yeah, it's used locally in a trusted setup on your own machine. And yeah, I remember all those good old days when I just synced up a full node, it was a few gigabytes of disk space, and ran Mist on top of it. And yeah, all the — it's magic. But yeah, unfortunately it didn't scale. No, no.

**[37:29] SPEAKER_03:** At the Museum of Ethereum here, I've got laptops running Geth 1.3.6, so Homestead Geth. And I mined Homestead back to life. So any hard fork that happens, the other old one doesn't go away, right? It doesn't disappear. It's just people don't associate any economic value with it and it kind of gets abandoned. But yeah, what I've done is first GPU and then down to CPU-mined that Homestead difficulty down to the level that you can CPU mine it again.

So I do, I have got Mist running on those. So we can go, we can transact. We can send a transaction between those and it should be possible to run AlethZero and AlethOne and Mix on that as well. I haven't had time to do that. But and ERC-20 tokens existed, you could have DAO tokens or MistCoin. Yeah, at that time. But yeah, the assumption that people would run their own node and it would all be self-sovereign local apps certainly did not come to fruition.

**[38:56] SPEAKER_01:** Well, yeah, that's when the light client came in, and then we assumed that, okay, then we do the light client and yeah, it will be all solved.

**[39:00] SPEAKER_03:** That's it. Yeah, that's what I was thinking is like, right, I've got a full node running on my smartwatch, that works, and I'll just wait for you and the other guys to sort out light client and just turn that on and there we go.

**[39:11] SPEAKER_01:** Well, actually the light client protocol worked fine. It's just, yeah, I spent like a really crazy amount of time figuring out how it could be decently incentivized in a truly decentralized way. Because yeah, I remember this — there was this idealism that, yeah, now we are almost done with everything, so we just have to find a real proper way for incentivizing things. But not in a way that there's a few companies where you can buy tokens, but truly in a decentralized way, which is much harder. Because yeah, then we have to somehow build decentralized trust and figure out market mechanisms that work without initial trust.

So yeah, this is something I spent years with. And honestly, I think I came up with some nice theoretical models and a lot of really complex code. But yeah, it's just, again, was like the wrong approach, maybe also at the wrong time. So we were just not there really. Yeah.

**[40:29] SPEAKER_03:** Because I mean, BitTorrent has obviously worked for distributing content for many years. But then you do have this tragedy of the commons, right? Yes, the latest Hollywood movie someone has ripped off and people want that, so that's going to get shared around, no problem. But things which are only of interest to a smaller number of people, without incentives it's just a leeching problem, right? Good full node runners would contribute, they'll turn on the LES as well, right? They would help supply that. But the incentives and economics are not easy.

**[41:16] SPEAKER_01:** Yeah, actually with BitTorrent it also usually, if you really want to use it, it requires trackers where you buy some priority access. So right, there are these private trackers and everything. Yeah, so and those are, this is also not completely decentralized, but actually it does work. So it's definitely better than nothing.

But for LES it wasn't really this easy, because this whole service was — like downloading movies was an application that everyone understood, that everybody used. And somehow with Ethereum it was always this, yeah, everyone felt the importance, but if you're nowhere near close to a really mature ecosystem — and so it was just, I don't think there would have been a big enough market really for these services, so that to really work out in a market-based way.

Yeah, but as we scale and accessing the whole dataset becomes more and more difficult, at a certain point I think we are going to have something like I reimagined several years ago. So yeah, it's just both timing and specifics. I was right about everything except timing and specifics.

**[42:51] SPEAKER_03:** Yeah, yes, yes. I mean, there's a number of things that seemed like they would be easy and quick and obvious and have taken so many years. I mean, like proof of stake, it was in the white paper. There was an assumption later in 2015 that that'll happen within six months, maybe three to six months. And then it's eight years before it actually went live.

And yeah, I mean, on storage, so Filecoin, their first white paper was in 2014 as well. Filecoin was not a new thing. And IPFS was around before Ethereum as well. And then yeah, Whisper kind of went for a while. And then now there's — and you'd have had Status driving a lot of those techs for a lot of those years as well. Jarrad Hope and team, who were also doing an Android version of the Java client, the same kind of time as I was looking at smartwatches.

**[44:06] SPEAKER_01:** Yeah, Jarrad Hope was also very eagerly waiting for the fully functional light client. Yeah.

**[44:12] SPEAKER_03:** Yeah, well, because they were building kind of decentralized WeChat, super app. But I guess kind of a competitor to Mist, really. Similar kind of thing, wanting to have a container for running dapps in, sitting on top of a local client. Again, having this completely self-sovereign kind of server app stack. But not easy.

And I can't remember who it was that was telling me that, so when they first saw MetaMask, which was at Devcon One — that was one of the grantee winners, was MetaMask — them thinking, "No, we — that's not what we want. We don't want some browser extension thing talking to a trusted endpoint. Like, that's absolutely the opposite. What are these guys doing?" And then that's become the standard flow, right?

**[45:18] SPEAKER_01:** Well, yeah, so this is still kind of an unsolved problem, to access everything in a truly decentralized way. But I think we are getting there over time. It's just, yeah, nothing is as simple as we initially imagined. And also there's a time for everything. And I think through decentralized infrastructure will be forced by scaling. And things sometimes just don't happen if they are not forced by some circumstance, some fact, some external factor. So yeah, as long as it works in a lazy way to just connect MetaMask to Infura, yeah, until then it's the standard way. Yeah.

**[46:15] SPEAKER_03:** Yeah. So I think I found two different talks of yours at Devcons talking really about light client. Do you remember, did you talk in London, or was Shanghai your first?

**[46:22] SPEAKER_01:** No, I talked at London, also Shanghai, and also in Cancun. Yeah, so those were the first two Devcons that were mostly about the light client. So they actually, the first release of the light client protocol was in '16, so it was around that time.

And later I already started to invent all the next chapters of decentralized technology. And yeah, it was really naive of me. But I also had this project back then where I started to try to make logs provable efficiently. And yeah, that was — so the initial attempt for that was in 2017 and now I'm back at it. Now I also have this trustless log index project. Yeah.

And so, all the approaches — 2017, that was just a more efficient way to organize the bloom filters, but it didn't really solve the problem of the bloom filters not adapting to the number of events. And also, I never even proposed putting it into consensus, which would have allowed the actual trustless proofs through the chain. So yeah, that also proved to be a hard problem, but yeah, this is one of the things what I presented in Cancun.

Right, right. Oh yeah, and also some kind of my ideas of state channels. So back then we didn't have L2s in a way. So actually, back then "layer two" just meant something that happens off-chain, not necessarily another blockchain. Yeah. And so yeah, I had these ideas about individual nodes all running their own blockchains and somehow organizing some off-chain calculations through that. But yeah, it also assumed a lot about how those would operate and probably would have never worked.

**[48:50] SPEAKER_03:** Yeah, I suspect, right. Yeah. So yeah, I mean we had state channels and then we had Plasma, and then eventually coming into optimistic rollups and then ZK later. Just many, many different attempts. So in terms of the Geth team, has that been similar over the years? Or have you had larger and smaller amounts of people? Has it been a similar kind of flow through that time?

**[49:36] SPEAKER_01:** I would say it was pretty consistently around 10 people throughout all these years. Sometimes eight, nine, sometimes 11, 12, but really in this range. We did improve our internal processes during the years, so yeah, now we do have all this issue and pull request triages and yeah. But really it's been, mostly that team was also always small enough so that we didn't need a lot of processes.

Right, honestly, the team culture, yeah, it did obviously change, especially with certain people coming and going. But I would also say it was always a good team culture. I always liked the Geth team. That's also why I never really looked into moving to other teams or other projects, because I felt that team is the best place to do meaningful things.

**[50:54] SPEAKER_03:** Yeah. I mean, it's funny because from the very start of Ethereum, the intention was to have multiple clients. Right, that was a very basic decision of saying we want a separation between the specification and the implementation, right? Because we don't want it to be like Bitcoin where you've got one codebase and then there's no competition, there's no...

**[51:21] SPEAKER_01:** Well, yeah, for Bitcoin's complexity that approach worked. But for Ethereum's complexity, I would say this was one of the best decisions. Yeah, it also contributed to almost running out of money by the time we launched mainnet. But I would say it was money well wasted. So...

**[51:43] SPEAKER_03:** Yes. No, I would agree. It was not efficient, but the outcome was very much worthwhile. Yeah.

**[51:52] SPEAKER_01:** And when we switched to proof of stake, we again successfully applied this pattern by running, by funding multiple CL implementations. And then testing every EL against every CL. Yeah, and then — yes, that's with all the combinations.

**[52:08] SPEAKER_03:** Five — is it five different primary consensus clients?

**[52:12] SPEAKER_01:** There are, I think it's five. Yeah.

**[52:15] SPEAKER_03:** And yeah, notably none of those were within the Foundation either. They were all independent companies and teams. So I mean, on the execution side there have been a good number of different alternative execution clients over the years. So I mean, how do you tend to work and interact in that kind of environment where you've got all these different — I guess starting with Parity, and then Besu and Nethermind, Erigon? So how do you work with other teams?

**[52:58] SPEAKER_01:** Well, we have now, we have all the ACD calls and testing calls. So mostly, I mean, we all do have working clients all the time. So by default we don't need to interact a lot. We have to interact when we are testing out new features. Yeah, there are the proper forums for that. So yeah.

And oh, it's also — some people keep more contacts outside of the Geth team, some people are more turning inwards and then just focusing on Geth issues. Yeah. But actually I think in the first years, communication was really not organized as well. So we really just tried to figure out things. And some people knew some people from the other teams, and yeah.

But actually these days we have much better processes for this. Also it's a much, much bigger challenge because there's so many more people. Actually, this is also something I realized during the time we really started working on proof of stake. So in 2017, it was the first time ether price went to several thousand dollars, and yeah, the Foundation had money to hire new teams and fund external teams.

And I remember that until 2017, I mostly met non-Go Ethereum people mostly at Devcons. Yeah. And maybe those people who lived in Berlin or one of those cities where there were multiple people, they met more people. But I was always in Hungary and worked remotely. And yeah, I mostly met most of the people at Devcons.

But around, I think it was 2018, when so many researchers and have been hired, and there were also the CL teams. And I remember Devcon 4 at Prague. Yeah, it was — so until then it was mostly, I don't know how many people exactly, but I do remember maybe 30, 40 people, I don't know. After every Devcon we stood up at the main stage and the group photo — "Oh yeah, we are the Ethereum Foundation." Yes, like it was that many people. And in '18 I was just shocked, like, who the hell are all these people? The whole Ethereum Foundation. Yeah, so it became a much bigger challenge. But also now we do have all these official forums. And also I try to go to more events, not just Devcons, in order to keep all the contacts live. Yeah.

**[56:00] SPEAKER_03:** Yeah. So I mean, looking back to when you first started working on Ethereum, did you have any kind of thought or vision of what things might have looked like 10 years later? Like, has it worked out as you expected or differently? Or what's — what's your looking back on these 10 years, what's your thought?

**[56:24] SPEAKER_01:** I always had a lot of visions. Yeah, maybe I was too focused on vision sometimes. Yeah. So the thing is that we all kind of have to imagine the future at every point, even though we know we can't imagine it as it will turn out. Yes, it never turns out exactly the way we want. But we always have to have some kind of direction, and we have to just have ideas of how things can turn out.

So yeah, around like 2017 I also realized that scaling will not happen just with L1. So yeah, I also had these ideas about how we could solve problems more efficiently with not even rollups, just application-specific state channels and stuff like that. Yeah. But it also — there was this really great project — oh, okay, I don't — yeah, right then...

**[57:20] SPEAKER_03:** Raiden.

**[57:21] SPEAKER_01:** Yeah, thank you. Thank you. So yeah, they properly implemented the protocol and everything. Yeah, I think it has always struggled with not many people using it. So it's like — there's a problem. It's a pain that the transactions are expensive, but still somehow maybe we just missed some organizing force to really move to some kind of layer two solutions. Yeah.

**[58:08] SPEAKER_03:** And it was meant to be Lightning for Ethereum, right? That was the thought.

**[58:12] SPEAKER_01:** Well, yeah, it was pretty much that idea. But then Lightning's kind of failed. So maybe not surprising if an Ethereum version of that's not really got...

**[58:24] SPEAKER_03:** Because you have routing issues, right? It's really complicated.

**[58:28] SPEAKER_01:** Yes, the channels seem to work great for consistent static topographies. If you want to do merchant to merchant, channels work great. Yeah, but opening those channels is still costly and non-trivial. And yeah, it's just — I also never really, I installed it, I tried it. Okay, this is interesting. But yeah, I never really made a payment through Raiden because there was just no occasion where the other party really wanted a Raiden transfer.

**[59:11] SPEAKER_03:** No, no. Well, thank you very much. I think we can wrap it up there. Okay. So thanks for your time, and thanks for all of your work on Geth over these very many years. Geth has always really been the backbone of Ethereum. New clients come and go, but Geth remains. Yeah.

**[59:35] SPEAKER_01:** So thank you. Thank you for having me here.

**[59:41] SPEAKER_03:** Okay. Thank you.