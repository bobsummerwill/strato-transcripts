**[00:03] SPEAKER_00:** Okay.

**[00:03] SPEAKER_01:** Boom.

**[00:04] SPEAKER_00:** We are live. Happy Wednesday, everybody. Hope you're all doing well. March 4, 2016. We're into the new month, 2026.

**[00:18] SPEAKER_02:** I'm sorry, he said 2016.

**[00:22] SPEAKER_03:** Did I?

**[00:22] SPEAKER_01:** 10 years ago.

**[00:24] SPEAKER_02:** Yes. Has flown, hasn't it?

**[00:27] SPEAKER_00:** That's it. I have to calculate my age. I don't know what year it is, even how old I am. But yes. So today we have a goodly number of people here. Myself as usual, Bob Somewell, head of ecosystem, Kieran James Lubin, the CEO down the bottom there. Victor Wong, top right. Michael, who often joins us, Michael Tan. And we have a guest appearance here from Dustin Norwood, who has the honor of being the number one ranked top contributor all time to the Strato code base. We're talking about open sourcing today. So seemed only right to have Dustin here. Before we go into open sourcing, we've just got a little bit for Michael to talk about.

**[01:26] SPEAKER_03:** Sure.

**[01:26] SPEAKER_04:** Let me just share my screen really quickly. So, yeah, as a lot of you know, we have wrapped up the points program for our first season. A million points distributed, you know, be sure to claim your points on the My rewards page. There was a lot of great usage, you know, some great aprs on different pools and different actions on the site and check where you are, the leaderboard and be ready for season two coming up soon.

**[02:02] SPEAKER_00:** Kaboom. Short and sweet. So, yeah, open sourcing. So, you know, it's. It's a big day. I was looking back, you know, we had a. Our first step towards this was the snapshot that we released in January of last year. But then today we are doing a full open sourcing and release of the entirety of everything that we have done as a project, as a company. Going Back to, to September 2014 was when the initial commit was from, from Jim on, on Ethereum H. At the time it was Ethereum H. Right, that was the initial name. And then Kieran joined that effort quite shortly. So Kieran, like how did all of this stuff start? Like this long journey.

**[03:08] SPEAKER_02:** Wow. Yeah, good, good question. I guess like, so I had worked to go back to let's say March, April 2014. I was in grad school at UC Berkeley and going into my qualifying exam, I was in the math department. And it was quite painful, but I passed it and I was sort of looking for something to do in the summer. Recall almost taking like a machine learning job, which I'm sure would have been interesting, but I was lucky enough to get my hands on the Ethereum white paper. And luckier still to start Work on it, I guess, you know, April maybe more of a May kickoff in earnest and kind of. Yeah, just sort of. So leaned all the way into it through those summer months and contacted a bunch of people, one of them being kind of former still informal advisor Steve Shu. Steve is a fairly famous theoretical physicist, formerly the head of research, VP research at Michigan State. He's still there as a professor. And Steve put me in touch with Jim maybe around July, August, like I don't, I haven't pulled the emails up and you know, at the time Jim was living pretty, pretty nearby where I was in the Bay Area. And so as soon as I'd kind of come back from the summer, we. Oh, and here's Jim now. Hello. We, we met up and kind of hit it off and just started, you know. Jim got interested enough to start building Ethereum H and fairly shortly later I started contributing as well. So yeah, that's the really brief origin on the code base. Victor, Jim and I are the co founders. We all met up January 2015 and that really kicked things into motion more formally around actually two conferences I was hosting, one called Crypto Economicon. The videos are still available on YouTube. Bobby, I think I sent that link to you, right? You were able to. Yeah, yeah, some, some classics in there. We should maybe put it in the show notes or something. Some, a who's who of faces showed up to that event and a more kind of commercial conference with O'Reilly Media at that time which sort of saw there was definitely a feeling like, you know, we're in the room. It's like being in the room with Tim Berners Lee or something or you know, like this, this thing is going to be big. The businessy types see it. The you know, radical open source devs see it and you know, we got to just sort of jump in and, and. There's been a lot of code since then.

**[06:13] SPEAKER_00:** So Jim, I was just saying at the start, 14th of September 2014 was the first commit there. So like what were you thinking when

**[06:28] SPEAKER_02:** you started

**[06:32] SPEAKER_00:** this was gonna go.

**[06:33] SPEAKER_01:** I mean like on day one, I just wanted to understand it. Like I kind of believe you can't understand something unless you are understanding it through the code. And you know, Ethereum's awesome. But I remember the first and I, I had a sense that there was

**[06:49] SPEAKER_03:** something awesome going on there.

**[06:50] SPEAKER_01:** But when I first started to like look into it to understand how it worked, a lot of the like videos that had been put out were sort of hyperbole and it didn't make sense to Me, like, I would go to these videos. Like, typical video would be like, ethereum is the fabric that, you know, underlies society. It is the future. You know, it is how we will build a new society. And I was like, okay, but what is. You know, and then I found the code base. So I was like, oh, okay, let me. Let me start playing with this. And, And. And also, like, just reading through a code base. It's not interactive. So I was like, let me. Let me see how this thing actually works. And I pulled up my favorite programming language. Haskell should be all of your favorite programming language, by the way. And I found a boot node and I connected to it, and I realized that commands were coming through to me. So I started adding code to talk back to these nodes and slowly picked up what it was and how it worked inside and what a blockchain is. And all of that was the beginning. But, you know, like, soon after that, realized that, you know, I'd put together enough lines of code that I had some, you know, I had built a tool that could be useful to. To the world. So.

**[08:12] SPEAKER_00:** What is a blockchain? What was your conclusion?

**[08:18] SPEAKER_01:** It's a long, technical. Okay, no, no, I'll give. I'll give you the more poetic answer. I think it is the fabric that under.

**[08:25] SPEAKER_02:** No, I mean,

**[08:29] SPEAKER_01:** it's. It's incentive. That's what it is. You know, like, you have a lot of people sitting around wanting to contribute to society, and yet, like, it's hard to coordinate everyone to, like, do things, like, in some aligned ways. And once you build some type of money, you can sort of align lots of groups of people to do something together. And so that's what it really put into the world. It's like incentives to get distributed characters from around the world to all be aligned in one direction. And you can sort of craft what that direction is,

**[09:14] SPEAKER_03:** by the way, Jim, in, like, to defend that. Like, you know, it's the underpinning of the new world. Vitalik's latest post, literally today, is about that. He's talking about sanctuary tech and how, you know, Ethereum has to move beyond finance. So, like, that thread has never left.

**[09:35] SPEAKER_01:** I mean, I did do the full circle. I was kind of like, laughing at, like, what is all this crazy hyperbole? And then I spent a lot of time understanding the technology, and then by the end, like, I, you know, something clicked in my mind and I was like, holy cow. This really is the, you know, like. Like the underpinning of the new world. And this is how. How we're going to build a new society and you need to have some way for, I mean, you, you can get a certain amount of free work in the world. I think Wikipedia shows that you just, if you just put up a tool and just, just lower the barrier of, of doing stuff, people will just come and do free work for you. But if you want to go a little bit beyond that, you have to start aligning people to some sort of common vision. And you need an incentive for that.

**[10:17] SPEAKER_03:** Not to call you out, Jim. But just a reminder, at that time, we were also thinking about doing a startup together. And the way you presented it to me was like, this might be amazing, or this might make absolutely no sense. I'm not exactly sure which.

**[10:32] SPEAKER_01:** Well, yeah, I mean, there are network effects and all this thing. I think I started, once I started understanding the technology, I said, okay, this is amazing. But it also might be that nobody will use it and it'll just like, be an amazing technology that just languishes. And it turns out that other people were interested. I remember like, you know, another, like, stepping stone is like, like, we started hanging out at Consensus more and more and I saw so many excited people there. I said, there's no way this is going to fail. There are just too many people who are really excited about this at this moment right now. People, like, willing to like, leave jobs, give up everything and come and just work on this stuff. So this is going to be something, you know, and it was, I mean,

**[11:23] SPEAKER_00:** and then how, how did things move from building a Haskell client into Strato being envisaged and what, what was the initial kind of vision?

**[11:37] SPEAKER_02:** So I guess we've always been like a certain kind of pragmatic people. And through building the client and then also trying to use like the early so like flavors of the RPC and all the tooling, we realized, you know, at day one, the devex was just not there. The today it's much better. The tools are, you know, reasonably mature. Although there's still things that, that bother me about, like the Ethereum devx that are just like choices that were made that made things unnecessarily difficult for, for no real reason. But, you know, you can also just like, AI around a lot of it now you got, but it was like, really difficult to get even, like a node up. And then once you've got the node up, you're like configuring connections to it. And they were initially like, so for some reason, and maybe a good reason, maybe not, the Ethereum people Felt like they had to write to a virtual machine, which we all know and love the evm. And they created maybe like four competing high level languages or three very early on there's lll, there was Serpent. Solidity was a little later. Right. There was the go flavored one

**[13:08] SPEAKER_00:** I found out recently that had got an earlier code name as well, which was H. Ll. So high level language was Mutown. But yeah, that was abandoned. That was done by Jeff Wilker, but

**[13:19] SPEAKER_01:** it was abandoned around. LL is like language, by the way.

**[13:23] SPEAKER_02:** Yeah, I'm sorry. LL was like language list.

**[13:28] SPEAKER_00:** Like language or low level language. I think it was.

**[13:31] SPEAKER_02:** I think that yes, this is the. There was a lot of like, you know, like nerd one upmanship in the earlier theorem. Maybe this is common in the open source space in general. Like there's kind of, you know, reminds me of like, like subtle swipes that academics put in their papers or something. You know, the naming of things and the. But you know, it kind of works. There was this like weird all against all but all for one competition in. In early Ethereum. And like guess we got stuck with Solidity, which you know is fine. Like it works, you know.

**[14:06] SPEAKER_01:** But yeah, well, go on, I got a point, but I'll let you to finish.

**[14:13] SPEAKER_02:** But yeah, so I guess we were like, okay, this tooling is no good. You can't get the node up. The APIs are weird. These languages are moving. So let's just solve that. At that O'Reilly conference I put on chain.com was there back when chain.com was like rest API infrastructure provider for Bitcoin, which was maybe for Bitcoin a model that was doomed. And Ethereum RPC providers that stuck came later than we did. That was the first thing we did. We're like, all right, let's get an API up. Let's make the routes sensible and let people get access to the live net. I guess that initially got called Strato, that bundle of things in doing so somehow we were enterprise or institutional coded and it was like not at all our intention. We thought it would be just an easier developer API and found the hardcore devs really liked the standard RPC interface and the enterprise devs were like, oh, I can put this in Postman. We got pulled in that direction and over the years going from POCs to pilots to powering consortia and all that sort of thing and I guess the, you know, the aggregated name for all of that was Strato. We sort of, we launched by, by Defcon1. So this is you know, on to end of 2015 we had, we're still working with. Within consensus at that time and I gotta be right back in a second. And had partnered with Microsoft to kind of create that category. I'll be two minutes. I have to check on something. Sorry guys.

**[16:14] SPEAKER_00:** Maybe Victor can continue here. So I mean from my memory it was DEVCON 1 where I first saw the block apps like name and branding. And I was aware of. Of Ethereum H existing.

**[16:34] SPEAKER_03:** Yeah.

**[16:35] SPEAKER_00:** But not really of what was. What was going on at that point.

**[16:40] SPEAKER_03:** So I think where the. So you know, we, we've always sort of followed this sort of like lean philosophy and I think our first test ground was, you know, the launch of Ethereum. We did the first hackathon at consensus. Right. So that was August, I think 2015. We when that happened and then. And it was interesting because people were building stuff really for the first time and the people who like people kind of built prototypes of a lot of the things we see now. You know, there was a gamefi app, there was like traceability apps, there was, you know, sort of defi ish apps. And but one of the interesting thing is like some of the judges were part of the more institutional traditional world. That's where they learned about what we were doing. And they were like, oh well, what you're doing. Yeah, we need a REST API to write against. We really want to use this. Microsoft came up and said, hey, if you guys want to do this with us, we want to promote Ethereum and you guys, but you have to offer a mode that allows you to run as a private blockchain. We don't want to have to make it a requirement that people have to go up and acquire some eth in order to do this. And that was really kind of like between August and I think devcon was November. Yeah, November. We were madly working to try to get this working on a way that we could deploy this on Azure and do that demo of write a DAP in 5 minutes for Devcon1. Interestingly, we were not their first choice. Another project which did Ethereum J, they were actually part of this. Microsoft wanted to work with them because they were a Java based client. We were this crazy Haskell thing. Jim.

**[18:51] SPEAKER_01:** Not there are.

**[18:53] SPEAKER_05:** Has.

**[18:53] SPEAKER_01:** Sorry, Microsoft Haskell.

**[18:56] SPEAKER_03:** Yeah, there are. And you know a bunch of the researchers are there. But you remember those conversations, they were like, hey, if this is going to be widely adopted, you know, that's like JAV is the most interesting thing. But you know, you guys are interesting too. And you Guys come along with it.

**[19:11] SPEAKER_00:** And you're telling me if. If Roman Mandalay had been a bit more business savvy and stable, that, you know, the whole path of the company may have been quite different?

**[19:21] SPEAKER_03:** Absolutely. Like, well, and I had some background with this because, you know, in my previous company, I had had. I worked with Microsoft before in their app. App world, but it took forever. Like, it took like eight months for me to get a meeting with Microsoft to start talking. So the fact that they came to us and, like, were like, hey, we want to do this thing with you, but we want to launch it in two months, you know, together, it was like, super. Like, I realized the opportunity and, yeah, I think Roman had other priorities at the time and kind of let the ball drop and, you know, that kind of kicked off everything. And then really, for that time, we were like, the only option if you wanted. Like, I. Azure was just launching, really, at that time, and so lots of people were getting free credits and a lot of people just want to like, hey, you know, I heard about this weird Ethereum blockchain thing. Can I just try it? Oh, they have a thing and they tried it and like, literally, like, hundreds of people used our solution very, very quickly. And from. Most of them were like, you know, complete nonsense. Like, they were just trying to, like, use it as a database and swap it out and do that kind of thing. But there were a few people who were, like, figured out what they could build with it enough that they wanted to build bigger projects, but they didn't know who to go to. And so that was really the next evolution of Strato. It was like, okay, now we have to support these, like, bigger projects where it's not just, you know, a dev node where someone is kind of connecting to it. It's like a real network or with multiple parties. And they have, like, you know, security ops requirements and like, DevOps teams and all of these things. We had to evolve the product in that way.

**[21:18] SPEAKER_00:** I seem to remember that Geth was on there as well at that start, that you could just launch a public get node to you.

**[21:25] SPEAKER_03:** It wasn't part of the original launch for Blockchain as a service. It did. It was added later, if I recall correctly. And, you know, like. And I think someone put it on AWS just as, like, an option. Like, it wasn't an official image or anything. They just put it on there. That might have been us for various reasons.

**[21:54] SPEAKER_00:** I mean, I. I remember there was a period shortly afterwards as well where people could, like, add their own as well.

**[22:02] SPEAKER_02:** Yeah.

**[22:02] SPEAKER_00:** Under this whole range of total scam projects, like slapping their shitty software up.

**[22:08] SPEAKER_03:** Yeah.

**[22:08] SPEAKER_00:** And saying, oh look, we're partnering with Microsoft. It's like, no, no, no.

**[22:15] SPEAKER_03:** Yeah. And it was very funny because like at the first consensus conference we kind of like were hosting a hackathon there and like there was a very early version of hyperledger there and like, you know, like I remember there was a room where like, you know, all the people were hacking it and like our room was full and like there was like one person in the hyper ledger room, which was very sad at the time.

**[22:46] SPEAKER_00:** So Jim, would you maybe like to say a little bit about like, you know, the architecture of the code base? Like what's, what is being open sourced here? What have we got?

**[23:00] SPEAKER_01:** Well, it's one of our nodes. You know what, let me sort of answer your question by going back to a point I was going to make before, but sort of turning the clock back to a topic that we had before and that is the various languages being used in the blockchain. And I guess I always considered it sort of a mistake that the EVM sort of resembled opcodes of a cpu. And my evidence in this favor is that I've lived through this before. Back in the 90s when the browser was kind of getting bigger and HTML had started to become a standard, people realized that they needed to have some way to program web pages too. And the first real attempt at doing this was actually a sort of large opcode CPU like plugin, which was the Java applet back in the day. It was bulky, ugly. You'd sort of like go to a webpage and it was almost like booting up your computer. You'd watch like the web page struggle a little bit and then kind of come up. And then eventually you might get something that looked a little bit like a computer screen sitting in the middle of your web page there. And that failed pretty miserably and it was replaced by a, you know, by JavaScript, as we all know and love now, which was sort of like it's a higher level scripting language that just sort of runs in various threads in the background in your browser. One of the biggest changes that we made is that although in the early days we certainly had the EVM in there and the code is actually still in there, but mostly commented out. Right now we have something called Solid vm which is a kind of like, well, it's solidity based, sort of like a JavaScript style language that runs as your contracts. One of the big differences is that since everything is opcode based in the Ethereum network itself, you have to compile everything down and you can't really see what your contracts are doing unless you try to decompile it or something. With us we just keep the solidity or the solid VM source code right there. So you can visit any contract and just look at what's running at any given time. Or if you know, if you send a command in, you just like send the solidity command right in the transaction. So that's one of the big things, is that we're not based on opcodes, we're based on this sort of slick scripting language running in the background. Solid vm, that's. I don't know, questions or comments?

**[26:09] SPEAKER_00:** Maybe if I reach out to Dustin. I was just looking. So you. I. As far as I can see, your first commit was the 9th of August 2017. So you joined in this journey not terribly long after all of this. And I mean, one of the key things I remember from my time at the ea, which is really where I met Victor and Kieran first, was that the differentiation that there was versus all of the other clients at the time is they were all monolithic single executables. But Strato is very much not that way. So how is it?

**[26:55] SPEAKER_05:** Yeah, so Strato instead runs as a set of microservices that for the most part are connected using Kafka as sort of an inter process communication bus. So whereas with Geth and maybe other clients, it all runs as a monolith, as one program. Each component of the node is its own process. So like the VM that, that runs solid VM, as Jim just mentioned, it's its own process. The P2Pmodule runs as its own process Ethereum discovery sequencer that sort of orders all the transactions and blocks before handing it off to the VM that's its own process, the API, et cetera. And this makes it a lot more robust because like if one thing goes down, it can be restarted without having to take the entire node down. But also it gives some nice replay properties where since we use Kafka, we can rerun like a second version of the second instance of each executable and it will rerun through the logs from Kafka and you can rederive the same state. It really helps with debugging. And yeah, of course there are some things that might be a little trickier, such as tracing a certain message through the entire platform, but I think overall it gives a lot of benefits versus the monolith architecture.

**[28:33] SPEAKER_01:** Yeah, it's a full separation of concerns. It's like the VM is just a monster that just sits there and gobbles up all the transactions coming at it through Kafka and then outputs all the data changes on the other end. And we have various other things in there. We have indexers. One of the things that we added also is at the end of all of the processing, just built into the system, there are these postgres indexers. Everything that output from the VM is goes to another Kafka stream and the indexers just gobble up all that stuff as it comes in and sit there and fill in tables all over the place. So we have all of the state and history just there for a quick SQL query. So you can see the whole history of the blockchain in the SQL query.

**[29:33] SPEAKER_00:** Yeah, I guess that that is really very different to lots of other clients. Right. Because it's sort of, I guess a bit more like some of the characteristics that you get off archival notes in that monolith.

**[29:49] SPEAKER_01:** Like, I don't want to beat on some of the architectural decisions in the first Ethereum too much because those guys did an amazing thing in many ways. But there are. I have my nitpicks and I think JSON RPC is sort of like a strange interface to the world. You know, we have a converter from JSON RPC that like really, it's just querying our stuff in the back end. But. But it's like what effectively has to happen in there is like to get any data, you have to sort. If you think of the blockchain as like, like a series of get like commits, like, you know, the version control git, every time a block goes through, that's like a commit and git. And if you want to get any data, you have to literally connect with JSON RPC and send something through to the VM that goes and does a checkout at that place in time and pulls that piece of information out. So a lot of overhead. Very difficult compared to just having a postgres database with everything and you just do your query and you get whatever you want. Wow.

**[30:56] SPEAKER_00:** I mean, I think a lot of those decisions basically just were straight copied from what Bitcoin was doing, plus, you know, are randomly pulled out of the air delta. You know, I've heard a lot of people say Ethereum is a science project gone live. Charles's favorite garbage, built by amateurs in a rush.

**[31:24] SPEAKER_02:** It's like Curtis Yarvin said something like Ethereum is good at nothing but succeeding.

**[31:32] SPEAKER_01:** There's definitely like a cultural difference between like sort of hardcore devs and, and maybe more front end or business business users. And I, I found over time that hardcore devs are very suspicious of SQL, whereas sort of like front end and business people love SQL. And I think, you know, like often I've had, we've had people at the company over the years who kind of looked at stuff and said like, I really like all this stuff, but you know, all that postgres stuff there, I'm suspicious of it. We should rewrite it to like just store the data in memory using like arrays and you know, and maps. But of course that's a world that the business people and the front end people would hate. So I think that was one of our big additions is sort of realizing that we wanted this data to not just be sitting there for the geek steams. We wanted to have an interface where it was easy to get to everything in all of history right away.

**[32:43] SPEAKER_00:** So I mean, in this agentic world. Kieran, how, how do you feel our code base is kind of aligned for agentic usage versus more monolithic clients?

**[32:58] SPEAKER_01:** Yeah.

**[32:59] SPEAKER_02:** Let me apologize to everyone dealing with the burning smell in the house. Initial triage seems to indicate no obvious danger.

**[33:10] SPEAKER_03:** You're not on fire. Right.

**[33:12] SPEAKER_02:** I checked fairly thoroughly.

**[33:14] SPEAKER_03:** Okay. Just to make sure.

**[33:17] SPEAKER_02:** Just, just making sure. So the. Yeah, it's a brave new world. The AI is remarkable. Like, just as a aside, we're wiring up some privacy features right now that Jim is developing. And I was testing them last night and there was sort of an edge case that Jim hadn't tested yet that I discovered. And like Opus 4.6 was just like, yeah, let me just fill that in for you. This is like hard zk, you know, flavored stuff where you're making, you know, exciting merkle trees and UTXO notes and all that sort of thing. And it seemed to just work. And he was like in the middle

**[34:05] SPEAKER_01:** of explaining the bug to me and before he finished explaining to me, he was like, oh wait, wait, robots got it.

**[34:12] SPEAKER_02:** It's so, you know, it has in a sense reduced the need to have like beautiful interfaces to everything because like, the AI is more patient and can read faster than a human. Like there was a strange moment, I would say, I don't know, summer 2025. We found at first that the AI could make new things, kind of get a POC done pretty fast, but sort of brittle, but couldn't handle this relatively huge code base that we have. And Then one day it was like, oh, not only can it handle it, it can read it way, way faster than I can. To the point where, know the early days I worked on the code base a bunch, but then you end up on the business side as a CEO and then once you have like you know, a BD meeting or two or an investor meeting or something like you can't code that day, your brain is shot from. But with the AI, I could just kind of like ease back into it, get it doing stuff and then start giving instructions. I could code again, you know, not like all the time, not doing, you know, big features usually or you know, maybe if it is, it tends to be peripheral, not like mainline core stuff that needs to be maintained. But getting the first version of a thing out, a UI refactor, fix a bug, et cetera, et cetera. In some ways we have to do nothing. But also the AI does like our API architecture. It just digs through it and finds the thing it needs. And I don't know if you meant the modular components of Strato or

**[35:57] SPEAKER_05:** what

**[35:57] SPEAKER_02:** you meant specifically, but we've got a bunch of processes that runs. It seems to. Sometimes it stops and starts them individually. It's like digging through and looking at the sequencer. I was syncing the testnet and I think it was a little bit stalled and then it finished. When I was doing this privacy testing last night and then I said, hey, just look again. It's like, oh yeah, you're right. The blocks got all the way through the pipeline. So it's so good. I don't know that we need to do anything all that specific, but certainly it likes how it's architected. Maybe sometimes it has trouble with the authentication in particular on the app site we have like a captcha and stuff. It can't get through the captcha but if you give it credentials.

**[36:51] SPEAKER_01:** The purpose of the captcha.

**[36:53] SPEAKER_02:** Yes, give it credentials locally, it can kind of do everything. Obviously Bob, you developed an MCP which works well. It doesn't even really need the mcp but it's good to just have it out there and we have plans to make human and agent friendly cli that and probably maybe we'll wrap it in skills. I'm not quite sure. Like MCPS might be the eight track of, you know, of AI enablement technologies.

**[37:28] SPEAKER_00:** Yeah, I mean they seem to have been a bit of a crutch. That's probably already like done.

**[37:33] SPEAKER_03:** Yeah.

**[37:37] SPEAKER_02:** Another thing, maybe more forward looking. I think everyone in crypto feels like agents are going to Be first class citizens. And honestly even before agents, so much of on chain commerce is automated anyway by volume. It's probably all bots run by sophisticated market makers who have trading backgrounds and so on. And then, and those bots make it possible by the way. Tradfi is like that too increasingly, maybe kind of completely now. Those bots make it, you know, reasonably easy for retail to get a good quote. They also, you know, liquidate people and, and this and that. But you need kind of profits for the institutions to come in and then the competition eventually competes those profits to moderate and retail gets a good quote. When you want to do a swap, right? So it's gonna like, it might get like more like that. You know, we've like one good thing is a pretty granular control of the fees. Like I think the agents can pick whatever chain they want because they're really smart and if you have high and indeterminate gas they might just like route around you, you know. And so the way we've set things up, we've got fees in our native stable and we'll probably have all of the native coins, coins swappable for fees soon enough. We haven't done that yet. I'm considering, you know, there's some of these more like agent native launchpads out there and I think we are thinking about having kind of like a restrained launch pad sort of feature that could help in certain scenarios like under collateralized lending. And I think the agents will be good at that. If you're going to have most of DeFi has a pool concept like AAVE being the biggest, right. Like if you want to borrow, put a whole bunch of money in the pool. It's over collateralized and there's not really any discretion for good reason. It's hard to scale discretion on the Internet especially most unsecured lending that happens has a different sort of some sort of enforcement threat. So when it's over collateralized you just take the collateral. It's kind of always collateralized in some way. It's like you know, you know, the guy, you know, where he lives, you know, all that sort of this social shaming or, or worse if someone doesn't and but I think the agents will be pretty good at that. Like in time they'll be less emotional than humans. You know, if they have enough context they don't really get tired. It's funny that they do get tired, right? Like in the same session. So yeah, I think it's going to be great. I don't know, like I haven't yet, sorry. Good.

**[40:31] SPEAKER_01:** I was going to say, I'm guessing most of our audience is familiar with AI at the moment, but if you're not using it day to day, I just want to be clear, clear that we're living through, like, in this couple of months, a huge revolution. There was like, up until just a couple months ago, I would have said, like, AI coding was more of a novelty, something to like, maybe do a quick prototype, but it was sort of worthless in dealing with the large code base. And that changed really fast. And that was about two months ago, maybe. And I've seen all over, all over Twitter, developers saying the same thing. I was shocked. A couple months ago I went in there and it popped in and just started debugging very complicated bugs in the system in front of my eyes. The screen was scrolling by quickly. It was coming back at the end with amazing solutions to things that would have taken me hours to do. This is changing fast and anybody who says they know how it's going to look in a year or two is lying to you right now. At the very least, what's changed in the last couple of months is going to be a big deal, but it could grow way beyond that, too. We don't quite know yet where this is going, but it's a very useful tool.

**[41:59] SPEAKER_00:** Yeah, I mean, it was really with those with the GPT 5.2 release and Opus 4.5 that were late November, early December, like, yeah, a massive phase switch and Claude Coates. It's not even been around long after that either.

**[42:17] SPEAKER_01:** I, I was using it for research. I was using the AI for research all the time before that. But now, like, huge areas, like, I, I just hand it over, but we're learning like, okay, so like, the story I sort of keep saying is, like, in the. If you go back and look at like in the 60s, there was like this belief that computers were just a new thing at that time. And they thought that you would be able to soon, like, pop a weather simulation on a computer and be able to forecast the weather a year in advance. Hey, there's going to be like a thunderstorm on, you know, May 4, one year from now at 4:15pm and of course you can't do that. And we didn't know it yet. And I think something similar is going. There's just like a similar learning for AI right now. We have, like, lots of guesses about how amazing this stuff's going to be, but we're sort of slowly going through and figuring out what's actually Possible and what's not possible and it's amazing what it's doing already, but we're not sure where it's going to end right now.

**[43:21] SPEAKER_00:** All right, well, I'm looking at the time, so maybe just let's close out Victor with, you know what, why are we open sourcing and what, you know, what kind of expectations or hopes do you have because of that?

**[43:38] SPEAKER_03:** Sorry, you're asking me? Well, maybe we can start with Dustin, I think.

**[43:46] SPEAKER_00:** Okay.

**[43:49] SPEAKER_05:** I mean, well, I see open sourcing as both sort of like step towards transparency, auditability and collaboration. So I mean one thing I love about the Haskell community is that like almost the entire set of libraries and everything is Open source on GitHub, on Hackage, et cetera. And I've really learned a lot just by going through different people's libraries and reading the code, understanding what it does, and I think by us sort of contributing to that open source ecosystem, people can learn what we've been doing and see the innovations that we've brought to the blockchain space and sort of how Strato differentiates itself from other blockchains and kind of like what we bring to the table.

**[44:45] SPEAKER_02:** Maybe I'll add, and probably you mentioned, you know, we've had, we had like an initial open sourcing effort kind of to show our commitment to it, but there was some effort to do to basically there were a couple things we had to clean up on a one off basis that we ended up kind of cleaning off kind of permanently. Also we were still in quite heavy development for version two of our application and so kind of continued in a closed source format for a while. But. You need to decentralize. We're doing it progressively. I think there is a right level

**[45:28] SPEAKER_04:** of,

**[45:31] SPEAKER_02:** especially with like new chains, new apps, you do want a little bit of the quality control training wheels in place before you just let the dove, you know, free and we've been vibe coded.

**[45:52] SPEAKER_00:** L1's not a good idea.

**[45:54] SPEAKER_02:** I mean they're making it, you know, I bet like compared to the average human, like AI code quality is, it's different but it's probably higher. I don't know. They do make, they do introduce bugs and they make, they lie to you, they make subtle mistakes, they, you know, but it's so fast that like the whoever is going to try to bring your thing down is using the AI now and you better just kind of try to stay ahead of it. Like it's a strange time. Develop pretty AI native means of working so that you just can't do stuff slowly anymore because the AI is so fast. You better be kind of like faster than the adversary, which is difficult to impossible. But I actually think Vive coded L1s are probably fine. Eventually you just, you need like really good test harnesses and security procedures to catch all of it. I guess it is a little hard to audit pure AI code. It's getting better though. Like, sometimes it just makes too much code, but I don't. They're going to do it themselves anyway, right? Like, I don't think. See, we had a ethereum vibe coded L1, right? Like already in like a couple. I, I saw this on X. So, you know, again, you gotta watch it for, you know, it's hard to just like say like, do it, but it's getting closer to that and I think a year or two, it'll just be better in all ways than humans. Like, we had Donald Knuth, you know, mentioning some problem he was working on that opus 4.6 solved. He's like 88 now. And I think he helped it. He did a lot of. I think it produced 31 proofs. I don't know, maybe one or two of them good, maybe more than that, but it's. We should admit that it's better at coding than we are and then guide it from more abstracted level. Go ahead, Jim.

**[48:04] SPEAKER_01:** I'll tell you why we're open sourcing. If we were just trying to sell a product, I wouldn't open. We're trying to build a network right now and nobody wants to use like proprietary tcp, IP or something you need for a network, you need some type of open standards. And this is the reference implementation. We want people to come in here, build other tools that sort of talk in the same language that we do, and we want to make that as easy as possible. And what I'm really imagining right now is like, we're about to go into a world where AI is going to need money and nobody's going to give a computer a bank account. So I think blockchain is the way that AI is going to sort of haggle and purchase stuff from each other. And I want this system to be as simple to use as possible, as open as possible. And so that's the real reason I think, think that, that open sourcing is important.

**[49:05] SPEAKER_00:** Yeah, I mean, I think the, you know, many, many SaaS platforms are just like absolutely screwed. Like, because, you know, they're built for humans, but they're just terrible for, for agentic stuff, you know, whatever, like having to log in and then you've got your crappy website and just really very manually kind of like, I mean computers as a whole, like a lot of it has ended up kind of like paper form stuff got digitized and you haven't really got like a lot beyond that. It's just your websites, what used to be a form and you've got your humans logging into a thing, doing a thing, exporting some stuff, copying files and all of that, like human shuffling I think is, is dropping away. So then anything like SASE or anything like without like a CLI or an API or some easy automation just is like to be rooted around.

**[50:11] SPEAKER_02:** Yeah, I've been saying, you know, AIs have brought UNIX back, text in, text out, but for the, for the mass market somehow. And it's a good thing it gets out of the proprietary data capture to some extent that a lot of platforms depend on. If you get your stuff out, you can take it with you.

**[50:30] SPEAKER_03:** Well, before we wrap up though, Bob, I just want to give you kudos because you've been driving this open source effort and it is no easy thing to push a 10 year old code base with all the issues and commits that have happened over those years into the wild. So thanks a lot for keeping us honest with this. We've wanted this to happen for much, much longer, but just getting it to happen has always been a big challenge.

**[50:57] SPEAKER_00:** Well, I mean back 2016 for real, not 2026 saying the wrong date. You know, when I was doing C relicensing, you know that Strato was another sort of considered possible option at that

**[51:12] SPEAKER_03:** point,

**[51:16] SPEAKER_00:** but you know, the timing didn't work and what have you. But there we are ten years later. Tada.

**[51:23] SPEAKER_03:** Nothing goes as fast as we think it will, but I'm glad we're here today, so. Yes, exactly.

**[51:28] SPEAKER_01:** By the way, I just want to say a little AI story to tell you where we're at in the world with AI. In the past when I've done this type of like we had to deal with licensing and the product, you always like kind of go through the like, like package by package, library by library and you always find something in there that you're like, oh, so I kind of messed up there, that one shouldn't be in or whatever. And then you have to run out and try to find new versions that were actually better license for that particular package. This time it was very different. There were a number of times where we found stuff that was like, oops, accidentally put this thing in and I literally just went to the AI and said write me a new version of this library. But, but we're just going to open it in a license we like. And it sat there from scratch and wrote a copy of that library in front of me. And it worked. Just like a one shot and it worked.

**[52:19] SPEAKER_00:** Let's not say copy because that's a bit in breach of license. Let's say White Room Reverse Engineer.

**[52:28] SPEAKER_01:** It wasn't doing a line by line copy, it was writing in front of my eyes.

**[52:34] SPEAKER_00:** But yeah, I mean I think, I think that will happen like with lot, you know the kind of the, the MPN micro package horror era I think is over because lots of these little things they can just get like bespoke written. I think you're only going to end up with very large, you know, very useful components that it makes no sense to rewrite. But lots of a little plumbing, you

**[53:01] SPEAKER_02:** know, you don't need to compare the end of the gpl.

**[53:04] SPEAKER_03:** Yeah, well, I think we're going to have to rethink security in general. We do have an exciting announcement about that, but we'll leave that to a future one. So.

**[53:17] SPEAKER_00:** All right, so yeah, I mean blog post to come out a little later but the repo, the mono repo is live on GitHub now. So that is strata net is the organization and the package there is Strato platform together with various other already open sourced pieces. So dive on in.

**[53:45] SPEAKER_01:** I'm Bob, our Twitter handles.

**[53:48] SPEAKER_00:** That's right. So I'm on Twitter. I am BobSamoil, same as my name. Michael is Mike B. Tan. Victor is Vic for Wong, Kieran is K. James Lubin. Jim is Jam Jamshid Jam Shade Hummus I believe.

**[54:08] SPEAKER_05:** Yes,

**[54:12] SPEAKER_00:** there you go. And Dustin, I'm afraid you'll have to say your own.

**[54:19] SPEAKER_03:** Are you muted?

**[54:22] SPEAKER_05:** My. My cloudbot is currently running my Twitter under a pseudonym. But the handle is semi groupioid.

**[54:32] SPEAKER_02:** Semi groupioid?

**[54:34] SPEAKER_05:** Yeah, I don't

**[54:38] SPEAKER_02:** have to.

**[54:38] SPEAKER_00:** All right, so yeah, open Claude it up. Get, get Claude code hacking on. On the platform. All the best everyone.

**[54:48] SPEAKER_03:** Take care everyone.

**[54:49] SPEAKER_00:** Bye bye bye everybody. All right. Okay, so hopefully that's a 1080p this time. We'll find out. Catch you later.

