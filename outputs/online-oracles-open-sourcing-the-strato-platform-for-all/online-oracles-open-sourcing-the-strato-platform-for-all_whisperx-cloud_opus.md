**[00:03] SPEAKER_06:** Okay, boom. We are live. Happy Wednesday, everybody. Hope you're all doing well. March the 4th, 2016. We're into the new month... 2026. I'm sorry, he said 2016. Did I... 10 years ago?

Yes, yes. 2020 has flown, hasn't it? That's it. I have to calculate my age. I don't know what year it is, even how old I am. But yes, so today we have a goodly number of people here. Myself as usual, Bob Summerwill, Head of Ecosystem. Kieren James-Lubin, the CEO, down the bottom there. We have Victor Wong, top right. Michael, who often joins us, Michael Tan. And we have a guest appearance here from Dustin Norwood, who has the honor of being the number one ranked top contributor all time to the STRATO code base. And we're talking about open sourcing today, so seemed only right to have Dustin here. So before we go into open sourcing, we've just got a little bit for Michael to talk about.

**[01:23] SPEAKER_00:** Sure, let me share my screen really quickly. So yeah, as a lot of you know, we have wrapped up the points program for our first season. A million points distributed. Be sure to claim your points on the My Rewards page. There was a lot of great usage, some great APRs on different pools and different actions on the site. And check where you are at the leaderboard.

**[01:55] SPEAKER_06:** And be ready for season two coming up soon. Kaboom. Short and sweet. So yeah, open sourcing. It's a big day. I was looking back, we had a first step towards this, the snapshot that we released in January of last year. But then today we are doing a full open sourcing and release of the entirety of everything that we have done as a project, as a company, going back to September 2014 was when the initial commit was from Jim on Ethereum H. At the time it was Ethereum H, right? That was the initial name. And then Kieren joined that effort quite shortly. So Kieren, how did all of this stuff start, like this long journey?

**[03:11] SPEAKER_05:** Wow, yeah, good question. I guess, so I had worked... go back to, let's say, March, April 2014. I was in grad school at UC Berkeley and going into my qualifying exam. I was in the math department and it was quite painful, but I passed it. And I was sort of looking for something to do in the summer. I recall almost taking like a machine learning job, which I'm sure would have been interesting. But I was lucky enough to get my hands on the Ethereum white paper and luckier still to start work on it. I guess, April, maybe more of a May kick off in earnest. And just sort of leaned all the way into it through those summer months and contacted a bunch of people. One of them being a kind of former, still informal advisor, Steve Shu. Steve is a fairly famous theoretical physicist, formerly the head of research, beefy research at Michigan State. He's still there as a professor. And Steve put me in touch with Jim maybe around July, August. I haven't pulled the emails up.

And at the time Jim was living pretty nearby where I was in the Bay Area. And so as soon as I'd come back from the summer, we... oh and here's Jim now, hello. We met up and kind of hit it off and just started, Jim got interested enough to start building Ethereum H. And fairly shortly later I started contributing as well. So yeah, that's the really brief origin on the code base. Victor, Jim, and I are the co-founders. We all met up January 2015, and that really kicked things into motion more formally around actually two conferences I was hosting. One called Crypto Economic, the videos are still available on YouTube. Bobby, I think I sent that link to you, right? You were able to...

**[05:22] SPEAKER_06:** Yeah, yeah, some classics in there. We should maybe put it in the show notes or something.

**[05:27] SPEAKER_05:** Some a who's who of faces showed up to that event. And a more kind of commercial conference with O'Reilly Media. At that time we sort of saw there was definitely a feeling like, we're in the room, it's like being in the room with Tim Berners-Lee or something, this thing is going to be big. The business-y types see it, the radical open source devs see it. And we got to just sort of jump in, and we did. There's been a lot of code since then.

**[06:09] SPEAKER_06:** So Jim, I was just saying at the start, 14th of September 2014 was the first commit there. So what were you thinking when you started?

**[06:32] SPEAKER_03:** Well, I thought this was gonna go... do I mean, like on day one I just wanted to understand it. I kind of believe you can't understand something unless you are understanding it through the code. And it turns awesome. But I remember the first, and I had a sense that there was something awesome going on there. But when I first started to look into it, to understand how it worked, a lot of the videos that had been put out were sort of hyperbole and it didn't make sense to me. I would go to these videos, like typical video would be like, "Ethereum is the fabric that underlies society. It is the future. It is how we will build a new society." And I was like, "Okay, but what is it?" And then I found the code base. So I was like, let me start playing with this.

And also, just reading through a code base, it's not interactive. So I was like, let me see how this thing actually works. And I pulled up my favorite programming language, Haskell — should be all of your favorite programming language, by the way — and I found a boot node and I connected to it. And I realized that commands were coming through to me, so I started adding code to talk back to these nodes and slowly picked up what it was and how it worked inside and what a blockchain is, and all of that. So that was the beginning thing. But soon after that, realized that I'd put together enough lines of code that I had some... I had built a tool that could be useful to the world.

**[08:25] SPEAKER_06:** So what is a blockchain? What was your conclusion?

**[08:28] SPEAKER_03:** It's a long technical... okay, no, no, I'll give you the more poetic answer. I think it is the fabric that under... no, I mean, it's incentive. That's what it is. You have a lot of people sitting around wanting to contribute to society, and yet it's hard to coordinate everyone to do things in some aligned way. And once you build some type of money, you can sort of align lots of groups of people to do something together. And so that's what it really put into the world. It's incentives to get distributed characters from around the world to all be aligned in one direction. And you can sort of craft what that direction is.

**[09:11] SPEAKER_01:** But by the way, Jim, to defend that, like, "it's the underpinning of the new world," Vitalik's latest post literally today is about that. He's talking about sanctuary tech and how Ethereum has to move beyond finance. So that thread has never left.

**[09:32] SPEAKER_03:** I mean, I did do the full circle. I was kind of laughing at all this crazy hyperbole, and then I spent a lot of time understanding the technology. And then by the end, something clicked in my mind and I was like, "Holy cow, this really is the underpinning of the new world, and this is how we're going to build a new society." And you need to have some way for... I mean, you can get a certain amount of free work in the world. I think Wikipedia shows that if you just put up a tool and lower the barrier of doing stuff, people will just come and do free work for you. But if you want to go a little bit beyond that, you have to start aligning people to some sort of common vision, and you need an incentive for that.

**[10:14] SPEAKER_01:** Yeah, no, not to call you out, Jim, but around that time we were also thinking about doing a startup together. And the way you presented it to me was like, "This might be amazing, or this might make absolutely no sense. I'm not exactly sure which."

**[10:33] SPEAKER_03:** Well, yeah, I mean, there are network effects and all this thing. I think once I started understanding the technology, I said, "Okay, this is amazing, but it also might be that nobody will use it and it'll just be an amazing technology that just languishes." And it turns out that other people were interested. I remember another stepping stone is we started hanging out at Consensus more and more, and I saw so many excited people there. I said, "There's no way this is going to fail. There are just too many people who are really excited about this at this moment right now." People willing to leave jobs, give up everything, and come and just work on this stuff. So this is going to be something. And it was.

**[11:23] SPEAKER_06:** And then how did things move from building a Haskell client into STRATO being envisaged? And what was the initial kind of vision?

**[11:33] SPEAKER_05:** So I guess we... I've always been like a certain kind of pragmatic people. And through building the client and then also trying to use the early flavors of the RPC and all the tooling, we realized day one the DevX was just not there. Today it's much better, the tools are reasonably mature, although there's still things that bother me about the Ethereum DevX that are just choices that were made that made things unnecessarily difficult for no real reason. But you can also just AI around a lot of it now, you get it.

But it was really difficult to get even a node up, and then once you've got the node up, you're configuring connections to it. And they were initially... so for some reason, and maybe a good reason, maybe not, the Ethereum people felt like they had to write to a virtual machine, which we all know and love, the EVM. And they created maybe like four competing high-level languages, or three, very early on. There's LLL, there was Serpent, Solidity was a little later, right? There was a Go flavor one...

**[13:02] SPEAKER_06:** Mutan. Mutan. Mutan. Though I found out recently that had got an earlier code name as well, which was HLL, so High Level Language.

**[13:12] SPEAKER_05:** Was Mutan... but yeah, that was abandoned. That was done by Jeff Wilcke. It was abandoned.

**[13:17] SPEAKER_06:** LLL is like language, by the way.

**[13:20] SPEAKER_05:** Yeah, I'm sorry. LLL was this... Lisp-Like Language, or Low Level Language, I think it was. I think that... yes, there was a lot of nerd one-upmanship in early Ethereum. Maybe this is common in the open source space in general. There's kind of, reminds me of like subtle swipes that academics put in their papers or something, the naming of things. But it kind of works. There was this weird all-against-all but all-for-one competition in early Ethereum. And I guess we got stuck with Solidity, which, it was fine, like it works.

But yeah, so I guess we were like, "Okay, this tooling is no good. You can't get the node up. The APIs are weird. These languages are moving. So let's just solve that." At that O'Reilly conference I put on, Chain.com was there, back when Chain.com was a REST API infrastructure provider for Bitcoin, which was maybe for Bitcoin a model that was doomed. And the RPC providers that stuck kind of came later than we did. But that was the first thing we did. We're like, "All right, let's get an API up, let's make the routes sensible, and let people get access to the live net."

And I guess that initially got called STRATO, right? That bundle of things. In doing so, somehow we were enterprise or institutional coded, and it was not at all our intention. We kind of thought it would be just an easier developer API. And kind of found the hardcore devs really liked the standard RPC interface, and the enterprise devs were like, "Oh, I can put this in Postman." And so we got kind of pulled in that direction. And over the years, going from POCs to pilots to powering consortia and all that sort of thing. And I guess the aggregated name for all of that was STRATO.

We launched by DevCon One, so this is end of 2015. We were still working within ConsenSys at that time. And had partnered with Microsoft to kind of create that category. I'll be two minutes, left to check on something. Sorry, guys.

**[16:11] SPEAKER_06:** Maybe Victor can continue here. So I mean, from my memory, it was DevCon One where I first saw the BlockApps name and branding, and STRATO. I was aware of Ethereum H existing, but not really of what was going on at that point. So...

**[16:43] SPEAKER_01:** We've always sort of followed this lean philosophy. And I think our first test ground was the launch of Ethereum. We did the first hackathon at Consensus, right? So that was August, I think, 2015 when that happened. And it was interesting because people were building stuff really for the first time. And people kind of built prototypes of a lot of things we see now. There was a GameFi app, there was traceability apps, there were sort of DeFi-ish apps.

But one of the interesting things is some of the judges were part of the more institutional, traditional world. And that's where they learned about what we were doing. And they were like, "Oh, well what you're doing, yeah, we need a REST API to write against. We really want to use this." And Microsoft kind of came up and said, "Hey, if you guys want to do this with us, we'll... we want to promote Ethereum and you guys. But you have to offer a mode that allows you to run as a private blockchain. We don't want to have to make it a requirement that people have to go up and acquire some ETH in order to do this."

And that was really kind of like, between August and, I think DevCon was November, yeah, November. So we were madly working to try to get this working as a way that we could deploy this on Azure and do that demo of like, "Write a dapp in five minutes," for DevCon One. And interestingly, we were not their first choice. Another project which did Ethereum J, they were actually part of this. Microsoft wanted to work with them because they were a Java-based client. We were this crazy Haskell thing. Jim, not to... although there are... sorry, Microsoft Haskell... yeah, there are, and a bunch of the researchers are there. But you remember those conversations? They were like, "Hey, if this could be widely adopted... Java is the most interesting thing, but you guys are interesting too, and you guys come along with it."

**[19:13] SPEAKER_06:** And that's what you're telling me? If Roman Mandaleil had been a bit more business savvy and stable, that the whole path of the company may have been quite different?

**[19:19] SPEAKER_01:** Absolutely. Well, I had some background with this because in my previous company I had worked with Microsoft before, in their app world. But it took forever, like it took like eight months for me to get a meeting with Microsoft to start talking. So the fact that they came to us and were like, "Hey, we want to do this thing with you, but we want to launch it in two months together," it was like super... I realized the opportunity.

And yeah, I think Roman had other priorities at the time and kind of let the ball drop. And that kind of kicked off everything. And then really for that time, we were like the only option. If you wanted... Azure was just launching really at that time. And so lots of people getting free credits, and a lot of people just wanted to, like, "Hey, I heard about this weird Ethereum blockchain thing. Can I just try it? Oh, they have a thing." And they tried it. And literally like hundreds of people used our solution very, very quickly.

And most of them were, complete nonsense. Like they were just trying to use it as a database and swap it out and do that kind of thing. But there were a few people who figured out what they could build with it enough that they wanted to build bigger projects, but they didn't know who to go to. And so that was really the next evolution of STRATO. It was like, "Okay, now we have to support these bigger projects where it's not just a dev node where someone is kind of connecting to it. It's a real network with multiple parties, and they have security ops requirements and dev ops teams and all of these things. We had to evolve the product in that way."

**[21:16] SPEAKER_06:** I seem to remember that Geth was on there as well at that start, that you could just launch a public Geth node too?

**[21:27] SPEAKER_01:** It wasn't part of the original launch for blockchain as a service. It was added later, if I recall correctly. And I think someone put it on AWS just as an option. Like it wasn't an official image or anything, they just put it on there. I mean, that might have been us.

**[21:52] SPEAKER_06:** For various reasons. I mean, I remember there was a period shortly afterwards as well where people could add their own as well. Yeah, and with this whole range of total scam projects, like slapping their crappy software up and saying, "Oh, look, we're partnering with Microsoft." It's like, no, no.

**[22:14] SPEAKER_01:** Yeah, yeah. And it was very funny because at the first Consensus conference we were hosting a hackathon there. And there was a very early version of Hyperledger there. And I remember there was a room where all the people were hacking it. And our room was full, and there was like one person in the Hyperledger room. It was very sad at the time.

**[22:46] SPEAKER_06:** So Jim, would you maybe like to say a little bit about the architecture of the code base? Like, what is being open sourced here? What have we got?

**[23:00] SPEAKER_03:** Well, it's one of our nodes. Let me sort of answer your question by going back to a point I was going to make before, but sort of turning the clock back to a topic that we had before. And that is the various languages being used in the blockchain. And I guess I always considered it sort of a mistake that the EVM sort of resembled opcodes of a CPU. And my evidence in this favor is that I've lived through this before, back in the '90s, when the browser was kind of getting bigger and HTML had started to become a standard. People realized that they needed to have some way to program web pages too. And the first real attempt at doing this was actually a sort of large opcode, CPU-like plugin, which was the Java applets back in the day. And it was bulky, ugly. You'd sort of go to a web page and it was almost like booting up your computer. You'd watch the web page struggle a little bit and then kind of come up. And then eventually you might get something that looked a little bit like a computer screen sitting in the middle of your web page there.

And that failed pretty miserably, and it was replaced by JavaScript, as we all know and love now, which was sort of like a higher-level scripting language that just sort of runs in various threads in the background in your browser.

So one of the biggest changes that we made is that although in the early days we certainly had the EVM in there, and the code is actually still in there but mostly commented out right now, we have something called SolidVM, which is a kind of like a JavaScript-style language that runs as your contracts. And one of the big differences is that since everything is opcode-based in the Ethereum network itself, you have to compile everything down and you can't really see what your contracts are doing unless you try to decompile it or something. And with us, we just keep the Solidity or the SolidVM source code right there, so you can visit any contract and just look at what you want at any point during time. Or if you send a command in, you just send the Solidity command right in the transactions. So that's one of the big things, is that we're not based on opcodes. We're based on this sort of slick scripting language running in the background, SolidVM.

**[26:02] SPEAKER_06:** So that's... questions or comments. Maybe if I reach out to Dustin. I was just looking — so as far as I can see, your first commit was the 9th of August 2017. So you joined in this journey not terribly long after all of this. And one of the key things I remember from my time at the EEA, which is really where I met Victor and Kieren first, was the differentiation that there was versus all of the other clients at the time, is they were all monolithic single executables. But STRATO is very much not that way. So how is it?

**[27:00] SPEAKER_04:** Yeah, so STRATO instead runs as a set of microservices that for the most part are connected using Kafka as sort of the inter-process communication bus. So whereas with Geth and maybe other clients, it all runs as a monolith, as one program, each component of the node is its own process. So the VM that runs SolidVM, as Jim just mentioned, it's its own process. P2P module runs as its own process. Ethereum discovery, sequencer that sort of orders all the transactions and blocks before handing it off to the VM, that's its own process. The API, etc.

And this makes it a lot more robust because if one thing goes down, it can be restarted sort of without having to take the entire node down. But also it gives some nice replay properties where, since we use Kafka, we can sort of rerun like a second version of or second instance of each executable and it will rerun through the logs from Kafka, and you can sort of re-derive the same state. It really helps with debugging. And yeah, of course, there are some things that might be a little trickier, such as tracing a certain message through the entire platform. But I think overall it gives a lot of benefits versus the monolith architecture.

**[28:33] SPEAKER_03:** Yeah, it's a full separation of concerns. The VM is just like a monster that just sits there and gobbles up all the transactions coming at it through Kafka and then outputs all the data changes on the other end. And we have various other things in there. We have indexers. One of the things that we added also is at the end of all of the processing, just built into the system, there are these Postgres indexers. So everything that output from the VM goes to another Kafka stream and the indexers just gobble up all that stuff as it comes in, and sit there and fill in tables all over the place. So we have all of the state and history just there for a quick SQL query. So you can see the whole history of the blockchain.

**[29:28] SPEAKER_06:** Yeah, and I mean, I guess that is really very different to lots of other clients, right? Because it's sort of, I guess, a bit more like some of the characteristics that you get off archival nodes.

**[29:45] SPEAKER_03:** In that monolith... I don't want to beat on some of the architectural decisions in the first Ethereum too much, because those guys did an amazing thing in many ways. But there are, I have my nitpicks. And I think JSON-RPC is sort of like a strange interface to the world. We have a converter from JSON-RPC that really it's just querying our stuff in the back end. But what effectively has to happen in there is like, to get any data, you have to start... if you think of the blockchain as like a series of Git commits, every time a block goes through, that's like a commit in Git. And if you want to get any data, you have to literally connect with JSON-RPC and send something through to the VM that goes and does like a checkout at that place in time and pulls that piece of information out. So a lot of overhead, very, very difficult compared to just having a Postgres database with everything and you just do your query and you get whatever you want.

**[30:54] SPEAKER_06:** So I mean, I think a lot of those decisions basically were just straight copied from what Bitcoin was doing, plus randomly pulled out of the air delta. I've heard a lot of people say Ethereum was a science project gone live, or Charles's favorite, "garbage built by amateurs in a rush."

**[31:22] SPEAKER_05:** But it's like Curtis Yarvin said something like, "Ethereum is good at nothing but succeeding."

**[31:32] SPEAKER_03:** There's definitely a cultural difference between sort of hardcore devs and maybe more front-end or business users. And I've found over time that hardcore devs are very suspicious of SQL, whereas sort of front-end and business people love SQL. And I think often, I've had... we've had people at the company over the years who kind of looked at stuff and said, "I really like all this stuff, but all that Postgres stuff there, I'm suspicious of it. We should rewrite it to just store the data in memory using arrays and maps." And so, but of course that's a world that the business people and the front-end people would hate. So I think that was one of our big additions, sort of realizing that we wanted this data to not just be sitting there for the geek teams. We wanted to have an interface where it was easy to get to everything in all of history right away.

**[32:38] SPEAKER_06:** Well, I mean, in this agentic world, Kieren, how do you feel our code base is kind of aligned for agentic usage versus more monolithic clients?

**[33:02] SPEAKER_05:** Yeah, let me apologize to everyone. I'm dealing with a burning smell in the house. Initial triage seems to indicate no obvious danger, but...

**[33:12] SPEAKER_06:** You're not on fire, right?

**[33:14] SPEAKER_05:** I'm not. I checked fairly thoroughly.

**[33:16] SPEAKER_06:** Okay, just making sure.

**[33:18] SPEAKER_05:** So the... yeah, it's a brave new world. The AI is remarkable. Just as an aside, we're wiring up some privacy features right now that Jim is developing, and I was testing them last night. And there was sort of an edge case that Jim hadn't tested yet that I discovered, and like Opus 4.6 was just like, "Yeah, let me just fill that in for you." This is like hard ZK-flavored stuff where you're making exciting Merkle trees and UTXO notes and all that sort of thing. And it seemed to just work.

**[34:01] SPEAKER_03:** And it was like in the middle of explaining the bug to me, and before he finished explaining to me, he was like, "Oh wait, wait, hey, robot's got it."

**[34:07] SPEAKER_05:** It's... so, in a sense it has reduced the need to have beautiful interfaces to everything, because the AI is more patient and can read faster than a human. There was a strange moment, I would say, I don't know, summer 2025. We found at first that the AI could make new things, kind of get a POC done pretty fast, but sort of brittle. But couldn't handle this relatively huge code base that we have. And then one day it was like, oh, not only can it handle it, it can read it way, way faster than I can.

To the point where, the early days I worked on the code base a bunch, but then you end up on the business side as a CEO. And then once you have a BD meeting or two, or an investor meeting or something, you can't code that day. Your brain is shot. But with the AI, I could just kind of ease back into it, get it doing stuff, and then start giving instructions. I could code again. Not all the time, not doing big features usually, or if it is, it tends to be peripheral, not mainline core stuff that needs to be maintained. But getting a first version of a thing out, a UI refactor, fix a bug, et cetera, et cetera.

And so in some ways we have to do nothing. But also the AI does like our API architecture. It just digs through it and finds the thing it needs. And I don't know if you meant the modular components of STRATO or what specifically. But we've got a bunch of processes it runs. It sort of seems to like... sometimes it stops and starts them individually. It's digging through and looking at the sequencer. Like, I was syncing the testnet and it was a little bit stalled, and then it finished when I was doing this privacy testing last night. And then I said, "Hey, just look again." It's like, "Oh yeah, you're right, the blocks got all the way through the pipeline."

So it's so good. I don't know that we need to do anything all that specific. But certainly it likes how it's architected. Maybe... it sometimes has trouble with the auth, in particular on the app site. We have a captcha and stuff. It can't get through the captcha.

**[36:38] SPEAKER_06:** The purpose of the captcha!

**[36:40] SPEAKER_05:** Yes. Give it credentials locally, it can kind of do everything. Obviously, Bob, you developed an MCP, which works well. It doesn't even really need the MCP, but it's good to just have it out there. And we have plans to make a human and agent-friendly CLI. And probably maybe we'll wrap it in skills. I'm not quite sure. MCPs might be the eight-track of AI enablement technologies.

**[37:28] SPEAKER_06:** Yeah, there seems to have been a bit of a crutch that's probably already done.

**[37:38] SPEAKER_05:** Yeah, maybe a more forward-looking... I think everyone in crypto feels like agents are going to be first-class citizens. And honestly, even before agents, so much of on-chain commerce is automated anyway. Like, by volume, it's probably all bots run by sophisticated market makers who have trading backgrounds. And those bots make it possible... by the way, trad-fi is like that too, increasingly, maybe kind of completely now.

Those bots make it reasonably easy for retail to get a good quote. They also liquidate people and this and that. But you need kind of profits for the institutions to come in, and then the competition eventually competes those profits to moderate, and retail gets a good quote when you want to do a swap, right?

So it's kind of like it might get more like that. One good thing is a pretty granular control of the fees. I think the agents can pick whatever chain they want because they're really smart. And if you have high and indeterminate gas, they might just route around you. And so the way we've set things up, we've got fees in our native stable, and we'll probably have all of the native coins swappable for fees soon enough. We haven't done that yet.

I'm considering... there's some of these more agent-native launchpads out there, and I think we are thinking about having kind of a restrained launchpad sort of feature that could help in certain scenarios, like under-collateralized lending. And I think the agents will be good at that. Like, if you're going to have... so most of DeFi has a pool concept. Aave being the biggest, right? Like if you want to borrow, put a whole bunch of money in the pool. It's over-collateralized and there's not really any discretion, for good reason. It's hard to scale discretion on the internet, especially... most unsecured lending that happens has some sort of enforcement threat. So when it's over-collateralized, you just take the collateral. It's kind of always collateralized in some way. It's like, you know the guy, you know where he lives, all that sort of... social shaming, or worse, if someone doesn't.

But I think the agents will be pretty good at that. In time they'll be less emotional than humans. If they have enough context, they don't really get tired. It's funny that they do get tired, right, in the same session. So yeah, I think it's going to be great.

**[40:34] SPEAKER_03:** I'm guessing most of our audience is familiar with AI at the moment. But if you're not using it day to day, I just want to be clear that we're living through, in this couple of months, a huge revolution. There was, like, up until just a couple months ago I would have said AI coding was more of a novelty, something to maybe do a quick prototype, but it was sort of worthless in dealing with a large code base. And that changed really fast, and that was about two months ago maybe. And I've seen all over Twitter, developers sort of saying the same thing.

I was kind of shocked a couple months ago. I went in there and it popped in and just started debugging very complicated bugs in the system in front of my eyes. Like, the screen was scrolling by quickly. It was coming back at the end with amazing solutions to things that would have taken me hours to do. So this is changing fast, and anybody who says they know how it's going to look in a year or two is lying right now. At the very least, what's changed in the last couple of months is going to be a big deal. But it could grow way beyond that too. So we don't quite know yet where this is going, but it's a very useful tool.

**[42:00] SPEAKER_06:** Yeah, I mean it was really with those GPT 5.2 release and Opus 4.5 that were late November, early December. Like, yeah, a massive phase switch. And Claude Code, it's not even around long after that either.

**[42:17] SPEAKER_03:** I was using it for research. I was using the AI for research all the time before that. But now huge areas, like, I just handed over. But we're learning, like, okay, so the story I sort of keep saying is, if you go back and look at the '60s, there was this belief... computers were just a new thing at that time. And they thought that you would be able to soon pop a weather simulation on a computer and be able to forecast the weather a year in advance. "Hey, there's going to be a thunderstorm on May 4th, one year from now, at 4:15 PM."

And of course you can't do that, and we didn't know it yet. And I think something similar is going... there's a similar learning for AI right now. We have lots of guesses about how amazing this stuff's going to be, but we're sort of slowly going through and figuring out what's actually possible and what's not possible. And it's amazing what it's doing already, but we're not sure where it's going to end right now.

**[43:24] SPEAKER_06:** All right. Well, I'm looking at the time, so maybe let's just close out. Victor, with why are we open sourcing and what kind of expectations or hopes do you have because of that?

**[43:39] SPEAKER_01:** So are you asking me? Yeah, like... well, maybe we should start with Dustin, I think.

**[43:51] SPEAKER_04:** Okay. I mean, well, I see open sourcing as both sort of a step towards transparency, auditability, and collaboration. So I mean, one thing I love about the Haskell community is that almost the entire set of libraries and everything is open source on GitHub, on Hackage, etc. And I've really learned a lot just by going through different people's libraries and reading the code, understanding what it does. And I think by us sort of contributing to that open source ecosystem, people can learn what we've been doing and sort of see the innovations that we've brought to the blockchain space. And sort of how STRATO differentiates itself from other blockchains and kind of what we bring to the table.

**[44:39] SPEAKER_05:** Maybe I'll add... you mentioned we had an initial open sourcing effort kind of to show our commitment to it. But there were some efforts to basically... there were a couple things we had to clean up on a one-off basis that we ended up kind of cleaning up permanently. Also, we were still in quite heavy development for version two of our application, and so kind of continued in a closed source format for a while.

But you need to decentralize. We're doing it progressively. I think there is a right level of, especially with new chains, new apps, you do want a little bit of the quality control training wheels in place before you just let the dove free. And we've been kind of like... one's not a good idea. I mean, they're making... I bet compared to the average human, AI code quality is... it's different but it's probably higher. I don't know. They do introduce bugs and they lie to you. They make subtle mistakes.

But it's so fast that whoever is going to try to bring your thing down is using the AI now, and you better just kind of try to stay ahead of it. It's a strange time. You develop pretty AI-native means of working, so that you just can't do stuff slowly anymore because the AI is so fast. You better be kind of faster than the adversary, which is difficult to impossible. But I actually think vibe-coded L1s are probably fine eventually. You just need really good test harnesses and security procedures to catch all of it.

I guess it is a little hard to audit pure AI code. It's getting better, though. Sometimes it just makes too much code. But they're going to do it themselves anyway, right? Like, I don't see... we had an Ethereum vibe-coded L1, right? Already, in like a couple... I saw this on X. So again, you gotta watch it. It's hard to just say, "Do it." But it's getting closer to that. And I think in a year or two, it'll just be better in all ways than humans.

We had Donald Knuth mentioning some problem he was working on that Opus 4.6 solved. He's like 88 now. And I think it helped... it produced 31 proofs, I don't know, maybe one or two of them good, maybe more than that. But we should admit that it's better at coding than we are and then guide it from a more abstracted level.

Go ahead, Jim.

**[48:05] SPEAKER_03:** I'll tell you why we're open sourcing. If we were just trying to sell a product, I wouldn't open source this. We're trying to build a network right now. And nobody wants to use proprietary TCP/IP or something. You need for a network some type of open standards, and this is the reference implementation. We want people to come in here, build other tools that sort of talk in the same language that we do. And we want to make that as easy as possible.

And what I'm really imagining right now is we're about to go into a world where AI is going to need money. And nobody's going to give a computer a bank account. So I think blockchain is the way that AI is going to sort of haggle and purchase stuff from each other. And I want this system to be as simple to use as possible, as open as possible. And so that's the real reason I think that open sourcing is important.

**[49:03] SPEAKER_06:** Yeah, I mean, I think many SaaS platforms are just absolutely screwed, because they're built for humans but they're just terrible for agentic stuff. Whatever, like having to log in and then you've got your crappy website and just really very manually kind of... I mean, computers as a whole, like a lot of it has ended up kind of like paper form stuff got digitized and you haven't really got a lot beyond that. It's just your website's what used to be a form, and you've got your humans logging into a thing, doing a thing, exporting some stuff, copying files. And all of that human shuffling, I think, is dropping away. So anything SaaS-y or anything without a CLI or an API or some easy automation just is going to be routed around.

**[50:13] SPEAKER_05:** Yeah, I've been saying AIs have brought Unix back. Text in, text out, but for the mass market somehow. And it's a good thing. It gets you out of the proprietary data capture to some extent that a lot of platforms depend on. If you get your stuff out, you can take it with you.

**[50:31] SPEAKER_01:** Well, before we wrap up though, Bob, I just want to give you kudos because you've been driving this open source effort. And it is no easy thing to push a 10-year-old code base with all the issues and commits that have happened over those years into the wild. So thanks a lot for keeping us honest with this. We've wanted this to happen for much, much longer, but just getting it to happen has always been a big challenge.

**[50:58] SPEAKER_06:** Well, I mean, back 2016, for real, not 2026, saying the wrong date. When I was doing C++ relicensing, STRATO was another sort of considered possible option at that point, right?

**[51:12] SPEAKER_01:** Yeah.

**[51:14] SPEAKER_06:** But the timing didn't work and what have you. But there we are, 10 years later.

**[51:21] SPEAKER_01:** Ta-da! Nothing goes as fast as we think it will, but I'm glad we're here today.

**[51:27] SPEAKER_06:** Yes, exactly.

**[51:29] SPEAKER_03:** By the way, I just want to say a little AI story to tell you where we're at in the world with AI. In the past when I've done this type of... like, we had to deal with licensing and the product, you always kind of go through package by package, library by library. And you always find something in there that you're like, "Oh, so I kind of messed up there. That one shouldn't be in," or whatever. And then you have to run out and try to find new versions that were actually in a better license for that particular package.

This time it was very different. There were a number of times where we found stuff that was like, "Oops, accidentally put this thing in." And I literally just went to the AI and said, "Write me a new version of this library, but we're just going to open it in a license we like." And it sat there from scratch and wrote a copy of that library in front of me, and it worked. Just like a one-shot, and it worked.

**[52:15] SPEAKER_06:** Let's not say "copy" because that's a bit in breach of license. Let's say "white room reverse engineer." But it wasn't doing a line-by-line copy. It was writing in front of my eyes. But yeah, I mean, I think that will happen with a lot... the kind of NPM micro-package horror era, I think, is over. Because lots of these little things, they can just get bespoke written. I think you're only going to end up with very large, very useful components that it makes no sense to rewrite. But lots of the little plumbing...

**[53:00] SPEAKER_05:** Yeah, you don't need to compare. The end of the GPL.

**[53:06] SPEAKER_01:** Yeah, well, I think we're going to have to rethink security in general. We do have an exciting announcement about that, but we'll leave that to a future one.

**[53:13] SPEAKER_06:** So, all right. So yeah, I mean, so blog post to come out a little later. But the repo, the mono repo, is live on GitHub now. So that is strato-dash-net is the organization, and the package there is STRATO Platform, together with various other already open sourced pieces. So I'm going to dive on in.

About our Twitter handles, that's right. So I'm on Twitter. I am Bob Summerwill, same as my name. Michael is Mike B Tan. Victor is Vic Four Wong. Kieren is K James Lubin. Jim is...

**[54:10] SPEAKER_03:** Jamshid. Jamshid. Jamshid Hummus. I believe, yeah. So yeah, Jamshid Hummus.

**[54:20] SPEAKER_06:** There you go. And Dustin, I'm afraid you'll have to sell your own. Are you muted?

**[54:24] SPEAKER_04:** My Claude bot is currently running my Twitter under a pseudonym, but the handle is Semi Groupoid.

**[54:31] SPEAKER_06:** Okay, Groupoid. Yeah, I don't know. Yeah, all right. So yeah, open Claude it up, get Claude code hacking on the platform. All the best, everyone. Take care, everyone.

**[54:44] SPEAKER_01:** Bye, bye. Thanks, everybody.

**[54:47] SPEAKER_06:** All right. Okay, so hopefully that's a wrap this time. We'll find out. Catch you later.