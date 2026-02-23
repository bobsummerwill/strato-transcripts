**[00:02] SPEAKER_00:** So, hello and welcome to DevCon 2026. So here recording for Early Days of Ethereum with Zolt Felfeldy. How do you pronounce your name?

**[00:14] SPEAKER_01:** Zolt Szelfeldi.

**[00:16] SPEAKER_00:** There you go. Anyway, so yeah, I was working out when we recently reconnected at DevConnect and I was working out that you're the third longest person at the Ethereum Foundation. Right. You've got Vitalik and then Felix and then you.

**[00:38] SPEAKER_01:** Yeah, I haven't really checked this fact yet, but honestly, yeah, it sounds great.

**[00:46] SPEAKER_00:** That's it. So, I mean, you're a very long time member of the Geth team.

**[00:52] SPEAKER_01:** Yes.

**[00:52] SPEAKER_00:** But what were you doing before you started at the foundation? What was your, your background? How did you find your way into the blockchain world?

**[01:02] SPEAKER_01:** Well, before Ethereum, I was working on really different types of projects. So I first started at a Hungarian software company, like really classic software company. We actually sold software in boxes like put on a shelf, like floppy disks. Put in a box on a shelf and you can buy the software. So like, like this type of like classic, classic software.

**[01:35] SPEAKER_00:** Five and a quarter. Five and a quarter inch floppies.

**[01:38] SPEAKER_01:** Yeah, yeah, actually three and a half.

**[01:42] SPEAKER_00:** Oh, okay. Three and a half. We're on to modern floppies.

**[01:46] SPEAKER_01:** Yeah, but maybe also like, like in. I started in 97, so maybe I was exaggerating a little. So by that time it was mostly, mostly CDs. We still used a lot of floppies anyway, so those. So at that company I did things related to. First things related to computer graphics. Like I wrote a ray tracing engine for some architectural software. And then I also did a lot of work on electronic circuit simulation and circuit design.

**[02:20] SPEAKER_00:** Right.

**[02:21] SPEAKER_01:** So yeah, really different things. And it was around 2011 when I first heard about Bitcoin and around 2012 when I started to realize that as weird as it sounds, it really is probably a big thing. Actually I first heard About Ethereum early 2014, a few months after the initial paper has been published.

**[02:53] SPEAKER_00:** Yeah.

**[02:54] SPEAKER_01:** And yeah, started contributing I think around November and officially joined EF at in 2015, March. So. Yeah.

**[03:05] SPEAKER_00:** And did you hear about it, you think, through, like through Danny and Victor or some other way?

**[03:14] SPEAKER_01:** Well, I, I did hear about it from like Danny and Victor's friend circle. So.

**[03:22] SPEAKER_00:** Right.

**[03:22] SPEAKER_01:** Yeah, but then Victor was already. Actually, actually I never didn't know Victor before. So I, I met. Heard about this thing through one of Denny's friends and then, then Victor was also in that wider circle and he came to Hungary and said, oh, I'm Already working on this. And then I, I started with my ideas and started to explain to him why this thing was probably will never work. And he was like, okay, you seem to have a good understanding of this. Why don't you come to work?

**[03:52] SPEAKER_00:** Right, right. And was I right in thinking that you said it was Swarm that you started with?

**[04:00] SPEAKER_01:** Well, yeah. So Swarm was part of this initial trinity of base technologies of Ethereum. So was supposed to be the storage layer for dapps. Yeah, I mean it was kind of a naive way of like how people imagine the decentralized applications back there. But honestly it made sense at the time. So I will say that, yeah, never, nothing ever turned out exactly the way that people imagined it. But we are still making a lot of progress. Progress. So yeah, Swarm was how we initially imagined this storage layer for Ethereum. And I mean this project still has merits, but yeah, this whole problem space is just a bit more complex. But yeah, so I started contributing to Swarm first and actually I brought the first 500 lines of Swarm.

**[05:02] SPEAKER_00:** There you go. Yeah, I mean I, I think if I remember rightly that Victor mentioned around May 2014 was when he first heard, you know, the trinity, this, this concept that you could have, you know, Ethereum as your sort of your compute an expensive database, Swarm as your decentralized storage and then Whisper as your messaging was that famous diagram, right, with the. There's like a circle and the things coming in and Whisper going around the edge and there's another one of those. But yeah, I mean, I guess it was devcon0 where Danny really presented a sort of a fleshed out vision of what that decentralized storage.

**[05:54] SPEAKER_01:** Yes, that's correct. I wasn't there at DEVCON 0 yet. So I've heard about this idea even before I heard about Ethereum. So Danny Oradeesh told me about this idea that he wants to do these kinds of hash based chunks storage and. Yeah, so it made total sense that he just pitched that.

**[06:14] SPEAKER_00:** That can fit in.

**[06:16] SPEAKER_01:** Yeah, at the time it was a perfect fit. Yeah. So he pitched this idea @Defcon0 and, and when they accepted it and hired Denny, then he called me and said because he already knew that I know of this project and. Yeah, then let's do it together.

**[06:38] SPEAKER_00:** There you go. And then. So you were hired into fdev? I did have a date for that. I've forgotten. I guess it was shortly after DEVCON 0, right. That you started there?

**[06:51] SPEAKER_01:** Yes, correct.

**[06:53] SPEAKER_00:** Did you go to Berlin or Amsterdam? When did you first meet other people? How did.

**[07:01] SPEAKER_01:** It was Amsterdam in February 15, right. That's where I met Jeffrey Wilke, the creator of Goethereum and the Go Ethereum team. Back then, I don't say get because their GATT was, was like this abbreviation was invented later. So yeah, that's where I met the Go Ethereum people. And I already had these contributions to Swarm and it was kind of an implied thing that maybe I might be hired, but there was really no official hiring process back then. Yeah, it was really just Jeff was this really laid back guy and he just, he just said, okay, okay man, I saw your contributions and let's talk some sometime this week. And I waited the whole week and waited for some, some serious interview like it was a dream job for me. Yeah, like, but by that time I, sorry. I was really enthusiastic about this whole thing and, and I felt like. So even though I felt that this whole initial design was. Yeah, I really couldn't imagine how it would scale and everything. And it is a hard problem. So yeah, it was true, but it was still worth starting it and I was really enthusiastic and I really wanted to get hired. And yeah, the whole week I just waited. And at the end of the week, like last half an hour before we all left home, Jeff just said, oh yeah, man, I wanted to talk to you. You're hired. Okay, that's a good talk. So, yeah, this is how the hiring process went back then.

**[08:50] SPEAKER_00:** Excellent. Well, that's easy. We like that. And so you, that was before you went to Amsterdam, I assume, I assume you went to Amsterdam after you had been hired.

**[09:04] SPEAKER_01:** No, no, no, it happened in Amsterdam.

**[09:06] SPEAKER_00:** Oh, you, I see. So you were there unhired on site.

**[09:10] SPEAKER_01:** Yeah, so, so I like, like Jeff agreed that if, I mean, I bought my own plane ticket but I could stay at the Airbnb team stayed and yeah, I just worked with them and showed my contributions and yeah, so, so I, I, I, I went to Amsterdam unhired.

**[09:27] SPEAKER_00:** But yeah, I mean, Right, right.

**[09:29] SPEAKER_01:** That plane ticket was a good investment. So.

**[09:31] SPEAKER_00:** Yeah. So did they not have office space at that point even?

**[09:36] SPEAKER_01:** Well, they did actually back then there was an Amsterdam office.

**[09:40] SPEAKER_00:** Right.

**[09:41] SPEAKER_01:** It was mostly for Jeff because Jeff lived in Amsterdam. But when Jeff left ef or maybe before that, I'm not sure exactly, but so this office was closed and actually it was a really small office last time I checked. Now I think it's a dentist, like works there. So yeah, it doesn't exist, but it was really just a small, small place. But I later I went to Berlin a lot. So after I was hired and yeah, it Was. It was for the GET team. It was the really, really. It was centered in. In somehow in. In Berlin, so.

**[10:24] SPEAKER_00:** Right, right. Because, yeah, I mean, I guess as well as Jeff, you've got Baz. Right. He was another Amsterdam person. Right. Bas Van Kerwal. But then maybe most of the other team members weren't in Berlin. Sorry, not in Amsterdam. I mean.

**[10:43] SPEAKER_01:** Yeah, yeah. No one else was in Amsterdam. Bas was there for a short time. Relatively short time. And Jeffrey also left after a while and started his own company. Developed games or something. Yeah.

**[11:01] SPEAKER_00:** Though he did have. Oh, ETH Labs was another one. Do you know anything about ETH Labs? Because when Jeff worked with JP Morgan to do Quorum, that was announced under the label F Labs. Never heard of that.

**[11:18] SPEAKER_01:** Yeah, I think I heard the name, but I didn't really know what it does. But yeah, this is something I knew that Jeff started working with JP Morgan in that time big Banks really, really wanted to just talk to us at every defcon and we were always invited to fancy dinners by some main people and so. So Venks really wanted to learn about the technology. So Jeff went for a while to work on Forum. Yes.

**[11:52] SPEAKER_00:** Yeah. I mean, unless I can somehow get in contact with Jeff. I guess it's a little bit of a mystery what exactly F Labs was. Though I suspect it might be a little bit like Ethersphere of just sort of being a name, a banner for activity activities rather than a legal entity. And another thing I don't know there, but I suspect is I don't think Jeff told Ming that he was doing that stuff with jpm. I suspect that he completely just did that on his own without any communication with Ming or with the ef. It's just he went and did it.

**[12:35] SPEAKER_01:** He never really told a lot to us about that. So we knew that. Yeah, he's working with JP Morgan, but probably it's a big bang. Probably he had to sign contracts on disclosure agreement, so just he probably couldn't share all the details.

**[12:51] SPEAKER_00:** No, no. I mean, I remember at some point and I can't remember the context, him saying he found it interesting because the consensus for that was on chain. Like the consensus for that was happening as smart contracts. So it was kind of almost like this pluggable consensus, but consensus pulled up, you know, into the app layer. So he found that quite interesting that the initial quorum consensus, it didn't last long, but I think Gav also was doing that sort of stuff on the C side that he did some proof of authority stuff before that happened on the Geth side before clique, there was this. Okay, well he actually made a different C client, so you've got eth, but he made another one that was called Fluidity or something which was pulling all the libraries in the same, but it was with a proof of authority consensus. But that was one of the last things he did before he went out to Parity. So I think both him and Jeff were interested at that. Thought of, well, how can you formulate these pieces in different ways for those kind of use cases? Interesting. But yeah, he left. I think it was. I think it was probably very early in 2017. I did find a period, but it was certainly ahead of. Ahead of DEVCON 3. Let me see if I can find the date.

**[14:42] SPEAKER_01:** Yeah, I don't remember the exact date and actually there was maybe there wasn't even a really exact date when Jeff left because basically a month after I joined, Peter Sinaidi joined and he was the team lead for a very long time. So Jeff basically kind of handed it over to Peter and for a while he was officially still team lead, but not really. We haven't seen seen him on the calls for a while.

**[15:14] SPEAKER_00:** No. So the date I found there was February 2017. But I think I got that from GitHub. I think that was like his final commit. But he probably tailed off a long time before that.

**[15:28] SPEAKER_01:** He already started focusing on other stuff like this forum stuff and his own things sometime in 16. So.

**[15:35] SPEAKER_00:** Yeah, yeah, so started a company called Grid Games with his brother building. Building a particular game though that also seems to have ceased. So. Yeah, he's unknown off in the world somewhere.

**[15:51] SPEAKER_01:** Yeah, that's pretty much all I know about him. We try to invite him a few times to just come to some event and meet up. But yeah, I think for some reason he really had enough of maybe not us, but, but, but things going on in, in the EF and.

**[16:13] SPEAKER_00:** Yeah, I mean, yeah, I think that would be the case that you. You know, when Ming came in, she both did legal tidy up, but also cut the spending a lot. You know that you'd had the crowd sale in July, August, September 2014, but coming up to the mainnet release a year later, like nearly all the money was gone. Yes, they spent it very fast.

**[16:40] SPEAKER_01:** Yeah. So DEFCON 1 was postponed because of that, but we didn't really feel a lot of this. Actually Jeff just said that now that the ether price is so low. Actually I think the lower point was 42 cents.

**[17:00] SPEAKER_00:** Yeah. And full year it didn't really move.

**[17:04] SPEAKER_01:** And Jeff just said that. Okay. We all have to take a payment cut but the payment cut was really just 10% and I think maybe he took a bigger one. So yeah, for us it was really not that bad. And the idea was that when ether price reaches $2 then yeah, we do have some go back some, some, some time to some money to go forward. So yeah, then, then our, our salaries went back. So. And that wasn't a lot of time. So yeah, actually for, for I think, yeah, this, I don't, don't really remember the price history and maybe it's not the most important thing but, but I think iterprice reached something like $10 pretty soon.

**[17:56] SPEAKER_00:** Just in the start of 2016.

**[17:58] SPEAKER_01:** Yeah, and we went even a little bit higher. But then we had the dao fork and the Shanghai attacks and well, given how turbulent those times were, the market held pretty well and with $10 Enterprise we could survive further.

**[18:17] SPEAKER_00:** Yeah, yeah, I mean that was quite a jump up. I mean I heard that at the worst point there was only four months of Runway left. You know, that was how close it was to running out of money. But yeah, there were those big cuts which really, you know, resulted in like Gav and the C team were the main kind of like victims of those cuts. But then, yeah, just into 2016. Pardon me. So I was hired in February 2016, same time as Greg Colvin came in and also Pavel was rehired. You know, he, he was working through imap, you know, working on that jit. But they, that contract stopped. But then, then he came back at that time as well. So it was this, this period through late 2015 to early 20s. Sixteen was like, you know, the absolute bottom of like are we even going to ship this thing? Are we going to run out of money before we get to mainnet? But then yeah, some of us were really coming in as backfill for that. For that C team. Yeah. So I mean DEFCON 1 was sort of, you know, you were mentioning in that series that had got canceled, but then consensus came in and actually like paid for that and said hey, we'll will like mainly organize it and kind of so that the thing can happen. So that was the big, you know, the first public event. So what are your memories of Defcon1?

**[20:00] SPEAKER_01:** Well, my subjective impression was that it's really amazing. Yeah. Compared to today's DEFCON, it was small, I think 300 something people maybe, but I'm not sure, but less than a thousand definitely. And yeah, it was really, really prestigious venues. Some old bank building on Threadneedle Seat street, like city of London. And yeah, I really felt like, okay, so now this is really a serious thing. And probably that was the reason why consensys stepped in and funded the event so we really could step up in terms of public appearance and appear as something really serious. And yeah, I remember all the big banks having the booths at DEFCON 1.

**[20:56] SPEAKER_00:** Right? Yeah. And then Microsoft as headline sponsor. It's like wow. Recognition, right? That you're like, wow, Microsoft are interested and supportive and yeah, I mean, I think for a lot of people it was a real kind of wow. Like this is for real. You know, sadly, I could not afford to go. I watched the livestream. I was not, I was not quite in and working yet. I was an enthusiastic contributor. But

**[21:34] SPEAKER_01:** yeah, so actually it was also like the first time for me when I met a larger number of Ethereum people. So yeah, I first met the Go Ethereum team in like early 15. And yeah, I went to Amsterdam one more time I think in May. But DEFCON 1 was the place where I really realized how big this thing is and, and it's really not just about client developers, but also even back then people presented about formal verification and all this stuff. So yeah, I realized that this is really big and probably everyone wants to be a part of it at least a little bit.

**[22:22] SPEAKER_00:** Yeah, yeah, yeah. I mean, looking back at DEFCON 1 videos, it's like everything, like any kind of use case you could think of, you know, there was somebody presenting about it, you know, just so, so early, more than 10 years ago. But you know, many, many concepts which were probably like massively too early to do, but maybe you can do them more now seem to be presented. You had Nick Szabo as well. Nick Szabo doing a keynote.

**[22:49] SPEAKER_01:** Yeah, yeah, yeah. Nick Sabo was also there.

**[22:53] SPEAKER_00:** So was that maybe the first time that you'd met a number of the people in Berlin like Christoph Jantz and Lefteris and maybe even Gav?

**[23:03] SPEAKER_01:** I think I met some of these people already in London and I think first time I went to Berlin office back then it was like the other. Like it was like the old office. Yeah, right. But so yeah, some people I met at Defcon 1, some people I met in Berlin.

**[23:22] SPEAKER_00:** But yeah. So no. So was that. Was DEFCON 1 the first time that you'd been to do Ethereum things in London or did you. Did you go to any sort of London meetups or meet any of those comms people earlier?

**[23:41] SPEAKER_01:** I didn't go to any meetups to London before, but actually I I did. So Victor, Victor was in London at the time and, and I was, I, I went to London around the time actually if you're doing some, some, some. Event with my old software company, the Hungarian software company.

**[24:10] SPEAKER_00:** Yeah.

**[24:10] SPEAKER_01:** So we went to London to, to like, like, like, like sell our software and everything. So I'm still working there.

**[24:17] SPEAKER_00:** Right.

**[24:17] SPEAKER_01:** And after that, yeah, I met up with Victor and talked about Nice, yeah,

**[24:21] SPEAKER_00:** Ethereum related things because yeah, he, From what he was describing and then I was looking at videos and things later. He had seen Gav talk in London in very, very early February, I think it was February 6th. So almost immediately after they'd had the Miami like you know, BTC Miami launch, you know, Vitalik's first public talk and, and the, you know, Anthony Di Orio's like mansion where they, you know, a lot of them met for the first time. Gav had been back in London, I think it was like a week, a week after and did a talk there that Victor had gone to. That was Victor's first, you know, in person meeting with any of these. And then you know, Gavard pulled him on board.

**[25:19] SPEAKER_01:** Yeah, so those are like the very early days I wasn't there. So when I first heard about Ethereum that was I think March or April 14th. So, so I first heard about the pre sale and yeah, that's where I first heard about this thing. But yeah, I know that Gavin was one of the very early founders of this and he wrote the yellow paper full of Greek ladders.

**[25:51] SPEAKER_00:** Very confusing. Yeah. And the C client of course. So the first time I think I saw your name or was in contact with you was about Light Client because I'd been trying to get Ethereum, ARM Linux cross builds running on my smartwatch and my thought there was get the thing running and then this Light client stuff is just kind of starting and scaling will be solved. Right. We're going to be able to run these nodes on anything. You know, you'll have them on your phone, smartwatch, router, they'll be in every operating system. You know, it's just will solve that scaling and that lightness. So you were plunged right into that problem. Right?

**[26:38] SPEAKER_01:** Yeah. So when Jeff hired me actually he put me on this, he has put me on this project. So he just said that, okay, it's great that I contributed to Swarm, but if I join the GATT team I will have to start working on the Light client because it's a very important thing and it hasn't been started yet. So yeah, I felt really good about It, I also felt like this is a big thing and yeah, back then it really felt like we do these few things, we have a working light client protocol and, and the whole trinity of base layer and then we're all good. Yeah, it wasn't that easy, but still those were the first steps and so I designed the LES protocol. In retrospect, it didn't make a lot of sense to design to build it over the devp2p layer because it, it wasn't easy to access from web browsers stuff. But also, also it was, it was a proof of work based light client.

**[27:51] SPEAKER_00:** Right.

**[27:52] SPEAKER_01:** So yeah, that, that project ended after a while but I'm still very much into like trustless chain access. So that's, that has usually been one of my focuses all the time. So right now I'm also working on, on something called the Trustless Execution Layer API which is similar to the Beacon REST API but works on the execution layer and provides everything with proofs. So yeah, I'm still very much into this because I think this is where Ethereum really makes sense if even normal users access chain data with proofs.

**[28:36] SPEAKER_00:** Right, right. And there was a project called Portal as well. Were you involved with Portal? That was a later kind of light client.

**[28:44] SPEAKER_01:** No, I wasn't. So Portal was Piper Mariam's brainchild. So by the time we kind of realized that LES was a nice first experiment, but maybe not the best approach, he started something different that was UDP based and also used different topologies. So it was kind of a DHT approach to storing the chain and the state. And yeah, actually I'm kind of, I think it's a bad thing that it, it's been completely canceled because actually to be honest, I never really believed that it will be an easily solvable problem to store the Merkel Petrusha tri of the state on dht but for the chain data it made perfect sense. So yeah, maybe, maybe the state would have been possible with a lot of work. But yeah, I mean Piper told me of few times about how he imagines to solve all the unsolvable problems and I felt like yeah, it sounds good but he just made a lot of really hard assumptions about VHTs that by the time I already worked on Discovery V5, so there was also this discovery protocol that basically we designed it in 2016 in Berlin with Felix.

**[30:20] SPEAKER_00:** Right.

**[30:20] SPEAKER_01:** And I released the original version and yeah, so. So I already knew that. Yeah, it's, it's, it's never so easy to imagine like a DHT that's that's efficiently formed and all the nodes are working and yeah, like this. So but, but for the, for the, for the chain data.

**[30:37] SPEAKER_00:** Right.

**[30:37] SPEAKER_01:** Especially with EIP 444. So like, like that lets the MEME protocol, the nodes processing meme protocol forget the ochain history. So it made perfect sense to at least put the chain history on a dht. But yeah, so it was an EF decision that it was discontinued at a point.

**[31:05] SPEAKER_00:** Well, I mean, I guess the thing is, you know, Patricia Merkle trees are not great for you know, the number of accesses and things anyway, let alone if you're making each of those steps over a networked, you know, DHT kind of setup. That's. Yeah, there's a lot of. It's so much transactional change complexity.

**[31:31] SPEAKER_01:** State 3 suffers from a lot of issues, especially in the Merkur Patricia State 3. Yeah and yeah, it's a huge data set that keeps changing all the time and keeps changing at completely random places and it's not as easy as task to distribute it. So actually it's getting harder to even synchronize it between full node storing the entire stuff.

**[32:00] SPEAKER_00:** So do you think that proofs are going to be a magic, you know, magic silver bullet here where by having you know, local proofs versus you know, massive really redundant state machines. Do you think there's a path here where.

**[32:19] SPEAKER_01:** Oh, oh yeah. No, it's not a silver bullet. So I assume you mean what people call statelessness. So it's a good thing. It definitely allows higher degree of scanning. But the state tree still has to be processed and maintained by someone and especially if most of the nodes have no incentive to process it. And yeah, now we are talking about 100x and thousandx scaling then even if we also do state expiry which is currently imagined in a way that we basically reset the state tree every year or something and have multiple state trees. So yeah, that has somewhat. But if we scale a thousand x then it will be a huge infrastructural centralization issue.

**[33:21] SPEAKER_00:** Right.

**[33:21] SPEAKER_01:** And yeah, by the way, this thing is not an unsolvable problem. I mean the state as it works today, unfortunately somehow makes it really hard to do any fundamental improvements over these properties. But people are considering different storage architectures. Of course we have to keep the existing contracts workable because that was our main promise from the beginning that we will not just shut down anything. Everything has 100% uptime. But it is a viable way to come up with more efficient storage methods and use it as an opt in alternative that will over time be available for much less and new contrast can be designed using those more efficient storage architectures.

**[34:28] SPEAKER_00:** Yeah, because Verkal trees seem to be the first sort of thought on that. But then that's kind of come and gone and maybe it's a binary tree

**[34:37] SPEAKER_01:** or actually it does either.

**[34:40] SPEAKER_00:** You don't think it's so important either.

**[34:42] SPEAKER_01:** I mean, I mean, I mean both are better than the Merkel Patricia 3 but in some ways. But they don't solve this fundamental issue by themselves. So still the thing is that the state is a permanent key value store and in order to avoid it growing forever. Yeah there's all these ideas about state expiry, but still it's going to be a huge data set and the method of hashing or consensus protocol representation doesn't fundamentally change this. So Verkle was supposed to provide more efficient Merkle proofs but also I guess somewhat more expensive state processing because it's like more expensive cryptography. Also if I'm correct, it's not quantum secure. So. And that was also a thing that I always felt like yeah, I'm not sure if it's a good idea to start working from now and I just saw it in front of my eyes how it's going to be canceled.

**[36:00] SPEAKER_00:** Yeah, yeah. I mean, I guess for running nodes in general, you know there's not a lot of incentive for people to run any kind of like node software themselves unless they are you know, a validator or you know, you're running an exchange or a business and you, you know, you need your node back end to that. You know, I guess the vision of that there was at the start, start of like well yeah, everyone will be running their own node and you, you. So you've got mist on top of it and you know, it's, it's local apps, you know and then that, that can have swarmed for the smart contracts and you know, you, it's almost like you won't have server architecture because everyone's running a server stack and then yeah,

**[36:46] SPEAKER_01:** that, that did not happen actually, actually that's. So that's why we are also stuck with the, with the JSON RPC API which doesn't provide proofs except for it get proofs but doesn't provide proofs for a lot of things because, because it was never meant to be used remotely. It was always imagined that it's used locally in a trusted setup on your own machine. And yeah, I remember all those good old days when I just synced up a FUA node it was a few gigabytes of disk space and ran mist on top of it. And yeah, it's magic but yeah, unfortunately it didn't scale.

**[37:26] SPEAKER_00:** No, no. At the Museum of Ethereum here I've got laptops running geth 1.36 so homestead geth and I mined Homestead back to life. So you know, any hard fork that happens, the old one doesn't go away, right? It doesn't disappear. It's just people don't associate any economic value with it and it kind of gets abandoned. But yeah, what I've done is first GPU and then down to CPU mined that homestead difficulty down to the level that you can CPU mine it again. So I do, I have got mist running on those so we can go and transact, we can send a transaction between those and it should be possible to run Aleph zero and Aleph one and mix on that as well. I haven't had time to do that. And ERC20 tokens existed. You could have DAO tokens or mist coin at that time. But yeah, the assumption that people would run their own node and it would all be self sovereign local apps certainly did not come to fruition.

**[38:54] SPEAKER_01:** Well, yeah, that's when the Light client came in and then we assumed that okay, then we do the light client and then it will be all solved.

**[39:01] SPEAKER_00:** But that's what I was thinking is like right, I've got, I've got a full node running on my smartwatch that works and I'll just wait for you and the other guys to sort out Light client and just turn that on and there we go.

**[39:15] SPEAKER_01:** Well, actually the Light client protocol worked fine. It's just, yeah, I spent like a really crazy amount of time figuring out how it could be decent like, like incentivized in a truly decentralized way. Because yeah, I, I remember this. There was this idealism that, that yeah, now, now we are almost done with everything so we just have to find a real proper way for incentivizing things. But not in a way that there's a few companies where you can buy tokens, but through truly in a decentralized way, which is much harder because yeah, then we have to somehow build decentralized trust and figure out market mechanisms that work without initial trust. So yeah, this is something I spent years with and honestly I think I came up with some nice theoretical models and a lot of really complex code. But yeah, it's just again was like the wrong approach, maybe also at the wrong time. So we were just not there. Really.

**[40:27] SPEAKER_00:** Yeah, because I mean BitTorrent has obviously worked for distributing content for many, many years. But then you, you do have this tragedy of the Commons, right, as yes, the latest Hollywood movie, someone has ripped it off and people, people want that. So that's going to get shared around, no problem. But things which are only of interest to a smaller number of people without incentives, it's just a leeching problem. Right,

**[41:00] SPEAKER_01:** good.

**[41:00] SPEAKER_00:** Full node runners would contribute, they'd turn on Les as well. Right. They would help supply that. But the incentives and economics of that, not easy.

**[41:14] SPEAKER_01:** Yeah. Actually with Bitterant it also usually if you really want to use it, it requires trackers where you buy some priority access. So there are these private trackers and everything. So yeah, and this is also not completely decentralized, but actually it does work. So it's definitely better than nothing. But for Alias it wasn't really this easy because this whole service was like downloading movies was an application that everyone understood that everybody used. And somehow with Ethereum it was always this. Yeah, everyone felt the importance, but if you're nowhere near close to a really mature ecosystem. And so it was just, I don't think there would have been a big enough market really for these services so that to really work out in a market based way. But as we scale and accessing the whole data set becomes more and more difficult. At a certain point I think we are going to have something like reimagined several years ago. So yeah, it's just both like timing and specifics. Yeah, I was right about everything except timing and specifics.

**[42:46] SPEAKER_00:** Yes, yes. Yeah. I mean there's a number of things that seemed like they would be easy and quick and obvious and have taken so many years. I mean like proof of stake, you know, the, it was in the white paper there was an assumption, you know, later in 2015 that will happen, you know, within six months, maybe three, six months. And then it's, it's eight years before, you know, it actually went live and. Yeah, I mean on storage. So Filecoin, their first white paper was in 2014 as well. You know, Filecoin was not a new thing and IPFS was around before Ethereum as well. And then, yeah, Whisper kind of went for a while and then now there's Waku and you've had status driving a lot of those techs for a lot of those years as well. You know, Jared Hope and team who were also doing Android version of the Java client, same kind of time as I was looking at smartwatches, Jared Hope

**[44:04] SPEAKER_01:** was also very eagerly waiting for Fully functionalized client.

**[44:10] SPEAKER_00:** Yeah, yeah, yeah. Well yeah, because you know they were building kind of decentralized WeWork, you know, super app but I guess kind of a competitor to mist really similar kind of thing wanting to have a container for running DAPPS in sitting on top of a local client again having this completely self sovereign kind of server app stack but not easy. I can't remember who it was that was telling me when they first saw metamask which was at devcon one that was one of the grantee winners was metamask them thinking no, that's not what we want. We don't want some browser extension thing talking to a trusted endpoint. That's absolutely the opposite. What are these guys doing? And then that's become the standard flow, right?

**[45:15] SPEAKER_01:** Well yeah, so this is still kind of an unsolved problem to access everything in a truly decentralized way but I think we are getting there over time. It's just nothing is as simple as we initially imagined. And also there's a time for everything and I think through decentralized infrastructure will be forced by scaling and things sometimes just doesn't happen if they are not forced by some circumstance some external factor. So as long as it works in a lazy way to just connect MetaMask to Infura until then it's the standard way.

**[46:12] SPEAKER_00:** Yeah, yeah. So I think I found two different talks of yours at devcons talking really about Light Client. Do you remember? Did you talk in London or was Shanghai your first?

**[46:26] SPEAKER_01:** No, I talked at London, also Shanghai and also in Cancun. Yeah so those were the first two dev concepts were mostly about the Light client. So they actually the first release of the Light client protocol was in 16 so it was around that time and later I already started to invent all, all the next chapters of decentralized technology. And yeah, it was really naive of me but I also had this project back then where I started to try to make logs provable efficiently and yeah that was the initial attempt for that was in 2017 and now I'm back at it. Now I'm also like I also have this trust as long index project and yeah so this old approach as 2017 that was just a more efficient way to organize the Bloom filters but it didn't really solve the problem of the Bloom filters not adapting to the number of events and also it never, I never even proposed it putting it into consensus which would have allowed actual trustless proofs through the chain.

**[47:58] SPEAKER_00:** Right.

**[47:58] SPEAKER_01:** So yeah that, that also proved to be a, a hard problem but yeah, this is one of the things what I presented in Cancun.

**[48:08] SPEAKER_00:** Right, right, right.

**[48:10] SPEAKER_01:** And also some kind of my, my ideas of, of state channels. So back then we didn't have like L2s in a way. So actually back then layer 2 just meant something that happens off chain, not necessarily another blockchain. And yeah, so yeah, I had these ideas about individual nodes running or running their own blockchains somehow organizing some off chain calculations through that. But yeah, it was also assumed a lot about how nodes would operate and probably would have never worked in retrospect.

**[48:53] SPEAKER_00:** Yeah, I mean we had state channels and then we had plasma and then eventually coming into optimistic roll ups and then ZK later. Just many, many different attempts.

**[49:06] SPEAKER_01:** Hello.

**[49:07] SPEAKER_00:** See you sir.

**[49:07] SPEAKER_01:** Great to see you.

**[49:10] SPEAKER_00:** So, so yeah, I mean I, I guess there's an awful lot of learning, right. Ten years worth of lots of people trying lots of different things. So I mean in terms of the Geth team, has that been similar over the years or have you had, you know, larger and smaller amounts of people? Has it been a similar kind of flow through that time?

**[49:36] SPEAKER_01:** I would say it was pretty consistently around 10 people throughout all these years, sometimes 8, 9, sometimes 11, 12. But really like in this range we did improve our internal processes during the years. So yeah, now we do have like all this issue and pull request triages and yeah, but really it's been mostly, mostly that team was also always small enough so that we didn't need a lot of processes. Honestly, the team culture, yeah, it did obviously did change, especially with certain people coming and going. But it also, I would say it was always a good team culture. I always liked the GATT theme. That's also why I never really looked into moving to other teams or other projects because I felt that the team is the best place to do meaningful things.

**[50:56] SPEAKER_00:** Yeah, I mean it's funny because from the very start of Ethereum, the intention was to have multiple clients. Right. That was a very basic decision of saying we want a separation between the specification and the implementation. Right. Because we don't want it to be like Bitcoin where you've got one code base and then like there's no like competition, there's no, you know.

**[51:20] SPEAKER_01:** Well, yeah, for Bitcoin's complexity that approach worked, but for Ethereum's complexity I would say this was one of the best decisions. Yeah, it also contributed to almost running out of money by the time we launched Mainnet. But I would say it was money well wasted.

**[51:40] SPEAKER_00:** So yes, no, I would agree it was not efficient, but the outcome was very much worthwhile.

**[51:48] SPEAKER_01:** Yeah. And when we switched to proof of stake we again successfully applied this pattern by funding multiple CL implementations and then testing every EL against every CL and then running testnets with all the five.

**[52:09] SPEAKER_00:** Is it five? Five different primary consensus clients? There are. I think it's five and yeah, notably none of those were within the foundation either. They were all independent companies and teams. So I mean on the execution side there have been a good number of different alternative execution clients over the years. So I mean how, how have you tended to work and interact in that kind of environment where you've got all these different I guess starting with Parity and then Bezu and Nevermind Eragon. So how do you work with other teams?

**[52:53] SPEAKER_01:** Well. Now we have all the ACD calls and testing calls so mostly, I mean we all do have working clients all the time. So by default we don't need to interact a lot. We have to interact when we are testing out new features. There are the prepared forums for that. So yeah. And it's also some people keep more contacts outside of the GET team, some people are more turning inwards and then just focusing on GET issues. But actually I think in the first years communication was really not organized well so we really just tried to figure out things and some people knew some people from the other teams but actually these days we have much better processes for this. Also it's a much, much bigger challenge because there are so many more people. Actually this, this is also something I realized during the time we really started working on proof of stake. So in 2017 was the first time Ether price went to several thousand dollars and yeah the foundation had that had money to hire new teams and found external teams. And I remember that until 2017 I mostly met non go Ethereum people mostly at defcons.

**[54:37] SPEAKER_00:** Right. Yeah.

**[54:37] SPEAKER_01:** And maybe those people who lived in Berlin or one of those cities where there were multiple people they, they met more people. But I, I, I, I, I was a mainly in Hungary and worked remotely and yeah I mostly met most of the people at Defcons but around I think it was 2018 where so many like researchers and have we hired and there were also the Seattle teams and I remember Death Code four as Prague. Yeah so until then it was mostly I don't know how many people exactly but I do remember it's maybe 30, 40 people. I don't know after every Defcon we stood up at the main stage and did a group photo.

**[55:28] SPEAKER_00:** Oh yeah, yeah.

**[55:28] SPEAKER_01:** We are the Ethereum Foundation.

**[55:30] SPEAKER_00:** Yes.

**[55:30] SPEAKER_01:** Like it was that Many people. And in 18 I just, I was just shocked. Like who the hell are all these people? The all Ethereum Foundation. So yeah, it was, it became a much bigger challenge. But also now we do have all these official forums and also I try to go to more events, not just defcons. So yeah. In order to keep all the context live.

**[56:00] SPEAKER_00:** Yeah, yeah. So I mean looking back to when you first started working on Ethereum,

**[56:08] SPEAKER_01:** did

**[56:08] SPEAKER_00:** you have any kind of thought or vision of what things might have looked like 10 years later? Like has it worked out as you expected or differently or what's your looking back on these 10 years? What's your thought?

**[56:25] SPEAKER_01:** I always had a lot of visions. Yeah, maybe I was too focused on visions sometimes at Yale. So thing is that we all kind of have to imagine the future at every point even though we know we can't imagine it as it will turn out. So it never turns out exactly the way we want but we always have to have some kind of direction and we have to just have ideas of how things can turn out. So yeah, around like 2017 I also realized that scaling will not happen just with L1. So I also had this, as I mentioned, had these ideas about how we could solve problems more efficiently with not even roll ups, just application specific state channels and stuff like that. But it also, there was this really great project. Oh, okay. I don't. Yeah.

**[57:34] SPEAKER_00:** Raiden.

**[57:35] SPEAKER_01:** Raiden. Yeah. Thank you. Thank you. So, so, so yeah, they, they properly implemented the protocol and everything.

**[57:41] SPEAKER_00:** Yeah.

**[57:41] SPEAKER_01:** I think it has always struggled with like not many people using it. So it's, it's, it's, it's, it's a pain. It's a pain that the transactions are expensive but still somehow maybe we just missed some organizing force to really move to some kind of layer two solutions and it was just.

**[58:10] SPEAKER_00:** Yeah, well it was meant to be lightning for Ethereum, right? That was the thought.

**[58:16] SPEAKER_01:** Well yeah, it was pretty much that

**[58:18] SPEAKER_00:** idea but then lightning's kind of failed so maybe not surprising if an Ethereum version of that's not really got. Because you've got routing issues. Right. It's really complicated that Channels seem to work great for consistent static topographies. If you want to do merchant to merchants channels work great.

**[58:46] SPEAKER_01:** Yeah. But opening those channels is still costly and non trivial and yeah, it's just. I also never really. I installed it, I tried it. I. Okay, this is interesting but I never really made a payment through Raiden because there was just no occasion where the other party really wanted Raiden Transfer.

**[59:14] SPEAKER_00:** No. No. Well, thank you very much. I think we can wrap it up there. So thanks for your time and thanks for all of your work on Geth over these very many years. Geth has always really been the backbone of Ethereum. New clients come and go, but Geth remains. So thank you.

**[59:39] SPEAKER_01:** Thank you for having me here.

**[59:40] SPEAKER_00:** Thank you so much.