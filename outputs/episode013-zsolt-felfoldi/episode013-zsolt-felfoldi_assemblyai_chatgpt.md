**[00:02] SPEAKER_00:** So, hello and welcome to FDenver 2026. Recording here for Early Days of Ethereum with Zsolt Felföldi. How do you pronounce your name?

**[00:14] SPEAKER_01:** Zsolt Felföldi.

**[00:16] SPEAKER_00:** There you go. Anyway, I was working out when we recently reconnected at Devconnect, and I was working out that you're the third longest-serving person at the Ethereum Foundation, right? You've got Vitalik, and then Felix, and then you.

**[00:38] SPEAKER_01:** Yeah, I haven't really checked this fact yet, but honestly, yeah, it sounds great.

**[00:46] SPEAKER_00:** That's it. You're a very long-time member of the Geth team.

**[00:52] SPEAKER_01:** Yes.

**[00:52] SPEAKER_00:** But what were you doing before you started at the Foundation? What was your background? How did you find your way into the blockchain world?

**[01:02] SPEAKER_01:** Before Ethereum, I was working on really different types of projects. I first started at a Hungarian software company, a really classic software company. We actually sold software in boxes, like put on a shelf—floppy disks. Put it in a box on a shelf and you can buy the software. So this type of classic software.

**[01:35] SPEAKER_00:** Five and a quarter. Five and a quarter inch floppies.

**[01:38] SPEAKER_01:** Yeah, yeah—actually three and a half.

**[01:42] SPEAKER_00:** Oh, okay. Three and a half. We're onto modern floppies.

**[01:46] SPEAKER_01:** Yeah, but maybe also—I started in 97, so maybe I was exaggerating a little. By that time it was mostly CDs. We still used a lot of floppies anyway, so those. At that company I did things related to—first things related to computer graphics. I wrote a ray tracing engine for some architectural software. And then I also did a lot of work on electronic circuit simulation and circuit design.

**[02:20] SPEAKER_00:** Right.

**[02:21] SPEAKER_01:** So yeah, really different things. And it was around 2011 when I first heard about Bitcoin, and around 2012 when I started to realize that, as weird as it sounds, it really is probably a big thing. Actually, I first heard about Ethereum early 2014, a few months after the initial paper had been published.

**[02:53] SPEAKER_00:** Yeah.

**[02:54] SPEAKER_01:** And yeah, started contributing I think around November, and officially joined EF in 2015, March. So, yeah.

**[03:05] SPEAKER_00:** And did you hear about it, you think, through Danny and Viktor, or some other way?

**[03:14] SPEAKER_01:** Well, I did hear about it from Danny and Viktor’s friend circle.

**[03:22] SPEAKER_00:** Right.

**[03:22] SPEAKER_01:** Yeah, but then Viktor was already—actually, I didn’t know Viktor before. I heard about this thing through one of Danny’s friends, and then Viktor was also in that wider circle, and he came to Hungary and said, “Oh, I’m already working on this.” And then I started with my ideas and started to explain to him why this thing probably will never work. And he was like, “Okay, you seem to have a good understanding of this. Why don’t you come to work?”

**[03:52] SPEAKER_00:** Right, right. And was I right in thinking that you said it was Swarm that you started with?

**[04:00] SPEAKER_01:** Well, yeah. Swarm was part of this initial trinity of base technologies of Ethereum. It was supposed to be the storage layer for dapps. It was kind of a naive way of how people imagined decentralized applications back then, but honestly it made sense at the time. Nothing ever turned out exactly the way people imagined it, but we are still making a lot of progress. So yeah, Swarm was how we initially imagined this storage layer for Ethereum. And I mean, this project still has merits, but this whole problem space is just a bit more complex. But yeah, I started contributing to Swarm first, and actually I wrote the first 500 lines of Swarm.

**[05:02] SPEAKER_00:** There you go. Yeah, I think if I remember rightly that Viktor mentioned around May 2014 was when he first heard the trinity—the concept that you could have Ethereum as your compute and expensive database, Swarm as your decentralized storage, and then Whisper as your messaging. That famous diagram, right, with the circle and the things coming in, and Whisper going around the edge. But yeah, I guess it was Devcon 0 where Danny really presented a sort of fleshed-out vision of decentralized storage.

**[05:54] SPEAKER_01:** Yes, that's correct. I wasn't there at Devcon 0 yet. I heard about this idea even before I heard about Ethereum. Danny told me about this idea that he wants to do this kind of hash-based chunk storage, and yeah, it made total sense that he just pitched that.

**[06:14] SPEAKER_00:** That can fit in.

**[06:16] SPEAKER_01:** Yeah, at the time it was a perfect fit. So he pitched this idea at Devcon 0, and when they accepted it and hired Danny, then he called me and said—because he already knew that I knew of this project—yeah, then let’s do it together.

**[06:38] SPEAKER_00:** There you go. And then you were hired into EF. I did have a date for that. I've forgotten. I guess it was shortly after Devcon 0, right, that you started there?

**[06:51] SPEAKER_01:** Yes, correct.

**[06:53] SPEAKER_00:** Did you go to Berlin or Amsterdam? When did you first meet other people? How did—

**[07:01] SPEAKER_01:** It was Amsterdam in February ’15. That's where I met Jeffrey Wilcke, the creator of Go Ethereum, and the Go Ethereum team. Back then, I don't say “Geth” because that abbreviation was invented later. So yeah, that's where I met the Go Ethereum people. And I already had these contributions to Swarm, and it was kind of an implied thing that maybe I might be hired, but there was really no official hiring process back then. It was really just Jeff—this really laid-back guy—and he just said, “Okay, man, I saw your contributions and let's talk sometime this week.” And I waited the whole week and waited for some serious interview—this was a dream job for me. By that time I was really enthusiastic about this whole thing, and I felt like—even though I felt that this whole initial design was hard, I really couldn't imagine how it would scale and everything. And it is a hard problem. So yeah, it was true, but it was still worth starting it, and I was really enthusiastic and I really wanted to get hired. And the whole week I just waited. And at the end of the week, like the last half an hour before we all left home, Jeff just said, “Oh yeah, man, I wanted to talk to you. You're hired.” Okay, that's a good talk. So yeah, this is how the hiring process went back then.

**[08:50] SPEAKER_00:** Excellent. Well, that's easy. We like that. And so that was before you went to Amsterdam, I assume. I assume you went to Amsterdam after you had been hired.

**[09:04] SPEAKER_01:** No, no, no. It happened in Amsterdam.

**[09:06] SPEAKER_00:** Oh, I see. So you were there unhired, on site.

**[09:10] SPEAKER_01:** Yeah. Jeff agreed that—I bought my own plane ticket, but I could stay at the Airbnb the team stayed at. And yeah, I just worked with them and showed my contributions. So I went to Amsterdam unhired.

**[09:27] SPEAKER_00:** Yeah, I mean—right, right.

**[09:29] SPEAKER_01:** That plane ticket was a good investment.

**[09:31] SPEAKER_00:** Yeah. So did they not have office space at that point even?

**[09:36] SPEAKER_01:** Well, they did actually. Back then there was an Amsterdam office.

**[09:40] SPEAKER_00:** Right.

**[09:41] SPEAKER_01:** It was mostly for Jeff because Jeff lived in Amsterdam. But when Jeff left EF—or maybe before that, I'm not sure exactly—this office was closed. And actually it was a really small office last time I checked. Now I think it's a dentist that works there. So yeah, it doesn't exist, but it was really just a small place. But later I went to Berlin a lot. After I was hired, it was for the Geth team. It was really centered in Berlin, so.

**[10:24] SPEAKER_00:** Right, right. Because as well as Jeff, you've got Bas, right? He was another Amsterdam person, Bas van Kralingen. But then maybe most of the other team members weren't in Amsterdam, I mean.

**[10:43] SPEAKER_01:** Yeah, no one else was in Amsterdam. Bas was there for a relatively short time. And Jeffrey also left after a while and started his own company—developed games or something.

**[11:01] SPEAKER_00:** Though he did have—oh, ETH Labs was another one. Do you know anything about ETH Labs? Because when Jeff worked with JPMorgan to do Quorum, that was announced under the label EF Labs. I'd never heard of that.

**[11:18] SPEAKER_01:** Yeah, I think I heard the name, but I didn't really know what it does. But yeah, I knew that Jeff started working with JPMorgan in that time. Big banks really, really wanted to talk to us at every Devcon, and we were always invited to fancy dinners by main people. So banks really wanted to learn about the technology. So Jeff went for a while to work on Quorum, yes.

**[11:52] SPEAKER_00:** Yeah. Unless I can somehow get in contact with Jeff, it's a little bit of a mystery what exactly EF Labs was. Though I suspect it might be a little bit like Ethersphere—just being a name, a banner for activities rather than a legal entity. And another thing I suspect is, I don't think Jeff told Ming Chan that he was doing that stuff with JPMorgan. I suspect that he completely just did that on his own without any communication with Ming or with the EF. He just went and did it.

**[12:35] SPEAKER_01:** He never really told a lot to us about that. So we knew that he was working with JPMorgan, but probably it’s a big bank. He probably had to sign contracts and nondisclosure agreements, so he probably couldn't share all the details.

**[12:51] SPEAKER_00:** No, no. I remember at some point—I can't remember the context—him saying he found it interesting because the consensus for that was on-chain. Like the consensus was happening as smart contracts. So it was kind of almost like this pluggable consensus, but consensus pulled up into the app layer. So he found that quite interesting. The initial Quorum consensus, it didn't last long. But I think Gav also was doing that sort of stuff on the C side: he did some proof-of-authority stuff before that happened on the Geth side before Clique. There was this—okay, well he actually made a different C client. So you've got eth, but he made another one that was called Fluidity or something, pulling all the libraries in the same, but with a proof-of-authority consensus. But that was one of the last things he did before he went out to Parity. So I think both him and Jeff were interested in that thought of, well, how can you formulate these pieces in different ways for those kind of use cases? Interesting. But yeah, he left. I think it was probably very early in 2017. I did find a period, but it was certainly ahead of Devcon 3. Let me see if I can find the date.

**[14:42] SPEAKER_01:** Yeah, I don't remember the exact date. And actually there maybe wasn't even a really exact date when Jeff left, because basically a month after I joined, Péter Szilágyi joined, and he was the team lead for a very long time. So Jeff basically kind of handed it over to Péter, and for a while he was officially still team lead, but not really. We haven't seen him on the calls for a while.

**[15:14] SPEAKER_00:** No. So the date I found there was February 2017. But I think I got that from GitHub. I think that was like his final commit. But he probably tailed off a long time before that.

**[15:28] SPEAKER_01:** He already started focusing on other stuff, like this Quorum stuff and his own things sometime in ’16.

**[15:35] SPEAKER_00:** Yeah, yeah. Started a company called Grid Games with his brother, building a particular game. Though that also seems to have ceased. So yeah, he's off in the world somewhere.

**[15:51] SPEAKER_01:** Yeah, that's pretty much all I know about him. We tried to invite him a few times to come to some event and meet up. But yeah, I think for some reason he really had enough of—maybe not us—but things going on in the EF.

**[16:13] SPEAKER_00:** Yeah. I think that would be the case. When Ming came in, she both did legal tidy-up, but also cut the spending a lot. You had the crowdsale in July, August, September 2014, but coming up to the Mainnet release a year later, nearly all the money was gone. They spent it very fast.

**[16:40] SPEAKER_01:** Yeah. So Devcon 1 was postponed because of that, but we didn't really feel a lot of this. Actually Jeff just said that now that the ETH price is so low—I think the low point was 42 cents.

**[17:00] SPEAKER_00:** Yeah. And for a full year it didn't really move.

**[17:04] SPEAKER_01:** And Jeff just said, “Okay, we all have to take a payment cut,” but the payment cut was really just 10%, and I think maybe he took a bigger one. So for us it was really not that bad. And the idea was that when ETH price reaches $2, then we go back to some normal level. Our salaries went back, and that wasn't a lot of time. I don't really remember the price history, and maybe it's not the most important thing, but I think ETH price reached something like $10 pretty soon.

**[17:56] SPEAKER_00:** Just in the start of 2016.

**[17:58] SPEAKER_01:** Yeah, and we went even a little bit higher. But then we had the DAO fork and the Shanghai attacks, and well, given how turbulent those times were, the market held pretty well. And with $10 ETH price we could survive further.

**[18:17] SPEAKER_00:** Yeah, yeah. That was quite a jump up. I heard that at the worst point there was only four months of runway left. That was how close it was to running out of money. But yeah, there were those big cuts which resulted in—Gav and the C team were the main victims of those cuts. But then, yeah, into 2016—pardon me—I was hired in February 2016, same time as Greg Colvin came in and also Pavel was rehired. He was working through IMAPP, working on that JIT, but that contract stopped. Then he came back at that time as well. So it was this period through late 2015 to early 2016 that was the absolute bottom of “Are we even going to ship this thing? Are we going to run out of money before we get to Mainnet?” But then some of us were really coming in as backfill for that C team. Devcon 1 had gotten canceled, but then ConsenSys came in and paid for that and said, “Hey, we’ll mainly organize it,” so the thing can happen. That was the big first public event. So what are your memories of Devcon 1?

**[20:00] SPEAKER_01:** My subjective impression was that it's really amazing. Compared to today’s Devcon, it was small—300-something people maybe—but I'm not sure. But less than a thousand definitely. It was a really prestigious venue, some old bank building on Threadneedle Street, City of London. And I really felt like, okay, now this is really a serious thing. Probably that was the reason why ConsenSys stepped in and funded the event so we really could step up in terms of public appearance and appear as something really serious. And I remember all the big banks having booths at Devcon 1.

**[20:56] SPEAKER_00:** Right. And then Microsoft as headline sponsor. It's like, wow—recognition, right? Microsoft are interested and supportive. I think for a lot of people it was a real kind of, “Wow, this is for real.” Sadly, I could not afford to go. I watched the livestream. I was not quite in and working yet. I was an enthusiastic contributor.

**[21:34] SPEAKER_01:** Yeah. It was also the first time for me when I met a larger number of Ethereum people. I first met the Go Ethereum team in early ’15. And I went to Amsterdam one more time, I think in May. But Devcon 1 was the place where I really realized how big this thing is, and it’s really not just about client developers. Even back then people presented about formal verification and all this stuff. So I realized that this is really big, and probably everyone wants to be a part of it at least a little bit.

**[22:22] SPEAKER_00:** Yeah, yeah. Looking back at Devcon 1 videos, it's like everything—any kind of use case you could think of, there was somebody presenting about it. So early, more than 10 years ago. Many concepts which were probably massively too early to do, but maybe you can do them more now, were being presented. You had Nick Szabo as well, Nick Szabo doing a keynote.

**[22:49] SPEAKER_01:** Yeah, yeah. Nick Szabo was also there.

**[22:53] SPEAKER_00:** Was that maybe the first time that you'd met a number of the people in Berlin, like Christoph Jentzsch and Lefteris and maybe even Gav?

**[23:03] SPEAKER_01:** I think I met some of these people already in London. And I think the first time I went to the Berlin office back then it was the old office. So yeah, some people I met at Devcon 1, some people I met in Berlin.

**[23:22] SPEAKER_00:** Was Devcon 1 the first time that you'd been to do Ethereum things in London, or did you go to any sort of London meetups or meet any of those comms people earlier?

**[23:41] SPEAKER_01:** I didn't go to any meetups in London before, but actually I went to London around the time I was doing some event with my old software company, the Hungarian software company.

**[24:10] SPEAKER_00:** Yeah.

**[24:10] SPEAKER_01:** We went to London to sell our software and everything. I was still working there. And after that I met up with Viktor and talked about Ethereum-related things.

**[24:21] SPEAKER_00:** Yeah, because from what he was describing, and then I was looking at videos and things later, he had seen Gav talk in London in very, very early February—I think it was February 6th—almost immediately after they'd had the BTC Miami launch, Vitalik's first public talk, and Anthony Di Iorio's mansion where a lot of them met for the first time. Gav had been back in London, I think it was like a week after, and did a talk there that Viktor had gone to. That was Viktor's first in-person meeting with any of these, and then Gav pulled him on board.

**[25:19] SPEAKER_01:** Yeah, those are the very early days. I wasn't there. When I first heard about Ethereum that was, I think, March or April ’14. I first heard about the presale, and that's where I first heard about this thing. But yeah, I know that Gavin was one of the very early founders of this, and he wrote the Yellow Paper full of Greek letters.

**[25:51] SPEAKER_00:** Very confusing. Yeah. And the C client, of course. The first time I think I saw your name, or was in contact with you, was about light clients. I'd been trying to get Ethereum ARM Linux cross-builds running on my smartwatch. My thought there was: get the thing running, and then this light client stuff is just starting and scaling will be solved, right? We're going to be able to run these nodes on anything. You'll have them on your phone, smartwatch, router, they'll be in every operating system. It will solve that scaling and that lightness. So you were plunged right into that problem, right?

**[26:38] SPEAKER_01:** Yeah. When Jeff hired me, he put me on this project. He just said, “Okay, it's great that you contributed to Swarm, but if you join the Geth team you will have to start working on the light client, because it's a very important thing and it hasn't been started yet.” So yeah, I felt really good about it. I also felt like this is a big thing. Back then it really felt like we do these few things, we have a working light client protocol, and the whole trinity of base layer, and then we're all good. It wasn't that easy, but still those were the first steps. So I designed the LES protocol. In retrospect, it didn't make a lot of sense to build it over the devp2p layer because it wasn't easy to access from web browsers. But also it was a proof-of-work-based light client. So yeah, that project ended after a while, but I'm still very much into trustless chain access. That has usually been one of my focuses all the time. Right now I'm also working on something called the Trustless Execution Layer API, which is similar to the Beacon REST API but works on the execution layer and provides everything with proofs. So yeah, I'm still very much into this because I think this is where Ethereum really makes sense: if even normal users access chain data with proofs.

**[28:36] SPEAKER_00:** Right, right. And there was a project called Portal as well. Were you involved with Portal? That was a later kind of light client.

**[28:44] SPEAKER_01:** No, I wasn't. Portal was Piper Merriam’s brainchild. By the time we kind of realized that LES was a nice first experiment, but maybe not the best approach, he started something different that was UDP-based and also used different topologies. It was kind of a DHT approach to storing the chain and the state. And yeah, actually I'm kind of—I think it's a bad thing that it’s been completely canceled, because to be honest, I never really believed that it will be an easily solvable problem to store the Merkle Patricia trie of the state on a DHT, but for the chain data it made perfect sense. So yeah, maybe the state would have been possible with a lot of work. But Piper told me a few times about how he imagines to solve all the unsolvable problems, and I felt like, yeah, it sounds good, but he just made a lot of really hard assumptions about DHTs. By that time I already worked on discv5—there was also this discovery protocol that we designed in 2016 in Berlin with Felix—and I released the original version. So I already knew that it's never so easy to imagine a DHT that's efficiently formed and all the nodes are working and yeah.

But for the chain data, especially with EIP-4444, which lets the mainnet protocol nodes forget the old chain history, it made perfect sense to at least put the chain history on a DHT. But yeah, it was an EF decision that it was discontinued at a point.

**[31:05] SPEAKER_00:** I guess the thing is, Merkle Patricia tries are not great for the number of accesses and things anyway, let alone if you're making each of those steps over a networked DHT kind of setup. That's—yeah, there's a lot of transactional change complexity.

**[31:31] SPEAKER_01:** State suffers from a lot of issues, especially in the Merkle Patricia state trie. And it's a huge data set that keeps changing all the time and keeps changing at completely random places, and it's not an easy task to distribute it. It's getting harder to even synchronize it between full nodes storing the entire stuff.

**[32:00] SPEAKER_00:** So do you think that proofs are going to be a magic silver bullet here, where by having local proofs versus massive really redundant state machines—do you think there's a path here where—

**[32:19] SPEAKER_01:** Oh, yeah—no, it's not a silver bullet. I assume you mean what people call statelessness. It's a good thing. It definitely allows a higher degree of scaling. But the state trie still has to be processed and maintained by someone, and especially if most of the nodes have no incentive to process it. And now we are talking about 100x and 1000x scaling. Then even if we also do state expiry—which is currently imagined in a way that we basically reset the state trie every year or something, and have multiple state tries—yeah, that helps somewhat. But if we scale 1000x then it will be a huge infrastructural centralization issue.

And by the way, this thing is not an unsolvable problem. I mean, the state as it works today unfortunately makes it really hard to do any fundamental improvements. But people are considering different storage architectures. Of course we have to keep the existing contracts workable because that was our main promise from the beginning: that we will not just shut down anything, everything has 100% uptime. But it is a viable way to come up with more efficient storage methods and use it as an opt-in alternative that will, over time, be available for much less, and new contracts can be designed using those more efficient storage architectures.

**[34:28] SPEAKER_00:** Yeah, because Verkle trees seemed to be the first sort of thought on that, but then that's kind of come and gone. And maybe it's a binary tree—

**[34:37] SPEAKER_01:** Or actually it does either.

**[34:40] SPEAKER_00:** You don't think it's so important either.

**[34:42] SPEAKER_01:** I mean, both are better than the Merkle Patricia trie in some ways, but they don't solve this fundamental issue by themselves. The thing is that the state is a permanent key-value store, and in order to avoid it growing forever, there are all these ideas about state expiry, but still it's going to be a huge data set. And the method of hashing or consensus protocol representation doesn't fundamentally change this.

Verkle was supposed to provide more efficient Merkle proofs, but also I guess somewhat more expensive state processing because it's more expensive cryptography. Also, if I'm correct, it's not quantum secure. And that was also a thing that I always felt like, yeah, I'm not sure if it's a good idea to start working from now, and I just saw it in front of my eyes how it's going to be canceled.

**[36:00] SPEAKER_00:** Yeah, yeah. I guess for running nodes in general, there's not a lot of incentive for people to run any kind of node software themselves unless they are a validator, or you're running an exchange or a business and you need your node backend to that. The vision at the start was, “Well yeah, everyone will be running their own node,” and you've got Mist on top of it and local apps, and then that can have Swarm for the smart contracts. It's almost like you won't have server architecture because everyone's running a server stack. And then, yeah—

**[36:46] SPEAKER_01:** That did not happen. That's why we are also stuck with the JSON-RPC API, which doesn't provide proofs, except for eth_getProof, but doesn't provide proofs for a lot of things because it was never meant to be used remotely. It was always imagined that it's used locally, in a trusted setup on your own machine.

I remember all those good old days when I just synced up a full node—it was a few gigabytes of disk space—and ran Mist on top of it. And yeah, it's magic, but unfortunately it didn't scale.

**[37:26] SPEAKER_00:** No. At the Museum of Ethereum here I've got laptops running geth 1.3.6, so Homestead Geth, and I mined Homestead back to life. Any hard fork that happens, the old one doesn't go away, right? It doesn't disappear. People just don't associate any economic value with it and it kind of gets abandoned. But what I've done is first GPU and then down to CPU mined that Homestead difficulty down to the level that you can CPU mine it again. So I have got Mist running on those. We can go and transact, we can send a transaction between those. And it should be possible to run AlethZero and AlethOne and Mist on that as well. I haven't had time to do that. And ERC-20 tokens existed—you could have DAO tokens or MistCoin at that time. But yeah, the assumption that people would run their own node and it would all be self-sovereign local apps certainly did not come to fruition.

**[38:54] SPEAKER_01:** Well, yeah. That's when the light client came in, and then we assumed that okay, then we do the light client and then it will be all solved.

**[39:01] SPEAKER_00:** But that's what I was thinking: right, I've got a full node running on my smartwatch, that works, and I'll just wait for you and the other guys to sort out light client and just turn that on and there we go.

**[39:15] SPEAKER_01:** Well, actually the light client protocol worked fine. I spent a really crazy amount of time figuring out how it could be decently incentivized in a truly decentralized way. Because I remember this idealism that now we are almost done with everything, so we just have to find a proper way for incentivizing things. But not in a way that there's a few companies where you can buy tokens—truly in a decentralized way, which is much harder. Then we have to somehow build decentralized trust and figure out market mechanisms that work without initial trust. This is something I spent years with. And honestly, I think I came up with some nice theoretical models and a lot of really complex code. But yeah, it was just, again, the wrong approach, maybe also at the wrong time. We were just not there, really.

**[40:27] SPEAKER_00:** Yeah, because BitTorrent has obviously worked for distributing content for many years. But then you do have this tragedy of the commons, right? The latest Hollywood movie—someone has ripped it off and people want that, so that's going to get shared around, no problem. But things which are only of interest to a smaller number of people, without incentives, it's just a leeching problem, right? Full node runners would contribute, they'd turn on LES as well, they would help supply that. But the incentives and economics of that—not easy.

**[41:14] SPEAKER_01:** Yeah. Actually with BitTorrent, if you really want to use it, it often requires trackers where you buy some priority access. So there are these private trackers and everything. So yeah, and this is also not completely decentralized, but actually it does work. It's definitely better than nothing.

But for LES it wasn't really this easy because downloading movies was an application that everyone understood, that everybody used. And with Ethereum it was always this—everyone felt the importance, but you’re nowhere near close to a really mature ecosystem. I don't think there would have been a big enough market for these services to really work out in a market-based way.

But as we scale and accessing the whole data set becomes more and more difficult, at a certain point I think we are going to have something like we imagined several years ago. It's just both timing and specifics. I was right about everything except timing and specifics.

**[42:46] SPEAKER_00:** Yes, yes. There are a number of things that seemed like they would be easy and quick and obvious and have taken so many years. Proof of stake—it was in the white paper. There was an assumption later in 2015 that it will happen within six months, maybe three to six months. And then it's eight years before it actually went live.

On storage: Filecoin, their first white paper was in 2014 as well. Filecoin was not a new thing. And IPFS was around before Ethereum as well. And then Whisper kind of went for a while, and now there's Waku. And you've had Status driving a lot of those techs for a lot of those years as well—Jarrad Hope and team—who were also doing Android versions of the Java client, same kind of time as I was looking at smartwatches. Jarrad Hope—

**[44:04] SPEAKER_01:** Was also very eagerly waiting for a fully functional light client.

**[44:10] SPEAKER_00:** Yeah, yeah, yeah. They were building kind of a decentralized “wework,” super app, but I guess kind of a competitor to Mist, really similar: wanting to have a container for running dapps, sitting on top of a local client, again having this completely self-sovereign server/app stack. But not easy.

I can't remember who it was that was telling me: when they first saw MetaMask—which was at Devcon 1, one of the grant winners—thinking, “No, that's not what we want. We don't want some browser extension thing talking to a trusted endpoint. That's absolutely the opposite. What are these guys doing?” And then that's become the standard flow, right?

**[45:15] SPEAKER_01:** Well, yeah. This is still kind of an unsolved problem: to access everything in a truly decentralized way. But I think we are getting there over time. It's just nothing is as simple as we initially imagined. And also there's a time for everything. Sometimes decentralized infrastructure will be forced by scaling. Things sometimes just don't happen if they are not forced by some circumstance, some external factor. So as long as it works in a lazy way to just connect MetaMask to Infura, until then it's the standard way.

**[46:12] SPEAKER_00:** Yeah, yeah. So I think I found two different talks of yours at Devcons talking really about light clients. Do you remember—did you talk in London, or was Shanghai your first?

**[46:26] SPEAKER_01:** No, I talked in London, also Shanghai, and also in Cancún. So those were the first few Devcons where I mostly talked about the light client. The first release of the light client protocol was in ’16, so it was around that time. Later I already started to invent all the next chapters of decentralized technology.

I also had this project back then where I started to try to make logs provable efficiently. The initial attempt for that was in 2017, and now I'm back at it. Now I also have this trustless log index project. This old approach in 2017 was just a more efficient way to organize the bloom filters, but it didn't really solve the problem of bloom filters not adapting to the number of events. And I never even proposed putting it into consensus, which would have allowed actual trustless proofs through the chain.

So yeah, that proved to be a hard problem, but this is one of the things I presented in Cancún.

And also some kind of my ideas of state channels. Back then we didn't have L2s in this way. So layer 2 just meant something that happens off-chain, not necessarily another blockchain. I had these ideas about individual nodes running their own blockchains, somehow organizing some off-chain calculations through that. But it also assumed a lot about how nodes would operate, and probably would have never worked in retrospect.

**[48:53] SPEAKER_00:** Yeah, I mean we had state channels, then we had Plasma, then eventually coming into optimistic rollups and then ZK later. Just many, many different attempts.

**[49:06] SPEAKER_01:** Hello.

**[49:07] SPEAKER_00:** See you, sir.

**[49:07] SPEAKER_01:** Great to see you.

**[49:10] SPEAKER_00:** So yeah, I mean, I guess there's an awful lot of learning, right? Ten years worth of lots of people trying lots of different things. In terms of the Geth team, has that been similar over the years, or have you had larger and smaller amounts of people? Has it been a similar kind of flow through that time?

**[49:36] SPEAKER_01:** I would say it was pretty consistently around 10 people throughout all these years—sometimes 8, 9, sometimes 11, 12—but really in this range. We did improve our internal processes during the years. Now we do have all this issue and pull request triage. But really the team was always small enough so that we didn't need a lot of processes.

Honestly, the team culture did obviously change, especially with certain people coming and going. But I would say it was always a good team culture. I always liked the Geth team. That's also why I never really looked into moving to other teams or other projects, because I felt that the team is the best place to do meaningful things.

**[50:56] SPEAKER_00:** Yeah, it's funny because from the very start of Ethereum, the intention was to have multiple clients, right? That was a very basic decision of saying we want a separation between the specification and the implementation, because we don't want it to be like Bitcoin where you've got one codebase and there's no competition.

**[51:20] SPEAKER_01:** Well, yeah. For Bitcoin's complexity that approach worked, but for Ethereum's complexity I would say this was one of the best decisions. It also contributed to almost running out of money by the time we launched Mainnet, but I would say it was money well wasted.

**[51:40] SPEAKER_00:** So yes, I would agree. It was not efficient, but the outcome was very much worthwhile.

**[51:48] SPEAKER_01:** Yeah. And when we switched to proof of stake, we again successfully applied this pattern by funding multiple CL implementations and then testing every EL against every CL, and then running testnets with all the five.

**[52:09] SPEAKER_00:** Is it five? Five different primary consensus clients? I think it's five. Notably none of those were within the Foundation either. They were all independent companies and teams.

So on the execution side there have been a good number of different alternative execution clients over the years: starting with Parity, and then Besu, and Nethermind, Erigon. How do you tend to work and interact in that kind of environment where you've got all these different teams?

**[52:53] SPEAKER_01:** Now we have all the ACD calls and testing calls. Mostly, we all do have working clients all the time, so by default we don't need to interact a lot. We have to interact when we are testing out new features. There are the prepared forums for that. Some people keep more contacts outside of the Geth team, some people turn inwards and focus on Geth issues.

In the first years, communication was really not organized well, so we really just tried to figure out things. Some people knew some people from the other teams. But these days we have much better processes for this.

Also it's a much bigger challenge because there are so many more people. This is also something I realized during the time we really started working on proof of stake. In 2017 was the first time ETH price went to several thousand dollars, and the Foundation had money to hire new teams and fund external teams. I remember that until 2017 I mostly met non-Go-Ethereum people mostly at Devcons.

**[54:37] SPEAKER_00:** Right. Yeah.

**[54:37] SPEAKER_01:** And maybe those people who lived in Berlin or one of those cities where there were multiple people, they met more people. But I was mainly in Hungary and worked remotely, and I mostly met most of the people at Devcons. But around, I think it was 2018, so many researchers were hired, and there were also the Seattle teams. I remember Devcon 4 in Prague. Until then it was mostly—I don’t know how many people exactly—but I do remember maybe 30, 40 people. After every Devcon we stood up at the main stage and did a group photo: “We are the Ethereum Foundation.” It was that many people. And in ’18 I was just shocked: who the hell are all these people? They’re all Ethereum Foundation. So yeah, it became a much bigger challenge. But also now we do have all these official forums, and I try to go to more events, not just Devcons, in order to keep all the context live.

**[56:00] SPEAKER_00:** Yeah, yeah. Looking back to when you first started working on Ethereum, did you have any kind of thought or vision of what things might have looked like 10 years later? Has it worked out as you expected, or differently? Looking back on these 10 years, what's your thought?

**[56:25] SPEAKER_01:** I always had a lot of visions. Maybe I was too focused on visions sometimes. The thing is that we all kind of have to imagine the future at every point, even though we know we can't imagine it as it will turn out. So it never turns out exactly the way we want, but we always have to have some kind of direction, and we have to have ideas of how things can turn out.

Around 2017 I also realized that scaling will not happen just with L1. I had these ideas about how we could solve problems more efficiently with not even rollups, just application-specific state channels and stuff like that.

But there was also this really great project—Raiden. They properly implemented the protocol and everything. I think it has always struggled with not many people using it. It's a pain that transactions are expensive, but still somehow maybe we just missed some organizing force to really move to some kind of layer 2 solutions, and it was just—

**[58:10] SPEAKER_00:** Yeah, well it was meant to be Lightning for Ethereum, right? That was the thought.

**[58:16] SPEAKER_01:** Well, yeah, it was pretty much that idea.

**[58:18] SPEAKER_00:** But then Lightning's kind of failed, so maybe not surprising if an Ethereum version of that's not really got—because you've got routing issues, right? Channels seem to work great for consistent static topographies. If you want to do merchant-to-merchant, channels work great.

**[58:46] SPEAKER_01:** Yeah. But opening those channels is still costly and non-trivial. I also never really—I installed it, I tried it, I thought okay, this is interesting, but I never really made a payment through Raiden because there was just no occasion where the other party really wanted a Raiden transfer.

**[59:14] SPEAKER_00:** No. Well, thank you very much. I think we can wrap it up there. Thanks for your time, and thanks for all of your work on Geth over these very many years. Geth has always really been the backbone of Ethereum. New clients come and go, but Geth remains. So thank you.

**[59:39] SPEAKER_01:** Thank you for having me here.

**[59:40] SPEAKER_00:** Thank you so much.