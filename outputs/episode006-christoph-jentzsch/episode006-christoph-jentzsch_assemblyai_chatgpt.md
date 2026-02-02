Because of output-size limits, I can’t safely deliver the entire cleaned transcript in a single response while keeping the 90–110% length requirement. I’m going to deliver the corrected transcript in multiple parts, preserving **all** content and **all** original timestamps exactly. Here is **Part 1** (from **[00:03]** through **[25:01]**). Ask for **Part 2** and I’ll continue from **[25:01]** onward.

---

**[00:03] SPEAKER_00:** Okay, recording is in. Pro is in progress. It says so. Hello everybody. Today, delighted to have Christoph Jentzsch with us. We did attempt to record this, Christoph and I, two weeks ago, but I forgot to press the record button. So we spoke for an hour or so and then it was not recorded. So this is round two. Hello Christoph, how are you?

**[00:30] SPEAKER_01:** Hi everyone.

**[00:31] SPEAKER_02:** Nice to meet you again. I’m doing good. I hope you too. Thanks for the invitation.

**[00:37] SPEAKER_00:** Fantastic. Christoph and I, our paths crossed for the first time way back in 2015 when I was trying to do C Ethereum on my smartwatch. And this was around the time that Christoph was still at the Ethereum Foundation. And then I think our paths have crossed a number of times since, and Kieren’s too.

**[01:11] SPEAKER_01:** Indeed.

**[01:13] SPEAKER_00:** So, Christoph, what were you doing with your life before you found Ethereum and joined this crazy journey?

**[01:24] SPEAKER_02:** So the journey started in 2013. I was doing my PhD in theoretical physics actually, about self-organizing systems. So like biology, six months in mathematical biology and other things. So I was studying systems which have local rules and global behavior, and I came across Bitcoin, which has just a small set of local rules and a global behavior as a currency.

But the reason I came across this was I was looking for cheap GPUs, like graphic cards, and the Bitcoin miners were selling their GPU mining rigs to get some FPGAs and later ASICs. And so that’s how I got into “what’s Bitcoin mining.” And so I bought my first bitcoin, got into this bubble, did read everything I could about it, and then I came across the white paper from Vitalik, early 2014, something like January, February, in some Bitcoin forum somewhere.

And I was already totally in love with the idea of Bitcoin being a decentralized currency and all the characteristics and features of it. And this white paper of Vitalik—if you read it again, it’s almost a prophecy, except of NFTs. Everything is in there: from DAOs, from ENS, like names, domain name systems, and all of that. So for me it opened up this option of building applications with the same characteristics as Bitcoin, but just not a currency, but everything else.

And so then I started reading everything about it. And in 2014—actually still 2014—in summer, I read the crowdsale was in 2014, right? Right, yeah, the crowdsale. So around the time the crowdsale happened, I watched a video from Gavin Wood. He was somewhere in Scandinavia, some conference there, the Nordics, and he talked about Ethereum. I loved it. And he said, “We want to open up an office in Berlin, looking for C++ developers.” I was a C++ developer. So in theoretical physics it’s 90% software development. So I said, “Well, I want to do this.”

So I took my parental leave time plus some vacation time and paused my PhD for like three or six months and said I will return after I’m done. I thought this is just a short project because they raised money—maybe six, maybe 12 months, 18 months or so—then it’s over. When I started, I thought about maybe three to six months and then I go back to my PhD. So I worked there with Ethereum, with Gavin Wood. It was a great time, and then I just decided to stay. It was so exciting.

**[04:03] SPEAKER_00:** So you never got to be a doctor?

**[04:06] SPEAKER_02:** No, I’m not a doctor. I did not finish my PhD, although I only had six months left, which was kind of a pity. I worked for like three years on that. But I also had, at the time, I think four or five kids. I needed some money. I didn’t get much money as a PhD student, so I did software development as a side hustle basically.

And so when I got this project, I said, “Well, let’s do this for two or three months as parental leave time, and then I can return.” And then I decided to really interrupt my PhD. I said I will maybe return one year later because I thought the Foundation will eventually run out of money because they’re not making any profits. They just raised donations, then they will spend them, and then it’s over. Then I can continue my PhD. That was originally the plan. It just came different.

**[04:50] SPEAKER_00:** I mean, I guess it’s never too late, right.

**[04:53] SPEAKER_02:** I actually sometimes think about if I should return. It’s just so much to learn again. Right now I’m doing Tokenize.it. I’m basically working on tokenizing German companies. It works very well. So currently I’m not planning on getting back anytime soon.

**[05:08] SPEAKER_00:** No, because famously you had Dr. Gavin Wood and Dr. Christian Reitwiessner as well, and I think there were a couple of other PhDs as well.

**[05:20] SPEAKER_02:** There was definitely.

**[05:22] SPEAKER_01:** I also dropped out of mine. I was actually in mathematical physics too. Interesting, similar background.

**[05:31] SPEAKER_02:** It’s actually the same, like theoretical physics. It’s the mathematical part of physics. I enjoyed it very much. I did thermodynamics and statistics mostly. Software development was really fun.

**[05:43] SPEAKER_01:** Well, by the way, Jim is trying to join. I don’t know if there’s anything that needs happening. He gets some browser.

**[05:53] SPEAKER_00:** Yeah, yeah, well he’ll pop up and we can add him, or if he’s—then never mind. So Christoph, in terms of getting hired into ÐΞV and—sorry if I just missed it—how did that happen? Did you meet Gav at a meetup? Did you…?

**[06:13] SPEAKER_02:** Yes. I actually listened to his talk as the online thing, and I actually just wrote him an email, said, “Look, I’m a developer, would love to join Ethereum, love what you’re doing.” And he invited me to meet him in Kreuzberg, Berlin, which again is about two hours drive from here. So I went up there, met him.

I remember the first conversation: he was talking about all the stuff they were going to build and said, “Well, what can you do?” And I just asked him, “What’s the most complicated stuff you have right now? Give me a complicated task. I somehow can figure it out.” So he talked about the Ethereum Virtual Machine, which needed some testing. So I just picked working on testing the Ethereum Virtual Machine, or like writing tests for it.

Back at the time, I actually had no real idea what he was talking about. Meaning, of course I did understand on the white paper level; I didn’t understand what Ethereum was about. But Gavin had this skill of writing the Yellow Paper, which is still incredible work. It’s such a great specification, different from Bitcoin not really having a specification, so multiple clients could be built. And in there he defined the Ethereum Virtual Machine.

And I think I read the paper six, seven times. I felt like I was one out of, I don’t know, 10 or 20 people in the world at the time who really understood the Yellow Paper. I did corrections to it. I have some pull requests actually in the Yellow Paper GitHub repo, added missing definitions and stuff like that.

And then what I mostly did was writing tests according to the specification, which then were, with the help of the C client—because this was his team—I was working also on the C codebase, cpp-ethereum, also the JavaScript version, and what else do we have, like a Haskell client and others. They were basically using my tests to see if they implemented the Ethereum Virtual Machine, also the state transitions and block creation, correctly.

**[08:05] SPEAKER_00:** Yeah, yeah. So just to have some timeline for the viewers: Vitalik wrote the White Paper in November 2013. Various other people sort of joined in on the efforts in December, including Gav and Jeff who started the C and Go clients respectively at the very end—oh my goodness—at the very end of December, kind of Christmas projects for them both.

January 2014, you had the public announcement of Ethereum at the Bitcoin Miami conference. It was as early as April 2014 that Gav wrote the Yellow Paper, which is, as you were saying, the formal specification. You had the crowdsale between July and September 2014. So then yeah, you were coming in right after that. So you had a wave of arrivals in September and October of that year, essentially because the crowdsale had happened. There was some money to actually hire people.

And then talking about where you met there initially, that group: so ÐΞV were and is a company coordinating the development of Ethereum stuff. So it’s a subsidiary of the Ethereum Foundation. They were working initially in a coworking space, but then—and it was between August and November of that year that the office was getting done up and tidied. And then in November you had Devcon 0, the first conference, an internal one where a lot of the people, that was their first face-to-face meeting.

How was Devcon 0? What was that like?

**[10:20] SPEAKER_02:** It was like a company retreat. So this was not a public conference. We did have, even though there were some outsiders who felt like part of the community, maybe also pushed some code.

And I remember—his name again—wrote the book also about Ethereum. And Alexis from IBM. Yeah, I think he was also there, just as an example of some people who are reading about Ethereum, interested in joining.

**[10:47] SPEAKER_00:** Of course Roman as well, right? Roman was there with the Java client.

**[10:52] SPEAKER_02:** But it was mostly developers. But also I think Stephan Tual was already there. So we had already the London team. So it was like an internal Ethereum meeting, kind of a meetup, almost. I think three days or so. I don’t know exactly—five days even. So it was a full week. I was there for the full week as far as I can remember.

I did a presentation about testing, how the test suite is very important. Yes, we had the Remix project. Solidity project, I think, mostly started during that time. Gavin used this for explaining his vision of Ethereum as a platform for decentralized applications. So building Swarm—I don’t know if Swarm and Whisper were already launched there, but at least the generic idea—the Mist browser.

So all those ideas are really sketched out there, like the technical roadmap, what we are going to build. Because we started just, of course, with the basic clients, like implementing the protocol. But he took it like: “What are we going to do in the next 12 months?” Building the Mist browser, like Remix, all those tools, to have a platform for decentralized applications.

I remember one slide which I think I posted on Twitter a while ago, but you have those three circles: one circle is one node, and you would see like they are connecting on the blockchain, using Swarm for the data, Whisper for the messages. And this whole picture was painted there.

And the people attending, I think around 50 people plus minus 10, don’t know exact number, were mostly developers talking about code, coding there. Joseph, I remember him being there, saying, “Well, all of you, you will create your own companies becoming millionaires.” I remember Joseph was talking about that, and I think mostly he was right. So most of those people in the room, in one way or another, co-founded, founded, or were early part of companies building on top of Ethereum in the years to come.

**[12:45] SPEAKER_00:** Yeah, yeah. Let me see if I can do a little screen share. No, never mind. I can’t work out how. Not to worry.

**[12:57] SPEAKER_01:** But yeah, this present button, so not working.

**[13:02] SPEAKER_00:** Yeah, I don’t see that. Is that on the right-hand side?

**[13:04] SPEAKER_01:** Somewhere, or at the bottom. You maybe have a different—For me, I appear on the top right, and below, and to the right of me, below, there’s a present button.

**[13:13] SPEAKER_00:** Right, with like a plus post maybe. Never mind, never mind. I was just going to show the iconic photo of people at Devcon 0, you know that big group shot with nearly everyone who was out there. So that’s a classic Ethereum photo.

So I was looking—sorry—there’s like 11 of the videos still around from Devcon 0. I think there were about 20 sessions. I’m still trying to dig out the others. Some of them, including yours, I have not managed to find yet.

**[13:50] SPEAKER_02:** Yeah, it was only about the test suite, how I built it, how people would use it. It was rather technical. There was not much of a vision in there.

**[13:59] SPEAKER_00:** Well, Lefteris presented on Emacs, so you’re not the most boring talk.

**[14:06] SPEAKER_02:** Again, it was just the nerds. And for most of them, the first time we actually met. Of course the C team, they didn’t know each other because they’re working in the coworking space. Lefteris and others were there. But then let’s say, I think it was the first time I actually met Vitalik because he came there then. Of course Jeffrey and his team, Stephan’s team, Joseph Lubin.

So for me it was the first time to meet all of them and have talks. And since we really had time—five days, a small group of people—we actually did have time to eat together, to talk. So it was not so crowded maybe as Devcon is today. Very intimate. Was good.

**[14:45] SPEAKER_00:** Yeah.

**[14:46] SPEAKER_01:** I mean, one thing I can’t quite remember. So there was a time there was an Ethereum Slack that was kind of open to the public. There were a lot of people. The sort of Ethereum affiliation status was fairly vague at that point. And we were—you know—I remember we were using Skype a lot in those days, just the team, and like Vitalik liked Skype.

And then at some point I sort of lost the thread of where the core—I can’t remember where the core development discussions were happening. And I’ll maybe I’ll ask Jim to comment also. Just like those tests: we kept getting them, and I think I’m thinking of something a little bit earlier on, and we’d build them, and Jim was mostly working on them and would update on the passing percentage, which would always be between like 93 and 98, and then something would change.

But yeah, where did the discussion—because yeah, between sale and Devcon 0 I think it kind of got a little bit—like moved around where the dev discussion.

**[16:02] SPEAKER_02:** Yeah, it was mostly Skype. We also had Skype channels for almost everything, like the C team and so on.

Then in a short time they used a note taker which had a name also with “E” something. Yeah, Etherpad, something like this, right. There were some notes being written there, but the communication was really, I would say, 99% Skype for me.

Later on we used a tool based on GitHub. What was the name of it? Gitter came later. This was like the replacement for Skype. But I didn’t use it too much. This was actually during the time—and I was actually leaving—but it was used also by the C++ team. There you had a channel per GitHub repo.

This was during the time that GitHub was completely reorganized because at the beginning it was like one big repo, everything; they made submodules; it was so messy. And during this process we got Gitter. But yeah, for me it was mostly Skype.

**[17:01] SPEAKER_00:** Yeah. And then annoyingly that kind of means a lot of these early discussions are kind of a bit lost because nobody is using Skype and Skype is getting deleted. This is happening in February of next year.

**[17:15] SPEAKER_01:** Oh, I thought it happened already.

**[17:16] SPEAKER_00:** No, you can still request to download, and I did, and then I haven’t heard anything back. And I want to do that to see if I can get some of those. So everybody apply to download your Skype data.

I remember with Gitter there was a discussion about this that I was involved with at the EF later, which was saying the problem with Skype is it wasn’t discoverable. You had to request to be added, but you had to know what was there to be able to do that request. So it was a bit of a chicken-and-egg situation.

Whereas Gitter, it was like a one-to-one with the repositories. So if you’re using a repo, there you go. There’s a one-to-one channel with that. And it was discoverable and archived.

But then Slack I think was even earlier. Oh, there was the forum as well, right? There was an Ethereum forum too.

**[18:07] SPEAKER_02:** Yeah, it was important. And then Slack—I think I got introduced to Slack by Stephan Tual when he created a community for The DAO. When he looked for a new communication tool, he went with Slack. And at that time it was not like today, like a business tool for a company. It was really communities. Like we had 5,000 people in our Slack, which is not how it’s used today.

**[18:28] SPEAKER_00:** Yeah, yeah. So welcome Jim. Your technical problem.

**[18:33] SPEAKER_03:** Hi. I had some technical problems for a while there, but I don’t know, I’m just listening to you guys. What happened that brought the whole world to Zoom suddenly?

**[18:47] SPEAKER_01:** It was in waves, at least on my side.

**[18:52] SPEAKER_03:** I don’t know, I just woke up one day and everything was Zoomed.

**[18:56] SPEAKER_01:** Yeah, from then on, it’s like a statistical phase transition, you know. I think it was two phases. I would always get invited to corporate—let’s say 2017 to 2019 when I was doing primarily BD—I found that I would get invited to any of 10 video conferencing tools. And like what is the Cisco one? WebEx. That was horrible. I would get that a lot. Google Meetings didn’t feel sufficiently corporate or something, even though it was okay. And Zoom had the best quality for a while. And I found that everyone picked Zoom at the same time, like mid 2018, let’s say.

**[19:45] SPEAKER_00:** I think it was just quality to me. Like Microsoft really fumbled, right? Skype had got such a lead for so long, but Zoom just seemed more reliable, whatever weird little proprietary magic they had going on.

**[20:00] SPEAKER_02:** Yeah.

**[20:00] SPEAKER_03:** And then I guess, yeah, I guess I was under the impression that Zoom is for businesses.

**[20:07] SPEAKER_01:** Well, that is true, but still, I mean this has gotten way better in the last 10 years, but still nothing really works for reliable video over the Internet. It’s just much better than what existed.

But there was a free version always and they would just time you out. So they had a fairly viral acquisition loop where—And I was just gonna say, in the pandemic once when people were locked down, it became a consumer tool where people would have like large yoga classes, or sermons, or whatever, with like 500 people on a Zoom, and then everyone bought.

**[20:52] SPEAKER_03:** Yeah, I remember it well. All of a sudden my parents were calling me up and they’re like, “We found this awesome new tool. You probably never heard of it. It’s called Zoom.”

**[21:02] SPEAKER_01:** But yeah, there were like 10.

**[21:04] SPEAKER_00:** Let’s move on from sharing about video platforms, eh? So I look back—so Jim’s first commits on the Haskell client were mid September 2014. So, you know, a couple of months ahead of Devcon 0. You’d had the Yellow Paper for five months at that time.

And I did find on our Slack a bit of a thread where things, I think from you, Christoph, were being discussed by Jim. I don’t know, did you guys interact directly at all on testing, Jim, Christoph?

**[21:51] SPEAKER_02:** Not directly, not as far as I can remember. I mean maybe there were some messages. I mean it has been a while ago.

**[21:58] SPEAKER_03:** I could be wrong. I may have met you briefly in London when we had that conference, but it would have been like, like “hi,” you know, quick greetings at an after party or something.

**[22:14] SPEAKER_02:** I mean, 10 years ago, lots of people, sure. We were the testing GitHub repo and we had all the major clients using it, and I was interacting mostly, asking and responding questions. I mean, of course the C team I was super close to. I used the C client also to pre-fill the tests. So this was per default, right? Except we found there was a test failing but it shouldn’t, but actually C was wrong. So sometimes this happened: the test was not really failing, just C was wrong.

But in the majority of cases C was right. We were just having those conversations and we found tons of issues. Not just in the beginning—I wrote those tests using actually bytecode, the very first tests. Then I went to a low-level Lisp-like language. This was LLL. This was the precursor to Solidity by Gavin.

Then in the end actually I had automated fuzz testing where I wrote software that would create thousands of tests, and we had some AWS—like over a hundred cores of machines—constantly creating tests, and we had always some failing on some versions of Geth or other clients. So this was mostly what I did during one and a half years.

**[23:28] SPEAKER_00:** Right, right. So yeah, I guess for the viewers, something that Ethereum chose to do differently from Bitcoin was to have this specification separate from the client software, right? So, you know, when Bitcoin started it was the code that happened first and the white paper afterwards, but the white paper wasn’t a protocol specification.

So Gav was doing that Yellow Paper spec in parallel with the C client, which was sort of the first one, while you have Vitalik working on the Python client, Jeff working on Go internally. But then you’ve got all these other clients as well: the Java one by Roman, I think started in about April or May. Jim and Kieren here with a Haskell client starting in September. You had JavaScript as well.

**[24:29] SPEAKER_02:** It’s more like a library. I don’t know if it’s really like a syncing client, but they have all the tools so you can, in your web app, kind of integrate parts of it to verify certain states.

**[24:39] SPEAKER_00:** Yeah, I mean, I think maybe they had a syncing client at some point, apart from it obviously couldn’t actually keep up—but theoretical. And yeah, like a little later there was a Ruby client as well. And yeah, at one point there were eight different clients.

**[25:01] SPEAKER_02:** Right. If you want to, I can tell the story of why we all are using Geth today.

---

If you want, I can also apply **house style consistency** across later sections (e.g., consistently using “Devcon,” “ÐΞV,” “Ethereum Foundation,” “mainnet,” “testnet,” “Genesis”), but I will not change meaning or remove content.