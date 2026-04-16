**[00:05] SPEAKER_00:** So yeah, I guess... okay, welcome to Early Days of Ethereum. Thank you. I'm here today with Cartoon for a rather different kind of topic and episode than normal because the "late days of Ethereum" is what it's called. Which, the late days, right? The late days, because yeah, you know, normally I'm talking about, you know, sort of social history of OGs and, you know, their memories at the time learning. But you have had a rather different focus on on-chain history.

**[00:53] SPEAKER_01:** Yeah, yeah, no, thanks for having me on the show. You know, I've been, as you know, a very big fan of your work. And um, yeah, I did... am not, as you said, an Early Days of Ethereum person. But, you know, I think that this project that I think we'll talk about is, in ways, a celebratory venture of the efforts of the folks who are worthy of this actual channel that you have and this Early Days of Ethereum effort.

**[01:23] SPEAKER_00:** So um, yeah, something... so, I mean, how did you yourself sort of get involved with Ethereum and this on-chain thesis?

**[01:31] SPEAKER_01:** So my Ethereum story, honestly, it started through investing, with many others. It came on during the boom of... you know, I kind of ignored all of the early pitches and articles I read towards the exciting technology of blockchain and where it could go. And kind of, you know, everything was focused in 2010 to 2013 about how you're either in it, which was the view, or it's absurd and it's for speculation, and everyone's going to lose their money and they're gambling and whatnot. So I kind of jumped on that bandwagon. I was interested, but on the side, and never really dove in. You know, I was even in 2012, a friend was mining Bitcoin in his aunt's closet, and he was telling me about it. He was very adamant. I respected the guy; I have a good friend, I respected him a lot. And so I guess I look back at that as like, "What were you doing? Why didn't you just listen?"

But he was telling me, "Hey, you should keep an eye on Ethereum as well." And at school, during Devcon 1, actually some of my classmates spoke at Devcon 1. I was telling Alex van de Sande that one of my classmates spoke at Devcon 1, right? But again, just didn't jump in. And then I inevitably jumped in until early 2021, I think, or 2020 it started popping up. And I saw some absurd tickers on this app called Stocktwits, which at the time I was kind of interested in over-the-counter stocks. This was the GameStop era.

**[03:45] SPEAKER_00:** It was around the GameStop era, yeah. There were all these absurd... the PancakeSwap era, actually.

**[03:50] SPEAKER_01:** Right, it's the PancakeSwap era, which was the platform where every absurd ticker at the time like, you know, Buckle coin or whatnot… I think it was BUTTIX. Yeah, BUTTIX was all Binance Smart Chain. I saw these tickers go 5,000 whatever percent every time they flashed at me, and I was like, "Okay, I've got to try one of these." And so I got in. But that led me to, "Okay, what am I actually buying?" And then I started to look into what an ERC-20... at that time it was already established, the standard and whatnot, of course. So I looked into that, and Binance Smart Chain, or whatever it's called, is just an emulation of Ethereum.

**[04:45] SPEAKER_00:** Yeah, yeah, just took the ERC-20 contract and repurposed it.

**[04:50] SPEAKER_01:** So the ERC-20 is… it's all just funny because, as we know, Fabian Vogelsteller made the pull request, the 20th pull request or something. But anyway, yeah, that led me to contract development. I was interested in it, and it went from fungible tokens to non-fungible tokens, and I got mixed up into an NFT project and became their software engineer, per se, or dev, as I came to find out all the terms of rugging and devving and whatever. Everyone was a dev!

**[05:30] SPEAKER_00:** And as a dev—sorry, we're all devs. Oh sorry, all the devs... With AI especially, we're all devs.

**[05:40] SPEAKER_01:** Yeah, yeah, every single version. My parents are devs, they're all devs. But it was funny to me at the time; I was struggling to sort of keep track of all the vernacular and take anything seriously. Especially, everything was on Twitter Spaces at the time, and everyone was establishing their voice on Twitter Spaces. So the word "rug" was probably said a lot... I think there's Rug Radio, which may not exist anymore.

**[06:05] SPEAKER_00:** Rekt. Oh yeah, rekt. It never was some version of rekt, yeah, just getting rekt.

**[06:10] SPEAKER_01:** Yeah. So I became this NFT developer, and I was developing all these different smart contracts. I found a lot of creativity was sort of... but everything was a bit of a copy of what somebody else had done in this case, and they were trying to push it.

**[06:40] SPEAKER_00:** And this is for security, because they're well-audited, so yeah, exactly. It's a risk management strategy.

**[06:47] SPEAKER_01:** Yeah, there's no AI to check so you just would copy somebody else's. And whether that meant copying already malicious code that was implemented or not, it was funny. I had actually one of the contracts... so this NFT project that brought me in and wanted me to help with development, their first contract was they hired a Fiverr developer. And it turned out, after we did the second contract and mutations or whatnot, that the original contract which they hired this Fiverr person to do, they had overwritten or rewrote this Ownable function such that they could... through the inherited function, they could actually jump in and take over anytime, right? They could pull the money that was in the contract. But it was hidden enough because it was on the inherited contract class, not the main one, that they didn't see. And I don't think anybody there was technical enough to even vet the contract.

**[07:56] SPEAKER_00:** Well, it happens apparently, back in the day, with a bunch of experts. So if you're just winging it, these things...

**[08:04] SPEAKER_01:** 100%. I mean, in my mind, because you were saying you copy these for security as a joke, I think that in my head at the time I was like, "Okay, there's this Fiverr gang that's out there just telling everybody to deploy these contracts and then they're shearing the funds or something." But it very well might have just been somebody copy-pasted that from some GitHub repo.

**[08:26] SPEAKER_00:** Yeah, they were the scammer. Yeah, they didn't even know, they were just the infection vector for scams.

**[08:32] SPEAKER_01:** Exactly. The lead dev at the time asked me, he said, "So what are the chances that we're going to get scammed here or whatnot?" And I was like, "Well, take the funds out of this contract, it doesn't seem like they can do anything, but... there's different funds in there... like, in theory, this person could come in at any time." Do they know about the fact that they've edited this function in a way? Maybe not, so maybe they just copied it from someone else. Ultimately, they forced their hand, because OpenSea actually maybe flagged them, maybe somebody flagged it for them or something, and I had to do a migration contract.

But all this development sort of was the seed of the interest for me, and then what led to Ethereum history was a few years later. Probably in like 2024 or something for me.

**[09:35] SPEAKER_00:** So pretty recently. Or maybe '23.

**[09:38] SPEAKER_01:** Yeah, yeah, probably 2023. Anyway, this coin popped up. So this was actually post-... there's this Relics group, this folks group of Discord friends that focus their time on collecting NFTs, old NFTs, and old contracts on not just Ethereum but they're into like... the one that was kind of like inscriptions and ordinals... not ordinals.

**[10:15] SPEAKER_00:** Before runes, no? Oh, Counterparty.

**[10:18] SPEAKER_01:** Counterparty. Yes, super old. And some of them don't like Counterparty NFTs or NFTs because they're not really... it's all built, you know, it only exists if you have this other massive meta-protocol.

**[10:35] SPEAKER_00:** Right, right.

**[10:36] SPEAKER_01:** So, you know, there's a debate and whatnot, but everybody collecting, they basically like these old things. And anyway, they reached out. They found Mistcoin. In their digging of old contracts, suddenly... and so Mistcoin was made like as an...

**[10:54] SPEAKER_00:** Example token for the Mist wallet, right?

**[11:04] SPEAKER_01:** Exactly, yeah, yeah. So Mistcoin was made by Alex van de Sande and Fabian Vogelsteller. You know well, and you've interviewed them. Fabian deployed it, but essentially they were, at the time, my understanding, developing a feature for the Mist wallet, the Ethereum wallet, to allow for anybody to deploy contracts. And so, at the time, before then, you couldn't just click this button. And within the feature, there were templates, right? So it was kind of like the first standard in a way.

**[11:45] SPEAKER_00:** It was. And it was...

**[11:47] SPEAKER_01:** At the time, the standard itself was being molded from before they launched and whatnot in the standardized repos, but this morphed into the current state of that more standard code, yeah.

**[11:54] SPEAKER_00:** And that was still pre-ERC-20, actually happening.

**[12:05] SPEAKER_01:** Exactly. Pre that. Whether it was the commit or the 20th pull request, I'm not sure. I'd have to ask Fabian or check... it's funny, actually, the way...

**[12:12] SPEAKER_00:** That works is, issues and pull requests are from that same ordinality. So it doesn't mean it was the 20th pull request, it was the 20th issue or pull request that had been created on that repo. So yeah, it can be either, because they never have the same numbering because that would be ambiguous. So it's the 20th time somebody either made a PR or issue, or put in any issue whatsoever, right? Anyone could just chuck any issue in and that would up the count. So a good number of the numbers are never anything, right? They never land right on the thing. An issue that says, "Hey, I don't really like the color red," right? So like, if you look at EIPs now, you know they're in the thousands, and it's not like because there have been a thousand proposed protocol changes.

**[13:22] SPEAKER_01:** Okay, chilling. Yeah, that's an interesting way of doing it. So yeah, so EIP-20, yeah. So this was November 3rd, was when they deployed that feature, and Mistcoin being the first one that they launched with it. Then Devcon 1, they talked about it a little bit. The standards panel.

**[13:45] SPEAKER_00:** Standards panel, yeah.

**[13:46] SPEAKER_01:** Simon de la Rouviere spoke about token standards itself. You know, he was also one of the few who were sort of helping mold this standard. And then a few days later, so the 19th, I think, or so. 19th of November is when Fabian and Vitalik sort of formalized this proposal. A slight adaptation change of the code of Mistcoin, but really this standard that they had been molding.

And it was funny, recently I found in this Ethereum history digging, this digging of old contracts, a coin that Vitalik had deployed, and it wasn't immediately clear that it was a token. You had to really look through the bytecode itself. And it didn't really... since it was written in Serpent...

**[14:48] SPEAKER_00:** Oh, right, yeah, yeah, yeah.

**[14:50] SPEAKER_01:** If you tried to decompile it with the decompiler on Etherscan, it didn't really work well. It's really hard to tell on the surface anyway. If you look through the bytecode, though, itself, and you're just raw looking at and analyzing it, which is much easier to do now with AI, you can tell it's a token, right? And it turned out it's actually this currency that he had deployed in the dapp-bin repo in September or earlier. Maybe September 8th or something, I don't know.

But what I thought was interesting after I had sort of found the exact Serpent code and proven that, hey, it compiles with this version of Serpent to this exact bytecode, and I posted about it. Vitalik actually commented on it as well on Reddit. And he didn't answer this question. So if he hears this, hopefully he responds. But what I was wondering is, so he deployed this days before—I think it was maybe November 6th—but days before he went and co-published this proposal, the standard. And it's sort of his old... what he would have wanted as a token. I don't know, what was his early proposal in a way. And I wonder if that was his sort of way of immortalizing, "Hey, I like this thing we ended up going with, now I'm going to immortalize mine on chain. You know, I like my way better." Different things. So that's how I like to imagine it's there. You know, one day maybe Vitalik will decide, "Hey, everybody should have my unnamed coin."

**[16:26] SPEAKER_00:** That's pretty... pretty random what people ended up pushing or not pushing.

**[16:38] SPEAKER_01:** And it's all, yeah, but there's only one. So I mean, I guess Vitalik doesn't make many mistakes and he probably even was using testnet or whatnot back then, but a lot of folks were testing in production.

**[16:51] SPEAKER_00:** Yeah, there was no economic value in the early days.

**[16:58] SPEAKER_01:** Right, right, it was, you know, trading at cents to the dollar back then. You're like, "Oh yeah, I spent 10 ETH on a test." But you know, a lot of the contracts now that I assume... So for Ethereum history, I'm...

**[17:19] SPEAKER_00:** Going to actually introduce them. Well, just before we get to that, so you spoke about Mistcoin as sort of being where you started. So is that wrapped now? Is it Wrapped Mistcoin? Because it was slightly pre-ERC-20, did Mistcoin need wrapping?

**[17:42] SPEAKER_01:** It needed wrapping. It doesn't have an approve function. It doesn't have a few other functions. It's one of the first named tokens, so, you know, in that way it's kind of special. And it doesn't adhere to the current standards such that if you tried to, you know, create a Uniswap pool for it, it wouldn't work. There are no approve or transferFrom methods that it needs. Just it's not going to move.

So essentially, if you wanted to make it tradable, which at the time... this Relics group had found a Mistcoin DAO that Alex had made and brought this Mistcoin in. Once they acquired some of the Mistcoin they were given, I think from both Alex and Hudson Jameson, if I'm not mistaken. They then were able to also pull more of Mistcoin from this DAO. I think Alex had put in a hundred thousand Mistcoin, which is like 10 percent of the entire supply, into this DAO, so they took that out. And then they used it, they gave it out to a lot of folks in their community of early NFTs. They kind of framed it as, "Hey, this is going to help early NFTs and this is going to help boost our community," and, you know, they were into that.

And so there is now a DAO that holds I think like maybe four percent of the supply at 40,000, and the rest is kind of given out to all their folks. And so when I bought it, you know, I bought it as a sucker. I bought it at like 50 hours of Mistcoin or something. I was like, "Cool, I can own this thing like everybody else." You know, my timeline didn't reach their timeline. You know, it's too late, a lesson for everybody! But at least at the time. But yeah, so they probably did very well. But they are also, you know, besides that, they are this group which, you know, I can't say I'm necessarily part of, but they very much care for consolidating relics specifically, as they call them. Specifically non-fungible tokens, so they're very much into just cool collector's items.

But that started Mistcoin and led me into this interest in early contracts. And once I started to dive into the story of Mistcoin itself, and you know, what Fabian and Alex were doing at the time, and how it was the beginning of basically everything that moves Ethereum today—everything that people are interested from an external perspective in, the tokenization of finance and whatnot, it all stems from the need for there to be a standard. And all that just sort of... "Okay, that understanding, that importance." It tried to lead me to say, "Okay, well what else is out there? What else was happening at the time that is either interesting today or will be interesting later, and can we sort of uncover that now?"

And so while I was writing a website for Mistcoin and helping with any sort of engineering projects that needed to sort of tell that story, on the side I started to download all of the contracts from 2015 and then 2016 and peruse through the bytecode. Before AI and all these LLMs were out there. So I was really just using decompilers like Python decompilers and running similarity text algorithms to try to figure out, "Okay, what is the likelihood of this being a token, or this being an ownable, or this being fungible, or this being something?" I'd look at deployer addresses, known deployer addresses type of thing, but it was much more difficult of an assessment than it is now. And I guess...

**[22:14] SPEAKER_00:** It's almost like a reverse engineering kind of discipline. You've got this... it has been a lossy thing, right? You know, that compilation process, it's not intrinsically reversible. You've got that data loss and you've got these patterns. But, you know, blockchains never die. Caveat, as compiled.

**[22:42] SPEAKER_01:** Exactly, yeah. It would be really great if it was possible to have, you know, to make Ethereum in a way that you could actually just store all the code itself and not have to do the bytecode, and you know, it's not feasible.

**[22:58] SPEAKER_00:** Well, I'll tell you what, a funny little thing, actually, is STRATO that I'm working on. That actually does happen for our chain because it has an alternate VM called a Solid VM, which is an EVM as well, but it's actually an interpreter. So what you have is you do have source code on chain which gets deterministically interpreted. So it's almost like you've kind of got Etherscan built in, kind of.

**[23:31] SPEAKER_01:** Kind of, right? And you don't have any issues with having to, you know, transmit large chunks of data...

**[23:38] SPEAKER_00:** Through consensus? No, it's been okay. I mean, yeah, you couldn't do that at a huge scale, right? You couldn't do that at a huge scale in a completely permissionless validator scenario, but yeah, there's an alternate universe, different things have been chosen.

**[24:05] SPEAKER_01:** Yeah, because, you know, like you said, it's before, it's been a challenge. I didn't even really attempt... there was a few attempts, you know. There was this person who has done a lot of work in trying to exactly prove the Mistcoin code, and eventually did, with the help of others. But it's a guessing game. You know, at a certain point you're trying to guess the order of functions, the functions themselves, the method names, and you get to a point where you get close. But so many things could go wrong. You know, there are so many possible permutations. There's the compiler version, there are the settings, there's the... like I mentioned, the order, the naming of the functions.

In some cases, even now with LLMs, it has made it impossible because, you know, I'm in one contract, for example, I'm down to just this one function name. And I know that it is more than 10 characters long, because I've tried every possible eight, seven... so I literally had this machine running on my computer just chugging through everything. And it's not... at first it wasn't even doing anything intelligent, it was literally going "a, a, a, a, b", yeah. So it actually, you know, you can't do that once you get to the higher characters, that just would take forever. But I just gave up, because what's the point? I mean, you know what the function does. And so you'll see on Ethereum History some say "near exact bytecode," and I'll actually indicate how close it was because I'd give up at a certain point. Because as long as you have the exact functionality and you're pretty close to completing bytecode—off by a few segments—then, right, right.

**[26:08] SPEAKER_00:** I mean, I guess there's probably a decent amount of the source code is probably on GitHub somewhere. That's another tactic.

**[26:16] SPEAKER_01:** Exactly. So yeah, yeah, when I'm doing this sort of what I call cracking—and there's an Ethereum history cracking skill and whatnot out there—one of the approaches is researching. So just going off Reddit and to GitHub and trying to find the contracts or contracts that are similar even back then. Right? Folks were doing... somebody would do something and another person would make a slight adaptation to it, you know, whether that's naming this function something slightly different, and now I can't guess it. But everything else, in this case, literally everything else was, like you said, published somewhere.

**[27:01] SPEAKER_00:** Yeah. So somewhere, yes, somewhere.

**[27:03] SPEAKER_01:** But you find it through keyword searches on GitHub and stuff that mentions...

**[27:09] SPEAKER_00:** Right.

**[27:10] SPEAKER_01:** Yeah, yeah, it's definitely a great tactic and it shows you can document everything on Ethereum History. But still, it's great to know that they're fragmented out there. As long as the internet is around, there are at least other folks documenting in time, thanks to the Internet Archive even. Even some things that have been removed are still out there.

And what one of the things I was pretty disappointed about, and maybe they'll bring it back one day, is Ethereum took down, last year or two years ago, the standards, the standardization repository. So literally this one GitHub repository that they just kept track... this wiki they kept track of all of the different standard commits as that progressed for tokens.

**[28:10] SPEAKER_00:** So this was a wiki within a given GitHub, Ethereum something.

**[28:13] SPEAKER_01:** Yeah, so a lot of the commits are still there on Internet Archive, and some folks had forked it at different junctures, so you can kind of find it at different stages. But I don't know what's the purpose of taking it down. I mean, I think they probably had some reason, maybe they didn't want to have confusion or something, but...

**[28:27] SPEAKER_00:** Yeah, it's... or sometimes it can just be incomplete ignorance of the consequences, that it's just somebody cleaning up or whatever.

**[28:33] SPEAKER_01:** Yeah. So I mean, I would imagine, hopefully that somebody at Ethereum has as they've sort of downloaded the repo over time and can stitch it back together.

**[28:52] SPEAKER_00:** So I... for a history of the white paper, so post-polar, you know, has done a lot of digging into those details, but it was only through him I realized that he had got some of those Internet Archive versions of the old wikis. I thought they were like all gone a very long time ago. Yeah, so it was kind of fun that those are still on the Internet Archive.

**[29:17] SPEAKER_01:** Another... and you probably remember this, but another thing I found on the Internet Archive is around that time in 2015, there was a bulletin that was kept up by somebody in Ethereum... okay, with... it was basically a forum where you can ask questions, but it was all seemingly self-posted or...

**[29:43] SPEAKER_00:** Oh, that just the Ethereum forum?

**[29:45] SPEAKER_01:** I think it was the Ethereum forum, and yeah, and there were people talking and had its own message threads, and...

**[29:51] SPEAKER_00:** Yeah, yeah, that was discourse. I think it's discourse, the software is. But yeah, that wasn't used for very long. Like, Reddit became a lot more popular. But then I remember there was a whole bunch of drama about, "Oh, we're going to shut the forum down, are we not?" And then it was like, "Oh, okay, maybe somebody in the community wants to maintain it." Yeah, "But then it's like, oh, but you can't because you'd be giving over the database that has all the DMs in it, and it would all be like..." So I think Hudson Jameson kept maintaining it for quite a while. I don't know if it could ultimately...

**[30:34] SPEAKER_01:** Yeah, it would be interesting, and there was definitely at least one contract that, through the Internet Archive, I could see that I was about to get some important information on it, and then it just, you know, next week it's gone. But yeah, some of these ventures into trying to document some of these contracts go quite deep into these internet archives, and they're not easy to peruse through. So you get into those old things that have been taken away and it kind of feels exciting, because it kind of feels like you're digging into something that nobody knows anymore. Yeah, that's what's kind of kept me going.

It seems like people are genuinely excited, you know. I don't know, it's a small group. And obviously, I only have sort of Reddit and those folks who are still on Twitter to speak to this. I wish there were other avenues, but there is a decent community of folks that still reminisce and still want to know about history. And, you know, the first programmable blockchain, what that really is to them, and not just from a people's perspective but like the actual testing, contracting.

**[31:59] SPEAKER_00:** So your site is ethereumhistory.com. So what features are there? What can people see if they visit that?

**[32:07] SPEAKER_01:** So my short elevator pitch is Wikipedia of Ethereum smart contracts. So the idea is, Etherscan itself is great. Etherscan tells you all the facts about every contract that they can find on chain, and you can see, of course, the bytecode. You can see the code if they verified it or not, but there's very hard restrictions on how you can verify it. And they only support a certain, you know, zero point something version of solc, right?

**[32:40] SPEAKER_00:** So like, probably the version when they started?

**[32:50] SPEAKER_01:** Probably, yeah, yeah. You can't go further back, so anything early you can't really verify. But beyond that, actually adding any descriptions or tags or anything is very difficult with Etherscan. So it's really not meant to add any meaningful documentation to a contract; it's really just there to say this thing exists. And outside of that, you know, there's nothing popular or nothing I could find that has any sort of purpose of recording the history like a Wikipedia would, right? And of course, maybe there are some projects that have gotten to the point at which there is a Wikipedia page, like for their token, yes. And it will probably say a link to Etherscan or a link to their contract address, maybe, which is probably meaningless to users. They're probably just given the website.

So basically, where's the home for this Wikipedia? Where's the home for folks who are interested in Ethereum to learn about those early contracts, learn about the story behind them, and look at the original code itself? You know, not like the bytecode, but let's look at the actual code. And I think there are two different things that people can take out of that.

One is, if you're interested in the stories, you can go back and sort of see the qualitative stories. They're not always going to be accurate because every story, right, is a sort of picture of what somebody remembers and tells one other person, and your memories are of course fickle and perhaps might not be exactly right. But hopefully, with the idea of Wikipedia, everybody sort of edits it over time and it becomes right.

**[35:10] SPEAKER_00:** So hive mind, yeah.

**[35:11] SPEAKER_01:** The hive mind, it's going to be perfect. It's very efficient. So anyway, right now the Ethereum History is not exactly efficient because there are 18 different historians, of which... the users are called historians, but of which have documented contracts, right? So you know, after everybody watches this video, everyone, sign up! It's free. But so one thing you can take away is the stories.

And then the other thing that you can take away is like actually reading the code of all these early contracts. And the vision I have there is once we do get the code, I want to find of every or most of these contracts—which we're making pretty strong headway right now—I want to find a way to represent that in some sort of visual in my head. I don't know how this is going to work out, but I picture like archaeology. Like rocks, you know, the way that you can look through the layers of the earth and read history through some sort of visual representation of that, but through code functions or methods or... I don't really know, it's kind of...

**[35:59] SPEAKER_00:** It's a loose thought in my mind, but I would love to see something with a scrubby timeline somehow that changes shape somehow, yeah.

**[36:07] SPEAKER_01:** I'm interested what sort of stories... what can we learn about the reuse of different types of methods and how they evolved, and then maybe the popularity of the contract, the amounts that it's been... which you could discern by the number of times it's been replicated or the number of transactions that have occurred to show the popularity of proposals. And then how long that has lasted over time.

**[36:37] SPEAKER_00:** And what that is is like species coming to life and dying off and... yeah, exactly. "Look at that dinosaur technique, that literally is a dinosaur technique that's not used anymore!"

**[36:52] SPEAKER_01:** And it's a hard thing to keep track of because, you know, a method has a purpose, right? And it has a name, but it's meant to do something. It might do several things. It might be part of a larger set of goals of functions that are calling it and whatnot. But if you're trying to find a thread through history, you might want to look at, you know... you're dealing with a semantics problem as well, because it doesn't have to be the exact method, but the same purpose. And has it gotten hardened, or worse, or better over time?

**[37:29] SPEAKER_00:** You're sort of wanting to infer design patterns out of it, or something, or higher level patterns or reasoning or... yeah, yeah.

**[37:43] SPEAKER_01:** Hopefully that's possible. And it's sort of like a loose thought in my mind, I don't know. We'll see what people want to build, you know, it's an open-source project so hopefully folks will add their own pull requests to that sort of thing or issues, and I'll mark them as proposals, EHIPs, regardless of whether it's an issue. EHIP-1. Or if anybody wants to grab a lot of pull requests, since I'm just going to go straight to that, right, just straight to commit, we're going. But that yeah, so the code and the stories are kind of the main goal now.

And the other angle I have: so I got into this downloading all of the 2015 to 2017 contracts, decompiling them all, loading them up into this database, and then on top of it I've added these indices on this database such that you can query through all of the decompiled code, right? The goal there was anybody should be able to find interesting things through the code. Maybe somebody's interested in mining, or they're looking for the first time that the word "cat" was written somewhere. The decompilation won't be perfect, it might not have the actual first "cat," right? There's a chance that it does. And this gives them the ability to search through text rather than just bytecode.

So that was the first idea. Now what happens is, every single time a contract is cracked, as I call it, to solve the exact code with this compiler and settings, that gets added to the index as well. So you can actually search through the code.

**[39:30] SPEAKER_00:** That sort of improves that discoverability. So what kind of different existing tools have you been using or found useful for the cracking and for researching? Yeah, and disassembling?

**[39:47] SPEAKER_01:** So the disassembling has been interesting. This whole cracking thing depends on the contract. The first thing I'll do, and of course all this heavy usage of AI here... always. Yeah, yeah, my AI overlord is helping me out every day. But you know, the first thing I'll have to do is just go through and see... hey, through my... they have this Ethereum history researcher skill that just goes through GitHub, Reddit, and tries to find... first, it will decompile it, or use the decompiled code I have already, and try to find anything that resembles it in GitHub or Reddit at the time. And if it finds a match or it knows of some match—you know, it obviously has its inherent knowledge already of the time these things were out there or published—then it will start there. So it's mostly about finding a starting point, if not the exact code. Sometimes it is the exact code. Sometimes it's like, you know, a very reused wallet at the time or whatnot or something, yeah.

So it's establishing a starting point, and then from there it's taking the different versions of solc at the time. Or it will try to, you know... is it Serpent, or is it LLL, or whatever it may have? Mutan, I haven't found it.

**[41:00] SPEAKER_00:** No Mutan?

**[41:02] SPEAKER_01:** Not yet. Only, I honestly so far only Serpent and... there's two: Serpent, solc of course, and then in some cases, it's just straight bytecode, I think, that they deployed. So, as far as the AI could discern, there wasn't actually any code. They just created the bytecode themselves and launched that.

**[41:41] SPEAKER_00:** It's strange, because I thought you always had LLL in the line. Or maybe this was only for Solidity. So I think for Solidity it was always built on top of LLL at the start, like kind of using LLL as an assembler, yeah. But Jeff was working on Mutan up almost until launch, so it might be that there's hardly any Mutan on mainnet. Like, probably a bunch of that on Olympic, but then it, you know, it's kind of...

**[42:22] SPEAKER_01:** For the ones that it discerned were all done in straight bytecode, it used Yul, I think, or something. It's...

**[42:32] SPEAKER_00:** Something is somewhat recent, like 2018. Yul? Yul. Yul, sorry, yeah. But who was it who was talking... was it? Oh, that was... yeah, I did an interview with Alex Beregszaszi. So, axic. A-x-i-c. Okay, who was Solidity co-lead for many, many years. So he was saying that when it started it was called Yul at first, like Julia, yeah. But with a J, I think. Okay. But then there's some other computer language called Julia already, so then that changed into Yul, y-u-l, which is a kind of intermediate representation in that the goal was that the Solidity would compile to Yul and then you would have a further compilation step on the back of that, well, hopefully. So I guess it kind of ended up being sort of like a bit like an assembler.

**[43:48] SPEAKER_01:** Uh, find out. Hopefully they're proud to know that AI is still referring to their work. Because for those few contracts, they choose to represent them in Yul. Right, that's good. Yeah, cool.

Yeah, so that's there. And so this part of it is research, part of it is getting a sort of narrowing, chipping down if you will, to this bytecode. And in the process, of course, it takes it to sort of, you know, the time at which this was deployed, right? So you know the different versions of solc that were out there at the time and you just try to do a trial and error kind of thing.

**[44:36] SPEAKER_00:** There's no metadata that ends up of the solc version in the final bytecode? I think correct me if I'm wrong, I think the metadata started a bit later. There was a particular newer version of solc where that started.

**[44:45] SPEAKER_01:** Yeah, I want to say that, because that became a thing. So the person who leads Sourcify reached out and has been really great. He's been helping... he expanded Sourcify such that it could go down to much earlier versions of solc. So I think you can be verifying on Sourcify and also adding all the methods that we uncover so that they're there for the world to sort of use.

**[45:15] SPEAKER_00:** And what does Sourcify do exactly?

**[45:18] SPEAKER_01:** I'm going to butcher this, but, you know, they seem to be the registry of not just methods that have been ever deployed on the blockchain, so a way to sort of make them accessible to everybody, but also to verify the actual source code of any particular contract, right? So it seemed to be something that you would do going forward for a long time, if I understood it correctly, but then they've started to also go backwards, backwards.

**[46:04] SPEAKER_00:** Backwards and so kind of like taking that functionality that you have within Etherscan but pull that out into a component that can be used independently.

**[46:22] SPEAKER_01:** Exactly. Yeah, maybe the idea was why should maybe Etherscan want to just replace it with Sourcify? But yeah, I've pinged Etherscan a few times, especially as I started to validate or crack a bunch of these earlier contracts that I could not verify. Essentially the way that you would verify on Etherscan for these older contracts is you would reach out to support at Etherscan, right?

**[46:58] SPEAKER_00:** Yes, that's how you would reach them.

**[47:00] SPEAKER_01:** Have them respond. And, you know, for Mistcoin we had to go through somebody and do... somebody who was there. And they, you know, eventually that person reached back and said, "We're going to help you get this verified." But I cold emailed a bunch of these and they're really interesting. I mean, they still haven't validated them. For example, GavCoin, G-A-V-coin. Vitalik's currency. You know, these are like arguably very interesting and prominent contracts from, you know, arguably very important people in the space, and they still haven't.

So I got this sort of blanket response that was, "Thank you, but you need to be the deployer. Are you the deployer? Could you sign this transaction?" And I was like, "Sorry, I'm not Vitalik, I cannot sign it." They ended up... somebody did reach out on Twitter and said, "Hey, yes, sorry about that, that's our blanket response. And here, actually we helped verify one." And it was one of these Peperium... you know Peperium? Peperium is like I think for 2017 or so, an NFT-like contract, like I think it's more of a fungible-like token but in some way that they added metadata onto it such that there's like...

**[48:40] SPEAKER_00:** This is not Piper Merriam, no?

**[48:42] SPEAKER_01:** No, it's not Piper Merriam! Yes, that would be hilarious if this was Piper. It should be, right! Yeah, it never rolled off the tongue the same way. Peperium, I think it's more about Pepe, you know. Right, every one of them I think has some sort of picture of Pepes, right? But anyway, so this Etherscan person verified that one of all the ones that I sent. And I was like, "One of the ones I care about." Where... my top ones, I don't want to say I care one way or another, but I'm sure a lot of people care about.

**[49:03] SPEAKER_00:** So Gav must have deployed GavCoin onto Olympic and onto Frontier then, separately?

**[49:11] SPEAKER_01:** Oh sure, I'm sure he did on Olympic, he must have. It's for fun, right.

**[49:19] SPEAKER_00:** Um, well, because there was a talk I found which was August 2014, I think. Yeah, yeah, with Jeff in London, yeah. Doing the DEX, demonstrating that on their DEX and joking around. That's, that's right, how GavCoin's the better coin, that's it! Gav saying, you know, he values GavCoin.

**[49:58] SPEAKER_01:** Yeah, so you know, I can't prove that GavCoin, the one I found, was right, but you know, I have a chain of information, a thread of different events that seem to have a strong case. Maybe Gavin will listen to this and decide to tell the whole world that he just deployed it and probably forgotten all such things many years ago.

There's another theory I've worked on, it could have been potentially deployed by that Roman, the person who ran that EtherCamp, Roman Mandeleil. Yeah, which I... I wasn't around so I don't really know. I mean, I know Piper I think did some work with EtherCamp at the time and I believe so. I don't really know, I'm just sharing things I read. So yeah, exactly, oh so that's why I think it might be part of... potentially deployed by him, because I think the deployer might have also deployed Hacker Gold. Right, so could that have been? Yeah, then I think it's possible now.

**[51:21] SPEAKER_00:** So then no, if it was Hacker Gold, that would be Roman, yeah for sure. So that, maybe this was... I'd have to look, I forget.

**[51:29] SPEAKER_01:** Now it's been a long time of looking at other contracts that followed the deployer, but some I found some connection to Hacker Gold as well. So maybe Roman wants to tell the world about... I don't know.

**[51:42] SPEAKER_00:** I don't know if anybody talks to Roman anymore. I used to be Facebook friends, but then he seems to have gone off. But yeah, he basically disappeared in 2017, really. But he was around...

**[52:00] SPEAKER_01:** Iconic himself, as I understand. Some of the firsts have been from him. It's quite a character.

**[52:08] SPEAKER_00:** And Hacker Gold, one of the things that they became, which is unbelievable at the time let alone now, they at Devcon 2 in Shanghai, so October 2016, this was, they did this demo called CashETH with Banco Santander. And it was basically a stablecoin on Ethereum in browser. So it was sort of like you've got some kind of MetaMasky thing for doing... sending stables in a browser on Ethereum, it was very novel at the time. Also very surprising that they did it with Roman. It's because he was a bit shady, or erratic, shall we say. Yes, he did not come across as the sort of person that you'd be doing a banking partnership with... no. But he went to Banco Santander and not JPMorgan, I guess, so but... sorry. But you know, that was happening, yeah, all that time back. Yeah, that's cool.

**[53:33] SPEAKER_01:** No, it's interesting, I feel like in the beginning, in the early years, banks were very interested in Ethereum. I think there were some sponsors for Devcon 1. Yeah, in grad school where I was, there was certainly UBS. UBS, yeah. I think JPMorgan might have been. So we had these, at BS school, we had these challenges that companies would come in and propose concepts to, and the students, the engineering and the business school students, would come up with solutions to these challenges in the form of products or companies or whatnot, or ideas. And one of the banking ones was blockchain. And basically the challenge was "incorporate blockchain into our platform in some way that's useful for us." Right. And the team of course... I think they explicitly said Ethereum, which just launched, it was like 2015. Right, why not, why not. But yeah, banks really, of course, they've stuck around with some other ETFs and making loads of money off of blockchain assets, off ERC-20s that came from Mistcoin! There you go. Got it back, okay. Well, which is also an arguable thing. What is it to say the origin of something.

**[55:09] SPEAKER_00:** Well, everything's built on top of everything else, right? It's all just ideas. Maybe that's a good place to wrap up. Sure, thanks so much, yeah, sir, you're very welcome. And ethereumhistory.com. Yes. This is the site for people to go. And so we've got a call to action to get people to come and come and have a look. You can sign up with Google...

**[55:45] SPEAKER_01:** Google, GitHub, create an account just simply with your wallet. You can create an account with a fake email, it doesn't matter. The idea is just to come in and help document old contracts. Whether that's... you're just, you know, there's somebody who's helping out a lot right now who's just spending his time during work because he's bored, you know, calling, telling his AI friend to help document. He's doing great work. He's cracking all these early contracts. And so if anyone's interested in just spending some time helping research and adding and documenting, you can just do it without any approval.

And this sort of Wikipedia of Ethereum will solve itself without imperfection over time. Which won't tell the right stories, of course, if you're malicious and you're trying to just mess everything up, please don't join, because we're trying to document Ethereum's history accurately. But, but yeah, it'd be great if it takes up. I mean, I think it really is something that doesn't exist anywhere else and should have utility for the people over time that it gets filled out.

And I do have this vision, I didn't say earlier, I have ideas already, I've already sort of formulated the contract, but of putting it on chain, so you know, basically like hashing the JSON of whatever content we want to keep and then pushing the hash on chain. So it's not an insane amount of money that needs to be deployed each time there is a change. But those things are difficult because of the monetary aspects of it, but it does, you know, it makes sense that something about Ethereum should have Ethereum involved.

**[57:28] SPEAKER_00:** Uh, I'm going to get the ouroboros snake eating itself exactly until it's all everything, because every time that you push one of your hashes on, then you've got to push the hash of the hash of the hash! Oh, it never ends, right? Because you...

**[57:49] SPEAKER_01:** That's true. Yeah, no, it has to be this... yeah, otherwise you lose the history of... you're right. Okay, that's a good point.

**[57:55] SPEAKER_00:** It can never end, it will grow until the whole of the chain is taken up by the hashes!

**[58:04] SPEAKER_01:** Which is poetic in a way, that Ethereum should be taken up by Ethereum.

**[58:12] SPEAKER_00:** Okay, well thanks so much. Thanks Bob, thanks y'all. Alright, thank you. I hope the audio is okay. I noticed that was buzzing, like the air con was a bit noisy at times, but then it stopped. Yeah, if it doesn't work we can always...

**[58:31] SPEAKER_01:** You...