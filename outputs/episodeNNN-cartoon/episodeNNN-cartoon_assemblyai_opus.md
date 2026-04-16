**[00:05] SPEAKER_00:** Welcome to Early Days of Ethereum. I'm here today with Cartoon for a rather different kind of topic, an episode than normal because...

**[00:26] SPEAKER_01:** The Wait Days of Ethereum is what it's called. The Wait Days of Ethereum.

**[00:31] SPEAKER_00:** Right, from the late days. Normally I'm talking about sort of social history of OGs and their memories at the time and everything, but you have had a rather different focus of on-chain history.

**[00:52] SPEAKER_01:** Yeah, no, thanks for having me on the show. I've been, as you know, a very big fan of your work. And I am not, as you said, an early days of Ethereum person, but I think that this project that I think we'll talk about is in ways a celebratory adventure of the efforts of the folks who are worthy of this actual channel that you have. This really is an Ethereum effort. So yeah.

**[01:27] SPEAKER_00:** So how did you yourself sort of get involved with Ethereum and this on-chain thesis?

**[01:35] SPEAKER_01:** So my Ethereum story, honestly, it started through investing, like probably many others. It came on during the boom. I kind of ignored all of the early nudges and articles I read to the exciting technology of blockchain and where it could go. Everything was focused in 2010-2013 about how either you're in it, which was the view, or it's absurd and it's speculative and everyone's going to lose their money and they're gambling and whatnot. So I kind of jumped on that bandwagon, was interested, but on the side, never really dove in. And I was even at 2012, a co-worker of mine was mining Bitcoin in his aunt's closet.

**[02:38] SPEAKER_00:** Right.

**[02:39] SPEAKER_01:** And was telling me about it and was very adamant. I respected the guy, a good friend, and I respected him a lot. And so I guess I look back at that as like, what were you doing? Why didn't you just listen? But he was telling me, hey, you should keep an eye on Ethereum as well. And I didn't. I went to grad school during DEVCON 1. Actually, some of my... I was telling, I think I was telling Alex Van de Sande that one of my classmates spoke at DEVCON 1, which is really cool, but again, just didn't jump in. And then I didn't inevitably jump in until every 2021, I think, or 2020, late 2020 or something, when everything started popping off and I saw some absurd tickers on this app called StockTwits, which at the time I was kind of interested in over-the-counter stocks.

**[03:44] SPEAKER_00:** Was this sort of GameStop era?

**[03:47] SPEAKER_01:** It was around the GameStop era. Yeah, there were all these absurdities. The PancakeSwap era. Actually PigSwap or whatever, which was the platform where every absurd ticker at the time, like Butthole Coin or whatnot on...

**[04:02] SPEAKER_00:** I think it was Butt Dix.

**[04:04] SPEAKER_01:** Yeah, Butt Dix is all Binance chain.

**[04:07] SPEAKER_00:** Right.

**[04:08] SPEAKER_01:** And one of them, I saw these tickers go 5,000 whatever percent every, you know, whatever. It flashed at me and I was like, okay, I've got to try one of these. And so I got in, but that led me to, okay, what am I actually buying? And then I started to look into what, you know, when ERC-20 at that time was already established the standard and whatnot, of course. But so looked into that and Binance Smart Chain, or that's what it's called, it's just an emulation of Ethereum. And they just took the ERC-20 contract and repurposed it.

**[04:42] SPEAKER_00:** So BRC-20, is it BRC-20?

**[04:46] SPEAKER_01:** Yeah, it's ERC-20. I think you're right. Exactly. And then if you look up their dictionary, it says, this is just ERC-20. Yes, but the code is of course exactly the same.

**[04:56] SPEAKER_00:** TRC-20 on TRON.

**[04:59] SPEAKER_01:** Yeah, they're all just... Yeah, there's a 20 on it all. Which is funny because as we know, Fabian just made the pull request, the 24th request or something. But so anyway, yeah, that led me to contract development. I was interested in. Went from fungible tokens to non-fungible tokens and got mixed up into an NFT project. I became their software engineer, per se, or dev, as I came to find out. All the terms of rugging and devving and whatever. Everyone was a dev and is a dev. Sorry to all.

**[05:42] SPEAKER_00:** We're all devs.

**[05:43] SPEAKER_01:** Oh, sorry, all the devs.

**[05:44] SPEAKER_00:** With AI especially, we're all devs. Yeah.

**[05:46] SPEAKER_01:** Every single version of the dev. My parents are devs. They're all devs. But it was funny to me at the time. I was struggling to sort of keep track of all the vernacular and take anything seriously. Especially everything was on Twitter Spaces at the time.

**[06:05] SPEAKER_00:** Right.

**[06:06] SPEAKER_01:** Everyone was establishing their voice on Twitter Spaces so that the word rug was probably said like five... There's Rug Radio which may not exist anymore.

**[06:16] SPEAKER_00:** Wrecked, R-A-K-T, ever was...

**[06:19] SPEAKER_01:** My version of wrecked. Yeah, I just got wrecked.

**[06:21] SPEAKER_00:** Yeah.

**[06:24] SPEAKER_01:** So I became this NFT's developer and I was developing all these different smart contracts. There wasn't... I found a lot of creativity. It was sort of everything was a bit of a copy of what somebody else had done in this space and they were trying to push it.

**[06:40] SPEAKER_00:** This is for security because they're well audited, you see. So risk management strategy.

**[06:47] SPEAKER_01:** Yeah, there's no AI to check so you just would copy somebody else's. And whether that meant copying already malicious code that was implemented or not. It was funny that actually one of the contracts... So this NFT project that brought me in and wanted me to help with development, their first contract they hired a Fiverr developer. And it turned out after we did the second contract and mutations and whatnot, it turned out that the original contract which they hired this Fiverr person to do, they had overridden... they had rewrote the owner function such that... the inherited function, they could actually jump in and take over any time. They could pull the money that was in the contract, but it was hidden enough because it was on the inherited contract class, not the main one, that they didn't see. And I don't think anybody there was technical enough to even vet the contract, let alone that.

**[07:56] SPEAKER_00:** Well, it happened to Parity back in the day with a bunch of experts. So if you're just winging it...

**[08:02] SPEAKER_01:** 100%. I mean, in my mind, because you were saying you copy these for security as a joke. I think that in my head at the time I was like, okay, there's this Fiverr game that's out there just telling everybody to deploy these contracts and then they're sharing the funds or something. But it very well might have just been somebody copy-pasted that from some GitHub repo. They weren't the scammer. They didn't even know they were.

**[08:29] SPEAKER_00:** They were just an infection vector for scams.

**[08:32] SPEAKER_01:** Exactly. The dev, the head dev at the time, asked me, he said, so what are the chances that we're going to get scammed here or whatnot? I was like, well, take the funds out of this contract. It doesn't seem like they can do anything, but there's other funds in there. In theory this person could come in at any time. Do they know about the fact that they have edited this function in a way? Maybe not. So maybe they just copied it from someone else. And ultimately they were forced their hand because OpenSea actually maybe flagged them. Maybe somebody flagged it for them or something, and I had to then do a migration contract for them and stuff.

But all this development sort of was the seed of the interest for me. And then what led to Ethereum history was a few years later, probably in like 2024 or something for me. So pretty recently, or maybe 2023. Anyway, MistCoin popped up online. And so this was actually post... There's this relics group, this folks group of Discord friends that focus their time on collecting NFTs, old NFTs and old contracts on not just Ethereum, but Ethereum too like...

**[10:02] SPEAKER_00:** Solana.

**[10:03] SPEAKER_01:** No, no, no, the Bitcoin one starts with C. They talk about... I don't... The one that was kind of like...

**[10:10] SPEAKER_00:** Oh, inscriptions and ordinals.

**[10:16] SPEAKER_01:** Not ordinals, before. So before runes.

**[10:19] SPEAKER_00:** No, oh, Counterparty, super old.

**[10:23] SPEAKER_01:** And some of them don't like Counterparty NFTs or NFTs because they're not really... It's all built. It only exists if you have this other...

**[10:34] SPEAKER_00:** Protocol client.

**[10:35] SPEAKER_01:** Right. So there's a debate and whatnot, but everybody collects, they basically collect these old things. And anyway, they reached out, they found MistCoin and they're digging old contracts and...

**[10:50] SPEAKER_00:** So MistCoin was made like as an example token for the Mist wallet. Right?

**[11:00] SPEAKER_01:** Exactly. Yeah. So MistCoin was made by Alex Van de Sande and Fabian Vogelsteller, who you know well, and you've interviewed. Fabian deployed it. But essentially they were at the time, my understanding, they were developing a feature for the Mist wallet, the Ethereum wallet.

**[11:20] SPEAKER_00:** Right.

**[11:22] SPEAKER_01:** To allow for anybody to deploy contracts. And so at the time...

**[11:26] SPEAKER_00:** Before then, deploy your own coin.

**[11:28] SPEAKER_01:** Yeah. Click this button. And within the feature there were templates. Right. So it was kind of like the first standard in a way. And at the time, the standard itself was being molded from before in the standardized repos. But this was the current state of sort of that morphed standard code.

**[11:52] SPEAKER_00:** Yeah. And that was still pre...

**[11:55] SPEAKER_01:** ERC-20 actually happening. Exactly pre that. Whether it was the 20th commit or the 20th pull request, I'm not sure. We have to ask, or check.

**[12:09] SPEAKER_00:** It's funny actually. The way that works is issues and pull requests are from that same ordinality. So it doesn't mean it was the 20th pull request. It was the 20th issue or pull request that had been created. So yeah, it can be either because they never have the same numbering because that would be ambiguous. So it's the 20th time somebody either made a PR or issue or put...

**[12:47] SPEAKER_01:** In any issue whatsoever.

**[12:49] SPEAKER_00:** Right. Anyone could just chuck any issue in and it counts. So a number of the... So a good number of the numbers never end up on anything. Right. They never like land on a thing.

**[13:06] SPEAKER_01:** An issue that says, hey, I don't really like the color red.

**[13:09] SPEAKER_00:** Right. So like if you look at EIPs now, they're in the thousands and it's not like there've been a thousand proposed protocol changes.

**[13:20] SPEAKER_01:** Seeds.

**[13:20] SPEAKER_00:** Okay, sure.

**[13:22] SPEAKER_01:** That's an interesting way of doing it. So yeah, so EIP-20. So this was November 3rd was when they deployed that feature and MistCoin being the first one that they launched with it. Then DEVCON 1, they talked about it a little bit.

**[13:40] SPEAKER_00:** Standards panels.

**[13:42] SPEAKER_01:** Standards panel. Simon.

**[13:46] SPEAKER_00:** Simon de la Rouviere.

**[13:47] SPEAKER_01:** De la Rouviere spoke about token standards itself. He was also one of the few who were sort of helping mold this standard. And then a few days later, so the 19th, I think, or so the 19th of November is when Fabian and Vitalik sort of formalized this proposal.

**[14:10] SPEAKER_00:** Right.

**[14:11] SPEAKER_01:** Of a slight adaptation, change of the code of MistCoin. But really this standard that they had been molding. And it was funny, recently I found this Ethereum history digging, this digging of old contracts, a coin that Vitalik had deployed. And it wasn't immediately clear that it was a token, because you have to really look through the bytecode itself. And it didn't really, when you... since it was written in Serpent, it didn't...

**[14:44] SPEAKER_00:** Oh, right, yeah, yeah, yeah.

**[14:45] SPEAKER_01:** If you tried to decompile it with the decompiler on Etherscan, it didn't really work well. And so you can't really tell on the surface anyway. If you look through the bytecode though itself and you're just raw looking at and analyzing it, which is much easier to do now with AI, you could tell it's a token.

**[15:04] SPEAKER_00:** Right.

**[15:05] SPEAKER_01:** And it turned out it's actually this currency that he had deployed in the Dapp Bin repo in September or earlier, maybe September 8th or something. I don't know. But...

**[15:18] SPEAKER_00:** Right.

**[15:18] SPEAKER_01:** But what I thought was interesting, after I had sort of found the exact Serpent code and proven that, hey, it compiles with this version of Serpent to this exact bytecode, and I posted about it, Vitalik actually commented on it as well on Reddit and he didn't answer this question. So if he hears this, hopefully he responds. But my what I was wondering is, so he deployed this days before, I think it was maybe November 6th, but days before he went and published, co-published this proposal, the standard. And it's sort of his old... It's what he would have wanted as a token if you want. I don't know what... It is his proposal, early proposal in a way. And I wonder if that was his sort of way of immortalizing, hey, I like this thing. We ended up going with... I'm going to immortalize mine on chain. I like my way better type of thing. So that's how I like to imagine it. But it's there, and one day maybe Vitalik will decide, hey, everybody should have my unnamed coin. And there's a million of them and hand it off, and they're at zero decimals.

**[16:34] SPEAKER_00:** That's pretty random, what people ended up pushing or not pushing, and it's all...

**[16:41] SPEAKER_01:** Yeah, but there's only one. So I mean, I guess Vitalik doesn't make many mistakes and he probably even was using testnets or whatnot back then. But a lot of folks were testing...

**[16:51] SPEAKER_00:** In production. Like, there was no economic value even, so right, right, why would...

**[16:58] SPEAKER_01:** You not? Trading at cents to a dollar at that point. So yeah, it was... Now you look back at it and you're like, oh yeah, I spent 10 ETH on... But a lot of the contracts now that I... So for Ethereum History, I'm sure they...

**[17:20] SPEAKER_00:** Introduce... Well, just before we get to that. So you spoke about MistCoin as sort of being where you started. So is that wrapped now? Is it wrapped? MistCoin. Was that... because it was slightly pre-ERC-20, does this coin need wrapping?

**[17:40] SPEAKER_01:** It needed wrapping. It doesn't have an approve function. It doesn't have a few other functions. It's one of the first named tokens that way. It's kind of special. And it doesn't adhere to the current standards such that if you tried to create a Uniswap pool for it, it wouldn't work. There's no approved from methods that it needs or transfer from and approve order...

**[18:15] SPEAKER_00:** Yeah, it's just... it's not going to move.

**[18:17] SPEAKER_01:** It's not going to move. So essentially, if you wanted to make it tradable, which at the time... So this group, this relics group had found it. They found a MistCoin DAO that Alex had made and this MistCoin. And once they acquired some of the MistCoin, they were given, I think, from both Alex and Hudson, if I'm not mistaken.

**[18:41] SPEAKER_00:** Right, right.

**[18:43] SPEAKER_01:** They then were able to also pull more MistCoin from this DAO. So I think Alex had put in 100,000 MistCoin, which is like 10% of the entire supply, into this DAO. So they took that out, and then they used it. They just gave it out to a lot of folks in their community of early entities. They kind of framed it as, hey, this is going to help early NFTs and we're just going to help boost our community. And they were into that. And so there is now a DAO that holds, I think, like maybe 4% of the supply, or 40,000.

**[19:25] SPEAKER_00:** Right, right.

**[19:26] SPEAKER_01:** And the rest was kind of given out to all their folks. And so when I bought it, I was a sucker. I bought it at like $50 or something. I was like, cool, I can own this thing like everybody else. By the time my timeline, it reached my time when it's too late.

**[19:44] SPEAKER_00:** Right.

**[19:44] SPEAKER_01:** Lesson for everybody. But, or at least at the time when everything was popping off. But yeah, so they probably did very well. But they're also, besides that, they are this group which I can't say I'm seriously part of, but they very much care for these older relics, specifically non-fungible tokens. So they're very much into that, which is cool collectors.

But that's... So MistCoin led me into this early interest in early contracts. And once I started to dive into the story of MistCoin itself, and what Fabian and Alex were doing at the time, and how it was the beginning of basically everything that moves Ethereum today, everything that people are interested in from an external perspective, from the tokenization of finance and whatnot. It all stems from the need for there to be a standard. And all that just sort of like, okay, that understanding that importance led me to say, okay, well what else is out there? What else was happening at the time then?

**[21:02] SPEAKER_00:** Right.

**[21:04] SPEAKER_01:** That is either interesting today or will be interesting later. And can we sort of uncover that now? And so while I was writing this, writing a website for MistCoin and helping with any sort of engineering projects that we needed to sort of tell that story, on the side I started to download all of the contracts on 2015 and then 2016 and perused through the bytecode before AI and all these LLMs were out there. So I was really just using decompilers, like Python decompilers, and I was running similarity text algorithms to try to figure out, okay, what is the likelihood of this being a token or this being an ownable, or this being fungible, or this being something. I'd look at deployer addresses, known deployer addresses, type of thing. But it was a much more difficult assessment than it is now.

**[22:15] SPEAKER_00:** It's almost like a reverse engineering kind of discipline. You've got this... it has been a lossy thing, right. That compilation process, it's not intrinsically reversible. You've got that data loss and you've got these patterns, but no blockchains ever die. Caveats compiled.

**[22:42] SPEAKER_01:** Exactly. Yeah. It would be really great if it was possible to make Ethereum in a way that you could actually just store all the code itself and not have to do the bytecode, of course. Not feasible.

**[22:58] SPEAKER_00:** I'll tell you a funny little thing actually. STRATO, that I'm working on, that actually does happen for our chain because it has an alternate VM called SolidVM, which is an EVM as well, but it's actually an interpreter.

**[23:18] SPEAKER_01:** So...

**[23:19] SPEAKER_00:** So what you have is you do have source code on chain which gets deterministically interpreted. So it's almost like you've kind of got Etherscan built in, kind of thing.

**[23:32] SPEAKER_01:** And you don't have any issues with having to transmit large chunks of data through consensus?

**[23:40] SPEAKER_00:** No, it's been okay. I mean, yeah, you wouldn't... couldn't do that at huge scale. You couldn't do that at huge scale in a completely permissionless validator scenario.

**[23:54] SPEAKER_01:** But it's still interesting to work.

**[23:57] SPEAKER_00:** There's an alternate universe.

**[24:01] SPEAKER_01:** Different things have been chosen to explore that. Yeah, because, like you said, it's been a challenge I didn't even really attempt. There were a few attempts. There's this person who has helped, has done a lot of work in trying to exactly prove the MistCoin code and eventually did through the help of a couple of others. But it's a guessing game. At a certain point you're trying to guess the order of functions, the functions themselves, the method names. And you get to a point where you get close, but so many things could go wrong. There's so many possible permutations, there's the compiler version, there's the settings, there's the order, the naming of the functions. In some cases even now with LLMs, it's made it impossible because in one contract, for example, I'm down to just this one function name and I know that it is more than 10 characters long because I've tried every possible 8, 7, 8, 9. So I literally had this machine running on my computer just chugging through everybody, and it's not... At first it wasn't even doing anything intelligent. It was literally going A-A-B. So actually you can't do that once you get to the higher character counts. It would take forever.

But I just gave up because what's the point? I mean, you know what the function does. And so you'll see on Ethereum History some say "near exact bytecode" and I'll actually indicate how close it was because I'd give up at a certain point.

**[25:53] SPEAKER_00:** Because as long as you have...

**[25:56] SPEAKER_01:** The exact functionality, and you're pretty close to complete, the bytecode's off by a few segments, then what would matter?

**[26:07] SPEAKER_00:** I mean, I guess there's probably a decent amount of the source code that's probably on GitHub somewhere.

**[26:14] SPEAKER_01:** That's another tactic. So yeah, when I'm doing this sort of what I've called cracking, and there's an Ethereum History cracking skill and whatnot out there. But one of the approaches is researching, so just going off the Reddit and to GitHub and trying to find the contracts or contracts that are similar. Even back then, folks were doing... somebody would do something and another person would make a slight adaptation to it, whether that's naming this function something slightly different. And now I can't guess it. But in this case, literally everything else was, like you said, published somewhere.

**[26:55] SPEAKER_00:** Yeah, somewhere. Somewhere when somebody said...

**[26:59] SPEAKER_01:** Yes, but you find it through keyword searches on GitHub and stuff that shows up.

**[27:04] SPEAKER_00:** Right, right. Yeah, yeah, yeah.

**[27:07] SPEAKER_01:** It's definitely a great tactic. And it shows, you can document everything on Ethereum History, but still it's great to know that they're fragmented out there. As long as the Internet is around, there are at least other folks documenting in time, thanks to the Internet Archive. Even some things that have been removed are still out there.

And one of the things I was pretty disappointed about, and maybe they'll bring it back one day, is Ethereum took down last year or two years ago the standards, the standardization requirements repository. So it's literally this one GitHub repository that they just kept track, this wiki, they kept track of all of the different standard commits as that progressed for tokens.

**[27:59] SPEAKER_00:** So this was a wiki within a given GitHub, Ethereum something.

**[28:05] SPEAKER_01:** Yeah. And so a lot of the commits are still there on Internet Archive and some folks had forked it at different junctures, so you can kind of find it at different stages.

**[28:16] SPEAKER_00:** Right, right.

**[28:17] SPEAKER_01:** But I don't know what's the purpose of taking it down? I mean, I think they probably had some reason. Maybe they didn't want to add confusion or something. But yeah, it's...

**[28:29] SPEAKER_00:** Or sometimes it can just be like in complete ignorance of the consequences, that it's just somebody cleaning up.

**[28:35] SPEAKER_01:** Right.

**[28:36] SPEAKER_00:** Or whatever.

**[28:38] SPEAKER_01:** Yeah. So I mean, I would imagine hopefully that somebody at Ethereum has that, as they sort of downloaded the repo over time and can stitch it back together.

**[28:49] SPEAKER_00:** So for history of the white paper, so Postrolar has done a lot of digging into those details, but it was only through him I realized that you had got some of those Internet Archive versions of the old wikis. I thought they were like all way beyond, like a very long time ago.

**[29:14] SPEAKER_01:** Yeah.

**[29:15] SPEAKER_00:** So it was kind of fun that those are still on the Internet Archive.

**[29:19] SPEAKER_01:** Another, and you probably remember this, but another thing I found on the Internet Archive is around that time, like 2015, there was a bulletin that was kept up by somebody in Ethereum.

**[29:32] SPEAKER_00:** Okay.

**[29:32] SPEAKER_01:** It was basically a forum where you can ask questions, but it was all seemingly self-hosted.

**[29:41] SPEAKER_00:** Oh, just the Ethereum forum.

**[29:43] SPEAKER_01:** I think it was the Ethereum forum. And yeah, there was... people were talking and it had its own message threads.

**[29:49] SPEAKER_00:** Yeah, yeah. So that was a Discourse. I think it's Discourse, the software is. But yeah, that wasn't used for very long. Like Reddit became a lot more popular. But then I remember there was a whole bunch of drama about, oh, we're going to shut the forum down, are we not? And then it was like, oh, well, okay, maybe somebody in the community wants to maintain it. Yeah. But then it's like, oh, but you can't because you'd be giving over the database that would have all the DMs in it and it'll be like... So I think Hudson kept maintaining it for quite a while.

**[30:30] SPEAKER_01:** I don't know if it did ultimately because, yeah, I mean, it would be interesting. There was definitely at least one contract that through the Internet Archive, I could see that I was about to get some important information on it and then it just, next, gone. So... but yeah, some of these ventures into trying to document some of these contracts go quite deep into these Internet archives and they're not easy to browse through. But you get into those old things that have been taken away and it kind of feels exciting because it kind of feels like you're digging into something that nobody knows anymore.

**[31:16] SPEAKER_00:** Yeah.

**[31:17] SPEAKER_01:** And that's what's kind of kept me going. That, and it seems like people are genuinely excited. I don't know. It's a small group and obviously I only have sort of Reddit and those folks who are still on Twitter to sort of speak to this. I wish there were other avenues, but there is a decent community of folks that still reminisce and still want to know about it. And they'll look at the history and the first programmable blockchain, what the early days were like, and not just from people's perspective, but like the actual contracting.

**[31:58] SPEAKER_00:** So your site is ethereumhistory.com. So what features are there? What can people see if they visit that?

**[32:09] SPEAKER_01:** So the way my short elevator pitch is: Wikipedia of Ethereum smart contracts. So the idea is Etherscan itself is great. Etherscan tells you all the facts about every contract that they can find on chain, and you can see, of course, the bytecode. You can see the code if they verified it or not. But there's very hard restrictions on how you can verify it.

**[32:38] SPEAKER_00:** Right.

**[32:39] SPEAKER_01:** And they only support up to a certain 0.4.3 or something version of Solidity.

**[32:48] SPEAKER_00:** Right. So like probably the version when they started. Probably.

**[32:52] SPEAKER_01:** Yeah, yeah. You can't go further back. So anything early you can't really verify. But beyond that, actually adding any descriptions or anything or any tags or anything is very difficult. Go looking at Etherscan. So it's really not meant to add any meaningful documentation to a contract. It's really just there to say this thing exists.

And outside of that, there's not either... there's nothing popular or nothing I could find that has any sort of purpose of recording the history like a Wikipedia would. Of course, there's some projects that have gotten to the point of which there is a Wikipedia page, like for that.

**[33:30] SPEAKER_00:** Yes.

**[33:31] SPEAKER_01:** And it will probably say link to Etherscan or link to show their contract address, maybe. Which probably not meaningless, that people really probably just paste that website. Yeah. So basically, where's the home for this Wikipedia? Where's the home for folks who are interested in Ethereum to learn about those early contracts, learn about the story behind them, and look at the original code itself? Not look at the bytecode, but let's look at the actual code.

And I think there's two different things that people can take out of that. One is, if you're interested in the stories, you can go back and see the qualitative stories. They're not always going to be accurate because every story, right, is a sort of picture of what somebody remembers and tells one other person. And your memories are of course just fickle and perhaps might not be exactly right. But hopefully, with the idea of Wikipedia, everybody sort of edits it over time and it becomes... so hive mind's going to be perfect. It's very efficient.

So anyway, right now Ethereum History is not exactly efficient because there are 18 different historians, of which the users are called historians, but of which four have documented contracts.

**[35:02] SPEAKER_00:** Right. So, a slow takeoff. After...

**[35:05] SPEAKER_01:** Everybody watches this video, it's... everyone sign up. It's free. But so one thing you can take away is the stories. And then the other thing that you can take away is actually reading the code of all these early contracts.

And the vision I have there is, once we do get the code, I want to find the code of every, or most of these contracts, which we're making pretty strong headway right now. I want to find a way to represent that in visual, some sort of visual. In my head, I don't know how this is going to work out, but I picture sort of archaeology, like rocks, the way that sort of you can look through the layers of the earth and history through...

**[35:51] SPEAKER_00:** Right.

**[35:52] SPEAKER_01:** Some sort of visual representation of that, but through code functions or methods or... I don't really know. It's kind of a loose thought in my mind, but I would love to use something...

**[36:03] SPEAKER_00:** With a scrubby timeline somehow that changes shape somehow.

**[36:09] SPEAKER_01:** Yeah, I'm interested. What sort of stories... what can we learn about the reuse of different types of methods and how they... and then maybe the popularity of the contract itself, the amounts that it's been... which you could discern by the number of times it's been replicated or the number of transactions that have occurred. So the popularity, and then how long that has lasted over time. And what that is, like species coming...

**[36:40] SPEAKER_00:** To life and dying off and...

**[36:43] SPEAKER_01:** Yeah, exactly.

**[36:45] SPEAKER_00:** Look at that dinosaur technique. That literally is a dinosaur technique that's not used anymore.

**[36:51] SPEAKER_01:** And it's a hard thing too. It's a hard thing to keep track of because a method has a purpose and it has a name, but it's meant to do something. It might do several things. It might be part of a larger set of goals of functions that are calling it and whatnot. But if you're trying to find a thread through history, you might want to look at... you're dealing with a semantics problem as well because it's kind of like, it doesn't have to be the exact method, but that same purpose, and has it...

**[37:24] SPEAKER_00:** Yeah.

**[37:24] SPEAKER_01:** Gotten hardened or worse or better over...

**[37:27] SPEAKER_00:** You're sort of wanting to infer design patterns out of it or something, or higher level patterns or reasoning or...

**[37:40] SPEAKER_01:** Yeah, yeah, yeah. Hopefully that's possible. And it's sort of a loose thought in my mind. I don't know. We'll see what people want to build. It's an open source project, so open. Hopefully folks will add their own pull requests, that sort of thing, or issues. And I'll mark them as proposals, EHIPs, regardless of whether it's an issue or a... Ronnie's EHIP 1 if anybody wants. There haven't been a lot of pull requests since I'm just going straight to...

**[38:16] SPEAKER_00:** Right. Just straight to commit. We're going.

**[38:20] SPEAKER_01:** But that... Yeah, that's the code. And the stories are kind of the one angle. And the other angle I have... So I got into this downloading all of the 2015-2017 contracts, decompiling them all right, loading them up into this database. And then on top of it I've added these indices on this database such that you can query through all of the decompiled code. And the goal there was anybody should be able to find interesting things through the code. Maybe somebody's interested in mining, or they're looking for the first time that the word "cat" was written somewhere. The decomposition won't be perfect. It might not have the actual first cat, but there's a chance that it does. And this gives them the ability to search through text rather than just bytecode.

So that was the first idea. Now what happens is every single time a contract is cracked, as I call it, to solve the exact code with compiling settings, that gets added to the index as well. So you actually search through that code. It sort of improves that discoverability.

**[39:35] SPEAKER_00:** So what kind of different existing tools have you been using or found useful for the...

**[39:41] SPEAKER_01:** For cracking and for researching?

**[39:44] SPEAKER_00:** Yeah, and disassembling.

**[39:47] SPEAKER_01:** So the disassembling has been interesting, the whole cracking thing. So it depends on the contract. The first thing I'll do... and of course, all of this, heavy usage of AI here. Yeah, yeah. My AI overlord is helping me out every day. But the first thing I'll have to do is just go through and see, hey, through my... I have this Ethereum History researcher skill that just goes through GitHub, Reddit and tries to find... First, it will decompile it and or use the decompiled code I have already and try to find anything that resembles it in GitHub or Reddit at the time. And if it finds a match or it knows of some match, it obviously has its inherent knowledge already, at the time these things were out there or published, then it will start there. So it's mostly about finding a starting point, if not the exact code. Sometimes it is the exact. Sometimes it's a very reused wallet of the time or whatnot or something.

**[40:50] SPEAKER_00:** Yeah.

**[40:52] SPEAKER_01:** So it's establishing a starting point, and then from there it's taking the different versions of Solidity at the time. Or it will try to... is it Serpent, or is it LLL or whatever?

**[41:07] SPEAKER_00:** It might have some Mutan.

**[41:09] SPEAKER_01:** I haven't found it.

**[41:10] SPEAKER_00:** No Mutan, not yet.

**[41:12] SPEAKER_01:** Only, honestly, so far, only Serpent, Solidity, of course. And then in some cases, this is straight bytecode. I think that they deployed, so they, as far as the AI could discern, there wasn't actually any code, that they just created the bytecode themselves and launched that.

**[41:39] SPEAKER_00:** Strange, because I thought you always had LLL in the line, or maybe this was only for Solidity. So I think for Solidity, it was always built on top of LLL at the start, like kind of using LLL as an assembler. But yeah, I mean, Jeff was working on Mutan up almost until launch, so it might be that there's hardly any Mutan on mainnet. Like probably a bunch of that on Olympic. But then...

**[42:19] SPEAKER_01:** I hope I find something. That would be interesting. Yeah. For the ones that it discerned were all done in straight bytecode, used Yul, I think, or something. It's something somewhat recent, like 2018.

**[42:40] SPEAKER_00:** Though, who was it I was talking... was it... Oh, that was... Yeah, I did an interview with Alex Beregszaszi, so Axic, who was Solidity co-lead for many, many years. So he was saying that started... it was called Julia at first. Like Julia. Yeah, but with a J, I think. But then there's some other computer language called Julia already. So then that changed into Yul, which is a kind of intermediate representation, in that the goal was that Solidity would compile to Yul and then you would have a further compilation step on the back of that.

**[43:42] SPEAKER_01:** Interesting.

**[43:42] SPEAKER_00:** Well, hopefully. So I guess it kind of ended up being sort of like a bit like an assembler kind of.

**[43:51] SPEAKER_01:** Hopefully they're proud to know that AI is still referring to their work because for those few contracts that did choose to represent them in... Right, there you go. Cool.

Yeah, so that's there. And so this part of it is research, part of it is getting a sort of narrowing, chipping down, if you will, to this bytecode. And in the process, of course, it takes sort of the time at which this was deployed. So the different versions of Solidity that were out there at the time. And you just try to... it's a trial and error type of thing on both sides.

**[44:36] SPEAKER_00:** There's no metadata that ends up of the Solidity version in the final bytecode?

**[44:43] SPEAKER_01:** I think, correct me if I'm wrong, I think metadata started a bit later. There was a particular version of Solidity that... Yeah. And I want to say that because that became a thing. So the person who leads Sourcify, right, reached out and has been really great. He's been helping. He expanded Sourcify such that it could go down to much earlier versions of Solidity. So I've been verifying on Sourcify and also adding all the methods that we uncover so that they're there for the world to sort of...

**[45:25] SPEAKER_00:** And what does Sourcify do exactly?

**[45:28] SPEAKER_01:** I'm going to butcher this, but sorry. But they seem to be the registry of not just methods that have ever been deployed on the blockchain. So a way to sort of collect all that knowledge and make it accessible to everybody, but also to verify the actual source code of any particular contract.

**[45:57] SPEAKER_00:** Right.

**[45:58] SPEAKER_01:** So it seemed to be something that you would do going forward for a lot of time, if I understood it correctly. But then they started to also go backwards, allowing...

**[46:07] SPEAKER_00:** So kind of like taking that functionality that you had within Etherscan, but pull that out into a component that can be used.

**[46:19] SPEAKER_01:** Exactly. Yeah. Maybe the idea was, why, maybe Etherscan would want to just replace it with Sourcify. But yeah, I've pinged Etherscan a few times, especially as I started to validate or crack a bunch of these earlier contracts that I could not verify. Essentially the way that you would verify on Etherscan for these older contracts is you would reach out to support at Etherscan.

**[46:48] SPEAKER_00:** Right?

**[46:50] SPEAKER_01:** Yeah, respond. And for MistCoin, we had to go through somebody who knew somebody who was there, and they eventually... that person reached back and said, we're going to help you get this verified. But I cold emailed a bunch of these and they're really interesting. I mean, they still haven't validated, for example, Gav... GavCoin.

**[47:09] SPEAKER_00:** Right.

**[47:11] SPEAKER_01:** Vitalik's currency. These are like arguably very interesting and novel contracts from arguably very important people in the space. And they still haven't. So I got this sort of blanket response that was, thank you, but you need to be the deployer. Would you... are you the deployer? Would you like to...

**[47:37] SPEAKER_00:** Sign this transaction?

**[47:39] SPEAKER_01:** I was like, sorry, I'm not VB, I cannot sign it. But they ended up... somebody did reach out on Twitter and said, hey, yes, sorry about that. That's our blanket response. And here, we actually helped verify one. And it was one of these Peperium. Peperium is like, I think, for 2017 or so, an NFT-like contract. Like, I think it's more of a fungible-like token, but in some way that they added metadata onto it such that there's like an image.

**[48:21] SPEAKER_00:** This is not Piper Merriam.

**[48:24] SPEAKER_01:** No, no, it's not Piper. That would be hilarious if this was Piper. It should be.

**[48:33] SPEAKER_00:** Right?

**[48:33] SPEAKER_01:** Yeah, never. They roll off the tongue the same way. Peperium. I think it's more about Pepe. Every one of them, I think, has some sort of picture of Pepe.

**[48:45] SPEAKER_00:** Right.

**[48:46] SPEAKER_01:** But anyway, so the Etherscan person verified that one out of all the ones that I sent, and I was like, verify one of the ones I care about. Verify one of the top ones. I don't want to say I care one way or another. I'm sure a lot of people care about...

**[49:06] SPEAKER_00:** So Gav must have deployed GavCoin onto Olympic and onto Frontier then, separately.

**[49:12] SPEAKER_01:** Oh, I'm sure. I'm sure he did on Olympic. Must have, because... for fun. Right?

**[49:18] SPEAKER_00:** Well, because there was the talk I found, which was August 2014, I think, with Jeff in London doing the DEX, demonstrating that their DEX. That's right, that's it. Gav's saying he values GavCoin...

**[49:48] SPEAKER_01:** Which... I have yet to find JeffCoin, so.

**[49:51] SPEAKER_00:** No, well, maybe JeffCoin only ever made it out onto Olympic. There in Utah and Gav was... Gav was running LLL.

**[50:06] SPEAKER_01:** Yeah. So I can't prove that GavCoin, the one I found, was deployed by Gavin himself.

**[50:13] SPEAKER_00:** Right.

**[50:14] SPEAKER_01:** But I have a chain of information, a thread of different events that seem to have a strong case. Maybe Gavin will listen to this and decide to tell the whole world that it was deployed by him.

**[50:33] SPEAKER_00:** Probably forgotten all such things many years ago.

**[50:36] SPEAKER_01:** There's another theory I have where it could have been potentially deployed by that Roman, the person who ran that... by the...

**[50:47] SPEAKER_00:** Which was Ether.Camp.

**[50:49] SPEAKER_01:** I wasn't around, so I don't really know. I mean, I know Piper, I think, did some work with Ether.Camp at the time, and I believe... So I don't really know that for sure, but those are things I read. So Gold... Yeah, exactly. Oh, so that's why I think it might be potentially deployed by him, because I think that the deployer might have also deployed Hacker Gold.

**[51:15] SPEAKER_00:** Right.

**[51:16] SPEAKER_01:** So could that have been Gavin? I think it's possible. No. So then...

**[51:20] SPEAKER_00:** No, if it was Hacker Gold, that would have been Roman. Yeah, for sure.

**[51:24] SPEAKER_01:** So then maybe this was Roman. Yeah, I don't know. I have to look. I forget now. It's been a long time of looking at other contracts. Follow the deployer thread. But some... I found some connection to Hacker Gold as well. So maybe Roman wants to tell the world about... I don't know if anybody talks to Roman anymore.

**[51:45] SPEAKER_00:** I used to be Facebook friends with him, but then he seems to have gone off that as well. But yeah, he basically disappeared in 2017. Really.

**[51:55] SPEAKER_01:** But he was around, iconic himself. As I understand, some of the firsts might have been from him.

**[52:03] SPEAKER_00:** He's quite a character. One of the things that Ether.Camp did, which is unbelievable at the time, let alone now, is they at DEVCON 2 in Shanghai. So October 2016, this was... they did this demo called Cash F with Banco Santander and it was basically a stablecoin on Ethereum in browser. So it was sort of like you got some kind of MetaMask-y thing for doing like sending stables in a browser on Ethereum. It was very novel at the time. Also very surprising that they did it with Roman. It's because he was a bit exit shady, or erratic, shall we say. He did not come across as the sort of person that you'd be doing a banking...

**[53:20] SPEAKER_01:** No, but he was... to Banco Santander and not JP Morgan.

**[53:24] SPEAKER_00:** I guess so. But...

**[53:26] SPEAKER_01:** Sorry, but...

**[53:28] SPEAKER_00:** But that was happening. Yeah. All that time back. Yeah.

**[53:32] SPEAKER_01:** That's cool. Yeah. No, it's interesting. I feel like in the beginning, in the early years, banks were very interested in Ethereum. I think there were some sponsors for DEVCON 1.

**[53:44] SPEAKER_00:** Yeah.

**[53:45] SPEAKER_01:** In grad school where I was, there was certainly UBS. I think JP Morgan might have been. So we had these... It was MBA school and we had these challenges that companies would come in and propose concepts to, and the students, the engineering and the business school students, would come up with sort of solutions to these challenges in the form of products or companies or whatnot or ideas. And one, the banking one was blockchain. And basically the challenge was, incorporate blockchain into our... in some way that's useful for us.

**[54:26] SPEAKER_00:** Right.

**[54:27] SPEAKER_01:** And it was... And the team, of course, I think they explicitly said Ethereum, which at the time just launched. It was like 2015.

**[54:36] SPEAKER_00:** Right, right.

**[54:40] SPEAKER_01:** But yeah, banks are really... Of course, they've stuck around. So now they're doing their ETFs and making boatloads of money off of blockchain assets, of ERC-20s that came from MistCoin.

**[54:56] SPEAKER_00:** There you go. And started back there.

**[55:00] SPEAKER_01:** Yeah.

**[55:00] SPEAKER_00:** Okay.

**[55:01] SPEAKER_01:** Which is also an arguable thing. What is it to say that it came from MistCoin as the origin of something?

**[55:11] SPEAKER_00:** Well, everything's built on top of everything else, right. It's all just ideas. All right, well, maybe that's a good place to wrap up.

**[55:21] SPEAKER_01:** Sure.

**[55:23] SPEAKER_00:** Thanks so much.

**[55:24] SPEAKER_01:** Yeah, thanks for having me on.

**[55:26] SPEAKER_00:** You're very welcome. And Ethereum Classic, sorry, Ethereum History, yes, is the site for people to go. And so we've got a call to action to get people to come in, come and have a look.

**[55:41] SPEAKER_01:** You can sign up with Google, GitHub. You can create an account just simply with your Ethereum wallet. You can create an account with a fake email. Doesn't matter. The idea is just to come in and help document old contracts. Whether that's... there's somebody who's helping out a lot right now who's just spending his time during work because he's bored. Colin, telling his AI friend to help document. He's doing great work. He's cracking all these early contracts.

And so if anyone's interested in just spending some time helping research and adding and documenting, you can just do it without any approval. And this sort of Wikipedia of Ethereum will solve itself out in perfection over time. We'll tell the right stories. Of course, if you're malicious and you're trying to just mess everything up, please don't join. Because we're trying to document Ethereum's history accurately.

But yeah, it would be great if it takes off. I mean, I think it really is something that doesn't exist anywhere else and should have utility for people over time if it gets filled out. And I do have this vision. I didn't say it earlier. I have this, and I have ideas already. I've already sort of formulated the contract, but putting it on chain so that basically, like hashing the JSON of the whatever content we want to keep and then pushing the hash on chain so it's not an insane amount of money that needs to be deployed each time there is a change. But...

**[57:18] SPEAKER_00:** Right.

**[57:18] SPEAKER_01:** Those things are difficult because of the monetary aspects of it. But it does make sense that something about Ethereum should have Ethereum involved.

**[57:28] SPEAKER_00:** We're going to get the Ouroboros snake eating itself.

**[57:34] SPEAKER_01:** Exactly.

**[57:36] SPEAKER_00:** Because every time that you push one of the hashes on, then you've got to push the hash of...

**[57:41] SPEAKER_01:** The hash of the hash of the hash.

**[57:43] SPEAKER_00:** It never ends. Right. Because you...

**[57:45] SPEAKER_01:** That's true. Yeah. No, it has to be this... It's... Yeah. Otherwise you lose the history, right? Of the... Yeah, you're right.

**[57:54] SPEAKER_00:** Okay.

**[57:54] SPEAKER_01:** That's a good point.

**[57:55] SPEAKER_00:** Can never end.

**[57:56] SPEAKER_01:** Never end.

**[57:59] SPEAKER_00:** It will grow until the whole of the chain is taken up by the hashes.

**[58:03] SPEAKER_01:** The hashes of the hashes. Which is poetic in a way that Ethereum should be taken up by Ethereum history.

**[58:12] SPEAKER_00:** Okay, well, thanks so much.

**[58:14] SPEAKER_01:** Thanks, Bob.

**[58:14] SPEAKER_00:** Cheers.