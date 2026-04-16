**[00:05] SPEAKER_00:** So, yeah, I mean, I guess too long. Yeah. Okay. Welcome to Early Days of Ethereum. I'm here today with Cartoon for a rather different kind of topic, an episode than normal because—

**[00:26] SPEAKER_01:** The Late Days of Ethereum is what it's called. The Late Days of Ethereum.

**[00:31] SPEAKER_00:** Right, from the late days because, yeah, you know, normally I'm talking about the sort of social history of OGs and their memories at the time and everything, but you have had a rather different focus of this on-chain history.

**[00:52] SPEAKER_01:** Yeah, yeah, no, thanks for having me on the show. You know, I've been, as you know, a very big fan of your work. And you know, I am not, as you said, an Early Days of Ethereum person, but, you know, I think that this project that I think we'll talk about is, you know, in ways a celebratory adventure of the efforts of the folks who are worthy of this actual channel that you have. This really is an Ethereum effort. So, yeah.

**[01:27] SPEAKER_00:** So I mean, how did you yourself sort of get involved with Ethereum and this on-chain thesis?

**[01:35] SPEAKER_01:** So my Ethereum story, honestly, it started through investing, like probably many others. It came on during the boom. I kind of ignored all of the early nudges and articles I read to the exciting technology of blockchain and where it could go. Kind of, everything was focused in 2010 to 2013 about how you're either in it, which was the view, or it's absurd and speculative, and everyone's going to lose their money and they're gambling and whatnot. So I kind of jumped on that bandwagon, was interested, but on the side, never really dove in. And you know, even at 2012, a coworker of mine was mining Bitcoin in his aunt's closet.

**[02:38] SPEAKER_00:** Right.

**[02:39] SPEAKER_01:** And was telling me about it and was very adamant. I respected the guy. I'm a good friend and I respected him a lot. And so I guess I look back at that as like, what were you doing? Why didn't you just listen? But he was telling me, "Hey, you should keep an eye on Ethereum as well." And you know, when I didn't, I went to grad school during Devcon 1. Actually, I think I was telling Alex van de Sande that one of my classmates spoke at Devcon 1, which is really cool, but again, I just didn't jump in.

And then I didn't inevitably jump in until early 2021, I think, or late 2020 or something, when everything started popping off and I saw some absurd tickers on this app called StockTwits, which at the time I was kind of interested in over-the-counter stocks.

**[03:44] SPEAKER_00:** This sort of GameStop era.

**[03:47] SPEAKER_01:** It was around the GameStop era. Yeah, there were all these absurdities. The PancakeSwap era. Actually PooCoin, which was the platform where every absurd ticker at the time, like Butthole Coin or whatnot...

**[04:02] SPEAKER_00:** I think it was ButtDoge.

**[04:04] SPEAKER_01:** Yeah, ButtDoge, it's all Binance chain.

**[04:07] SPEAKER_00:** Right.

**[04:08] SPEAKER_01:** And one of them, you know, I saw these tickers go 5,000 whatever percent. It flashed at me and I was like, okay, I've got to try one of these. And so I got in, but that led me to, "Okay, what am I actually buying?" And then started to look into when ERC-20 at that time was already established, the standard and whatnot, of course. But so I looked into that and, you know, Binance Smart Chain, they just took the ERC-20 contract and repurposed it.

**[04:42] SPEAKER_00:** So BEP-20, is it BEP-20?

**[04:46] SPEAKER_01:** Yeah, it's ERC-20, I think. I think you're right. Exactly. And then if you look up their dictionary, it says, this is just ERC-20. Yes, but the code is of course exactly the same.

**[04:56] SPEAKER_00:** TRC-20 on Tron.

**[04:59] SPEAKER_01:** Yeah, they're all just—yeah, there's a 20 on it all. Which is funny because, as we know, Fabian just made the pull request, the 20 pull request or something. But so anyway, yeah, that led me to contract development. I was interested in it. Went from fungible tokens to non-fungible tokens and got mixed up into an NFT project. I became their software engineer, per se, or dev, as I came to find out. All the terms of rugging and devving and whatever. Everyone was a dev and is a dev. Sorry to all.

**[05:42] SPEAKER_00:** We're all devs. With AI especially. We're all devs. Yeah.

**[05:46] SPEAKER_01:** Every single version of a dev. My parents are devs. They're all devs. But it was funny to me at the time. I was struggling to sort of keep track of all the vernacular and take anything seriously. Especially, everything was on Twitter Spaces at the time.

**[06:05] SPEAKER_00:** Right.

**[06:06] SPEAKER_01:** Everyone was establishing their voice on Twitter Spaces so that the word "rug" was probably said like five times... there's Rug Radio, which may not exist anymore.

**[06:16] SPEAKER_00:** Rekt. R-E-K-T.

**[06:19] SPEAKER_01:** My version of rekt. Yeah, I just got rekt.

**[06:21] SPEAKER_00:** Yeah.

**[06:24] SPEAKER_01:** So I became this NFTs developer and I was developing all these different smart contracts. I found a lot of creativity. Everything was a bit of a copy of what somebody else had done in this space and they were trying to push it.

**[06:40] SPEAKER_00:** This is for security, because they're well audited, you see. So it's a risk management strategy.

**[06:47] SPEAKER_01:** Yeah, there's no AI to check, so you just would copy somebody else's. And whether that meant copying already malicious code that was implemented or not. It was funny that actually, one of the contracts... so this NFT project that brought me in and wanted me to help with development, their first contract, they hired a Fiverr developer. And it turned out after we did the second contract and mutations and whatnot, it turned out that the original contract, which they hired this Fiverr person to do, they had rewritten the owner function such that the inherited function could actually jump in and take over anytime. They could pull the money that was in the contract, but it was hidden enough because it was on the inherited contract class, not the main one, that they didn't see. And I don't think anybody there was technical enough to even vet the contract, let alone that.

**[07:56] SPEAKER_00:** Well, it happened to Parity back in the day with a bunch of experts. So if you're just winging it, these things...

**[08:02] SPEAKER_01:** 100%. I mean, in my mind, because you were saying you copy these for security as a joke, I think that in my head at the time I was like, "Okay, there's this Fiverr game that's out there just telling everybody to deploy these contracts and then they're sharing the funds or something." But it very well might have just been somebody copy-pasted that from some GitHub repo. They weren't the scammer. They didn't even know they were.

**[08:29] SPEAKER_00:** They were just an infection vector for scams.

**[08:32] SPEAKER_01:** Exactly. The head dev at the time asked me, he said, "So what are the chances that we're going to get scammed here or whatnot?" I was like, "Well, take the funds out of this contract. It doesn't seem like they can do anything, but you know, there's other funds in there. In theory, this person could come in at any time." Do they know about the fact that they have edited this function in a way? Maybe not. So maybe they just copied it from someone else and ultimately their hand was forced because OpenSea actually maybe flagged them. Maybe somebody flagged it for them or something, and I had to then do a migration contract for them and stuff.

But all this development sort of was the seed of the interest for me. And then what led to Ethereum history was a few years later, probably in like 2024 or something for me. So pretty recently, or maybe 23, you know, probably 2023. Anyway, MistCoin popped up online and so this was actually post—there's this Relics group, this group of Discord friends that focus their time on collecting NFTs, old NFTs and old contracts, on not just Ethereum, but Ethereum to like...

**[10:02] SPEAKER_00:** Solana.

**[10:03] SPEAKER_01:** No, no, no, the Bitcoin one starts with C. They talk about—the one that was kind of like—

**[10:10] SPEAKER_00:** Oh, Inscriptions and Ordinals.

**[10:16] SPEAKER_01:** Not Ordinals, before. So, before Runes.

**[10:19] SPEAKER_00:** Oh, Counterparty. Super old.

**[10:23] SPEAKER_01:** And some of them don't like Counterparty NFTs because they're not really—it's all built and it only exists if you have this other...

**[10:34] SPEAKER_00:** Protocol client.

**[10:35] SPEAKER_01:** Right. So there's a debate and whatnot, but they basically collect these old things. And anyway, they reached out, they found MistCoin, and they're digging up old contracts.

**[10:50] SPEAKER_00:** So MistCoin was made as an example token for the Mist Wallet. Right?

**[11:00] SPEAKER_01:** Exactly. Yeah, yeah. So MistCoin was made by Alex van de Sande and Fabian Vogelsteller, who you know well, and you've interviewed. Fabian deployed it. But essentially they were, at the time, my understanding, developing a feature for the Mist Wallet, the Ethereum wallet.

**[11:20] SPEAKER_00:** Right.

**[11:22] SPEAKER_01:** To allow for anybody to deploy contracts. And so at the time, you know...

**[11:26] SPEAKER_00:** Deploy your own coin.

**[11:28] SPEAKER_01:** Yeah. Click this button. And within the feature there were templates. Right? So it was kind of like the first standard in a way. And it was, at the time the standard itself was being molded from before in the standardized repos. But this morphed—this was the current state of that morphed standard code.

**[11:52] SPEAKER_00:** Yeah. And that was still pre—

**[11:55] SPEAKER_01:** Pre-ERC-20 actually, exactly pre that. Whether it was the 20th commit or the 20th pull request, I'm not sure. We have to ask to check.

**[12:09] SPEAKER_00:** It's funny actually. The way that works is, issues and pull requests are from that same ordinality. So it doesn't mean it was the 20th pull request. It was the 20th issue or pull request that had been created. It can be either because they never have the same numbering, because that would be ambiguous. So it's the 20th time somebody either made a PR or issue or put in—

**[12:47] SPEAKER_01:** Any issue whatsoever.

**[12:49] SPEAKER_00:** Right. Anyone could just chuck any issue in a count. So a good number of the numbers never end up being anything. Right? They never land on a thing.

**[13:06] SPEAKER_01:** An issue that says, "Hey, I don't really like the color red."

**[13:09] SPEAKER_00:** Right. So like, if you look at EIPs now, you know, they're in the thousands, and it's not because there have been a thousand proposed protocol changes.

**[13:20] SPEAKER_01:** I see.

**[13:20] SPEAKER_00:** Okay, sure.

**[13:22] SPEAKER_01:** That's an interesting way of doing it. So yeah, EIP-20. So this was November 3rd when they deployed that feature. And MistCoin being the first one that they launched with it. Then Devcon 1, they talked about it a little bit.

**[13:40] SPEAKER_00:** Standards panels.

**[13:42] SPEAKER_01:** Standards panel. Simon de la Rouviere spoke about token standards itself. He was also one of the few who were helping mold this standard. And then a few days later, the 19th of November is when Fabian and Vitalik formally formalized this proposal.

**[14:10] SPEAKER_00:** Right.

**[14:11] SPEAKER_01:** Of a slight adaptation, change of the code of MistCoin. But really, this standard that they had been molding. And it was funny, recently I found through this Ethereum history digging, this digging of old contracts, a coin that Vitalik had deployed. And it wasn't immediately clear that it was a token, you know, because you have to really look through the bytecode itself. And since it was written in Serpent, you couldn't really decompile it.

**[14:44] SPEAKER_00:** Oh, right, yeah, yeah, yeah.

**[14:45] SPEAKER_01:** If you tried to decompile it with the decompiler on Etherscan, it didn't really work well. And so you can't really tell on the surface, anyway. If you look through the bytecode, though, itself, and you're just raw looking at it and analyzing it, which is much easier to do now with AI, you could tell it's a token.

**[15:04] SPEAKER_00:** Right.

**[15:05] SPEAKER_01:** And it turned out it's actually this currency that he had deployed in the dapp-bin repo in September, or earlier maybe, September 8th or something. I don't know, but—

**[15:18] SPEAKER_00:** Right.

**[15:18] SPEAKER_01:** But what I thought was interesting, after I had sort of found the exact Serpent code and proven that, hey, this compiles with this version of Serpent to this exact bytecode, and I posted about it, Vitalik actually commented on it as well on Reddit. And he didn't answer this question—so if he hears this, hopefully he responds—but what I was wondering is, he deployed this days before, I think it was maybe November 6th, but days before he went and co-published the proposal standard, and it's sort of what he would have wanted as a token. I don't know, it was his early proposal in a way. And I wonder if that was his sort of way of immortalizing, "Hey, I like this thing we ended up going with, I'm going to immortalize mine on-chain, you know, I like my way better" type of thing. So that's how I like to imagine it. But it's there, and one day maybe Vitalik will decide, "Hey, everybody should have my unnamed coin," and there's a million of them and he hands it off and they're at zero decimals.

**[16:34] SPEAKER_00:** That's pretty random what people ended up pushing or not pushing and it's all—

**[16:41] SPEAKER_01:** Yeah, but there's only one. So I mean, I guess Vitalik doesn't make many mistakes and he probably even was using testnets or whatnot back then, but a lot of folks were testing...

**[16:51] SPEAKER_00:** In production! Like there's no economic value even, ha. Right, right. Why would you not?

**[16:58] SPEAKER_01:** Trading at cents to a dollar at that point, so yeah. Now you look back at it and you're like, "Oh yeah, I spent 10 ETH on that," but a lot of the contracts now that I feature for Ethereum History—I'm sure they'll introduce it...

**[17:20] SPEAKER_00:** Well, just before we get to that, so you spoke about MistCoin as sort of being where you'd started. So is that wrapped now? Is it wrapped? MistCoin, was that because it was slightly pre-ERC-20, does this coin need wrapping?

**[17:40] SPEAKER_01:** It needed wrapping. It doesn't have an approve function, it doesn't have a few other functions. It's one of the first named tokens that way, it's kind of special. And it doesn't adhere to the current standards such that if you tried to create a Uniswap pool for it, it wouldn't work. There's no approve, transferFrom, or methods that it needs.

**[18:15] SPEAKER_00:** Yeah, it's just it's not going to move.

**[18:17] SPEAKER_01:** It's not going to move. So essentially, if you wanted to make it credible... which at the time, so this group, this Relics group had found it. They found a MistCoin DAO that Alex had made. And once they acquired some of the MistCoin they were given, I think from both Alex and Hudson, if I'm not mistaken.

**[18:41] SPEAKER_00:** Right, right.

**[18:43] SPEAKER_01:** They then were able to also pull more MistCoin from this DAO. So I think Alex had put in 100,000 MistCoin, which is like 10% of the entire supply, into this DAO. So they took that out. And then they used it, they gave it out to a lot of folks in their community of early NFTs. They kind of framed it as, "Hey, this is going to help early NFTs and we're just going to help boost our community." And they were into that. And so there is now a DAO that holds, I think, maybe 4% of the supply of 40,000.

**[19:25] SPEAKER_00:** Right, right.

**[19:26] SPEAKER_01:** And the rest was kind of given up to all their folks. And so when I bought it, you know, I bought it, I was a sucker. I bought it at like $50 or something. I was like, cool, I can own this thing like everybody else, you know. By the time it reached my timeline, it's too late.

**[19:44] SPEAKER_00:** Right.

**[19:44] SPEAKER_01:** Lesson for everybody. Or at least at the time when everything was popping off. But, yeah, so they probably did very well. But they're also, you know, besides that they are this group which, you know, I can't say I'm seriously part of, but they very much care for these older relics, specifically non-fungible tokens. So they're very much into that, which is cool as collectors.

So MistCoin led me into this interest in early contracts. And once I started to dive into the story of MistCoin itself and what Fabian and Alex were doing at the time, and how it was the beginning of basically everything that moves Ethereum today. Everything that people are interested in from an external perspective, from the tokenization of finance and whatnot, it all stems from the need for there to be a standard. And all that just sort of led me to say, "Okay, well what else is out there? What else was happening at the time then?"

**[21:02] SPEAKER_00:** Right.

**[21:04] SPEAKER_01:** That is either interesting today or will be interesting later. And can we sort of uncover that now? And so while I was writing a website for MistCoin and helping with any engineering projects that we needed to tell that story, on the side, I started to download all of the contracts on 2015 and then 2016, and perused through the bytecode. This was before AI and all these LLMs were out there. So I was really just using decompilers like Python decompilers, and I was running similarity text algorithms to try to figure out, okay, what is the likelihood of this being a token or this being an ownable, or this being fungible or this being something? I'd look at deployer addresses, known deployer addresses, that type of thing. But it was much more—it was a much more difficult assessment than it is now.

**[22:15] SPEAKER_00:** It's almost like a reverse engineering kind of discipline. You've got this, it has been a lossy thing, right? You know, that compilation process, it's not intrinsically reversible. You've got that data loss and you've got these patterns. But, you know, no blockchains ever die. Caveats compiled.

**[22:42] SPEAKER_01:** Exactly. Yeah, it would be really great if it was possible to make Ethereum in a way that you could actually just store all the code itself and not have to do the bytecode, of course. Not feasible.

**[22:58] SPEAKER_00:** I'll tell you what funny little thing actually is, STRATO, that I'm working on, that actually does happen for our chain because it has an alternate VM called SolidVM, which is an EVM as well, but it's actually an interpreter.

**[23:18] SPEAKER_01:** So.

**[23:19] SPEAKER_00:** So what you have is you do have source code on-chain which gets deterministically interpreted. So it's almost like you've kind of got Etherscan built in.

**[23:32] SPEAKER_01:** And you don't have any issues with having to transmit large chunks of data through consensus?

**[23:40] SPEAKER_00:** No, it's been okay. I mean, yeah, you couldn't do that at huge scale in a completely permissionless validator scenario.

**[23:54] SPEAKER_01:** But it's still interesting to work with.

**[23:57] SPEAKER_00:** There's an alternate universe.

**[24:01] SPEAKER_01:** Different things have been chosen to explore that. Yeah, because, you know, like you said, it's been a challenge. I didn't even really attempt—there was a few attempts. There's this person who has done a lot of work in trying to exactly prove the MistCoin code and eventually did through the help of a couple of others. But it's a guessing game, you know. At a certain point you're trying to guess the order of functions, the functions themselves, the method names, and you get to a point where you get close, but so many things could go wrong. You know, there's so many possible permutations, there's the compiler version, there's the settings, there's the naming of the functions. In some cases even now with LLMs, it has made it impossible. Because, you know, in one contract for example, I'm down to just this one function name and I know that it is more than 10 characters long, because I've tried every possible 8, 7, 8, 9... So I literally had this machine running on my computer just chugging through everybody. And at first it wasn't even doing anything intelligent, it was literally going, a, a, b. You can't actually do that once you get to the higher character count, it would take forever. But I just gave up because what's the point? I mean, you know what the function does and so you'll see on Ethereum History some say "near exact bytecode" and I'll actually indicate how close it was, because I'd give up at a certain point.

**[25:53] SPEAKER_00:** Because as long as you have the exact functionality and you're pretty close to complete... the bytecode is off by a few segments, then what would matter?

**[26:07] SPEAKER_01:** I mean, I guess, you know, there's probably a decent amount of the source code is probably on GitHub somewhere.

**[26:14] SPEAKER_00:** That's another tactic.

**[26:16] SPEAKER_01:** So yeah, when I'm doing this sort of what I've called "cracking"—and there's an Ethereum History cracking skill and whatnot out there—but one of the approaches is researching. So just going off to Reddit and to GitHub and trying to find the contracts, or contracts that are similar. Even back then folks were doing—somebody would do something and another person would make a slight adaptation to it. Whether that's naming this function something slightly different, and now I can't guess it. But in this case, literally everything else was published somewhere.

**[26:55] SPEAKER_00:** Yeah, somewhat, somewhere, somewhere when somebody said...

**[26:59] SPEAKER_01:** Yes, but you find it through, you know, keyword searches on GitHub and stuff that shows up.

**[27:04] SPEAKER_00:** Right, right. Yeah, yeah, yeah.

**[27:07] SPEAKER_01:** It's definitely a great tactic. And it shows, you can document everything on Ethereum History, but still, it's great to know that they're fragmented out there. As long as the Internet is around, there are at least other folks documenting in time. Thanks to the Internet Archive, even some things that have been removed are still out there. And one of the things I was pretty disappointed about, and maybe they'll bring it back one day is, Ethereum took down last year or two years ago the standards, the standardization requirements repository. So it's literally this one GitHub repository that they just kept track, this wiki, they kept track of all of the different standard commits as that progressed for tokens.

**[27:59] SPEAKER_00:** So this was a wiki within a given GitHub, Ethereum something.

**[28:05] SPEAKER_01:** Yeah. And so a lot of the commits are still there on Internet Archive, and some folks had forked it at different junctures so you can kind of find it at different stages.

**[28:16] SPEAKER_00:** Right, right.

**[28:17] SPEAKER_01:** But I don't know what's the purpose of taking it down? I mean, I think they probably had some reason, maybe they didn't want to add confusion or something, but yeah.

**[28:29] SPEAKER_00:** Or sometimes it can just be completely in ignorance of the consequences, that it's just somebody cleaning up.

**[28:35] SPEAKER_01:** Right.

**[28:36] SPEAKER_00:** Or whatever.

**[28:38] SPEAKER_01:** Yeah. So I mean I would imagine hopefully that somebody at Ethereum has that, that they sort of downloaded the repo over time and can stitch it back together.

**[28:49] SPEAKER_00:** So for the history of the white paper, post Polar has done a lot of digging into those details, but it was only through him I realized that you had got some of those Internet Archive versions of the old wikis. I thought they were like all way beyond, like a very long time ago.

**[29:14] SPEAKER_01:** Yeah.

**[29:15] SPEAKER_00:** So it was kind of fun that those are still on the Internet Archive.

**[29:19] SPEAKER_01:** Another, and you probably remember this, but another thing I found on the Internet Archive is around that time, like 2015, there was a bulletin that was kept up by somebody in Ethereum.

**[29:32] SPEAKER_00:** Okay.

**[29:32] SPEAKER_01:** It was basically a forum where you can ask questions, but it was all seemingly self-hosted.

**[29:41] SPEAKER_00:** Oh, just the Ethereum forum.

**[29:43] SPEAKER_01:** I think it was the Ethereum forum. And yeah, people were talking and it had its own message threads.

**[29:49] SPEAKER_00:** Yeah, yeah. So that was a Discourse. I think it's Discourse, the software is. But yeah, that wasn't used for very long, like Reddit became a lot more popular. But then I remember there was a whole bunch of drama about, "Oh, we're going to shut the forum down, are we not?" And then it was like, "Oh well okay, maybe somebody in the community wants to maintain it." Yeah. But then it's like, "Oh, but you can't because you'd be giving over the database that would have all the DMs in it." So I think Hudson kept maintaining it for quite a while.

**[30:30] SPEAKER_01:** I don't know if it did ultimately because, yeah, I mean, it would be interesting. There was definitely at least one contract that through the Internet Archive, I could see that I was about to get some important information on it and then it's just gone. So some of these ventures into trying to document some of these contracts go quite deep into these Internet archives and they're not easy to peruse through. But you get into those old things that have been taken away and it's exciting because it kind of feels like you're digging into something that nobody knows anymore.

**[31:16] SPEAKER_00:** Yeah.

**[31:17] SPEAKER_01:** And that's what's kind of kept me going. That, and it seems like people are genuinely excited. You know, I don't know, it's a small group, and obviously I only have Reddit and those folks who are still on Twitter to speak to this. I wish there were other avenues, but there is a decent community of folks that still reminisce and still want to know about it. And they'll look at the history and the first programmable blockchain, what the early days were like, and not just from people's perspective, but the actual contracts.

**[31:58] SPEAKER_00:** So I mean, your site is ethereumhistory.com, so what features are there? What can people see if they visit that?

**[32:09] SPEAKER_01:** So my short elevator pitch is: Wikipedia of Ethereum smart contracts. So the idea is, Etherscan itself is great. Etherscan tells you all the facts about every contract that they can find on-chain, you know, and you can see, of course, the bytecode. You can see the code if they verified it or not. But there's very hard restrictions on how you can verify it.

**[32:38] SPEAKER_00:** Right.

**[32:39] SPEAKER_01:** And they only support up to a certain 0.4.3 or something version of Solidity.

**[32:48] SPEAKER_00:** Right. So like probably the version when they started. Probably.

**[32:52] SPEAKER_01:** Yeah, yeah. You can't go further back. So anything early you can't really verify. But beyond that, actually adding any descriptions or tags or anything is very difficult on Etherscan. So it's really not meant to add any meaningful documentation to a contract. It's really just there to say this thing exists. And outside of that, there's nothing popular or nothing I could find that has any sort of purpose of recording the history like a Wikipedia would. Of course, there's some projects that have gotten to the point at which there is a Wikipedia page for that.

**[33:30] SPEAKER_00:** Yes.

**[33:31] SPEAKER_01:** And it will probably just link to Etherscan or show their contract address, which doesn't mean much, people really just trust that website. Yeah. So basically, where's the home for this Wikipedia? Where's the home for folks who are interested in Ethereum to learn about those early contracts, learn about the story behind them, and look at the original code itself? Not look at the bytecode, but let's look at the actual code. And I think there's two different things that people can take out of that. One is if you're interested in the stories, you can go back and see the qualitative stories. They're not always going to be accurate because every story is a snapshot of what somebody remembers and tells one other person. And your memories are of course just fickle and perhaps might not be exactly right. But hopefully, with the idea of Wikipedia, everybody sort of edits it over time and it becomes this hive mind that gets perfected. It's very efficient.

So anyway, right now the Ethereum History is not exactly efficient because there are 18 different historians, of which the users are called historians, but of which four have documented contracts.

**[35:02] SPEAKER_00:** Right. So you know, after a slow takeoff, after—

**[35:05] SPEAKER_01:** Everybody watches this video, everyone signs up, it's free. But so one thing you can take away is the stories, and then the other thing that you can take away is actually reading the code of all these early contracts. And the vision I have there is once we do get the code, I want to find of every or most of these contracts, which we're making pretty strong headway on right now, I want to find a way to represent that in some sort of visual in my head. I don't know how this is going to work out, but I picture like archaeology, like rocks, you know, the way that you can look through the layers of the earth and history.

**[35:51] SPEAKER_00:** Right.

**[35:52] SPEAKER_01:** Some sort of visual representation of that, but through code functions or methods. I don't really know, it's a loose thought in my mind, but I would love to use something...

**[36:03] SPEAKER_00:** With a scrubby timeline somehow that changes shape somehow.

**[36:09] SPEAKER_01:** Yeah. I'm interested, what sort of stories, what can we learn about the reuse of different types of methods and how they—and then maybe the popularity of the contract itself, the amounts that it's been used, which you could discern by the number of times it's been replicated or the number of transactions that have occurred. So the popularity of them, and then how long that has lasted over time, and what that looks like.

**[36:40] SPEAKER_00:** Species coming to life and dying off and—

**[36:43] SPEAKER_01:** Yeah, exactly.

**[36:45] SPEAKER_00:** "Look at that dinosaur technique that literally is a dinosaur technique that's not used anymore."

**[36:51] SPEAKER_01:** And it's a hard thing too. It's a hard thing to keep track of because a method has a purpose and it has a name, but it's meant to do something. It might do several things. It might be part of a larger set of goals of functions that are calling it and whatnot. But if you're trying to find a thread through history, you might want to look at—you're dealing with a semantics problem as well, because it kind of like it doesn't have to be the exact method, but that same purpose, and has it—

**[37:24] SPEAKER_00:** Yeah.

**[37:24] SPEAKER_01:** Gotten hardened or worse or better over—

**[37:27] SPEAKER_00:** You're sort of wanting to infer design patterns out of it or something, or higher literal higher level patterns or reasoning or, you know...

**[37:40] SPEAKER_01:** Yeah, yeah, yeah. Hopefully that is possible. And it's sort of a loose thought in my mind. I don't know. We'll see what people want to build. You know, it's an open source project, so hopefully folks will add their own pull requests or issues, and I'll mark them as proposals, EIPs, regardless of whether it's an issue or a PR, to EIP-1 if anybody wants. There haven't been a lot of pull requests since I just go straight to main.

**[38:16] SPEAKER_00:** Right. Just straight to commit. We're going.

**[38:20] SPEAKER_01:** But yeah, that's the code, and the stories are kind of the angle now. And the other angle I have, so I got into downloading all of the 2015 to 2017 contracts, decompiling them all, right? Loading them up into this database, and then on top of it I've added these indices on this database such that you can query through all of the decompiled code. And the goal there was, anybody should be able to find interesting things through the code. Maybe somebody's interested in mining or they're looking for the first time that the word "cat" was written somewhere. The decompilation won't be perfect. It might not have the actual first cat, but there's a chance that it does. And this gives them the ability to search through text rather than just bytecode. So that was the first idea. Now what happens is, every single time a contract is "cracked," as I call it, to solve the exact code with compiling settings, that gets added to the index as well. So you actually search through that code. It sort of improves that discoverability.

**[39:35] SPEAKER_00:** So what kind of different existing tools have you been using or found useful for...

**[39:41] SPEAKER_01:** For cracking and for researching?

**[39:44] SPEAKER_00:** Yeah, and disassembling.

**[39:47] SPEAKER_01:** So the disassembling has been interesting, this whole cracking thing. It depends on the contract. The first thing I'll do is—and of course, all of this I heavy usage of AI here. Yeah, yeah. My AI overlord is helping me out every day. But the first thing I'll have to do is just go through and see, hey, through my—I have this Ethereum History researcher skill that just goes through GitHub, Reddit, and tries to find... First it will decompile it, or use the decompiled code I have already, and try to find anything that resembles it in GitHub or Reddit at the time. And if it finds a match or it knows of some match, it obviously has its inherent knowledge already of the time these things were out there or published, then it will start there. So it's mostly about finding a starting point, if not the exact code. Sometimes it is the exact. Sometimes it's a very reused wallet of the time or something.

**[40:50] SPEAKER_00:** Yeah.

**[40:52] SPEAKER_01:** So it's establishing a starting point and then from there it's taking the different versions of Solidity at the time. Or it will try to, you know, is it Serpent or is it LLL or whatever.

**[41:07] SPEAKER_00:** It might have some Mutan.

**[41:09] SPEAKER_01:** I haven't found it.

**[41:10] SPEAKER_00:** No Mutan, not yet.

**[41:12] SPEAKER_01:** Honestly, so far, only Serpent. And there's two: Serpent, Solidity, of course. And then in some cases, it's just straight bytecode that they deployed, so as far as the AI could discern, there wasn't actually any code, they just created the bytecode themselves and launched that.

**[41:39] SPEAKER_00:** Strange, because I thought you always had LLL in the line, or maybe this was only for Solidity. So I think for Solidity, it was always built on top of LLL at the start, kind of using LLL as an assembler. But yeah, I mean, Jeff was working on Mutan up almost until launch, so it might be that there's hardly any Mutan on mainnet, like probably a bunch of that on Olympia.

**[42:19] SPEAKER_01:** I hope I find something that would be interesting. Yeah. For the ones that it discerned were all done in straight bytecode, they used Yul, I think or something. It's something somewhat recent, like 2018. Yul, yeah.

**[42:40] SPEAKER_00:** Though who was it I was talking to, was it? Oh, that was... yeah, I did an interview with Alex 'axic' Beregszaszi, who was Solidity co-lead for many, many years. So he was saying that started, it was called Julia at first. Like Julia. Yeah, but with a J I think. But then there's some other computer language called Julia already. So then that changed into Yul, which is a kind of an intermediate representation in that the goal was that Solidity would compile to Yul and then you would have a further compilation step on the back of that.

**[43:42] SPEAKER_01:** Interesting.

**[43:42] SPEAKER_00:** Well, hopefully. So I guess it kind of ended up being a bit like an assembler.

**[43:51] SPEAKER_01:** Hopefully they're proud to know that AI is still referring to their work, because for those few contracts that did choose to represent them in Yul, right, there you go. Cool. Yeah, so that's there. And so this part of it's research, part of it is sort of narrowing, chipping down, if you will, to this bytecode. In the process, of course it takes the time at which this was deployed. So the different versions of Solidity that were out there at the time. And you just try to—it's a trial and error type of thing on both sides.

**[44:36] SPEAKER_00:** There's no metadata that ends up of the Solidity version in the final bytecode?

**[44:43] SPEAKER_01:** I think, correct me if I'm wrong, I think metadata started a bit later. There was a particular version of Solidity that... and I want to say that because that became a thing as the person who leads Sourcify, right, reached out and has been really great. He's been helping. He expanded Sourcify such that it could go down to much earlier versions of Solidity. So I've been verifying on Sourcify and also adding all the methods that we uncover so that they're there for the world.

**[45:25] SPEAKER_00:** And what does Sourcify do exactly?

**[45:28] SPEAKER_01:** I'm going to butcher this, but sorry. But they seem to be the registry of not just methods that have been ever deployed on the blockchain—so a way to sort of collect all that knowledge and make it accessible to everybody—but also to verify the actual source code of any particular contract.

**[45:57] SPEAKER_00:** Right.

**[45:58] SPEAKER_01:** So it seemed to be something that you would do going forward for a lot of time, if I understood it correctly. But then they started to also go backwards, backwards and allowing...

**[46:07] SPEAKER_00:** So kind of taking that functionality that you had within Etherscan, but pulling that out into a component that can be used.

**[46:19] SPEAKER_01:** Exactly. Yeah. Maybe the idea was Etherscan would want to just replace it with Sourcify. But yeah, I've pinged Etherscan a few times, especially as I started to validate or crack a bunch of these earlier contracts that I could not verify. Essentially the way that you would verify on Etherscan for these older contracts is you would reach out to support at Etherscan.

**[46:48] SPEAKER_00:** Right?

**[46:50] SPEAKER_01:** Yeah, respond. And for MistCoin, we had to go through somebody who knew somebody who was there and eventually that person reached back and said, "We're going to help you get this verified." But I cold emailed a bunch of these and they're really interesting. I mean, they still haven't validated, for example, Gav. GavCoin.

**[47:09] SPEAKER_00:** Right.

**[47:11] SPEAKER_01:** Vitalik's currency. You know, these are arguably very interesting and novel contracts from arguably very important people in the space. And they still haven't. So I got this sort of blanket response that was, "Thank you, but you need to be the deployer. Are you the deployer? Would you like to sign this transaction?"

**[47:37] SPEAKER_00:** Sign this transaction?

**[47:39] SPEAKER_01:** I was like, "Sorry, I'm not VB, I cannot sign it." But somebody did reach out on Twitter and said, "Hey, yes, sorry about that. That's our blanket response. And here, actually, we helped verify one." And it was one of these Peperium... Peperium is like, I think from 2017 or so, an NFT-like contract. Like, I think it's more of a fungible-like token, but in some way they added metadata onto it such that there's an image.

**[48:21] SPEAKER_00:** This is not Piper Merriam.

**[48:24] SPEAKER_01:** No, no, it's not Piper. That would be hilarious if this was Piper.

**[48:33] SPEAKER_00:** Right?

**[48:33] SPEAKER_01:** Yeah, they roll off the tongue the same way. Peperium. I think it's more about Pepe. Every one of them, I think, has some sort of picture of Pepe.

**[48:45] SPEAKER_00:** Right.

**[48:46] SPEAKER_01:** But anyway, so the Etherscan person verified that one out of all the ones that I sent and I was like, "Verify one of the ones I care about! Verify one of the top ones." I don't want to say I care one way or another, I'm sure a lot of people care about it.

**[49:06] SPEAKER_00:** So Gav must have deployed GavCoin onto Olympia and onto Frontier then, separately.

**[49:12] SPEAKER_01:** Oh, I'm sure. I'm sure he did on Olympia. Must have, for fun, right?

**[49:18] SPEAKER_00:** Well, because there was the talk I found, which was August 2014, I think, with Jeff in London doing the DEX, demonstrating their DEX. That's right. That's it. Gav's saying, you know, he values GavCoin...

**[49:48] SPEAKER_01:** Which I have yet to find JeffCoin, so.

**[49:51] SPEAKER_00:** No, well, maybe JeffCoin only ever made it out onto Olympia. They're in Mutan, and Gav was running LLL.

**[50:06] SPEAKER_01:** Yeah. So, you know, I can't prove that GavCoin, the one I found, was deployed by Gavin himself.

**[50:13] SPEAKER_00:** Right.

**[50:14] SPEAKER_01:** But I have a chain of information, a thread of different events that seem to have a strong case. Maybe Gavin will listen to this and decide to tell the whole world that it just was deployed by him.

**[50:33] SPEAKER_00:** Probably forgotten all such things many years ago.

**[50:36] SPEAKER_01:** There's another theory I have where it could have been potentially deployed by that Roman, the person who ran that, Roman Mandeleil. Yeah, man.

**[50:47] SPEAKER_00:** Which was EtherCamp.

**[50:49] SPEAKER_01:** I wasn't around, so I don't really know. I mean, I know Piper, I think, did some work with EtherCamp at the time, and I believe so. I don't really know that for sure, but those are things I read.

**[51:15] SPEAKER_00:** Right.

**[51:16] SPEAKER_01:** Oh, so that's why I think it might be potentially deployed by him, because I think that the deployer might have also deployed Hacker Gold.

**[51:20] SPEAKER_00:** No, if it was Hacker Gold, that would have been Roman. Yeah, for sure.

**[51:24] SPEAKER_01:** So then maybe this was Roman. Yeah, I don't know. I have to look. I forget now. It's been a long time of looking at other contracts and following the deployer thread, but I found some connection to Hacker Gold as well. So maybe Roman wants to tell the world about it. I don't know if anybody talks to Roman anymore.

**[51:45] SPEAKER_00:** I used to be Facebook friends with him, but then he seems to have gone off that as well. But yeah, he basically disappeared in 2017, really?

**[51:55] SPEAKER_01:** But he was around... I kind of, as I understand, some of the firsts might have been from him.

**[52:03] SPEAKER_00:** He's quite a character. One of the things that EtherCamp did, which is unbelievable at the time, let alone now, is they, at Devcon 2 in Shanghai, so October 2016, this was, they did this demo called CashETH with Banco Santander and it was basically a stablecoin on Ethereum in-browser. So it was sort of like you got some kind of MetaMask-y thing for doing... like sending stables in a browser on Ethereum. It was very novel at the time. Also very surprising that they did it with Roman, because he was a bit—a bit eccentric or erratic, shall we say. He did not come across as the sort of person that you'd be doing a banking...

**[53:20] SPEAKER_01:** No, but it was Banco Santander and not JPMorgan.

**[53:24] SPEAKER_00:** I guess so. But...

**[53:26] SPEAKER_01:** Sorry, but.

**[53:28] SPEAKER_00:** But, you know, that was happening all that time back. Yeah.

**[53:32] SPEAKER_01:** That's cool. Yeah. No, it's interesting. I feel like in the beginning, in the early years, banks were very interested in Ethereum. I think there were some sponsors for Devcon 1.

**[53:44] SPEAKER_00:** Yeah.

**[53:45] SPEAKER_01:** In grad school where I was, there was certainly UBS. Yeah, I think JPMorgan might have been. So we had these—it was MBA school and we had these challenges that companies would come in and propose concepts to, and the engineering and the business school students would come up with solutions to these challenges and in the form of products or companies or ideas. And the banking one was blockchain. And basically the challenge was: incorporate blockchain into our—in some way that's useful for us.

**[54:26] SPEAKER_00:** Right.

**[54:27] SPEAKER_01:** And the team, of course, I think explicitly said Ethereum, which at the time just launched. It was like 2015.

**[54:36] SPEAKER_00:** Right, right.

**[54:40] SPEAKER_01:** But yeah, banks are really, of course they've stuck around, so now they're doing their ETFs and making boatloads of money off of blockchain assets of ERC-20s that came from MistCoin.

**[54:56] SPEAKER_00:** There you go. And started back there.

**[55:00] SPEAKER_01:** Yeah.

**[55:00] SPEAKER_00:** Okay.

**[55:01] SPEAKER_01:** Which is also an arguable thing. What is it to say that it came from MistCoin as the origin of something?

**[55:11] SPEAKER_00:** Well, everything's built on top of everything else. Right. It's all just ideas. All right, well, maybe that's a good place to wrap up.

**[55:21] SPEAKER_01:** Sure.

**[55:23] SPEAKER_00:** Thanks so much.

**[55:24] SPEAKER_01:** Yeah, thanks for having me on.

**[55:26] SPEAKER_00:** You're very welcome. And Ethereum History, yes, is the site for people to go. And so we've got a call to action to get people to come in, come and have a look.

**[55:41] SPEAKER_01:** You can sign up with Google, GitHub, you can create an account just simply with your Ethereum wallet. You can create an account with a fake email, it doesn't matter. The idea is just to come in and help document old contracts. Whether you're just, you know—there's somebody who's helping out a lot right now who's just spending his time during work because he's bored, calling in his AI friend to help document. He's doing great work. He's cracking all these early contracts. And so if anyone's interested in just spending some time helping research and adding and documenting, you can just do it without any approval. And this sort of Wikipedia of Ethereum will sort itself out in perfection over time. We'll tell the right stories. Of course, if you're malicious and you're trying to just mess everything up, please don't join, because we're trying to document Ethereum's history accurately.

But yeah, it would be great if it takes off. I mean, I think it really is something that doesn't exist anywhere else and should have utility for people over time if it gets filled out. And I do have this vision—I didn't say it earlier—I have this vision, and I have ideas already, I've already sort of formulated the contract, but putting it on-chain so that, you know, basically hashing the JSON of whatever content we want to keep and then pushing the hash on-chain so it's not an insane amount of money that needs to be deployed each time there is a change. But...

**[57:18] SPEAKER_00:** Right.

**[57:18] SPEAKER_01:** Those things are difficult because of the monetary aspects of it. But it does make sense that something about Ethereum should have Ethereum involved.

**[57:28] SPEAKER_00:** We're going to get the Ouroboros snake eating itself.

**[57:34] SPEAKER_01:** Exactly.

**[57:36] SPEAKER_00:** Because every time that you push one of the hashes on, then you've got to push the hash of—

**[57:41] SPEAKER_01:** The hash of the hash of the hash.

**[57:43] SPEAKER_00:** It never ends, right? Because you...

**[57:45] SPEAKER_01:** That's true. Yeah. No, it has to be this... otherwise you lose the history, right, of the... yeah, you're right.

**[57:54] SPEAKER_00:** Okay.

**[57:54] SPEAKER_01:** That's a good point.

**[57:55] SPEAKER_00:** Can never end.

**[57:56] SPEAKER_01:** Never end.

**[57:59] SPEAKER_00:** It will grow until the whole of the chain is taken up by the hashes.

**[58:03] SPEAKER_01:** The hashes of the hashes. Which is poetic in a way, that Ethereum should be taken up by Ethereum history.

**[58:12] SPEAKER_00:** Okay, well, thanks so much.

**[58:14] SPEAKER_01:** Thanks, Bob.

**[58:14] SPEAKER_00:** Cheers. All right. Thank you. I hope the audio is okay. I noticed that was buzzing, like the aircon was a bit noisy at times, but then it stopped.

**[58:29] SPEAKER_01:** Yeah. If it doesn't work, we can always tell.