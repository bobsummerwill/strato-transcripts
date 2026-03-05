**[00:01] SPEAKER_03:** So hello, and welcome to ETHDenver 2026. So here recording for Early Days of Ethereum with Zsolt Felföldi. How do you pronounce your name? Zsolt? Zsolt. There you go. Anyway, so yeah, I was working out when we were recently reconnected at Devconnect, and I was working out that you're the third longest person at the Ethereum Foundation, right? That you've got Vitalik and then...

**[00:34] SPEAKER_01:** Felix. And then you. Yeah, I haven't really checked this fact yet, but honestly, yeah, it...

**[00:44] SPEAKER_03:** Sounds great, that's it. So I mean, you're a very long-time member of the Geth team, yes. But what were you doing before you started at the Foundation? What was your background? How did you find your way into the blockchain world?

**[00:58] SPEAKER_01:** Well, before Ethereum, I was working on really different types of projects. I first started at a Hungarian software company, like a really classic software company. We actually sold software in boxes, like put on a shelf, disks. Like yeah, like floppy disks put in a box on a shelf, and you can buy the software. So like this type of classic, classic software.

Five and a quarter inch floppies. Yeah, actually, three and a half. Oh, okay, three and a half, we're onto modern floppies! Yeah, but maybe also I said in '97, so maybe I was exaggerating a little. By that time it was mostly CDs. We still used a lot of floppies anyway.

So at that company, I did things related to computer graphics, like I wrote a ray tracing engine for some architectural software, and then I also did a lot of work on electronic circuit simulation and circuit design. Right. So yeah, really different things.

And it was around 2011 when I first heard about Bitcoin, and around 2012 when I started to realize that, as weird as it sounds, it really is probably a big thing. And yeah, actually I first heard about Ethereum early 2014, a few months after the initial paper had been published. And yeah, started contributing, I think, around November, and officially joined EF...

**[03:02] SPEAKER_03:** ...in 2015, March. So yeah. And did you hear about it, you think, through like, through Daniel Nagy and Viktor Trón, or some other way?

**[03:10] SPEAKER_01:** Well, I did hear about it from Daniel and Viktor's friend circle. So right. But then Viktor was already actually... I didn't know Viktor before. So I heard about this thing through one of his friends, and then Viktor was also in that wider circle. And he came to Hungary and said, "Oh, I'm already working on this." And then I started with my ideas and started to explain to him why this thing probably will never work. And he was like, "Okay, you seem to have a good understanding of this. Why don't you come to work?"

**[03:52] SPEAKER_03:** Right, right, right. So yeah, and was I right in thinking that you said it was Swarm that you started with?

**[03:59] SPEAKER_01:** Well, yeah. So Swarm was part of this initial trinity of base technologies of Ethereum. So it was supposed to be the storage layer for dapps. I mean, it was kind of a naive way of how people imagined decentralized applications back then, but honestly, it made sense at the time. I will say that nothing ever turned out exactly the way that people imagined it, but we are still making a lot of progress.

So yeah, Swarm was how we initially imagined the storage layer for Ethereum. And I mean, this project still has merits, but yeah, this whole problem space is just a bit more complex. Yeah. So I started contributing to Swarm first, and actually, I wrote the first like 500 lines...

**[05:02] SPEAKER_03:** ...of Swarm! There you go. Yeah, I mean, I think if I remember rightly, that Viktor mentioned around May 2014 was when he first heard that trinity. That this concept that you could have Ethereum as your compute and expensive database, Swarm as your decentralized storage, and then Whisper as your messaging.

There's that famous diagram, right? With the circle, and the things coming in, and Whisper going around the edge, and there's another one of those. But yeah, I guess it was Devcon 0 where Daniel really presented a sort of a fleshed-out vision of what that decentralized storage is.

**[05:51] SPEAKER_01:** Yes, that's correct. I wasn't there at Devcon 0 yet. So I've heard about this idea even before I heard about Ethereum. So Daniel already told me about this idea, that he wants to do this kind of hash-based chunk storage. And yeah, it made total sense that he just pitched that it can fit in. Yeah. At the time it was a perfect fit.

So he pitched this idea at Devcon 0, and when they accepted it and hired him, then he called me and said, because he already knew that I know of this project, "Let's do it together." So there you go.

**[06:40] SPEAKER_03:** And then so you were hired into ethdev? Yes, I did have a date for that, I've forgotten. I guess it was shortly after Devcon 0 right, that you started there? Did you go to Berlin or Amsterdam? Well, when did you first meet other people? How did it go?

**[07:07] SPEAKER_01:** It was Amsterdam in February '15. Right. That's where I met Jeffrey Wilcke, the creator of Go Ethereum, and the Go Ethereum team back then. I don't say Geth because that abbreviation was invented later. But so yeah, that's where I met the Go Ethereum people.

And I already had these contributions to Swarm, and it was kind of an implied thing that maybe I might be hired, but there was really no official hiring process back then. Right. So yeah, it was really just... Jeff was this really laid-back guy, and he just said, "Okay, man, I saw your contributions, and let's talk sometime this week."

And yeah, I waited the whole week and waited for some serious interview. Like, it was a dream job for me. Like, I was really enthusiastic about this whole thing, and I felt like, even though I felt that this whole initial design was... yeah, I couldn't really imagine how it would scale and everything, and yeah, it is a hard problem. So it was true, but it was still worth starting it. And I was really enthusiastic and I really wanted to get hired.

And yeah, the whole week I just waited, and at the end of the week, like the last half an hour before we all left home, Jeff just said, "Oh yeah, when I wanted to talk to you, you're hired." Okay, that's a good...

**[08:47] SPEAKER_03:** ...talk! So yeah, this is how the hiring process went back then. Excellent. Well, that's easy, we like that. And so, that was before you went to Amsterdam, I assume? I assume you went to Amsterdam after you had been hired?

**[09:07] SPEAKER_01:** No, no, no, it happened in Amsterdam. Oh, you see, so you were there unhired on site! Yeah. So Jeff agreed that if I bought my own plane ticket, I could stay at the Airbnb where the whole team stayed. And yeah, I just worked with them and showed my contributions, and yeah. So I went to Amsterdam unhired, but yeah, I mean... right.

**[09:29] SPEAKER_03:** Right, that plane ticket was a good investment. So yeah, did they not have office space at that point even?

**[09:35] SPEAKER_01:** Well, they did. They actually, back then, there was an Amsterdam office. Right. It was mostly for Jeff because Jeff lived in Amsterdam. But when Jeff left, or maybe before that, I'm not sure exactly, but this office was closed. And actually, it was a really small office. Right. Last time I checked now, I think it's a dentist works there. Yeah, it doesn't exist, but it was really just a small place.

But later I went to Berlin a lot after I was hired, and yeah, it was for the Geth team, it was really centered somehow in Berlin. So...

**[10:27] SPEAKER_03:** Right, right. Because yeah, I mean, I guess as well as Jeff, you've got Bas van Kesteren, right? He was another Amsterdam person, right? But then maybe most of the other team members weren't in Berlin... sorry, not in Amsterdam?

**[10:41] SPEAKER_01:** I mean, yeah, yeah. No one else was. Quite distributed. Bas was there for a short time, relatively short time. And Jeffrey also left after a while. Yeah. And started his own...

**[10:57] SPEAKER_03:** ...company, right? Grid Games or something? Yeah. Though he did have... EthLabs was another one. Do you know anything about EthLabs? Because when Jeff worked with JP Morgan to do Quorum, that was announced under the label EthLabs.

**[11:20] SPEAKER_01:** Never heard of that. Yeah, I think I heard the name, but I didn't really know what it does. But yeah, this is something I knew, that Jeff started working with JP Morgan back then. And then in that time, big banks really wanted to just talk to us at every Devcon, and we were always invited to fancy dinners by some main people. And yeah, so banks really wanted to learn about the technology. So Jeff went for a while to work on Quorum, yes. True. Yeah.

**[11:56] SPEAKER_03:** Yeah, I mean, I guess unless I can somehow get in contact with Jeff, I guess it's a little bit of a mystery what exactly EthLabs was. Though I suspect it might be a little bit like Ethcore, of just sort of being a name, a banner for activities rather than a legal entity.

And another thing I don't know there but I suspect is, I don't think Jeff told Ming Chan that he was doing that stuff with JP Morgan. I suspect that he completely just did that on his own without any communication with Ming or with the EF. It's just...

**[12:34] SPEAKER_01:** Well, actually, he never really told a lot to us about that. So we knew that, yeah, he's working with JP Morgan, but probably like, it's a big bank, probably he had to sign a non-disclosure agreement. So he probably couldn't share all the details.

**[12:54] SPEAKER_03:** No, no. I mean, I remember at some point, and I can't remember the context, him saying he found it interesting because the consensus for that was on-chain. Like the consensus for that was happening as smart contracts, so it was kind of almost like this pluggable consensus, but consensus pulled up into the app layer. So he found that quite interesting that the initial Quorum consensus—it didn't last long—but I think Gavin Wood also was doing that sort of stuff on the C++ side.

That he did some proof of authority stuff before that happened on the Geth side, you know, before Clique. That this was perfectly... well, you can, he actually made a different C++ client. So you've got eth, but he made another one that was called like Fluidity or something which was like pulling all the libraries in the same, but it was with a proof of authority consensus.

But he did that, that was one of the last things he did before he went out to Parity. So I think both him and Jeff were interested in that thought of, "Well, how can you formulate these pieces in different ways for those kind of use cases?" Interesting. But yeah, he left... I think it was probably very early in 2017. I did find a period, but it was certainly ahead of Devcon 3. Let me see if I can find the date. Yeah.

**[14:44] SPEAKER_01:** I don't remember the exact date, and actually there was maybe there wasn't even a really exact date when Jeff left. Because, basically a month after I joined, Péter Szilágyi joined, and he was the team lead for a very long time. So Jeff basically kind of handed it on to Péter. And for a while, he was officially still team lead, but not really. We haven't seen him on the calls for...

**[15:13] SPEAKER_03:** No, so the date I found there was February 2017, but I think I got that from GitHub. I think that was like his final commit. But he probably tailed off...

**[15:29] SPEAKER_01:** Yeah, he's a long time... yeah, he already started focusing on other stuff, like this Quorum stuff and then his own things, sometime in '16. So yeah.

**[15:37] SPEAKER_03:** Started a company called Grid Games with his brother just building a particular game, but that also seems to have ceased. So yeah, he's unknown off in the world somewhere.

**[15:52] SPEAKER_01:** Yeah, that's pretty much all I know about him. We tried to invite him a few times to just come to some event and meet up, and yeah, I think for some reasons he really had enough of, maybe not us, but things going on in the EF.

**[16:09] SPEAKER_03:** Yeah, I mean, yeah, I think that would be the case that, you know, when Ming came in, she both did legal tidy up but also cut the spending a lot. You had the crowd sale in July, August, September 2014, but coming up to the mainnet release a year later, like practically all the money was gone.

**[16:36] SPEAKER_01:** Yes, they spent it very fast. Yeah. So that Devcon 1 was a postponed one because of that. Yeah. And we didn't really feel a lot of this, actually. Jeff just said that now that Ether price is so low—actually, I think the lower point was 42 cents—and for a whole year it didn't really move. And Jeff just said that, "Okay, we all have to take a payment cut."

But the payment cut was really just 10 percent, and I think maybe he took a bigger one. So yeah, for us it was really not that bad. And the idea was that when Ether price reaches two dollars, then yeah, we do have some money to go forward. So yeah, then our salaries went back. And that wasn't a lot of time.

So yeah, actually for this, I don't really remember the price history, and maybe it's not the most important thing, but I think Ether price reached something like 10 dollars pretty soon, like in 2016. The start of 2016. Yeah, and we went even a little bit higher, but then we had the DAO fork and the Shanghai attacks, and well, given how turbulent those times were, the markets held pretty well. So yeah. And with a 10 dollar Ether price, we could survive further, and yeah.

**[18:18] SPEAKER_03:** Yeah, I mean that was quite a jump up. I mean, I heard that at the worst point, there was only four months of runway left. You know, that was how close it was to running out of money. But yeah, there were those big cuts which really resulted in, like, Gavin and the C++ team were the main kind of victims of those cuts.

But then, yeah, just into 2016... pardon me, so I was hired in February 2016, same time as Greg Colvin came in. And also Paweł Bylica was rehired, you know, he was working through IMAPP working on that JIT, but that contract stopped, but then he came back at that time as well. So it was this period through late 2015 to early 2016 was like, you know, the absolute bottom of, "Are we even going to ship this thing? Are we going to run out of money before we get to mainnet?"

But then yeah, some of us were really coming in as backfill for that C++ team. Yeah. So I mean, Devcon 1 was sort of, you were mentioning in that series that had got cancelled, but then ConsenSys came in and actually paid for that and said, "Hey, we'll mainly organize it and kind of so that the thing can happen." So that was the big, you know, the first public event. So what are your memories of Devcon 1?

**[19:55] SPEAKER_01:** Well, my subjective impression was that it's really amazing. Yeah. Compared to today's Devcons, it was small. I think three hundred something people. Maybe, I'm not sure, about less than a thousand. Yeah. And it was in a really prestigious venue, some old bank building or Threadneedle Street, yeah, it's like City of London.

And yeah, I really felt like, "Okay, so now this is really a serious thing," and probably that was the reason why ConsenSys stepped in and funded the event. So we really could step up in terms of public appearance and appear something really serious. And yeah, I remember all the big banks having the presence, like the booth at Devcon 1. Right. So yeah. And then Microsoft...

**[20:59] SPEAKER_03:** ...as headline sponsor. It's like, wow, right! Like recognition, right? That you're like, "Wow, Microsoft are interested and supportive." And yeah, I mean, I think for a lot of people it was a real kind of wow, like, "This is for real." You know. Sadly, I could not afford to go. I watched the live stream. I was not quite in and working yet. I was an enthusiastic contributor, but yeah.

**[21:34] SPEAKER_01:** Actually, it was also like the first time for me when I met a larger number of Ethereum people. Right. I first met the Go Ethereum team in early '15, and yeah, I went to Amsterdam one more time, I think in May. But Devcon 1 was the place where I really realized how big this thing is.

And it's really not just about client developers, but also, even back then, people presented about formal verification and all this stuff. So yeah, I realized that this is really big and probably everyone wants to be a part of it, at least a little bit.

**[22:20] SPEAKER_03:** Yeah, yeah, yeah. I mean, looking back at Devcon 1 videos, it's like everything. Like any kind of use case you could think of, you know, there was somebody presenting about it. You know, this so, so early, more than 10 years ago. But you know, many, many concepts which were probably massively too early to do, but maybe you can do them all now, seem to be presented. You had Nick Szabo as well. Nick Szabo doing a keynote. Yeah, yeah, yeah, Nick Szabo was also there. So was that maybe the first time that you'd met a number of the people in Berlin like Christoph Jentzsch and Lefteris Karapetsas and maybe even Gavin?

**[23:00] SPEAKER_01:** I think I met some of these people already in London, and I think first time I went to Berlin office back then... it was like, they need the other... like it was like the old office. Yeah. Right. But um, so yeah, some people I met at Devcon 1, some people I met in Berlin, but yeah.

**[23:24] SPEAKER_03:** So was Devcon 1 the first time that you'd been to do Ethereum things in London, or did you go to any sort of London meetups or meet any of those comms people earlier?

**[23:39] SPEAKER_01:** I didn't go to any meetups in London before, but actually, I did... so Viktor was in London at the time, and I went to London around the time, actually if you're doing some event with my old software company. The Hungarian software company! Oh right! Yeah, so we went to London to basically sell our software and everything, so I was still working there. Right. And after that, yeah, I met up with Viktor and talked about things.

**[24:23] SPEAKER_03:** Because yeah, he... from what he was describing, and then I was looking at videos and things later, he had seen Gavin talk in London in very very early February. I think it was February the 6th. So almost immediately after they'd had the Miami — like, you know, B2C Miami launch, Vitalik's first public talk, and Anthony Di Iorio's mansion where they, you know, a lot of them met for the first time — Gavin had been back in London, I think it was like a week after, and did a talk there that Viktor had gone to. That was Viktor's first, you know, in-person meeting with any of these. And then Gavin had pulled him on board. Yeah.

**[25:22] SPEAKER_01:** So those are like the very, very early days. I wasn't there. So when I first heard about Ethereum, that was I think March or April '14. So I first heard about the pre-sale, and yeah, like that's where I first heard about this thing. But yeah, I know that Gavin was like one of the very early founders of this, and he wrote the yellow paper. Yeah. Full of Greek letters, yes.

**[25:51] SPEAKER_03:** Very confusing. Yeah, and the C++ client, of course. So the first time I think I saw your name or was in contact with you was about light client, because you know, I'd been trying to get Ethereum ARM Linux cross builds running on my smartwatch.

And my thought there was, get the thing running, and then this light client stuff is just kind of starting, and you know, like, scaling will be solved, right? We're going to be able to like run these nodes on anything, you know? You'll have them on your phone, smartwatch, router, they'll be in every operating system, you know? It's just, we'll solve that scaling and that lightness. So you were plunged right into that problem, right?

**[26:38] SPEAKER_01:** Yeah. So when Jeff hired me, actually, he put me on this project. So he just said that, "Okay, it's great that I contributed to Swarm, but if I joined the Geth team, I will have to start working on the light client because it's a very important thing and it hasn't been started yet." Yeah. So yeah, I felt really good about it. Like, yeah, I also felt like this is a big thing.

And yeah, back then it really felt like we do these few things: we have a working light client protocol and the whole trinity of a base layer, and then we're all good. Yeah. But it wasn't that easy. But still, those were the first steps. And so I designed the LES protocol. Yeah. In retrospect, it didn't make a lot of sense to build it over the devp2p layer, right? Because, yeah, like, it wasn't easy to access from web browsers and stuff, but also it was a proof of work based light client.

So yeah, that project ended after a while. But I'm still very much into trustless chain access. So that has usually been one of my focuses all the time. Right now I'm also working on something called the Trustless Execution Resources... Execution Layer API. Right. Which is similar to the Beacon Chain REST API, but works on the execution layer and provides everything with proofs. So yeah, I'm still very much into this because I think this is where it really makes sense if even normal users access chain data with proofs.

**[28:36] SPEAKER_03:** Right, right. And there was a project called Portal as well. Were you involved with Portal? That was a later kind of light client.

**[28:42] SPEAKER_01:** No, I wasn't. So Portal was Piper Merriam's brainchild. So by the time we kind of realized that LES was a nice first experiment but maybe not the best approach, he started something different that was UDP based, and also used different topologies. So it was kind of a DHT approach to storing the chain and the state, and yeah.

Actually, I'm kind of... like, I think it's a bad thing that it's been completely canceled. Because well, actually, to be honest, I never really believed that it will be an easily solvable problem to store the Merkle Patricia Trie of the state right on the DHT. But for the chain data, yeah, it made perfect sense. So yeah, maybe the state would have been possible with a lot of work. But yeah, I mean, Piper told me a few times about how he imagines the order to solve all the unsolvable problems. And I felt like, yeah, it sounds good, but he just made a lot of really hard assumptions about DHTs.

By the time, I already worked on Discovery v5. So there was also this discovery protocol that basically we designed in 2016 in Berlin with Felix, and I released the original version. And yeah, so I already knew that yeah, it's never so easy to imagine a DHT that's efficiently formed, that all the nodes are working, and yeah, like this.

But for the chain data, right, especially with EIP-4444. So like, that lets the nodes processing main protocol forget the old chain history. Right. So it made perfect sense to at least put the chain history on a DHT. Yeah. But yeah, so it was an EF decision that it was discontinued at point. Well, I mean, I guess the thing is...

**[31:06] SPEAKER_03:** ...you know, Patricia Merkle trees are not great for, you know, the number of accesses and things anyway. Let alone if you're making each of those steps over a networked, you know, DHT kind of setup. That's, yeah, there's a lot of, it's so much transactional change, yeah, complexity.

**[31:32] SPEAKER_01:** State tree suffers from a lot of issues, especially a Merkle Patricia state tree. And yeah, it's a huge data set that keeps changing all the time and keeps changing at completely random places. Yeah. And it's not an easy task to distribute it. Right. So actually, it's getting harder to even synchronize it between the full nodes storing the entire state. Yeah. Yeah.

**[31:59] SPEAKER_03:** So um, do you, do you think that proofs are going to be a magic, you know, magic silver bullet here? Where by having, you know, local proofs versus, you know, massive really redundant state machines... Do you think there's a path here where...

**[32:24] SPEAKER_01:** Oh, no, it's not a silver bullet. So I assume you mean what people call statelessness. So it's a good thing. It definitely allows a higher degree of scaling, but the state tree still has to be processed and maintained by someone. And especially if most of the nodes have no incentive to process it... yeah. And if we scale a thousand x, then it will be a huge infrastructural centralization issue. Right.

And yeah, by the way, this thing is not an unsolvable problem. I mean, the state as it works today, yeah, unfortunately somehow makes it really hard to do any fundamental improvements over these properties. But people are considering different storage architectures. Yeah, of course, we have to keep the existing contracts workable, because that was our main promise from the beginning. Right. That we will not just shut down anything; yeah, everything has 100 percent uptime.

But it is a viable way to come up with more efficient storage methods and use it as an opt-in alternative that will over time be available for much less, and new contracts can be designed using those more efficient storage architectures.

**[34:26] SPEAKER_03:** Yeah, because Verkle trees seem to be the first sort of thought on that, but then those, yeah, that's kind of come and gone, and maybe it's a binary tree or, actually, it does either.

**[34:40] SPEAKER_01:** So, importantly either. I mean, both are better than the Merkle Patricia Trie. Yeah. But in some ways, they don't solve this fundamental issue by themselves. So still the thing is that the state is a permanent key-value store, and in order to avoid it growing forever, yeah, there's all these ideas about state expiry. But still, it's going to be a huge data set, and the method of hashing or consensus protocol representation doesn't fundamentally change this.

So Verkle was supposed to provide more efficient Merkle proofs, but also I guess somewhat more expensive state processing because it's like more expensive cryptography. Right. Also, if I'm correct, it's not quantum secure. So, right. And that was also a thing that where I always felt like, yeah, I'm not sure if it's a good idea to start working from now, and I just saw it in front of my eyes how it's going to be cancelled. And yeah, so...

**[36:04] SPEAKER_03:** Yeah, I mean, I guess for running nodes in general, you know, there's not a lot of incentive for people to run any kind of node software themselves unless they are, you know, a validator or, you know, you're running an exchange or a business and you need your backend to that.

You know, I guess the vision that there was at the start of, like, "Well yeah, everyone will be running their own node and so you've got Mist on top of it, and you know, it's local apps, you know, and then that can have Swarm for the smart contracts," and you know, it's almost like you won't have server architecture because everyone's running a server stack. And then, yeah, that did not happen.

**[36:47] SPEAKER_01:** Actually, that's why we are also stuck with the JSON RPC API, which doesn't provide proofs except for eth_getProof, but doesn't provide proofs for a lot of things. Because it was never meant to be used remotely. It was always imagined that yeah, it's used locally in a trusted setup on your own machine.

And yeah, I remember all those good old days when I just synced up a full node, it was a few gigabytes of disk space, and ran Mist on top of it. And yeah, it's magic. But yeah, unfortunately it didn't scale. So...

**[37:29] SPEAKER_03:** No, at the Museum of Ethereum here, I've got laptops running Geth 1.3.6, so Homestead Geth. And I mined Homestead back to life! So um, you know, any hard fork that happens, the old one doesn't go away, right? It doesn't disappear. It's just people don't associate any economic value with it and it kind of gets abandoned.

But yeah, what I've done is—first GPU and then down to CPU—mined that Homestead difficulty down to the level that you can CPU mine it again. So I do have Mist running on those, so we can go and transact. We can send a transaction between those and it should be possible to run AlethZero and AlethOne and Mix on that as well. I haven't had time to do that, but... and you know, ERC-20 tokens existed, you know, you could have DAO tokens or Mist coin at that time.

But yeah, the assumption that people would run their own node and it would all be self-sovereign local apps certainly did not come to fruition.

**[38:56] SPEAKER_01:** Well yeah, that's when the light client came in and then we assumed that okay, then we do the light client and yeah, it will be all solved.

**[39:00] SPEAKER_03:** That's it! Yeah, that's what I was thinking, is like, "Right, I've got a full node running on my smartwatch that works, and I'll just wait for you and the other guys to, you know, sort out light client and just turn that on and there we go."

**[39:11] SPEAKER_01:** Well actually, the light client protocol worked fine. It's just, yeah, I spent like a really crazy amount of time figuring out how it could be incentivized in a truly decentralized way. Because yeah, I remember this idealism that, yeah, now we are almost done with everything, so we just have to find a real proper way for incentivizing things. But not in a way that there's a few companies where you can buy like tokens, but truly in a decentralized way, which is much harder.

Because yeah, then we have to somehow build decentralized trust and figure out market mechanisms that work without initial trust. So yeah, this is something I spent years with. And honestly, I think I came up with some nice theoretical models and a lot of really complex code, but yeah, it's just again was like the wrong approach, maybe also at the wrong time. So we were just not there really. Yeah.

**[40:29] SPEAKER_03:** Because I mean, BitTorrent has obviously worked for distributing content for many, many years. But then you do have this tragedy of the commons, right? Is, yes, the latest Hollywood movie, someone has ripped it off and people want that, so that's going to get shared around no problem. But things which are only of interest to a smaller number of people, without incentives, it's just a leeching problem, right? You kind of... good full node runners would contribute, you know, they'll turn on the LES as well, right? They would help supply that. But the incentives and economics are that... not easy.

**[41:16] SPEAKER_01:** Yeah, actually with BitTorrent, it also usually, if you really want to use it, it requires trackers where you buy some priority access. So right, there are these private trackers and everything. Yeah. So yeah, and those are also like not completely decentralized. But actually it does work, so it's definitely better than nothing.

But for LES, it wasn't really this easy, because this whole service was, like... downloading movies was an application that everyone understood, that everybody used. And somehow with Ethereum, it was always this, yeah, everyone felt the importance, but it figured nowhere near close to a really mature ecosystem. And so it was just, I don't think there would have been a big enough market really for these services to really work out in a market-based way. Yeah.

But as we scale, and accessing the whole dataset becomes more and more difficult, at a certain point I think we are going to have something like I reimagined several years ago. So yeah, it's just both like timing and specifics. Yeah. I was right about everything except timing and specifics. Yeah, yes, yes.

**[42:51] SPEAKER_03:** Yeah, I mean there's a number of things that seemed like they would be easy and quick and obvious and have taken so many years. I mean, like proof of stake, you know. It was in the white paper, there was an assumption, you know, later in 2015, "That'll happen, you know, within six months, maybe three, six months." And then it's eight years before, you know, it actually went live.

And yeah, I mean on storage... so Filecoin, their first white paper was in 2014 as well. You know, Filecoin was not a new thing, and IPFS was around before Ethereum as well. But... and then yeah, Whisper kind of went for a while, and then now there's... and you'd have, you've had Status driving a lot of those texts for a lot of those years as well. You know, Jarrad Hope and team, who were also doing Android versions of the Java client, you know, the same kind of time as I was looking at smartwatches.

**[44:06] SPEAKER_01:** Yeah. Jarrad Hope was also very eagerly waiting for the fully functional light client. Yeah! Yeah, well...

**[44:12] SPEAKER_03:** Yeah, because you know, they were building kind of decentralized WeChat, you know, super app. But I guess, you know, kind of a competitor to Mist, really. Similar kind of thing, you know, wanting to have a container for running dapps in, sitting on top of a local client. Again, you know, having this completely self-sovereign kind of server app stack. But not easy.

And I can't remember who it was that was telling me that, so when they first saw MetaMask, which was at Devcon 1 — that was one of the grantee winners was MetaMask — them thinking, "No, we, that's not what we want. We don't want like, you know, some browser extension thing talking to a trusted endpoint. Like, that's absolutely the opposite. Like, what are these guys doing?" And then that's, you know, that's become the standard flow, right?

**[45:18] SPEAKER_01:** Well yeah. So this is still kind of an unsolved problem to access everything in a truly decentralized way. But I think we are getting there over time. It's just... yeah, nothing is as simple as we initially imagined. And also, there's a time for everything.

And I think true decentralized infrastructure will be forced by scaling. And things sometimes just don't happen if they are not forced by some circumstance, some fact, some external factor. So yeah, as long as it works in a lazy way to just connect MetaMask to Infura, yeah, until then, it's the standard way. Yeah, yeah. So I think...

**[46:15] SPEAKER_03:** I found two different talks of yours at Devcons talking really about light client. Do you remember, did you talk in London or was Shanghai your first?

**[46:22] SPEAKER_01:** No, I talked at London. Also Shanghai. And also, also in Cancún. Yeah. So those were the first two Devcons that were mostly about the light client. So actually, the first release of the light client protocol was in '16. So it was around that time.

And later, I already started to invent all like the next chapters of decentralized technology. And yeah, it was really naive of me, but I also had this project back then where I started to try to make logs provable efficiently. And yeah, that was, so the initial attempt for that was in 2017. And now I'm back at it. Now I also have this trustless log index project. Yeah. And yeah.

So all the approaches in 2017, that was just a more efficient way to organize the Bloom filters, but it didn't really solve the problem of the Bloom filters not adapting to the number of events. And also, I never even proposed putting it into consensus, which would have allowed the actual trustless proofs through the chain. Right. So yeah, that also proved to be a hard problem. But yeah, this is one of the things what I presented in Cancún. Right, right.

Oh yeah, and also some kind of... my ideas of state channels. So back then, we didn't have like L2s in a way. So actually back then, Layer 2 just meant something that happens off-chain, not necessarily another blockchain. Yeah. And yeah. So I had these ideas about individual nodes running, all running their own blockchains and somehow organizing some off-chain calculations through that. But yeah, it's also like assumed a lot about how those would operate and probably would...

**[48:50] SPEAKER_03:** ...have never worked! Yeah, suspect, right? Yeah. So yeah, I mean we had state channels and then we had Plasma, and then eventually coming into optimistic rollups and then ZK later. Just many, many different attempts. Hello, see you sir. Great to see you. Okay.

So um, so yeah, I mean I guess there's an awful lot of learning, right? Ten years worth of lots of people trying lots of different things. So I mean in terms of the Geth team, has that been similar over the years, or have you had, you know, larger and smaller amounts of people? Has it been a similar kind of flow through that time?

**[49:36] SPEAKER_01:** I would say it was pretty consistently around 10 people throughout all these years. Sometimes eight, nine, sometimes 11, 12, but really like in this range. We did improve our internal processes during the years. So yeah, now we do have all this issue and pull request triages and yeah, but really it's been mostly… mostly the team was also always small enough so that we didn't need a lot of processes. Right, right.

Honestly, the team culture, yeah, it did obviously change especially with certain people coming and going. But it also, I would say it was always a good team culture. I always liked the Geth team, that's also why I never really looked into moving to other teams or other projects. Because I felt that that team is the best place to, right, do meaningful...

**[50:54] SPEAKER_03:** ...things. Um, yeah, I mean, it's funny because from the very start of Ethereum, the intention was to have multiple clients, right? That was a very basic decision of saying, "We want a separation between the specification and the implementation." Right, because we don't want it to be like Bitcoin where you've got one codebase and then like, there's no like competition, there's no, you know...

**[51:21] SPEAKER_01:** Well yeah, for Bitcoin's complexity that approach worked. But for Ethereum's complexity, I would say this was one of the best decisions. Yeah. It also contributed to almost running out of money by the time we launched mainnet, but I would say it was money well wasted. So...

**[51:43] SPEAKER_03:** Yes, no, I would agree, it was not efficient but the outcome was very much worthwhile. Yeah. And, when we switched to proof of stake...

**[51:52] SPEAKER_01:** We again successfully applied this pattern by funding multiple CL implementations and then testing every EL against every CL. Yeah. And then... Yes, that's with all the combinations.

**[52:08] SPEAKER_03:** Five, is it five different primary consensus clients? There are, I think it's five. Yeah. And yeah, notably none of those were within the Foundation either. They were all independent companies and teams. So I mean on the execution side, there have been, you know, a good number of different alternative execution clients over the years. So I mean, how have you tended to work and interact in that kind of environment where you've got all these different, you know, I guess starting with Parity, and then Besu, and Nethermind, Erigon. So how do you work with other teams?

**[52:58] SPEAKER_01:** Well, we have now... we have all the ACD calls and testing calls. So mostly, I mean, we all do have working clients all the time, so by default we don't need to interact a lot. We have to interact when we are testing out new features. Yeah, there are the prepared forums for that. So yeah. And, oh, it's also, some people keep more contacts outside of the Geth team, some people are more turning inwards and then just focusing on Geth issues. Yeah.

But actually, I think in the first years, communication was really not organized as well. So we really just tried to figure out things, and some people knew some people from the other teams, and yeah. But actually these days, we have much better processes for this. Also, it's a much, much bigger challenge because there's so many more people.

Actually, this is also something I realized during the time we really started working on proof of stake. So, in 2017... it was the first time Ether price went to several thousand dollars, and yeah, the Foundation had money to hire right, new teams and fund external teams. And I remember that, until 2017, I mostly met non-Go Ethereum people mostly at Devcons. Right, yeah, yeah.

And maybe those people who lived in Berlin or one of those cities where there were multiple people, they met more people. But I was always in Hungary and worked remotely, and yeah, I mostly met most of the people at Devcons. Yeah.

But around, I think it was 2018 when so many researchers and CL teams have been hired. And I remember Devcon 4 at Prague. Yeah. It was... so until then it was mostly, I don't know how many people exactly, but I do remember it's maybe 30, 40 people. I don't know. After every Devcon, yeah, we stood up at the main stage and the group photo, "Oh yeah, we are the Ethereum Foundation." Yes, like it was that many people. Yeah. And in '18, I just, I was just shocked like, "Who the hell are all these people? The whole Ethereum Foundation?" Yeah.

So yeah, it became a much bigger challenge, but also now we do have all these official forums, and also I try to go to more events, not just Devcons. So yeah, in order to keep all the contacts live. Yeah.

**[56:00] SPEAKER_03:** Yeah. So I mean, looking back to when you first started working on Ethereum, did you have any kind of thought or vision of what things might have looked like 10 years later? Has it worked out as you expected, or differently, or what's your looking back on these 10 years, what's your thought?

**[56:24] SPEAKER_01:** I always had a lot of visions. Yeah. I, maybe I was too focused on vision sometimes. So the thing is that we all kind of have to imagine the future at every point, even though we know we can't imagine it as it will turn out. Yes, it never turns out exactly the way we want, but we always have to have some kind of direction, and we have to just have ideas of how things can turn out.

So yeah, around 2017, I also realized that scaling will not happen just with L1. So yeah, I also had these ideas about how we could solve problems more efficiently with, not even rollups, just application-specific state channels and stuff like that. Yeah.

But it also, there was this really great project... right, Raiden! Yeah. Thank you, thank you. So yeah, they properly implemented the protocol and everything. Yeah. I think it has always struggled with not many people using it. So it's like a problem, it's a pain that the transactions are expensive. But still, somehow, maybe we just missed some organizing force to really move to some kind of Layer 2 solutions. Yeah. And...

**[58:08] SPEAKER_03:** ...and it was just, yeah. Well, it was meant to be Lightning for Ethereum, right? That was the thought. Well yeah, it was pretty much that idea, but then Lightning's kind of failed. So maybe not surprising if an Ethereum version of that's not really got... because you know, you have routing issues, right? It's really complicated. Yes. The channels seem to work great for consistent static topologies. You know, if you want to do merchant to merchant, like, channels work great. Yeah.

**[58:44] SPEAKER_01:** But opening those channels is still costly and non-trivial, and yeah, it's just, I also never really... I installed it, I tried it, I said "Okay, this is interesting," but yeah, I never really made a payment through Raiden because there was just no occasion where the other party...

**[59:11] SPEAKER_03:** ...really wanted a Raiden transfer. No, no. Well, thank you very much, I think we can wrap it up there. Okay, so thanks for your time, and thanks for all of your work on Geth over these very many years. You know, Geth has always really been the backbone of Ethereum. You know, new clients come and go, but Geth remains. Yeah, so thank you.

**[59:41] SPEAKER_00:** Thank you for having me here. Okay, thank you.