**SPEAKER_02:**
[00:00] Okay, recording is in progress. Hello, everybody. Today, we're delighted to have Christoph with us. We did attempt to record this with Christoph and me two weeks ago, but I forgot to press the record button. So, this is round two. Hello, Christoph, how are you?

**SPEAKER_00:**
[00:05] Hi, Rob. Nice to meet you again. I'm doing good. I hope you too. Thanks for the invitation.

**SPEAKER_02:**
[00:10] Fantastic. So, Christoph and I, our paths crossed for the first time way back in 2015 when I was trying to do C++ Ethereum on my smartwatch. And this was around the time that Christoph was still at the Ethereum Foundation. Then, I think I crossed paths with you across a number of times since, and Kieran's too. Indeed. So, Christoph, what were you doing with your life before you found Ethereum and joined this crazy journey?

**SPEAKER_00:**
[00:25] So, the journey started in 2013. I was doing my PhD in theoretical physics, actually about self-organizing systems. So, like biology, six months in mathematical biology and other things. So, I was studying systems which have local rules and global behavior. And I came across Bitcoin, which is just a small set of local rules and a global behavior as a currency. But the reason I came across this was I was looking for cheap GPUs like graphic cards, and the Bitcoin miners were selling their GPU mining rigs to get some FPGAs and later ASICs. And so, that's how I got into what's Bitcoin mining, and so I bought my first Bitcoin, got into this bubble, did read everything I could about it, and then I came across the white paper from Vitalik, early 2014, something like January or February, and some Bitcoin forum somewhere. And I was already totally in love with the idea of Bitcoin being a decentralized currency and all the characteristics and features of it. And this white paper, Vitalik, if you read it again, it's almost a prophecy, except for NFTs, everything's in there, from DAOs to ENS, like names, this domain name system, and all of that. So, for me, it opened up this option of building applications with the same characteristics as Bitcoin, but just not a currency, but everything else. And so, then I started reading everything about it. And in 2014, in summer, I read that the crowd sale was in 2014, right? So, around the time the crowd sale happened, I watched a video from Gavin Wood. He was somewhere in Scandinavia, some conference there, um, the Nordics, and he talked about Ethereum. I loved it, and he said, "You want to open up an office in Berlin, looking for C++ developers." I was a C++ developer, so I said, "Well, I want to do this." So, I took my parental leave time, plus some vacation time, and passed my PhD for like three or six months, and said, "I will return after I'm done." I thought this was just a short project because they raised money, maybe six, maybe 12 months, 18 months or so, then it's over. When I started, I thought about maybe three to six months, and then I go back to my PhD. So, I worked there with Ethereum, with Gavin Wood, it was a great time, and then just decided to stay. It was so exciting.

**SPEAKER_02:**
[01:45] So, you never got to be a doctor? No, I'm not a doctor.

**SPEAKER_00:**
[01:50] I did not finish my PhD, although I only had six months left, which was kind of a pity. I worked for three years on that. But I also had, at the time, I think, four or five kids. I needed some money. I didn't get much money as a PhD student. So, I did software development as a side hustle, basically. And so, when I got this project, I said, "Well, let's do this for two or three months as a parental leave time, and then I can return." And then I decided to really interrupt my PhD. That was originally the plan, just came different. I mean, I guess it's never too late, right? I actually sometimes think about it, but I should return. It's just so much to learn again. I'm right now doing Tokenize.it. I'm basically working on tokenizing German companies. It works very well. And so, currently, I'm not planning on getting back anytime soon.

**SPEAKER_02:**
[02:30] No, because I mean, famously, you had, you know, Dr. Gavin Wood and Dr. Christian Reitweissner as well. And I think there were a couple of other PhDs as well.

**SPEAKER_01:**
[02:35] There was definitely. I also dropped out of mine. I was actually in mathematical physics too. Interesting.

**SPEAKER_00:**
[02:40] It's actually the same. Like theoretical physics, it's the mathematical part of physics. I enjoyed it very much. I did thermodynamics and statistics, mostly software development. It was really fun.

**SPEAKER_01:**
[02:50] Well, by the way, Jim is trying to join. I don't know if there's anything that needs happening. He gets some browser issues.

**SPEAKER_02:**
[02:55] Yeah, yeah, well, he'll pop up, and we can add him, or if he's... I'll say, then never mind. So, so, Christoph, in terms of, um, you know, getting hired into FDev, and I'm sorry if I just missed it, so...

**SPEAKER_00:**
[03:05] How did that happen? Did you... you meet Gav at a meetup? Did you say yes? I actually listened only to his talk; it was an online thing, and I actually just wrote him an email, said, "Look, I would love to join Ethereum, love what you're doing," and he invited me to meet him in Kreuzberg, Berlin, so, which is about two hours' drive from here. So, I went up there, met him, I remember the first conversation; he was talking about all the stuff they were going to build, and said, "Well, what can you do?" And I just asked him, "What's like the most complicated stuff you have right now? Like, give me a complicated task; I somehow can figure it out." So, he talked about the Ethereum Virtual Machine, which needed some testing. So, I just picked working on testing the Ethereum Virtual Machine, or like writing tests for it. Back at the time, I actually had no real idea what he was talking about, meaning, of course, I did understand on the white paper level; I did understand what Ethereum was about. But Gavin had this skill of writing the Yellow Paper, which is still incredible work, like it's such a great specification, different from Bitcoin, really having a specification. So, multiple clients could be built. And in there, he defined the Ethereum Virtual Machine. And I think I read the paper six, seven times; I felt like it was one out of, don't know, 10 or 20 people in the world at the time who really understood the Yellow Paper. I did corrections to it; I have some pull requests actually in the Yellow Paper GitHub repo, um, added missing definitions and stuff like that. And then, what I mostly did was writing tests according to the specification, which then were with the help of the C++ client, because this was his team. So, I was working also on the C++ code base. And so, Geth, PyEthereum, also the JavaScript version, and what else did we have? Like Haskell client, and others. I'm basically using my tests to see if they implemented the EVM, also the state transitions and block creation, correctly.

**SPEAKER_02:**
[05:00] Yeah. Yeah. So, I mean, just to have some timeline for the viewers, so, um, Vitalik wrote the white paper in November 2013. Um, various other people sort of joined in on the efforts, uh, in December, including, uh, including Gav and Jeff, who, uh, who started the C++ and Go, uh, clients, uh, respectively, at the very end of December, kind of like Christmas projects for them both. January 2014, he had sort of like the public announcement of Ethereum at the Bitcoin Miami conference. Um, it was as early as April 2014 that Gav wrote the Yellow Paper, which is, you know, the formal specification. Um, you had the crowd sale between July and September 2014. Um, so then, yeah, you were coming in right after that, you know, so you had a wave of arrivals in September and October of that year, essentially, because the crowd sale had happened, there was some money to actually hire people. Um, and then, talking about, you know, where you, where you met, there, uh, initially, that group, so FDev were, and is, a company coordinating the development of Ethereum stuff. It's a subsidiary of the Ethereum Foundation. Um, were working initially in a co-working space, but then got an offer, and it was between August and November of that year that the office was getting, like, done up and tidied, and then, in November, you had DevCon Zero, um, you know, the first conference, uh, you know, an internal one, where a lot of the people, that was their first sort of face-to-face meetings. How was DevCon Zero? How was that? What was that like?

**SPEAKER_00:**
[06:30] It was like a company retreat. So, it was not a public conference. Even though there were some outsiders who felt like part of the community, maybe also pushed some code. I remember, I was in his name again, wrote the book also about Ethereum, did Lexus, from IBM. I think Henning was also there, just as an example of some people who were like, reading about Ethereum, interested in joining. Of course, Joseph Rubin. Roman was there. But it was mostly developers. But also, I think Stefan was already there. So, they had already the London team. So, it was like an internal Ethereum meeting, kind of a meetup, almost, I think, three days or so. Five days, even. So, it was a full week. I was there for the full week, as far as I can remember. I did a presentation about testing, how the test suite is very important. Yes, we had Remix projects, Solidity project, I think, mostly started at the time. Gavin used this for explaining his vision of Ethereum as a platform for decentralized applications, so building Swarm. I don't know if Swarm and Rsk were already launched there, but at least, the generic idea, the technical roadmap, what we are going to build, and because we started just, of course, with the basic clients, like implementing the protocol, but he took it, like, kind of, what are we going to do in the next 12 months? The Mist browser, Remix, those tools, to have a platform for these and those applications. I remember one slide, which I think I posted on Twitter a while ago. You have those three circles. One circle is at one node. You would see they are connecting on the blockchain, using Swarm for the data, Whisper for the messages. This whole picture was painted there. And there are people attending, I think, around 50 people, plus, minus 10, don't know the exact number, where most of the developers talking about code, coding there. Joseph, I remember him being there, saying, "Well, all of you, you will create your own companies, becoming millionaires." I remember Joseph talking about that. And I think, mostly, he was right. So, most of those people in the room...

**SPEAKER_02:**
[08:00] In one way or another, co-founded, founded, or early part of companies building on top of Ethereum in the years to come, yeah, yeah, um, let me see if I can do a little screen share... no, no, I can't work out how... not to worry. But, yeah, there's this present button. Does that not work? Yeah, I don't see that. Is that on the right-hand side somewhere, or at the bottom?

**SPEAKER_01:**
[08:15] Maybe you have a different... For me, I appear on the top right, and below. And to the right of me, below, there's a present button with like a plus.

**SPEAKER_02:**
[08:20] Oh, never mind. Never mind. I was just going to show the iconic photo of people at DevCon Zero, right? You know, that's this big group shot with nearly everyone who was out there. You know, so that's a classic Ethereum photo. So, I was looking... sorry, there's... like 11 of the videos, they're still around from DevCon Zero, I think they're around 20 sessions. I'm still trying to dig out the others, some of them, including yours, I have not managed to find yet.

**SPEAKER_00:**
[08:40] It was only about the test suite, how it was built, how people would use it. It was rather technical. There was not much of a vision in there.

**SPEAKER_03:**
[08:45] Well, Lefteris presented on Emacs, so you're not the most boring talk.

**SPEAKER_00:**
[08:50] Again, it was just some nerds starting. Also, for most of them, it was the first time we actually met. Now, of course, the C++ team, they didn't know each other, because they're working in the co-working space. Lev Teres and others were there. But then, let's say, I think it was the first time I actually met Vitalik, because he came there. Then, of course, Jeffrey and his team, Stefan Tual and his team, Joseph Lubin. So, for me, it was the first time to meet all of them, and having talks. And since we really had time, five days, a small group of people, we actually did have time to eat together, to talk. So, it was not so crowded, maybe, as DevCon is today. Very intimate. It was good.

**SPEAKER_02:**
[09:30] Yeah, I mean, far from it.

**SPEAKER_01:**
[09:35] One thing I can't quite remember. So, there was a time there was an Ethereum Slack that was kind of open to the public. You know, there were a lot of people. The sort of Ethereum affiliation status was fairly vague at that point. And we were using Skype a lot in those days, just the team, um, like Vitalik liked to Skype, um, and then, at some point, I sort of lost the thread of, like, where the core... I can't remember where the core development discussions were happening. And I'll maybe I'll ask Jim to comment also, just like those tests. We kept, like, getting them, and I think I'm thinking of some a little bit earlier on, and we'd build them. And Jim was mostly working on them, and one update on the, like, passing percentage, which would always be between, like, 93 and 98%. And then something would change, you know. Um, but, yeah, like, where did the discussion... because, yeah, between, like, sale and DevCon Zero, I think it kind of got a little bit like moved around, where the dev discussion was.

**SPEAKER_00:**
[10:30] Yeah, it was mostly Skype. We also had Skype channels for almost everything, like the C++ team, and so on. Then, in a short time, there was a note-taker, which had a name also with E something. Etherpad? Yeah, Etherpad, something like this, right? There were some notes being written there, but the communication was really, I would say, 99% Skype for me. Later on, we used a tool, based on GitHub, what was the name of it?

**SPEAKER_02:**
[10:50] Gitter. It was called Gitter.

**SPEAKER_00:**
[10:55] Gitter came later. This was like the replacement for Skype, but I didn't use it too much. This was actually during the time when I was actually leaving. But it was done, used also by the C++ team. There, you had a channel per GitHub repo. This was during the time that GitHub was completely reorganized, because, at the beginning, it was like one big repo with everything. Then, we had those submodules. It was so messy. And then, during this process, we got Gitter. But, yeah, for me, it was mostly Skype.

**SPEAKER_02:**
[11:20] Yeah, and then, annoyingly, that kind of means a lot of these early discussions are kind of like a bit lost, because nobody is using Skype, and Skype is getting like deleted. This is happening in February of next year. Oh, I thought it happened already. So, you can still request a download, and I did, and then I haven't heard anything back. And I want to do that to see if I can get some of those. So, everybody, apply to download your Skype data. I remember, with Gitter, there was a discussion about this that I was involved with, at the EF, later, which was saying, the problem with Skype is it wasn't discoverable. You know, you had to add, you had to request to be added, but you had to know what was there to be able to do that request. So, it was a bit of a chicken and egg situation. Whereas Gitter, it was like a one-to-one with the repositories. So, if you're using a repo, there you go. There's a one-to-one channel with that. And it was discoverable, and archived. But then, Slack, I think, was even earlier. Oh, and there was the forum, as well, right? It was an Ethereum forum, too.

**SPEAKER_00:**
[12:10] Yeah, it was important. And then, Slack, I think, I got introduced to Slack by Stéphane Toual, when he created a community for the DAO. When he looked for a new communication tool, he went with Slack. And, at that time, it was not like today, like a business tool for the company. It was really communities. Like, we had 5,000 people in our Slack, which is not how it's used today.

**SPEAKER_02:**
[12:30] Yeah, yeah. So, welcome, Jim. Are your technical problems?

**SPEAKER_04:**
[12:35] Hi, sorry. I had some technical problems for a while there. I don't know. I'm just listening to you guys. What happened that brought the whole world to Zoom suddenly?

**SPEAKER_01:**
[12:40] It was in waves. On my side...

**SPEAKER_04:**
[12:45] I don't know. I just woke up one day, and everything was Zoomed from then on.

**SPEAKER_01:**
[12:50] It was like a statistical phase transition. I think it was two phases. I would always get invited to corporate, let's say, 2017 to 2019, when I was doing primarily BD. I found that I would get invited to any of 10 video conferencing tools. And, like, you know, what was the Cisco one? WebEx. That was horrible. I would get that a lot. Google meetings didn't feel sufficiently corporate, or something, even though it was okay. And Zoom had the best quality for a while. And I found that everyone picked Zoom at the same time, like mid-2018, let's say.

**SPEAKER_02:**
[13:20] I think it was just quality to me. Yeah, I mean, Microsoft really fumbled, right? Skype had got such a lead for so long, but Zoom just seemed more reliable, whatever weird little proprietary magic they had going on. Yeah, and then, I guess, yeah, I guess I was under the impression that, like, Zoom was for businesses.

**SPEAKER_01:**
[13:35] I think that's, well, that is true. But it was just that, still, I mean, this has gotten way better in the last 10 years, but still, nothing really works for reliable video over the internet. It's just much better than what existed, but there was a free version, always, and it would just, like, time you out, so, like, they had a fairly viral acquisition loop, where, like, I was just going to say, in the pandemic, uh, once, when people were locked down, it became a consumer tool, where people would have, like, large yoga classes, or, you know, sermons, or whatever, with, like, 500 people on a Zoom, and then everyone, yeah...

**SPEAKER_04:**
[14:10] I remember it well. All of a sudden, my parents were calling me up, and they were like, "We found this awesome new tool." "You've probably never heard of it." "It's called Zoom."

**SPEAKER_03:**
[14:15] But, yeah, there were, like, 10.

**SPEAKER_02:**
[14:20] Let's move on from sharing about video platforms. So, I look back. So, Jim's first commits on the Haskell client were mid-September 2014. So, you know, a couple of months ahead of DevCon 0, that you'd had the Yellow Paper for five months at that time. And I did find, on our Slack, um, you know, a bit of a thread, where, where things, I think, from you, Christoph, were being discussed by Jim. I don't know, did you guys interact directly at all, on, on testing, Jim, Christoph? Not directly, not as far as I can remember. I mean, maybe there was some messages, I mean, it's about, it has been a while ago.

**SPEAKER_04:**
[14:50] I could be wrong. I may have met you briefly in London, when we had that conference. But it would have been like quick greetings at an after-party or something.

**SPEAKER_00:**
[14:55] I mean, 10 years ago, lots of people, sure. We were testing GitHub repo, and we had all the major clients using it. And I was interacting, mostly asking, responding questions. I mean, of course, the C++ team, I was super close to. I used the C++ team also to pre-fill the tests. So, this was... per default, right, except we found there was a test failing, but actually, C++ was wrong. So, sometimes this happened. The test was not really failing, just C++ was wrong. But in the maturity of cases, C++ was right. So, we were just having those conversations, and we found tons of issues. We did, not just in the beginning, I wrote those tests using actually bytecode, the very first test. Then I went to a low-level Lisp-like language. This was LLL. This was the... precursor to Solidity, by Gavin. And then, in the end, actually, I had automated fast testing, where I wrote software that would create thousands of tests. We had some AWS, like, over 100 cores of machines, constantly creating tests. We had always some failing on some versions of Geth or other clients. So, this was mostly what I did during one and a half years.

**SPEAKER_02:**
[16:00] Right, right. So, yeah, I mean, I guess, for the viewers, something that Ethereum chose to do differently from Bitcoin was to have this specification separate from the client software, right? So, you know, when Bitcoin started, uh, it was the code that happened first, and the white paper afterwards, but the white paper wasn't a protocol specification. So, um, you know, Gav was doing that Yellow Paper spec in parallel with the C++ client, which was sort of the first one, while you have Vitalik working on the Python client, Jeff working on the Go, internally, but then you've got all these other clients as well, right? So, the Java one by Roman, I think, started in about April or May. You know, ourselves, Jim, and Kieran, here, with... with a Haskell client, starting in September. You had JavaScript as well.

**SPEAKER_00:**
[16:40] Right. It's more like a library. I don't know if it's really like a syncing client, but they have all the tools, so you can, in your web app, kind of integrate parts of it, to verify certain states.

**SPEAKER_03:**
[16:45] Yeah, I mean, I think, maybe, they had a syncing client at some point, apart from it, obviously, couldn't actually keep up, but theoretical.

**SPEAKER_02:**
[16:50] And... and, yeah, like a little later, there was a Ruby client, as well. And, yeah, at one point, there were eight different clients.

**SPEAKER_00:**
[16:55] Right. If you want to, I can tell the story of why we all are using Geth today. Yeah, please do. Because this is absolutely not a given. At the time, of course, everyone had different opinions. But the C++ client was really the fastest, the most solid one, passing all the tests, and so on. But Gavin always wanted to add new features. We went to a refactoring, and he was a perfectionist, which is not bad for this kind of software. And then, the time came for the security audit, because everybody wants to launch Ethereum now, and he said, "Before we launch it, those clients need to have a proper security audit by an external company." And one of the companies doing this was Deja Vu, in Seattle. So, I actually went there with a team for the audit, and because Gavin wanted to build some more features, that, well, let's just guess, can go first, let's first order the Gold client, when they are done, I'm done with the features I want to build, and then we're going into the audit for the C++ client. So, Geth was audited. They had some issues. They fixed the issues. And now it's fine. And so, there was technically no reason why not. Well, actually, we could launch Ethereum now. We have a fully audited client. Testnet is running for a while. No major issues. No failing tests for a long time. So, why would we wait for the C++ client to be audited? I mean, they all really had the pressure of money running out. We need to launch now. And then, a decision was made. Let's launch this Geth. Uh, they can still use C++. It's just not audited. Let's say, in two months or so, the audit is done, and then they can use C++ even more, if they want. So, but then, the big mistake was, in my view, when they made this announcement, "You can start now," they recommended using Geth, because this was the audited one. So, almost everybody, um, one Geth. This was like, we started with almost 100% Geth, and then there was just a minor other clients using it. Only very few did use them. And so, after the audit was done, nobody switched. We're like, "Sure, but Geth is running. I'm synced. What's the issue? Why should I switch?" And so, we had this 19, 10, or 18, 20 distribution. It just stayed like this. So, if Gavin would have been... either say, "Let's just do the audit now, and we just have both audited, and then start." Maybe we'd have 50-50. Or even the other way around, if they would have first audited the C++ and Ethereum would have been launched without a Geth audit, they would have received a total switch. And then, of course, money was going low in the foundation. They had to reduce the team. And because Geth was the most used one, there were some issues with Gavin. Another story, maybe have a talk with him. And so, in the end, Ming decided to basically kick out the complete C++ team. This was then shortly before DevCon 1. So, something like November, October-ish. But, yeah, I think the reason for that was also C++ wasn't really that used. Also, there are other reasons as well. But you can see how a tiny thing can have such big consequences down the road, like him doing Polkadot today, and all of that. And he was great. I mean, I really, I still think, I think, maybe we would have had a mistake in sharding way earlier if Gavin would have stayed. So, without him, they moved slower. And, of course, the price went up. There were no security-relevant things. So, changes happened not quickly anymore, but take more time, and so on. But I think this was a big loss for Ethereum, that Gavin left, basically, in 2015.

**SPEAKER_01:**
[20:00] Yeah, it's amazing, the client-side was the cause. I think it was part of it, but it, uh, you know, having, um, the process, maybe started, uh, with the Red Wedding, which we just, uh, in some other early days of Ethereum episodes, like, he, um...

**SPEAKER_00:**
[20:10] Yes, there were more issues than that, definitely. Like, this was not the deciding part, but it was like those things were adding up. I remember that Gavin had this idea of turning the foundation into a DAO, and then having a for-profit entity next to it, which would build things and make money. So, there were many different commercial ideas at the time. So, he then basically started on his own, ETH Core. I remember he wanted to have me as part of it, but I decided to do Slockit at the time. So, that's why I didn't become a co-founder of ETH Core. Another story, we can go into this if you want. You know what happened after that. But there are many reasons we are part of it. I think also, him and Ming didn't really get along too much. There was not really a trust relationship going on. Of course, money running out, different visions of how Ethereum should evolve, technically and economically, if you want. All played a role, but I think it was just one part that the C++ client wasn't that much used, and the reason for that was Geth being audited, and launching without an audit for the C++ client. Yeah, um, I mean, talking about features, so, yeah, there's a ton of stuff on that on that C++ team. Aleph, Aleph zero, as well. And Aleph one. So, Aleph one being the GUI...

**SPEAKER_00:**
[21:10] ...miner, um, and then, I know, how would you describe Aleph zero, kind of the first interface to the blockchain, in some way, like the first graphical interface to a blockchain client? And what could it do? Of course, it could mine. You could deploy a smart contract. You could visit, make it visible, somewhat, what's happening there. It was not really end-user-friendly, in any way, but it was just a replacement of what people just do on the command line. Usually, command line, when your client has some input, has some output. And it was the first kind of graphical user interface, graphical user interface, replacing the command line.

**SPEAKER_02:**
[21:40] I guess it's sort of like a combination of, like, what you have with the block explorer now, apart from it, that's like a view-only, and this was both a view and a, and a do, um, yeah. But, yeah, those GUI clients.

**SPEAKER_00:**
[21:50] But much more influential than the Mist browser. The Mist browser, I think, there's a video by Alex van der Sander. It's like a 10-minute video on YouTube. They had this prototype. They're not working yet, but just take it until you make it. The vision of the Mist browser. And this also really made us understand how Ethereum could work for the end-user. Having different identities connected to wallets, and you would load those steps. Is it an IPFS hash, or... even over Swarm, one day, the app was loading, and you could do some finance stuff there. This gave us an idea of what Ethereum could be. It was so, you have to think, Vitalik gave us a rather technical vision, and, uh, intellectual thing, but Gavin gave us his pros, internet vision. Alexander gave us this very concrete thing, what an end-user could do with that, in the next six to 12 months, maybe. It's very important.

**SPEAKER_02:**
[22:40] Yeah, I mean, it's a very, very expensive vision. And, yeah, it was, you know, Gav, as you say, you know, Web3 was him. Prior to that, the language I saw was really about Bitcoin with smart contracts. You know, that was really sort of the genesis of the talent going through, uh, that journey of colored coins, and Master Coins, and meta-protocols, um, and that kind of positioning of Bitcoin as a calculator, and Ethereum's a smartphone. But it was all that kind of, like, blockchains and applications, right? It wasn't that full Web3 vision, which I think... And that really came from Gavin.

**SPEAKER_00:**
[23:10] We have to attribute this to him. He was having this big vision. This attracted also so many people. It attracted also even the business people. They could now understand what it actually is. Other than this was just like tech. Let's see. But this is like a broad vision of how business function, how, like, this new financial world would happen. They could understand this far better. Then, having this iPhone calculator comparison, this was maybe a nice technical thing.

**SPEAKER_02:**
[23:40] Yeah. Yeah. But then, for it being a very expensive vision, that's, that's a lot of work. Sure.

**SPEAKER_00:**
[23:45] But I just thought, somewhere...

**SPEAKER_02:**
[23:50] That's it. So, I mean, you know, talking about Gavin, the features. So, yeah, there's a ton of stuff on that on that C++ team. Aleph, Aleph zero, as well. And Aleph one. So, Aleph one being the GUI...

**SPEAKER_00:**
[24:00] ...miner, um, and then, I know, how would you describe Aleph zero, kind of the first interface to the blockchain, in some way, like the first graphical interface to a blockchain client? And what could it do? Of course, it could mine. You could deploy a smart contract. You could visit, make it visible, somewhat, what's happening there. It was not really end-user-friendly, in any way, but it was just a replacement of what people just do on the command line. Usually, command line, when your client has some input, has some output. And it was the first kind of graphical user interface, graphical user interface, replacing the command line.

**SPEAKER_02:**
[24:30] I guess it's sort of like a combination of, like, what you have with the block explorer now, apart from it, that's like a view-only, and this was both a view and a, and a do, um, yeah. But, yeah, those GUI clients.

**SPEAKER_00:**
[24:40] But much more influential than the Mist browser. The Mist browser, I think, there's a video