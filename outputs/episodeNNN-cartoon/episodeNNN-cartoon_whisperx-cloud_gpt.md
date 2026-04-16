**[00:05] SPEAKER_00:** So yeah, I guess, okay, welcome to Early Days of Ethereum. Thank you. I'm here today with Cartoon for a rather different kind of topic and episode than normal, because The Late Days of Ethereum is what it's called. The late days, right? The late days, because normally I'm talking about social history of OGs and their memories at the time, learning. But you have had a rather different focus on on-chain history.

**[00:53] SPEAKER_01:** Yeah, no, thanks for having me on the show. I've been, as you know, a very big fan of your work. And yeah, I'm not, as you said, an early days of Ethereum person, but I think this project that we'll talk about is, in ways, a celebratory venture of the efforts of the folks who are worthy of this actual channel that you have, this Early Days of Ethereum effort.

**[01:23] SPEAKER_00:** So, yeah, I mean, how did you yourself get involved with Ethereum and this on-chain thesis?

**[01:31] SPEAKER_01:** So my Ethereum story, honestly, started through investing. Like many others, it came on during the boom. I kind of ignored all of the early edges and articles I read toward the exciting technology of blockchain and where it could go. Everything was focused in 2010 to 2013 about how it's either you're in it, which was the view, or it's absurd, and it's speculative, and everyone's going to lose their money, and they're gambling and whatnot. So I kind of jumped on that bandwagon, was interested, but on the side, and never really dove in.

I even had a friend in 2012 mining Bitcoin in his aunt's closet, and he was telling me about it. He was very adamant. I respected the guy. He was a good friend. I respected him a lot. And so I guess I look back at that as, what were you doing? Why didn't you just listen? But he was telling me, hey, you should keep an eye on Ethereum as well.

At school during Devcon 1, actually, one of my classmates spoke at Devcon 1. I was telling Alex van de Sande that one of my classmates spoke at Devcon 1, right? But again, just didn't jump in. And then I didn't inevitably jump in until maybe 2021. I think under 2020 it started popping up. And I saw some absurd tickers on this app called StockTwits, which at the time I was kind of interested in. Over-the-counter stocks, this was the GameStop era.

**[03:43] SPEAKER_00:** Yeah, there were all these absurd—

**[03:45] SPEAKER_01:** It was the PancakeSwap era, actually.

**[03:47] SPEAKER_00:** Right, right.

**[03:48] SPEAKER_01:** It was the PancakeSwap era, which was the platform where every absurd ticker at the time, like BuckleCoin or whatnot, I think it was, but ticks—

**[03:59] SPEAKER_00:** Yeah, but ticks was all Binance Chain, right?

**[04:02] SPEAKER_01:** You know, I saw these tickers go 5,000-whatever percent every whatever flashed at me, and I was like, okay, I've got to try one of these. And so I got in. But that led me to, okay, what am I actually buying? Then I started to look into what ERC-20 at that time was, already established, the standard and whatnot, of course. So I looked into that, and Binance Smart Chain, or that's what it's called, it's just an emulation of—

**[04:33] SPEAKER_00:** Yeah, yeah.

**[04:34] SPEAKER_01:** Just took the ERC-20 contract and repurposed it. So the ERC-20s, they're all just funny because, as we know, Fabian just made the—was the pull request the 24th request or something. But anyway, yeah, that led me to contract development. I was interested, and it went from fungible tokens to non-fungible tokens, and I got mixed up into an NFT project and became their software engineer, per se, or dev, as I came to find out all the terms of rugged and devving and whatever. Everyone was a dev.

**[05:14] SPEAKER_00:** As a dev—sorry, we're all the devs. Oh sorry, all the devs. With AI especially, we're all devs.

**[05:20] SPEAKER_01:** Yeah, every single person. My parents are devs. They're all devs. But it was funny to me at the time. I was struggling to sort of keep track of all the vernacular and take anything seriously, especially everything was on Twitter Spaces at the time. Everyone was establishing their voice on Twitter Spaces. So the word rug was probably set up—there's Rug Radio, which may not exist anymore.

**[05:46] SPEAKER_00:** Wrecked. Oh yeah, there was always some version of wrecked.

**[05:50] SPEAKER_01:** Yeah, I just got wrecked. So I became this NFTs-to-developer, and I was developing all these different smart contracts. There wasn't—I found a lot of creativity was sort of—but everything was a bit of a copy of what somebody else had done in this case, and they were trying to push it.

**[06:40] SPEAKER_00:** This is for security because they're well audited.

**[06:43] SPEAKER_01:** Yeah, exactly.

**[06:47] SPEAKER_00:** It's a risk management strategy.

**[06:49] SPEAKER_01:** There's no AI to check, so you just would copy somebody else's. Whether that meant copying already malicious code that was implemented or not, it was funny. Actually, one of the contracts—so this NFT project that brought me in and wanted me to help with development, their first contract was—they hired a Fiverr developer. It turned out, after we did the second contract and mutations and whatnot, that the original contract, which they hired this Fiverr person to do, they had rewrote this owner-only function such that they could, the inherited function, actually jump in and take over any time, right? They could pull the money that was in the contract. But it was hidden enough because it was on the inherited contract class, not the main one, that they didn't see. And I don't think anybody there was technical enough to even vet the contract well.

**[07:56] SPEAKER_00:** Well, it happens, apparently, back in the day with a bunch of experts. So if you're just winging it, these things—

**[08:04] SPEAKER_01:** A hundred percent. I mean, in my mind, because you were saying you copy these for security as a joke, I think that in my head at the time I was like, okay, there's this Fiverr gang that's out there just telling everybody to deploy these contracts, and then they're sharing the funds or something. But it very well might have just been somebody copy-pasted that from some GitHub repo.

**[08:24] SPEAKER_00:** Yeah, they were the scammer. They didn't even know. They were just the infection vector for scams.

**[08:32] SPEAKER_01:** Exactly. The lead, the head dev at the time, asked me, he said, so what are the chances that we're going to get scammed here or whatnot? And I was like, well, they can take the funds out of this contract. It doesn't seem like they can do anything, but there's different funds in there. In theory, this person could come in at any time. Do they know about the fact that they've edited this function in a way? Maybe not. So maybe they just copied it from someone else. And ultimately they were forced— their hand was forced because OpenSea actually maybe flagged them, maybe somebody flagged it for them or something, and I had to do a migration contract. But all this development was the seed of the interest for me.

And then what led to Ethereum history was, a few years later, probably in like 2024 or something for me, so pretty recently.

**[10:12] SPEAKER_00:** Or maybe 2023.

**[10:14] SPEAKER_01:** Yeah, yeah, probably 2023. Anyway, this coin popped up. And so this was actually post—there's this Relics group, this folks group of Discord friends, that focus their time on collecting NFTs, old NFTs, and old contracts on not just Ethereum, but they're into the one that was kind of like—oh—inscriptions and ordinals, not ordinals before—

**[10:42] SPEAKER_00:** Counterparty?

**[10:43] SPEAKER_01:** Counterparty, yes. Super old. And some of them don't like Counterparty NFTs or NFTs because they're not really, it's all built, it only exists if you have this other Meta protocol.

**[10:55] SPEAKER_00:** Right, right.

**[10:56] SPEAKER_01:** So there's a debate and whatnot, but everybody collecting, they basically like these old things. Anyway, they reached out. They found MISCoin in their digging of old contracts. So MISCoin was made as a—

**[10:54] SPEAKER_00:** Example token for the Mist wallet, right?

**[11:00] SPEAKER_01:** Exactly. Yeah, yeah. MISCoin was made by Alex van de Sande and Fabian Vogelsteller, who you know well, and you've interviewed. Fabian deployed it. But essentially they were, at the time, my understanding, developing a feature for the Mist wallet, the Ethereum wallet, to allow anybody to deploy contracts. So at the time, before then, you can't click this button. And within the feature there were templates, right? So it was kind of like the first standard in a way. At the time, the standard itself was being molded from before launch and whatnot in the standardized repos, but this morphed—this was the current state of that more standard code.

**[11:54] SPEAKER_00:** Yeah, and that was still pre-ERC-20 actually happening.

**[11:59] SPEAKER_01:** Exactly. Pre that. Whether it was the commit or the—

**[12:05] SPEAKER_00:** Or the 20th pull request.

**[12:06] SPEAKER_01:** I'm not sure. I'd have to ask Fabian or check.

**[12:10] SPEAKER_00:** It's funny, actually, the way that works is issues and pull requests are from that same ordinality. So it doesn't mean it was the 20th pull request. It was the 20th issue or pull request that had been created. So yeah, it can be either, because they never have the same numbering because that would be ambiguous. So it's the 20th time somebody either made a PR or issue or put in any issue whatsoever. Anyone could just chuck any issue in, and that would up the count. So a good number of the numbers are never anything. They never land right on the thing. An issue that says, hey, I don't really like the color red, right? So if you look at EIPs now, they're in the thousands, and it's not because there have been a thousand proposed protocol changes.

**[13:22] SPEAKER_01:** Okay, that's an interesting way of doing it. So yeah, EIP-20. So this was November 3rd, was when they deployed that feature, and MISCoin being the first one that they launched with it then. At Devcon 1 they talked about it a little bit. Standards panel. Simon de la Rouviere spoke about token standards itself. He was also one of the few who were helping mold this standard.

Then a few days later, the 19th, I think, or so, 19th November, is when Fabian and Vitalik sort of formalized this proposal, the slight adaptation, change of the code of MISCoin, but really this standard that they had been molding.

It was funny, recently I found through Ethereum history, digging of old contracts, a coin that Vitalik had deployed. It wasn't immediately clear that it was a token. You have to really look through the bytecode itself, and it didn't really—if you tried to decompile it with the decompiler on Etherscan, it didn't really work well or really tell on the surface. Anyway, if you look through the bytecode though itself and you're just raw looking at it and analyzing it, which is much easier to do now with AI, you could tell it's a token, right? It turned out it's actually this currency that he had deployed in the Dapp Bin repo in September, or earlier, maybe September 8th or something, I don't know.

But what I thought was interesting, after I had found the exact Serpent code and proven that, hey, it compiles with this version of Serpent to this exact bytecode, and I posted about it, Vitalik actually commented on it as well and read it. He didn't answer this question, so if he hears this hopefully he responds. But what I was wondering is, so he deployed this days before, I think maybe November 6th, but days before he went and co-published this proposal, the standard. And it's sort of his old what he would have wanted as a token, I don't know, his early proposal in a way. And I wonder if that was his way of immortalizing, hey, I like this thing, we ended up going with something else, now I'm going to immortalize mine on-chain. I like my way better. Different things. So that's how I like to imagine it's there. One day maybe Vitalik will decide, hey, everybody—

**[16:26] SPEAKER_00:** Should have my unnamed coin. That's pretty random, what people ended up pushing or not pushing.

**[16:38] SPEAKER_01:** And it's all—yeah, but there's only one. So I guess Vitalik doesn't make many mistakes, and he probably even was using testnet or whatnot back then. But a lot of folks were testing in—

**[16:51] SPEAKER_00:** Production. Yeah. This is like, there's no economic value in the army, so—

**[16:57] SPEAKER_01:** Right, right. It was trading a cent to the dollar back then. You're like, oh yeah, I spent 10 ETH on—yes. But a lot of the contracts now that I—

**[17:19] SPEAKER_00:** I'm going to actually introduce them. Well, just before we get to that: so you spoke about MISCoin as sort of being where you started. So is that wrapped now? Is it Wrapped MISCoin? Was that because it was slightly pre-ERC-20? Did MISCoin need wrapping?

**[17:42] SPEAKER_01:** It needed wrapping. It doesn't have an approve function. It doesn't have a few other functions. It's one of the first named tokens, so in that way it's kind of special. And it doesn't adhere to the current standards such that if you tried to create a Uniswap pool for it, it wouldn't work. There's no approve and transferFrom methods that it needs, or transferFrom and approve, it's just not going to move. So essentially, if you wanted to make it tradable—which at the time, so this group, this Relics group, had found a MISCoin DAO that Alex had made and brought this MISCoin in. Once they acquired some of the MISCoin, they were given, I think, from both Alex and Hudson if I'm not mistaken—

**[18:31] SPEAKER_00:** Right, right.

**[18:32] SPEAKER_01:** They then were able to also pull more of MISCoin from this DAO. So I think Alex had put in 100,000 MISCoin, which is like 10% of the entire supply, into this DAO. So they took that out. And then they used it, they just gave it out to a lot of folks in their community of early NFTs. They kind of framed it as, hey, this is going to help early NFTs and it's going to help boost our community, and they were into that.

So there is now a DAO that holds, I think, maybe 4% of the supply, at 40,000.

**[19:06] SPEAKER_00:** Right, right.

**[19:07] SPEAKER_01:** The rest is kind of given up to all their folks. And so when I bought it, I bought it as a sucker. I bought it at like $50 a MISCoin or something. I was like, cool, I can own this thing like everybody else. By the time it reached my timeline, it's too late, right? A lesson for everybody, at least at the time. But yeah, so they probably did very well.

Besides that, they are this group, which I can't say I'm necessarily part of, but they very much care for cultural relics specifically, as they call them, specifically non-fungible tokens. So they're very much cool collectors.

But MISCoin led me into this early interest in early contracts. Once I started to dive into the story of MISCoin itself, and what Fabian and Alex were doing at the time, and how it was the beginning of basically everything that moves Ethereum today, everything that people are interested in from an external perspective, in the tokenization of finance and whatnot, it all stems from the need for there to be a standard. That understanding, that importance, led me to say, okay, well what else is out there? What else was happening at the time that is either interesting today or will be interesting later, and can we sort of uncover that now?

So while I was writing a website for MISCoin and helping with any engineering projects that needed to tell that story, on the side I started to download all of the contracts from 2015 and then 2016 and peruse through the bytecode before AI and all these LLMs were out there. So I was really just using decompilers, like Panoramix decompilers, and running similarity text algorithms to try to figure out, okay, what is the likelihood of this being a token, or this being ownable, or this being fungible, or this being something? Look at deployer addresses, known deployer addresses, type of thing. But it was a much more difficult assessment than it is now.

**[22:14] SPEAKER_00:** I guess it's almost like a reverse engineering kind of discipline. You've got this—it has been a lossy thing, right? That compilation process, it's not intrinsically reversible. You've got that data loss and you've got these patterns, but no blockchain ever stores comments.

**[22:42] SPEAKER_01:** Exactly. Yeah, it would be really great if it was possible to make Ethereum in a way that you could actually just store all the code itself and not have to do the bytecode.

**[22:54] SPEAKER_00:** Well, I'll tell you what funny little thing actually is: STRATO, that I'm working on, that actually does happen for our chain, because it has an alternate VM called a SolidVM, which is an EVM as well, but it's actually an interpreter. So what you have is you do have source code on-chain, which gets deterministically interpreted. So it's almost like you've kind of got Etherscan built in, kind of.

**[23:31] SPEAKER_01:** Kind of, right. And you don't have any issues with having to transmit large chunks of data through—

**[23:38] SPEAKER_00:** Consensus? No, it's been okay. I mean, yeah, you couldn't do that at a huge scale. You couldn't do that at a huge scale in a completely permissionless validator scenario, but yeah, there's an alternate universe where different things had been chosen.

**[24:05] SPEAKER_01:** Yeah, because like you said, before it's been a challenge. I didn't even really attempt—there were a few attempts. There's this person who has helped and has done a lot of work in trying to exactly prove the MISCoin code, and eventually did, with the help of others. But it's a guessing game. At a certain point you're trying to guess the order of functions, the functions themselves, the method names, and you get to a point where you get close, but so many things could go wrong. There are so many possible permutations. There's the compiler version, there are those settings, there's, like I mentioned, the order, the naming of the functions.

In some cases, even now with LLMs, it's made it impossible. In one contract, for example, I'm down to just this one function name, and I know that it is more than 10 characters long because I've tried every possible eight, seven. So I literally had this machine running on my computer just chugging through every—

**[25:33] SPEAKER_00:** At first it wasn't even doing anything intelligent. It was literally going A-A-A-A-B.

**[25:38] SPEAKER_01:** Yeah. So actually, you can't do that once you get to the higher character count. That just would take forever. But I just gave up because what's the point? You know what the function does. So you'll see on Ethereum History some say “near exact bytecode,” and I'll actually indicate how close it was, because I'd give up at a certain point. As long as you have the exact functionality and you're pretty close to complete, and the bytecode is off by a few segments, then—

**[26:08] SPEAKER_00:** Right, right. I mean, I guess a decent amount of the source code is probably on GitHub somewhere.

**[26:16] SPEAKER_01:** That's another tactic. So yeah, when I'm doing this sort of what I call cracking—and there's an Ethereum History “cracking” skill and whatnot out there—but one of the approaches is researching. So just going off Reddit and to GitHub and trying to find the contracts, or contracts that are similar. Even back then folks were doing something and another person would make a slight adaptation to it, whether that's naming this function something slightly different and now I can't guess it, but everything else in this case literally is, like you said, published somewhere.

**[26:52] SPEAKER_00:** Yeah, somewhere, somewhere.

**[26:54] SPEAKER_01:** Yes, but you find it through keyword searches on GitHub and stuff that mentions it.

**[26:59] SPEAKER_00:** Right, right.

**[27:00] SPEAKER_01:** Yeah, it's definitely a great tactic. It shows you can document everything on Ethereum History, but still it's great to know that they're fragmented out there. As long as the internet is around, there are at least other folks documenting in time. Thanks to the Internet Archive, even some things that have been removed are still out there.

One of the things I was pretty disappointed about—and maybe they'll bring it back one day—is Ethereum took down, last year or two years ago, the standards repository, the standardization repository. So literally this one GitHub repository, they just kept track, this wiki, they kept track of all of the different standard commits as that progressed for tokens.

**[27:50] SPEAKER_00:** So this was a wiki within a given GitHub Ethereum something?

**[27:55] SPEAKER_01:** Yeah, so a lot of the commits are still there on Internet Archive, and some folks had forked it at different junctures, so you can kind of find it at different stages.

**[28:07] SPEAKER_00:** Right, right.

**[28:08] SPEAKER_01:** But I don't know what's the purpose of taking it down. I mean, I think they probably had some reason. Maybe they didn't want to have confusion or something.

**[28:27] SPEAKER_00:** Yeah, or sometimes it can just be in complete ignorance of the consequences. It's just somebody cleaning up or whatever.

**[28:33] SPEAKER_01:** Yeah. So I would imagine, hopefully, that somebody at Ethereum has downloaded the repo over time and can stitch it back together.

**[28:52] SPEAKER_00:** For the History of the White Paper, Pol Lanski has done a lot of digging into those details, but it was only through him I realized that he had got some of those Internet Archive versions of the old wikis. I thought they were all gone a very long time ago. So it was kind of fun.

**[29:17] SPEAKER_01:** Yeah, those are still on the Internet Archive. And you probably remember this, but another thing I found on the Internet Archive is around that time in 2015 there was a bulletin that was kept up by somebody in Ethereum. It was basically a forum where you can ask questions, but it was all seemingly self-posted.

**[29:38] SPEAKER_00:** Oh, that's just the Ethereum forum, I think.

**[29:42] SPEAKER_01:** I think it was the Ethereum forum.

**[29:44] SPEAKER_00:** Yeah, and people were talking and it had its own message threads. Yeah, yeah. That was a Discourse, I think. Discourse the software. But yeah, that wasn't used for very long. Reddit became a lot more popular. But then I remember there was a whole bunch of drama about, oh, we're going to shut the forum down, are we not? And then it was like, oh okay, maybe somebody in the community wants to maintain it. But then it's like, oh, but you can't because you'd be giving over the database that has all the DMs in it, and it would all be—so I think Hudson kept maintaining it for quite a while. I don't know if it ultimately died, because—

**[30:34] SPEAKER_01:** It would be interesting. And there was definitely at least one contract that through the Internet Archive I could see that I was about to get some important information on it, and then next week it's gone. But yeah, some of these ventures into trying to document some of these contracts go quite deep into these Internet Archives, and they're not easy to browse through. But you get into those old things that have been taken away and it feels exciting, because it kind of feels like you're digging into something that nobody knows anymore. That's what's kind of kept me going.

And it seems like people are genuinely excited. It's a small group, and obviously I only have Reddit and those folks who are still on Twitter to speak to this. I wish there were other avenues. But there is a decent community of folks that still reminisce and still want to know about it and know about history, and the first programmable blockchain, what that really was like. And not just from people's perspective, but the actual testing, contracting.

So I mean, your—

**[31:59] SPEAKER_00:** So your site is ethereumhistory.com. What features are there? What can people see if they visit that?

**[32:07] SPEAKER_01:** So the way—my short elevator pitch is: Wikipedia of Ethereum smart contracts. The idea is Etherscan itself is great. Etherscan tells you all the facts about every contract that they can find on-chain. You can see, of course, the bytecode, you can see the code if they verified it or not. But there are very hard restrictions on how you can verify it, right? And they only support—

**[32:40] SPEAKER_00:** A certain 0.something version of solc, right? Probably the version when they started.

**[32:50] SPEAKER_01:** Probably, yeah, yeah. You can't go further back. So anything early, you can't really verify. But beyond that, actually adding any descriptions or anything, or any tags or anything, is very difficult with Etherscan. So it's really not meant to add any meaningful documentation to a contract. It's really just there to say this thing exists. And outside of that, there's nothing popular, or nothing I could find, that has any sort of purpose of recording the history like a Wikipedia would.

And of course maybe there are some projects that have gotten to the point at which there is a Wikipedia page for them, and it will probably say a link to Etherscan or a link to your show, their contract address maybe, which is probably meaningless to people. They probably just place the website.

So basically: where's the home for this Wikipedia? Where's the home for folks who are interested in Ethereum to learn about those early contracts, learn about the story behind them, and look at the original code itself? Not the bytecode, but let's look at the actual code.

And I think there are two different things that people can take out of that. One is, if you're interested in the stories, you can go back and sort of see the qualitative stories. They're not always going to be accurate because every story is a picture of what somebody remembers and tells one other person, and your memories are of course fickle and perhaps might not be exactly right, and even a fear.

But hopefully with the idea that Wikipedia is everybody sort of edits it over time and it becomes—

**[34:34] SPEAKER_00:** Right, so hive mind.

**[34:36] SPEAKER_01:** The hive mind. It's going to be perfect. It's very efficient. So anyway, right now Ethereum History is not exactly efficient, because there are 18 different historians, of which the users are called historians, who have documented contracts. So after everybody watches this video, everyone sign up, it's free.

But one thing you can take away is the stories. And then the other thing that you can take away is actually reading the code of all these early contracts. And the vision I have there is, once we do get the code, I want to find, of every or most of these contracts—which we're making pretty strong headway on right now—I want to find a way to represent that in some sort of visual. In my head, I don't know how this is going to work out, but I picture archaeology, like rocks, the way that you can look through the layers of the earth and write history through them. Some sort of visual representation of that, but through code functions or methods. I don't really know. It's kind of—

**[35:59] SPEAKER_00:** It's a loose thought in my mind, but I would love something with a scrubby timeline somehow that changes shape somehow.

**[36:07] SPEAKER_01:** Yeah. I'm interested in what sort of stories, what can we learn about the reuse of different types of methods and how they—and then maybe the popularity of the contract. The amounts that it's been—what you could discern by the number of times it's been replicated, or the number of transactions that have occurred, or the popularity of people—and then how long that has lasted over time.

**[36:37] SPEAKER_00:** Yeah, and what that is like, species coming to life and dying off.

**[36:42] SPEAKER_01:** Yeah, exactly.

**[36:43] SPEAKER_00:** Look at that dinosaur technique that literally is a dinosaur technique that's not used anymore.

**[36:52] SPEAKER_01:** Yeah, and it's a hard thing to keep track of because a method has a purpose, right? It has a name, but it's meant to do something. It might do several things. It might be part of a larger set of goals, of functions that are calling it and whatnot. But if you're trying to find a thread through history, you might want to look at—you’re dealing with a semantics problem as well, because it doesn't have to be the exact method, but the same purpose. Has it gotten hardened, or worse, or better over time?

**[37:29] SPEAKER_00:** You're wanting to infer design patterns out of it or something, or higher-level patterns or reasoning.

**[37:38] SPEAKER_01:** Yeah, yeah. Hopefully that's possible. It's a loose thought in my mind. I don't know. We'll see what people want to build. It's an open source project, so hopefully folks will add their own pull requests to that sort of thing, or issues, and I'll mark them as proposals, EHIPs, regardless of whether it's an issue.

**[37:58] SPEAKER_00:** Right, right. EHIP-1. Or if anybody wants to grab a lot of pull requests, since I'm just going to go straight to that.

**[38:06] SPEAKER_01:** Right, just straight to commit. We're going. But yeah, the code and the stories are kind of the angle now.

And the other angle I have: so I got into this downloading all of the 2015 to 2017 contracts, decompiling them all, loading them up into this database. Then on top of it I've added these indices on this database such that you can query through all of the decompiled code. The goal there was anybody should be able to find interesting things through the code. Maybe there's somebody interested in mining, or they're looking for the first time that the word “cat” was written somewhere. The decompilation won't be perfect. It might not have the actual first cat. There's a chance that it does. And this gives them the ability to search through text rather than just bytecode.

So that was the first idea. Now what happens is every single time a contract is cracked, as I call it—meaning we've solved the exact code with the compiler and settings—that gets added to the index as well. So you can actually search through that code.

**[39:30] SPEAKER_00:** That sort of improves that discoverability. So what kind of different existing tools have you been using or found useful while cracking, and for researching, and disassembling?

**[39:47] SPEAKER_01:** So the disassembling has been interesting. This whole cracking thing, it depends on the contract. The first thing I'll do—and of course, all this heavy usage of AI here, always.

**[39:58] SPEAKER_00:** Yeah, yeah.

**[39:59] SPEAKER_01:** My AI overlord is helping me out every day. But the first thing I'll have it do is just go through and see, hey, through my Ethereum History researcher skill that just goes through GitHub, Reddit, and tries to find first—it will decompile it, or use the decompiled code I have already, and try to find anything that resembles it in GitHub or Reddit at the time. If it finds a match, or it knows of some match—it obviously has its inherent knowledge already, at the time these things were out there or published—then it will start there.

So it's mostly about finding a starting point, if not the exact code. Sometimes it is exact. Sometimes it's a very reused wallet at the time, or something. So it's establishing a starting point. And then from there it's taking the different versions of solc at the time, or it will try to determine, is it Serpent or is it LLL or whatever. It may have some Mutan.

I haven't found any Mutan, not yet. Honestly, so far only Serpent and—there's two, so Serpent, Solidity of course, and then in some cases it's just straight code. I think they deployed straight bytecode. So as far as the AI could discern, there wasn't actually any code. They just created the bytecode themselves and launched that.

**[41:41] SPEAKER_00:** It's strange, because I thought you always had LLL in the line, or maybe this was only for Solidity. I think for Solidity it was always built on top of LLL at the start, kind of using LLL as an assembler. But yeah, I mean Jeff was working on Mutan up almost until launch, so it might be that there's hardly any Mutan on mainnet. Probably a bunch of that on Olympic, but then it kind of—

**[42:22] SPEAKER_01:** Yeah, for the ones that it discerned were all done in straight bytecode, it used Yul, I think, or something.

**[42:32] SPEAKER_00:** That's somewhat recent, like 2018. Yul?

**[42:35] SPEAKER_01:** Yul, sorry.

**[42:37] SPEAKER_00:** Though who was it who was talking—oh, that was Alex Beregszaszi, axic, A-X-I-C, okay, who was Solidity co-lead for many, many years. So he was saying that started—it was called Yul at first, like Julia, but with a J, I think. But then there’s some other computer language called Julia already, so then that changed into Yul, Y-U-L, which is an intermediate representation. The goal was that Solidity would compile to Yul and then you would have a further compilation step on the back of that. Well, hopefully. So I guess it kind of ended up being sort of like an assembler.

**[43:48] SPEAKER_01:** Hopefully they're proud to know that AI is still referring to their work, because for those few contracts it chose to represent them in Yul.

**[43:58] SPEAKER_00:** Right. That's good. Yeah, cool.

**[44:01] SPEAKER_01:** Yeah, so that's there. And so this part of it is research, part of it is chipping down, if you will, to this bytecode. In the process, of course, it takes it to the time at which this was deployed. So you know the different versions of solc that were out there at the time, and you just try to trial-and-error kind of thing.

**[44:36] SPEAKER_00:** There's no metadata that ends up of the solc version in the final bytecode, I think. Correct me if I'm wrong.

**[44:45] SPEAKER_01:** I think the metadata started a bit later. There was a particular newer version of solc where that started, yeah. I want to say that because that became a thing as I—so the person who leads Sourcify reached out and has been really great. He's been helping. He expanded Sourcify such that it could go down to much earlier versions of solc. So I think you can be verifying on Sourcify and also adding all the methods that we uncover so that they're there for the world to sort of—

**[45:25] SPEAKER_00:** And what does Sourcify do exactly?

**[45:28] SPEAKER_01:** I'm going to butcher this, but sorry. They seem to be the registry of not just methods that have ever been deployed on the blockchain, a way to make that accessible to everybody, but also to verify the actual source code of any particular contract. So it seemed to be something that you would do going forward for a lot of contracts, if I understood it correctly. But then they've started to also go—

**[46:04] SPEAKER_00:** Backwards.

**[46:05] SPEAKER_01:** Backwards. Exactly. Yeah, maybe the idea was, why should—maybe Etherscan would want to just replace it with Sourcify.

But yeah, I've pinged Etherscan a few times, especially as I started to validate or crack a bunch of these earlier contracts that I could not verify. Essentially the way that you would verify on Etherscan for these older contracts is you would reach out to support at Etherscan.

**[46:36] SPEAKER_00:** Right, yes.

**[46:38] SPEAKER_01:** That's how you would reach them. And they respond. For MISCoin we had to go through somebody, somebody who was there, and eventually that person reached back and said we're going to help you get this verified. But I cold emailed a bunch of these, and they're really interesting. I mean, they still haven't validated them. For example, GAVCoin, Vitalik's currency, these are arguably very interesting and probable contracts and from arguably very important people in the space, and they still haven't.

So I got this sort of blanket response that was, thank you, but you need to be the deployer. Are you the deployer? Have you signed this? Can you sign this transaction? And I was like, sorry, I'm not 0xBB2, I cannot sign it.

Somebody did reach out on Twitter and said, hey yes, sorry about that, that's our blanket response. And here, actually, we helped verify one. And it was one of these Pepes, you know. Peperium, you know, this Peperium is like I think from 2017 or so, an NFT-like contract. I think it's more of a fungible token, but in some way they added metadata onto it.

**[48:23] SPEAKER_00:** This is not Pepemon, no.

**[48:25] SPEAKER_01:** No, no, it's not Pepemon.

**[48:27] SPEAKER_00:** Piper Merriam? No.

**[48:29] SPEAKER_01:** Yes, that would be hilarious if this was Piper.

**[48:32] SPEAKER_00:** It should be, right? They roll off the tongue the same way.

**[48:36] SPEAKER_01:** Peperium, I think it's more about Pepe. Every one of them, I think, has some sort of picture of Pepes. But anyway, so this Etherscan person verified that one of all the ones that I sent, and I was like, one of the ones I care about? One of the top ones? I don't want to say I care one way or another.

**[49:03] SPEAKER_00:** I'm sure a lot of people care about it. So GAVCoin must have deployed GAVCoin onto Olympic and onto Frontier then separately.

**[49:11] SPEAKER_01:** Oh sure, I'm sure he did on Olympic. He must have. It's for fun, right?

**[49:19] SPEAKER_00:** Well, because there was the talk I found, which was August 2014, I think.

**[49:24] SPEAKER_01:** Yeah, yeah.

**[49:25] SPEAKER_00:** With Jeff in London.

**[49:27] SPEAKER_01:** Yeah.

**[49:28] SPEAKER_00:** Doing the DEX, you know, demonstrating that. Joking around, that's right, how GAVCoin's the better coin. That's it. Gav saying he values GAVCoin.

**[49:58] SPEAKER_01:** Yeah, so I can't prove that GAVCoin, the one I found, was right. But I have a chain of information, a thread of different events, that seem to make a strong case. Maybe Gavin will listen to this and decide to tell the whole world that it was deployed.

There's another theory I've worked on. It could have been potentially deployed by Roman, the person who ran that—

**[50:25] SPEAKER_00:** Mandalay?

**[50:26] SPEAKER_01:** Yeah, which I wasn't around, so I don't really know. I mean, I know Piper, I think, did some work with Ether Camp at the time.

**[50:35] SPEAKER_00:** I believe so.

**[50:36] SPEAKER_01:** So I don't really know. I'm sure about things I read. So yeah, exactly. That's why I think it might be potentially deployed by him, because I think the deployer might have also deployed Hacker Gold.

**[50:50] SPEAKER_00:** Right, so could that have been—

**[50:52] SPEAKER_01:** Yeah, then I think it's possible.

**[50:55] SPEAKER_00:** If it was Hacker Gold, that would be Roman, for sure. So maybe this was—

**[51:02] SPEAKER_01:** Yeah, I have to look, I forget now. It's been a long time of looking at other contracts that follow the deployer. But I found some connection to Hacker Gold as well. So maybe Roman wants to tell the world about it.

**[51:21] SPEAKER_00:** I don't know if anybody talks to Roman anymore. I used to be Facebook friends, but then he seems to have gone off. But yeah, he basically disappeared in 2017, really. But he was around. Iconic himself, as I understand.

**[52:00] SPEAKER_01:** Some of the firsts that have been from him. Quite a character.

**[52:08] SPEAKER_00:** Hacker Gold—one of the things that became dated, which is unbelievable at the time, let alone now, is they—at Devcon 2 in Shanghai, so October 2016, they did this demo called CashF with Banco Santander. It was basically a stablecoin on Ether in-browser. So it was sort of like you've got some kind of MetaMask-y thing for doing sending stables in a browser on Ethereum. It was very novel at the time. Also very surprising that they did it with Roman, because he was a bit—

**[52:48] SPEAKER_01:** Exit shady?

**[52:50] SPEAKER_00:** Erratic, shall we say. Yes. He did not come across as the sort of person that you'd be doing a banking partnership with.

**[52:58] SPEAKER_01:** No.

**[53:00] SPEAKER_00:** But he went to Banco Santander and not JPMorgan, I guess. Sorry. But that was happening all that time back.

**[53:11] SPEAKER_01:** Yeah, that's cool. No, it's interesting. I feel like in the beginning, in the early years, banks were very interested in Ethereum. I think there were some sponsors for Devcon 1.

**[53:25] SPEAKER_00:** Yeah, in grad school, where I was, there was certainly UBS.

**[53:31] SPEAKER_01:** UBS, yeah. I think JPMorgan might have been. At business school we had these challenges that companies would come in and propose concepts to, and the students, the engineering and the business school students, would come up with solutions to these challenges in the form of products or companies or ideas. And one of the banking ones was blockchain. Basically the challenge was: incorporate blockchain in some way that's useful for us. And the team, of course, I think they explicitly said Ethereum, which had just launched. It was like 2015.

**[54:14] SPEAKER_00:** Right. Why not? Why not?

**[54:17] SPEAKER_01:** But yeah, banks really—of course they've stuck around. Some other ETFs and making loads of money off of blockchain assets, of ERC-20s that came from MISCoin, there you go, and started back—

**[55:00] SPEAKER_00:** Okay. Well, which is also an arguable thing, what is it to say that the origin of something—

**[55:09] SPEAKER_01:** Well, everything's built on top of everything else, right? It's all just ideas.

**[55:14] SPEAKER_00:** Maybe that's a good place to wrap up.

**[55:16] SPEAKER_01:** Sure.

**[55:17] SPEAKER_00:** Thanks so much.

**[55:18] SPEAKER_01:** Yeah.

**[55:19] SPEAKER_00:** So you're very welcome. And ethereumclassic—sorry, ethereumhistory.com, yes, is the site for people to go to. So we've got a call to action to get people to come and have a look. You can sign up with Google.

**[55:45] SPEAKER_01:** GitHub, create an account simply with your wallet, you can create an account with a fake email, it doesn't matter. The idea is just to come in and help document old contracts. Whether that's you're just—there's somebody who's helping out a lot right now who's just spending his time during work because he's bored, telling his AI friend to help document. He's doing great work. He's cracking all these early contracts. So if anyone's interested in just spending some time helping research and adding and documenting, you can just do it without any approval.

This sort of Wikipedia of Ethereum will solve itself, with imperfection, over time. It won't tell the right stories, of course, if you're malicious and you're trying to just mess everything up, so please don't join if that's your goal, because we're trying to document Ethereum's history accurately. But yeah, it'd be great if it takes off. I mean, I think it really is something that doesn't exist anywhere else and should have utility for people over time as it gets filled out.

And I do have this vision, I didn't say earlier, I have ideas already, I've already sort of formulated the contract, of putting it on-chain. Basically hashing the JSON of whatever content we want to keep and then pushing the hash on-chain so it's not an insane amount of money that needs to be deployed each time there is a change. But those things are difficult because of the monetary aspects of it. But it makes sense that something about Ethereum should have Ethereum involved.

**[57:28] SPEAKER_00:** I'm going to get the ouroboros, the snake eating itself.

**[57:32] SPEAKER_01:** Exactly.

**[57:33] SPEAKER_00:** Until it's all everything, because every time that you push one of your hashes on, then you've got to push the hash of the hash of the hash. It never ends, right?

**[57:44] SPEAKER_01:** That's true.

**[57:45] SPEAKER_00:** Because you—

**[57:46] SPEAKER_01:** You're right. Okay, that's a good point.

**[57:49] SPEAKER_00:** It can never end. It will grow until the whole of the chain is taken up by the hashes.

**[58:04] SPEAKER_01:** Which is poetic, in a way, that Ethereum should be taken up by Ethereum.

**[58:12] SPEAKER_00:** Okay, well, thanks so much.

**[58:14] SPEAKER_01:** Thanks, Bob.

**[58:16] SPEAKER_00:** All right, thank you. I hope the audio is okay. I've noticed there was buzzing, like the air con was a bit noisy at times, but then it stopped. Yeah, if it doesn't work, we can always—

**[58:31] SPEAKER_01:** You.