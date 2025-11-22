**SPEAKER_00:**
[00:00] Okay, recording is in.
[00:02] Pro is in progress.
[00:05] It says so.
[00:07] Hello everybody.
[00:09] Today.
[00:10] Delighted to have Christoph Jens with us.
[00:14] We did attempt to record this, Christoph and I, two weeks ago, but I forgot to press the record button.
[00:19] So we spoke for an hour or so and then it was not recorded.
[00:23] So this is round two.
[00:25] Hello Christoph, how are you?

**SPEAKER_01:**
[00:28] Hi everyone.
[00:29] Nice to meet you again.
[00:31] I'm doing good.
[00:33] I hope you too.
[00:35] Thanks for the invitation.

**SPEAKER_00:**
[00:37] Fantastic.
[00:39] Christoph and I, our paths crossed for the first time way back in 2015 when I was trying to do C Ethereum on my smartwatch.
[00:44] And this was around the time that Christoph was still at the Ethereum Foundation.
[00:48] And then I think our paths have crossed a number of times since, and Kieran's too.

**SPEAKER_02:**
[00:52] Indeed.

**SPEAKER_00:**
[00:54] So, Christoph, what were you doing with your life before you found Ethereum and joined this crazy journey?

**SPEAKER_01:**
[00:59] So, the journey started in 2013.
[01:01] I was doing my PhD in theoretical physics, actually about self-organizing systems—like biology, six months in mathematical biology and other things.
[01:08] So I was studying systems which have local rules and global behavior, and I came across Bitcoin, which has just a small set of local rules and a global behavior as a currency.
[01:16] The reason I came across this was I was looking for cheap GPUs, like graphic cards, and the Bitcoin miners were selling their GPU mining rigs to get some FPGAs and later ASICs.
[01:24] And so that's how I got into Bitcoin mining.
[01:26] So I bought my first bitcoin, got into this bubble, read everything I could about it, and then came across the white paper from Vitalik, early 2014, maybe January or February, in some Bitcoin forum somewhere.
[01:35] I was already totally in love with the idea of Bitcoin being a decent currency and all the characteristics and features of it.
[01:41] And this white paper of Vitalik—and if you read it again, it's almost a prophecy, except for NFTs—everything is in there: DAOs, ENS, domain name systems, all of it.
[01:49] For me, it opened up this option of building applications with the same characteristics as Bitcoin, but not just as a currency—everything else.
[01:57] So then I started reading everything about it.
[02:00] And actually, still in 2014, in summer, I remember the crowdsale was in 2014.
[02:05] Right, yeah, the crowdsale.
[02:07] So around the time the crowdsale happened, I watched a video from Gavin Wood—he was somewhere in Scandinavia, at some conference there, the Nordics, talking about Ethereum.
[02:17] I loved it.
[02:18] And he said, "I want to open up an office in Berlin looking for C++ developers."
[02:22] I was a C++ developer, so in theoretical physics it's 90% software development.
[02:27] So I said, "Well, I want to do this."
[02:29] So I took my parental leave plus some vacation time and paused my PhD for like three or six months and said, "I will return after I'm done."
[02:36] I thought this was just a short project because they raised money, maybe six, maybe 12, 18 months or so, then it's over.
[02:41] When I started, I thought maybe three to six months and then I'd go back to my PhD.
[02:45] So I worked there with Ethereum—Gavin Wood was great—and then just decided to stay.
[02:49] It was so exciting.

**SPEAKER_00:**
[02:51] So you never got to be a doctor?

**SPEAKER_01:**
[02:54] No, I'm not a doctor.
[02:56] I did not finish my PhD, although I only had six months left, which was kind of a pity.
[02:59] I worked for three years on that, but I also had, at the time, I think, four or five kids.
[03:04] I needed some money.
[03:05] I didn't get much money as a PhD student, so I did software development as a side hustle, basically.
[03:10] And so, when I got this project, I said, "Well, let's do this for two or three months as parental leave time and then I can return."
[03:16] And then I decided to really interrupt my PhD, thinking I would maybe return one year later, because I thought the foundation would eventually run out of money because they're not making any profits, they just raised donations, then they'd spend them and then it's over.
[03:26] Then I could continue my PhD.
[03:28] That was originally the plan; just came different.

**SPEAKER_00:**
[03:31] I mean, I guess it's never too late, right?

**SPEAKER_01:**
[03:33] I actually sometimes think about if I should return.
[03:36] It's just so much to learn again.
[03:38] I'm right now doing tokenize it.
[03:40] I'm basically working on tokenizing German companies.
[03:43] It works, works very well.
[03:45] So currently, I'm not planning on getting back anytime soon.

**SPEAKER_00:**
[03:48] No, because I mean, famously, you had Dr. Gavin Wood and Dr. Christian Reitwiessner as well, and I think there were a couple of other PhDs as well.

**SPEAKER_01:**
[03:55] There was definitely.

**SPEAKER_02:**
[03:56] I also dropped out of mine.
[03:58] I was actually in mathematical physics, too.
[03:59] Interesting similar background.

**SPEAKER_01:**
[04:02] It's actually the same as theoretical physics.
[04:05] It's the mathematical part of physics.
[04:07] I enjoyed it very much.
[04:09] I did thermodynamics and statistics mostly.
[04:12] Software development was really fun.

**SPEAKER_02:**
[04:14] Well, by the way, Jim is trying to join.
[04:16] I don't know if there's anything that needs happening—he gets some browser.

**SPEAKER_00:**
[04:19] Yeah, yeah, well, he'll pop up and we can add him, or if he's—
[04:22] Then never mind.
[04:23] So Christoph, in terms of getting hired into FDEV—and I'm sorry if I just missed it.
[04:27] So how did that happen?
[04:29] Did you meet Gav at a meetup?
[04:31] Did you say?

**SPEAKER_01:**
[04:33] Yes, I actually, I listened only to his talk, an online thing, and I actually just wrote him an email, said, "Look, I see this last developer—would love to join Ethereum, love what you're doing."
[04:41] And he invited me to meet him in Kreuzberg, Berlin, which is about a two-hour drive from here.
[04:46] So I went up there, met him.
[04:48] I remember the first conversation—he was talking about all the stuff they were going to build and said, "Well, what can you do?"
[04:53] And I just asked him, "What's the most complicated stuff you have right now? Give me a complicated task; I can figure it out."
[04:59] So he talked about the Ethereum Virtual Machine, which needed some testing.
[05:03] So I just picked working on testing the Ethereum Virtual Machine or writing tests for it.
[05:07] Back at the time, I actually had no real idea what he was talking about; meaning, of course, I did understand on the white paper level—I understood what Ethereum was about—but Gavin had this skill of writing the yellow paper, which is still an incredible work.
[05:18] It's such a great specification, different from Bitcoin—really having a specification so multiple clients could be built.
[05:24] And in there, he defined the Ethereum Virtual Machine.
[05:27] I think I read the paper six, seven times.
[05:30] I felt like I was one out of, I don't know, 10 or 20 people in the world at the time who really understood the yellow paper.
[05:35] I did corrections to it.
[05:36] I have some pull requests actually in the yellow paper GitHub repo—added missing definitions and stuff like that.
[05:41] And then what I mostly did was write tests according to the specification, which, with the help of the C++ client—because this was his team, I was working also on the C++ codebase, and so Geth, PyEthereum, also the JavaScript version, and what else did we have, like five, Haskell client and others—they were basically using my tests to see if they implemented the Ethereum Virtual Machine and the state transitions and block creation correctly.

**SPEAKER_00:**
[06:03] Yeah, yeah.
[06:04] So I mean, just to have some timeline for the viewers.
[06:07] So Vitalik wrote the white paper in November 2013.
[06:11] Various other people sort of joined in on the efforts in December, including Gav and Jeff, who started the C++ and Go clients respectively at the very end—
[06:17] Oh my goodness—at the very end of December, kind of Christmas projects for them both.
[06:21] January 2014, you had sort of the public announcement of Ethereum at the Bitcoin Miami conference.
[06:27] It was as early as April 2014 that Gav wrote the yellow paper, which is, as you were saying, the formal specification.
[06:34] You had the crowd sale between July and September 2014.
[06:38] So then, yeah, you were coming in right after that, you know, so you had a wave of arrivals in September and October of that year, essentially because the crowd sale had happened.
[06:46] There was some money to actually hire people.
[06:48] And then talking about where you met there—initially that group.
[06:53] So FDEV were, and is, a company coordinating the development of Ethereum stuff.
[06:57] So it's a subsidiary of the Ethereum Foundation.
[07:00] They were working initially in a co-working space but then—
[07:02] And it was between August and November of that year that the office was getting done up and tidied.
[07:07] And then in November you had DEVCON 0, you know, the first conference, you know, an internal one where a lot of the people—that was their first sort of face-to-face meeting.
[07:16] How was DEVCON 0?
[07:18] What was that like?

**SPEAKER_01:**
[07:20] It was like a company retreat.
[07:22] So this was not a public conference.
[07:24] We did have—even though there were some outsiders who felt like part of the community, maybe also pushed some code.
[07:29] And I remember the—what was his name again, wrote the book also about Ethereum—did Alexis from IBM.
[07:35] Yeah, I think he was also there, just as an example of some people who were reading about Ethereum, interested in joining.

**SPEAKER_00:**
[07:41] Of course Roman as well, right?
[07:43] Roman was there with the Java client.

**SPEAKER_01:**
[07:45] But it was mostly developers.
[07:47] But also I think Stefan Tual was already there.
[07:50] So we had already the London team.
[07:52] So it was like an internal Ethereum meeting—kind of a meetup, almost.
[07:57] I think three days or so, don't know exactly, five days even.
[08:00] So it was a full week.
[08:02] I was there for the full week as far as I can remember.
[08:05] I did a presentation about testing, how the test suite is very important.
[08:09] Yes, we had the remix project.
[08:11] Solidity project I think mostly started during the time—Gavin used this for explaining his vision of what Ethereum as a platform for decentralized application.
[08:19] So building Swarm.
[08:21] I don't know if Swarm and Whisper was already launched there, but at least the generic idea, the Mist browser.
[08:26] So all those ideas were really sketched out there—like the technical roadmap, what we are going to build, because we started just, of course, with the basic clients implementing the protocol.
[08:35] But he took it, like, "What are we going to do in the next 12 months?" Building the Mist browser, Remix, those tools to have a platform for decentralized applications.
[08:43] I remember one slide, which I think I posted on Twitter a while ago—
[08:46] You have those three circles: one circle is one node, and you would see, like, they are connecting on the blockchain, using Swarm for the data, Whisper for the messages, and you—like, this whole picture was painted there.
[08:56] And the people attending, I think around 50 people plus-minus 10, don't know the exact number, were mostly developers talking about code and coding there.
[09:06] Joseph, I remember him being there saying, "Well, all of you, you will create your own companies becoming millionaires."
[09:12] I remember CH was talking about that, and I think, mostly, he was right.
[09:16] So most of those people in the room in one way or another co-founded, founded, or were early part of companies building on top of Ethereum in the years to come.

**SPEAKER_00:**
[09:24] Yeah, yeah.
[09:25] Let me see if I can do a little, a little screen share.
[09:28] No, never mind.
[09:29] I can't work out how—not, not to worry.

**SPEAKER_02:**
[09:33] But, but yeah, there's this present button.
[09:36] So, not working.

**SPEAKER_00:**
[09:39] Yeah, I don't see that.
[09:41] Is that on the right-hand side?

**SPEAKER_02:**
[09:43] Somewhere or at the bottom—you maybe have a different—
[09:45] For me, I appear on the top right and below, and to the right of me below there's a present button.

**SPEAKER_00:**
[09:50] Right.
[09:51] With like a plus, post, maybe—never mind, never mind.
[09:54] I was just going to show the iconic photo of people at DEVCON 0, right?
[09:57] You know, that's this big group shot with nearly everyone who was out there.
[10:01] You know, so that's a classic Ethereum photo.
[10:04] So I was looking—sorry, there's like 11 of the videos are still around from DEVCON 0.
[10:10] I think there were about 20 sessions.
[10:13] I'm still trying to dig out the others.
[10:15] Some of them, including yours, I have not managed to find yet.

**SPEAKER_01:**
[10:18] Yeah, it was only about the test suite, how I built it, how people would use it.
[10:22] It was rather technical.
[10:24] There was not much of a vision in there.

**SPEAKER_00:**
[10:27] Well, Lefteris presented on Emacs, so you're not the most boring talk.

**SPEAKER_01:**
[10:31] Again, it was just the nerds starting—also for most of them, the first time we actually met.
[10:36] Of course, the C++ team, they didn't know each other because they're working in the co-working space, Lefteris and others were there.
[10:42] But then, let's say, I think it was the first time I actually met Vitalik because he came there then, of course Jeffrey and his team, Stefan's team, Joseph Lubin.
[10:53] So it was, for me, the first time to meet all of them and having talks.
[10:58] And since we really had time—five days, a small group of people—we actually did have time to eat together, to talk.
[11:06] So it was not so crowded maybe as DEVCON is today.
[11:09] Very intimate.
[11:11] Was good.

**SPEAKER_00:**
[11:13] Yeah.

**SPEAKER_02:**
[11:15] I mean, one thing I can't quite remember.
[11:17] So there was a time there was an Ethereum Slack that was kind of open to the public.
[11:21] There were a lot of people.
[11:23] The sort of Ethereum affiliation status was fairly vague at that point.
[11:27] And we were, you know—I, I remember we were using Skype a lot in those days.
[11:30] Just, just the team and like Vitalik liked to Skype.
[11:32] And then at some point I sort of lost the thread of, like, where the core—like, I can't remember where the core development discussions were happening.
[11:37] And I'll maybe—I'll ask Jim to comment also.
[11:40] Just, like, those tests—we kept, like, getting them, and I think—I'm thinking of some a little bit earlier on—and we'd build them, and Jim was mostly working on them and would update on the, like, passing percentage, which would always be between like 93 and 98, and then something would change, you know.
[11:55] But yet, like, where did the discussion—
[11:58] Because, yeah, between, like, sale and DEVCON 0 I think it kind of got a little bit—it like moved around, where the dev discussion—

**SPEAKER_01:**
[12:07] Yeah, it was mostly Skype.
[12:09] We also had Skype channels for almost everything, like the C++ team and so on.
[12:13] Then I, in a short time, they used a—it was a note taker which had a name, also with E something.
[12:18] Yeah.
[12:19] EtherPad, something like this.
[12:21] Right.
[12:22] There were some notes being written there, but the communication was really, I would say, 99% Skype for me.
[12:28] Later on, we used a tool based on GitHub.

**SPEAKER_00:**
[12:31] What was the name of—was it called Gitter?

**SPEAKER_01:**
[12:34] Gitter came later.
[12:36] This was like the replacement for Skype.
[12:38] But I didn't use it too much.
[12:39] This was actually during the time when I was leaving, but it was indeed used also by C++.
[12:46] There you had a channel per GitHub repo.
[12:48] This was during the time that GitHub was completely reorganized because at the beginning it was like one big repo with everything, then they made submodules—was so messy.
[12:55] And during this process, we got Gitter.
[12:58] But, yeah, for me, it was mostly Skype.

**SPEAKER_00:**
[13:00] Yeah.
[13:01] And, and then, annoyingly, that kind of means a lot of these early discussions are kind of like a bit lost because nobody is—is using Skype.
[13:09] And Skype is getting, like, deleted.
[13:12] This is happening in February of next year.

**SPEAKER_02:**
[13:15] Oh, I thought it happened already.

**SPEAKER_00:**
[13:17] It's—no, you can still request to download.
[13:20] And I did, and then I haven't heard anything back and want to do that to see if I can get some of those.
[13:25] So everybody apply to download your, your Skype data.
[13:29] I remember with Gitter there was a discussion about this that I was involved with at the EF later, which was saying the problem with Skype is it wasn't discoverable.
[13:37] You know, you had to add—you had to request to be added, but you had to know what was there to be able to do that request.
[13:43] So it was a bit of a chicken and egg situation.
[13:46] Whereas Gitter, it was like a one-to-one with the repositories.
[13:50] So if you're using a repo—there you go—there's a one-to-one channel with that.
[13:54] And it was discoverable and archived.
[13:56] But then Slack, I think, was even earlier.
[13:59] So...
[14:00] Oh, there was the forum as well, right?
[14:02] There was an Ethereum forum, too.

**SPEAKER_01:**
[14:04] Yeah, it was important.
[14:06] And then Slack.
[14:07] I think I got introduced to Slack by Stefan Tual when he created a community for The DAO.
[14:12] When he looked for a new communication tool, he went with Slack.
[14:16] And at that time, it was not like today, like a business tool for the company.
[14:20] It was really communities.
[14:22] Like, we had 5,000 people in our Slack, which is not how it's used today.

**SPEAKER_00:**
[14:25] Yeah, yeah.
[14:26] So, welcome Jim.
[14:28] Your technical problem—

**SPEAKER_03:**
[14:29] Hi.

**SPEAKER_01:**
[14:31] Sorry.

**SPEAKER_03:**
[14:33] I had some technical problems for a while there, but I don't know, I'm just listening to you guys.
[14:36] What happened that brought the whole world to Zoom suddenly?

**SPEAKER_02:**
[14:41] It was in waves, look for—on my side—

**SPEAKER_03:**
[14:44] I don't know, I just woke up one day and everything was Zoomed.

**SPEAKER_02:**
[14:47] Yeah, from then on, species like a statistical phase transition, you know?
[14:51] I think it was—it was two phases.
[14:53] I would always get invited to corporate—like, let's say, 2017 to 2019, when I was doing primarily BD, I found that I would get invited to any of 10 video conferencing tools.
[15:03] And, like, what is the Cisco one—Webex.
[15:05] That was horrible.
[15:06] I would get that a lot.
[15:08] Google Meetings didn't feel sufficiently corporate or something, even though it was okay.
[15:13] And Zoom had the best quality for a while.
[15:15] And I found that everyone picked Zoom at the same time—like mid-2018, let's say.

**SPEAKER_00:**
[15:19] I think it was just quality to me.
[15:22] Like, I mean, Microsoft really fumbled, right?
[15:25] Skype had got such a lead for so long.
[15:28] But Zoom just seemed more reliable.
[15:30] Whatever weird little proprietary magic they had going on.

**SPEAKER_01:**
[15:33] Yeah.

**SPEAKER_03:**
[15:34] And then, I guess, yeah, I guess I was under the impression that Zoom is for businesses.

**SPEAKER_02:**
[15:38] I think that's—well, that is true, but it was just that still, I mean, this has gotten way better in the last 10 years, but still nothing really works for reliable video over the Internet.
[15:47] It's just much better than what existed.
[15:51] But there was a free version always, and they would just, like, time you out.
[15:54] So, like, they had a fairly viral acquisition loop where, like—
[15:58] And I was just gonna say, in the pandemic once, when people were locked down, it became a consumer tool where people would have, like, large yoga classes or, you know, sermons or whatever with like 500 people on a Zoom and then everyone bought.

**SPEAKER_03:**
[16:09] Yeah, I remember it well.
[16:10] All of a sudden, like, my parents were calling me up and they're like, "We found this awesome new tool—you probably never heard of it, it's called Zoom."

**SPEAKER_02:**
[16:15] But yeah, there were like 10.

**SPEAKER_00:**
[16:17] Let's move on from sharing about video platforms, eh?
[16:20] So, so I look back—so, so Jim's first commits on the Haskell client were mid-September 2014.
[16:26] So, you know, a couple of months ahead of, ahead of DEVCON 0, that you'd had the yellow paper for—for, for—for five months at that time.
[16:34] And I, I did find on our Slack, you know, a bit of a thread where, where things I think from you, Christoph, were, were being discussed by Jim.
[16:42] I don't know.
[16:43] Did you guys interact directly at all on testing, Jim? Christoph?

**SPEAKER_01:**
[16:47] Not directly, not as far as I can remember.
[16:50] I mean maybe there were some messages.
[16:52] I mean, it's about—it has been a while ago.

**SPEAKER_03:**
[16:55] I could be wrong.
[16:56] I may have met you briefly in London when we had that conference, but it would have been like, hi, you know, quick, quick greetings at a part, you know, an after party or something.

**SPEAKER_01:**
[17:05] I mean, 10 years ago, lots of people, sure.
[17:08] We were the testing GitHub repo, and we had all the major clients using it, and I was interacting mostly, asking, responding to questions.
[17:14] I mean, of course, the C++ team I was super close to, I used the C++ client also to pre-fill the tests, so this was per default, except we found there was a test failing—but it should—but actually C++ was wrong.
[17:25] So sometimes this happened—the test was not really failing, just C++ was wrong.
[17:29] But in the majority of cases C++ was right.
[17:32] We were just having those conversations and we found tons of issues.
[17:36] Not just in the beginning—I wrote those tests using actually bytecode, the very first tests.
[17:41] Then I went to a low-level Lisp-like language, this was LLL, this was the precursor to Solidity by Gavin.
[17:47] Then in the end, actually, I had automated fast testing where I wrote software that would create thousands of tests, and we had some AWS, like over a hundred cores of machines constantly creating tests, and we had always some failing on some versions of Geth or other clients.
[18:00] So this was mostly what I did during one and a half years.

**SPEAKER_00:**
[18:03] Right, right.
[18:05] So, yeah, I mean, I guess for the—for the viewers, something that Ethereum chose to do differently from Bitcoin was to have this specification separate from the client software.
[18:16] Right.
[18:17] So, you know, when Bitcoin started, it was the code that happened first and the white paper afterwards, but the white paper wasn't a protocol specification.
[18:26] So, you know, Gav was doing that yellow paper spec in parallel with the C++ client, which was sort of the first one, while you have Vitalik working on the Python client, Jeff working on the Go internally.
[18:37] But then you've got all these other clients as well—the Java one by Roman I think started in about April or May, ourselves—Jim and Kieran here with a Haskell client starting in September.
[18:47] You had JavaScript as well.

**SPEAKER_01:**
[18:49] It's more like a library.
[18:51] I don't know if it's really like a syncing client, but they have all the tools so you can, in your web app, kind of integrate parts of it to verify certain states.

**SPEAKER_00:**
[18:58] Yeah, I mean, I think maybe they had a syncing client at some point, apart from it obviously couldn't actually keep up—but in theory.
[19:04] And, yeah, like a little later, there was a Ruby client as well.
[19:08] And yeah, at one point there were eight different clients.

**SPEAKER_01:**
[19:10] Right.
[19:11] If you want to, I can tell the story of why we all are using Geth today.
[19:13] Yeah, absolutely.
[19:14] Not a given.
[19:15] At the time, of course, everyone had different opinions, but the C++ client was really the fastest, the most solid one, passing all the tests, and so on.
[19:23] But Gavin always wanted to add new features, do a refactoring, and he was a perfectionist, which is not bad for this kind of software.
[19:29] And then the time came for the security audit, because everybody wants to launch Ethereum now.
[19:34] And we said before we launch it, those clients need to have a proper security audit by an external company.
[19:39] And one of the companies doing this was Deja Vu in Seattle.
[19:43] So I actually went, revisited the team for the audit, and because Gavin wanted to build some more features, said, "Well, let's let Geth go first.
[19:51] Let's first audit the Go client.
[19:53] They are done.
[19:54] I'm done with the features I want to build.
[19:56] And then we're going into the audit for the C++ client."
[19:59] So Geth was audited, picked.
[20:01] They had some issues, they fixed the issues, and now it's time.
[20:04] And so there was technically no reason why not—well, actually, we could launch Ethereum now and have a fully audited client.
[20:10] Testnet is running for a while, no major issues, no failing tests for a long time—so why would we wait for the C++ client to be audited?
[20:17] And I mean, everyone really had the pressure of money running out: we need to launch now.
[20:21] So, and then the decision was made, let's launch with Geth.
[20:25] They can still use C++, it's just not audited, let's say in two months or so the audit is done and then they can use C++ even more if they want.
[20:31] So, but then the big mistake was, in my view, when they made this announcement of, "You can start now," they recommended using Geth because it was the audited one.
[20:39] So almost everybody ran Geth.
[20:42] This was like—we started with almost 100% Geth and then all the minor other clients used it, only very few did use them.
[20:49] And so after the audit was done, nobody switched, like, "Sure, but Geth is running, I'm synced, like, what's the issue, why should I switch?"
[20:56] And so we had this 90/10 or 80/20 distribution—it just stayed like this.
[21:01] So if Gavin would have either said, "Let's just do the audit now and wait, if both are audited then step," maybe we would have had 50/50, or even the other way around—if they would have first audited the C++ client and Ethereum would have been launched without a Geth audit, like, we would have seen a total switch.
[21:14] And then, of course, money was going low in the foundation, they had to reduce the team.
[21:18] And because Geth was the most used one, there were some issues with Gavin—another story, maybe you have a talk with him—and so in the end Ming decided to basically kick out the complete C++ team.
[21:29] This was then shortly before DEVCON 1, so something like November/October-ish.
[21:35] So, but yeah, I think the reason for that was also the C++ team wasn't really that used—also, there are other reasons as well.
[21:42] But you can see how a tiny thing can have such big consequences down the road; like him doing Polkadot today and all of that.
[21:49] And it was great—I mean, I really, I still think, maybe we would have Proof of Stake and sharding way earlier if Gavin would have stayed.
[21:58] So without him, they moved slower—of course the price went up, there were more security-relevant things, so changes happened not quickly anymore, but take more time and so on.
[22:08] But I think this was a big loss for Ethereum, that Gavin left basically in 2015.

**SPEAKER_00:**
[22:13] Yeah, it's pretty amazing.

**SPEAKER_02:**
[22:15] The client side was the cause—I think it was part of it, but you know, having the process maybe started with the "Red Wedding," which we discussed in some other early days of Ethereum episodes.
[22:26] Like, I remember very clearly in the room—like, you know, two weeks into my Ethereum tenure at that time—that he was talking about brain drain if it was only going to be a non-profit foundation and not going to have a commercial arm.

**SPEAKER_01:**
[22:39] Yes.
[22:40] There were more issues with that, definitely—this was not the deciding part, but it was like those things were adding up.
[22:45] I remember that Gavin had this idea of turning the foundation into a DAO and then having a for-profit entity next to it, which would build things and make money.
[22:53] So, there were many different commercial ideas at the time.
[22:57] So he then basically started on his own, Ethcore.
[23:01] I remember he wanted to have me as part of it, but I decided to do Slock.it at the time, so that's why I did not become a co-founder of Ethcore.
[23:09] Another story—we can go into this if you want—what happened after that.
[23:12] But there are many reasons that were part of it.
[23:15] I think also him and Ming didn't really get along too much—there was not really a trust relationship going on.
[23:21] Of course, money running out, different visions of how Ethereum should evolve technically and economically, if you want—all played a role.
[23:32] But I think it was just one part: that the C++ client wasn't really used that much, and the reason for that was Geth being audited, launching without an audit for the C++ client.

**SPEAKER_00:**
[23:41] Yeah, I mean, talking about features—so, so many things happened, right?
[23:46] You know, Gav had this period of incredible productivity between that December and that April, of getting from nothing—you know, just having the white paper all the way through to having a working client, you know, having the yellow paper, as you mentioned.
[23:59] You know, there's this, this dirty diagram showing how Whisper and Ethereum and Swarm were intended to fit together.
[24:10] And I found some more timing on that—so Swarm was envisaged by Daniel Nagy as far back as 2011, you know, it was an idea he'd been working on for like three years before that.
[24:21] I spotted on the Whisper presentation that Gavin did that—that was a pre-Ethereum idea as well.
[24:29] So it was probably only when all of these people came together, it was like, "Well, you've got this storage idea, you've got this blockchain kind of, like, CPU/database-y idea, and then if you have messaging, all of these things can fit together."
[24:41] But it's also, we're going to build our own idea as well.

**SPEAKER_01:**
[24:44] Browser.
[24:45] Browser.

**SPEAKER_00:**
[24:46] I'm sorry.

**SPEAKER_01:**
[24:47] Plus the Mist browser.
[24:48] So the complete thing—it's a, it's a complete platform for decentralized applications, end-to-end.
[24:54] This was the big vision, and also this was what attracted me to it.
[24:58] I mean, having someone having a really broad vision of a new Internet, if you want—that's what he called Web3—that's where the term comes from—because it was not just a little tool, it was a complete new Internet called Web3, from data to messaging to smart contracts, blockchains to IDE to browser.
[25:16] And this vision was very, very attractive.
[25:19] This attracted all the talent and the developers because they loved building that.

**SPEAKER_00:**
[25:23] Yeah, I mean, it's a very, very expansive vision.
[25:27] And, yeah, it was, you know—Gav, as you say, you know "Web3" was him—prior to that, I like the language I saw was really about "Bitcoin with smart contracts," you know, that was already sort of the genesis of Vitalik going through that journey of colored coins and Mastercoin and meta-protocols, and that kind of positioning of "Bitcoin is a calculator and Ethereum's a smartphone."
[25:47] But it was all that kind of, like, blockchains and applications, right?
[25:51] It wasn't that full Web3 vision, which I think—

**SPEAKER_01:**
[25:53] And that really came from Gavin.
[25:56] You have to attribute this to him.
[25:58] He was having this big vision.
[25:59] This attracted also so many people—this attracted even the business people, they could now understand what it actually is, other than, "This was just like tech, let's see."
[26:08] But this is like a broad vision of how business function, how, like, this new financial world would happen.
[26:14] They could understand this far better than having this iPhone-calculator comparison—this was maybe a nice technical thing.

**SPEAKER_00:**
[26:21] Yeah, yeah.
[26:22] But then for it being a very expansive vision, that's a lot of work.

**SPEAKER_01:**
[26:26] Sure.
[26:27] But you have to start somewhere.

**SPEAKER_00:**
[26:29] That's it.
[26:30] So I mean, you know, talking about Gavin, the features—so yeah, there was a ton of stuff on that on that C++ team: AlethZero as well, and AlethOne.
[26:40] So AlethOne being the GUI miner.
[26:43] Then, I know, how would you describe AlethZero?

**SPEAKER_01:**
[26:46] Kind of first interface to the blockchain in some way, like the first graphical interface to a blockchain client.
[26:52] And what could it do? Of course, you could mine, you could deploy a smart contract, you could visit, make it visible somewhat, what's happening there.
[27:00] It was not really end-user friendly in any way, but it was just a replacement of what people just do on the command line—usually command line, run your client, some input, have some output.
[27:09] And it was the first kind of graphical user interface, graphical user interface replacing the command line.

**SPEAKER_00:**
[27:14] I guess it's sort of like a combination of what you have with the block explorer now, apart from it—that's like a view only, and this was both a view and a do.

**SPEAKER_01:**
[27:22] Yep.

**SPEAKER_00:**
[27:23] But, yeah, those, those GUI clients so—

**SPEAKER_01:**
[27:26] Much, much more influential than the Mist browser.
[27:30] The Mist browser—I think there's a video by Alex Van de Sande, it's like a 10-minute video on YouTube.
[27:36] They had this prototype—not working yet, but just like, "fake it until you make it," the vision of the Mist browser—and this also really made us understand how Ethereum could work for the end user.
[27:44] Having different identities connected to wallets, and you would load those dapps with an IPFS hash or over Swarm—one day the app was loading and you could do some finance stuff there.
[27:55] This gave us an idea of what Ethereum could be.
[27:58] So you have to think, Vitalik gave us a rather technical vision and broad intellectual thing, but Gavin gave us this pro-Internet vision.
[28:06] Alexandr, Alex Van de Sande gave us this very concrete thing—what an end user could do with that in the next six to 12 months, maybe.
[28:13] That's very important.

**SPEAKER_00:**
[28:16] Just yesterday, actually, there was an announcement from Uniswap about them sort of turning on fees and doing various things that more kind of, to do with the company and the protocol time together.
[28:27] And I saw a reaction to that saying, "You know, well, I'm never going to, you know, I'm never going to use this again, you know, you can't, like, extract ongoing revenue out of a protocol," and this person then said, "It's time for Mist 2."

**SPEAKER_01:**
[28:39] Totally.
[28:40] I've said this before, we need the—

**SPEAKER_00:**
[28:43] Full vision so that you've got hosted and the apps and you don't need a server and you don't need a company, and you can just make this pure, you know, immutable smart contract wrapped in a UI that's all decentralized.
[28:52] You think we can have a Mist 2?

**SPEAKER_01:**
[28:54] I would love to see this.
[28:56] I heard people think about this before.
[28:58] I don't know if anybody really started the project, but should be totally doable today.
[29:02] It's not rocket science, you know.

**SPEAKER_02:**
[29:03] Let me interject.
[29:05] We ourselves have made different attempts at this where you just download the app from the chain itself, pretty much—it worked fine.
[29:12] I guess it just wasn't as much differentiator; it made things a little slower to do it this way all the time.
[29:18] I also think one of the people that took the Web3—the world computer vision—sort of seriously was, like, the Internet Computer people.
[29:26] And I don't know anyone that uses Internet Computer, but, like, every once in a while I see tweets about it, and I'm like, "That sounds great, yeah, serve the app from the chain."
[29:34] You know, it's got some cool, like, smart contracting language in it and I guess there's just no demand if it, like, slows the app down even slightly.
[29:40] And I think MetaMask and then many other wallets were sort of enough.
[29:44] Still not the whole thing, but, yeah, I guess it's like you got to get people to use it if you want it to be maximally cypherpunk too.

**SPEAKER_01:**
[29:52] I fully agree.
[29:54] And I mean, yeah, the problem with this is you only need it if you really need it—meaning if Uniswap failed, the interface is not there, it's like a backup, but it's not what you want to use daily.
[30:05] And if you remember maybe, Kieran, at DEVCON 1, when they presented MetaMask, my first thought was, "Oh, this is totally away from the vision, like, how can you not run a full node? How dare you, like, to just serve over RPCs and Infura?"
[30:16] Almost—not a scam, but it was not what we intended to build.
[30:21] Today it's like, this is a decentralized version of it, this is like non-custodial MetaMask, or the good guys compared to all the others.
[30:28] See how the view shifted over the years?
[30:30] Then it was absolutely required to run a full node if the Mist browser, this is how it's done—and now we have MetaMask and Infura, and today this is really the version which is viewed as the original non-custodial Ethereum vision.
[30:44] So how things are shifting, basically.
[30:47] But yes, you only need those things if things are falling apart.
[30:51] Just as an example, so many people use the Gnosis Safe.
[30:55] Let's say the Gnosis Safe UI is gone—technically it shouldn't be a problem to run another one, but it really needs to be something on IPFS, that needs to be something which can self-host so I can still access my wallet without going to the command line.
[31:06] So for those reasons you need it.
[31:07] And the Mist browser was sort of as the fallback for every dapp.
[31:13] Like, of course you can have your application run on a normal.com domain on AWS—fine—but if you could serve the same app in a decentralized fashion as a backup, this would be great because you could still use it if the company, let's say Uniswap, fails, if someone builds a nice Uniswap UI served by IPFS directly interacting with the smart contracts.

**SPEAKER_02:**
[31:32] Yeah, yeah, that's fair.
[31:34] Also, I mean, Uniswap I think is controversial—I know Jim wanted to say something controversial—because they had the company-level fee skim and then so, I think they've turned the on-chain fee on.
[31:42] I don't know that they've turned the company fee off; I haven't read that for detail.

**SPEAKER_00:**
[31:46] I believe so, because one of the replies was saying, "Okay, so how are your shareholders gonna like that?"

**SPEAKER_02:**
[31:50] Yeah, okay, fair enough.
[31:52] Well, hopefully they hold a bunch of the UNI and it will, you know, mark to market.

**SPEAKER_00:**
[31:55] They're doing a bunch of burn so that, you know, it should be to the benefit of all stakeholders.
[31:59] But, yeah, just this interesting kind of contrast, right, between completely immutable, you know, force of nature smart contracts versus, you know, more permissioned, more tied to a company, more sort of like wanting to have fees for maintenance kind of question.
[32:13] I mean, again, you know, it's like treasuries, I guess, either.

**SPEAKER_01:**
[32:17] But this opens up the questions—how should an Ethereum app be built economically?
[32:21] And this is also a question being answered during that time.
[32:26] The DAO was one approach: should be fully on-chain, all the revenue should be on-chain.
[32:34] There should be no for-profit entity directly attached to it, and Slock.it, the company I built after that, would be a service provider for them, getting paid by them for work being done for the DAO for one version.
[32:47] I was always skeptical, and still am, about companies where you have, effectively, two cap tables—meaning you have a token cap table, if you want (of course, it's a utility token, governance token, and so on), but effectively it's kind of ownership in the protocol, and then you have a for-profit company with shareholders.
[33:03] And this is always, I think, very dangerous because you don't know where to go into—where's the value, in the shares of the company or on the token?
[33:10] This was the main reason all those companies had those nonprofit foundations in Switzerland, rightfully so, because they said you only want to have one cap table, like the Ethereum Foundation.
[33:20] There were no shareholders of Ethereum, there was a nonprofit foundation and a token.
[33:25] The token—if you want to have a share in the economic success of the protocol, you would buy Ether.
[33:31] And so, later on, there were many other token projects where they had a nonprofit foundation, so no shareholders, no second cap table, and then you would have only the token and all the value would be there.
[33:41] And now with Uniswap you have this problem of having, again, shareholders and tokens.
[33:47] I think that's dangerous and not a good idea, actually.

**SPEAKER_00:**
[33:49] Yeah, yeah.
[33:50] So perhaps let's talk about—actually, just before we get to DEVCON 1—so the launch, right?
[33:55] So obviously a lot of testing and coordination and this different series of proof of concepts.
[34:01] So I mean, how did you know it was good enough?
[34:04] Like, what was that testing flow and collaboration like?

**SPEAKER_01:**
[34:09] There are many indicators.
[34:11] One being the Olympic testnet running smoothly for a while.
[34:15] Other one, as I said, the client having an audit, which worked.
[34:19] And then, there was saying, "Okay, now if Christoph doesn't find any failing tests for like three weeks or four weeks or something, we are ready."
[34:28] And this was the case.
[34:29] And so we said, now we can set the launch date.
[34:32] And the launch itself is also a bit typical—typically Gavin or also Vitalik, nobody wanted to push a button, like nobody just, like, start a chain.
[34:41] So what was done was there was a script written which has as an input parameter the hash of the Olympic testnet at a certain block height.
[34:50] So everybody could, using this script plus the software (plus C++ or Go client, of course) and the hash, which was at that time in the future of the big testnet, start that chain.
[35:00] So there was no—at, like, launch day—we were just viewing it, there was nothing to be done.
[35:05] Was like everything was—everything, all the information was out there.
[35:08] People were just simultaneously starting the blockchain, and then over the peer-to-peer network, this was actually more, more harder stuff—they found themselves on Reddit and others to share IP addresses: "Connect to me," "Connect to my peer," "Connect to my peer."
[35:22] And so then they started to come together.
[35:26] And, of course, the longest chain was the valid one.
[35:29] So as soon as you found a peer which had their own chain, you would sync and say, "Well, yes, this is a longer one," and you would stop mining on top of his chain.
[35:37] So basically, the canonical chain emerged from that within, I don't know, 30 minutes or one hour, and then we had the chain running, and this was like a beauty to behold—to just see how this works out as intended.
[35:50] Completely decentralized, nobody did anything—you just—I was in the C++ Berlin office in Köber M37, a nice office, and we just watched it.
[36:01] And we were somewhere mining there with their laptops—wasn't really—and we were all excited.
[36:08] It started.
[36:09] I actually think two or three weeks after, or maybe four, we had the first little hard fork.
[36:15] Meaning there was some smart contract doing something, the gas, and C++ had a different result.
[36:20] It was for me almost the middle of the night at 10pm or 11pm.
[36:24] So I remember seeing this, looking for one hour or so, finding what's the issue.
[36:30] Then I found it, wrote a test about it—C++ was right, Geth was wrong.
[36:35] So gave it to Jeff, they fixed this, I think within one hour.
[36:38] And, like, after five hours everything was done and they basically called out the miners, "Please update your client."
[36:44] So, then it was fine.
[36:45] So this was the early days, but it was a successful launch, nevertheless.

**SPEAKER_00:**
[36:48] Did the Haskell client sync at genesis?

**SPEAKER_01:**
[36:50] I do not know, Tim.

**SPEAKER_03:**
[36:52] No, we were able to sync at genesis time for like a year or so; we were syncing.
[36:57] But I remember, like, that week Kieran and I were more interested in trying to get a miner in place.
[37:01] So that was what that week looked like for us.

**SPEAKER_02:**
[37:04] Yeah, I had—I was living in an apartment just south of Berkeley campus at this time.
[37:10] And Jim had taken me to Fry's to build a machine a few months prior, like a build machine.
[37:15] It had a good GPU in it.

**SPEAKER_03:**
[37:17] Yeah, Fry's is dead now, RIP.

**SPEAKER_02:**
[37:19] So I was running a miner there, and we built a couple in Jim's garage.
[37:23] It got very hot in Jim's garage, which was, you know, those machines were consuming a fair bit of power.
[37:29] Mine exploded after a few weeks—it was actually just the power.

**SPEAKER_01:**
[37:32] So I was—

**SPEAKER_02:**
[37:34] I thought the whole machine was bricked, and Jim said, "You know, I think everything but the power supply will be okay."
[37:39] And it was the case that everything but the power supply was okay.
[37:42] But then I stopped mining, and I think Jim would shut—

**SPEAKER_03:**
[37:44] We didn't even bother to buy cases at that time.

**SPEAKER_00:**
[37:47] Right?

**SPEAKER_03:**
[37:48] Yeah, you may have had a case.
[37:50] I had mine just sitting, wires out.

**SPEAKER_02:**
[37:52] Yeah, yeah, indeed.
[37:53] Sure you weren't over at that time?
[37:55] We were always, you know, sort of, at least at that time, short-handed people-wise, always catching up a little bit on the features, etc., but it—it ran perfectly well.

**SPEAKER_01:**
[38:04] There was always new features coming.
[38:08] I remember it was really one of the sweet memories during the pre-launch, sitting together with Gavin, Vitalik, Jeffrey, and me in one room at the C++ office, like the nice Gavin office, he had this 80s style thing, and we think, "Okay, what was wrong in our protocol?"
[38:22] Then they discussed with a whiteboard, changes.
[38:25] Then the first thing: "Okay, Christoph, you add a test for this protocol change."
[38:28] Then, in the meantime, at the same time, you're coding it.
[38:30] "Okay, you're done creating the test, let's see if they all pass it."
[38:33] If they all pass it, it's like, done, new feature, the directly new release.
[38:38] And so this is because not done with all the other clients.
[38:41] So they basically had to catch up.
[38:43] It was like information update of the yellow paper: here's a new test, here's, like, a little EtherPad description of what the new protocol looks like, and then please update your clients.

**SPEAKER_03:**
[38:52] But the yellow paper got me to a certain point—sorry, yellow paper always got me to a certain point, but it was always behind the other—the other clients.
[39:00] So I would always find out that like, I was behind because I went in the morning and connected to the testnet, and I was no longer connecting, or I was getting some state root mismatch or something, and then I'd have to, like, go and dig through usually the C++ client.
[39:13] I think there was maybe one or two times where—I can't remember why—I think there was one or two things that went to Geth first, but usually it was C++.
[39:20] I'd have to go digging through the newest code to find the changes and then bring them in, then a few weeks later I'd see it in the yellow paper.

**SPEAKER_00:**
[39:27] Unlike what you have now, where leading into a hard fork, you've got all that discussion and speccing up upfront and, like, yeah, applying the code into the clients, but only enabled for a testnet and going through that dance and then ready to go.
[39:39] I mean, at that point, as you say, it's done in those clients first and then spec later, it looked like from—

**SPEAKER_03:**
[39:49] Where I was standing, it looked like there was a lot of competition between the different clients and the developers there, and I think they sort of, like, took pride in having the new thing in as fast as possible.
[39:59] And so that sort of led to an environment maybe where there was not as much discussion—it was like, "I'm gonna throw it in and then I get the bragging rights."

**SPEAKER_01:**
[40:06] That was—there was always a fight, Geth vs. C++ team, about who's the best, and, like, Gavin was having a big ego and Jeff was more like, "Just give me a new spec, I'll just code it."
[40:15] But yeah, it was more or less this decision by the three of them.
[40:19] I was basically not playing a very major role in the room and then writing a test for it.
[40:23] But they discussed it, after it was clear, they just did it.
[40:26] But it was pre-launch—after launch, of course, this was different.

**SPEAKER_00:**
[40:30] Sorry—

**SPEAKER_03:**
[40:31] Oh, I was just gonna say, like, I don't—like, a lot of the changes were just, like, some change in the EVM or, or, or pricing or something.
[40:39] And so, so often it was like, you know, I would freak out in the morning when I wasn't working, but then, like, by 11 o'clock or in the, you know, a.m., I had found, like, "Oh, I see, such and such opcode just doubled in price" or something.
[40:52] So I would just put that in.
[40:54] But the big one was RLPx, which is essentially like a big SSL replacement.
[40:59] And that one was, like, freaking me out for a couple of weeks; I was, like, digging around, trying to find any information about that.
[41:05] Eventually, I had to reverse engineer—maybe that was the one that was in Geth first, I can't remember—but I had to sit there and reverse engineer, I had to run either C++ or Geth and then, like, put lots of logging information in to see what in the world was happening and then print out all the stuff and then find, like, the appropriate, you know, crypto libraries to mimic that.
[41:19] And what was the background on that, and how it went in so quickly and, like, there was nothing in the yellow paper about that at all?
[41:27] And when that came in, it was just a shock to me.

**SPEAKER_01:**
[41:29] Do you know at which time this came? Because I was focusing on the Ethereum Virtual Machine at the time, this was more like...
[41:35] Okay, I know Gavin—I think it was Gavin doing some optimization; he was always thinking about the long term, so if something would be 10% more efficient, "We have to do this," right?

**SPEAKER_02:**
[41:43] I think so.
[41:44] I remember, like, there was a devp2p, libp2p website that was released about that time.
[41:48] It still might have been after the giant change went in.
[41:51] So, I also—we were working together regularly, you know, in the Bay Area this time, and I think, so Jim did, like, 96% of the changeover, but we had at the time, like, separate processes—one was more like a client and one more like a server, we merged them later.
[42:05] And, yeah, it was like, there was a big document describing, like, how the DHT for peer discovery would go in.
[42:13] But then you needed, like, a way to identify the peers, maybe, and this system kind of gave them an identity with, like, you know, in an SSL style.
[42:21] Like, basically there was, like, a node cert, in effect, and then you had to, like, there were session keys, and, you know, this, this, that, and the other.

**SPEAKER_00:**
[42:27] It was—

**SPEAKER_02:**
[42:28] It took a long time to implement that thing.
[42:32] But, yeah, I think maybe, Bob, you would know that—I think this was—
[42:35] Someone else wrote this big thing, this might have been Alex.

**SPEAKER_00:**
[42:39] Yeah, it was Alex Leverington did that. So, saying about documentation or whatever—there was a wiki, right? There was an Ethereum wiki, and a number of things were documented only on the wiki.
[42:48] And I think these kind of wire protocol pieces were part of that.
[42:52] But, yeah, Alex Leverington was the first hire into that Berlin office and he primarily—I mean, he works on a few different C++ things, but the main thing he's known for is DevP2P, which was that common underlying peer-to-peer protocol—though you already had libp2p, which is the transport for IPFS, that already existed at the time.
[43:09] There was a bit of not-invented-here going on, but, yeah, he was there for DEVCON 0 as well, and he spoke on—

**SPEAKER_01:**
[43:17] I remember Alex, I was not too much into the peer-to-peer side of the codebase; I was more into the EVM and Solidity smart contract side.

**SPEAKER_00:**
[43:23] I tell you what, there was a bit of a funny crossover with the later part of yours, was Alex Leverington worked with John Garrett on a project called Airlock.
[43:29] I remember that, I saw it.

**SPEAKER_01:**
[43:31] Later, like after we did our presentation, had the Slock.it stuff going, they showed us videos of—very earlier than us.
[43:37] So yes, they were actually tough, time-wise.
[43:41] They did this before we did, but I did not know about it at all, and so we did it more or less in parallel then, and we just launched a bit quicker, like, to go into the public with the project.
[43:51] Theirs, from their side, was more like a little side project, didn't look like a big company or intended to be.
[43:57] Yeah, I remember this project.

**SPEAKER_00:**
[43:59] Yeah, so I think that was at the hackathon at the Bitcoin Expo in April 2014 that they did that, and Stefan actually did an interview with them—you can see that on YouTube.
[44:10] You know, this is like talking about early Ethereum projects—you know, and this is like over a year before the mainnet, like so far back, some of these.
[44:18] But, yeah, like, some of that spec stuff was, it was not in the yellow paper, and it was just sort of floating around and a long time before there was real consolidation of that full client spec.
[44:26] But you managed to do it anyway.
[44:28] Jim managed to build the client.

**SPEAKER_03:**
[44:31] It was a busy week, but I just—it was just notable to me because, at least from what I was seeing, it went from zero to one, like overnight.
[44:38] I had never heard of it the night before, and then the next morning it was like in the clients and working and I couldn't connect to anything.

**SPEAKER_02:**
[44:45] Which is normally the pattern, but, yeah, just—this one was like the biggest one-time change that I can recall, either.

**SPEAKER_01:**
[44:49] Yeah, yeah.
[44:50] Again, this was pre-launch days, things had to move fast.
[44:54] There was a lot of pressure going around, it was messy, there was not much coordination between the clients except for maybe some Skype groups.
[45:01] And in the end, yes, usually Gavin and Jeff just made decisions and executed as quick as they could.
[45:09] So this all changed after launch; then things became a bit slowed down, and people consolidated, and every change was a big thing, rightfully so.

**SPEAKER_00:**
[45:17] Yeah, yeah.
[45:18] So, back on the timeline—so it was July 2015 that mainnet launched with a Frontier hard fork.
[45:25] And then as you touched on, you had Ming—so Ming's first official day was 1st August 2015, at which point the foundation had been running on for a year or so and was close to out of money.
[45:35] You know, touching on your thinking—it would only last for a certain amount of time, you know, a year on that raise, which I think was around 16 or perhaps $18 million, was nearly all gone.
[45:44] So you had these quite hard decisions about, you know, which part of this grand vision was going to be funded initially.

**SPEAKER_01:**
[45:52] Right.
[45:53] And I remember talking to her at the time, she felt like, "I have to clean up the whole mess," like, "The paperwork and everything was totally messy, working with lawyers, accountants, and so on, and getting cleanup basically of the foundation."
[46:04] I mean, for me, I did expect it to last something like that.
[46:07] So, for me, it was clear they're not making any money.
[46:10] I didn't know, like, how big the reserve was—the detail, I think, was like, I don't know, 5%, something in this range, like how much ether the foundation held.
[46:19] At the time there wasn't that much value either—price was like $0.50, €1 or something.
[46:24] So it was clear this would not last forever.
[46:28] So I was thinking about going back to my PhD, or then I came across this idea about Slock.it and becoming, like, building a company.
[46:36] And Slock.it was the idea of—maybe similar to Airlock—smart contracts are essentially permission systems.
[46:45] 90% of a smart contract is who's allowed to do what.
[46:48] In case of an ERC-20, it's just who's allowed to send a token or setting an allowance.
[46:53] And in terms of a DAO, it's who can vote for what and making decisions, and then money gets transferred.
[46:59] So what if we could put this permission system into IoT, like, who's allowed to switch on/off, use, change, admin rights, whatever—you put this into a smart contract.
[47:09] And I thought that Ether will never become a currency—Bitcoin was a digital currency.
[47:16] And, actually, if you talk to Ethereum people at the time, we were not thinking about competing with Bitcoin—Bitcoin was a digital currency, we were building a platform for decentralized applications; Ether was just used to run it.
[47:27] I once heard the statement somewhere on Twitter where once that "Bitcoin is a currency which needs a blockchain to function, but Ethereum is a blockchain that needs a currency to function."
[47:37] I think it's very true.
[47:39] And so back I thought, okay, Ethereum will not be used as a currency, but it might be used as a currency for IoT devices.
[47:45] So instead of the Internet of Things, building the "Economy of Things," and this is kind of what drove us.
[47:52] And then we wanted to build this Universal Sharing Network as an application—at the time Uber and Airbnb just became big—we thought, well, all those sharing economy services should run on chain.
[48:03] So let's build this, called the Universal Sharing Network.
[48:07] And then we thought about how to start with something tangible.
[48:09] And then we had the Slock lock—actually, it's here in the background.
[48:13] If you see it, it's there.
[48:15] I have this DEVCON 1 physical smart lock which we connected to the Ethereum blockchain using our own software and had this idea of people paying to open the lock.
[48:25] And that's what we presented at DEVCON 1, together with this idea, which actually only came up like three or four days earlier, to connect this with a DAO—and the rest is history, what happened after that.
[48:36] But we didn't intend and we didn't start Slock.it for building a DAO—we wanted to build Universal Sharing Network.
[48:43] Then we thought, well, this is way too big for us, we want to now focus on this Airbnb use case for door locks.
[48:49] And then we thought about fundraising.
[48:51] We talked to a bunch of VCs.
[48:53] I actually—I remember flying to New York, talking to VCs there.
[48:56] Everybody said no.
[48:57] Then I met Joseph Lubin—he said yes, maybe under some conditions—we just did not agree on the terms in detail at that, but I was presenting at the Bitcoin meetup in New York, and the first application was a bitcoin application about arbitrage trading—it was kind of boring.
[49:12] And then I came as a door lock, was like super fascinating—could open the door by paying some Ether.
[49:18] So it went well, but we had—didn't have any money.
[49:22] So we thought about doing something like an ICO.
[49:25] But this was now after the launch of Ethereum.
[49:29] So I started coding an ICO smart contract—why should we have the money directly?
[49:33] It could stay in the contract, and then people could vote for giving us part of it.
[49:37] Then we said, well, we could make proposals to it, and then they can vote if the proposal is good or not good or not, then the money would be released to us.
[49:45] Then they think, why could not everybody make a proposal, like, everybody could create it, everybody can make a proposal, and it's completely open, and we are just one of many service providers to the DAO building this Universal Sharing Network.
[49:55] And this was the origin of the DAO—only, like, again, three days before DEVCON 1, we actually decided we would go for it and put it into the presentation.

**SPEAKER_00:**
[50:04] Yeah, amazing.
[50:05] I mean, so, on the timeline, again, trying to judge it—so Stefan was, I guess, Chief Communications Officer or so, up until September of 2015.
[50:14] That's when he left.
[50:15] Had you left already by then? Can you remember?

**SPEAKER_01:**
[50:18] No, I didn't really leave because I was technically a freelancer, although I was working full time for it.
[50:25] I didn't have, like, a formal employment contract.
[50:28] So I was—continued to work I think until end of the year.
[50:32] And then I just talked: "Well, you just put down my hours, basically, if you need me, tell me I just invoice what I'm doing."
[50:37] But I was really leaving actually in December, January—I think the last invoice was for December.
[50:43] And when Stefan Tual left or was being left—I mean, there's another conversation, how he left the foundation; it was not—he didn't agree with some people getting Ethereum—is another story for another day, I guess.
[50:57] But he was really a crucial part in building up this Ethereum community.
[51:01] Like, all this meetup culture—the meetup culture didn't really exist like that before he was going from place to place, finding someone, running meetups.
[51:08] So he was very important for that.
[51:10] And I, I know—I was a coder, Alex Simon, who I co-founded Slock.it with, was also a coder.
[51:16] We needed someone who can talk to the people, can do marketing and this stuff, and we said, well he has the right address book, he knows the right people, everybody knows him in the community.
[51:22] I think, let's ask him if he wants to join us.
[51:24] And he did.
[51:26] And I think he was a very important part in making the DAO what it was—later on he did some messages which I also didn't like, and so he was a bit in this craze what happened then, and I think the community was very, very hard with him because he was not always reacting maybe as he should in some situations after the hack, but nevertheless he played a very important part in the history of Ethereum and also...

**SPEAKER_00:**
[51:48] Of course of the DAO and, and so, so DEVCON was November 2015.
[51:54] So that was announced earlier in the year, I think, I think September-ish, but ended up being canceled—you know, because the foundation were basically, you know, the same making out money piece, but then, primarily with ConsenSys funding and support, you know, "Hey, it's back on."
[52:08] So that was in London and, you know, significantly larger event obviously than DEVCON 0 because it was the first, you know, public Ethereum outing, with Microsoft as a headline sponsor.
[52:17] You had Nick Szabo speaking as well, maybe Satoshi, maybe not Satoshi.

**SPEAKER_02:**
[52:21] I think he strongly alluded to it in the presentation—it was funny.

**SPEAKER_00:**
[52:24] So, so, yeah, how was that for you then, Christoph? What was, you know, it was totally—

**SPEAKER_01:**
[52:29] Different than DEVCON 0, because this felt like, now we're going out in the world and show to the public.
[52:35] It was a fancy space in London with a really fancy, like, almost cathedral-looking space to present again.
[52:43] We had Vitalik and Gavin talking about the vision of Ethereum, and if you look at the talks being given, I really think people, entrepreneurs today should just rewatch them because they all have been 10 years too early—be it about Uport building identity solutions, I think it was Boardroom doing that governance on chain, many, many ConsenSys startups.
[53:00] Of course we, as Slock.it, thinking about, well, "Let's connect IoT and the blockchain"—again, all of that 10 years too early.
[53:09] I remember also Simon speaking about—not my brother, I forgot his last name, but Simon speaking about everybody getting a token, like he really predicted this token economy would now thrive, which happened.
[53:19] So it was a great place to be.
[53:21] Everybody was looking into the future, building the future—it was very, very exciting.
[53:27] It was very important that ConsenSys was funding this, it was crucial—the step-on-one moment, showing "Ethereum is live, now we show you what we will build with it."
[53:38] But still there were no applications running, so it was all visions and thinking.
[53:44] And so, this is one reason why, when we then did the DAO, the DAO was held like almost the first real thing you could do with Ethereum—that's why so many people jumped onto it.
[53:57] And then the, maybe to just finish this off, the narrative changed—it was not anymore a DAO for the Universal Sharing Network, but maybe because of the curators we chose, which were important figures in the Ethereum space and many other things, it turned into like an investment fund, or like an index fund for Ethereum applications.
[54:19] Because now, after 20, 30, 40 million was in, it was clear this was not just money for Slock.it and the USN, this was money for more cases and more people applied for it.
[54:29] It became like every decentralized application—or many of them, not everyone—saying, "I'm applying for getting funding from the DAO," so the DAO would pump all the applications.
[54:39] So it's like, you invested in, maybe Bitcoin 10 years, five years ago, became rich.
[54:44] Now you invested into Ether, went well, and now you can invest in the application layer.
[54:49] You do that through putting money into the DAO.
[54:52] This was not a story we told—not how we intended it—but that's how the narrative changed during the fundraising and then became that big.

**SPEAKER_00:**
[54:59] Yeah, I mean, it was interesting.
[55:00] You—

**SPEAKER_01:**
[55:01] You're saying that—you're muted, Bob, I cannot hear you. Is it—maybe it's just me?

**SPEAKER_00:**
[55:06] Can you hear me?

**SPEAKER_02:**
[55:07] I can still—

**SPEAKER_03:**
[55:08] I hear him.

**SPEAKER_01:**
[55:09] Sorry, I have an issue here. This was my system. So now I'm back.

**SPEAKER_00:**
[55:12] Can you hear me? Can you hear me, Christoph?

**SPEAKER_01:**
[55:15] No, I have to switch back to—let's—can you hear me now?

**SPEAKER_00:**
[55:18] Yeah, I can hear you. I could always hear you for some reason.

**SPEAKER_01:**
[55:21] Oh, we—

**SPEAKER_00:**
[55:22] We've heard you—hear you anymore.

**SPEAKER_03:**
[55:23] This was like me an hour ago, by the way.

**SPEAKER_02:**
[55:25] Streamyard.

**SPEAKER_01:**
[55:26] Okay, my audio is completely broken, so I will try to fix this. We can continue.

**SPEAKER_03:**
[55:30] I basically had to like close it and come back again with my earphones, but I don't know.

**SPEAKER_00:**
[55:34] Perhaps while we're waiting, Kieran and Jim, you could talk a little bit about the Strato launch at—

**SPEAKER_03:**
[55:37] I thought you were going to say you could sing a little song. I got nervous for a second there.

**SPEAKER_02:**
[55:40] You know, okay, so in this period of time—

**SPEAKER_01:**
[55:43] We were working—just reconnect, just turn it off and on again.

**SPEAKER_02:**
[55:46] We were working as part of ConsenSys and one of the kind of marketing, business development people at the time, Andrew Keys primarily, had put together a partnership with Microsoft.
[55:56] I don't know if they ended up co-sponsoring DEVCON 1 per se—

**SPEAKER_00:**
[56:00] They were the headline.

**SPEAKER_02:**
[56:01] Yeah, so they put money in for that because they also, like, paid for a bunch of PR and all those sorts of things too.
[56:08] And so we had maybe a month or two lead time to work with them, and so the idea was that, you know, they've got cloud infrastructure, it's a good place to run blockchain nodes.
[56:15] They also have corporate clients that were actually very interested in the technology.
[56:19] We worked pretty closely with them in the run-up to make our software available on the Azure cloud, as did Roman of the Java client, which to some extent was everyone's preference because people know Java in the enterprise world.
[56:31] But I think we stuck with it quite a bit longer than Roman did.
[56:34] And, you know, it was blockchain as a service was the big announcement.
[56:37] It was this December 2015—

**SPEAKER_00:**
[56:39] It was November.

**SPEAKER_02:**
[56:40] November. Was it November? Well, must have been December, really. November.
[56:43] There was a—once the announcement happened, there was a little tick in the Microsoft stock price which we always, like, "Whoa," like, there's a little, little bump there.
[56:50] And a lot of excitement, for sure.
[56:52] Got a million phone calls after that, that was, like, you know, good, good feeling of being the hotness, that only happens so many times in someone's life, you know.
[57:00] But tremendous interest on the back of the blockchain as a service announcement.
[57:04] We did a live demo.
[57:05] It was, it was fun.
[57:07] The Internet—you know, it gets in vogue to make fun of the UK these days on X, etc.—the Internet in the conference facility was not so good.
[57:13] So I was very worried about the transactions actually going through, but they did during the live demo.
[57:17] I think there's footage of it somewhere.

**SPEAKER_00:**
[57:19] Can you hear us again now, Christoph?

**SPEAKER_01:**
[57:21] Yes, I can hear you.
[57:22] I hope you can hear me, too.

**SPEAKER_00:**
[57:24] Okay, so the demo that you did at DEVCON 1, again, another iconic event, because, yeah, you have that physical smart lock just sitting there on your shelf and, you know, it rotated right, you know, right—you did your transaction.

**SPEAKER_01:**
[57:34] We just had a Raspberry Pi connected via, I think it was Zigbee or Z-Wave back then, to the door lock.
[57:41] And on the Raspberry Pi we had actually an Ethereum client running and we had a smart contract on chain where you could send some money to it—or Ether actually—when it received some Ether, it would open up.
[57:53] This was basically the demo.
[57:55] But it was cool to see something physical, someone using Ethereum for, as I said before, the economy of things connected to IoT devices.
[58:02] Since most of the people in the room were still nerds and devs, they loved that kind of stuff.

**SPEAKER_00:**
[58:08] And there was also the kettle, wasn't there? The—

**SPEAKER_01:**
[58:10] Yes, there was also a kettle where we just turned a smart plug, like a power plug, we could also turn on/off—same protocol, same thing.
[58:18] So we just wanted to show it's not just the door lock company because, actually, you're not producing those, you're just connecting existing door locks to it.
[58:25] Wanted to show this idea of the Universal Sharing Network—everything which you can turn on/off or lock up and unlock could be now connected to this network.
[58:33] And everybody could put almost everything in there—like a washing machine; you pay for using the washing machine, or a bicycle lock.
[58:42] We even had padlocks connected to it, so you could have it like your locker room and you have a padlock in front of it and sell whatever's in there by having someone pay to open the padlock.
[58:51] This was the generic idea.
[58:53] I mean, we got some VC money later after, like in 2017, we built it.
[58:58] Nobody used it.
[58:59] It was like—not just too early—it was not—it was like everything for everyone all at once.
[59:04] And, of course, nothing for no one.
[59:07] It felt like the app was not great.
[59:10] So we failed B2C-wise at Slock.it.
[59:12] We then turned into more consulting projects to build Incube, which was an IoT client.
[59:17] Made some money with that, had about 50 people actually employed at the time.
[59:22] In 2019, when we sold the company to Blockchains Inc., Jeffrey Berns—another story.

**SPEAKER_00:**
[59:26] So I remember speaking to Stefan at the time, so Stefan was involved with that demo, right?
[59:31] Right, it was Stefan who came up on stage to make his little cup of tea with the kettle there.
[59:35] But I remember speaking to him, that he'd been concerned about what the reception for him would be like, you know, having had this, you know, passing of ways with the foundation just two months before.
[59:44] But he was saying it was all very, it was all very friendly and people, you know, very excited about the project.

**SPEAKER_01:**
[59:50] Right.

**SPEAKER_00:**
[59:51] And saying actually about that IoT and pieces, so in January 2015 you had a demo that happened at the Consumer Electronics Show, the CES in Vegas, which was a collaboration between IBM and Samsung.
[01:00:07] So the aforementioned Henning Diedrich, part of—

**SPEAKER_01:**
[01:00:09] That.

**SPEAKER_00:**
[01:00:10] And that again was months before mainnet, but you had a proto-Web3 stack there, which was I think PoC 5 of Ethereum.
[01:00:18] You didn't have Whisper, you had another thing called Telehash, and you didn't have—you had BitTorrent.
[01:00:23] So there was this proto-Web3 stack there and they had demos like a washing machine buying its own detergent and scheduling its own repair.
[01:00:32] So, so yeah, that, that was happening a little earlier and, and yes, I mean, so Slock.it itself did a number of these different products, right?
[01:00:39] There was something with electrical charging and something to do with toll roads—is that right?

**SPEAKER_01:**
[01:00:42] Right.
[01:00:43] We had a prototype running with RWE or Innogy in Germany—they're doing, like, all the, at the time, most of the charging stations.
[01:00:50] So this was in general, like, we got a lot of attention, of course also after The DAO hack and all of that, and so that's kind of why we became a consulting company because so many asked us, "Could you do a prototype issue?" because there were not many Ethereum builders at the time.
[01:01:03] So we had been building on Ethereum now since one or two years, which you could not find anybody doing this.
[01:01:08] So we were building lots of nice prototypes and some almost production stuff and always related to IoT devices connected to the blockchain—this was our core business.
[01:01:16] And on top of this, you built those prototypes; we did a lot of work for the Energy Web Foundation, I don't know if you're familiar with them, this was in Switzerland.
[01:01:23] They are kind of a fork of Ethereum, focusing on all the energy use cases—we built most of their stuff in 2018, beginning of 2019, until they hired their own developers.
[01:01:35] Gavin was also part of this a while.
[01:01:38] So, yes, this was still—I mean, if you remember this time, Kieran, you say there was so much enterprise interest—enterprise at a time were just learning, looking into this, wanted to build prototypes, not yet production stuff.
[01:01:51] So, and there was a huge demand for blockchain experts, for doing consulting, for going to conferences, explain to them what a blockchain is—with, at every tech conference you needed some blockchain talk.
[01:02:02] And this was kept basically mostly us, and they paid sometimes like €4,000 for a talk—like, as a company, we said, well, we need the money, let's go there.
[01:02:13] So we—of course you also have to think about us as persons, as Simon and me, we didn't get any money for almost a year.
[01:02:21] Like, we worked for—we were not rich people, we come from ordinary families, and we said, well, we can work for like three to four months without a salary, let's like build The DAO and then it becomes big, The DAO is paying Slock.it to build it.
[01:02:33] Of course, after the hack it was clear there will never ever be a payment, so we can—we made zero money out of The DAO, so we needed to stop doing, start doing some work, and this was in the beginning, let's do consulting for those large companies.
[01:02:48] This is how Slock.it began to survive.
[01:02:51] Many people said you can, like, bury Slock.it after what happened, like your name is burned forever, and we decided to stay as a team—I mean, as a founder team, we own our mistakes, maybe we are open and transparent about it as much as we could; it was, of course, an honest mistake.
[01:03:07] I mean, you can talk for—it could be another session just for The DAO.
[01:03:11] I mean, The DAO is a lot of topics, I just put here very shortly, just talking about it from a company perspective.
[01:03:19] And then Stefan Tual, he was saying, well, he was trying to get VC money, Simon and I, we were doing those consulting gigs.
[01:03:26] And once we had VC money, what happened as a company was we got $2 million, then we built the product, hired people for that, got more and more consulting gigs.
[01:03:36] So we always said, well, let's do them and just hire more people.
[01:03:40] And in the end we had like 50 people, five or ten doing the product and 40 people doing consulting.
[01:03:45] And then we got bought by Jeff Berns from Blockchains Inc.
[01:03:49] Remember, maybe at DEVCON 3, I think, where he did this big tour in Prague, right—wanted to build a city?
[01:03:55] I think I love the vision, he obviously had money, he wanted to build it on top of Ethereum mainnet.
[01:04:01] I'll think about how maybe I can channel those billions into the right direction, building it all as intended on Ethereum mainnet, which was working fine for the beginning.
[01:04:09] And then I found out once you're an entrepreneur, you never can be an employee again, so I had to leave.
[01:04:17] So, but, it's maybe actually, it's too far in the future.
[01:04:21] I mean, that's one thing I think I have to say here because you talked about DEVCON 1 and you skipped a little bit DEVCON 2.
[01:04:28] You said in DEVCON 1, Stefan Tual was very concerned how people perceived him and they were very gentle, forgiving, and nice to him, so he was well received and then he built The DAO community.
[01:04:40] I was super worried to go to DEVCON 2 because this was after the DAO hack—I was, like, seriously thinking someone, they might beat me up there, like, around the corner there are some people, like, I kind of almost destroyed Ethereum with the spark and so much attention to it and all the money lost for some people, or like the time of records gone—it depends on how you feel it.
[01:05:02] So, but when I went to DEVCON 2, people were so nice, forgiving, basically hugging me when I was giving the talk there.
[01:05:10] And the only thing I didn't like was the foundation telling me I was not allowed to speak about The DAO, which was like, "What? Like, I'm speaking here to the Ethereum community, how can I not speak about The DAO?"
[01:05:21] And so I talked about a pretty boring talk about security, and I think every second talk was about security at DEVCON 2, it was just about how we get those smart contracts secure.
[01:05:33] So I gave a rather boring talk, but in the end I just said, "Well, thank you for your understanding," and it was a hard time and so on, and they were, like, somewhat—there were standing ovations.
[01:05:46] I remember becoming emotional because this was—I did not expect this.
[01:05:51] I really expected, like, "Guy, you messed up Ethereum, like, we almost lost it all."
[01:05:57] So I think this just speaks to the Ethereum community, how they treated Stefan, how they treated me—even though mistakes were made, honest mistakes, at least from what I can tell.
[01:06:09] This is such a great community of really nice people who really want to change the world, capable, and also now financially capable of really doing things.

**SPEAKER_00:**
[01:06:17] I was watching that video quite recently, actually, and yeah, it was cut off a little bit.
[01:06:22] You know, it was quite a long ovation there and, yeah, you could certainly see that emotion in you.
[01:06:29] And that's when we first met, actually, was in Shanghai for DEVCON 2.
[01:06:33] I remember was—was on the sidelines there in that main conference hall and, yeah, it was lovely to see that, that's for sure.
[01:06:39] Okay.

**SPEAKER_02:**
[01:06:40] Yeah, I think good notes.
[01:06:42] Just... Bob, you were the one who tried to impose half hour to hour rule.
[01:06:47] We're at a solid 120 right here.

**SPEAKER_00:**
[01:06:50] Me the other time, maybe we, you know, we've reached a, you know, a good kind of end point, I guess.
[01:06:56] So what happened after Blockchains LLC for you then?

**SPEAKER_01:**
[01:07:00] So because of time, I’ll keep it short.
[01:07:02] So, yes, we got bought by Jeffrey Berns, Blockchains LLC at the time.
[01:07:07] Again, the reason for this was he wanted to build a new city in the desert.
[01:07:11] He wanted to do all on IoT, all on Ethereum, from scratch.
[01:07:16] And as a developer, it was a dream—building from scratch on a green field on top of Ethereum with our tech.
[01:07:22] And I felt comfortable in the beginning.
[01:07:24] In the end, I felt like, "We need to release stuff," and there were some voices at the company which didn’t want to release until, like, a very, very big product was done—for many reasons, that didn't happen.
[01:07:35] I don’t want to get into that too much.
[01:07:37] So after two years I left Blockchains—it was called Inc. back then, they made a change in their name.
[01:07:43] And I did, for six months, I did really nothing; I forced myself to do nothing, which was great after so many stressful years.
[01:07:50] And then I started a venture studio called Kopos Ventures where we tried out many different ideas—we had EM3, which was a decentralized messaging protocol, GasHog, you can save transaction costs on Ethereum.
[01:08:01] What else did we have?
[01:08:02] We had some domain name stuff, but we didn't release it at the end.
[01:08:06] But the biggest one was Tokenize.it, and this was me—built something for German, for now, German startups; in the end, we want to do it all over Europe, and we’re just tokenizing their shares and doing fundraising.
[01:08:19] So in summary, it's like a Web3-based AngelList for Europe—it's the one sentence description for Americans also to understand, you know AngelList, it’s a great tool for business angel investing.
[01:08:29] We want to do the same for Europe, for all countries there, and build it on-chain; so tokenizing all those shares and enabling private as well as public fundraising.
[01:08:40] So some called "legal ICOs" if you want, but also for private fundraising.
[01:08:44] Our customers—currently we have more than, maybe a good, good way to end this—we have now more than 400 investments from more than 320 business angels and more than 50 companies.
[01:08:55] Those are traditional German GmbHs raising from super conservative business angels and doing it completely on-chain.
[01:09:00] They're paying in stablecoins, getting their tokenized shares in their non-custodial wallet, they're all getting a Gnosis Safe wallet from us, using Privy for login.
[01:09:08] So, we build it as intended and we get normal people to use it.
[01:09:12] For me, this is kind of a dream come true because I'm—I love the Web3 bubble, I love this community, I love to work inside there, but for me, Tokenize is a way to make this technology available where it belongs, like to startups and investors outside of our Web3 bubble.
[01:09:28] And I’m super, super happy that I could keep up those values, that the complete platform is non-custodial—they have their safe on Ethereum holding their tokens, paying stablecoins.
[01:09:37] So I'm very happy to see this over the next years, we want to basically roll out this all over Europe and become—yes, the Web3-based AngelList for Europe.
[01:09:45] That's the goal.

**SPEAKER_00:**
[01:09:47] Fantastic.
[01:09:48] Hope to see you at DEVCON 8.

**SPEAKER_01:**
[01:09:50] Me too.
[01:09:51] I'm looking forward to it, and as of now, and I don't intend any change, stick to Ethereum.
[01:09:56] I love the community.
[01:09:57] I continue building and try to get a lot of people using it.

**SPEAKER_00:**
[01:10:00] Have you been to every DEVCON?

**SPEAKER_01:**
[01:10:02] Yes, I said, yes, I've been to every DEVCON.
[01:10:05] The last one was actually the first one that I didn't give a talk, and also went to every EthCC except for one where there was COVID—that was the reason I couldn't come.
[01:10:15] But yes, actually I intend to continue to come to every DEVCON.
[01:10:18] It's like, you meet the people like Thrifting, Lefteris, of course, Vitalik and many others, it's just a sweet spirit there.
[01:10:26] Nice community.
[01:10:27] Love seeing how it all grows, listen to those exciting talks.
[01:10:30] I mean, for Tokenize.it, it's not as relevant—it's not like our customers or it's a tech.
[01:10:36] Of course, we're just doing an ERC-20 token on Ethereum, it's super easy, no deep tech.
[01:10:42] Sometimes I miss doing deep tech, but, well, I just enjoy being there, seeing what it all—what all happened, and remembering those magic days.
[01:10:51] And just like, only once in a lifetime or two times in a lifetime you have this moment where everything comes together—the right time, the right place, the right people.
[01:10:59] This certainly were those, like, one and a half years I worked for Ethereum, but definitely like the prime of my career in terms of who I worked with, what we accomplished, the impact we had on the world, and this sweet cypherpunk spirit there and what we did.
[01:11:12] It was really great.
[01:11:14] I always sometimes get emotional thinking about this and meeting those people again at DEVCON.

**SPEAKER_00:**
[01:11:18] Fantastic.
[01:11:19] Well, thank you for all your contributions to that success.

**SPEAKER_01:**
[01:11:23] Likewise.

**SPEAKER_00:**
[01:11:25] All the best.
[01:11:26] Okay.
[01:11:27] Oh, just one more. Where can we find you?

**SPEAKER_01:**
[01:11:29] You can find me usually on Twitter for the Ethereum people: chr_yench, of course.
[01:11:33] I have a complicated name, not many vowels in there, but you can find it.
[01:11:37] Or, of course, on LinkedIn.
[01:11:39] Actually, for my company, I'm more active on LinkedIn, which I was never before, but that's where we get our clients—Tokenize.it.
[01:11:46] Yeah, but usually you can find me on Twitter, follow me there, or on LinkedIn.

**SPEAKER_00:**
[01:11:50] Excellent.
[01:11:51] Okay, thanks so much.
[01:11:53] Have a great day.

**SPEAKER_02:**
[01:11:54] Thank you.

**SPEAKER_01:**
[01:11:56] You too.
[01:11:57] It was great talking to you.