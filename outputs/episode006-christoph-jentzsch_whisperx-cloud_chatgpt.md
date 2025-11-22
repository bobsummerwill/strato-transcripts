**SPEAKER_08:**
[00:01] Okay, recording is in progress, it says. So, hello everybody. Today, I'm delighted to have Christoph Jentz with us. We did attempt to record this, Christoph and I, two weeks ago, but I forgot to press the record button, so we spoke for an hour or so and then it was not recorded. So this is round two. So, hello Christoph, how are you?

**SPEAKER_01:**
[00:24] Hi, Rob. Nice to meet you again. I'm doing good. I hope you too. Thanks for the invitation.

**SPEAKER_08:**
[00:28] Fantastic, yeah. So Christoph and I, our paths crossed for the first time way back.
[00:33] Back in 2015, when I was trying to do C++ Ethereum on my smartwatch. And this was around the time that Christoph was still at the Ethereum Foundation. And then I think I crossed paths a number of times since, and Kieran's too.
[00:44] Indeed. So, Christoph, what were you doing with your life before you found Ethereum and joined this crazy journey?

**SPEAKER_01:**
[00:52] So the journey started in 2013. I was doing my PhD in theoretical physics, actually about self-organizing systems. So, like biology—six months in mathematical biology and other things. So I was studying systems which have local rules and global behavior. And I came across Bitcoin, which is just a small set of local rules and a global behavior as a currency.
[01:13] But the reason I came was I was looking for cheap GPUs, like graphic cards. And the Bitcoin miners were selling their GPU mining rigs to get some FPGAs and later ASICs. And so that's how I got into Bitcoin mining. So I bought my first Bitcoin, got into this bubble, read everything I could about it.
[01:34] And then I came across the white paper from Vitalik early 2014, something like January, February, in some Bitcoin forum somewhere. And I was already totally in love with the idea of Bitcoin being a decentralized currency and all the characteristics and features of it. And this white paper by Vitalik—if you read it again, it's almost a prophecy. Except for NFTs, everything's in there: DAOs, ENS (domain names), all the terms and all of that.
[02:05] So for me, it opened up this option of building applications with the same characteristics as Bitcoin, but just not a currency—everything else. And so then I started reading everything about it. In 2014, in summer, I read that the crowdsale was in 2014, right? Yeah. So around the time the crowdsale happened, I watched a video from Gavin Wood. He was somewhere in the Nordics, some conference there.
[02:33] He talked about Ethereum. I loved it, and he said he wanted to open up an office in Berlin and was looking for C++ developers. I was a C++ developer—so in theoretical physics, it's 90% software development—so I thought, well, I want to do this. So I took my parental leave time plus some vacation time and paused my PhD for like three or six months,
[02:55] and said, I will return after I'm done. I thought this was just a short project because they raised money, maybe six, maybe twelve or eighteen months or so, then it's over. When I started, I thought maybe three to six months, and then I go back to my PhD. So I worked there with Ethereum, Gavin Wood. It was a great time, and then I just decided to stay. It was so exciting.
[03:16] So you never got to be a doctor? No, I'm not a doctor. I did not finish my PhD, although I only had six months left, which was kind of a pity. I worked for three years on that. But I also had at the time, I think, four or five kids. I needed some money. I didn't get much money as a PhD student. So I did software development as a side hustle, basically.
[03:39] And so when I got this project, I said, well, let's do this for two or three months as parental leave time. Then I can return. And then I decided to really interrupt my PhD. I said I will maybe return one year later because I thought the foundation would eventually run out of money because they're not making any profits. They just raised donations, then they will spend them, and then it's over. Then I can continue my PhD. That was originally the plan. It just came different. I mean, I guess it’s never too late, right?
[04:09] I actually sometimes think about if I should return. It's just so much to learn again. I'm right now doing Tokenize It. I'm basically working on tokenizing German companies. It works very well. So currently I'm not planning on getting back anytime soon. No, because I mean, famously you had, you know, Dr. Gavin Wood and Dr. Christian Reitwiessner as well. And I think there were a couple of other PhDs as well. There was definitely...

**SPEAKER_04:**
[04:30] I also dropped out of mine. I was actually in mathematical physics too. Interesting. Similar background. It's actually the same. Like theoretical physics, it's the mathematical part of physics. I enjoyed it very much. I did thermodynamics and statistics, mostly software development. It was really fun. Well, by the way, Jim is trying to join. I don't know if there's anything that needs happening. He gets some browser issues.

**SPEAKER_08:**
[04:51] Yeah, yeah, well he'll pop up and we can add him, or if he's—I'll see, and then never mind. So Christoph, in terms of getting hired into EthDev—and I'm sorry if I just missed it—so

**SPEAKER_01:**
[05:01] How did that happen? Did you meet Gav at a meetup, did you say? Yes. Actually, I listened only to his talk—it was an online thing. I actually just wrote him an email, said, look, I would love to join Ethereum, love what you're doing. And he invited me to meet in Kreuzberg, Berlin.
[05:16] So, which again is about two hours' drive from here. So I went up there, met him. I remember the first conversation—he was talking about all the stuff they were going to build, and said, well, what can you do? And I just asked him, what's the most complicated stuff you have right now? Like, give me a complicated task. I can somehow figure it out. So he talked about the Ethereum Virtual Machine, which did some testing.
[05:40] I'm Jim. So I just picked working on testing the Ethereum Virtual Machine, or like writing tests for it. Back at the time, I actually had no real idea what he was talking about. Meaning, of course, I did understand on the white paper level, I did understand what Ethereum was about.
[05:55] But Gavin had this skill of writing the yellow paper, which is still incredible work—it's such a great specification, different from Bitcoin, really having a specification so multiple clients could be built. And in there he defined the Ethereum Virtual Machine.
[06:14] And I think I read the paper six or seven times. I felt like I was one out of, I don't know, 10 or 20 people in the world at the time who really understood the yellow paper. I did corrections to it. I have some pull requests actually in the yellow paper GitHub repo, added missing definitions and stuff like that.
[06:33] And then what I mostly did was writing tests according to the specification, which then were—with the help of the C++ client, because this was his team. So I was working also on the C++ codebase. And so Geth, PyEthereum, also the JavaScript version. And what else did we have? Like Haskell client and others. They're basically using my tests to see if they implemented the Ethereum machine, also the state transitions and block creation, correctly.

**SPEAKER_08:**
[06:58] Yeah, yeah, so I mean, just—just to have some timeline for the viewers:
[07:02] So, Vitalik wrote the white paper in November 2013. Various other people sort of joined in on the efforts in December, including Gav and Jeff, who started the C++ and Go clients respectively at the very end—
[07:13] oh my goodness—at the very end of December, kind of Christmas projects for them both. January 2014, you had the public announcement of Ethereum at the Bitcoin Miami conference. It was as early as April 2014 that Gav wrote the yellow paper, which is, you know, as you were saying, the sort of formal specification.
[07:32] You had the crowdsale between July and September 2014. So then, yeah, you were coming in right after that, you know. So you had a wave of arrivals in September and October of that year, essentially because the crowdsale had happened; there was some money to actually hire people.
[07:49] And then, talking about where you met there, initially that group—so EthDev were and is a company coordinating the development of Ethereum stuff. So it's a subsidiary of the Ethereum Foundation.
[08:02] They were working initially in a co-working space but then got off it, and it was between August and November of that year that the office was getting done up and tidied. Then in November you had DevCon Zero, the first conference, you know, an internal one.

**SPEAKER_01:**
[08:20] Where a lot of the people, that was their first sort of face-to-face meetings. How was DevCon Zero? How was that? What was that like?
[08:27] It was like a company retreat. So it was not a public conference. Even though there were some outsiders who felt like part of the community, maybe also pushed some code. I remember—I was in—what was his name again? Wrote the book also about Ethereum, did lectures.
[08:46] From IBM. Oh, Henning. I think Henning. Yeah, I think he was also there, just as an example of some people who were reading about Ethereum, interested in joining. Of course, Joseph Lubin. Roman as well, right? Roman. Roman was there—Roman Mandeleil with the Java client. But it was mostly developers. But also, I think Stefan Tual was already there. So, he had already the London team. So, it was like an internal Ethereum meeting—kind of a meetup almost. I think three days or so—I don't know exactly—five days even.
[09:18] So it was a full week. I was there for the full week, as far as I can remember. I did a presentation about testing, how the test suite is very important. Yes, we had Remix projects, Solidity project I think, mostly started at the time. Gavin used this for explaining his vision of Ethereum as a platform for decentralized applications, so building Swarm. I don't know if Swarm and RISCOS was already launched there, but at least the generic idea, the Mist browser,
[09:48] So all those ideas are really sketched out there, like the technical roadmap, what we are going to build. Because we started just, of course, with the basic clients, like implementing the protocol. But he took it—what are we going to do in the next 12 months, building the Mist browser,
[10:03] like Remix, all of those tools, to have a platform for these and those applications. I remember one slide, which I think I posted on Twitter a while ago, where you have those three circles: one circle is one node, and you would see they're connecting on the blockchain, using Swarm for the data, Whisper for the messages. This whole picture was painted there.
[10:23] And there are people attending, I think around 50 people, plus or minus 10—I don't know the exact number—where most of the developers are talking about code, coding there. Joseph, I remember him being there saying, "Well, all of you, you will create your own companies, becoming millionaires." I remember Joseph talking about that. And I think mostly he was right. So most of those people in the room...

**SPEAKER_08:**
[10:45] In one way or another co-founded, founded, or were early part of companies building on top of Ethereum in the years to come. Yeah, yeah.
[10:53] Let me see if I can do a little screen share... No, no, I can't work at home. Not to worry. But yeah, there's this present button...

**SPEAKER_04:**
[10:59] Is that not working?
[11:01] Yeah, I don't see that. Is that on the right-hand side somewhere or at the bottom? Maybe you have a different... For me, I appear on the top right and below. And to the right of me below, there's a present button with like a plus sign.

**SPEAKER_08:**
[11:16] But you're the host, maybe. Never mind, never mind. I was just going to show the iconic photo of people at DevCon Zero, right? You know, that's this big group shot with nearly everyone who was out there—so that's a classic Ethereum photo.
[11:29] So I was looking—sorry, there's, like, 11 of the videos are still around from DevCon Zero. I think there were about 20 sessions. I'm still trying to dig out the others. Some of them, including yours, I have not managed to find yet.

**SPEAKER_01:**
[11:41] Yeah, it was only about the test suite—how I built it, how people would use it. It was rather technical. There was not much of a vision in there. Well, Lefteris presented on Emacs, so you're not the most boring talk.
[11:56] Again, it was just some nerds starting. Also, for most of them, it was the first time we actually met. And of course, the C++ team, they didn't know each other because they were working in the co-working space. Lefteris and others were there. But then, let's say, I think it was the first time I actually met Vitalik,
[12:12] because he came there. Then, of course, Jeffrey and his team, Stefan Tual and his team, Joseph Lubin. So for me, it was the first time to meet all of them and having talks. And since we really had time—five days, a small group of people—we actually had time to eat together, to talk. So it was not so crowded maybe as DevCon is today. Very intimate. It was good. Yeah, I mean, far from it.

**SPEAKER_04:**
[12:35] One thing I can't quite remember. So there was a time—there was an Ethereum Slack that was kind of open to the public. You know, there were a lot of people. The sort of Ethereum affiliation status was fairly vague at that point.
[12:47] And I remember we were using Skype a lot in those days, just the team. And Vitalik liked to Skype. And then at some point, I sort of lost the thread of like, where the core—I can't remember where the core development discussions were happening. And maybe I'll ask Jim to comment. Also, just like, those tests, we kept like, getting them. And I think I'm thinking of some a little bit earlier on and we'd build them. And Jim was mostly working on them and one update on the like, passing percentage, which would always be between like 93 and 98%. And then something would change, you know.

**SPEAKER_01:**
[13:18] But, yeah, like, where did the discussion—because, yeah, between, like, sale and DevCon Zero, I think it kind of got a little bit moved around where the dev discussion was. Yeah. It was mostly Skype. We also had Skype channels for almost everything, like the C++ team and so on. Then in a short time they used the—it was a note taker, which had a name also with E something. Etherpad?
[13:44] Yeah, something like this, right? There were some notes being written there, but the communication was really, I would say, 99% Skype for me. Later on, we used a tool based on GitHub—what was the name of it? Gitter. It was called Gitter. Gitter came later. This was like the replacement for Skype, but I didn't use it too much. This was actually during the time when I was actually leaving. But it was done, used also by C++ team. There you had a channel per GitHub repo. This was during the time that GitHub was completely reorganized because at the beginning it was like one big repo with everything. Then we had the submodules—it was so messy. And then during this process, we got Gitter.
[14:24] But yeah, for me, it was mostly Skype.

**SPEAKER_08:**
[14:26] Yeah, and then annoyingly, that kind of means a lot of these early discussions are kind of like a bit lost because nobody is using Skype. And Skype is getting deleted. This is happening in February of next year.
[14:39] Oh, I thought it happened already. So you can still request a download, and I did, and then I haven't heard anything back and want to do that to see if I can get some of those. So everybody apply to download your Skype data.
[14:50] I remember with Gitter, there was a discussion about this that I was involved with at the EF later, which was saying the problem with Skype is it wasn't discoverable. You had to request to be added, but you had to know what was there to be able to do that request. So it was a bit of a chicken and egg situation.
[15:09] Whereas Gitter, it was like a one-to-one with the repositories. So if you're using a repo, there you go. There's a one-to-one channel with that. And it was discoverable and archived. But then Slack, I think, was even earlier. Oh, and there was the forum as well, right? There was an Ethereum forum too.

**SPEAKER_01:**
[15:28] Yeah, it was important. And then Slack, I think I got introduced to Slack by Stéphane Tual when he created a community for the DAO. When he looked for a new communication tool, he went with Slack. And at that time, it was not like today, like a business tool for the company. It was really communities. Like we had 5,000 people in our Slack, which is not how it's used today.
[15:51] Yeah, yeah. So welcome, Jim. Your technical problem.

**SPEAKER_04:**
[15:56] Hi, sorry. I had some technical problems for a while there.

**SPEAKER_01:**
[15:59] But I don't know. I'm just listening to you guys.

**SPEAKER_04:**
[16:01] What happened that brought the whole world to Zoom suddenly? It was in waves. On my side. I don't know. I just woke up one day and everything was Zoomed from then on. Species, like a statistical phase transition. I think it was two phases.
[16:16] I would always get invited to corporate—let's say 2017 to 2019, when I was doing primarily BD, I found that I would get invited to any of 10 video conferencing tools.
[16:27] And, like, you know, what was the Cisco one? WebEx. That was horrible. I would get that a lot. Google meetings didn't feel sufficiently corporate or something, even though it was okay. And Zoom had the best quality for a while. And I found that everyone picked Zoom at the same time, like mid-2018, let's say. I think it was just quality to me. Yes.

**SPEAKER_08:**
[16:47] I mean, Microsoft really fumbled, right? Skype had got such a lead for so long, but Zoom just seemed more reliable—whatever weird little proprietary magic they had going on.
[16:56] Yeah, and then I guess I was under the impression that, like, Zoom was for businesses.

**SPEAKER_04:**
[17:00] I think that's—well, that is true. But it was just that—still, I mean, this has gotten way better in the last 10 years, but still nothing really works for reliable video over the internet. It's just much better than what existed.
[17:13] But there was a free version always and it would just time you out—so they had a fairly viral acquisition loop where—I was just going to say, in the pandemic, once when people were locked down, it became a consumer tool where people would have, like, large yoga classes or, you know, sermons or whatever with, like, 500 people on a Zoom, and then everyone got it.

**SPEAKER_02:**
[17:37] I remember it well. All of a sudden, my parents were calling me up and they were like, "We found this awesome new tool. You probably never heard of it. It's called Zoom."

**SPEAKER_08:**
[17:45] Well, yeah, there were like ten. Let's move on from sharing about video platforms.
[17:50] So, I look back—so Jim’s first commits on the Haskell client were mid-September 2014. So, you know, a couple of months ahead of DevCon Zero, you'd had the yellow paper for five months at that time. And I did find on our Slack,
[18:07] you know, a bit of a thread where things I think from you, Christoph, were being discussed by Jim. I don't know, did you guys interact directly at all on testing—Jim, Christoph?

**SPEAKER_02:**
[18:18] Not directly, not as far as I can remember. I mean, maybe there were some messages—I mean, it's been a while ago.

**SPEAKER_01:**
[18:26] I could be wrong. I may have met you briefly in London when we had that conference. But it would have been like quick greetings at an afterparty or something.

**SPEAKER_02:**
[18:35] I mean, 10 years ago, lots of people, sure. We were testing the GitHub repo, and we had all the major clients using it. And I was interacting, mostly asking, responding to questions. I mean, of course, the C++ team I was super close to. I used the C++ team also to pre-fill the tests.
[18:51] So this was by default, except we found there was a test failing, but actually C++ was wrong. So sometimes this happened. The test was not really failing, just C++ was wrong. But in the majority of cases, C++ was right. So we were just having those conversations, and we found tons of issues. We did—not just in the beginning, I wrote those tests using actually bytecode, the very first tests. Then I went to a low-level Lisp-like language. This was LLL. This was the
[19:17] precursor to Solidity by Gavin. And then in the end, actually, I had automated, like, fast testing where I wrote software that would create thousands of tests—we had some AWS, like over 100 cores of machines constantly creating tests, and we had always some failing on some versions of Geth or other clients. So this was mostly what I did during one and a half years.

**SPEAKER_08:**
[19:41] Right, right. So yeah, for the viewers, something that Ethereum chose to do differently from Bitcoin was to have this specification separate from the client software, right? So, you know, when Bitcoin started, it was the code that happened first and the white paper afterwards, but the white paper wasn't a protocol specification. So, you know, Gav
[20:01] was doing that yellow paper spec in parallel with the C++ client, which was sort of the first one, while you have Vitalik working on the Python client, Jeff working on the Go internally, but then you've got all these other clients as well, right? So the Java one by Roman, I think, started in about April or May. You know, ourselves, Jim and Kieran here with,

**SPEAKER_01:**
[20:23] with a Haskell client starting in September. You had JavaScript as well. Right. It's more like a library. I don't know if it's really like a syncing client, but they had all the tools so you can, in your web app, kind of integrate parts of it to verify certain states. Yeah. I mean, I think maybe they had a syncing client at some point, apart from it obviously couldn't actually keep up, but theoretical. And...

**SPEAKER_08:**
[20:47] And yeah, a little later, there was a Ruby client as well.

**SPEAKER_01:**
[20:49] And yeah, at one point there were eight different clients. Right. If you want to, I can tell the story of why we all are using Geth today. Yeah, this is absolutely not a given at the time. Yeah, of course, everyone had different opinions, but the C++ client was really the fastest, the most solid one, passing all the tests and so on. But Gavin always wanted to add new features. We went to a refactoring and he was a perfectionist, which is not bad for this kind of software.
[21:19] And then the time came for the security audit, because everybody wanted to launch Ethereum now. And we said, before we launch it, those clients need to have a proper security audit by an external company. And one of the companies doing this was Deja Vu in Seattle. So I actually went there with a team for the audit. And because Gavin wanted to build some more features, he said, well, let's just—Geth can go first. Let's first audit the Go client. When they're done, I'm done with the features I wanted to build. And then we're going into the audit for the C++ client.
[21:54] So Geth was audited, they had some issues, they fixed the issues, and now it's fine. And so there was technically no reason why—not, well, actually, we could launch Ethereum now. We have a fully audited client, testnet is running for a while, no major issues, no failing tests for a long time. So why would we wait for the C++ client to be audited? I mean, they all really had the pressure of money was running out, we need to launch now. So, and then the decision was made, let's launch with Geth.
[22:24] They can still use C++. It's just not audited. Let's say in two months or so, the audit is done, and then they can use C++ even more if they want. But then the big mistake was, in my view, when they made this announcement of you can start now, they recommended using Geth because it was the audited one. So almost everybody ran Geth.
[22:42] This was like, we started with almost 100% Geth, and then there was just a minor other clients using, only very few did use them. And so after the audit was done, nobody switched. "Sure, but Geth is running, I'm synced, what's the issue? Why should I switch?" And so we had this 19:1 or 18:2 distribution. It just stayed like this.
[23:03] So if Gavin would have been either, say, let's just do the audit now, and we just have both audited and then start, maybe we would have 50-50. Or even the other way around, if they would have first audited in C++ and Ethereum had been launched without a Geth audit, they would have received a total switch. And then, of course, money was going low in the foundation. They had to reduce the team. And because Geth was the most used one, there were some issues with Gavin.
[23:29] Another story, maybe have a talk with him. And so, in the end, Ming decided to basically kick out the complete C++ team. This was then shortly before DevCon 1—so something like November, October-ish. But yeah, I think the reason for that was also C++ wasn't really that used. Also, there are other reasons as well. But you can see how a tiny thing can have such big consequences down the road, like him doing Polkadot today and all of that.
[24:01] And he was great. I mean, I really, I still think, maybe we would have had a mistake in sharding way earlier if Gavin would have stayed. So without him, they moved slower. And of course, the price went up. There were no security relevant things. So changes happened not quickly anymore, but take more time, and so on. But I think this was a big loss for Ethereum that Gavin left basically in 2015.

**SPEAKER_04:**
[24:22] Yeah, it's amazing. The client side was the cause. I think it was part of it. The process maybe started with the Red Wedding, which we discussed in some other early days of Ethereum episodes.
[24:33] I remember very clearly in the room—it was like two weeks into my Ethereum tenure at that time—that he was talking about brain drain if it was only going to be a nonprofit foundation and not going to have a commercial arm.

**SPEAKER_01:**
[24:48] Yes, there were more issues than that. Definitely. This was not the deciding part, but it was like those things were adding up. I remember that Gavin had this idea of turning the foundation into a DAO and then having a for-profit entity next to it, which would build things and make money. So there were many different commercial ideas at the time. So he then basically started on his own Ethcore. I remember he wanted to have me as part of it, but I decided to do Slockit at the time. So that's why I did not become a co-founder of Ethcore.
[25:16] Another story—we can go into this if you want, you know, what happened after that. But there are many reasons, part of it. I think also him and Ming didn't really get along too much. There was not really a trust relationship going on. Of course, money running out, different visions of how Ethereum should evolve technically and economically, if you want.
[25:36] All played a role, but I think it was just one part that the C++ client was not really used that much, and the reason for that was Geth being audited, and launching without an audit for the C++ team. Yeah, I mean, talking about features—so, so many things happened, right?

**SPEAKER_08:**
[25:55] Gav had this period of incredible productivity between that December and that April of getting from nothing, just having the white paper, all the way through to having a working client, having the yellow paper.
[26:07] As you mentioned, you know, there’s this diagram showing how Whisper and Ethereum and Swarm were intended to fit together, and I found some more timing on that. Swarm was envisaged by Daniel Nagy as far back as 2011.
[26:21] It was an idea he’d been working on for like three years before that. I spotted on the Whisper presentation that Gavin did that that was a pre-Ethereum idea as well, so it was probably only when all of these people came together—it was like, well, you’ve got this storage idea, you’ve got this blockchain kind of like CPU/database-y idea,
[26:41] and then if you have messaging, all of these things can fit together. But it’s also, we’re going to build our own IDE as well. Browser. Browser, Mist Browser. I'm sorry? Plus the Mist Browser.

**SPEAKER_01:**
[26:52] The complete thing—it’s a complete platform for decentralized applications, end to end. This was the big mission and also this was what attracted me to it. I mean, having someone having a really proud vision of a new internet, if you want. That’s what he called Web3; that’s where the term comes from. Because it was not just a little tool, it was a complete new internet called Web3, from data to messaging to smart contract blockchains to IDE to browser.

**SPEAKER_08:**
[27:22] And this vision was very, very attractive. This attracted all the talent and the developers because they loved building that. Yeah, I mean, it’s a very, very expensive vision. And yeah, it was, you know, Gav—as you say, you know, Web3 was him. Prior to that, the language I saw was really about Bitcoin with smart contracts. You know, that was really sort of the genesis of Vitalik going through
[27:50] that journey of colored coins and master coins and meta-protocols and that kind of positioning of Bitcoin as a calculator and Ethereum as a smartphone.

**SPEAKER_01:**
[28:00] But it was all that kind of blockchains and applications, right? It wasn't that full Web3 vision, which I think really came from Gavin. You have to attribute this to him. He was having this big vision. This attracted also many people. It attracted even the business people—they could now understand what it actually is. Other than—this was just a tech, let's see—but this is like a broad vision of how business would function, how this new financial world would happen. They could understand this far better.

**SPEAKER_08:**
[28:28] Than having this iPhone/calculator comparison. This was maybe a nice technical thing. Yeah. Yeah. But then for it being a very expensive vision, that's a lot of work. Sure. But I just thought somewhere... That's it. So I mean, you know, talking about Gavin, the features—so yeah, there's a ton of stuff on that C++ team. AlethZero as well. And AlethOne. So AlethOne being the GUI...

**SPEAKER_01:**
[28:56] Miner. And then I know—how would you describe AlethZero? Kind of the first interface to the blockchain in some way, like the first graphical interface to a blockchain client.
[29:08] And what could it do? Of course, you could mine, you could deploy a smart contract, you could visit, make it visible somewhat, what's happening there. It was not really end user friendly in any way, but it was just a replacement of what people just do on the command line. Usually, command line, when your client has some input, has some output, and it was the first kind of graphical user interface, graphical user interface replacing the command line. I guess it's sort of like a combination of...

**SPEAKER_08:**
[29:33] Like what you have with the block explorer now, apart from it, that's like a view only, and this was both a view and a do.

**SPEAKER_01:**
[29:38] But yeah, those GUI clients, but much more influential than the Mist browser. The Mist browser—I think there's a video by Alex van de Sande, it's like a 10-minute video on YouTube—they had this prototype. They're not working yet, but just fake it until you make it—the vision of the Mist browser. And this also really made us understand how Ethereum could work for the end user: having different identities connected to wallets, and you would load those dapps. Is it an IPFS hash or...
[30:03] even over Swarm one day, the app was loading, and you could do some finance stuff there. This gave us an idea of what Ethereum could be. So you have to think, yeah, Vitalik gave us a rather technical vision and a profound intellectual thing, but Gavin gave us this pro-internet vision. Alex van de Sande gave us this very concrete thing of what an end user could do with that in the next six to twelve months, maybe. That's very important.

**SPEAKER_08:**
[30:32] Just yesterday, actually—so there was an announcement from Uniswap about them turning on fees and doing various things that are more kind of to do with the company and the protocol tying together. And I saw a reaction to that saying, "Well, I'm never going to use this again. You can't extract ongoing revenue out of a protocol." And this person then said, "It's time for Mist 2." Totally. I've heard this before. We need the full vision so that you've got hosted and dapps and you don't need a server and you don't need a company and you can just make this pure, immutable smart contract wrapped in a UI that's all decentralized.

**SPEAKER_01:**
[31:02] You think we could have a Mist 2? I would love to see this. I heard people thinking about this before. I don't know if anybody really started the project, but...

**SPEAKER_04:**
[31:12] Should be totally doable today. It's not rocket science. You know, let me interject. We ourselves have made sort of different attempts at this where, like, you just download the app from the chain itself. Pretty much it worked fine, and I guess it just wasn't as much a differentiator. Like, it made things a little slower to do it this way all the time.
[31:36] I also think, like, one of the people that took the Web3—the world computer vision—sort of seriously, it was like the Internet Computer people. And I don't know anyone that uses Internet Computer, but every once in a while I see tweets about it, and I'm like, "That sounds great. Yeah, start the app from the chain." You know, it's got some cool smart contracting language in it. Yeah.
[31:55] I guess there's just no demand if it slows the app down even slightly. And I think MetaMask and then many other wallets were sort of enough—still not the whole thing—but yeah, I guess it's like you got to get people to use it if you want it to be maximally cypherpunk, too. I fully agree, and I mean, yeah...

**SPEAKER_01:**
[32:14] The problem with this is you only need it if you really need it. Meaning, if Uniswap failed, the interface is not there. It's like a backup. But it's not what you want to use daily. And if you remember, maybe, Kieran, you were there at DevCon 1. When they presented MetaMask,
[32:33] my first thought was, "Oh, this is totally away from the vision—like, how can you not run a full node? How dare you, like, just serve over RPC with Infura?" Like, almost—not a scam, but it was not what we intended to build. Today, it's like, this is a decentralized version of it; this is, like, non-custodial—the MetaMask guys are the good guys
[33:01] compared to all the others. See how the view shifted over the years. Back then, it was absolutely required to run a full node with the Mist browser—this is how it’s done. And now we have MetaMask plus Infura. And today, this is really the version which is viewed as the original non-custodial Ethereum vision.
[33:21] How things are shifting, basically. But yes, you only need those things if things are falling apart. Just as an example, so many people use the Gnosis Safe. Let's say the Gnosis Safe UI is gone. Technically, it shouldn't be a problem to run another one, but there really needs to be something on IPFS, there needs to be something which can self-host, so I can still access my wallet without going to the command line.
[33:42] So for those reasons, you need it. And the Mist browser was sort of as the fallback for every dapp. Of course, you can have your application run on a normal .com domain on AWS, fine. But if you could serve the same app in a decentralized fashion as a backup, this would be great because you could still use it if the company—for example, Uniswap—if the company fails. If someone builds a nice Uniswap UI served by IPFS, directly interacting with the smart contracts…

**SPEAKER_04:**
[34:14] Yeah, that's fair. Also, Uniswap, I think, is controversial. I know Jim wanted to say something. Controversial because they had the company-level fee skim, and then I think they've turned the on-chain fee on.

**SPEAKER_08:**
[34:28] I don't know that they've turned the company fee off—I haven't read that for detail.

**SPEAKER_04:**
[34:32] I believe so, because one of the replies was saying, "Okay, so how are your shareholders gonna like that?" Yeah, okay, fair enough. Well, hopefully they hold a bunch of the UNI and it will, you know—tomorrow they're doing a bunch of burns so that it should be to the benefit of all stakeholders. But yeah, just sort of this interesting kind of contrast, right, between
[34:54] completely immutable, force-of-nature smart contracts versus more permissioned, more tied to a company, more wanting to have fees for maintenance kind of question.

**SPEAKER_01:**
[35:05] I mean, it's like treasuries, I guess, either or. But this opens up the questions: how should the Ethereum app be built economically? And this was also a question being answered during that time. This was being—the DAO was one approach of it should be fully on chain. All the revenue should be on chain. There should be no for-profit entity directly attached to it. And Slockit, the company I built after that, would be a service provider for them, getting paid by them for work being done for the DAO—one version.
[35:36] I was always skeptical and still am about companies where you have effectively two cap tables, meaning you have a token cap table if you want—of course, it's a utility token, governance token, and so on—but effectively, it's kind of ownership in the protocol. And then you have a for-profit company with shareholders. And this is always, I think, very dangerous because you don't know where to go into—where's the value? On the shares of the company or on the token?
[36:08] This was the main reason all those companies had those non-profit foundations in Switzerland—rightfully so, because they said you only want to have one cap table. Like the Ethereum Foundation—there were no shareholders of Ethereum. There was a non-profit foundation and a token. The token, if you want to have a share in the economic success of the protocol, you would buy Ether.
[36:29] And so later on, there were many other token projects where they had a non-profit foundation—so no shareholders, no second cap table, and then you would have only the token and all the value would be there. And now with Uniswap you have this problem of having again shareholders and tokens, and I think that's dangerous and not a good idea, actually.

**SPEAKER_08:**
[36:54] Yeah. Yeah. So, perhaps let's talk about DevCon—actually, just before we get to DevCon 1—so the launch, right? Obviously a lot of testing and coordination and this different series of proof of concepts. So, I mean, when—how did you know it was good enough? Like, what was that testing flow and collaboration like?

**SPEAKER_01:**
[37:18] So there are many indicators, one being the Olympic testnet running smoothly for a while, other one where C++ client having an audit which worked. And then they were saying, OK, now if Christoph doesn't find any failing tests for like three weeks or four weeks or something, we are ready. And this was the case. And so we said we can set a launch date.
[37:39] The launch itself is also a bit—typically Gavin or also Vitalik, nobody wanted to push a button, like nobody—just like start the chain. So what was done was there was a script written which has as an input parameter the hash of the Olympic testnet at a certain block height. So everybody could, using this script plus the software—plus C++ or Go client of course—
[38:00] plus the hash, which was at that time in the future of the Olympic test, let's start that chain. So there was no—at the launch day, we were just viewing it. There was nothing to be done. It was like, everything was—all the information was out there. People were just simultaneously starting the blockchain. And then over the peer-to-peer network, this was actually the more harder stuff. They found themselves on Reddit and others to share IP addresses: "connect to my peer, connect to my peer."
[38:28] And so then they started to come together, and of course the longest chain was the valid one. So as soon as you found a peer which had their own chain, you would say, "Yes, this is a longer one." You would stop and start mining on top of his chain, and so basically the canonical chain emerged from that within, I don't know, 30 minutes or one hour, and then we had the chain running. And this was
[38:55] like a beauty to behold—to just see how this works out as intended. Completely decentralized. Nobody did anything. It's just—I was in the C++ Berlin office in Kreuzberg,
[39:08] nice office, and we just watched it. And we were somewhere mining there with the laptop. And we were all excited as it started. I actually think two or three weeks after, or maybe four, we had the first little hard fork, meaning there was some smart contract doing something that Geth and C++ had a different result. It was, for me, almost the middle of the night, like 10 PM or 11 PM. So I remember seeing this, looking for one hour or so, finding what's the issue. Then I found it, wrote a test about it.
[39:38] Peter Szilagyi was right. Geth was wrong. So we gave it to Jeff, they fixed this. I think we said one hour and then like after five hours, everything was done. It basically called up the miners, "Please update your client." And then it was fine. So this was the early days, but it was a successful launch. Nevertheless, did the Haskell client sync at Genesis? I do not know, Jim.

**SPEAKER_02:**
[40:04] No, we were able to sync at Genesis time for like a year or so we were syncing. But I remember like that week, Kieran and I were more interested in trying to get a miner in place. So that was what that week looked like for us.

**SPEAKER_04:**
[40:18] Yeah, I had—I was living in an apartment just south of Berkeley campus at this time, and a woman had taken me to Fry's to build a machine a few months prior, like a build machine. It had a good GPU in it. Yeah. Fry's is dead now. RIP.
[40:33] So I was running a miner there and we built a couple in Jim's garage.
[40:37] It got very hot in Jim's garage, which was—you know, those things were consuming a fair bit of power. Mine exploded after a few weeks. It was actually just the power supply. So I thought the whole machine was bricked, and Jim said, "You know, I think everything but the power supply will be okay." And it was the case that everything but the power supply was okay, but then I stopped mining.
[40:58] And I think Jim would shut—we didn't even bother to buy cases at that time. Right. Yeah. You may have had a case. I had mine just sitting, wires out. Yeah. Yeah. Indeed. Sure. At that time we were always, you know, sort of, at least at that time, shorthanded people wise. So it's catching up a little bit on the features, etc., but it ran perfectly well.

**SPEAKER_01:**
[41:23] There was always new features coming. I remember one of the sweet memories during the pre-launch: sitting together with Gavin, Vitalik, Jeffrey, and me in one room at the C++ office—like, the nice Gavin office. He had this 80s-style thing. And we'd think, OK, what was wrong in our protocol? Then they discussed the whiteboard changes. Then the first day: "OK, Christoph, you add a test for this protocol change." Then we are, at the same time, coding it.
[41:49] "OK, you're done creating your test? Let's see if they all pass it. If they all pass it, it's like done: new feature, directly new release." And so this was done with all the other clients. So they basically had to catch up. It was like information update of the yellow paper. Here's a new test. Here's like a little Etherpad description of what the new protocol looks like. And then please update your clients. Yellow paper got me to a certain point.

**SPEAKER_02:**
[42:18] Sorry. Yellow paper always got me to a certain point, but it was always behind the other clients. So I would always find out that I was behind because I went in the morning and connected to the testnet and I was no longer connecting or I was getting some state mismatch or something. And then I'd have to go and dig through usually the C++ client. I think there was maybe one or two times where
[42:39] I can't remember why—I think there was one or two things that went to Geth first—but usually it was C++, and I'd have to go digging through the newest code to find the changes and then bring them in, and then a few weeks later I'd see it in the yellow paper. So, yeah.

**SPEAKER_08:**
[42:56] Yeah, so unlike what you have now, where leading into a hard fork, you know, you've got all that discussion and spec-ing up front and like applying the code into the clients that only enabled for a testnet, and going through that dance, and then ready to go. Yeah, I mean, at that point, as you say, it's kind of like done in those clients first, and then back later.

**SPEAKER_02:**
[43:17] It looked like from where I was standing, it looked like there was a lot of competition between the different clients and the developers there. And I think they sort of, like, took pride in having the new thing in as fast as possible. And so that sort of led to an environment maybe where there was not as much discussion. It was like, "I'm going to throw it in and then I get the bragging rights."

**SPEAKER_01:**
[43:39] There was always a fight between Geth and the C++ team about who's the best. And Gavin was having a big ego. And Jeff was more like, "Just give me the new spec. I just code it." But yeah, it was more or less this decision by the three of them. I was basically playing a very major role in the room and then writing a test for it. But they discussed it. After it was cleared, they just did it. But it was pre-launch. After launch, of course, this was different. So I'm saying about having…

**SPEAKER_08:**
[44:08] Sorry, go on, Jeff.

**SPEAKER_02:**
[44:09] Oh, I was just going to say, like, I know, like, a lot of the changes were just, like, some change in the EVM or pricing or something. And so often it was like, you know, I would, like, freak out in the morning when I wasn't working. But then, like, by 11 o'clock or, you know, a.m., I had found, like, "Oh, I see, such and such opcode just doubled in price," or something. So I would just put that in. But the big one was RLPx, which is essentially, like, a big SSL replacement.
[44:36] And that one was, like, freaking me out for a couple of weeks. I was, like, digging around trying to find any information about that. Eventually I had to reverse engineer—maybe that was the one that was in Geth first. I can't remember.
[44:48] But I had to sit there and reverse engineer. I had to run either C++ or Geth and then put lots of logging information in to see what in the world was happening, and then print out all the stuff, and then find, like, the appropriate, you know, crypto libraries to mimic that. And what was the background on that and how it went in so quickly?...

**SPEAKER_01:**
[45:10] Like, there was nothing in the yellow paper about that at all. And when that came in, it was just a shock to me. Just—do you know which time this came? Because I was focusing on the Ethereum Virtual Machine at the time. This was more like—okay, I know Gavin—I think was Gavin doing some optimization? He was always thinking about the long term, so if something would be 10% more efficient, you have to do this, right, I think.

**SPEAKER_04:**
[45:37] So I remember there was a devp2p, libp2p website that was released about that time. It still might have been after the giant change went in. Also, we were working together regularly in the Bay Area at this time,
[45:53] so Jim did, like, 96% of the changeover, but we had at the time, like, separate processes—one was more like a client and one more like a server—we merged them later.
[46:02] And yeah, it was like—so there was a big document describing how the DHT for peer discovery would go in, but then you needed, like, a way to identify the peers maybe. And this system kind of gave them an identity with, like, a—you know, in an SSL style—basically there was a node cert, in effect. And then you had to like—there were session keys, and you know, this, that, and the other. It took a long time to implement that thing.

**SPEAKER_08:**
[46:29] But yeah, I think—maybe Bob, you would know that—I think this was, someone else wrote this big thing. This might have been Alex. Yeah, it was—Alex did that.
[46:42] So, saying about sort of documentation or whatever, there was a wiki, right? It was an Ethereum wiki and a number of things were documented only on the wiki, and I think these kind of wire protocol pieces were part of that.
[46:53] But yeah, Alex Leverington was the first hire into that Berlin office. And he primarily—I mean, he worked on a few different C++ things. But the main thing he's known for is devp2p, which was that common underlying P2P protocol. Though you already had libp2p, which is the transport for IPFS. That already existed at the time. So it was a bit of not invented here going on.
[47:18] But, yeah, he was there for DevCon Zero as well. And he spoke on Alex. I was not too much into the peer-to-peer side of the codebase. I was more into the EVM and Solidity smart contract side. You know, there was a bit of funny crossover with the later part of yours: Alex Leverington worked with
[47:38] John Gerrits on a project called Airlock.

**SPEAKER_01:**
[47:42] So I remember that. I saw it later, like after we did our presentation and had the Slockit and stuff going—they showed us videos of it, it was even earlier than us. So yes, they were, actually, timeline-wise, they did this before we did, but I did not know about it at all. So we did it more or less in parallel then, and we just launched a bit quicker, to go into the public with the project. It had been from their side more like a little side project, didn't look like a big company, or intended to be.

**SPEAKER_08:**
[48:13] Yeah, I remember this project a lot. Yeah. So I think that was at the hackathon at the Bitcoin Expo in April 2014 that they did that. And Stefan actually did an interview with them—you can see that on YouTube. You know, this is like talking about early Ethereum projects.
[48:29] You know, and this is like over a year before the mainnet, like so far back, some of these. But yeah, like some of that spec stuff, it was not in the yellow paper and it was just sort of floating around, and a long time before there was real consolidation of that full client spec. But you managed to do it anyway, Jim. You managed to build the client.

**SPEAKER_02:**
[48:52] It was a busy week. But it was just notable to me because, at least from what I was seeing, it went from zero to one like overnight. I had never heard of it the night before. And then the next morning it was in the clients and working and I couldn't connect to anything.

**SPEAKER_01:**
[49:10] Which is normally the pattern, but yeah—just this one was the biggest one-time change that I can recall either. Yeah, and again, this was pre-launch days. Things had to move fast. There was a lot of pressure going around. It was messy. There was not much coordination between the clients except for maybe some Skype groups, and in the end, yes, Vitalik, Gavin, and Jeff just made decisions and executed as quick as they could.
[49:38] So this all changed after launch—then things became a bit slowed down and people consolidated, and every change was a big thing, rightfully so.

**SPEAKER_08:**
[49:50] Yeah, so back on the timeline—so it was July 2015 that Mainnet launched with the Frontier hard fork. And then as you touched on, you had Ming. So Ming's first official day was the 1st of August 2015,
[50:05] at which point the foundation had been running on for a year or so and was close to out of money. Touching on your thinking it would only last for a certain amount of time, a year on, that raise, which I think was around $16 or perhaps $18 million, was nearly all gone. So you have these quite hard decisions about what...

**SPEAKER_01:**
[50:27] Which part of this grand vision was going to be funded initially. Right. And I remember talking to her at the time. She felt like, "I have to clean up the whole mess," like, the paperwork and everything was totally messy, working with lawyers, accountants, and so on, and getting a clean up basically of the foundation. I mean, for me, I did expect it to last something like that. So it was for me, it was clear they are not making any money.
[50:52] I didn't know, like, how big the reserve was—the detail, I think, was like, I don't know, five percent, something in this range—like, how much ETH the foundation held at the time. There wasn't that much value either—price like 50 cents, one euro or something—so it was clear this would not last forever. So I was thinking about going back to my PhD. But then I came across this idea about Slockit and building a company. Slockit was the idea of, maybe similar to Airlock,
[51:23] smart contracts are essentially permission systems. 90% of a smart contract is who's allowed to do what. In case of the ERC-20, it's just who's allowed to send the token or setting an allowance. And in terms of the DAO, it's who can vote for what and making decisions, and then money gets sent. So what if we could put this permission system into IoT?
[51:47] And who's allowed to switch on, off, use, change, admin rights, whatever—you put this into a smart contract. And I thought that Ether will never become a currency. Bitcoin was a digital currency. And actually, if you talk to Ethereum people at the time, we were not thinking about competing with Bitcoin. Bitcoin was a digital currency. We were building a platform for decentralized applications. Ether was just used to run it. I once heard the statement somewhere on Twitter where everyone said,
[52:17] "Bitcoin is a currency which needs a blockchain to function, and Ethereum is a blockchain that needs a currency to function." I think it's very true. And so I thought, okay, Ethereum will not be used as a currency, but it might be used as a currency for IoT devices—instead of the Internet of Things, building the Economy of Things.
[52:41] And this is kind of what drove us. And then we wanted to build this Universal Sharing Network as an application. At the time, Uber and Airbnb just became big. We thought, well, all those sharing economy services should run on-chain. So let's build this called the Universal Sharing Network. Then we thought about how to start with something tangible, and then we had this door lock. Actually, it's here in the background. If you see it, it's there.
[53:10] I have this DevCon1 physical smart lock, which we connected to the Ethereum blockchain using our own software and had this idea of people paying to open the lock. And that's what we presented at DevCon1,
[53:27] together with this idea, which actually only came up three or four days earlier, to connect this with a DAO. And the rest is history, what happened after that. But we didn't intend, and we didn't start Slockit for building a DAO. We wanted to build a Universal Sharing Network. Then we thought, well, this is way too big for us. We want to now focus on this Airbnb use case for door locks.
[53:54] And then we thought about fundraising. We talked to a bunch of VCs. I actually remember flying to New York, talking to VCs there. Everybody said no. Then I met Joseph Lubin. He said, yes, maybe under some conditions. We just did not agree on the terms in detail then. But I presented at the Bitcoin meetup in New York. And they're all like—the first application was a Bitcoin application about arbitrage trading. It was kind of boring. And then I came with a door lock. It was super fascinating. You could open the door by paying some Ether.
[54:27] So it went well, but we didn't have any money. So we thought about doing something like an ICO. But this was now after the launch of Ethereum. So if I started coding an ICO-like smart contract, why should we have the money directly? It could stay in the contract and then people could vote for giving us part of it.
[54:47] Then we said, well, we could make proposals to it, and then they can vote if the proposal is good or not. Then the money would be released to us. Then we think, why could not everybody make a proposal? Everybody could pay it. Everybody can make a proposal. And now it's completely open. And we are just one of many service providers to the DAO building this Universal Sharing Network. And this was the origin of the DAO. And only again, three days before DevCon 1, we actually decided we would go for it and put it into the presentation.

**SPEAKER_08:**
[55:22] Yeah, amazing. I mean, so on the timeline, again, trying to judge it. So Stefan was, I guess, Chief Communications Officer until September of 2015. That's when he left. Had you left already by then? Can you remember?

**SPEAKER_01:**
[55:38] No, I didn't really leave because I was technically a freelancer, although I was working full time for it. I didn't have like a formal employment contract. So I was continuing to work, I think, until the end of the year. And then I just talked, well, just put down my hours, basically. If you need me, tell me. I just invoice what I'm doing. But I was really leaving, actually, in December, January.
[56:04] I think the last invoice was for December. And when Stefan Tual left or was being left, there's another conversation how he left the foundation. He didn't agree with some people getting Ether, which is another story for another day, I guess.
[56:25] But he was really a crucial part in building up this Ethereum community. Like all this meetup culture—the meetup culture didn't really exist like that before. He was going from place to place, finding someone, running meetups. So he was very important for that. And I know I was a coder. I processed Simon, who I co-founded Slockit with, was also a coder. We needed someone who can talk to the people, can do marketing and this stuff. And we said, well, he has the right address book, he knows the right people. Everybody knows him in the community.
[56:55] I think, let's ask him if he wants to join us. And he did, and I think he was a very important part of making the DAO what it was later on. He did some messages which I also didn't like, and so he ended up a bit in disgrace with what happened then. And I think the community was very, very hard with him because he was not always reacting maybe as he should in some situations after the hack. But nevertheless, he played a very important part in the history of Ethereum and also, of course, the DAO.

**SPEAKER_08:**
[57:24] And so DevCon was November 2015. So that was announced earlier in the year, I think September-ish, but ended up being cancelled, you know, because the foundation were basically, you know, this same "running out of money" piece.
[57:38] But then primarily with ConsenSys funding and support, you know, hey, it's back on.
[57:45] So that was in London, and, you know, significantly larger event, obviously, than DevCon Zero, because it was the first—you know, public Ethereum outing with Microsoft as a headline sponsor. You had Nick Szabo speaking as well. Maybe Satoshi, maybe not Satoshi. I don't think he said that. Strongly alluded to it in the presentation. It was funny. So, yeah, how was that for you then, Christoph? What was, you know…

**SPEAKER_01:**
[58:10] It was totally different than DevCon Zero because this felt like now we're going out in the world and showing to the public. It was a fancy space in London. It was a really fancy, like almost cathedral-looking, space for 2%. Again, we had Vitalik and Gavin talking about the vision of Ethereum. And if you look at the talks being given,
[58:29] I really think entrepreneurs today should just rewatch them because they all have been 10 years too early. Be it about uPort building identity solution; I think it was Boardroom doing that governance on chain; many, many ConsenSys startups, of course. We as Slockit thinking about, well, let's connect IoT to blockchain—again, all of that 10 years too early. I remember also Simon...
[59:00] Speaking about—no, not my brother—I forgot his last name, but Simon speaking about everybody getting a token. He really predicted this token economy would now thrive, which happened. So it was a great place to be. Everybody was looking into the future, building the future. It was very, very exciting. It was very important that ConsenSys was funding this. It was crucial, this DevCon 1 moment showing Ethereum is live now. We show you what we will build with it. But still, there were no applications running.
[59:31] It was all visions and thinking. It's one reason why when we then did the DAO, the DAO was held as almost the first real thing you could do with Ethereum—that's why so many people jumped onto it. And then, maybe just finishing this off, the narrative changed. It was not anymore a DAO for the Universal Sharing Network, but maybe because of the curators we chose—which were like
[59:57] important figures in the Ethereum space and many other things—it turned into like an investment fund or like an index fund for Ethereum applications. Because now after 20, 30, 40 million was in, it was clear this was not just money for Slockit and the USN, this was money for more cases, and more people applied for it. It became like every
[01:00:22] decent application, or many of them, not everyone, saying, "I'm applying for getting funding from the DAO." So the DAO would fund all the applications. So it's like: you invested in Bitcoin five years ago, became rich. Now you invest in Ether, went well. And now you can invest in the application layer. You do that through putting money into the DAO. This was not the story we told, not how we intended it. But that's how the narrative changed during the fundraising, and then it became that big.

**SPEAKER_03:**
[01:00:54] Yeah, but it was interesting. You're saying that...but I cannot hear you. Maybe it's—maybe it's just me. Can you hear me? I mean, I am sorry. I have an issue here with my... Do you...? This is me, system. So... Now I'm back. Can you hear me? Can you hear me, Christoph?

**SPEAKER_01:**
[01:01:13] No.

**SPEAKER_03:**
[01:01:14] I get to switch back to... Let's... Can you hear me now?

**SPEAKER_01:**
[01:01:18] Yeah, I can hear you. I could always hear you, some reason.

**SPEAKER_03:**
[01:01:21] Oh, we've heard you anymore. This was like me an hour ago, by the way. Streamyard. OK, my audio is completely broken, so I will try to fix this. We can continue.

**SPEAKER_02:**
[01:01:32] I basically had to close it and come back again with my earphones, but I don't know. Perhaps while we're waiting, Kieran and Jim, you could talk a little bit about the Strato launch. I thought you were going to say you could sing a little song. I got nervous for a second there.

**SPEAKER_04:**
[01:01:48] You know, OK, so in this period of time, we were just—reconnect. Just turn off and on again. We were working as part of ConsenSys, and one of the kind of marketing/business development people at the time, Andrew Keys, primarily, had put together a partnership with Microsoft. I don't know if they ended up
[01:02:12] co-sponsoring DevCon1 per se, but their headline, yeah—they put money in for that because they also like paid for a bunch of PR and all those sort of things too.
[01:02:22] And so we had maybe a month or two lead time to work with them. And so the idea was that we
[01:02:28] —you know, they've got cloud infrastructure. It's a good place to run blockchain nodes. They also have corporate clients that were actually very interested in the technology. And so we worked
[01:02:36] pretty closely with them in the run-up to make our software available on the Azure cloud, as did Roman of the Java client, which to some extent was everyone's preference because people know Java in the enterprise world, but I think they
[01:02:49] —we sort of stuck with it quite a bit longer than Roman did. And, you know, sort of blockchain as a service was the big announcement—it was December 2015. There was November. Was it November? It must have been December. Really? November. There was a—once the announcement happened, there's a little tick in the Microsoft stock price, which we were like, "Whoa! There's a little bump there!"
[01:03:12] And a lot of excitement, for sure. Got a million phone calls after that. That was like a good feeling of being the hotness that only happens so many times in someone's life. But tremendous interest on the back of the blockchain as a service announcement. We did a live demo. It was fun. The internet gets in vogue to make fun of the UK these days on
[01:03:31] X, etc. The internet in the conference facility was not so good. So I was very worried about the transactions actually going through. But they did during the live demo. I think there's footage of it somewhere. Can you hear us again now, Christoph?

**SPEAKER_01:**
[01:03:47] Yes, I can hear you. I hope you can hear me too. OK. So the demo that you did at DevCon 1, again, another iconic event.

**SPEAKER_08:**
[01:03:55] Because, yeah, you had that physical smart lock just sitting there on your shelf and, you know, it rotated, right? You know, you did your transaction...

**SPEAKER_01:**
[01:04:03] We just had a Raspberry Pi connected via, I think it was ZigBee or Z-Wave back then, to the door lock. And on the Raspberry Pi, we had actually an Ethereum client running. And we had a smart contract on-chain where you could send some money to it—or Ether, actually. And when it received some Ether, it would open up. This was basically the demo.
[01:04:26] But it was cool to see something physical, something using Ethereum for, as I said before, the economy of things connected to IoT devices. Since most of the people in the room are still nerds and devs, they love that kind of stuff.

**SPEAKER_08:**
[01:04:43] And there was also the kettle, wasn't there? Yes, there was also a kettle. Maybe it just turned a smart plug, like a power plug. We could also turn it on and off. Same protocol, same thing. So we just wanted to show it's not just the door lock company, because actually we're not producing those. We're just connecting existing door locks to it. We want to show this idea of the Universal Sharing Network. Everything which you can turn on, off, or lock up and unlock could now be connected to this network. And everybody could…
[01:05:13] They put almost everything in there, like a washing machine—you pay for using the washing machine, or a bicycle lock. We even had padlocks connected to it, so you could have, like, your locker room and you have a padlock in front of it and sell whatever's in there by having someone pay to open the padlock. This was the generic idea. I mean, we got some VC money later, after the—like in 2017,
[01:05:39] We built it. Nobody used it. Not just too early. It was like everything for everyone all at once. And of course, nothing for no one. It felt like the app was not great. So we failed B2C-wise. At Slockit, we then turned into more consulting projects. We built Incube, which was an IoT client. Made some money with that. Had about 50 people actually employed at the time. In 2019, we sold the company to Blockchains Inc.—Jeffrey Berns. Another story.

**SPEAKER_08:**
[01:06:11] So I remember speaking to Stefan at the time. So Stefan was involved with that demo, right? It was Stefan who came up on stage to make his little cup of tea with the kettle there. But I remember speaking to him
[01:06:22] that he'd been concerned about what the reception for him would be like, you know, having had this, you know, passing of ways with the foundation just two months before, but he was saying it was all very, it was all very friendly and people, you know, very excited about the project. Right.
[01:06:36] And saying actually about that IoT and pieces, so in January 2015 you had a demo that happened at the Consumer Electronics Show, CES in Vegas, which was a collaboration between IBM and Samsung. So the aforementioned Henning Diedrich, part of that. And that
[01:06:56] —that again was months before mainnet, but you had a proto Web3 stack there, which was I think PoC5 of Ethereum. You didn't have Whisper, you had another thing called Telehash and you didn't have—you had BitTorrent. So there was this proto Web3 stack there and they had demos like a washing machine
[01:07:15] buying its own detergent and scheduling its own repair. So yeah, that was happening a little earlier. And yeah, so I mean...

**SPEAKER_01:**
[01:07:22] So Slockit itself did a number of these different products, right? There was something with electrical charging and something to do with toll roads. Is that right? Right. We had a prototype running with RWE, or innogy, in Germany. They're doing, like, all the time, most of the charging stations. So this was in general.
[01:07:47] We got a lot of attention, of course, also after the DAO hack and all of that. And so that's kind of why we became a consulting company, because so many asked us, "Could we do a prototype with you?" Because there were not many Ethereum builders at the time. So we had been building on Ethereum now since one year, two years,
[01:08:10] which—you could not find anybody doing this—so we were building lots of nice prototypes and some almost production stuff and always related to IoT devices connected to the blockchain. This was our core business. And on top of this, we built those prototypes. We did a lot of work for the Energy Web Foundation—I don't know if you're familiar with them. This was in Switzerland. They are kind of a fork of Ethereum focusing on all the energy use cases. We built most of their stuff in 2018, beginning of 2019,
[01:08:41] until they hired their own developers. And Gavin was also part of this a while. So yes, this was still—I mean, if you remember this time, I'm curious to say, there was so much enterprise interest. Enterprises at the time were just learning, looking into this, wanted to build prototypes, not yet production stuff.
[01:09:07] So there was a huge demand for blockchain experts, for doing consulting, for going to conferences, explain to them what a blockchain is. But at every tech conference, we had some blockchain talk, and this was mostly us. And they paid sometimes like €4,000 for a talk, so as a company we said, "Well, we need the money, let's go there."
[01:09:31] Of course, you also have to think about us as persons—the Simons and me, we didn't get any money for almost a year. We were not rich people, we come from ordinary families. And we said, well, we can work for like three to four months without a salary. Let's build the DAO. And then the DAO becomes big, the DAO is paying Slockit to build it. And of course, after the hack, it was clear there will never, ever be a payment.
[01:09:57] So we made zero money out of the DAO. So we needed to start doing some work. And this was in the beginning, let's do consulting for those large companies. This is how Slockit began to survive. Many people said, "You can bury Slockit after what happened. Your name is burned forever."
[01:10:24] And we decided to stay as a team. I mean, as a founder team, we own our mistakes, maybe we are open and transparent about it as much as we could. It was, of course, an honest mistake. We can talk for it. It could be another session just for the DAO. I mean, the DAO is a lot of topics. I just put here very shortly, just talking about it from a company perspective.
[01:10:55] And then Stefan, he was saying, well, he was trying to get VC money. Simon and I, we were doing those consulting gigs. And once we had VC money, what happened as a company was we got 2 million euros, or dollars, and then we built the product, hired people for that, got more and more consulting gigs. So we always said, well, let's do them and just hire more people. And in the end, we had like 50 people, 5 or 10 doing the product and 40 people doing consulting.
[01:11:25] And then we got bought by Jeff Berns from Blockchains Inc. Remember, maybe at DevCon 3, I think? Four. Four in Prague, right? Wanted to build a city. I think, I loved the vision. He obviously had money. He wanted to build it on top of Ethereum mainnet. I was thinking about how maybe I can channel those billions into the right direction, building it all as intended on Ethereum mainnet, which was working fine for the beginning, and then...
[01:11:55] I found out once you're an entrepreneur, you never can be an employee again. And so I had to leave. But maybe it's just too far in the future. I mean, that's one thing I think I have to say here, because you talked about DevCon 1, and we skipped a little bit DevCon 2. You said in DevCon 1, Stefan Tual was very concerned how people perceived him, and they were very gentle, forgiving, and nice to him. So he was well-received, and then he built the DAO community.
[01:12:28] I was super worried to go to DevCon 2 because this was after the DAO hack. I was like seriously thinking someone might beat me up there. I went to the corner and I said, people, I kind of almost destroyed Ethereum with the smart contract—so much attention to it and all the money lost for some people or the time of growth gone. It depends on how you view it.
[01:12:55] But when I went to DevCon 2, people were so nice, forgiving, basically hugging me. When I was giving the talk there, the only thing I didn't like was the foundation telling me I was not allowed to speak about the DAO, which was like, "I am speaking here to the Ethereum community, how can I not speak about the DAO?" And so I talked about—
[01:13:21] pretty boring talk about security—and I think every second talk was about security at DevCon 2. It was just about how we get those smart contracts secure. So I kept a rather boring talk, but in the end I just said, "Well, thank you for your understanding," and it was about half time, and so on, and there were like some of the standing ovations—I remember becoming emotional because this was—I did not expect this. I really expected, "Guy, you messed up Ethereum. You almost lost it all."
[01:13:53] So I think this just speaks to the Ethereum community—how they treated Stefan, how they treated me—even though mistakes were made, honest mistakes, at least from what I can tell. This is such a great community of really nice people who really want to change the world, capable and also now financially capable of really doing things. I was watching that video quite recently, actually. And yeah, it was quite... Cut off a little bit at the end. The end is...

**SPEAKER_08:**
[01:14:26] You know, it was quite a long ovation there and, and yeah, you could certainly see that emotion in you. Um, and that's when we first met actually was in Shanghai for DevCon 2. I remember was—was on the sidelines there in that main, uh, main conference hall. And, and yeah, it was lovely to see that. That's for sure. Okay.

**SPEAKER_04:**
[01:14:50] Yeah, I think good notes. Just, Bob, you were the one who tried to impose a half hour to hour rule. We're at a solid 1:20 right here. That's it. Like me the other time. Maybe we've reached a good kind of end point, I guess. So what happened after Blockchains LLC for you, then?

**SPEAKER_01:**
[01:15:08] So because of time, I’ll keep it short. So yes, we got bought by Jeffrey Berns—Blockchains LLC at the time. Again, the reason for this being he wanted to build a new city in the desert. He wanted to do all on IoT, all on Ethereum from scratch as a developer dream, building from scratch on a green field on top of Ethereum with our tech.
[01:15:29] And I felt comfortable at the beginning. In the end, I felt like we need to release stuff. And there were some voices at the company who didn't want to release until a very, very big product was done. For many reasons, that didn't happen. I don't want to get into that too much. So after two years, I left Blockchains—back then it was called Inc., they made the change in their name.
[01:15:54] And I did, for six months, I did really nothing. I forced myself to do nothing, which was great after so much stressful years. And then I started a venture studio called Corpus Ventures, where we tried out many different ideas. We had EM3, which was a decentralized messaging protocol; GasHawk, you can save transaction costs on Ethereum. What else did we have?
[01:16:23] So we had some domain name stuff, but we didn't release it at the end. But the biggest one was Tokenize It. And this was—we built something for now German startups. In the end, we wanted to do it all over Europe. We were just tokenizing their shares and doing fundraising.
[01:16:44] In summary, it's like a Web3-based AngelList for Europe. It's the one-sentence description for Americans also to understand. AngelList is a great tool for business angel investing. We want to do the same for Europe—for all countries there—and build it on chain. So tokenizing all those shares and enable private as well as public fundraising. Some called it "legal ICOs," if you want, but also for private fundraising. Our customers currently...
[01:17:15] have more than 400 investments from more than 320 business angels and more than 50 companies. Those are traditional German GmbHs raising from super conservative business angels, doing it completely on-chain. They are paying in stablecoins, getting their tokenized shares in their non-custodial wallet. They're all getting a Gnosis Safe wallet from us,
[01:17:38] using Privy for login. So we build it as intended, and we get normal people to use it. For me, this is kind of a dream come true because I'm out of—I love the Web3 bubble, I love this community, I love to work inside there, but for me, Tokenize It is a way to make this technology available where it belongs, like to startups and investors outside of our Web3 bubble. And I'm super, super happy
[01:18:06] that I could keep up those values that they have—complete platform is non-custodial, they have their Safe on Ethereum holding their tokens, paying stablecoins. So I'm very happy to see this. Over the next years, we want to basically roll out just all over Europe and become, yes, the Web3-based AngelList for Europe. That's the goal. Fantastic. So hope to see you at DevCon 8.
[01:18:35] Me too. I'm looking forward to it. As of now, I don't intend any change. Stick to Ethereum. I love the community. I continue building and try to get a lot of people using it. Have you been to every DevCon?
[01:18:46] Yes. Yes, I've been to every DevCon. The last one was actually the first one I didn't give a talk. And I also went to every EthCC, except for one—that was COVID. There was a reason I couldn't come. But yes, I intend to continue to come to every DevCon. It's like you meet the people like Griff Green, Jeff Karras,
[01:19:09] of course, Vitalik, and many others. It's just a sweet spirit there. Nice community. Love seeing how it all grows. Listen to those exciting talks. I mean, for Tokenize It, it's not as relevant—it's not like our customers or the tech, of course. We're just doing an ERC-20 token on Ethereum. It's super easy. It's no deep tech. Sometimes I miss doing deep tech, but, well, I just enjoy being there, seeing what all happened, and remembering those magic days. And it's like only once in a lifetime or two times in a lifetime you have this...
[01:19:44] this moment where everything comes together, the right time, the right place, the right people. This certainly were those like one and a half years that I worked for Ethereum—definitely like the prime of my career in terms of who I worked with, what we accomplished, the impact we had on the world, and this sweet cypherpunk spirit there and what we did there. It was really great. I always sometimes get emotional thinking about this and meeting those people again at DevCon.

**SPEAKER_08:**
[01:20:15] Fantastic. Well, thank you for all your contributions to that success. Likewise. All the best. Okay. Oh, just one more. Where can we find you?

**SPEAKER_01:**
[01:20:27] You can find me usually on Twitter for the Ethereum people, CHRJens. Of course, I have a complicated name, not many vowels in there, but you find it. Or, of course, on LinkedIn—actually for my company, I'm more active on LinkedIn, which I was never before, but that's where we get our clients as Tokenize It. But usually you can find me on Twitter. Follow me there or on LinkedIn. Excellent. Okay. Thanks so much. Have a great day. Thank you. It was great talking to you. Bye.