**[00:03] SPEAKER_00:** Okay.

**[00:03] SPEAKER_01:** Boom.

**[00:04] SPEAKER_00:** We are live. Happy Wednesday, everybody. Hope you're all doing well. March 4, 2016. We're into the new month, 2026.

**[00:18] SPEAKER_02:** I'm sorry, he said 2016.

**[00:22] SPEAKER_03:** Did I?

**[00:22] SPEAKER_01:** 10 years ago.

**[00:24] SPEAKER_02:** Yes. Time has flown, hasn't it?

**[00:27] SPEAKER_00:** That's it. I have to calculate my age. I don't know what year it is, even how old I am. But yes. So today we have a goodly number of people here. Myself as usual, Bob Summerwill, head of ecosystem, Kieren James-Lubin, the CEO down at the bottom there. Victor Wong, top right. Michael, who often joins us, Michael Tan. And we have a guest appearance here from Dustin Norwood, who has the honor of being the number one ranked top contributor all time to the Strato code base. We're talking about open sourcing today. So it seemed only right to have Dustin here. Before we go into open sourcing, we've just got a little bit for Michael to talk about.

**[01:26] SPEAKER_03:** Sure.

**[01:26] SPEAKER_04:** Let me just share my screen really quickly. So, yeah, as a lot of you know, we have wrapped up the points program for our first season. A million points distributed, be sure to claim your points on the My Rewards page. There was a lot of great usage, some great APRs on different pools and different actions on the site, and check where you are on the leaderboard and be ready for season two coming up soon.

**[02:02] SPEAKER_00:** Kaboom. Short and sweet. So, yeah, open sourcing. It's a big day. I was looking back, our first step towards this was the snapshot that we released in January of last year. But today we are doing a full open sourcing and release of the entirety of everything that we have done as a project, as a company. Going back to September 2014 was when the initial commit was from Jim on EthereumH. At the time it was EthereumH. Right, that was the initial name. And then Kieren joined that effort quite shortly. So Kieren, how did all of this stuff start? Like this long journey.

**[03:08] SPEAKER_02:** Wow. Yeah, good question. I guess to go back to let's say March, April 2014, I was in grad school at UC Berkeley and going into my qualifying exam in the math department. And it was quite painful, but I passed it and I was sort of looking for something to do in the summer. I recall almost taking a machine learning job, which I'm sure would have been interesting, but I was lucky enough to get my hands on the Ethereum white paper. And luckier still to start work on it, I guess, maybe more of a May kickoff in earnest. I leaned all the way into it through those summer months and contacted a bunch of people, one of them being former—still informal—advisor Steve Hsu. Steve is a fairly famous theoretical physicist, formerly the VP of research at Michigan State. He's still there as a professor. And Steve put me in touch with Jim maybe around July, August, I haven't pulled the emails up. At the time, Jim was living pretty nearby where I was in the Bay Area. And so as soon as I'd come back from the summer, we met up and kind of hit it off and just started. Jim got interested enough to start building EthereumH, and fairly shortly later I started contributing as well.

So yeah, that's the really brief origin on the code base. Victor, Jim, and I are the co-founders. We all met up January 2015 and that really kicked things into motion more formally around actually two conferences I was hosting. One called Crypto Economicon. The videos are still available on YouTube. Bobby, I think I sent that link to you, right? You were able to pull them up. Yeah, some classics in there. We should maybe put it in the show notes or something. A who's who of faces showed up to that event, and a more commercial conference with O'Reilly Media at that time, which sort of saw there was definitely a feeling like we're in the room. It's like being in the room with Tim Berners-Lee or something. Like this thing is going to be big. The businessy types see it, the radical open source devs see it, and we got to just sort of jump in. And there's been a lot of code since then.

**[06:13] SPEAKER_00:** So Jim, I was just saying at the start, 14th of September 2014 was the first commit there. What were you thinking when you started, where this was gonna go?

**[06:33] SPEAKER_01:** I mean, like on day one, I just wanted to understand it. I kind of believe you can't understand something unless you are understanding it through the code. And Ethereum's awesome. I had a sense that there was something awesome going on there. But when I first started to look into it to understand how it worked, a lot of the videos that had been put out were sort of hyperbole and it didn't make sense to me. A typical video would be like, "Ethereum is the fabric that underlies society. It is the future. It is how we will build a new society." And I was like, okay, but what is it? And then I found the code base. So I was like, okay, let me start playing with this.

Just reading through a code base, it's not interactive. So I was like, let me see how this thing actually works. And I pulled up my favorite programming language—Haskell should be all of your favorite programming language, by the way—and I found a bootnode and I connected to it, and I realized that commands were coming through to me. So I started adding code to talk back to these nodes and slowly picked up what it was and how it worked inside and what a blockchain is. And all of that was the beginning. But soon after that, I realized that I'd put together enough lines of code that I had built a tool that could be useful to the world.

**[08:12] SPEAKER_00:** What is a blockchain? What was your conclusion?

**[08:18] SPEAKER_01:** It's a long, technical... Okay, no, I'll give you the more poetic answer. I think it is the fabric that underlies society...

**[08:25] SPEAKER_02:** No, I mean...

**[08:29] SPEAKER_01:** It's incentives. That's what it is. You have a lot of people sitting around wanting to contribute to society, and yet it's hard to coordinate everyone to do things in aligned ways. And once you build some type of money, you can sort of align lots of groups of people to do something together. And so that's what it really put into the world. It's incentives to get distributed characters from around the world to all be aligned in one direction. And you can sort of craft what that direction is.

**[09:14] SPEAKER_03:** By the way, Jim, to defend that "it's the underpinning of the new world" idea—Vitalik's latest post, literally today, is about exactly that. He's talking about sanctuary tech and how Ethereum has to move beyond finance. So that thread has never left.

**[09:35] SPEAKER_01:** I mean, I did do the full circle. I was kind of laughing at what is all this crazy hyperbole, and then I spent a lot of time understanding the technology, and then by the end, something clicked in my mind and I was like, holy cow. This really is the underpinning of the new world. And this is how we're going to build a new society. You need to have some way for coordination. I mean, you can get a certain amount of free work in the world. I think Wikipedia shows that if you just put up a tool and lower the barrier of doing stuff, people will just come and do free work for you. But if you want to go a little bit beyond that, you have to start aligning people to some sort of common vision. And you need an incentive for that.

**[10:17] SPEAKER_03:** Not to call you out, Jim. But just a reminder, at that time, we were also thinking about doing a startup together. And the way you presented it to me was like, "This might be amazing, or this might make absolutely no sense. I'm not exactly sure which."

**[10:32] SPEAKER_01:** Well, yeah. I mean, there are network effects and all this thing. Once I started understanding the technology, I said, okay, this is amazing. But it also might be that nobody will use it, and it'll just be an amazing technology that languishes. And it turns out that other people were interested. I remember another stepping stone was when we started hanging out at ConsenSys more and more, and I saw so many excited people there. I said, "There's no way this is going to fail. There are just too many people who are really excited about this at this moment right now." People willing to leave jobs, give up everything, and come and just work on this stuff. So this is going to be something. And it was.

**[11:23] SPEAKER_00:** And then how did things move from building a Haskell client into Strato being envisaged, and what was the initial kind of vision?

**[11:37] SPEAKER_02:** So I guess we've always been a certain kind of pragmatic people. And through building the client and then also trying to use the early flavors of the RPC and all the tooling, we realized at day one, the DevEx was just not there. Today it's much better. The tools are reasonably mature, although there are still things that bother me about the Ethereum DevEx that are just choices that were made that made things unnecessarily difficult for no real reason. But, you know, you can also just AI around a lot of it now. But it was really difficult to get even a node up. And then once you've got the node up, you're configuring connections to it.

And they were initially incredibly complex. So for some reason—and maybe a good reason, maybe not—the Ethereum people felt like they had to write to a virtual machine, which we all know and love as the EVM. And they created maybe four competing high-level languages, or three very early on. There was LLL, there was Serpent. Solidity was a little later. Right. There was the Go-flavored one.

**[13:08] SPEAKER_00:** I found out recently that had got an earlier code name as well, which was HLL. So High Level Language was Mutan. But yeah, that was abandoned. That was done by Jeff Wilcke.

**[13:19] SPEAKER_01:** LLL is Lisp Like Language, by the way.

**[13:23] SPEAKER_02:** Yeah, I'm sorry. LLL was Lisp Like Language.

**[13:28] SPEAKER_00:** Lisp Like Language or Low Level Language, I think it was.

**[13:31] SPEAKER_02:** I think yes, this is it. There was a lot of nerd one-upmanship in early Ethereum. Maybe this is common in the open source space in general. It reminds me of subtle swipes that academics put in their papers or something, the naming of things. But you know, it kind of works. There was this weird all-against-all but all-for-one competition in early Ethereum. And I guess we got stuck with Solidity, which you know, is fine. Like, it works.

**[14:06] SPEAKER_01:** Well, go on, I got a point, but I'll let you finish.

**[14:13] SPEAKER_02:** So I guess we were like, okay, this tooling is no good. You can't get the node up. The APIs are weird. These languages are moving. So let's just solve that. At that O'Reilly conference I put on, Chain.com was there, back when Chain.com was a REST API infrastructure provider for Bitcoin, which was maybe for Bitcoin a model that was doomed. And Ethereum RPC providers that stuck came later than we did. That was the first thing we did. We were like, all right, let's get an API up. Let's make the routes sensible and let people get access to the live net. I guess that initially got called Strato, that bundle of things.

In doing so, somehow we were enterprise or institutional coded, and it was not at all our intention. We thought it would be just an easier developer API, and found the hardcore devs really liked the standard RPC interface, and the enterprise devs were like, "Oh, I can put this in Postman." We got pulled in that direction, and over the years, going from POCs to pilots to powering consortia and all that sort of thing... and I guess the aggregated name for all of that was Strato. We sort of launched by Devcon 1. So this is the end of 2015. We were still working within ConsenSys at that time and had partnered with Microsoft to kind of create that category. I'll be right back in a second. I'll be two minutes. I have to check on something. Sorry guys.

**[16:14] SPEAKER_00:** Maybe Victor can continue here. So from my memory, it was Devcon 1 where I first saw the BlockApps name and branding. And I was aware of EthereumH existing, but not really of what was going on at that point.

**[16:40] SPEAKER_03:** So you know, we've always sort of followed this lean philosophy, and I think our first test ground was the launch of Ethereum. We did the first hackathon at ConsenSys, right? So that was August, I think 2015. And it was interesting because people were building stuff really for the first time. People kind of built prototypes of a lot of the things we see now. There was a GameFi app, there were traceability apps, there were sort of DeFi-ish apps.

One of the interesting things is some of the judges were part of the more institutional traditional world. That's where they learned about what we were doing. And they were like, "Oh well, what you're doing—yeah, we need a REST API to write against. We really want to use this." Microsoft came up and said, "Hey, if you guys want to do this with us, we want to promote Ethereum, but you guys have to offer a mode that allows you to run as a private blockchain. We don't want to have to make it a requirement that people have to go and acquire some ETH in order to do this."

And that was really kind of between August and I think Devcon was November. We were madly working to try to get this working in a way that we could deploy this on Azure and do that demo of "write a dapp in 5 minutes" for Devcon 1. Interestingly, we were not their first choice. Another project which did EthereumJ, they were actually part of this. Microsoft wanted to work with them because they were a Java-based client. We were this crazy Haskell thing. Right, Jim?

**[18:51] SPEAKER_01:** Microsoft has Haskell.

**[18:56] SPEAKER_03:** Yeah, there are. And you know a bunch of the researchers are there. But you remember those conversations, they were like, "Hey, if this is going to be widely adopted, Java is the most interesting thing. But you guys are interesting too, and you guys come along with it."

**[19:11] SPEAKER_00:** And you're telling me if Roman Mandeleil had been a bit more business savvy and stable, that the whole path of the company may have been quite different?

**[19:21] SPEAKER_03:** Absolutely. I had some background with this because in my previous company I had worked with Microsoft before in their app world, but it took forever. It took like eight months for me to get a meeting with Microsoft to start talking. So the fact that they came to us and were like, "Hey, we want to do this thing with you, but we want to launch it in two months, together"—it was super. I realized the opportunity, and yeah, I think Roman had other priorities at the time and kind of let the ball drop, and that kind of kicked off everything.

And then really, for that time, we were like the only option if you wanted to launch on Azure. Azure was just launching really at that time, and so lots of people were getting free credits and a lot of people just wanted to say, "Hey, I heard about this weird Ethereum blockchain thing. Can I just try it?" Oh, they clearly have a thing, and they tried it, and literally hundreds of people used our solution very, very quickly.

Most of them were complete nonsense. They were just trying to use it as a database and swap it out and do that kind of thing. But there were a few people who figured out what they could build with it enough that they wanted to build bigger projects, but they didn't know who to go to. And so that was really the next evolution of Strato. It was like, okay, now we have to support these bigger projects where it's not just a dev node where someone is connecting to it. It's like a real network with multiple parties. And they have security ops requirements and DevOps teams and all of these things. We had to evolve the product in that way.

**[21:18] SPEAKER_00:** I seem to remember that Geth was on there as well at that start, that you could just launch a public Geth node.

**[21:25] SPEAKER_03:** It wasn't part of the original launch for Blockchain as a Service. It did get added later, if I recall correctly. And you know, I think someone put it on AWS just as an option. Like, it wasn't an official image or anything. They just put it on there. That might have been us for various reasons.

**[21:54] SPEAKER_00:** I mean, I remember there was a period shortly afterwards as well where people could add their own as well, and there was this whole range of total scam projects slapping their crappy software up and saying, "Oh look, we're partnering with Microsoft." It's like, no, no, no.

**[22:08] SPEAKER_03:** Yeah. And it was very funny because at the first Consensus conference we were kind of hosting a hackathon there, and there was a very early version of Hyperledger there. I remember there was a room where all the people were hacking it, and our room was full, and there was like one person in the Hyperledger room, which was very sad at the time.

**[22:46] SPEAKER_00:** So Jim, would you maybe like to say a little bit about the architecture of the code base? Like, what is being open sourced here? What have we got?

**[23:00] SPEAKER_01:** Well, it's one of our nodes. You know what, let me sort of answer your question by going back to a point I was going to make before, turning the clock back to the various languages being used in the blockchain. I guess I always considered it sort of a mistake that the EVM resembled opcodes of a CPU. My evidence in this favor is that I've lived through this before. Back in the 90s when the browser was kind of getting bigger and HTML had started to become a standard, people realized that they needed to have some way to program web pages too. And the first real attempt at doing this was actually a sort of large opcode CPU-like plugin, which was the Java applet back in the day. It was bulky, ugly. You'd sort of go to a webpage and it was almost like booting up your computer. You'd watch the web page struggle a little bit and then kind of come up. And then eventually you might get something that looked a little bit like a computer screen sitting in the middle of your web page. And that failed pretty miserably and it was replaced by JavaScript, as we all know and love now, which was a higher-level scripting language that just sort of runs in various threads in the background in your browser.

One of the biggest changes that we made is that although in the early days we certainly had the EVM in there—and the code is actually still in there, but mostly commented out right now—we have something called SolidVM, which is a Solidity-based, JavaScript-style language that runs as your contracts. One of the big differences is that since everything is opcode-based in the Ethereum network itself, you have to compile everything down and you can't really see what your contracts are doing unless you try to decompile it or something. With us we just keep the Solidity or the SolidVM source code right there. So you can visit any contract and just look at what's running at any given time. Or if you send a command in, you just send the Solidity command right in the transaction. So that's one of the big things, is that we're not based on opcodes, we're based on this slick scripting language running in the background. SolidVM, that's it. Questions or comments?

**[26:09] SPEAKER_00:** Maybe if I reach out to Dustin. I was just looking. As far as I can see, your first commit was the 9th of August 2017. So you joined in this journey not terribly long after all of this. And I mean, one of the key things I remember from my time at the EEA, which is really where I met Victor and Kieren first, was that the differentiation that there was versus all of the other clients at the time is they were all monolithic single executables. But Strato is very much not that way. So how is it?

**[26:55] SPEAKER_05:** Yeah, so Strato instead runs as a set of microservices that for the most part are connected using Kafka as sort of an inter-process communication bus. So whereas with Geth and maybe other clients, it all runs as a monolith, as one program, each component of the node is its own process. So like the VM that runs SolidVM, as Jim just mentioned, it's its own process. The P2P module runs as its own process. The Ethereum discovery sequencer that sort of orders all the transactions and blocks before handing it off to the VM, that's its own process. The API, et cetera.

And this makes it a lot more robust because if one thing goes down, it can be restarted without having to take the entire node down. But also it gives some nice replay properties where, since we use Kafka, we can rerun a second instance of each executable and it will rerun through the logs from Kafka and you can rederive the same state. It really helps with debugging. Of course, there are some things that might be a little trickier, such as tracing a certain message through the entire platform, but I think overall it gives a lot of benefits versus the monolith architecture.

**[28:33] SPEAKER_01:** Yeah, it's a full separation of concerns. The VM is just a monster that sits there and gobbles up all the transactions coming at it through Kafka and then outputs all the data changes on the other end. And we have various other things in there. We have indexers. One of the things that we added also is at the end of all the processing, just built into the system, are these PostgreSQL indexers. Everything mapped up from the VM goes to another Kafka stream and the indexers just gobble up all that stuff as it comes in and sit there and fill in tables all over the place. So we have all of the state and history just there for a quick SQL query. So you can see the whole history of the blockchain in the SQL query.

**[29:33] SPEAKER_00:** Yeah, I guess that is really very different to lots of other clients, right? Because it's sort of a bit more like some of the characteristics that you get off archival nodes in that monolith.

**[29:49] SPEAKER_01:** I don't want to beat on some of the architectural decisions in the first Ethereum too much, because those guys did an amazing thing in many ways. But I have my nitpicks, and I think JSON-RPC is sort of a strange interface to the world. We have a converter from JSON-RPC that really is just querying our stuff in the back end. But what effectively has to happen in there is, to get any data, you have to think of the blockchain as a series of Git commits. Every time a block goes through, that's like a commit in Git. And if you want to get any data, you have to literally connect with JSON-RPC and send something through to the VM that goes and does a checkout at that place in time and pulls that piece of information out. So a lot of overhead. Very difficult compared to just having a PostgreSQL database with everything where you just do your query and you get whatever you want.

**[30:56] SPEAKER_00:** I mean, I think a lot of those decisions basically just were straight copied from what Bitcoin was doing, plus drawn randomly out of the air. You know, I've heard a lot of people say Ethereum is a science project gone live. Charles's favorite: garbage, built by amateurs in a rush.

**[31:24] SPEAKER_02:** It's like Curtis Yarvin said something like "Ethereum is good at nothing but succeeding."

**[31:32] SPEAKER_01:** There's definitely a cultural difference between hardcore devs and maybe more front-end or business users. I've found over time that hardcore devs are very suspicious of SQL, whereas front-end and business people love SQL. Often we've had people at the company over the years who looked at stuff and said, "I really like all this stuff, but all that PostgreSQL stuff there, I'm suspicious of it. We should rewrite it to just store the data in memory using arrays and maps." But of course, that's a world that the business people and the front-end people would hate. So I think that was one of our big additions, realizing that we wanted this data to not just be sitting there for the geek teams. We wanted to have an interface where it was easy to get to everything in all of history right away.

**[32:43] SPEAKER_00:** So in this agentic world, Kieren, how do you feel our code base is aligned for agentic usage versus more monolithic clients?

**[32:58] SPEAKER_01:** Yeah.

**[32:59] SPEAKER_02:** Let me apologize to everyone dealing with the burning smell in the house. Initial triage seems to indicate no obvious danger.

**[33:10] SPEAKER_03:** You're not on fire, right?

**[33:12] SPEAKER_02:** I checked fairly thoroughly.

**[33:14] SPEAKER_03:** Okay. Just to make sure.

**[33:17] SPEAKER_02:** Just making sure. So yeah, it's a brave new world. The AI is remarkable. Just as an aside, we're wiring up some privacy features right now that Jim is developing. And I was testing them last night and there was sort of an edge case that Jim hadn't tested yet that I discovered. And Opus 4.6 was just like, "Yeah, let me just fill that in for you." This is hard ZK flavored stuff where you're making exciting Merkle trees and UTXO notes and all that sort of thing. And it seemed to just work. And he was in the middle...

**[34:05] SPEAKER_01:** ...of explaining the bug to me, and before he finished explaining it to me, he was like, "Oh wait, wait, the robot's got it."

**[34:12] SPEAKER_02:** It has in a sense reduced the need to have beautiful interfaces to everything because the AI is more patient and can read faster than a human. There was a strange moment, I would say summer 2025. We found at first that the AI could make new things, kind of get a POC done pretty fast, but sort of brittle, but couldn't handle this relatively huge code base that we have. And then one day it was like, oh, not only can it handle it, it can read it way, way faster than I can. In the early days I worked on the code base a bunch, but then you end up on the business side as a CEO, and once you have a BD meeting or two or an investor meeting, your brain is shot so you can't code that day. But with the AI, I could just kind of ease back into it, get it doing stuff, and then start giving instructions. I could code again.

Not all the time, not doing big features usually, or if it is, it tends to be peripheral, not mainline core stuff that needs to be maintained. But getting the first version of a thing out, a UI refactor, fixing a bug, et cetera, et cetera. In some ways we have to do nothing. The AI just digs through our API architecture and finds the thing it needs. I don't know if you meant the modular components of Strato specifically, but we've got a bunch of processes that run. It seems to sometimes stop and start them individually. It's digging through and looking at the sequencer. I was syncing the testnet and I think it was a little bit stalled, and then it finished when I was doing this privacy testing last night. And then I said, "Hey, just look again." It's like, "Oh yeah, you're right. The blocks got all the way through the pipeline."

It's so good. I don't know that we need to do anything all that specific, but certainly it likes how it's architected. Maybe sometimes it has trouble with the authentication in particular. On the app side we have a CAPTCHA and stuff. It can't get through the CAPTCHA, but if you give it credentials...

**[36:51] SPEAKER_01:** That's the purpose of the CAPTCHA.

**[36:53] SPEAKER_02:** Yes. Give it credentials locally, it can kind of do everything. Obviously Bob, you developed an MCP which works well. It doesn't even really need the MCP, but it's good to just have it out there. And we have plans to make a human- and agent-friendly CLI, and maybe we'll wrap it in skills, I'm not quite sure. MCPs might be the eight-track of AI enablement technologies.

**[37:28] SPEAKER_00:** Yeah, I mean they seem to have been a bit of a crutch that's probably already done.

**[37:37] SPEAKER_02:** Another thing, maybe more forward-looking. I think everyone in crypto feels like agents are going to be first-class citizens. Honestly, even before agents, so much of on-chain commerce is automated by volume. It's probably all bots run by sophisticated market makers who have trading backgrounds and so on. TradFi is like that too, increasingly. Those bots make it reasonably easy for retail to get a good quote. They also liquidate people and so on. You need profits for the institutions to come in, and then the competition eventually competes those profits to moderate and retail gets a good quote when you want to do a swap. So it's gonna get more like that.

One good thing is a pretty granular control of the fees. I think the agents can pick whatever chain they want because they're really smart, and if you have high and indeterminate gas, they might just route around you. So the way we've set things up, we've got fees in our native stablecoin, and we'll probably have all of the native coins swappable for fees soon enough. We haven't done that yet. I am considering these more agent-native launchpads out there, and I think we are thinking about having a restrained launchpad sort of feature that could help in certain scenarios like undercollateralized lending. I think the agents will be good at that.

If you're going to have most of DeFi has a pool concept like Aave being the biggest. If you want to borrow, you put a whole bunch of money in the pool. It's overcollateralized, and there's not really any discretion for good reason. It's hard to scale discretion on the internet, especially most unsecured lending that happens has some sort of enforcement threat. So when it's overcollateralized, you just take the collateral. It's always collateralized in some way. But I think the agents will be pretty good at that. In time they'll be less emotional than humans. If they have enough context, they don't really get tired. It's funny that they do get tired though, in the same session. So yeah, I think it's going to be great.

**[40:31] SPEAKER_01:** I was going to say, I'm guessing most of our audience is familiar with AI at the moment, but if you're not using it day-to-day, I just want to be clear that we're living through a huge revolution right now in these couple of months. Up until just a couple of months ago, I would have said AI coding was more of a novelty, something to maybe do a quick prototype, but it was sort of worthless in dealing with a large code base. And that changed really fast. That was about two months ago, maybe. And I've seen all over Twitter developers saying the same thing. I was shocked. A couple of months ago I went in there, and it popped in and just started debugging very complicated bugs in the system in front of my eyes. The screen was scrolling by quickly. It was coming back at the end with amazing solutions to things that would have taken me hours to do. This is changing fast, and anybody who says they know how it's going to look in a year or two is lying to you right now. At the very least, what's changed in the last couple of months is going to be a big deal, but it could grow way beyond that too. We don't quite know yet where this is going, but it's a very useful tool.

**[41:59] SPEAKER_00:** Yeah, I mean, it was really with the GPT-5.2 release and Opus 4.5 that came out late November, early December—a massive phase switch. And Claude Code's not even been around long after that either.

**[42:17] SPEAKER_01:** I was using the AI for research all the time before that. But now huge areas I just hand it over. But we're learning. The story I sort of keep saying is, if you go back to the 60s, there was this belief that computers were a new thing, and they thought that you would be able to soon pop a weather simulation on a computer and be able to forecast the weather a year in advance. "Hey, there's going to be a thunderstorm on May 4, one year from now at 4:15 PM." And of course you can't do that. And we didn't know it yet. I think something similar is going on. There's just a similar learning for AI right now. We have lots of guesses about how amazing this stuff is going to be, but we're slowly going through and figuring out what's actually possible and what's not possible. It's amazing what it's doing already, but we're not sure where it's going to end right now.

**[43:21] SPEAKER_00:** All right, well, I'm looking at the time, so maybe let's close out. Victor, why are we open sourcing, and what kind of expectations or hopes do you have because of that?

**[43:38] SPEAKER_03:** Sorry, you're asking me? Well, maybe we can start with Dustin, I think.

**[43:46] SPEAKER_00:** Okay.

**[43:49] SPEAKER_05:** I mean, I see open sourcing as a step towards transparency, auditability, and collaboration. One thing I love about the Haskell community is that almost the entire set of libraries and everything is open source on GitHub, on Hackage, et cetera. And I've really learned a lot just by going through different people's libraries and reading the code, understanding what it does. By us contributing to that open source ecosystem, people can learn what we've been doing and see the innovations that we've brought to the blockchain space and sort of how Strato differentiates itself from other blockchains and what we bring to the table.

**[44:45] SPEAKER_02:** Maybe I'll add, we had an initial open sourcing effort to show our commitment to it, but there were a couple of things we had to clean up permanently. Also we were still in quite heavy development for version two of our application and continued in a closed source format for a while. But you need to decentralize. We're doing it progressively. I think there is a right level of quality control training wheels in place before you just let the dev run free, especially with new chains and new apps. And we've been vibe-coded.

**[45:52] SPEAKER_00:** Vibe-coded L1s are not a good idea.

**[45:54] SPEAKER_02:** I mean, compared to the average human, AI code quality is different, but it's probably higher. They do introduce bugs, they make subtle mistakes, they lie to you. But it's so fast that whoever is going to try to bring your thing down is using the AI now, and you better try to stay ahead of it. It's a strange time. Develop pretty AI-native means of working so that you just can't do stuff slowly anymore because the AI is so fast. You better be faster than the adversary, which is difficult to impossible.

But I actually think vibe-coded L1s are probably fine. Eventually you just need really good test harnesses and security procedures to catch all of it. I guess it is a little hard to audit pure AI code. It's getting better though. Sometimes it just makes too much code. We had an Ethereum vibe-coded L1 already, I saw this on X. So you gotta watch it. But it's getting closer to that, and I think in a year or two, it'll just be better in all ways than humans. We had Donald Knuth mentioning some problem he was working on that Opus 4.6 solved. He's 88 now. I think he helped it. I think it produced 31 proofs. Maybe one or two of them good, maybe more than that. But we should admit that it's better at coding than we are, and then guide it from a more abstracted level. Go ahead, Jim.

**[48:04] SPEAKER_01:** I'll tell you why we're open sourcing. If we were just trying to sell a product, I wouldn't open it. We're trying to build a network right now, and nobody wants to use proprietary TCP/IP. For a network, you need open standards. And this is the reference implementation. We want people to come in here, build other tools that talk in the same language that we do, and we want to make that as easy as possible. What I'm really imagining right now is we're about to go into a world where AI is going to need money, and nobody's going to give a computer a bank account. So I think blockchain is the way that AI is going to haggle and purchase stuff from each other. And I want this system to be as simple to use as possible, as open as possible. So that's the real reason I think that open sourcing is important.

**[49:05] SPEAKER_00:** Yeah, I mean, I think many SaaS platforms are just absolutely screwed because they're built for humans, but they're terrible for agentic stuff. Having to log in, and you've got your crappy website—really very manually kind of digitizing paper forms. You haven't really got a lot beyond that. It's just a website that used to be a form, and you've got humans logging into a thing, exporting some stuff, copying files. All of that human shuffling I think is dropping away. So anything without a CLI or an API or some easy automation is just likely to be routed around.

**[50:11] SPEAKER_02:** Yeah, I've been saying AIs have brought UNIX back. Text in, text out, but for the mass market somehow. And it's a good thing. It gets out of the proprietary data capture that a lot of platforms depend on. If you get your stuff out, you can take it with you.

**[50:30] SPEAKER_03:** Well, before we wrap up though, Bob, I just want to give you kudos because you've been driving this open source effort, and it is no easy thing to push a 10-year-old code base with all the issues and commits that have happened over those years into the wild. So thanks a lot for keeping us honest with this. We've wanted this to happen for much, much longer, but just getting it to happen has always been a big challenge.

**[50:57] SPEAKER_00:** Well, back in 2016 for real—not 2026, saying the wrong date—when I was doing C++ relicensing, Strato was another considered possible option at that point, but the timing didn't work. But there we are ten years later. Ta-da.

**[51:23] SPEAKER_03:** Nothing goes as fast as we think it will, but I'm glad we're here today. Exactly.

**[51:28] SPEAKER_01:** By the way, I just want to say a little AI story to tell you where we're at in the world with AI. In the past when I've done this type of licensing thing, you always go through package by package, library by library, and you find something in there where you're like, "Oops, I kind of messed up there, that one shouldn't be in." And then you have to run out and try to find new versions that were actually better licensed for that particular package. This time it was very different. There were a number of times where we found stuff that was like, "Oops, accidentally put this thing in," and I literally just went to the AI and said, "Write me a new version of this library, but we're just going to open it in a license we like." And it sat there and wrote a copy of that library from scratch in front of me. And it worked. Just like a one-shot, and it worked.

**[52:19] SPEAKER_00:** Let's not say "copy" because that's a bit in breach of license. Let's say "clean-room reverse engineer."

**[52:28] SPEAKER_01:** It wasn't doing a line-by-line copy, it was writing in front of my eyes.

**[52:34] SPEAKER_00:** But yeah, I think that will happen. The npm micro-package horror era I think is over because lots of these little things can just get bespoke written. I think you're only going to end up with very large, very useful components where it makes no sense to rewrite them. But lots of little plumbing, you can just do your own.

**[53:01] SPEAKER_02:** You know, it compares to the end of the GPL.

**[53:04] SPEAKER_03:** Yeah, well, I think we're going to have to rethink security in general. We do have an exciting announcement about that, but we'll leave that to a future one.

**[53:17] SPEAKER_00:** All right, so yeah. Blog post to come out a little later, but the monorepo is live on GitHub now. So that is stratonet is the organization, and the package there is strato-platform together with various other already open-sourced pieces. So dive on in.

**[53:45] SPEAKER_01:** Bob, our Twitter handles.

**[53:48] SPEAKER_00:** That's right. So I'm on Twitter as BobSummerwill, same as my name. Michael is Mike B. Tan. Victor is vicforwong. Kieren is kjameslubin. Jim is jamshid. And Dustin, I'm afraid you'll have to say your own.

**[54:19] SPEAKER_03:** Are you muted?

**[54:22] SPEAKER_05:** My Claude bot is currently running my Twitter under a pseudonym. But the handle is semigroupioid.

**[54:32] SPEAKER_02:** Semigroupioid?

**[54:34] SPEAKER_05:** Yeah.

**[54:38] SPEAKER_00:** All right, so yeah, Claude it up. Get Claude Code hacking on the platform. All the best everyone.

**[54:48] SPEAKER_03:** Take care everyone.

**[54:49] SPEAKER_00:** Bye-bye everybody. All right. Okay, so hopefully that's at 1080p this time. We'll find out. Catch you later.