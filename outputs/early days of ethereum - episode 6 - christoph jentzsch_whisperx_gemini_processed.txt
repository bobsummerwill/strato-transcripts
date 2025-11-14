**SPEAKER_02:**
[00:01] Okay, recording is in progress, it says. So, hello everybody.
[00:05] Today, I'm delighted to have Christoph Jentzsch with us.
[00:09] We did attempt to record this, Christoph and I, two weeks ago, but I forgot to press the record button.
[00:13] So we spoke for an hour or so, and then it was not recorded. So this is round two.
[00:18] So hello, Christoph. How are you?

**SPEAKER_00:**
[00:20] Hi, Rob.
[00:21] Nice to meet you again.
[00:22] I'm doing good.
[00:23] I hope you too.
[00:24] Thanks for the invitation.

**SPEAKER_02:**
[00:25] Fantastic. Yeah.
[00:27] So Christoph and I, our paths crossed for the first time way back in 2015 when I was trying to do C++ Ethereum on my smartwatch.
[00:36] And this was around the time that Christoph was still at the Ethereum Foundation.
[00:40] And then I think I crossed paths a number of times since, and Kieran's too.
[00:43] Indeed.
[00:44] So, Christoph.
[00:46] What were you doing with your life before you found Ethereum and joined this crazy journey?

**SPEAKER_00:**
[00:51] So the journey started in 2013.
[00:54] I was doing my PhD in theoretical physics, actually about self-organizing systems.
[00:59] So like biology, six months in mathematical biology and other things.
[01:03] So I was studying systems which have local rules and global behavior.
[01:07] And I came across Bitcoin, which is just a small set of local rules and a global behavior as a currency.
[01:13] But the reason I came across this was I was looking for cheap GPUs, like graphic cards, and the Bitcoin miners were selling their GPU mining rigs to get some FPGAs and later ASICs.
[01:24] And so that's how I got into what's Bitcoin mining. And so I bought my first Bitcoin, got into this bubble, did read everything I could about it.
[01:31] And then I came across the white paper from Vitalik, early 2014, something like January, February, in some Bitcoin forum somewhere.
[01:40] And I was already totally in love with the idea of Bitcoin being a decentralized currency and all the characteristics and features of it.
[01:47] And this white paper from Vitalik—and if you read it again, it's almost a prophecy—except for NFTs, everything's in there, from DAOs, from ENS-like names, this domain name systems, and all of that.
[02:00] So for me, it opened up this option of building applications with the same characteristics as Bitcoin, but just not a currency, but everything else.
[02:11] And so then I started reading everything about it.
[02:13] And in 2014, in summer, I read that the crowdsale was in 2014, right?
[02:19] So around the time the crowdsale happened, I watched a video from Gavin Wood.
[02:23] He was somewhere in Scandinavia, some conference there, in the Nordics, and he talked about Ethereum. I loved it.
[02:30] And he said he wanted to open up an office in Berlin, looking for C++ developers. I was a C++ developer.
[02:36] In theoretical physics, it's 90% software development. So I said, well, I want to do this.
[02:41] So I took my parental leave time, plus some vacation time, and paused my PhD for like three or six months and said, I will return after I'm done.
[02:51] I thought this was just a short project because they raised money, maybe six, maybe 12 months, 18 months or so, then it's over.
[02:59] When I started, I thought about maybe three to six months, and then I go back to my PhD.
[03:04] So I worked there with Ethereum, with Gavin Wood, it was a great time, and then just decided to stay.
[03:10] It was so exciting.

**SPEAKER_02:**
[03:12] So you never got to be a doctor?

**SPEAKER_00:**
[03:13] No, I'm not a doctor.
[03:15] I did not finish my PhD, although I only had six months left, which was kind of a pity.
[03:20] I worked for three years on that.
[03:22] But I also had at the time, I think, four or five kids.
[03:25] I needed some money.
[03:26] I didn't get much money as a PhD student.
[03:28] So I did software development as a side hustle, basically.
[03:32] And so when I got this project, I said, well, let's do this for two or three months as parental leave time, and then I can return.
[03:37] And then I decided to really interrupt my PhD. I thought I will maybe return one year later because I thought the foundation would eventually run out of money because they're not making any profits. It just raised donations, then they're spent, and that's over.
[03:51] Then I can continue my PhD. That was originally the plan. It just came differently.
[03:55] I mean, I guess it's never too late, right?
[03:57] I actually sometimes think about it, that I should return.
[04:01] It's just so much to learn again.
[04:03] I'm right now doing Tokenize.it.
[04:05] I'm basically working on tokenizing German companies.
[04:08] It works very well.
[04:10] And so currently I'm not planning on getting back anytime soon.

**SPEAKER_02:**
[04:13] No, because I mean, famously you had, you know, Dr. Gavin Wood and Dr. Christian Reitwiessner as well.
[04:19] And I think there were a couple of other PhDs as well.

**SPEAKER_01:**
[04:21] There was, definitely.
[04:23] I also dropped out of mine.
[04:24] I was actually in mathematical physics too.
[04:26] Interesting.
[04:27] Similar background.

**SPEAKER_00:**
[04:28] It's actually the same.
[04:29] Like theoretical physics, it's the mathematical part of physics.
[04:33] I enjoyed it very much.
[04:34] I did thermodynamics and statistics, mostly software development.
[04:38] It was really fun.

**SPEAKER_01:**
[04:39] Well, by the way, Jim is trying to join.
[04:41] I don't know if there's anything that needs happening.
[04:43] He gets some browser issues.

**SPEAKER_02:**
[04:45] Yeah, yeah, well, he'll pop up and we can add him. Or if he's—I'll say then, then never mind.
[04:50] So, so, so Christoph, in terms of, um, you know, getting hired into EthDev, and I'm sorry if I just missed it.

**SPEAKER_00:**
[04:56] So how did that happen?
[04:57] Did you meet Gav at a meetup?
[04:59] Did you say yes?
[05:00] I actually—I listened only to his talk. It was an online thing.
[05:04] And I actually just wrote him an email, said, "Look, I would love to join Ethereum. Love what you're doing."
[05:09] And he invited me to meet him in Kreuzberg, Berlin, which is about two hours' drive from here.
[05:15] So I went up there, met him.
[05:17] I remember the first conversation, he was talking about all the stuff they were going to build and said, "Well, what can you do?"
[05:23] And I just asked him, "What's the most complicated stuff you have right now? Like, give me a complicated task. I somehow can figure it out."
[05:29] So he talked about the Ethereum Virtual Machine, which needed some testing.
[05:33] So I just picked working on testing the Ethereum Virtual Machine, or like writing tests for it.
[05:39] Back at the time, I actually had no real idea what he was talking about.
[05:43] Meaning, of course, I did understand on the white paper level, I did understand what Ethereum was about.
[05:49] But Gavin had this skill of writing the yellow paper, which is still incredible work.
[05:54] Like it's such a great specification, different from Bitcoin, really having a specification.
[05:59] So multiple clients could be built.
[06:01] And in there, he defined the Ethereum Virtual Machine.
[06:04] And I think I read the paper six, seven times. I felt like I was one out of, I don't know, 10 or 20 people in the world at the time who really understood the yellow paper.
[06:12] I did corrections to it. I have some pull requests actually in the yellow paper GitHub repo, um, added missing definitions and stuff like that.
[06:21] And then what I mostly did was writing tests according to the specification, which then were with the help of the C++ client, because this was his team.
[06:30] So I was working also on the C++ code base.
[06:33] And so Geth, PyEthereum, also the JavaScript version, and what else did we have?
[06:39] Like a Haskell client and others.
[06:42] I'm basically using my tests to see if they implemented the virtual machine, also the state transitions, and block creation correctly.

**SPEAKER_02:**
[06:51] Yeah.
[06:51] Yeah.
[06:52] So, I mean, just to have some timeline for the viewers.
[06:57] So, um, Vitalik wrote the white paper in November 2013.
[07:01] Um, various other people sort of joined in on the efforts in December, including Gav and Jeff, who started the C++ and Go clients respectively at the very end of December, kind of Christmas projects for them both.
[07:22] January 2014, he had sort of the public announcement of Ethereum at the Bitcoin Miami conference.
[07:29] It was as early as April 2014 that Gav wrote the yellow paper, which is, you know, as you're saying, the sort of formal specification.
[07:36] Um, you had the crowdsale between July and September 2014.
[07:41] Um, so then yeah, you were coming in right after that, you know.
[07:44] So you had a wave of arrivals in September and October of that year, essentially, because the crowdsale had happened, there was some money to actually hire people.
[07:53] Um, and then talking about, you know, where you met there initially, that group, so EthDev were and is a company coordinating the development of Ethereum stuff.
[08:03] So it's a subsidiary of the Ethereum Foundation.
[08:05] Um, they were working initially in a co-working space, but then got an office, and it was between August and November of that year that the office was getting, you know, done up and tidied.
[08:14] And then in November, you had DevCon 0, you know, the first conference, an internal one, where a lot of the people, that was their first sort of face-to-face meetings.
[08:26] How was DevCon 0?
[08:28] How was that?
[08:29] What was that like?

**SPEAKER_00:**
[08:30] It was like a company retreat.
[08:32] So it was not a public conference.
[08:34] Even though there were some outsiders who felt like part of the community, maybe also pushed some code.
[08:39] I remember, what was his name again? He wrote the book also about Ethereum, did his thesis from IBM.
[08:48] I think Henning was also there, just as an example of some people who were like, reading about Ethereum, interested in joining.
[08:55] Of course, Joseph Lubin.

**SPEAKER_02:**
[08:56] Roman was there.

**SPEAKER_00:**
[08:58] But it was mostly developers.
[08:59] But also, I think Stefan was already there.
[09:02] So they had already the London team.
[09:04] So it was like an internal Ethereum meeting, kind of a meetup almost, I think three days or so.
[09:09] Five days even.
[09:10] So it was a full week.
[09:11] I was there for the full week, as far as I can remember.

**SPEAKER_01:**
[09:12] Well, Lefteris presented on Emacs, so you're not the most boring talk.

**SPEAKER_00:**
[09:16] I did a presentation about testing, how the test suite is very important.
[09:21] Yes, we had Remix projects, Solidity project, I think, mostly started at the time.
[09:27] Gavin used this for explaining his vision of Ethereum as a platform for decentralized applications, so building Swarm.
[09:35] I don't know if Swarm and Whisper already launched there, but at least the generic idea, the Mist browser.
[09:41] So all those ideas are really sketched out there, like the technical roadmap of what we are going to build.
[09:47] And because we started just, of course, with the basic clients, like implementing the protocol, but he took it like, kind of, what are we going to do in the next 12 months? The Mist browser, Remix, all those tools to have a platform for dapps.
[10:05] I remember one slide, which I think I posted on Twitter a while ago.
[10:09] You have those three circles.
[10:11] One circle is at one node.
[10:13] You would see they are connecting on the blockchain, using Swarm for the data, Whisper for the messages.
[10:19] This whole picture was painted there.
[10:21] And there are people attending, I think around 50 people, plus, minus 10, don't know the exact number, where most of the developers were talking about code, coding there.
[10:30] Joseph, I remember him being there saying, "Well, all of you, you will create your own companies, becoming millionaires."
[10:37] I remember Joseph talking about that.
[10:39] And I think mostly he was right.
[10:41] So most of those people in the room...

**SPEAKER_02:**
[10:43] ...in one way or another co-founded, founded, or were an early part of companies building on top of Ethereum in the years to come. Yeah, yeah.
[10:50] Um, let me see if I can do a little screen share. No, no, I can't work it out. Not to worry.
[10:54] But yeah, there's this present button.

**SPEAKER_01:**
[10:56] Does that not work?

**SPEAKER_02:**
[10:57] Yeah, I don't see that.
[10:58] Is that on the right-hand side somewhere or at the bottom?

**SPEAKER_01:**
[11:00] Maybe you have a different... For me, I appear on the top right and below.
[11:03] And to the right of me below, there's a present button with like a plus.

**SPEAKER_02:**
[11:06] Oh, never mind.
[11:07] Never mind.
[11:08] I was just going to show the iconic photo of people at DevCon 0, right?
[11:12] You know, that big group shot with nearly everyone who was out there.
[11:15] You know, so that's a classic Ethereum photo.
[11:18] So I was looking... sorry, there's like 11 of the videos that are still around from DevCon 0.
[11:22] I think there were around 20 sessions. I'm still trying to dig out the others.
[11:26] Some of them, including yours, I have not managed to find yet.

**SPEAKER_00:**
[11:29] It was only about the test suite, how I built it, how people would use it.
[11:32] It was rather technical.
[11:33] There was not much of a vision in there.
[11:37] Again, it was just some nerds starting.
[11:39] Also, for most of them, it was the first time we actually met.
[11:42] Now, of course, the C++ team, they knew each other because they were working in the co-working space.
[11:47] Lefteris and others were there.
[11:49] But then, let's say, I think it was the first time I actually met Vitalik, because he came there.
[11:55] Then, of course, Jeffrey and his team, Stefan Tual and his team, Joseph Lubin.
[12:00] So for me, it was the first time to meet all of them and having talks.
[12:04] And since we really had time, five days, a small group of people, we actually did have time to eat together, to talk.
[12:11] So it was not so crowded maybe as DevCon is today.
[12:14] Very intimate.
[12:15] It was good.

**SPEAKER_02:**
[12:16] Yeah, I mean, far from it.

**SPEAKER_01:**
[12:17] One thing I can't quite remember.
[12:19] So there was a time there was an Ethereum Slack that was kind of open to the public.
[12:22] You know, there were a lot of people.
[12:24] The sort of Ethereum affiliation status was fairly vague at that point.
[12:28] And we were, you know, I remember we were using Skype a lot in those days, just the team.
[12:33] Um, and like Vitalik liked to Skype.
[12:35] Um, and then at some point, I sort of lost the thread of where the core... I can't remember where the core development discussions were happening.
[12:44] And I'll maybe I'll ask Jim to comment also, just like those tests.
[12:48] We kept like getting them.
[12:49] And I think I'm thinking of some a little bit earlier on, and we'd build them.
[12:53] And Jim was mostly working on them, and we'd want an update on the passing percentage, which would always be between like 93 and 98%.
[13:01] And then something would change, you know.
[13:03] Um, but yeah, like, where did the discussion... because yeah, between like the sale and DevCon 0, I think it kind of got a little bit moved around where the dev discussion was.

**SPEAKER_00:**
[13:13] Yeah, it was mostly Skype.
[13:15] We also had Skype channels for almost everything, like the C++ team and so on.
[13:20] Then in a short time, there was a note taker, which had a name also with an E something.
[13:25] Etherpad?

**SPEAKER_02:**
[13:26] Etherpad.

**SPEAKER_00:**
[13:26] Yeah, Etherpad, something like this, right?
[13:29] There were some notes being written there, but the communication was really, I would say 99% Skype for me.
[13:35] Later on, we used a tool based on GitHub. What was the name of it?

**SPEAKER_02:**
[13:42] Gitter.
[13:43] It was called Gitter.

**SPEAKER_00:**
[13:44] Gitter came later.
[13:45] This was like the replacement for Skype, but I didn't use it too much.
[13:49] This was actually during the time when I was actually leaving.
[13:52] But it was then used also by the C++ team.
[13:55] There you had a channel per GitHub repo.
[13:58] This was during the time that GitHub was completely reorganized because at the beginning it was like one big repo with everything.
[14:04] Then we had those submodules.
[14:06] It was so messy.
[14:07] And then during this process, we got Gitter.
[14:10] But yeah, for me, it was mostly Skype.

**SPEAKER_02:**
[14:12] Yeah, and then annoyingly, that kind of means a lot of these early discussions are kind of a bit lost because nobody is using Skype and Skype is getting deleted.
[14:21] This is happening in February of next year.
[14:23] Oh, I thought it happened already.
[14:24] So you can still request a download, and I did, and then I haven't heard anything back.
[14:27] And I want to do that to see if I can get some of those.
[14:29] So everybody apply to download your Skype data.
[14:32] I remember with Gitter, there was a discussion about this that I was involved with at the EF later, which was saying the problem with Skype is it wasn't discoverable.
[14:40] You had to request to be added, but you had to know what was there to be able to do that request.
[14:44] So it was a bit of a chicken and egg situation.
[14:47] Whereas Gitter, it was like a one-to-one with the repositories.
[14:50] So if you're using a repo, there you go.
[14:52] There's a one-to-one channel with that.
[14:54] And it was discoverable and archived.
[14:56] But then Slack, I think, was even earlier.
[14:59] Oh, and there was the forum as well, right?
[15:01] It was an Ethereum forum too.

**SPEAKER_00:**
[15:02] Yeah, it was important.
[15:04] And then Slack, I think I got introduced to Slack by Stéphane Tual when he created a community for The DAO.
[15:10] When he looked for a new communication tool, he went with Slack.
[15:13] And at that time, it was not like today, like a business tool for the company.
[15:17] It was really communities.
[15:19] Like we had 5,000 people in our Slack, which is not how it's used today.

**SPEAKER_02:**
[15:23] Yeah, yeah.
[15:24] So welcome, Jim.
[15:26] Are your technical problems solved?

**SPEAKER_04:**
[15:27] Hi, sorry.
[15:28] I had some technical problems for a while there.
[15:30] I don't know.
[15:31] I'm just listening to you guys.
[15:33] What happened that brought the whole world to Zoom suddenly?

**SPEAKER_01:**
[15:35] It was in waves.
[15:36] On my side...

**SPEAKER_04:**
[15:37] I don't know.
[15:38] I just woke up one day and everything was Zoom from then on.

**SPEAKER_01:**
[15:41] It was like a statistical phase transition.
[15:43] I think it was two phases.
[15:44] I would always get invited to corporate, let's say 2017 to 2019 when I was doing primarily BD, I found that I would get invited to any of 10 video conferencing tools.
[15:56] And, like, you know, what was the Cisco one?
[15:58] WebEx.
[15:59] That was horrible.
[16:00] I would get that a lot.
[16:01] Google meetings didn't feel sufficiently corporate or something, even though it was okay.
[16:06] And Zoom had the best quality for a while.
[16:08] And I found that everyone picked Zoom at the same time, like mid-2018, let's say.

**SPEAKER_02:**
[16:13] I think it was just quality, to me.
[16:14] Yeah.
[16:15] I mean, Microsoft really fumbled, right?
[16:17] Skype had got such a lead for so long, but Zoom just seemed more reliable, whatever weird little proprietary magic they had going on.
[16:24] Yeah, and then I guess, yeah, I guess I was under the impression that like Zoom was for businesses.

**SPEAKER_01:**
[16:29] I think that's, well, that is true.
[16:31] But it was just that still, I mean, this has gotten way better in the last 10 years, but still nothing really works for reliable video over the internet.
[16:38] It's just much better than what existed.
[16:41] But there was a free version always, and it would just like time you out.
[16:44] So like they had a fairly viral acquisition loop where, like, I was just going to say, in the pandemic, once when people were locked down, it became a consumer tool where people would have like large yoga classes or, you know, sermons or whatever with like 500 people on a Zoom.
[16:58] And then everyone, yeah...

**SPEAKER_04:**
[16:59] I remember it well.
[17:00] All of a sudden, my parents were calling me up and they were like, "We found this awesome new tool.
[17:04] You've probably never heard of it.
[17:05] It's called Zoom."

**SPEAKER_01:**
[17:07] But yeah, there were like 10.

**SPEaker_02:**
[17:08] Let's move on from sharing about video platforms.
[17:11] So I looked back.
[17:12] So Jim's first commits on the Haskell client were mid-September 2014.
[17:17] So, you know, a couple of months ahead of DevCon 0.
[17:20] You'd had the yellow paper for five months at that time.
[17:23] And I did find on our Slack, um, you know, a bit of a thread where things, I think from you, Christoph, were being discussed by Jim.
[17:32] I don't know, did you guys interact directly at all on testing, Jim, Christoph?

**SPEAKER_00:**
[17:36] Not directly, not as far as I can remember.
[17:38] I mean, maybe there was some messages. I mean, it has been a while ago.

**SPEAKER_04:**
[17:42] I could be wrong.
[17:43] I may have met you briefly in London when we had that conference.
[17:46] But it would have been like quick greetings at an after party or something.

**SPEAKER_00:**
[17:50] I mean, 10 years ago, lots of people, sure.
[17:53] We were testing the GitHub repo and we had all the major clients using it.
[17:57] And I was interacting, mostly asking, responding to questions.
[18:01] I mean, of course, the C++ client I was super close to.
[18:04] I used the C++ client also to pre-fill the tests.
[18:07] So this was per default right, except we found there was a test failing, but actually C++ was wrong.
[18:13] So sometimes this happened.
[18:14] The test was not really failing, just C++ was wrong.
[18:18] But in the majority of cases, C++ was right.
[18:21] So we were just having those conversations, and we found tons of issues.
[18:25] We did, not just in the beginning, I wrote those tests using actually bytecode, the very first test.
[18:31] Then I went to a low-level Lisp-like language.
[18:34] This was LLL.
[18:36] This was the precursor to Solidity by Gavin.
[18:41] And then in the end, actually, I had automated fuzz testing where I wrote software that would create thousands of tests.
[18:47] We had some AWS, like over 100 cores of machines constantly creating tests.
[18:52] We had always some failing on some versions of Geth or other clients.
[18:56] So this was mostly what I did during one and a half years.

**SPEAKER_02:**
[19:00] Right, right.
[19:01] So, so yeah, I mean, I guess for the viewers, something that Ethereum chose to do differently from Bitcoin was to have this specification separate from the client software, right?
[19:10] So, you know, when Bitcoin started, it was the code that happened first and the white paper afterwards, but the white paper wasn't a protocol specification.
[19:18] So, um, you know, Gav was doing that yellow paper spec in parallel with the C++ client, which was sort of the first one, while you have Vitalik working on the Python client, Jeff working on the Go internally, but then you've got all these other clients as well, right?
[19:33] So the Java one by Roman, I think, started in about April or May.
[19:37] You know, ourselves, Jim and Kieran here with the Haskell client starting in September.
[19:43] You had JavaScript as well.

**SPEAKER_00:**
[19:44] Right.
[19:45] It's more like a library.
[19:46] I don't know if it's really like a syncing client, but they have all the tools so you can, in your web app, kind of integrate parts of it to verify certain states.

**SPEAKER_01:**
[19:54] Yeah.
[19:54] I mean, I think maybe they had a syncing client at some point, apart from it obviously couldn't actually keep up, but theoretically.

**SPEAKER_02:**
[20:00] And yeah, like a little later, there was a Ruby client as well.
[20:04] And yeah, at one point, there were eight different clients.

**SPEAKER_00:**
[20:06] Right.
[20:07] If you want to, I can tell the story of why we all are using Geth today.
[20:11] Yeah, please do.
[20:12] Because this is absolutely not a given.
[20:14] At the time, of course, everyone had different opinions.
[20:17] But the C++ client was really the fastest, the most solid one, passing all the tests and so on.
[20:23] But Gavin always wanted to add new features.
[20:26] We went through a refactoring, and he was a perfectionist, which is not bad for this kind of software.
[20:32] And then the time came for the security audit, because everybody wanted to launch Ethereum now.
[20:37] And he said before we launch it, those clients need to have a proper security audit by an external company.
[20:43] And one of the companies doing this was Deja Vu in Seattle.
[20:47] So I actually went there with a team for the audit.
[20:50] And because Gavin wanted to build some more features, it was like, "Well, let's just let Geth go first. Let's first audit the Go client."
[20:58] When they are done, I'm done with the features I want to build, and then we're going into the audit for the C++ client.
[21:05] So Geth was audited.
[21:07] They had some issues.
[21:08] They fixed the issues.
[21:10] And now it's fine.
[21:11] And so there was technically no reason why not.
[21:14] Well, actually, we could launch Ethereum now.
[21:16] We have a fully audited client.
[21:18] Testnet is running for a while.
[21:20] No major issues.
[21:21] No failing tests for a long time.
[21:24] So why would we wait for the C++ client to be audited?
[21:27] I mean, they all really had the pressure of money was running out.
[21:30] We need to launch now.
[21:32] And then a decision was made.
[21:34] Let's launch with Geth.
[21:36] They can still use C++. It's just not audited.
[21:39] Let's say in two months or so the audit is done, and then they can use C++ even more if they want.
[21:44] So but then the big mistake was, in my view, when they made this announcement of, "You can start now," they recommended using Geth because this was the audited one.
[21:52] So almost everybody went Geth.
[21:56] This was like, we started with almost 100% Geth, and then there were just minor other clients using it.
[22:02] Only very few did use them.
[22:04] And so after the audit was done, nobody switched.
[22:07] They were like, "Sure, but Geth is running.
[22:09] I'm synced.
[22:10] What's the issue?
[22:11] Why should I switch?"
[22:12] And so we had this 90-10 or 80-20 distribution.
[22:18] It just stayed like this.
[22:19] So if Gavin would have been either saying, "Let's just do the audit now and we just have both audited and then start," maybe we'd have 50-50.
[22:29] Or even the other way around, if they would have first audited the C++ client and Ethereum would have been launched without a Geth audit, they would have seen a total switch.
[22:38] And then, of course, money was going low in the foundation.
[22:42] They had to reduce the team.
[22:44] And because Geth was the most used one, there were some issues with Gavin.
[22:49] Another story, maybe have a talk with him.
[22:52] And so in the end, Ming decided to basically kick out the complete C++ team.
[22:57] This was then shortly before DevCon 1.
[23:00] So something like November, October-ish.
[23:03] But yeah, I think the reason for that was also the C++ client wasn't really that used.
[23:07] Also, there are other reasons as well.
[23:09] But you can see how a tiny thing can have such big consequences down the road, like him doing Polkadot today and all of that.
[23:17] And he was great.
[23:18] I mean, I really, I still think, I think maybe we would have had sharding way earlier if Gavin would have stayed.
[23:25] So without him, they moved slower.
[23:28] And of course, the price went up.
[23:29] There were no security-relevant things.
[23:32] So changes happened not quickly anymore, but took more time and so on.
[23:36] But I think this was a big loss for Ethereum that Gavin left basically in 2015.

**SPEAKER_01:**
[23:42] Yeah, it's amazing. The client side was the cause.
[23:45] I think it was part of it, but, you know, having the process maybe started with the Red Wedding, which we just covered in some other Early Days of Ethereum episodes.
[23:56] He—I remember very clearly in the room, I was like two weeks into my Ethereum tenure at that time, that he was talking about brain drain if it was only going to be a nonprofit foundation and not going to have a commercial arm.

**SPEAKER_00:**
[24:10] Yes, there were more issues than that, definitely.
[24:13] Like this was not the deciding part, but it was like those things were adding up.
[24:17] I remember that Gavin had this idea of turning the foundation into a DAO and then having a for-profit entity next to it, which would build things and make money.
[24:26] So there were many different commercial ideas at the time.
[24:29] So he then basically started on his own, EthCore.
[24:33] I remember he wanted to have me as part of it, but I decided to do Slock.it at the time.
[24:39] So that's why I did not become a co-founder of EthCore.
[24:43] Another story, we can go into this if you want.
[24:45] You know what happened after that.
[24:47] But there are many reasons. We are part of it.
[24:49] I think also him and Ming didn't really get along too much.
[24:52] There was not really a trust relationship going on.
[24:55] Of course, money running out, different visions of how Ethereum should evolve technically and economically, if you want, all played a role.
[25:04] But I think it was just one part that the C++ client wasn't used that much.
[25:08] And the reason for that was Geth being audited and launching without an audit for the C++ client.

**SPEAKER_02:**
[25:12] Yeah. I mean, talking about features, so many things happened, right?
[25:17] You know, Gav had this period of incredible productivity between that December and that April of getting from nothing, you know, just having the white paper, all the way through to having a working client, you know, having the yellow paper.
[25:27] As you mentioned, you know, there's this diagram showing how Whisper and Ethereum and Swarm were intended to fit together.
[25:35] And I found some more timing on that.
[25:37] Swarm was envisaged by Daniel Nagy as far back as 2011.
[25:41] You know, it was a year—an idea he'd been working on for like three years before that.
[25:45] I spotted on the Whisper presentation that Gavin did that that was a pre-Ethereum idea as well.
[25:51] So it was probably only when all of these people came together, it was like, "Well, you've got this storage idea, you've got this blockchain kind of like CPU/database-y idea, oh, and then if you have messaging..."
[26:02] You know, all of these things can fit together.
[26:04] But it's also, we're going to build our own IDE as well.

**SPEAKER_00:**
[26:07] Browser, yeah, plus the Mist browser, the complete thing.
[26:12] It's a complete platform for decentralized applications, end to end.
[26:16] This was the big vision, and also this was what attracted me to it.
[26:19] I mean, having someone having a really broad vision of a new internet, if you want.
[26:24] That's what he called Web3. That's where the term comes from, because it was not just a little tool.
[26:29] It was a complete new internet called Web3, from data to messaging to smart contract blockchains, to IDE, to browser.
[26:37] And this vision was very, very attractive.
[26:40] This attracted all the talent and the developers because they loved building that.

**SPEAKER_02:**
[26:45] Yeah, I mean, it's a very, very expensive vision.
[26:48] And yeah, it was, you know, Gav, as you say, you know, Web3 was him.
[26:52] Prior to that, the language I saw was really about Bitcoin with smart contracts.
[26:57] You know, that was really sort of the genesis of the idea, going through that journey of colored coins and master coins and meta protocols.
[27:06] Um, and that kind of positioning of Bitcoin as a calculator and Ethereum as a smartphone.
[27:12] But it was all that kind of like blockchains and applications, right?
[27:15] It wasn't that full Web3 vision, which I think really came from Gavin.

**SPEAKER_00:**
[27:19] We have to attribute this to him.
[27:21] He was having this big vision.
[27:23] This attracted also so many people.
[27:25] It attracted also even the business people.
[27:28] They could now understand what it actually is.
[27:31] Other than this was just like tech.
[27:33] Let's see.
[27:34] But this is like a broad vision of how businesses function, how this new financial world would happen.
[27:39] They could understand this far better than having this iPhone-calculator comparison. This was maybe a nice technical thing.

**SPEAKER_02:**
[27:47] Yeah.
[27:47] Yeah.
[27:48] But then for it being a very expensive vision, that's a lot of work.

**SPEAKER_00:**
[27:51] Sure.
[27:52] But I just started somewhere.

**SPEAKER_02:**
[27:53] That's it.
[27:54] So, I mean, you know, talking about Gavin, the features.
[27:57] So, yeah, there's a ton of stuff on that C++ team.
[28:01] Aleph, Aleph Zero as well.
[28:04] And Aleph One.
[28:05] So Aleph One being the GUI miner.
[28:09] And then I know, how would you describe Aleph Zero?

**SPEAKER_00:**
[28:11] Kind of the first interface to the blockchain in some way, like the first graphical interface to a blockchain client.
[28:18] And what could it do?
[28:19] Of course, it could mine.
[28:21] You could deploy a smart contract.
[28:23] You could visit, make it visible somewhat what's happening there.
[28:27] It was not really end-user friendly in any way, but it was just a replacement of what people just do on the command line.
[28:34] Usually on the command line, your client has some input, has some output.
[28:38] And it was the first kind of graphical user interface, a graphical user interface replacing the command line.

**SPEAKER_02:**
[28:44] I guess it's sort of like a combination of like what you have with a block explorer now, apart from that's a view-only, and this was both a view and a do.
[28:54] Yeah.
[28:55] But yeah, those GUI clients.

**SPEAKER_00:**
[28:56] But much more influential was the Mist browser.
[28:59] The Mist browser, I think there's a video by Alex van de Sande.
[29:03] It's like a 10-minute video on YouTube.
[29:05] They had this prototype.
[29:07] It was not working yet, but "fake it 'til you make it."
[29:10] The vision of the Mist browser.
[29:12] And this also really made us understand how Ethereum could work for the end user.
[29:17] Having different identities connected to wallets, and you would load those dapps.
[29:21] Is it an IPFS hash or even over Swarm one day, the app was loading and you could do some finance stuff there.
[29:30] This gave us an idea of what Ethereum could be.
[29:32] So you have to think, Vitalik gave us a rather technical vision and broad intellectual thing, but Gavin gave us this broad internet vision.
[29:41] Alex van de Sande gave us this very concrete thing what an end user could do with that in the next six to 12 months, maybe.
[29:48] It's very important.

**SPEAKER_02:**
[29:49] Just yesterday, actually.
[29:51] So there was an announcement from Uniswap about them sort of turning on fees and doing various things that are more kind of to do with, you know, the company and the protocol tying together.
[30:01] And I saw a reaction to that saying, you know, "Well, I'm never going to use this again.
[30:06] You know, you can't like extract ongoing revenue out of a protocol."
[30:11] And this person then said, um, "It's time for Mist 2. Totally.
[30:16] We need the full vision so that you've got hosted dapps and you don't need a server and you don't need a company and you can just make this pure, you know, immutable smart contract wrapped in a UI that's all decentralized."
[30:29] You think we could have a Mist 2?

**SPEAKER_00:**
[30:31] I would love to see this.
[30:32] I heard people thinking about this before.
[30:35] I don't know if anybody really started the project, but...

**SPEAKER_01:**
[30:37] It should be totally doable today.
[30:39] It's not rocket science, you know.
[30:41] Um, let me interject. We ourselves have made sort of different attempts at this where like you just download the app from the chain itself, pretty much.
[30:48] Um, it worked fine.
[30:50] And I guess it just wasn't as much a differentiator.
[30:53] Like it made things a little slower to do it this way all the time.
[30:57] I also think like one of the people that took the Web3, the world computer vision sort of seriously was like the Internet Computer people.
[31:05] And I don't know anyone that uses Internet Computer, but like every once in a while I see tweets about it and I'm like, "That sounds great.
[31:12] Yeah, start the app from the chain."
[31:14] You know, it's got some cool like smart contracting language in it.

**SPEAKER_00:**
[31:16] Yeah.

**SPEAKER_01:**
[31:17] I guess there's just no demand if it like slows the app down even slightly.
[31:22] Um, and I think MetaMask and then many other wallets were sort of enough.
[31:26] Still not the whole thing, but yeah, I guess it's like you got to get people to use it if you want it to be maximally cypherpunk too.

**SPEAKER_00:**
[31:33] I fully agree. And I mean, the problem with this is you only need it if you really need it.
[31:39] Meaning if Uniswap failed, the interface is not there.
[31:43] It's like a backup.
[31:44] It's not what you want to use daily.
[31:46] And if you remember, when they presented MetaMask, my first thought was, "Oh, this is totally away from the vision.
[31:54] Like, how can you not run a full node? How can you dare to just serve over RPC with Infura?"
[32:01] Like, it was almost not a scam, but it was not what we intended to build.
[32:05] Today, it's like this is the decentralized version of it.
[32:08] This is like non-custodial.
[32:09] MetaMask are the good guys compared to all the others.
[32:14] Like, see how the view shifted over the years.
[32:18] Like, then it was absolutely required to run a full node with the Mist browser.
[32:22] This is how it's done.
[32:23] And now we have MetaMask plus Infura.
[32:26] And today, this is really the version which is viewed as the original non-custodial Ethereum vision.
[32:32] How things are shifting, basically.
[32:35] But yes, you only need those things if things are falling apart.
[32:38] Just as an example, so many people use the Gnosis Safe.
[32:42] Let's say the Gnosis Safe UI is gone.
[32:45] Technically, it shouldn't be a problem to run another one, but it really needs to be something on IPFS.
[32:51] It needs to be something which can self-host so I can still access my wallet without going to the command line.
[32:57] So for those reasons, you need it.
[32:59] And the Mist browser was thought of as the fallback for every dapp.
[33:03] Like, of course, you can have your application run on a normal .com domain on AWS, fine.
[33:08] But if you could serve the same app in a decentralized fashion as a backup, this would be great because you could still use it if the company behind Uniswap, the company, fails.
[33:17] If someone builds a nice Uniswap UI served by IPFS, directly interacting with the smart contracts.

**SPEAKER_01:**
[33:23] Yeah, that's fair.
[33:24] Also, Uniswap, I think, is controversial.
[33:26] I know Jim wanted to say something.
[33:28] Controversial because they had the company-level fee skim, and then I think they've turned the on-chain fee on.
[33:33] I don't know that they've turned the company fee off.
[33:35] I haven't read that in detail.

**SPEAKER_02:**
[33:37] I believe so, because one of the replies was saying, "Okay, so how are your shareholders going to like that?"

**SPEAKER_01:**
[33:41] Yeah, okay, fair enough.
[33:43] Well, hopefully they hold a bunch of the UNI and it will mark the market.

**SPEAKER_02:**
[33:46] They're doing a bunch of burns, so that should be to the benefit of all stakeholders.
[33:50] But yeah, just sort of this interesting kind of contrast, right, between completely immutable, you know, force of nature smart contracts versus, you know, more permissioned, more tied to a company, more sort of like wanting to have fees for maintenance kind of question.
[34:07] I mean, it's like treasuries, I guess.

**SPEAKER_00:**
[34:08] But this opens up the question, how should an Ethereum app be built economically?
[34:14] And this is also a question being answered during that time.
[34:17] The DAO was one approach of, it should be fully on-chain.
[34:20] All the revenue should be on-chain.
[34:22] There should be no for-profit entity directly attached to it.
[34:25] And Slock.it, the company I built after that, would be a service provider for them, getting paid by them for work being done for the DAO.
[34:33] That's one version.
[34:34] I was always skeptical and still am about companies where you have effectively two cap tables, meaning you have a token cap table, if you want.
[34:42] Of course, it's a utility token, governance token, and so on.
[34:45] But effectively, it's kind of ownership in the protocol.
[34:49] And then you have a for-profit company with shareholders.
[34:52] And this is always, I think, very dangerous because you don't know where it's going into.
[34:57] Where's the value?
[34:58] On the shares of the company or on the token?
[35:01] This was the main reason all those companies had those nonprofit foundations in Switzerland.
[35:06] Rightfully so, because they said, you only want to have one cap table, like the Ethereum Foundation.
[35:11] There were no shareholders of Ethereum.
[35:13] There was a nonprofit foundation and a token.
[35:16] The token, if you want to have a share in the economic success of the protocol, you would buy Ether.
[35:21] And so later on, there were many other token projects where they had a nonprofit foundation, so no shareholders, no second cap table, and then you would have only the token and all the value would be there.
[35:32] And now with Uniswap, you have this problem of having again shareholders and tokens, and I think that's dangerous and not a good idea actually.

**SPEAKER_02:**
[35:40] Yeah, yeah.
[35:41] So perhaps let's talk about DevCon, actually, just before we get to DevCon 1.
[35:46] So the launch.

**SPEAKER_00:**
[35:47] Right.

**SPEAKER_02:**
[35:48] So obviously, a lot of testing and coordination and this different series of proof of concepts.
[35:54] So I mean, how did you know it was good enough?
[35:57] Like, what was that testing flow and collaboration like?

**SPEAKER_00:**
[36:00] There are many indicators. One being the Olympic testnet running smoothly for a while.
[36:05] Other one was the Geth client having an audit which worked.
[36:09] Um, and then they were saying, "Okay, now if Christoph doesn't find any failing tests for like three weeks or four weeks or something, we are ready."
[36:17] And this was the case.
[36:18] And so we said that we can set a launch date.
[36:21] The launch itself, it's also a bit typical. Typically Gavin or also Vitalik, nobody wanted to push a button.
[36:28] Like nobody just wanted to start the chain.
[36:30] So what was done was there was a script written which has as an input parameter the hash of the Olympic testnet at a certain block height.
[36:39] So everybody could, using this script plus the software, plus the C++ or Go client, of course, having plus the hash, which was at that time in the future of the Olympic testnet, start the chain.
[36:52] So there was no—at launch day, we were just viewing it.
[36:55] There was nothing to be done.
[36:57] It was like, everything was, all the information was out there.
[37:00] People were just simultaneously starting the blockchain.
[37:03] And then over the peer-to-peer network—this was actually the more harder stuff—they found themselves on Reddit and others to share IP addresses, like, "Connect to my peer, connect to my peer."
[37:14] And so then they started to come together. And of course, the longest chain was the valid one.
[37:18] So as soon as you found a peer which had their own chain, you would say, "Yes, this is a longer one." You would stop and start mining on top of his chain.
[37:26] And so basically the canonical chain emerged from that within, I don't know, 30 minutes or one hour.
[37:32] And then we had the chain running. And this was like a beauty to behold.
[37:38] Like to just see how this works out as intended, completely decentralized.
[37:42] Nobody did have to do anything.
[37:44] I was in the C++ Berlin office in Kreuzberg, 37a, with a nice office, and we just watched it.
[37:55] And we were somewhere mining there with a laptop.
[37:57] And we were all excited as it started.
[38:00] I actually think two or three weeks after, or maybe four, we had the first little hard fork, meaning there was some smart contract doing something that Geth and C++ had a different result.
[38:13] It was, for me, almost the middle of the night at 10 PM or 11 PM.
[38:17] So I remember seeing this, looking for one hour or so, finding what the issue was.
[38:22] Then I found it, wrote a test about it.
[38:24] C++ was right.
[38:26] Geth was wrong.
[38:27] So we gave it to Jeff.
[38:28] They fixed this.
[38:30] I think we said one hour and like after five hours, everything was done.
[38:34] It was a basic call that the miners please update your client.
[38:37] Um, so, and then it was fine.
[38:39] So this was the early days, but it was a successful launch.

**SPEAKER_02:**
[38:42] Nevertheless, did the Haskell client sync at Genesis?
[38:46] I do not know, Jim.

**SPEAKER_04:**
[38:47] No, we were able to sync at Genesis time for like a year or so. We were syncing.
[38:52] But I remember like that week, Kieran and I were like more interested in trying to get a miner in place.
[38:58] So that was what that week looked like for us.

**SPEAKER_01:**
[39:00] Yeah, I was living in an apartment just south of Berkeley campus at this time.
[39:04] And Jim had taken me to Fry's to build a machine a few months prior, like a build machine.
[39:09] It had a good GPU in it.

**SPEAKER_04:**
[39:11] Yeah, Fry's is dead now.

**SPEAKER_01:**
[39:12] RIP.
[39:14] So I was running a miner there, and we built a couple in Jim's garage.
[39:17] It got very hot in Jim's garage, which was, you know, those things were consuming a fair bit of power.
[39:23] Mine exploded after a few weeks.
[39:25] It was actually just the power supply.
[39:27] So I thought the whole machine was bricked, and Jim said, "You know, I think everything but the power supply will be okay."
[39:32] And it was the case that everything but the power supply was okay, but then I stopped mining.
[39:36] And I think Jim would shut it.

**SPEAKER_04:**
[39:37] We didn't even bother to buy cases at that time.

**SPEAKER_01:**
[39:39] Right.
[39:40] Yeah.

**SPEAKER_04:**
[39:40] You may have had a case.
[39:42] I had mine just sitting with wires out.

**SPEAKER_01:**
[39:43] Yeah.
[39:44] Yeah.
[39:44] Indeed.
[39:46] Sure.
[39:46] At that time, we were always, you know, sort of, at least at that time, shorter-handed people-wise.
[39:52] So it was catching up a little bit on the features, et cetera.
[39:55] But it ran perfectly well.

**SPEAKER_00:**
[39:56] There were always new features coming.
[39:58] I remember, it was like we—one of the sweet memories during the pre-launch—sitting together with Gavin, Vitalik, Jeffrey, and me in one room at the C++ office, like the nice Gavin office.
[40:10] He had this '80s style thing.
[40:12] And we'd think, "Okay, what was wrong in our protocol?"
[40:15] Then they discussed on the whiteboard changes.
[40:17] Then the first day, "Okay, Christoph, you write a test for this protocol change."
[40:21] Then we are, at the same time, we are coding it.
[40:24] "Okay, you're done creating a test? Let's see if they all pass it."
[40:27] If they all pass it, it's done, a new feature, a direct new release.
[40:31] And so this was done with all the other clients.
[40:33] So they basically had to catch up.
[40:35] It was like information, update of the yellow paper, here's a new test, here's like a little Etherpad description of what the new protocol looks like, and then please update your clients.

**SPEAKER_04:**
[40:44] But the yellow paper got me to a certain point.
[40:48] Sorry.
[40:48] The yellow paper always got me to a certain point, but it was always behind the other clients.
[40:53] So I would always find out that I was behind because I went in the morning and connected to the testnet and I was no longer connecting or I was getting some state mismatch or something.
[41:03] And then I'd have to go and dig through, usually the C++ client.
[41:07] I think there was maybe one or two times where I can't remember why.
[41:11] I think there was one or two things that went to Geth first, but usually it was C++.
[41:16] And I'd have to go digging through the newest code to find the changes and then bring them in.
[41:21] And then a few weeks later, I'd see it in the yellow paper.

**SPEAKER_02:**
[41:23] Yeah.
[41:24] Yeah, so unlike what you have now, where leading into a hard fork, you know, you've got all that discussion and spec-ing up front and applying the code into the clients, but only enabled for a testnet and going through that dance and then ready to go.
[41:36] Yeah, I mean, at that point, as you say, it's kind of done in those clients first and then backported later.

**SPEAKER_04:**
[41:42] It looked like from where I was standing, it looked like there was a lot of competition between the different clients and the developers there.
[41:49] And I think they sort of took pride in having the new thing in as fast as possible.
[41:54] And so that sort of led to an environment maybe where there was not as much discussion. It was like, "I'm going to throw it in and then I get the bragging rights."

**SPEAKER_00:**
[42:01] There was always a fight between the Geth and C++ team about who's the best.
[42:05] And Gavin was having a big ego.
[42:07] And Jeff was more like, "Just give me the new spec.
[42:09] I'll just code it."
[42:10] But yeah, it was more or less this decision by the three of them.
[42:14] I was basically not playing a very major role.
[42:16] I was in the room and then writing a test for it.
[42:18] But they discussed it.
[42:20] After it was cleared, they just did it.
[42:22] But it was pre-launch.
[42:24] After launch, of course, this was different.

**SPEAKER_02:**
[42:26] Saying about having...
[42:27] Sorry, go on, Jim.

**SPEAKER_04:**
[42:28] Oh, I was just going to say, like, I know a lot of the changes were just like some change in the EVM or pricing or something.
[42:35] And so often it was like, you know, I would freak out in the morning when it wasn't working.
[42:39] But then, like, by 11 o'clock a.m., I had found, like, "Oh, I see, like, such and such opcode just doubled in price or something."
[42:47] So I would just put that in.
[42:48] But the big one was RLPx, which is essentially like a big SSL replacement.
[42:55] And that one was like freaking me out for a couple of weeks.
[42:58] I was like digging around, trying to find any information about that.
[43:01] Eventually, I had to reverse engineer.
[43:03] Maybe that was the one that was in Geth first.
[43:05] I can't remember.
[43:06] But I had to sit there and reverse engineer.
[43:08] I had to run either C++ or Geth and then put lots of logging information in to see what in the world was happening and then print out all the stuff and then find the appropriate crypto libraries to mimic that.
[43:20] What was the background on that and how it went in so quickly?

**SPEAKER_00:**
[43:22] Like there was nothing in the yellow paper about that at all, and when that came in, it was just a shock to me.
[43:27] Do you know which time this came?
[43:29] Because I was focusing on the Ethereum Virtual Machine at the time.
[43:32] This was more like, okay, I know Gavin, I think it was Gavin doing some optimization.
[43:36] He was always thinking about the long term.
[43:38] So if something would be 10% more efficient, he had to do this, right? I think...

**SPEAKER_01:**
[43:42] I remember like there was a devp2p, libp2p website that was released about that time.
[43:48] It still might have been after the giant change went in.
[43:51] So I also, we were working together regularly, you know, in the Bay Area at this time.
[43:55] And I think Jim did like 96% of the changeover, but we had at the time like separate processes.
[44:03] One was more like a client and more like a server. We merged them later.
[44:06] Um, and yeah, it was like... so there was a big document describing like how the DHT for peer discovery would go in.
[44:16] But then you needed like a way to identify the peers, maybe.
[44:19] And this system kind of gave them an identity with like a, you know, in a SSL style.
[44:26] Like basically there was like a node cert, in effect, and then you had to, like, there were session keys and, you know, this, that, and the other.
[44:33] It was—it took a long time to implement that thing.

**SPEAKER_02:**
[44:36] Um, but yeah, I think, um, maybe Bob, you would know that. I think this was someone else wrote this big thing. This might have been Alex.
[44:43] Yeah, it was Alex who did that.
[44:45] Um, so saying about sort of documentation or whatever, there was a wiki, right?
[44:49] It was an Ethereum wiki, and a number of things were documented only on the wiki.
[44:53] Um, and I think these kind of wire protocol pieces were part of that.
[44:58] But yeah, Alex Leverington was the first hire into that Berlin office, um, and he primarily—I mean, he worked on a few different C++ things, but the main thing he's known for is devp2p, which was that common underlying peer-to-peer protocol.
[45:12] Though you already had libp2p, which is the transport for IPFS, that already existed at the time.
[45:17] So there was a bit of "not invented here" going on.
[45:20] Um, but yeah, he was there for DevCon 0 as well.

**SPEAKER_00:**
[45:24] And he spoke. I remember Alex.
[45:26] I was not too much into the peer-to-peer side of the code base.
[45:29] I was more into the EVM and Solidity, smart contract side.

**SPEAKER_02:**
[45:34] I tell you what, there was a bit of funny crossover with the later part of yours, was Alex Leverington worked with John Gerrits on a project called Airlock.

**SPEAKER_00:**
[45:46] So, I remember that. I saw it later, like after we did our presentation and had Slock.it and stuff going.
[45:52] They showed us videos of it earlier than us. So yes, they were actually, time-wise, they did this before we did, but I did not know about it at all.
[46:00] And so we did it more or less in parallel then.
[46:02] And we just launched a bit quicker, like to go to the public with the project.
[46:06] It has been—from their side was more like a little side project, it looked like, not a big company or intended to be.

**SPEAKER_02:**
[46:11] Yeah, I remember this project.
[46:12] So I think that was at the hackathon at the Bitcoin Expo in April 2014 that they did that.
[46:19] And Stefan actually did an interview with them.
[46:21] You can see that on YouTube. You know, this is like talking about early Ethereum projects, you know, and this is like a over a year before the mainnet.
[46:30] It's so far back, some of these.
[46:32] Um, but yeah, like some of that spec stuff was not in the yellow paper and it was just sort of floating around, and a long time before there was real consolidation of that full client spec.
[46:42] But you managed to do it anyway, Jim. You managed to build the client.

**SPEAKER_04:**
[46:45] It was a busy week.
[46:46] But it was just notable to me because at least from what I was seeing, it went from zero to one overnight.
[46:52] I had never heard of it the night before, and then the next morning it was in the clients and working, and I couldn't connect to anything.

**SPEAKER_01:**
[46:59] Which is normally the pattern, but yeah, just this one was like the biggest one-time change that I can recall either.

**SPEAKER_00:**
[47:04] Yeah, yeah.
[47:05] Again, this was pre-launch days.
[47:07] Things had to move fast.
[47:08] There was a lot of pressure going around.
[47:11] It was messy.
[47:12] There was not much coordination between the clients, except for maybe some Skype groups.
[47:16] And in the end, yes, Vitalik, Gavin, and Jeff just made decisions and executed as quick as they could.
[47:22] So this all changed after launch. Then things became a bit slowed down and people consolidated, and every change was a big thing, rightfully so.
[47:30] Um, yeah.

**SPEAKER_02:**
[47:31] Yeah. So back on the timeline, um, so it was July 2015 that mainnet launched with the Frontier hard fork.
[47:40] Um, and then as you touched on, you had Ming.
[47:43] So Ming's first official day was the 1st of August 2015, at which point the foundation had been running on for a year or so and was close to out of money.
[47:54] Touching on your thinking it would only last for a certain amount of time, a year on, that raise, which I think was around $16 or perhaps $18 million, was nearly all gone.
[48:04] So you had these quite hard decisions about what...

**SPEAKER_00:**
[48:05] ...which part of this grand vision was going to be funded initially, right?
[48:10] And I remember talking to her at the time, she felt like, "I have to clean up the whole mess."
[48:14] Like the paperwork and everything was totally messy, working with lawyers, accountants, and so on, and getting a cleanup basically of the foundation.
[48:22] I mean, for me, I did expect it to last something like that.
[48:25] So for me, it was clear they are not making any money.
[48:28] Um, I didn't know like how big the reserve was in detail.
[48:31] I think it was like, I don't know, 5% something in this range, like how much ETH the foundation held at the time.
[48:37] There wasn't that much value either. Price was like 50 cents, one euro or something.
[48:41] So it was clear this would not last forever.
[48:44] So I was thinking about going back to my PhD, or then I came across this idea about Slock.it and building a company.
[48:52] And Slock.it was the idea of—maybe similar to Airlock—smart contracts are essentially permission systems.
[49:00] 90% of a smart contract is who's allowed to do what.
[49:04] In case of the ERC-20, it's just who's allowed to send the token or setting an allowance.
[49:09] And in terms of the DAO, it's who can vote for what and make decisions, and then money gets sent.
[49:15] So what if we could put this permission system into IoT?
[49:19] And who's allowed to switch on, off, use, change, admin rights, whatever.
[49:24] You put this into a smart contract.
[49:26] And I thought that Ether will never become a currency.
[49:29] Bitcoin was a digital currency.
[49:31] And actually, if you talk to Ethereum people at the time, we were not thinking about competing with Bitcoin.
[49:36] Bitcoin was a digital currency.
[49:38] We were building a platform for decentralized applications.
[49:41] Ether was just used to run it.
[49:44] I once heard the statement somewhere on Twitter where someone said, "Bitcoin is a currency which needs a blockchain to function, and Ethereum is a blockchain that needs a currency to function."
[49:55] This is, I think, very true.
[49:57] And so back then, I thought, okay, Ether will not be used as a currency, but it might be used as a currency for IoT devices.
[50:06] So instead of the Internet of Things, building the Economy of Things.
[50:11] And this is kind of what drove us.
[50:13] And then we wanted to build this universal sharing network as an application.
[50:17] At the time, Uber and Airbnb just became big.
[50:20] We thought, well, all those sharing economy services should run on-chain.
[50:24] So let's build this called the universal sharing network.
[50:27] And then we thought about how to start with something tangible.
[50:31] And then we had this door lock.
[50:33] Actually, it's here in the background.
[50:35] If you see it, it's there.
[50:37] I have this DevCon 1 physical smart lock, which we connected to the Ethereum blockchain using our own software, and had this idea of people pay to open the lock.
[50:47] And that's what we presented at DevCon 1, together with this idea, which actually only came up like three or four days earlier, to connect this with a DAO.
[50:58] And the rest, you know the history what happened after that.
[51:01] But we didn't intend and we didn't start Slock.it for building a DAO.
[51:04] We wanted to build a universal sharing network.
[51:06] Then we thought, "Well, this is way too big for us. We want to now focus on this Airbnb use case for door locks."
[51:13] And then we thought about fundraising.
[51:15] We talked to a bunch of VCs.
[51:16] I actually remember flying to New York, talking to VCs there.
[51:20] Everybody said no.
[51:22] Then I met Joseph Lubin.
[51:23] He said, "Yes, maybe under some conditions."
[51:26] We just did not agree on the terms in detail then.
[51:29] But I was presenting at the Bitcoin meetup in New York.
[51:32] And they all—the first application was a Bitcoin application about arbitrage trading.
[51:37] It was kind of boring.
[51:39] And then I came with a door lock.
[51:40] It was super fascinating.
[51:42] You could open the door by paying some Ether.
[51:44] So it went well, but we didn't have any money.
[51:47] So we thought about doing something like an ICO, but this was now after the launch of Ethereum.
[51:52] So if I started coding an ICO-like smart contract, why should we have the money directly?
[51:58] It could stay in the contract and then people could vote for giving us part of it.
[52:03] We said, "Well, we could make proposals to it and then they can vote if the proposal is good or not."
[52:08] Then the money would be released to us.
[52:10] Then we thought, "Why could not everybody make a proposal?"
[52:13] Like everybody could pay in, everybody can make a proposal, and so it's completely open, and we are just one of many service providers to the DAO, building this universal sharing network.
[52:23] And this was the origin of The DAO.
[52:25] And only like, again, three days before DevCon 1, we actually decided we would go for it and put it into the presentation.

**SPEAKER_02:**
[52:32] Yeah, amazing.
[52:33] I mean, so on the timeline again, trying to judge it.
[52:36] So Stefan was, I guess, Chief Communications Officer or Community until September of 2015.
[52:44] That's when he left.
[52:45] Had you left already by then? Can you remember?

**SPEAKER_00:**
[52:48] No, I didn't really leave because I was technically a freelancer, although I was working full time for it.
[52:53] I didn't have a formal employment contract.
[52:56] So I was continuing to work, I think, until the end of the year.
[52:59] And then I just put down my hours, basically.
[53:03] If you need me, tell me.
[53:04] I just invoice what I'm doing.
[53:06] But I was really leaving actually in December, January.
[53:09] I think the last invoice was for December.
[53:11] And when Stefan Tual left or was being left—there's another conversation how he left the foundation.
[53:18] He didn't agree with some people getting Ether, which is another story for another day, I guess.
[53:23] But he was really a crucial part in building up this Ethereum community.
[53:27] Like all this meetup culture.
[53:29] The meetup culture didn't really exist like that before.
[53:32] He was going from place to place, finding someone running meetups.
[53:36] So he was very important for that.
[53:38] And I know I was a coder.
[53:40] I was with Simon, who I co-founded Slock.it with, was also a coder.
[53:44] We needed someone who can talk to the people, can do marketing and this stuff.
[53:48] And we said, "Well, he has the right address book.
[53:51] He knows the right people.
[53:52] Everybody knows him in the community.
[53:54] I think let's ask him if he wants to join us."
[53:56] And he did.
[53:58] And I think he was a very important part of making The DAO what it was.
[54:02] Later on, he did some messages, which I also didn't like.
[54:05] And so he was a bit in disgrace after what happened then.
[54:08] And I think the community was very, very hard with him because he was not always reacting maybe as he should in some situations after the hack.
[54:16] But nevertheless, he played a very important part in the history of Ethereum and also, of course, of The DAO.

**SPEAKER_02:**
[54:22] And so, so DevCon was November 2015. So that was announced earlier in the year, I think September-ish, but ended up being canceled, you know, because the foundation were basically, you know, this running-out-of-money piece.
[54:38] Uh, but then primarily with ConsenSys funding and support, uh, you know, "Hey, it's back on."
[54:43] Um, so that was in, that was in London.
[54:46] Um, and you know, significantly larger event, obviously, than DevCon 0 because it was the first, you know, public Ethereum outing with Microsoft as a headline sponsor.
[54:59] You had Nick Szabo speaking as well.
[55:02] Maybe Satoshi, maybe not Satoshi.
[55:04] I don't think he said that.

**SPEAKER_01:**
[55:05] He strongly alluded to it in the presentation.
[55:07] It was funny.

**SPEAKER_02:**
[55:09] So, yeah, how was that for you then, Christoph?
[55:11] What was, you know...

**SPEAKER_00:**
[55:12] It was totally different than DevCon 0 because this felt like now we're going out in the world and show it to the public.
[55:19] It was a fancy space in London.
[55:21] It was a really fancy, almost cathedral-looking space to present in.
[55:25] Again, we had Vitalik and Gavin talking about the vision of Ethereum.
[55:30] And if you look at the talks being given...
[55:33] I really think entrepreneurs today should just re-watch them because they all have been 10 years too early.
[55:40] Be it about Uport building identity solution.
[55:44] I think it was Boardroom doing governance on-chain.
[55:47] Many, many ConsenSys startups, of course.
[55:50] We as Slock.it thinking about, "Well, let's connect IoT to blockchain."
[55:55] Again, all of that 10 years too early.
[55:58] I remember also Simon speaking about—not my brother, I forgot his last name—but Simon speaking about everybody getting a token.
[01:00:05] He really predicted this token economy would now thrive, which happened.
[01:00:09] So it was a great place to be.
[01:00:11] Everybody was looking into the future, building the future.
[01:00:14] It was very, very exciting.
[01:00:16] It was very important that ConsenSys was funding this.
[01:00:19] It was crucial, this DevCon 1 moment showing Ethereum is live now.
[01:00:24] We show you what we will build with it.
[01:00:26] But still, there were no applications running.
[01:00:28] It was all visions and thinking.
[01:00:31] And so there's one reason why when we then did The DAO, The DAO was hailed like almost the first real thing you could do with Ethereum.
[01:00:38] That's why so many people jumped onto it.
[01:00:41] And then maybe just finishing this off, the narrative changed.
[01:00:44] It was not anymore a DAO for the universal sharing network, but maybe because of the curators we chose, which were like important figures in the Ethereum space and many other things, it turned into like an investment fund or like an index fund for Ethereum applications.
[01:01:03] Because now after 20, 30, 40 million was in, it was clear this was not just money for Slock.it and the USN.
[01:01:09] This was money for more cases and more people applied for it.
[01:01:13] It became like every decentralized application, or many of them, not everyone, they were saying, "I'm applying for getting funding from The DAO."
[01:01:21] So The DAO would pump all the applications.
[01:01:24] So it's like you invested in Bitcoin 10, five years ago, became rich.
[01:01:28] Now you invest into Ether, went well.
[01:01:30] And now you can invest in the application layer.
[01:01:33] You do that through putting money into The DAO.
[01:01:35] This was not a story we told, not how we intended it, but that's how the narrative changed during the fundraising and then became that big.

**SPEAKER_02:**
[01:01:42] Yeah, I mean, it was interesting you saying that you did, but I cannot hear you.

**SPEAKER_00:**
[01:01:45] Maybe it's just me.
[01:01:47] Can you hear me?
[01:01:48] I mean, I am sorry.
[01:01:50] I have an issue here with my...

**SPEAKER_02:**
[01:01:51] You do?

**SPEAKER_00:**
[01:01:52] This is me.
[01:01:53] So now I'm back.

**SPEAKER_02:**
[01:01:55] Can you hear me?
[01:01:56] Can you hear me, Christoph?

**SPEAKER_00:**
[01:01:57] No, I have to switch back to, um, let's see. Can you hear me now?
[01:02:00] Yeah, I can hear you. I could always hear you.
[01:02:02] For some reason, I couldn't hear you anymore.
[01:02:03] This was like me an hour ago, by the way. StreamYard... okay, my audio is completely broken.
[01:02:08] So I will try to fix this. We can continue.

**SPEAKER_04:**
[01:02:10] I basically had to close it and come back again with my earphones, but I don't know.

**SPEAKER_02:**
[01:02:14] Perhaps while we're waiting, Kieran and Jim, you could talk a little bit about the Strato launch.

**SPEAKER_04:**
[01:02:18] I thought you were going to say, "You could sing a little song."
[01:02:20] I got nervous for a second there.

**SPEAKER_01:**
[01:02:22] You know, okay, so in this period of time, we were just reconnecting.

**SPEAKER_00:**
[01:02:26] Just turn it off and on again.

**SPEAKER_01:**
[01:02:28] We were working as part of ConsenSys and one of the kind of marketing, business development people at the time, Andrew Keys, primarily had put together a partnership with Microsoft.
[01:02:39] I don't know if they ended up co-sponsoring DevCon 1 per se, but their headline...
[01:02:45] Yeah, they—so they put money in for that because they also paid for a bunch of PR and all those sort of things too.
[01:02:51] Um, and so we had maybe a month or two lead time to work with them.
[01:02:55] Um, and so the idea was that we, you know, they've got cloud infrastructure, it's a good place to run blockchain nodes.
[01:03:02] They also have corporate clients that were actually very interested in the technology.
[01:03:06] And so we worked with them pretty closely in the run-up to make our software available on the Azure cloud, as did Roman of the Java client, which to some extent was everyone's preference because people know Java in the enterprise world.
[01:03:22] But I think we sort of stuck with it quite a bit longer than Roman did.
[01:03:27] And you know, so Blockchain as a Service was the big announcement.
[01:03:31] Was this December 2015? No, it was November. It must have been December really. November.
[01:03:37] Uh, there was a—once the announcement happened, there's a little tick in the Microsoft stock price, which we were like, "Whoa!"
[01:03:43] Like there's a little bump there.
[01:03:45] And a lot of excitement for sure.
[01:03:48] Got a million phone calls after that.
[01:03:50] That was like a good feeling of being the hotness that only happens so many times in someone's life.
[01:03:55] But tremendous interest on the back of the Blockchain as a Service announcement.
[01:03:59] We did a live demo.
[01:04:01] It was fun.
[01:04:02] The internet gets in vogue to make fun of the UK these days on X, et cetera.
[01:04:08] The internet in the conference facility was not so good.
[01:04:11] So I was very worried about the transactions actually going through.
[01:04:14] But they did during the live demo.
[01:04:16] I think there's footage of it somewhere.

**SPEAKER_02:**
[01:04:18] Can you hear us again now, Christoph?

**SPEAKER_00:**
[01:04:20] Yes, I can hear you.
[01:04:21] I hope you can hear me too.

**SPEAKER_02:**
[01:04:22] Okay.
[01:04:23] So the demo that you did at DevCon 1, again, another iconic event, because yeah, you had that physical smart lock just sitting there on your shelf, and you know, it rotated, right?
[01:04:36] You did your transaction.

**SPEAKER_00:**
[01:04:37] We just had a Raspberry Pi connected via, I think it was Zigbee or Z-Wave back then, to the door lock.
[01:04:44] And on the Raspberry Pi, we had actually an Ethereum client running.
[01:04:47] And we had a smart contract on-chain where you could send some money to it, or Ether actually, and when it received some Ether, it would open up.
[01:04:55] This was basically the demo.
[01:04:57] But it was cool to see something physical, um, using Ethereum for, as I said before, the Economy of Things, connected to IoT devices.
[01:05:07] Since most of the people in the room are still nerds and devs, they loved that kind of stuff.

**SPEAKER_02:**
[01:05:12] And there was also the kettle, wasn't there?

**SPEAKER_00:**
[01:05:14] Yes, there was also a kettle.
[01:05:16] Maybe just turned a smart plug, like a power plug.
[01:05:19] We could also turn it on and off.
[01:05:21] Same protocol, same thing.
[01:05:23] So we just want to show it's not just a door lock company, because actually we were not producing those.
[01:05:28] We were just connecting existing door locks to it.
[01:05:30] We want to show this idea of the universal sharing network.
[01:05:34] Everything which you can turn on, off, or lock up and unlock could be now connected to this network.
[01:05:40] And everybody could put almost everything in there, like a washing machine.
[01:05:44] You pay for using the washing machine, or a bicycle lock.
[01:05:47] We even had padlocks connected to it.
[01:05:49] So you could have like your locker room and you have a padlock in front of it and sell whatever's in there by having someone pay to open the padlock.
[01:05:56] This was the generic idea.
[01:05:58] I mean, we got some VC money later after that, like in 2017.
[01:06:02] We built it.
[01:06:03] Nobody used it.
[01:06:05] It was not just too early. It was like everything for everyone all at once.
[01:06:09] And of course, nothing for no one.
[01:06:11] It felt like the app was not great.
[01:06:13] So we failed B2C-wise.
[01:06:15] At Slock.it, we then turned into more consulting projects.
[01:06:19] We built Incube, which was an IoT client.
[01:06:22] Made some money with that.
[01:06:23] Had about 50 people actually employed at the time.
[01:06:26] In 2019, we sold the company to Blockchains, Inc.
[01:06:30] Jeffrey Berns.
[01:06:32] Another story.

**SPEAKER_02:**
[01:06:33] Um, so I remember speaking to Stefan at the time.
[01:06:37] So Stefan was involved with that demo, right?
[01:06:39] It was Stefan who came up on stage to make his little cup of tea with the kettle there.
[01:06:44] But I remember speaking to him that he'd been concerned about what the reception for him would be like, you know, having had this passing of ways with the foundation just two months before.
[01:06:55] But he was saying it was all very, it was all very friendly and people, you know, were very excited about the project.

**SPEAKER_00:**
[01:07:01] Right.

**SPEAKER_02:**
[01:07:02] And saying actually about that IoT piece.
[01:07:04] So in January 2015, you had a demo that happened at the Consumer Electronics Show, CES, in Vegas, which was a collaboration between IBM and Samsung.
[01:07:13] So the aforementioned Henning Diedrich was part of that.
[01:07:16] And that again was months before mainnet, but you had a proto-Web3 stack there, which was, I think, PoC-5 of Ethereum.
[01:07:24] You didn't have Whisper, you had another thing called Telehash. And you didn't have—you had BitTorrent.
[01:07:29] So there was this proto-Web3 stack there, and they had demos like a washing machine buying its own detergent and scheduling its own repair.
[01:07:38] So, so yeah, that was happening a little earlier. And yes, I mean...

**SPEAKER_00:**
[01:07:41] So Slock.it itself did a number of these different products, right?
[01:07:44] There was something with electrical charging and something to do with toll roads.
[01:07:47] Is that right?
[01:07:48] Right.
[01:07:48] We had a prototype running with RWE or innogy in Germany.
[01:07:53] They're doing all the—a lot at the time, most of the charging stations.
[01:07:58] So this was in general, we got a lot of attention, of course, also after The DAO hack and all of that.
[01:08:04] And so that's kind of why we became a consulting company, because so many asked us, "Could we do a prototype with you?"
[01:08:10] Because there were not many Ethereum builders at the time.
[01:08:13] So we have been building on Ethereum now since one year or two years, which you could not find anybody doing this.
[01:08:20] So we were building lots of nice prototypes and some almost production stuff, and always related to IoT devices connected to the blockchain.
[01:08:29] This was a core business.
[01:08:30] And on top of this, we built those prototypes.
[01:08:33] We did a lot of work for the Energy Web Foundation.
[01:08:36] I don't know if you're familiar with them.
[01:08:38] This was in Switzerland.
[01:08:39] They are kind of a fork of Ethereum focusing on all the energy use cases.
[01:08:44] We built most of their stuff in 2018, beginning of '19, until they hired their own developers.
[01:08:52] And Gavin was also part of this a while.
[01:08:55] So, yes, this was still—I mean, if you remember this time, Kieran, you say there was so much enterprise interest.
[01:09:01] Enterprises at the time were just learning, looking into this, wanted to build prototypes, not yet production stuff.
[01:09:07] Um, so and there was a huge demand for it, for blockchain experts for doing consulting, for going to conferences, explaining to them what a blockchain is.
[01:09:15] At every tech conference, you needed some blockchain talk.
[01:09:18] And this was kept basically mostly us, and they paid sometimes like 4,000 euro for a talk.
[01:09:23] As a company, you said, "Well, we need the money, let's go there."
[01:09:26] So, of course, you also have to think about us as persons.
[01:09:29] Simon and me, we didn't get any money for almost a year.
[01:09:32] Like we worked for—we were not rich people, we come from ordinary families.
[01:09:37] And we said, "Well, we can work for like three to four months without a salary. Let's build The DAO."
[01:09:42] And then The DAO becomes big, The DAO is paying Slock.it to build it.
[01:09:45] And of course, after the hack, it was clear there will never ever be a payment.
[01:09:49] So we made zero money out of The DAO.
[01:09:52] So we needed to start doing some work.
[01:09:54] And this was in the beginning, let's do consulting for those large companies.
[01:09:58] This is how Slock.it began to survive.
[02:00:01] Many people said, "You can bury Slock.it after what happened.
[02:00:04] Your name is burned forever."
[02:00:06] And we decided to stay as a team.
[02:00:08] I mean, as a founder team, we owned our mistakes.
[02:00:11] Maybe we are open and transparent about it as much as we could.
[02:00:15] It was, of course, an honest mistake.
[02:00:17] We can talk for it.
[02:00:18] It could be another session just for The DAO.
[02:00:20] I mean, The DAO is a lot of topics.
[02:00:22] I just put here very shortly, just talking about it from a company perspective.
[02:00:26] And then Stefan, he was saying, "Well," he was trying to get VC money.
[02:00:30] Simon and I, we were doing those consulting gigs.
[02:00:33] And once we had VC money—what happened as a company was we got 2 million euros or dollars.
[02:00:39] And then we built the product, hired people for that, got more and more consulting gigs.
[02:00:44] So we always said, "Well, let's do them and just hire more people."
[02:00:48] And in the end, we had like 50 people, 5 or 10 doing the product and 40 people doing consulting.
[02:00:54] And then we got bought by Jeff Berns from Blockchains, Inc.
[02:00:58] Remember maybe at DevCon 3, I think.
[03:00:00] Four.
[03:00:01] Four in Prague, right?
[03:00:03] Wanted to build a city.
[03:00:04] I loved the vision.
[03:00:05] He obviously had money.
[03:00:07] He wanted to build it on top of Ethereum mainnet.
[03:00:10] I was thinking about how maybe I can channel those billions into the right direction, building it all as intended on Ethereum mainnet, which was working fine for the beginning.
[03:00:19] And then I found out once you're an entrepreneur, you never can be an employee again.
[03:00:25] And so I had to leave.
[03:00:27] But maybe actually it's too far in the future.
[03:00:29] I mean, that's one thing I think I have to say here, because you talked about DevCon 1 and we skipped a little bit DevCon 2.
[03:00:35] You said in DevCon 1, Stefan Tual was very concerned how people perceived him.
[03:00:40] And they were very gentle, forgiving, and nice to him.
[03:00:43] So he was well-received, and then he built The DAO community.
[03:00:47] I was super worried to go to DevCon 2 because this was after The DAO hack.
[03:00:52] I was seriously thinking someone might beat me up there.
[03:00:55] I went to the corner and I almost destroyed Ethereum with this fork and so much attention to it and all the money lost for some people, or the time of growth gone.
[04:01:04] It depends on how you view it.
[04:01:06] So, but when I went to DevCon 2, people were so nice, forgiving, basically hugging me when I was giving the talk there.
[04:01:14] And the only thing I didn't like was the foundation telling me I was not allowed to speak about The DAO, which was like, "I am speaking here to the Ethereum community.
[04:01:23] Well, how can I not speak about The DAO?"
[04:01:25] And so I talked about a pretty boring talk about security.
[04:01:30] And I think every second talk was about security at DevCon 2.
[04:01:34] It was just about how we get those smart contracts secure.
[04:01:37] So I gave a rather boring talk.
[04:01:39] But in the end, I just said, "Well, thank you for your understanding.
[04:01:43] And it was a hard time and so on."
[04:01:45] And they were like, there were some standing ovations. I remember becoming emotional because this was, I did not expect this.
[04:01:52] I really expected like, "Guy, you messed up Ethereum.
[04:01:55] Like, we almost lost it all."
[04:01:57] So I think this just speaks to the Ethereum community, how they treated Stefan, how they treated me, even though mistakes were made, honest mistakes, at least from what I can tell.
[05:02:07] Uh, so this is such a great community of really nice people who really want to change the world, capable and also now financially capable of really doing things.
[05:02:16] I was watching that video quite recently, actually.
[05:02:18] Um, and yeah, it was quite cut off a little bit. In the end, it is...

**SPEAKER_02:**
[05:02:22] You know, it was quite a long ovation there.
[05:02:24] And yeah, you could certainly see that emotion in you.
[05:02:27] And that's when we first met, actually, was in Shanghai for DevCon 2, I remember.
[05:02:32] Was on the sidelines there in that main conference hall.
[05:02:35] And yeah, it was lovely to see that.
[05:02:37] That's for sure.
[05:02:38] Okay.

**SPEAKER_01:**
[05:02:39] Yeah, I think good notes. Just Bob, you were the one who tried to impose a half hour to hour rule. We're at a solid 1:20 right here.
[05:02:49] The other time maybe with me.
[05:02:50] You know, we've reached a good kind of endpoint, I guess.
[05:02:53] So what happened after Blockchains LLC for you then?

**SPEAKER_00:**
[05:02:57] So because of time, I keep it short.
[05:03:00] So yes, we got bought by Jeffrey Berns, Blockchains LLC at the time.
[05:03:04] Again, the reason for this being he wanted to build a new city in the desert.
[05:03:08] He wanted to do it all on IoT, all on Ethereum from scratch.
[05:03:12] It's a developer's dream, building from scratch on a green field on top of Ethereum with our tech.
[05:03:17] And I felt comfortable at the beginning. In the end, I felt like we need to release stuff.
[05:03:22] And there were some voices of the company which didn't want to release until like a very, very big product was done.
[05:03:27] For many reasons, that didn't happen.
[05:03:29] I don't want to get into that too much.
[05:03:31] So after two years, I left Blockchains.
[05:03:34] Back then it was called Inc.
[05:03:36] They made a change in their name.
[05:03:38] And I did for six months, I did really nothing.
[05:03:41] I forced myself to do nothing, which was great after so many stressful years.
[05:03:46] And then I started a venture studio called Corpus Ventures, where we tried out many different ideas.
[05:03:52] We had EM3, which was a decentralized messaging protocol, GasHawk, you can save transaction costs on Ethereum.
[05:03:59] What else did we have?
[06:00:00] So with some domain name stuff, but we didn't get—we didn't release it at the end.
[06:00:04] But the biggest one was Tokenize.it.
[06:00:06] And this was, we built something for German—for now, German startups.
[06:00:11] In the end, we want to do it all over Europe.
[06:00:13] We're just tokenizing their shares and doing fundraising.
[06:00:16] So in summary, it's like a Web3-based AngelList for Europe.
[06:00:22] It's the one-sentence description for Americans also to understand.
[06:00:25] AngelList, it's a great tool for business angel investing.
[06:00:29] We want to do the same for Europe, for all countries there, and build it on-chain.
[06:00:33] So tokenizing all those shares and enabling private as well as public fundraising.
[06:00:38] So some called legal ICOs, if you want, but also for private fundraising.
[06:00:43] Our customers currently...
[06:00:45] you have more than—maybe a good way to end this.
[06:00:47] You have now more than 400 investments from more than 320 business angels in more than 50 companies.
[06:00:55] Those are traditional German GmbHs raising from super conservative business angels, doing it completely on-chain.
[07:01:02] They are paying in stablecoins, getting their tokenized shares in their non-custodial wallet.
[07:01:07] They're all getting a Gnosis Safe wallet from us, using Privy for login.
[07:01:12] So we build it as intended and we get normal people to use it.
[07:01:16] For me, this is kind of a dream come true because I'm out of—I love the Web3 bubble.
[07:01:21] I love this community.
[07:01:22] I love to work inside there.
[07:01:24] But for me, Tokenize.it is a way to make this technology available where it belongs, like to startups and investors outside of our Web3 bubble.
[07:01:32] And I'm super, super happy that we could keep up those values that they have.
[07:01:37] The complete platform is non-custodial.
[07:01:39] They have their safe on Ethereum, holding their tokens, paying in stablecoins.
[07:01:44] So I'm very happy to see this.
[07:01:46] Over the next years, we want to basically roll out this all over Europe and become, yes, the Web3-based AngelList for Europe.
[07:01:54] That's the goal.

**SPEAKER_02:**
[07:01:55] Fantastic.
[07:01:57] So hope to see you at DevCon 8.

**SPEAKER_00:**
[07:02:00] Me too.
[07:02:00] I'm looking forward to it.
[07:02:02] As of now, I don't intend any change.
[07:02:04] Stick to Ethereum.
[07:02:05] I love the community.
[07:02:06] I continue building and try to get a lot of people using it.

**SPEAKER_02:**
[07:02:09] Have you been to every DevCon?

**SPEAKER_00:**
[07:02:11] Yes.
[07:02:11] Yes, I said yes.
[07:02:12] I've been to every DevCon.
[07:02:14] The last one was actually the first one that I didn't give a talk.
[07:02:18] And I also went to every ECC except for one that was COVID.
[07:02:22] There was some reason I couldn't come.
[07:02:23] But yes, I'm actually, I intend to continue to come to every DevCon.
[07:02:27] It's like you meet the people like Griff Green, Lefteris, of course, Vitalik, and many others.
[07:02:35] It's just a sweet spirit there.
[07:02:37] Nice community.
[07:02:38] Love seeing how it all grows.
[07:02:40] Listen to those exciting talks.
[07:02:42] I mean, for Tokenize.it, it's not as relevant.
[07:02:44] It's not like our customers or the tech, of course.
[07:02:47] We're just doing an ERC-20 token on Ethereum.
[07:02:50] It's super easy.
[07:02:51] It's no deep tech.
[07:02:53] Sometimes I miss doing deep tech, but, well, I just enjoy being there, seeing what all happened, and remembering those magic days.
[07:03:00] And it's like only once in a lifetime or two times in a lifetime you have this moment where everything comes together: the right time, the right place, the right people.
[07:03:09] This certainly, were those one and a half years I worked for Ethereum, are definitely the prime of my career in terms of who I worked with, what we accomplished, the impact we had on the world, and the sweet cyberpunk spirit there and what we did there.
[07:03:23] It was really great.
[07:03:24] I always sometimes get emotional thinking about this and meeting those people again at DevCon.

**SPEAKER_02:**
[07:03:29] Fantastic.
[07:03:31] Well, thank you for all your contributions to that success.

**SPEAKER_00:**
[07:03:33] Likewise.

**SPEAKER_02:**
[07:03:34] All the best.
[07:03:35] Okay.
[07:03:36] Oh, just one more.
[07:03:37] Where can we find you?

**SPEAKER_00:**
[07:03:39] You can find me usually on Twitter for the Ethereum people, C-H-R-Y-E-N-G.
[07:03:45] Of course, I have a complicated name, not many vowels in there, but you'll find it.
[07:03:49] Or, of course, on LinkedIn.
[07:03:51] Actually, for my company, I'm more active on LinkedIn, which I was never before, but that's where we get our clients and tokenize it.
[07:03:58] Yeah, but usually you can find me on Twitter or follow me there on LinkedIn.

**SPEAKER_02:**
[07:04:02] Excellent.
[07:04:03] Okay.
[07:04:04] Thanks so much.
[07:04:05] Have a great day.

**SPEAKER_00:**
[07:04:06] Thank you.
[07:04:07] You too.
[07:04:08] It was great talking to you.
[07:04:09] Bye.