**[00:01] SPEAKER_03:** So, hello and welcome to ETHDenver. So here recording for Early Days of Ethereum with Zsolt Felföldi. How do you pronounce your name? Zsolt? Zsolt. There you go. Anyway, so yeah, I was working out when we recently reconnected at Devconnect, and I was working out that you're the third longest person at the Ethereum Foundation, right? That you've got Vitalik and then...

**[00:34] SPEAKER_01:** Felix, and then you. Yeah, I haven't really checked this fact yet, but honestly, yeah, it...

**[00:44] SPEAKER_03:** Sounds great, that's it. So I mean, you're a very long-time member of the Geth team.

**[00:58] SPEAKER_01:** Yes.

**[00:58] SPEAKER_03:** But what were you doing before you started at the Foundation? What was your background? How did you find your way into the blockchain world?

**[00:58] SPEAKER_01:** Well, before Ethereum, I was working on really different types of projects. I first started at a Hungarian software company, like a really classic software company. We actually sold software in boxes, like put on a shelf, discs. Like floppy disks, put in a box on a shelf, and you can buy the software. So like this type of classic software. Five-and-a-quarter-inch floppies. Actually, three-and-a-half. We're on to modern floppies! But maybe also, I started in '97, so maybe I was exaggerating a little. So by that time it was mostly CDs, but we still used a lot of floppies anyway.

So at that company, I did things related to computer graphics. I wrote a ray tracing engine for some architectural software, and then I also did a lot of work on electronic circuit simulation and circuit design. So really different things. And it was around 2011 when I first heard about Bitcoin, and around 2012 when I started to realize that, as weird as it sounds, it really is probably a big thing.

And actually, I first heard about Ethereum early 2014, a few months after the initial paper had been published. And I started contributing, I think around November, and officially joined the EF...

**[03:02] SPEAKER_03:** ...in March 2015. So yeah! And did you hear about it, do you think, through Dani and Viktor or some other way?

**[03:10] SPEAKER_01:** Well, I did hear about it from Dani and Viktor's friend circle. But then Viktor was already... actually I didn't know Viktor before. So I heard about this thing through one of his friends. And then Viktor was also in that wider circle, and he came to Hungary and said, "Oh, I'm already working on this." And then I started with my ideas and started to explain to him why this thing probably will never work. And he was like, "Okay, you seem to have a good understanding of this. Why don't you come to work?"

**[03:52] SPEAKER_03:** Right, right, right. So yeah! And am I right in thinking that you said it was Swarm that you started with?

**[03:59] SPEAKER_01:** Well, yeah. So Swarm was part of this initial trinity of base technologies of Ethereum. It was supposed to be the storage layer for dapps. I mean, it was kind of a naive way of how people imagined decentralized applications back then, but honestly, it made sense at the time. So I will say that nothing ever turned out exactly the way that people imagined it, but we are still making a lot of progress.

So yeah, Swarm was how we initially imagined the storage layer for Ethereum. And I mean, this project still has merits, but this whole problem space is just a bit more complex. So I started contributing to Swarm first, and actually I wrote the first 500 lines...

**[05:02] SPEAKER_03:** ...of Swarm, there you go! Yeah, I mean, I think if I remember rightly that Viktor mentioned around May 2014 was when he first heard that trinity. That this concept that you could have Ethereum as your compute and expensive database, Swarm as your decentralized storage, and then Whisper as your messaging. There's that famous diagram, right? With the circle and the things coming in and Whisper going around the edge, and there's another one of those. But I guess it was Devcon 0 where Dani really presented a fleshed-out vision of what that decentralized storage...

**[05:51] SPEAKER_01:** Yes, that's correct. I wasn't there at Devcon 0 yet, so I've heard about this idea even before I heard about Ethereum. Dani already told me about this idea that he wants to do this kind of hash-based chunk storage. And it made total sense that he just pitched that so that can fit in. At the time it was a perfect fit.

So he pitched this idea at Devcon 0, and when they accepted it and hired Dani, then Dani called me and said—because he already knew that I know of this project—"Let's do it together." So there you go.

**[06:40] SPEAKER_03:** And then so you were hired into ethdev. I did have a date for that, I've forgotten. I guess it was shortly after Devcon 0 that you started there, correct? Did you go to Berlin or Amsterdam? When did you first meet other people? How did it...?

**[07:07] SPEAKER_01:** It was Amsterdam in February '15. That's where I met Jeffrey Wilcke, the creator of go-ethereum, and the go-ethereum team back then. I don't say Geth because that abbreviation was invented later. So yeah, that's where I met the go-ethereum people. I already had these contributions to Swarm, and it was kind of an implied thing that maybe I might be hired, but there was really no official hiring process back then.

It was really just... Jeff was this really laid-back guy, and he just said, "Okay man, I saw your contributions, and let's talk sometime this week." And I waited the whole week and waited for some serious interview. It was a dream job for me. By that time, I was really enthusiastic about this whole thing. And I felt like, even though I felt that this whole initial design was... I really couldn't imagine how it would scale and everything, and it is a hard problem... it was true, but it was still worth starting it.

I was really enthusiastic and I really wanted to get hired. And the whole week I just waited, and at the end of the week, like the last half an hour before we all left home, Jeff just said, "Oh yeah, when I wanted to talk to you... you're hired."

**[08:47] SPEAKER_03:** Okay, that's a good talk! So yeah, this is how the hiring process went back then. Excellent, well that's easy, we like that. And so that was before you went to Amsterdam, I assume? I assume you went to Amsterdam after you had been hired?

**[09:07] SPEAKER_01:** No, no, no, it happened in Amsterdam. So Jeff agreed that if I bought my own plane ticket, I could stay at the Airbnb where the whole team stayed, and I just worked with them and showed my contributions. So I went to Amsterdam unhired, but yeah.

**[09:29] SPEAKER_03:** Right, right, that plane ticket was a good investment! So yeah, did they not have office space at that point even?

**[09:35] SPEAKER_01:** Well, they did. Actually, back then there was an Amsterdam office. It was mostly for Jeff, because Jeff lived in Amsterdam. But when Jeff left, or maybe before that, I'm not sure exactly, this office was closed. And actually it was a really small office. Last time I checked now, I think a dentist works there. It doesn't exist, but it was really just a small place.

But later I went to Berlin a lot after I was hired and it was for the Geth team, it was really centered in Berlin.

**[10:27] SPEAKER_03:** Right, right, because as well as Jeff, you've got Bas, right? Bas van Kesteren. He was another Amsterdam person. But then maybe most of the other team members weren't in Amsterdam.

**[10:41] SPEAKER_01:** Yeah, no one else was. We were quite distributed. Bas was there for a relatively short time, and Jeffrey also left after a while, and started his own company.

**[10:57] SPEAKER_03:** Right, developed games or something. I think EthLab was another one. Do you know anything about EthLab? Because when Jeff worked with JP Morgan to do Quorum, that was announced under the label EthLab.

**[11:20] SPEAKER_01:** I think I heard the name, but I didn't really know what it does. But this is something I knew, that Jeff started working with JP Morgan back then. And in that time, big banks really wanted to just talk to us at every Devcon, and we were always invited to fancy dinners by some main people. So banks really wanted to learn about the technology. So Jeff went for a while to work on Quorum, yes, true.

**[11:56] SPEAKER_03:** Yeah, I mean unless I can somehow get in contact with Jeff, I guess it's a little bit of a mystery what exactly EthLab was. Though I suspect it might be a little bit like the Ethereum Foundation, just being a name, a banner for activities rather than a legal entity. And another thing I don't know there, but I suspect, is I don't think Jeff told Ming that he was doing that stuff with JP Morgan. I suspect that he completely just did that on his own without any communication with Ming or with the EF. It's just...

**[12:34] SPEAKER_01:** Well, actually, he never really told a lot to us about that. So we knew that he's working with JP Morgan, but probably, like it's a big bank, he had to sign a non-disclosure agreement. So he probably couldn't share all the details.

**[12:54] SPEAKER_03:** No, I mean, I remember at some point, and I can't remember the context, him saying he found it interesting because the consensus for that was on-chain. Like the consensus for that was happening as smart contracts. So it was kind of almost like this pluggable consensus, but consensus pulled up into the app layer. So he found that quite interesting that the initial Quorum consensus. It didn't last long, but I think Gav also was doing that sort of stuff on the C++ side. He did some proof of authority stuff before that happened on the Geth side, you know, before Clique.

He actually made a different C++ client. So you've got eth, but he made another one that was called something like Fluidity, which was pulling all the libraries in the same, but it was with a proof of authority consensus. He did that as one of the last things he did before he went out to Parity. So I think both him and Jeff were interested in that thought of, "Well, how can you formulate these pieces in different ways for those kind of use cases?" Interesting.

But yeah, he left... I think it was probably very early in 2017. I did find a period, but it was certainly ahead of Devcon 3. Let me see if I can find the date.

**[14:44] SPEAKER_01:** And actually, maybe there wasn't even a really exact date when Jeff left. Because basically a month after I joined, Péter Szilágyi joined, and he was the team lead for a very long time. So Jeff basically kind of handed it on to Péter. And for a while he was officially still team lead, but not really. We haven't seen him on the calls for...

**[15:13] SPEAKER_03:** No, so the date I found there was February 2017. But I think I got that from GitHub. I think that was like his final commit, but he probably tailed off a long time before.

**[15:29] SPEAKER_01:** Yeah, he already started focusing on other stuff, like this Quorum stuff and then his own things, sometime in '16.

**[15:37] SPEAKER_03:** Started a company called Grid Games with his brother just building a particular game, but that also seems to have ceased. So he's unknown off in the world somewhere.

**[15:52] SPEAKER_01:** Yeah, that's pretty much all I know about him. We tried to invite him a few times to just come to some event and meet up, but I think for some reasons he really had enough of maybe not us, but things going on in the EF.

**[16:09] SPEAKER_03:** Yeah, I think that would be the case. When Ming came in, she both did legal tidy up but also cut the spending a lot. You had the crowd sale in July, August, September 2014, but coming up to the Mainnet release a year later, nearly all the money was gone.

**[16:36] SPEAKER_01:** Yes, they spent it very fast. So that Devcon 1 was a postponed one because of that. And we didn't really feel a lot of this, actually. Jeff just said that now that ether price is so low—actually, I think the lowest point was 42 cents, and for a full year it didn't really move—and Jeff just said that, okay, we all have to take a payment cut. But the payment cut was really just 10 percent, and I think maybe he took a bigger one. So yeah, for us it was really not that bad.

And the idea was that when ether price reaches two dollars, then we do have some money to go forward. So then our salaries went back. And that wasn't a lot of time. So actually, I don't really remember the price history, and maybe it's not the most important thing, but I think ether price reached something like ten dollars pretty soon. Like in the start of 2016. And we went even a little bit higher, but then we had the DAO fork and the Shanghai attacks. Given how turbulent those times were, the markets held pretty well. So with ten-dollar ether price we could survive further, and yeah.

**[18:18] SPEAKER_03:** Yeah, I mean that was quite a jump up. I heard that at the worst point there was only four months of runway left. That was how close it was to running out of money. But yeah, there were those big cuts which really resulted in like Gav and the C++ team were the main kind of victims of those cuts.

But then just into 2016, pardon me, so I was hired in February 2016, same time as Greg Colvin came in and also Pavel was rehired. He was working through IMAP, working on that JIT, but that contract stopped, but then he came back at that time as well. So this period through late 2015 to early 2016 was like the absolute bottom of "Are we even going to ship this thing? Are we going to run out of money before we get to Mainnet?" But then yeah, some of us were really coming in as backfill for that C++ team.

So Devcon 1 was sort of you were mentioning in that series that had got cancelled, but then ConsenSys came in and actually paid for that and said, "Hey, we'll mainly organize it and kind of so that the thing can happen." So that was the big first public event. What are your memories of Devcon 1?

**[19:55] SPEAKER_01:** Well, my subjective impression was that it's really amazing. Compared to today's Devcons, it was small. I think three hundred something people, maybe less than a thousand. And it was in a really prestigious venue, some old bank building on Threadneedle Street. It's like the City of London. And yeah, I really felt like, okay, so now this is really a serious thing.

And probably that was the reason why ConsenSys stepped in and funded the event, so we really could step up in terms of public appearance and appear something really serious. And I remember all the big banks having a presence, like the booth at Devcon 1.

**[20:59] SPEAKER_03:** And then Microsoft as headline sponsor! It's like wow, recognition, right? That you're like, wow, Microsoft are interested and supportive. And yeah, I mean, I think for a lot of people it was a real kind of wow, like this is for real! Sadly, I could not afford to go. I watched the live stream. I was not quite in and working yet, I was an enthusiastic contributor, but yeah.

**[21:34] SPEAKER_01:** Actually it was also the first time for me when I met a larger number of Ethereum people. I first met the go-ethereum team in early '15, and I went to Amsterdam one more time I think in May. But Devcon 1 was the place where I really realized how big this thing is. And it's really not just about client developers, but also even back then people presented about formal verification and all this stuff. So I realized that this is really big and probably everyone wants to be a part of it, at least a little bit.

**[22:20] SPEAKER_03:** Yeah, yeah, I mean looking back at Devcon 1 videos, it's like everything. Any kind of use case you could think of, there was somebody presenting about it. You know, this so early, more than 10 years ago, but many concepts which were probably massively too early to do, but maybe you can do them all now, seemed to be presented. You had Nick Szabo as well, Nick Szabo doing a keynote.

**[23:00] SPEAKER_01:** Yeah, Nick Szabo was also there.

**[23:02] SPEAKER_03:** So was that maybe the first time that you'd met a number of the people in Berlin? Like Christoph Jentzsch and Lefteris, and maybe even Gav?

**[23:00] SPEAKER_01:** I think I met some of these people already in London, and I think the first time I went to the Berlin office, back then it was the old office. But some people I met at Devcon 1, some people I met in Berlin.

**[23:24] SPEAKER_03:** So was Devcon 1 the first time that you'd been to do Ethereum things in London? Or did you go to any London meetups or meet any of those people earlier?

**[23:39] SPEAKER_01:** I didn't go to any meetups in London before, but actually I did... so Viktor was in London at the time, and I went to London around the time, actually doing some event with my old software company, the Hungarian software company. So we went to London to sell our software and everything, so I was still working there! And after that, yeah, I met up with Viktor and talked about things.

**[24:23] SPEAKER_03:** Because yeah, he... from what he was describing, and then I was looking at videos and things later, he had seen Gav talk in London in very very early February. I think it was February the 6th. So almost immediately after they'd had the Miami b2c launch, Vitalik's first public talk, and Anthony Di Iorio's mansion where a lot of them met for the first time. Gav had been back in London, I think it was a week after, and did a talk there that Viktor had gone to. That was Viktor's first in-person meeting with any of these, and Gav had pulled him on board.

**[25:22] SPEAKER_01:** Those are the very, very early days, I wasn't there. So when I first heard about Ethereum, that was I think March or April '14. So I first heard about the pre-sale, and that's where I first heard about this thing. But yeah, I know that Gavin was one of the very early founders of this, and he wrote the Yellow Paper.

**[25:51] SPEAKER_03:** Full of Greek letters, yes. Very confusing. And the C++ client, of course.

So the first time I think I saw your name or was in contact with you was about light client. Because I'd been trying to get Ethereum ARM Linux cross-builds running on my smartwatch, and my thought there was, get the thing running, and then this light client stuff is just kind of starting, and scaling will be solved, right? We're going to be able to run these nodes on anything. You'll have them on your phone, smartwatch, router... they'll be in every operating system. We'll solve that scaling and that lightness. So you were plunged right into that problem, right?

**[26:38] SPEAKER_01:** Yeah, so when Jeff hired me actually, he put me on this project. So he just said that, okay, it's great that I contributed to Swarm, but if I join the Geth team, I will have to start working on the light client because it's a very important thing and it hasn't been started yet. So I felt really good about it. I also felt like this is a big thing.

Back then it really felt like we do these few things, we have a working light client protocol and the whole eternity of a base layer, and then we're all good. But it wasn't that easy! But still those were the first steps. So I designed the LES protocol. In retrospect, it didn't make a lot of sense to build it over the devp2p layer because it wasn't easy to access from web browsers and stuff. But also it was a Proof of Work-based light client.

So that project ended after a while. But I'm still very much into trustless chain access. That has usually been one of my focuses all the time. Right now, I'm also working on something called the Trustless Execution Layer API, which is similar to the Beacon REST API, but works on the execution layer and provides everything with proofs. So I'm still very much into this because I think this is where it really makes sense if even normal users access chain data with proofs.

**[28:36] SPEAKER_03:** Right, right. And there was a project called Portal as well. Were you involved with Portal? That was a later kind of light client?

**[28:42] SPEAKER_01:** No, I wasn't. So Portal was Piper Merriam's brainchild. And by the time we kind of realized that LES was a nice first experiment but maybe not the best approach, he started something different that was UDP-based and also used different topologies. So it was kind of a DHT approach to storing the chain and the state.

Actually, I'm kind of... I think it's a bad thing that it's been completely canceled because, well, honestly I never really believed that it will be an easily solvable problem to store the Merkle Patricia Trie of the state on the DHT. But for the chain data, it made perfect sense. Maybe the state would have been possible with a lot of work. But I mean Piper told me a few times about how he imagines to solve all the unsolvable problems and I felt like yeah, it sounds good, but he just made a lot of really hard assumptions about DHTs.

By the time I already worked on Discovery v5. There was also this discovery protocol that basically we designed in 2016 in Berlin with Felix, and I released the original version. So I already knew that it's never so easy to imagine a DHT that's efficiently formed, that all the nodes are working... but for the chain data, right, especially with EIP-4444. Like that lets the main protocol, the nodes processing main protocol, forget all chain history. So it made perfect sense to at least put the chain history on a DHT. But it was an EF decision that it was discontinued.

**[31:06] SPEAKER_03:** Well, I mean I guess the thing is, Merkle Patricia trees are not great for the number of accesses and things anyway. Let alone if you're making each of those steps over a networked DHT kind of setup. There's a lot of transactional change.

**[31:32] SPEAKER_01:** Yeah, complexity... the state tree suffers from a lot of issues, especially the Merkle Patricia State Trie. And it's a huge data set that keeps changing all the time, and keeps changing at completely random places. And it's not an easy task to distribute it. Actually, it's getting harder to even synchronize it between the full nodes storing the entire state.

**[31:59] SPEAKER_03:** So do you think that proofs are going to be a magic silver bullet here, where by having local proofs versus massive really redundant state machines... do you think there's a path here where...

**[32:24] SPEAKER_01:** Oh, no, it's not a silver bullet. So I assume you mean what people call statelessness. So it's a good thing, it definitely allows a higher degree of scaling, but the state tree still has to be processed and maintained by someone. And especially if most of the nodes have no incentive to process it... and now we are talking about a 100x and 1000x scaling, then even if we also do state expiry—which is currently imagined in a way that we basically reset the state tree every year or something and have multiple state trees—that helps somewhat.

But if we scale 1000x, then it will be a huge infrastructural centralization issue. And by the way, this thing is not an unsolvable problem. I mean, the state as it works today unfortunately somehow makes it really hard to do any fundamental improvements over these properties. But people are considering different storage architectures. Of course, we have to keep the existing contracts workable because that was our main promise from the beginning. We will not just shut down anything, everything has 100% uptime. But it is a viable way to come up with more efficient storage methods and use it as an opt-in alternative that will over time be available for much less, and new contracts can be designed using those more efficient storage architectures.

**[34:26] SPEAKER_03:** Yeah, because Verkle trees seem to be the first sort of thought on that, but then that's kind of come and gone, and maybe it's a binary tree or...

**[34:40] SPEAKER_01:** Either! I mean, both are better than the Merkle Patricia Tree in some ways, but they don't solve this fundamental issue by themselves. Still, the thing is that the state is a permanent key-value store. And in order to avoid it growing forever, there's all these ideas about state expiry, but still it's going to be a huge data set. And the method of hashing or consensus protocol representation doesn't fundamentally change this.

So Verkle was supposed to provide more efficient Merkle proofs, but also I guess somewhat more expensive state processing because it's more expensive cryptography. Also, if I'm correct, it's not quantum secure. That was also a thing where I always felt like, yeah, I'm not sure if it's a good idea to start working from now. And I just saw it in front of my eyes how it's going to be cancelled.

**[36:04] SPEAKER_03:** Yeah, I mean I guess for running nodes in general, you know, there's not a lot of incentive for people to run any kind of node software themselves unless they are a validator or you're running an exchange or a business and you need your back-end to that. I guess the vision at the start was like, "Well yeah, everyone will be running their own node and you've got Mist on top of it, and it's local apps, and then that can have Swarm for the smart contracts." It's almost like you won't have server architecture because everyone's running a server stack. And then yeah, that did not happen.

**[36:47] SPEAKER_01:** Actually, that's why we are also stuck with the JSON-RPC API! Which doesn't provide proofs. Except for `eth_getProof`, but it doesn't provide proofs for a lot of things. Because it was never meant to be used remotely! It was always imagined that it's used locally in a trusted setup on your own machine. And I remember all those good old days when I just synced up a full node, it was a few gigabytes of disk space, and ran Mist on top of it. It's magic! But unfortunately, it didn't scale.

**[37:29] SPEAKER_03:** No, no, at the Museum of Ethereum here, I've got laptops running Geth 1.3.6, so Homestead Geth, and I mined Homestead back to life. So any hard fork that happens, the old one doesn't go away, right? It doesn't disappear, it's just people don't associate any economic value with it and it kind of gets abandoned.

But yeah, what I've done is first GPU and then down to CPU mine that Homestead difficulty down to the level that you can CPU mine it again. So I do have Mist running on those so we can go and transact, we can send a transaction between those. And it should be possible to run AlethZero and Mix on that as well. I haven't had time to do that. But ERC-20 tokens existed! You could have DAO tokens or Mist coin at that time. But yeah, the assumption that people would run their own node and it would all be self-sovereign local apps certainly did not come to fruition.

**[38:56] SPEAKER_01:** Well, yeah, that's when the light client came in. And then we assumed that okay, we do the light client, and it will be all solved.

**[39:00] SPEAKER_03:** That's it! Yeah, that's what I was thinking. It's like, right, I've got a full node running on my smartwatch that works, and I'll just wait for you and the other guys to sort out light client and just turn that on, and there we go.

**[39:11] SPEAKER_01:** Well, actually the light client protocol worked fine. It's just I spent like a really crazy amount of time figuring out how it could be incentivized in a truly decentralized way. Because I remember this idealism that, yeah, now we are almost done with everything, so we just have to find a real proper way for incentivizing things. But not in a way that there's a few companies where you can buy tokens, but truly in a decentralized way. Which is much harder, because then we have to somehow build decentralized trust and figure out market mechanisms that work without initial trust.

So yeah, this is something I spent years with. And honestly, I think I came up with some nice theoretical models and a lot of really complex code, but it's just again was like the wrong approach, maybe also at the wrong time. So we were just not there really.

**[40:29] SPEAKER_03:** Yeah, because BitTorrent has obviously worked for distributing content for many, many years, but then you do have this tragedy of the commons, right? The latest Hollywood movie, someone has ripped it off and people want that, so that's going to get shared around no problem. But things which are only of interest to a smaller number of people, without incentives, it's just a leeching problem. Good full node runners would contribute, they'll turn on the LES as well and they would help supply that. But the incentives and economics are not easy.

**[41:16] SPEAKER_01:** Yeah, actually with BitTorrent it also usually, if you really want to use it, requires trackers where you buy some priority access. Right, there are these private trackers and everything. And those are also not completely decentralized, but actually it does work. So it's definitely better than nothing.

But for LES it wasn't really this easy. Because this whole service, like downloading movies, was an application that everyone understood, that everybody used. And somehow with Ethereum, it was always this... yeah, everyone felt the importance, but we were nowhere near close to a really mature ecosystem. So it was just... I don't think there would have been a big enough market really for these services to really work out in a market-based way.

But as we scale and accessing the whole dataset becomes more and more difficult, at a certain point I think we are going to have something like I reimagined several years ago. So yeah, it's just both timing and specifics. I was right about everything except timing and specifics! Yeah.

**[42:51] SPEAKER_03:** Yes, yes. I mean, there's a number of things that seemed like they would be easy and quick and obvious and have taken so many years. I mean, like Proof of Stake. It was in the white paper, there was an assumption later in 2015, "That'll happen within six months, maybe three, six months," and then it's eight years before it actually went live.

And yeah, I mean on storage... so Filecoin, their first white paper was in 2014 as well. Filecoin was not a new thing, and IPFS was around before Ethereum as well. And then yeah, Whisper kind of went for a while, and then now there's... you've had Status driving a lot of those techs for a lot of those years as well. Jarrad Hope and team who were also doing an Android version of the Java client, the same kind of time as I was looking at smartwatches.

**[44:06] SPEAKER_01:** Yeah, Jarrad Hope was also very eagerly waiting for the fully functional light client.

**[44:12] SPEAKER_03:** Yeah! Because they were building kind of a decentralized WeChat, you know, super app. But I guess, you know, kind of a competitor to Mist really, similar kind of thing. Wanting to have a container for running dapps sitting on top of a local client again. You know, having this completely self-sovereign server app stack, but not easy.

And I can't remember who it was that was telling me that when they first saw MetaMask—which was at Devcon 1, that was one of the grantee winners was MetaMask—them thinking, "No, we... that's not what we want. We don't want like some browser extension thing talking to a trusted endpoint. Like that's absolutely the opposite. What are these guys doing?" And then that's become the standard flow, right?

**[45:18] SPEAKER_01:** Well, yeah. So this is still kind of an unsolved problem to access everything in a truly decentralized way. But I think we are getting there over time. It's just nothing is as simple as we initially imagined. And also, there's a time for everything. I think true decentralized infrastructure will be forced by scaling, and things sometimes just don't happen if they are not forced by some external factor. So yeah, as long as it works in a lazy way to just connect MetaMask to Infura, until then it's the standard way.

**[46:15] SPEAKER_03:** Yeah. So I think I found two different talks of yours at Devcons talking really about light client. Do you remember, did you talk in London or was Shanghai your first?

**[46:22] SPEAKER_01:** No, I talked at London, also Shanghai, and also in Cancún. Yeah, so those were the first three Devcons that were mostly about the light client. Actually, the first release of the light client protocol was in '16. So it was around that time. And later I already started to invent all the next chapters of decentralized technology.

And yeah, it was really naive of me, but I also had this project back then where I started to try to make logs provable efficiently. And that initial attempt for that was in 2017, and now I'm back at it. Now I also have this trustless log index project. And yeah, all the approaches in 2017, that was just a more efficient way to organize the Bloom filters. But it didn't really solve the problem of the Bloom filters not adapting to the number of events. And also, I never even proposed putting it into consensus, which would have allowed actual trustless proofs through the chain. So yeah, that also proved to be a hard problem.

But yeah, this is one of the things I presented in Cancún. And also some of my ideas of state channels. So back then we didn't have L2s in a way. Actually back then Layer 2 just meant something that happens off-chain, not necessarily another blockchain. So yeah, I had these ideas about individual nodes running all their own blockchains and somehow organizing some off-chain calculations through that. But yeah, it assumed a lot about how those would operate and probably would have never worked.

**[48:50] SPEAKER_03:** Yeah, I suspect right! Yeah, I mean, we had state channels and then we had Plasma, and then eventually coming into optimistic rollups, and then ZK later. Just many, many different attempts. Hello, see you sir, great to see you. Okay, so yeah, I mean I guess there's an awful lot of learning, right? 10 years worth of lots of people trying lots of different things. So I mean in terms of the Geth team, has that been similar over the years or have you had larger and smaller amounts of people? Has it been a similar kind of flow through that time?

**[49:36] SPEAKER_01:** I would say it was pretty consistently around 10 people throughout all these years. Sometimes eight, nine, sometimes 11, 12, but really in this range. We did improve our internal processes during the years! So yeah, now we do have all these issue and pull request triages and everything. But really it's been mostly that the team was always small enough so that we didn't need a lot of processes.

Honestly, the team culture did obviously change, especially with certain people coming and going. But I would say it was always a good team culture. I always liked the Geth team. That's also why I never really looked into moving to other teams or other projects. Because I felt that team is the best place to do meaningful things.

**[50:54] SPEAKER_03:** Yeah, I mean it's funny, because from the very start of Ethereum, the intention was to have multiple clients, right? That was a very basic decision of saying we want a separation between the specification and the implementation, because we don't want it to be like Bitcoin where you've got one code base and then there's no competition, there's no...

**[51:21] SPEAKER_01:** Well, yeah, for Bitcoin's complexity that approach worked. But for Ethereum's complexity, I would say this was one of the best decisions. Yeah, it also contributed to almost running out of money by the time we launched Mainnet, but I would say it was money well wasted! So yes.

**[51:43] SPEAKER_03:** No, I would agree, it was not efficient, but the outcome was very much worthwhile.

**[51:52] SPEAKER_01:** And when we switched to Proof of Stake, we again successfully applied this pattern by funding multiple CL implementations and then testing every EL against every CL.

**[52:08] SPEAKER_03:** Yes, with all the combinations. Five, is it five different primary consensus clients? There are, I think it's five. And notably none of those were within the Foundation either. They were all independent companies and teams. So I mean on the execution side, there have been a good number of different alternative execution clients over the years. So how have you tended to work and interact in that kind of environment where you've got all these different, I guess starting with Parity, and then Besu, and Nethermind, Erigon. So how do you work with other teams?

**[52:58] SPEAKER_01:** Well, now we have all the ACD calls and testing calls. So mostly, I mean, we all do have working clients all the time. So by default we don't need to interact a lot. We have to interact when we are testing out new features. There are the proper forums for that. And also some people keep more contacts outside of the Geth team, some people are more turning inwards and just focusing on Geth issues.

But actually, I think in the first years communication was really not organized as well. We really just tried to figure out things, and some people knew some people from the other teams. But actually these days we have much better processes for this. Also it's a much, much bigger challenge because there's so many more people.

Actually, this is also something I realized during the time we really started working on Proof of Stake. So in 2017 it was the first time ether price went to several thousand dollars. And the Foundation had money to hire new teams and fund external teams. And I remember that until 2017, I mostly met non-go-ethereum people mostly at Devcons. And maybe those people who lived in Berlin or one of those cities where there were multiple people, they met more people. But I was always in Hungary and worked remotely. And I mostly met most of the people at Devcons.

But around, I think it was 2018 when so many researchers and things had been hired, and there were also the CL teams. And I remember Devcon 4 at Prague. So until then, it was mostly... I don't know how many people exactly, but I do remember it's maybe 30, 40 people. After every Devcon we stood up at the main stage and had the group photo. "Oh yeah, we are the Ethereum Foundation! Yes!" Like it was that many people. And in '18 I was just shocked like, who the hell are all these people?! The whole Ethereum Foundation?!

So yeah, it became a much bigger challenge. But also now we do have all these official forums, and also I try to go to more events, not just Devcons, in order to keep all the contacts live.

**[56:00] SPEAKER_03:** Yeah. So looking back to when you first started working on Ethereum, did you have any kind of thought or vision of what things might have looked like 10 years later? Like, has it worked out as you expected or differently, or what's your looking back on these 10 years? What's your thought?

**[56:24] SPEAKER_01:** I always had a lot of visions. Maybe I was too focused on vision sometimes. The thing is that we all kind of have to imagine the future at every point, even though we know we can't imagine it as it will turn out. Yes, it never turns out exactly the way we want, but we always have to have some kind of direction and we have to just have ideas of how things can turn out.

So around 2017 I also realized that scaling will not happen just with L1. So yeah, I also had these ideas about how we could solve problems more efficiently with, not even rollups, just application-specific state channels and stuff like that. But there was also this really great project... Raiden. Yeah, thank you.

So yeah, they properly implemented the protocol and everything. I think it has always struggled with not many people using it. So it's a pain that the transactions are expensive, but still somehow maybe we just missed some organizing force to really move to some kind of Layer 2 solutions.

**[58:08] SPEAKER_03:** And it was just... well it was meant to be Lightning for Ethereum, right? That was the thought. Well yeah, it was pretty much that idea, but then Lightning's kind of failed. So maybe not surprising if an Ethereum version of that's not really caught on. Because you know, you have routing issues, right? It's really complicated. Yes, the channels seem to work great for consistent static topologies. You know, if you want to do merchant to merchant, that like channels work great.

**[58:44] SPEAKER_01:** Yeah, but opening those channels is still costly and non-trivial. And it's just... I also never really installed it... I tried it! I was like, okay this is interesting, but I never really made a payment through Raiden because there was just no occasion where the other party really wanted a Raiden transfer.

**[59:11] SPEAKER_03:** No, no. Well, thank you very much, I think we can wrap it up there. Okay. So thanks for your time and thanks for all of your work on Geth over these very many years. You know, Geth has always really been the backbone of Ethereum. New clients come and go, but Geth remains.

**[59:41] SPEAKER_01:** Yeah. Thank you. Thank you for having me here.