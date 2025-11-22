**SPEAKER_00:**
[00:00] Okay, recording is in progress. It says so.
[00:05] Hello everybody.
[00:06] Today, delighted to have Christoph Jentzsch with us.
[00:09] We did attempt to record this, Christoph and I, two weeks ago, but I forgot to press the record button.
[00:14] So we spoke for an hour or so and then it was not recorded.
[00:17] So this is round two.
[00:19] Hello Christoph, how are you?

**SPEAKER_01:**
[00:21] Hi everyone.
[00:22] Nice to meet you again.
[00:23] I'm doing good.
[00:24] I hope you too.
[00:26] Thanks for the invitation.

**SPEAKER_00:**
[00:27] Fantastic.
[00:28] Christoph and I, our paths crossed for the first time way back in 2015 when I was trying to do C++ Ethereum on my smartwatch.
[00:36] And this was around the time that Christoph was still at the Ethereum Foundation.
[00:41] And then I think our paths have crossed a number of times since, and Kieran's too.

**SPEAKER_02:**
[00:46] Indeed.

**SPEAKER_00:**
[00:47] So, so Christoph, what were you doing with your life before you found Ethereum and joined this crazy journey?

**SPEAKER_01:**
[00:54] So the journey started in 2013.
[00:58] I was doing my PhD in theoretical physics actually about self-organizing systems.
[01:03] So like biology, systems in mathematical biology and other things.
[01:06] So I was studying systems which have local rules and global behavior and I came across Bitcoin, which has just a small set of local rules and a global behavior as a currency.
[01:17] But the reason I came across this was I was looking for cheap GPUs like graphic cards and the Bitcoin miners were selling their GPU mining rigs to get some FPGAs and later ASICs.
[01:29] And so that's how I got into what's Bitcoin mining.
[01:32] And so I bought my first Bitcoin, got into this bubble, did read everything I could about it and then I came across the white paper from Vitalik, early 2014, something like January, February in some Bitcoin forum somewhere.
[01:46] And I was already totally in love with the idea of Bitcoin being a decentralized currency and all the characteristics and features of it.
[01:53] And this white paper of Vitalik, and if you read it again, it's almost a prophecy, except of NFTs.
[01:59] Everything is in there from DAOs, from ENS, like names, domain name systems and all of that.
[02:05] So for me it opened up this option of building applications with the same characteristics as Bitcoin, but just not a currency but everything else.
[02:14] And so then I started reading everything about it.
[02:17] And in 2000, actually still 2014, in summer, I read the crowdsale was in 2014.
[02:24] Right, right, yeah, the crowdsale.
[02:26] So around the time the crowdsale happened, I did watch a video from Gavin Wood.
[02:30] He was somewhere in the Scandinavia, some conference there, the Nordics and he talked about Ethereum.
[02:36] I loved it.
[02:36] And he said, "You want to open up an office in Berlin looking for C++ developers."
[02:40] I was a C++ developer so in theoretical physics it's 90% software development.
[02:45] So I said well I want to do this.
[02:47] So I took my parental leave time plus some vacation time from and paused my PhD for like three or six months and said I will return after I'm done.
[02:56] I thought this is just a short project because they raised money maybe six, maybe maybe 12 months, 18 months or so, then it's over.
[03:04] When I started I thought about maybe three to six months and then I go back to my PhD.
[03:07] So I worked there with Ethereum with Gavin Wood, was a great time and then just decided to stay.
[03:12] It was so exciting.

**SPEAKER_00:**
[03:13] So, so you never got to be a doctor?

**SPEAKER_01:**
[03:15] No, I'm not a doctor.
[03:16] I did not finish my PhD, although I only had six months left which was kind of a pity.
[03:21] I worked like for three years on that.
[03:23] But I also had at the time, I think four or five kids.
[03:26] I needed some money.
[03:27] I didn't get much money as a PhD student so I did software development as a side hustle basically.
[03:33] And so when I got this project I said well let's do this for two or three months as a parental leave time and then I can return.
[03:39] And then I decided to really interrupt my PhD is that I will maybe return one year later because I thought the foundation will eventually run out of money because they're not making any profits, they just raised donations, then they will spend them and then it's over.
[03:52] Then I can continue my PhD.
[03:53] That was originally a plan, just came different.

**SPEAKER_00:**
[03:56] I mean I guess it's never too late, right.

**SPEAKER_01:**
[03:58] I actually sometimes think about if I should return.
[04:01] It's just so much to learn again.
[04:03] I'm right now doing Tokenize.it.
[04:05] I'm basically working on tokenizing German companies.
[04:08] It works, works very well.
[04:10] So currently I'm not planning on getting back anytime soon.

**SPEAKER_00:**
[04:13] No, because I mean famously you had, you know, Dr. Gavin Wood and Dr. Christian Reitwiessner as well and I think, I think there were a couple of other PhDs as well.

**SPEAKER_01:**
[04:22] There was definitely.

**SPEAKER_02:**
[04:23] I also dropped out of mine.
[04:24] I was actually in mathematical physics too.
[04:26] Interesting, similar background.

**SPEAKER_01:**
[04:28] It's actually the same like theoretical physics.
[04:30] It's the mathematical part of physics.
[04:32] I enjoyed it very much.
[04:33] I did thermodynamics and statistics mostly.
[04:36] Software development was really fun.

**SPEAKER_02:**
[04:38] Well, by the way, Jim is trying to join.
[04:40] I don't know if there's anything that needs happening he gets some browser.

**SPEAKER_00:**
[04:42] Yeah, yeah, well he'll pop up and we can add him or if he's then never mind.
[04:47] So Christoph in terms of getting hired into EthDev and I'm sorry if I just missed it.
[04:52] So how, how did that happen?
[04:54] Did you meet Gav at a meetup?
[04:56] Did you say?

**SPEAKER_01:**
[04:57] Yes, I actually, I listen only to his talk as for the online thing and I actually just wrote him an email, said look, I see C++ developer would love to join Ethereum, love what you're doing.
[05:07] And he invited me to meet me in Kreuzberg, Berlin, so which again is about two hours drive from here.
[05:12] So I went up there, met him.
[05:14] I remember the first conversation he was talking about all the stuff they were going to build and said well what, what can you do?
[05:20] And I just asked him what's like the most complicated stuff you have right now, like give me a complicated task, I somehow can figure it out.
[05:27] So he talked about the Ethereum Virtual Machine which needed some testing.
[05:32] So, so I just picked working on testing the Ethereum Virtual Machine or like writing test for it.
[05:37] Back at the time I actually had no real idea what he was talking about.
[05:40] Meaning of course I did understand on the white paper level I didn't understand what Ethereum was about.
[05:46] But Gavin had this skill of writing the Yellow Paper which is still incredible work.
[05:50] Like it's a such a great specification, different from Bitcoin really having a specification so multiple clients could be built.
[05:57] And in there he defined the Ethereum Virtual Machine.
[06:00] And I, I think I read the paper six, seven times.
[06:03] I felt like I was one out of don't know, 10 or 20 people in the world at the time who really understood the Yellow Paper.
[06:09] I did corrections to it.
[06:10] I have some pull requests actually in the Yellow Paper GitHub repo added missing definitions and stuff like that.
[06:16] And then what I mostly did was writing test according to the specification which then were with the help of the C++ client because this was his teams.
[06:24] I was working also on the C++ codebase and so Geth, the C++ Ethereum client, also the JavaScript version and what else do we have like five Haskell client and others.
[06:35] They're basically using my test to see if they are implemented Ethereum Virtual Machine also the state transitions and block creation correctly.

**SPEAKER_00:**
[06:41] Yeah, yeah.
[06:42] So I mean just just to have some timeline for the, for the viewers.
[06:45] So Vitalik wrote the white paper in November 2013.
[06:49] Various other people sort of joined in on the efforts in December, including Gav and Jeff who started the C++ and Go clients respectively at the very end.
[06:58] Oh my goodness, at the very end of December kind of Christmas projects for them both.
[07:03] January 2014 you had sort of like the, the public announcement of Ethereum at the, at the Bitcoin Miami conference.
[07:10] It was as early as April 2014 that Gav wrote the Yellow Paper which is, you know, as you were saying, the sort of formal specification.
[07:18] You had the crowdsale between July and September 2014.
[07:22] So then yeah, you, you were coming in right after that, you know, so you had a wave of arrivals in September and October of that year.
[07:29] Essentially because the crowdsale had happened.
[07:31] There was some money to actually hire people and then talking about, you know, where you where you met there initially that group.
[07:38] So EthDev were and is a company coordinating the development of of Ethereum stuff.
[07:44] So it's a subsidiary of the Ethereum Foundation.
[07:46] They were working initially in a co working space but then and it was between August and November of that year that the office was getting like, you know, done up and tidied.
[07:56] And then in November you had Devcon 0, you know, the first conference, you know, an internal one where a lot of the people that was their first sort of face to face meeting.
[08:06] How was Devcon 0?
[08:08] How was that?
[08:09] What was that like?

**SPEAKER_01:**
[08:10] It was like a company retreat.
[08:12] So this was not a public conference.
[08:14] We did have even though there were some outsiders who felt like part of the community maybe also pushed some code.
[08:19] And I remember his name again, who wrote the book also about Ethereum from IBM.
[08:26] Yeah, I think he was also there just as an example of some people who are like reading about Ethereum, interested in joining.

**SPEAKER_00:**
[08:33] Of course Roman as well, right?
[08:34] Roman.
[08:35] Roman was there with the Java client.

**SPEAKER_01:**
[08:37] But it was mostly developers.
[08:38] But also I think Stephan Tual was already there.
[08:41] So we had already the London team.
[08:43] So it was like an internal Ethereum meeting.
[08:46] Kind of a meetup.
[08:47] Almost.
[08:48] Almost.
[08:48] I think three days or so.
[08:50] I don't know exactly five days even.
[08:52] So it was a full week.
[08:53] I was there for the full week as far as I can remember.
[08:55] I did a presentation about testing how the test suite is very important.
[08:59] Yes, we had to Remix project, Solidity project I think mostly started during the time Gavin used this for a explaining his vision of what Ethereum as a platform for decentralized application.
[09:12] So building Swarm.
[09:14] I don't know if Swarm and Whisper was already launched there but at least like the generic idea, the Mist browser.
[09:20] So all those ideas are really sketched out there like the technical roadmap.
[09:24] What we are going to build because we started just of course with the basic clients like implementing the protocol.
[09:30] But he took it like kind of what are we going to do in the next 12 months building the Mist browser, like Remix of those tools to have a platform for decentralized applications.
[09:41] I remember one slide which I think I posted on Twitter a while ago, but you have those three circles, one circle is one node and you would see like they are connecting on the blockchain using Swarm for the data, Whisper for the messages.
[09:54] And you like this whole picture was painted there and the people attending, I think around 50 people plus minus 10, don't know exact number where mostly developers talking about code coding there.
[10:05] Joseph, I remember him being there saying well all of you, you will create your own companies becoming millionaires.
[10:12] I remember Joseph was talking about that and I think mostly was he was right.
[10:16] So most of those people in the room in one way or another co founded, founded or early part of companies building on top of Ethereum in the years to come.

**SPEAKER_00:**
[10:24] Yeah, yeah.
[10:25] Let me see if I can do a little, a little screen share.
[10:27] No, never mind.
[10:28] I can't work out how not, not to worry.

**SPEAKER_02:**
[10:31] But, but yeah, this is present button.
[10:33] So not working.

**SPEAKER_00:**
[10:34] Yeah, I don't see that.
[10:35] Is that on the right hand side.

**SPEAKER_02:**
[10:36] Somewhere or at the bottom you maybe have a different.
[10:38] For me, I appear on the top right and below and to the right of me below there's a present button.

**SPEAKER_00:**
[10:43] Right.
[10:44] With like a plus post maybe.
[10:46] Never mind, never mind.
[10:47] I was just going to show the iconic photo of people at Devcon 0.
[10:50] Right.
[10:51] You know that's this big group shot with nearly everyone who was out there, you know.
[10:55] So that's a classic Ethereum photo.
[10:58] So I was looking, Sorry, there's like 11 of the videos are still around from Devcon 0.
[11:03] I think there were about 20 sessions.
[11:05] I'm still trying to dig out the others.
[11:07] Some of them, including yours, I have not managed to find yet.

**SPEAKER_01:**
[11:10] Yeah, it was only about the test suite, how it build it, how people would use it.
[11:14] It was rather technical.
[11:15] There was not much of a vision in there.

**SPEAKER_00:**
[11:17] Well, Lefteris presented on Emacs so you're not the most boring talk.

**SPEAKER_01:**
[11:21] Again.
[11:22] It was just the nerds starting also for most of them.
[11:24] The first time we actually met, of course the C++ team, they didn't know each other because they're working in the co working space Lefteris and others were there.
[11:32] But then let's say I think it was the first time I actually met Vitalik because he came there then of course Jeffrey and his team, Stephan's team, Joseph Lubin.
[11:41] So it was for me it was the first time to meet all of them and having talks and since we really had time, five days, a small group of people, we actually do have time to eat together to talk.
[11:51] So it was not so crowded maybe as Devcon is today.
[11:55] Very intimate.
[11:56] Was good.

**SPEAKER_00:**
[11:57] Yeah.

**SPEAKER_02:**
[11:57] I mean one thing I can't quite remember.
[12:00] So there was a time there was an Ethereum Slack that was kind of open to the public.
[12:03] There were a lot of people.
[12:04] The sort of Ethereum affiliation status was fairly vague at that point.
[12:08] And we were, you know I, I remember we were using Skype a lot in those days.
[12:12] Just, just the team and like Vitalik like to Skype.
[12:15] And then at some point I sort of lost the thread of like where the core like I can't remember where the core development discussions were happening.
[12:22] And I'll maybe I'll ask Jim to comment also.
[12:25] Just like those tests we kept like getting them and I think I'm thinking of some a little bit earlier on and we'd build them and Jim was mostly working on them and would update on the like passing percentage which would always be between like 93 and 98 and then something would change, you know.
[12:39] But yet like where did the discussion?
[12:41] Because yeah between like sale and Devcon 0 I think it kind of got a little bit.
[12:46] It like moved around where the dev discussion.

**SPEAKER_01:**
[12:48] Yeah, it was mostly Skype.
[12:49] We also had Skype channels for almost everything like the C++ team and so on.
[12:54] Then I in a short time they used a, it was a notetaker which had a name also with E something.
[13:00] Yeah.
[13:00] Etherpad, something like this.
[13:02] Right.
[13:03] There were some notes being written there but the communication was really I would say 99% Skype for me.
[13:09] Later on we used a tool based on GitHub.

**SPEAKER_00:**
[13:12] What was the name of was called Gitter.

**SPEAKER_01:**
[13:13] Gitter came later.
[13:15] This was like the replacement for Skype.
[13:16] But I didn't use it too much.
[13:18] This was actually during the time and I was actually leaving but it was then used also by C++.
[13:22] There you had a channel per GitHub repo.
[13:25] This was during the time that GitHub was completely reorganized because at the beginning was like one big repo is everything they made sub modules was so messy.
[13:33] And during those, during this process we got Gitter.
[13:36] But yeah for me it was mostly Skype.

**SPEAKER_00:**
[13:38] Yeah.
[13:38] And and then annoyingly that kind of means a lot of these early discussions are kind of like a bit lost because nobody is is using Skype.
[13:46] And Skype is getting like deleted.
[13:49] This is happening in February of next year.

**SPEAKER_02:**
[13:51] Oh, I thought it happened already.

**SPEAKER_00:**
[13:52] It's no, you can still request to download.
[13:54] And I did and then I haven't heard anything back and want to do that to see if I can get some of those.
[13:58] So everybody apply to download your your Skype data.
[14:02] I remember the with, with Gitter there was a discussion about this that I was involved with at the EF later which was saying the problem with Skype is it wasn't discoverable.
[14:11] You know, you had to add, you had to request to be added, but you had to know what was there to be able to do that request.
[14:17] So it was a bit of a chicken and egg situation.
[14:19] Whereas Gitter, it was like a one to one with the repositories.
[14:23] So if you're using a repo.
[14:25] There you go.
[14:25] There's a one to one channel with that.
[14:27] And it was discoverable and archived.
[14:30] But then Slack I think was even earlier.
[14:32] So.
[14:33] Oh, there was the forum as well.
[14:34] Right?
[14:35] It was an Ethereum forum too.

**SPEAKER_01:**
[14:36] Yeah, it was important.
[14:37] And then Slack.
[14:38] I think I got introduced to Slack by Stephan Tual when he created a community for The DAO.
[14:44] When he looked for a new communication tool, he went with Slack.
[14:48] And at that time it was not like today like a business tool for the company.
[14:52] It was really communities.
[14:53] Like we had 5,000 people in our Slack, which is not how it's used today.

**SPEAKER_00:**
[14:57] Yeah, yeah.
[14:58] So welcome Jim.
[15:00] Your technical problem.

**SPEAKER_03:**
[15:00] Hi.

**SPEAKER_01:**
[15:01] Sorry.

**SPEAKER_03:**
[15:02] I had some technical problems for a while there, but I don't know, I'm just listening to you guys.
[15:06] What, what, what happened that brought the whole world to Zoom?
[15:09] Suddenly.

**SPEAKER_02:**
[15:10] It was in waves look for on my side.

**SPEAKER_03:**
[15:11] I don't know, I just, I just woke up one day and everything was Zoomed.

**SPEAKER_02:**
[15:15] Yeah.
[15:16] From then on species like a statistical phase transition, you know.
[15:19] I think it was, it was two faces.
[15:21] I would always get invited to corporate like let's say 2017 to 2019 when I was doing primarily BD, I found that I would get invited to any of 10 video conferencing tools.
[15:32] And like what is the Cisco one was the Webex.
[15:35] That was horrible.
[15:36] I would get that a lot.
[15:38] Google Meetings didn't feel sufficiently corporate or something even though it was okay.
[15:43] And Zoom had the best quality for a while.
[15:45] And I found that everyone picked Zoom at the same time.
[15:48] Like mid 2018, let's say.

**SPEAKER_00:**
[15:50] I think it was just quality to me.
[15:51] Like I mean Microsoft really fumbled.
[15:54] Right.
[15:54] Skype had got such a lead for so long.
[15:57] But Zoom just seemed more reliable.
[15:59] Whatever weird little proprietary magic they had going on.

**SPEAKER_01:**
[16:01] Yeah.

**SPEAKER_03:**
[16:02] And then I guess, yeah, I guess I was under the impression that like Zoom is for businesses.

**SPEAKER_02:**
[16:07] I think that's.
[16:07] Well that is true, but it was just that still, I mean this, this has gotten way better in the last 10 years, but still nothing really works for reliable video over the the Internet.
[16:17] It's, it's just much better than, than what existed.
[16:20] But there was a free version always and they would just like time you out.
[16:24] So like they had a fairly viral acquisition loop where like.
[16:27] And I was just gonna say in the pandemic once when people were locked down, it became a consumer tool where people would have like yard, large yoga classes or you know, sermons or whatever with like 500 people on a Zoom and then everyone bald.

**SPEAKER_03:**
[16:40] Yeah, I remember it well.
[16:41] All of a sudden like my, my parents were like calling me up and they're like, we found this awesome new tool.
[16:46] You probably never heard of it, it's called Zoom.

**SPEAKER_02:**
[16:48] But yeah, there were like 10.

**SPEAKER_00:**
[16:49] Let's move on from sharing about video platforms, eh?
[16:53] So, so I look back, so, so Jim's first commits on on the Haskell client were mid September 2014.
[17:02] So you know, a couple of months ahead of, ahead of Devcon 0 that you'd had the Yellow Paper for, for, for five months at that time.
[17:11] And I, I did find on our Slack, you know, a bit of a thread where, where things I think from you Christoph, were, were being discussed by Jim.
[17:21] I don't know.
[17:22] Did you guys interact directly at all on on testing Jim Christoph?

**SPEAKER_01:**
[17:27] Not directly, not as far as I can remember.
[17:30] I mean maybe there were some messages.
[17:31] I mean it's about, it has been a while ago.

**SPEAKER_03:**
[17:34] I could be wrong.
[17:35] I may have met you briefly in London when we had that conference, but it would have been like, like hi, you know, quick, quick, quick greetings at a part, you know, an after party or something.

**SPEAKER_01:**
[17:45] I mean 10 years ago, lots of people.
[17:48] Sure.
[17:48] We were the testing GitHub repo and we had all the major clients using it and I was interacting mostly asking responding questions.
[17:56] I mean of course the C++ team I was super close to.
[17:59] I used the C++ client also to pre fill the tests.
[18:03] So this was per default.
[18:04] Right.
[18:05] Except we found there was a test failing.
[18:07] But it should.
[18:08] But actually C++ was wrong.
[18:09] So sometimes this happened.
[18:10] The test was not really fading, just C++ was wrong.
[18:13] But in the majority of cases C++ was right.
[18:16] We were just having those conversations and we found tons of issues not just in the beginning I wrote those tests using actually bytecode, the very first test.
[18:25] Then I went to a low level Lisp like language.
[18:28] This was LLL, this was the precursor to Solidity, by Gavin.
[18:32] Then in the end actually I had automated fuzz testing where I wrote software that would create thousands of tests and we had some AWS like over a hundred cores of machines constantly creating tests and we had always some failing on some versions of Geth or other clients.
[18:48] So this was mostly what I did during one and a half years.

**SPEAKER_00:**
[18:51] Right, right.
[18:52] So, so yeah, I mean, I guess for the, for the viewers, something that Ethereum chose to do differently from Bitcoin was to have this specification separate from the client software.
[19:03] Right.
[19:03] So you know, when Bitcoin started it was the code that happened first and the, the white paper afterwards.
[19:08] But, but the white paper wasn't a protocol specification.
[19:12] So you know, Gav was doing that Yellow Paper spec in parallel with the C++ client which was sort of the, the first one.
[19:20] While you have Vitalik working on the Python client, Jeff working on the Go internally.
[19:24] But then you've got all these other clients as well.
[19:27] The Java one by Roman I think started in about April or May ourselves.
[19:32] Jim and Kieran here with a Haskell client starting in September.
[19:36] You had JavaScript as well.

**SPEAKER_01:**
[19:37] It's more like a library.
[19:38] I don't know if it's really like a syncing client, but they have all the tools so you can, in your web app kind of integrates part of parts of it to verify certain states.

**SPEAKER_00:**
[19:48] Yeah, I mean I think maybe they had a syncing client at some point apart from it obviously like couldn't actually keep up but theoretical and, and yeah, like a little later there was a Ruby client as well.
[19:59] And yeah, at one point there were eight different clients.

**SPEAKER_01:**
[20:01] Right.
[20:02] If you want to, I can tell the story of why we all are using Geth today.
[20:06] Yeah, absolutely.
[20:06] Not a given.
[20:07] At the time, of course everyone had different opinions, but the C++ client was really the fastest, the most solid one, passing all the tests and so on.
[20:16] But Gavin always wanted to add new features, do a refactoring and he was a perfectionist, which is not bad for this kind of software.
[20:25] And then the time came for the security audit because everybody wants to launch Ethereum now and we said before we launch it, those clients needs to be have a proper security audit by an external company.
[20:36] And one of the companies doing this was Deja vu in Seattle.
[20:41] So I actually went with his team for the audit and because Gavin wanted to build some more features, said, well, let's just Geth can go first.
[20:49] Let's first audit the Go client.
[20:51] They are done.
[20:52] I'm done with the the features I want to build and then we going into the audit for the C++ client.
[20:58] So Geth was audited picked.
[21:00] They had some issues.
[21:01] They fixed the issues and now it's time.
[21:04] And so there was technically no reason why not.
[21:07] Well actually we could launch Ethereum now and we have a fully audited client.
[21:11] Testnet is running for a while.
[21:12] No major issues, no fading tests for a long time.
[21:16] So why would we wait for the C++ client to be audited?
[21:20] And I mean they all really had the pressure of money was running out.
[21:23] We need to launch now.
[21:24] So and then the decision was made, let's launch with Geth.
[21:28] They can still use C++.
[21:29] It's just not audited.
[21:31] Let's say in two months or so the audit is done and then they can use C++ even more if they want.
[21:36] So but then the big mistake was in my view when they made this announcement of you can start now.
[21:42] They recommended using Geth because it was the audited one.
[21:46] So almost everybody run Geth.
[21:48] This was like we started with almost 100% Geth and then I was just a minor.
[21:54] Other clients use it only very few did use them.
[21:56] And so after the audit was done, nobody switched for like sure.
[22:01] But Geth is running I'm synced like what's the issue?
[22:04] Why should I switch?
[22:06] And so we had this 90-10 or 80-20 distribution.
[22:11] It just stayed like this.
[22:12] So if Gavin would have been either say let's just do the audit now and we just if both audited then Step maybe would have 50-50 or even the other way around if they would have first added the C++ and Ethereum would have been launched without a Geth audit.
[22:28] Like we would have seen a total switch.
[22:30] And then of course money was going low in the foundation.
[22:33] They had to reduce the team.
[22:35] And because Geth was the most used one, there were some issues with Gavin.
[22:39] Another story, maybe you have a talk with him.
[22:42] And so in the end Ming decided to basically kick out the complete C++ team.
[22:46] This was then in shortly before Devcon 1.
[22:49] So something like November, October, ish.
[22:52] So but yeah, I think the reason for that was also C++ team wasn't really that used.
[22:56] Also there are other reasons as well.
[22:58] But you can see how a tiny thing can have such big consequences down the road.
[23:03] Like him doing Polkadot today and all of that.
[23:06] And it was great.
[23:07] I mean I really I still think I said maybe would have proof-of-stake and sharding way earlier if Gavin would have stayed.
[23:14] So without him they moved slower that of course the price went up, there were more security relevant things.
[23:19] So changes happened not quickly anymore, but take more time and so on.
[23:24] But I think this was a big loss for Ethereum that Gavin left basically in 2015.

**SPEAKER_00:**
[23:29] Yeah, it's pretty amazing.

**SPEAKER_02:**
[23:29] The client side was the cause.
[23:31] I think it was part of it.
[23:33] But it, you know, having the process maybe started with the Red Wedding which we discussed in some other early days of Ethereum episodes like he, I remember very clearly in the room like you know, two weeks into my Ethereum tenure at that time that he was talking about brain drain if it was only going to be a non profit foundation and not going to have a commercial arm.

**SPEAKER_01:**
[23:51] Yes.
[23:51] There were more issues with that definitely like this was not the deciding part but it was like those things were adding up.
[23:57] I remember that Gavin had this idea of turning the Foundation into a DAO and then having for profit entity next to it which would build things and make money.
[24:06] So there were many different commercial ideas at the time.
[24:09] So he then basically started on his own EthCore.
[24:12] I remember he wanted to have me as part of it but I decided to do Slock.it at the time.
[24:18] So that's why I did not became a co founder of EthCore.
[24:21] Another story we can go into this, we want you know, you know what happened after that.
[24:25] But there's many reasons we're part of it.
[24:27] I think also him and Ming didn't really get along too much.
[24:30] There was not really a trust relationship going on.
[24:33] Of course, money running out, different visions of how Ethereum should evolve technically and economically if you want all played a role.
[24:41] But I think it was just one part that the C++ client wasn't really used that much.
[24:45] And the reason for that was Geth being audited launching without an audit for the C++ client.

**SPEAKER_00:**
[24:51] Yeah, I mean talking about features.
[24:53] So, so many things happened.
[24:55] Right.
[24:55] You know Gav had this period of incredible productivity between that December and that April of getting from nothing.
[25:02] You know, just like just having the white paper all the way through to having a working client.
[25:07] You know having the, having the Yellow Paper as you mentioned.
[25:10] You know there's this, this dirty diagram showing how, how Whisper, and Ethereum, and Swarm were intended to fit together.
[25:18] And I, I, I found some more timing on that was so Swarm was envisaged by Daniel Nagy as far back as 2011.
[25:26] You know it was a, it was a year an idea he'd been working on for like three years before that.
[25:31] I spotted on the Whisper presentation that Gavin did that.
[25:35] That was a pre Ethereum idea as well.
[25:37] So it was probably only when all of these people came together, it was like, well, you've got this storage idea, you've got this blockchain kind of like CPU databasey idea.
[25:47] And then if you have messaging, all of these things can fit together.
[25:50] But it's also.
[25:52] We're going to build our own idea as well.

**SPEAKER_01:**
[25:52] Browser.
[25:53] Browser.

**SPEAKER_00:**
[25:53] I'm sorry.

**SPEAKER_01:**
[25:54] Plus the Mist browser.
[25:56] So the complete thing, it's a.
[25:57] It's a complete platform for decentralized applications, end to end.
[26:02] This was the big vision and also this was what attracted me to it.
[26:06] I mean, having someone having a really proud vision of a new Internet, if you want.
[26:10] That's what he called Web3.
[26:12] That's where the term comes from.
[26:14] Because it was not just a little tool.
[26:15] It was a complete new Internet called Web3.
[26:19] From data to messaging to smart contract blockchains to IDE to browser.
[26:25] And this vision was very, very attractive.
[26:28] This attracted all the talent and the developers because they loved building that.

**SPEAKER_00:**
[26:32] Yeah, I mean, it's a very, very expansive vision.
[26:35] And yeah, it was, you know, Gav, as you say, you know, Web3 was him prior to that.
[26:40] I like the language I saw was really about Bitcoin with smart contracts.
[26:45] You know, that was already sort of the genesis of Vitalik, going through that, that journey of colored coins and Mastercoin and meta-protocols and that that kind of positioning of Bitcoin is a calculator and Ethereum's a smartphone.
[26:59] But it was all that, that kind of like blockchains and applications.
[27:02] Right.
[27:03] It wasn't that that full Web3 vision, which I think.

**SPEAKER_01:**
[27:06] And that really came from Gavin.
[27:07] You have to attribute this to him.
[27:09] He was having this big vision.
[27:11] This attracted also so many people.
[27:13] This attracted also that even the business people, they could now understand what it actually is.
[27:18] Other than this was just like tech.
[27:20] Let's see.
[27:21] But this is like a broad vision of how business function, how like this new financial world would happen.
[27:27] Happen.
[27:27] They could understand this far better than having this iPhone calculator comparison.
[27:32] This was maybe a nice technical thing.

**SPEAKER_00:**
[27:34] Yeah, yeah.
[27:34] But then for it being a very expensive vision, that's that's a lot of work.

**SPEAKER_01:**
[27:39] Sure.
[27:40] But I have to start somewhere.

**SPEAKER_00:**
[27:41] That's it.
[27:42] So I mean, you know, talking about Gavin, the features.
[27:45] So yeah, there was a ton of stuff on that, on that C++ team.
[27:49] Aleth.
[27:50] AlethZero as well.
[27:52] And AlethOne.
[27:54] So AlethOne being the GUI miner then.
[27:57] I know.
[27:57] How would you describe AlethZero.

**SPEAKER_01:**
[27:59] Kind of first interface to the blockchain in some way like the first graphical interface to a blockchain client.
[28:06] And what could it do?
[28:08] Of course you could mine, you could deploy a smart contract, you could visit, make it visible somewhat what's happening there.
[28:15] It was not really end user friendly in any way but it was just a replacement of what people just do on the command line usually command line, run your client some input, have some output.
[28:26] And it was the first kind of graphical use interface.
[28:29] Graphical use interface replacing the command line.

**SPEAKER_00:**
[28:32] I guess it's sort of like a combination of like what you have with the block explorer now apart from it.
[28:37] That's, that's like a view only.
[28:39] And this was both of you and a, and a, and a do.

**SPEAKER_01:**
[28:42] Yep.

**SPEAKER_00:**
[28:43] But yeah those, those GUI clients so.

**SPEAKER_01:**
[28:45] Much, much more influential than the Mist browser.
[28:48] The Mist browser.
[28:49] I think there's a video by Alex Van de Sande, it's like a 10 minute video on YouTube.
[28:54] They had this prototype not working yet, but just like take, take it until you make it.
[28:58] The vision of the Mist browser and, and this also really made us understand how Ethereum could work for the end user.
[29:05] Having different identities connected to wallets and you would load those dapps with a IPFS hash or over Swarm.
[29:13] One day the app was loading and you could do some finance stuff there.
[29:17] This gave us an idea of what Ethereum could be.
[29:20] It was.
[29:20] So you have to think Vitalik gave us a rather technical vision and broad intellectual thing but Gavin gave us this pro Internet vision.
[29:30] Alexander, Alex Van de Sande gave us this very concrete thing what an end user could do with that in the next six to 12 months maybe.
[29:38] That's very important.

**SPEAKER_00:**
[29:39] Just yesterday actually.
[29:41] So there was, there was an announcement from Uniswap about them sort of turning on fees and doing various things that more kind of to do with, you know, the company and the protocol time together.
[29:52] And I saw a reaction to that saying, you know, well I'm never going to, you know, I'm never going to use this again.
[29:58] You know, you can't like, you know, extract ongoing revenue out of a protocol and, and this person then said it's time for Mist 2.0.

**SPEAKER_01:**
[30:06] Totally.
[30:07] I've said this before, we need the.

**SPEAKER_00:**
[30:08] Full vision so that you've got hosted and the apps and you don't need a server and you don't need a company and you can just make this pure, you know, immutable smart contract wrapped, wrapped in a UI that's, that's all decentralized.
[30:21] You think we can have a Mist 2.0.

**SPEAKER_01:**
[30:23] I would love to see this.
[30:24] I heard people think about this before.
[30:26] I don't know if anybody really started the project, but should be totally doable today.
[30:30] It's not rocket science, you know.

**SPEAKER_02:**
[30:32] Let me interject.
[30:33] We ourselves have made different attempts at this where you just download the app from the chain itself pretty much it worked fine.
[30:40] I guess it just wasn't as much differentiator.
[30:42] It made things a little slower to do it this way all the time.
[30:45] I also think one of the people that took the Web3 the world computer vision sort of seriously was like the Internet Computer people.
[30:52] And I don't know anyone that uses Internet Computer but like the every once in a while I see tweets about it and I'm like that sounds great.
[30:59] Yeah, serve the app from the chain.
[31:01] You know, it's got some cool like smart contracting language in it and I guess there's just no demand if it like slows the app down even slightly.
[31:09] And I think MetaMask and then many other wallets were sort of enough.
[31:13] Still not the whole thing but.
[31:15] But yeah, I guess it's like you got to get people to use it if you want it to be maximally cypherpunk too.

**SPEAKER_01:**
[31:21] I fully agree.
[31:22] And I mean yeah, the problem with this is you only need it if you really need it.
[31:26] Meaning if Uniswap failed, the interface is not there.
[31:30] It's like a backup, but it's not what you want to use daily.
[31:33] And if you remember maybe Kieran you have Devcon 1.
[31:36] When they presented MetaMask, my first thought was oh, this is totally away from the vision.
[31:41] Like how can you not run a full node?
[31:44] How can you dare you like to just serve over RPCs and Infura like almost.
[31:49] No, not a scam, but it was not what we intended to build today.
[31:53] It's like this is a decentralized version of it.
[31:55] This is like non custodial MetaMask or the good guys compared to all the others.
[32:00] See how the view shifted over the years.
[32:03] Then it was absolutely required to run a full node with the Mist browser.
[32:06] This is how it's done.
[32:07] And now we have MetaMask and Infura and today this is really the version which is viewed as the original non custodial Ethereum vision.
[32:16] So how things are shifting basically.
[32:18] But yes, you only need those things if things are falling apart.
[32:21] Just as an example, so many people use the Gnosis Safe.
[32:25] Let's say the Gnosis Safe UI is gone.
[32:27] Technically it shouldn't be a problem to run another one, but it really needs to be something on IPFS that needs to be something which can self host so I can still access my wallet without going to the command line.
[32:38] So for those reasons you need it.
[32:40] And the Mist browser was sort of as the fallback for every dapp.
[32:44] Like of course you can have your application run on a normal.com domain on on AWS.
[32:49] Fine.
[32:50] But if you could serve the same app in a decentralized fashion as a backup, this would be great because you could still use it if the company that's a uni swap, the company fails if someone builds a nice Uniswap UI served by IPFS directly interacting with the smart contracts.

**SPEAKER_02:**
[33:05] Yeah, yeah, that's, that's fair.
[33:07] Also, I mean Uniswap I think is controversial.
[33:09] I know Jim wanted to say something controversial because they had the company level fee skim and then so I think they've turned the on chain fee on.
[33:16] I don't know that they've turned the company fee off.
[33:18] I haven't read that for detail.

**SPEAKER_00:**
[33:19] I believe so because one of the replies was saying okay, so how are your like shareholders gonna like that?

**SPEAKER_02:**
[33:25] Yeah, okay, fair enough.
[33:26] Well hopefully they hold a bunch of the, the UNI and it will, you know, mark to market.

**SPEAKER_00:**
[33:31] They're doing a bunch of burn so that you know, it should be to the benefit of all stakeholders.
[33:36] But yeah, just sort of this interesting kind of contrast right between completely immutable, you know, force of nature smart contracts versus you know, more permission, more tied to a company, more sort of like wanting to have fees for maintenance kind of kind of question.
[33:51] I mean again, you know, it's like Treasuries I guess either.

**SPEAKER_01:**
[33:55] But this opens up the questions how should an Ethereum app be built economically?
[34:00] And this is also a question being answered during that time this was being the DAO was one approach of should be fully on chain, all the revenue should be on chain.
[34:08] There should be no for profit entity directly attached to it and Slock.it.
[34:13] The company I built after that would be a service provider for them, getting paid by them for work being done for the DAO for one version I was always skeptical and still am about companies where you have effectively two cap tables, meaning you have a token cap table if you want.
[34:30] Of course it's a utility token governance token and so on, but effectively its kind of ownership in the protocol and then you have a for profit company with shareholders and this is always, I think very dangerous because you don't know where to go into what's, where's the value and the shares of the company or on the token.
[34:47] This was the main reason all those companies had those nonprofit foundations in Switzerland, rightfully so, because they said you only want to have one cap table like the Ethereum Foundation.
[34:57] There was no shareholders of Ethereum.
[34:59] There was a nonprofit foundation and a token.
[35:01] The token, if you want to have a share in the economic success of the protocol, you would buy ether.
[35:07] And so later on there were many other token projects where they had a non profit foundation.
[35:12] So no shareholders, no second cap table.
[35:15] And then you would have only the token and all the value would be there.
[35:18] And now with Uniswap you have this problem of having again shareholders and tokens.
[35:23] I think that's dangerous and not a good idea actually.

**SPEAKER_00:**
[35:26] Yeah, yeah.
[35:27] So perhaps let's talk about actually just before we get to Devcon 1.
[35:32] So the launch, right.
[35:33] So obviously a lot of testing and coordination and this different series of proof of concepts.
[35:38] So I mean how did you know it was good enough?
[35:41] Like what was that testing flow and collaboration?

**SPEAKER_01:**
[35:43] Like there are many indicators.
[35:45] One being the Olympic testnet running smoothly for a while.
[35:49] Other one where as I said, the client having an audit, which worked.
[35:53] And then that was saying, okay, now if Christoph doesn't find any failing tests for like three weeks or four weeks or something, we are ready.
[36:02] And this was the case.
[36:03] And so we said that now we can set the launch date.
[36:06] And the launch itself is also a bit typically, typically Gavin or also Vitalik.
[36:12] Nobody wanted to push a button like nobody just like start a chain.
[36:16] So what was done was there was a script written which has as an input parameter the hash of the Olympic testnet at a certain block height.
[36:25] So everybody could using this script plus the software, plus C++ or Go client of course having plus the hash which was at that time in the future of the big testnet, start that chain.
[36:38] So there was no at like at launch day.
[36:41] We were just viewing it.
[36:42] There was nothing to be done.
[36:43] Was like everything was everything.
[36:44] All the information was out there.
[36:46] People were just simultaneously starting the blockchain and then over the peer-to-peer network.
[36:52] This was actually more, more harder stuff.
[36:54] They found themselves on Reddit and others to share IP addresses like connect to miss connect to my peer.
[37:00] Connect to my peer.
[37:01] And so then they started to come together.
[37:04] And of course the longest chain was the valid one.
[37:06] So as soon as you found a peer which had their own chain, you would think and say well yes, this is a longer one.
[37:12] He would stop, stop mining on top of his chain.
[37:14] So basically the canonical chain emerged from that within, I don't know, 30 minutes or one hour.
[37:20] And then we had the chain running and this was like a beauty to behold.
[37:24] Like to just see how this works out as intended.
[37:27] Completely decentralized.
[37:28] Nobody did that do anything.
[37:30] You just.
[37:31] I was in the C++ Berlin office in Kreuzberg, M37.
[37:34] A nice office.
[37:36] And we just watched it.
[37:37] And we are somewhere mining there with their laptop.
[37:39] Wasn't really.
[37:41] And we are all excited.
[37:42] It started.
[37:43] I actually think.
[37:44] I think two or two or three weeks after, or maybe four, we had the first little hard fork.
[37:51] Meaning there was some smart contract doing something that Geth and C++ had a different result.
[37:56] It was for me almost the middle of the night at 10pm or 11pm.
[38:00] So I remember seeing this, looking for one hour or so finding what's the what's the issue.
[38:06] Then I found it, wrote a test about it.
[38:08] C++ was right, Geth was wrong.
[38:10] So gave it to Jeff.
[38:12] They fixed this, I think within one hour.
[38:14] And like after five hours everything was done and they basically called out the miners.
[38:18] Please update your client.
[38:20] So.
[38:21] And then it was fine.
[38:22] So this was the early days, but it was a successful launch nevertheless.

**SPEAKER_00:**
[38:26] Did the Haskell client sync at genesis?

**SPEAKER_01:**
[38:29] I do not know, Jim.

**SPEAKER_03:**
[38:31] No, we.
[38:32] We were able to sync a genesis time for like a year or so.
[38:36] We were sinking.
[38:37] But I remember like that week Kieran and I were like more interested in trying to get a miner in place.
[38:43] So that was what that week looked like for us.

**SPEAKER_02:**
[38:45] Yeah, I had.
[38:46] I was living in a apartment just south of Berkeley campus at this time.
[38:50] And Jim had taken me to Fry's to build a machine a few months prior.
[38:54] Like a build machine.
[38:55] It had a good GPU in it.

**SPEAKER_03:**
[38:57] Yeah, Fry's is dead now, rip.

**SPEAKER_02:**
[39:00] So I was running a miner there and we built a couple in Jim's garage.
[39:03] It got very hot in Jim's garage which was, you know, those.
[39:06] Those things were consuming a fair bit of power.
[39:08] Mine exploded after a few weeks.
[39:10] It was actually just the power.

**SPEAKER_01:**
[39:12] So I was.

**SPEAKER_02:**
[39:12] I thought the whole machine was bricked.
[39:14] And Jim said, you know, I think everything but the power supply will be okay.
[39:17] And it was the case that everything with the power supply was okay.
[39:19] But then I stopped mining and I think Jim would shut.

**SPEAKER_03:**
[39:21] We didn't even bother to buy cases at that time.

**SPEAKER_00:**
[39:23] Right?

**SPEAKER_03:**
[39:24] Yeah, you may have had a case.
[39:25] I had mine just sitting wires out.

**SPEAKER_02:**
[39:28] Yeah, yeah, indeed.
[39:29] Sure you weren't over at that time?
[39:31] We were always, you know, sort of, at least at that time, shorter handed people wise, always catching up A little bit on the features, etc.
[39:39] But it, it ran perfectly well.

**SPEAKER_01:**
[39:41] There was always new features coming.
[39:43] I remember it was really one of the sweet memories during the pre-launch sitting together with Gavin Vitalik, Jeffrey and me in one room at the C++ office, like the nice Gavin's office.
[39:54] He had this 80s style thing and we think okay, what was wrong in our protocol?
[39:58] Then they discussed with a whiteboard changes.
[40:01] Then the first thing, okay, Christoph, you had a test for this protocol change.
[40:05] Then we are in the mean at the same time you're coding it that okay, you're done creating the test.
[40:10] Let's see if they all pass it.
[40:11] If they all pass it, it's like done.
[40:13] You feature the directly new release.
[40:16] And so this is because not done with all the other clients.
[40:18] So they basically had to catch up.
[40:20] It was like information update of the Yellow Paper.
[40:23] Here's a new test, here's like a little Etherpad description of what the new protocol looks like and then please update your clients.

**SPEAKER_03:**
[40:29] But Yellow Paper got me to a certain point.
[40:31] Sorry, Yellow Paper always got me to a certain point but it was always behind the other.
[40:35] The other clients.
[40:37] So I would always find out that like I, I was behind because I went in the morning and connected to the test net and I was no longer connecting or I was getting some state route mismatch or something.
[40:47] And then I'd have to like go and dig through usually the C++ client.
[40:51] I think there was a maybe one or two times where I can't remember why.
[40:55] I think there was one or two things that went to Geth first but usually it was C++.
[40:59] I'd have to go digging through the newest code to find the changes and then bring them in.
[41:04] Then a few weeks later I'd see it in the Yellow Paper.

**SPEAKER_00:**
[41:06] Unlike what you have now where leading into a hard fork you've got all that discussion and specking up for front and like yeah, applying the code into the clients but only enabled for a test net and going through that dance and then ready to go.
[41:19] Yeah, I mean at that point, as you say it's.
[41:21] It's kind of like done in those clients first.
[41:23] And then speculator it looked like from.

**SPEAKER_03:**
[41:25] Where I was standing, it looked like there was a lot of competition between the different clients and the developers there.
[41:31] And I think they sort of like took pride in having the new thing in as fast as possible.
[41:36] And so that sort of led to an environment maybe where there was not, not as much discussion.
[41:41] It was like I'm gonna throw it in and then I get the bragging rights.

**SPEAKER_01:**
[41:44] That was.
[41:45] There was always a fight, Geth versus C++ team about who's the best.
[41:49] And like Kevin was having a big ego and Jeff was more like just give it a, give it a new spec.
[41:55] I just coded.
[41:56] So.
[41:57] But yeah, it was more or less this decision by the three of them.
[42:01] I was basically not playing a very major role in the room and then writing a test for it.
[42:04] But they discussed it after it was clear, they just did it.
[42:07] But it was pre launch after launch.
[42:09] Of course this was different.

**SPEAKER_00:**
[42:10] Sorry.

**SPEAKER_03:**
[42:11] Oh, I was just gonna say like I, I don't.
[42:13] Like a lot of the changes were just like some change in the EVM or, or, or pricing or something.
[42:19] And so so often it was like, you know, I would like freak out in the morning when I wasn't working, but.
[42:25] But then like by 11 o' clock or in the, you know, am I had found like, oh, I see like such and such opcode just doubled in price or something.
[42:33] So I would just put that in.
[42:34] But the big one was RLPx, which is essentially like a big SSL replacement.
[42:40] And that one was like freaking me out for a couple of weeks.
[42:43] I was like digging around trying to find any information about that.
[42:46] Eventually I had to reverse engineer.
[42:48] Maybe that was the one that was in Geth first.
[42:50] I can't remember.
[42:51] But I had to sit there and reverse engineer.
[42:53] I had to run either C++ or Geth and then like put lots of logging information in to see what in the world was happening and then print out all the stuff and then find like the appropriate, you know, crypto libraries to, to.
[43:05] To mimic that and what was the, the background on on that and how it went in so quickly and like I.
[43:12] There was nothing in the Yellow Paper about that at all.
[43:15] And when that came in, it was just a shock to me.

**SPEAKER_01:**
[43:17] Just do you know it at which time this came because I was focusing on the Ethereum Virtual Machine at the time this was more like.
[43:23] Okay, I know Gavin think it was Gavin doing some optimization.
[43:27] He was always thinking about the long term.
[43:29] So if something would be 10% more efficient, we have to do this, right?

**SPEAKER_02:**
[43:32] I think so.
[43:33] I remember like there was a devp2p, libp2p website that was released about that time.
[43:39] It still might have been after the giant change went in.
[43:42] So I also.
[43:43] We were working together regularly, you know, in the Bay Area this time and I think so Jim did like 96% of the changeover.
[43:50] But we had at the time like separate processes.
[43:53] One was more like a client and more like a server we merged them later and yeah, it was like there was a big document one describing like how the DHT for peer discovery would go in.
[44:03] But then you needed like a way to identify the peer years maybe and this system kind of gave them an identity with like a.
[44:09] You know, in in a SSL-style.
[44:11] Like basically there was like a node cert in effect and then you had to like there were session keys and you know, this, this, that and and the other.

**SPEAKER_00:**
[44:19] It was.

**SPEAKER_02:**
[44:20] It took a long time to to implement that thing.
[44:23] But yeah, I think maybe Bob, you would know that.
[44:24] I think this was.
[44:25] Someone else wrote this big thing.
[44:27] This might have been Alex.

**SPEAKER_00:**
[44:28] Yeah, it was Alex Leverington did that so saying about sort of documentation or whatever.
[44:33] There was a wiki, right?
[44:35] There was an Ethereum wiki and a number of things were documented only on the wiki.
[44:39] And I think these.
[44:40] These kind of wire protocol pieces were part of that.
[44:43] But yeah, Alex Leverington was the first hire into that Berlin office and he primarily.
[44:48] I mean he works on a few different C things but the main thing he's known for is is devp2p which was that that common underlying peer to peer protocol though you already had libp2p which is the transport for IPFS that already existed at the time times.
[45:06] There was a bit of not invented here going on but but yeah he he was there for for Devcon 0 as well.
[45:12] And he spoke on.

**SPEAKER_01:**
[45:13] Remember Alex, I was not too much into the peer to peer side of the code base.
[45:17] I was more into the EVM and Solidity smart contract side.

**SPEAKER_00:**
[45:21] I tell you what, there was a bit of funny crossover with the later part of yours was Alex Leverington worked with John Garrett on a project called Airlock.
[45:28] So I remember that I saw it.

**SPEAKER_01:**
[45:30] Later like after we did our presentation had the Slock.it stuff going.
[45:34] They showed us videos of very earlier than us.
[45:37] So yes, they were actually tough time wise.
[45:39] They did this before we did but I did not know about it at all.
[45:43] And so we did it more or less in parallel then and we just launched a bit quicker like to go into the public with the project.
[45:50] There has been from their side was more like a little side project.
[45:52] Didn't look like a big company or intended to be.
[45:55] Yeah I remember this project.

**SPEAKER_00:**
[45:57] Yeah so I think that was.
[45:58] That was at the hackathon at the Bitcoin Expo in April 2014 that they did that and Stephan actually did an interview with them.
[46:05] You can see that on YouTube.
[46:07] You know this is like talking about earlier theory and projects.
[46:10] You know, and this is like a over a year before the mainnet, like so far back some of these.
[46:15] But, but yeah, like some of that spec stuff was, it was not in the Yellow Paper and it was just sort of floating around and a long time before there was real consolidation of that full client spec.
[46:25] But you managed to do it anyway.
[46:26] Jim managed to build the client.

**SPEAKER_03:**
[46:28] It was a busy week but I, I just, it was just notable to me because it's at least from what I was seeing, went from zero to one like overnight.
[46:36] I had never heard of it the night before and then the next morning it was like in the clients and working and I couldn't connect to anything.

**SPEAKER_02:**
[46:42] Which is normally the pattern.
[46:43] But yeah, just this one was like the biggest one time change that I can recall either.

**SPEAKER_01:**
[46:48] Yeah, yeah.
[46:49] Again this was pre launch days.
[46:51] Things had to move fast.
[46:52] There was a lot of pressure going around, it was messy, there was not much coordination between the clients except for maybe some scrap groups.
[46:59] And in the end, yes, recently Gavin and Jeff just made decisions and executed as quick as they could.
[47:06] So this all changed after launch.
[47:08] Then things became a bit slowed down and people consolidated and every change was a big thing, rightfully so.

**SPEAKER_00:**
[47:15] Yeah, yeah.
[47:15] So back on the timeline.
[47:17] So it was July 2015 that Mainnet launched with a Frontier hard fork.
[47:22] And then as you touched on, you had Ming.
[47:24] So Ming's first official day was 1st August 2015, at which point the foundation had been running on for a year or so and was close to out of money.
[47:35] You know, touching on your, your thinking it would only last for a certain amount of time, you know, a year on that raise, which I think was around 16 or perhaps $18 million was nearly all gone.
[47:47] So you had these quite hard decisions about, you know, what, which part of this grand vision was, was going to be funded initially.

**SPEAKER_01:**
[47:54] Right.
[47:55] And I remember talking to her at the time, she felt like I have to clean up the whole mess.
[47:59] Like the paperwork and everything was totally messy.
[48:02] Working with lawyers, accountants and so on and getting cleanup basically of the foundation, I mean for me I did expect it to last something like that.
[48:11] So it was, for me it was clear they are not making any money.
[48:14] I didn't know like how big the reserve was.
[48:16] The detail I think was like don't know, 5%, something in this range, like how much easier the foundation hold.
[48:22] At the time there wasn't that much value either price like $0.50, €1 or something.
[48:28] So it was clear this would not last forever.
[48:30] So I was thinking about going back to my PhD or then I came across this idea about Slock.it and becoming like building a company.
[48:39] And Slock.it was the idea of maybe similar to Airlock.
[48:43] Smart contracts are essentially permission systems.
[48:46] 90% of a smart contract is who's allowed to do what.
[48:50] In case of an ERC-20, it's just who's allowed to send a token or setting an allowance.
[48:55] And in terms of a DAO is who can vote for what and making decisions and then money gets transferred.
[49:01] So what if we could put this permission system into IoT and like who's allowed to switch on, off, use, change, admin rights, whatever.
[49:10] You put this into a small contract.
[49:12] And I thought that ether will never become a currency.
[49:15] Bitcoin was the digital currency.
[49:17] And actually if you think it talk to Ethereum people at the time, we were not thinking about competing with Bitcoin.
[49:23] Bitcoin was a digital currency.
[49:25] We were building a platform for decentralized applications.
[49:28] Ether was just used to run it.
[49:30] I once heard the statement somewhere on Twitter where once that Bitcoin is a currency which needs a blockchain to function, that Ethereum is a blockchain that needs a currency to function.
[49:40] This is.
[49:40] I think it's very true.
[49:42] And so back I thought, okay, Ethereum will not be used as a currency, but it might be used as a currency for IoT devices.
[49:50] So instead of the Internet of things, building the economy of things, and this is kind of what, what drove us.
[49:57] And then we wanted to build this universal sharing network as an application that at the time, Uber and Airbnb just became big.
[50:04] We thought, well, all those sharing economy services should run on chain.
[50:08] So let's build this called the universal sharing network.
[50:11] And then we thought about how to start with something tangible.
[50:15] And then we had the store lock.
[50:16] Actually, it's here in the background.
[50:18] If you see it, it's there.
[50:20] I have this Devcon 1 physical smart lock which we connected to the Ethereum blockchain using our own software and had this idea of people pay to open the lock.
[50:31] And that's what we presented at Devcon 1 together with this idea, which actually only came up like three or four days earlier to connect this with a DAO and the rest is history.
[50:42] What happened after that?
[50:44] But we didn't intend and we didn't start Slock.it for building a DAO.
[50:48] We wanted to build universal share network.
[50:50] Then we thought, well, this is way too big for us.
[50:52] We want to now focus on this Airbnb use case for door locks.
[50:56] And then we thought about fundraising.
[50:58] We talked to a bunch of VCs.
[51:00] I actually, I remember flying to New York, talking to VCs there.
[51:04] Everybody said no.
[51:05] Then I met Joseph Lubin.
[51:06] He said yes, maybe under some conditions.
[51:09] We just did not agree on the terms in detail at that.
[51:12] But I was presented at the Bitcoin meetup in New York and they all like the first application was a Bitcoin application about arbitrage trading.
[51:20] It was like kind of boring.
[51:22] And then I came as a door lock was like super fascinating.
[51:24] Could open the door by paying some ether.
[51:27] So it went well, but we had.
[51:28] Didn't have any money.
[51:30] So we thought about doing something like an ICO.
[51:33] But this was now after the launch of Ethereum.
[51:36] So if I.
[51:37] I started coding an ICO-like smart contract.
[51:40] Why, why should we have have the money directly?
[51:43] It could stay in the contract and then people could vote for giving us part of it.
[51:47] Then we said well we could make proposals to it and then they can vote if the proposal is good or not good or not.
[51:53] Then the money would be released to us.
[51:55] Then they think why could not everybody make a proposal?
[51:58] Like everybody could procreate it.
[51:59] Everybody can make a proposal and those completely open.
[52:03] And we are just one of many service providers to the DAO building this universal shared network.
[52:08] And this was the origin of the DAO.
[52:11] Only like again, three days before Devcon 1, we actually decided we would go for it and put it into the presentation.

**SPEAKER_00:**
[52:18] Yeah amazing.
[52:19] I mean so on the timeline again trying to judge it.
[52:22] So Stephan was I guess chief communications officer or community until September of 2015.
[52:29] That's when when he left.
[52:31] Had you, had you left already by then?
[52:33] Can you remember?

**SPEAKER_01:**
[52:34] No, I didn't really leave because I was technically a freelancer, although I was working full time for it.
[52:39] I didn't have like a formal employment contract.
[52:41] So I was continued to work I think until end of the year.
[52:45] And then I just talked.
[52:46] Well, did you just put down my hours?
[52:48] Basically if you need me, tell me I just invoice what I'm doing and.
[52:52] But I was really leaving actually in December, January I think the last invoice was for December.
[52:57] And when Stephan Tual left or was being left, I mean there's another conversation.
[53:02] How he left the foundation is.
[53:04] It was not.
[53:05] He didn't agree with some people getting Ethereum is another story for another day, I guess.
[53:11] And.
[53:12] But he was really a crucial part in building up this Ethereum community.
[53:16] He like all this meetup culture.
[53:18] The meetup culture didn't really exist like that before he was going from place to place, finding someone, running meetups.
[53:25] So he was very important for that.
[53:27] And I, I know I was a coder, I press assignment who I co-founded Slock.it was also a coder.
[53:32] We needed someone who can talk to the people can do marketing and this stuff and we said well he has the right address book, he knows the right people, everybody knows him in the community.
[53:42] I think let's ask him if he wants to join us.
[53:44] And he did.
[53:45] And I think he was a very important part of making The DAO what it was later on he did some messages which I also didn't like and so he a bit in this craze what happened then?
[53:57] And I think the community was very, very hard with him because he was not always reacting maybe as he should in some situations after the hack but nevertheless he played a very important part in the history of Ethereum and also.

**SPEAKER_00:**
[54:10] Of course of the Dow and, and so, so Defcon was November 2015.
[54:15] So that was announced earlier in the year I think, I think September ish but ended up being canceled you know because the, the foundation were basically you know the same making out money piece but then primarily with ConsenSys funding and support, you know, hey, it's back on.
[54:30] So that was in, that was in London and you know significantly larger event obviously than Devcon 0 because it was the first you know, public Ethereum outing with Microsoft as a headline spot sponsor.
[54:43] You had Nick Szabo speaking as well, maybe Satoshi, maybe not Satoshi.

**SPEAKER_02:**
[54:48] I don't think strongly alluded to it in the presentation.
[54:51] It was funny.

**SPEAKER_00:**
[54:52] So, so yeah, how, how was that for you then Christoph?
[54:55] What was, you know it was totally.

**SPEAKER_01:**
[54:56] Different than Devcon 0 because this, this felt like now we're going out in the world and show to the public.
[55:03] It was a fancy space in London with a really fancy like almost cathedral-looking space to, to present again.
[55:10] We had Vitalik and Gavin talking about the vision of Ethereum and if you look at the talks being given I really think people entrepreneurs today should just rewatch them because they all have been 10 years too early.
[55:24] Be it about uPort building identity solution.
[55:27] I think it was a Boardroom doing that governance on chain many, many ConsenSys startups.
[55:33] Of course we as Slock.it think about well let's connect IoT in the blockchain again all of that 10 years too early.
[55:40] I remember also Simon speaking about not my brother, I forgot his last name but Simon speaking about everybody getting a token like he really predicted this token economy would now thrive which happened.
[55:51] So it was a great place to be.
[55:54] Everybody was looking into the future.
[55:56] Building the future was very, very exciting.
[55:59] It was very important that ConsenSys was funding this.
[56:02] It was crucial.
[56:03] The Devcon 1 moment, showing Ethereum is live.
[56:06] Now we show you what we will build with it.
[56:09] But still there were no applications running.
[56:11] So it's all visions and thinking.
[56:13] And so this one reason why when we then did the DAO, The DAO was held like almost the first real thing you could do with Ethereum.
[56:20] That's why so many people jumped onto it.
[56:22] And then the maybe to just finishing this off, the narrative changed.
[56:26] It was not anymore a DAO for the Universal Sharing Network, but maybe because of the creators we choose, which were like important figures in the Ethereum space and many other things.
[56:37] It turned into like an investment fund or like an index fund for Ethereum applications.
[56:43] Because now after 20, 30, 40 million was in.
[56:46] It was clear this was not just money for Slock.it and the USN.
[56:50] This was money for more cases and more people applied for it.
[56:54] It became like every decent application, or many of them, not everyone saying, I'm applying for getting funding from the DAO.
[57:01] So the DAO would pump all the applications.
[57:04] So it's like you invested in maybe Bitcoin 10 years, five years ago, became rich.
[57:09] Now you invested into Ether, went well, and now you can invest in the application layer.
[57:14] You do that through putting money into the DAO.
[57:16] This was not a story we told, not how we intended it, but that's how the narrative changed during the fundraising and then became that big.

**SPEAKER_00:**
[57:24] Yeah, I mean, it was interesting.
[57:25] You.

**SPEAKER_01:**
[57:26] You're saying that you're muted, Bob, I cannot hear you.
[57:28] Is it.
[57:29] Maybe it's just me?

**SPEAKER_00:**
[57:31] Can you hear me?

**SPEAKER_02:**
[57:32] I can still.

**SPEAKER_03:**
[57:32] I.
[57:33] I hear him.

**SPEAKER_01:**
[57:34] Sorry, I have an issue here.
[57:35] This was me system.
[57:37] So now I'm back.

**SPEAKER_00:**
[57:38] Can.
[57:38] Can you hear me?
[57:39] Can you hear me?
[57:39] Christoph?

**SPEAKER_01:**
[57:40] No, I have to switch back to.
[57:42] Let's.
[57:42] Can you hear me now?

**SPEAKER_00:**
[57:44] Yeah, I can hear you.
[57:45] I could always hear you some reason.

**SPEAKER_01:**
[57:46] Oh, we.

**SPEAKER_00:**
[57:47] We've heard you hear you anymore.

**SPEAKER_03:**
[57:48] This was like me an hour ago, by the way.

**SPEAKER_02:**
[57:51] Streamyard.

**SPEAKER_01:**
[57:53] Okay, my audio is completely broken, so I will try to fix this.
[57:56] We can continue.

**SPEAKER_03:**
[57:57] I basically had to like close it and come back again with my earphones, but I don't know.

**SPEAKER_00:**
[58:02] Perhaps while we're waiting, Kieran and Jim, you could talk a little bit about the the Strato launch at.

**SPEAKER_03:**
[58:08] I thought you were going to say you could sing a little song.
[58:10] I got nervous for a second there.

**SPEAKER_02:**
[58:12] You know.
[58:13] Okay, so in this period of time.

**SPEAKER_01:**
[58:15] we were working just reconnect, just turn it off and on again.

**SPEAKER_02:**
[58:18] We were working as part of ConsenSys and one of the kind of marketing, business development people at the time, Andrew Keys primarily had put together a partnership with Microsoft.
[58:29] I don't know if they ended up co sponsoring Devcon 1 person.

**SPEAKER_00:**
[58:32] They were the headline.

**SPEAKER_02:**
[58:33] Yeah, so they put money in for that because they also like paid for a bunch of PR and all those sort of things too.
[58:39] And so we had maybe a month or two lead time to work with them.
[58:43] And so the idea was that, you know, they've got cloud infrastructure, it's a good place to run blockchain nodes.
[58:49] They also have corporate clients that were actually very interested in the technology.
[58:53] We worked pretty closely with them in the run up to make our software available on the Azure cloud, as did Roman of the Java client, which to some extent was everyone's preference because people know Java in the enterprise world.
[59:06] But I think we stuck with it quite a bit longer than, than Roman did.
[59:10] And you know, so it was Blockchain as a Service was the big announcement.
[59:13] It was this December 2015.

**SPEAKER_00:**
[59:15] There was November.

**SPEAKER_02:**
[59:16] November.
[59:17] Was it November?
[59:18] Well, must have been December really.
[59:20] November.
[59:20] There was a.
[59:21] Once the announcement happened, there's a little tick in the Microsoft stock price which we always like, whoa.
[59:27] Like there's a little, little bump there.
[59:29] And a lot of excitement for sure.
[59:31] Got a million phone calls after that.
[59:33] That was like, you know, good, good feeling of being the hotness that only happens so many times in someone's life, you know.
[59:40] But tremendous interest on the back of the Blockchain as a Service announcement.
[59:44] We did a live demo.
[59:45] It was, it was fun.
[59:47] The Internet, you know, gets in vogue to make fun of the UK these days on the, on X, etc.
[59:53] The Internet in the conference facility was not so good.
[59:56] So I was very worried about the transactions actually going through, through.
[59:59] But they did during the live demo.
[01:00:01] I think there's footage of it somewhere.

**SPEAKER_00:**
[01:00:03] Can you hear us again now, Christoph?

**SPEAKER_01:**
[01:00:05] Yes, I can hear you.
[01:00:06] I hope you can hear me too.

**SPEAKER_00:**
[01:00:08] Okay, so the demo that you did at Devcon 1, again, another iconic event because yeah, you have that physical smart lock just sitting there on your shelf and you know, it rotated right, you know, right, you did your transaction.

**SPEAKER_01:**
[01:00:23] We just had a Raspberry Pi connected via, I think it was Zigbee or Z-Wave back then to the door lock.
[01:00:30] And on the Raspberry Pi we had actually an Ethereum client running and we had a smart contract on chain where you could send some money to it or ether, actually, when it received some ether, it would open up.
[01:00:44] This was basically the demo.
[01:00:46] But it was cool to see something physical.
[01:00:48] Some of them using Ethereum for, as I said before, the economy of things connected to IoT devices.
[01:00:54] Since most of the people in the room are still nerds and devs, they they love that kind of stuff.

**SPEAKER_00:**
[01:00:59] And there was also the kettle, wasn't there?
[01:01:01] The.

**SPEAKER_01:**
[01:01:02] Yes, there was also a kettle where we just turned a smart plug, like a power plug.
[01:01:07] We could also turn on off.
[01:01:08] Same protocol, same thing.
[01:01:10] So we just want to show it's not just the door lock company because actually you're not producing those.
[01:01:15] They're just connecting existing door locks to it.
[01:01:17] Wanted to show this idea of the universal sharing network.
[01:01:21] Everything which you can turn on, off or lock up and unlock could be now connected to this network.
[01:01:27] And everybody could put almost everything in there.
[01:01:30] Like a washing machine.
[01:01:31] You pay for using the washing machine or a bicycle lock.
[01:01:35] We even had padlocks connected to it so you could have it like your locker room and you have a padlock in front of it and sell whatever's in there by having someone pay to open the padlock.
[01:01:45] This was the generic idea.
[01:01:47] I mean, we got some VC money later after the, like in 2017, we built it.
[01:01:52] Nobody used it.
[01:01:53] It was like, not just too early.
[01:01:55] It was not.
[01:01:56] It was like everything for everyone all at once.
[01:01:59] And of course, nothing for no one.
[02:00:01] It felt like the app was not great.
[02:00:03] So we failed B2C wise at Slock.it.
[02:00:06] We then turned into more consulting projects to build IN3, which was an IoT client.
[02:00:12] Made some money with that at about 50 people actually deployed employed at the time.
[02:00:16] In 2019, when we sold the company to Blockchains, Inc.
[02:00:20] Jeffrey Berns, another.
[02:00:22] Another story.

**SPEAKER_00:**
[02:00:23] So I remember speaking to Stephan at the time.
[02:00:25] So Stephan was involved with that demo.
[02:00:27] Right?
[02:00:27] Right.
[02:00:28] It was Stephan who came up on stage to make his little cup of tea with the, with the, with the kettle there.
[02:00:34] But I remember speaking to him that he'd been concerned about what the reception for him would be like, you know, having had this, you know, passing of ways with with the foundation just two months before.
[02:00:46] But he was saying it was all very.
[02:00:47] It was all very friendly and people, you know, very excited about the project.

**SPEAKER_01:**
[02:00:51] Right.

**SPEAKER_00:**
[02:00:52] And saying actually about that IoT and pieces.
[02:00:55] So in January 2015, you had a demo that happened at the Consumer Electronics show, the CES in Vegas, which was a collaboration between IBM and Samsung.
[03:00:04] So the aforementioned Henning Diedrich, part of.

**SPEAKER_01:**
[03:00:06] That.

**SPEAKER_00:**
[03:00:06] And that again was months before mainnet.
[03:00:09] But you had a proto web 3 stack there, which was I think POC 5 of Ethereum.
[03:00:14] You didn't have Whisper, you had another thing called Telehash and you didn't have.
[03:00:18] You had BitTorrent.
[03:00:20] So there was this Proto Web 3 stack there and they had demos like a washing machine buying its own detergent and scheduling its own repair.
[03:00:27] So.
[03:00:28] So yeah, that, that was happening a little earlier and, and yes, I mean, so Slock.it itself did a number of these different products.
[03:00:36] Right.
[03:00:36] There was something with electrical charging and something to do with toll roads.
[03:00:40] Is that right?

**SPEAKER_01:**
[03:00:41] Right.
[03:00:41] We had a prototype running with RWE or innogy in Germany.
[03:00:46] They're doing like all the, at the time, most of the charging stations.
[03:00:50] So this was in general like we got a lot of attention of course also after the DAO hack and all of that.
[03:00:56] And so that's kind of why we became a consulting company because so many asked us could we do a prototype issue because there were not many Ethereum builders at the time.
[04:00:03] So we have been building on Ethereum now since one year or two years, which you could not find anybody doing this.
[04:00:08] So we are building lots of nice prototypes and some almost production stuff and always related to IoT devices connected to the blockchain.
[04:00:16] This was a core business.
[04:00:18] And on top of this you built those prototypes.
[04:00:20] We did a lot of work for the Energy Web Foundation.
[04:00:23] I don't know if you're familiar with them, this was in Switzerland.
[04:00:26] They are kind of a fork of Ethereum, focusing on all the energy use cases.
[04:00:30] He built most of their stuff in 2018, beginning of 19, until they hired their own developers.
[04:00:35] Gavin was also part of this a while.
[04:00:37] So yes, this was still.
[04:00:39] I mean if you remember this time, Kieran, you said there was so much enterprise interest, enterprises at the time.
[04:00:45] We're just learning, looking into this, wants to build prototypes, not yet production stuff.
[04:00:51] Um, so.
[04:00:52] And there was a huge demand for, for blockchain experts, for doing consulting, for going to conferences.
[04:00:58] Explain them what a blockchain is with.
[05:00:00] At every tech conference you needed some blockchain talk.
[05:00:03] And this was kept basically mostly us and they paid sometimes like €4,000 for a talk.
[05:00:08] Like as a company you said, well, we need the money, let's go there.
[05:00:11] So we, of course you also have to think about us as persons, as Simon and me.
[05:00:16] We didn't get any, any money for almost a year.
[05:00:18] Like we worked for.
[05:00:19] We were not rich people, we come from ordinary families and we said, well, we can work for like three to four months without a salary.
[05:00:26] Let's like build the DAO and then we becomes big.
[05:00:29] The DAO is paying Slocker to build it.
[05:00:31] Of course, after the hack it was clear there will never ever be a payment.
[05:00:35] So we can.
[05:00:36] We made zero money out of the DAO, so we needed to stop doing, start doing some work.
[05:00:41] And this was in the beginning.
[05:00:43] Let's do consulting for those large companies.
[05:00:45] This is how Slock.it began to survive.
[05:00:47] Many people said you can like bury Slock.it after what happened, like your name is burned forever.
[05:00:53] And we decided to to stay as a team.
[05:00:55] I mean as a founder team.
[05:00:56] We own our mistakes.
[05:00:58] Maybe we are open and transparent about it as much as we could.
[06:01:02] It was of course an honest mistake.
[06:01:04] I mean you can talk for.
[06:01:05] It could be another session just for the DAO.
[06:01:07] I mean the DAO is a lot of topics I just put here very shortly.
[06:01:10] Just, just talking about it from a company perspective.
[06:01:13] And then Stephan Tual, he was saying, well, he was trying to get VC money.
[06:01:17] Simon and I, we were doing those consulting gigs.
[06:01:20] And Once we had VC money, what happened as a company was we got 2 million euros and of dollars and then we built the product, hired people for that, got more and more consulting gigs.
[06:01:31] So we always said, well, let's do them and just hire more people.
[06:01:34] And the end we had like 50 people, five or 10 doing the product and 40 people doing consulting.
[06:01:40] And then we got bought by Jeffrey Berns from Blockchains, Inc.
[06:01:43] Remember, maybe at Devcon 3, I think where he did this big tour in Prague, right.
[06:01:48] Want to build a city?
[06:01:50] I think I love the vision.
[06:01:51] He obviously had money.
[06:01:53] He wanted to build it on top of Ethereum mainnet.
[06:01:56] I'll think about how maybe I can channel those billions into the right direction.
[07:02:00] Building is all as intended on Ethereum mainnet, which was working fine for the beginning.
[07:02:05] And then I found out once you're an entrepreneur, you never can be an employee again.
[07:02:08] So I had to leave.
[07:02:10] So.
[07:02:11] But it's maybe actually it's too far in the future.
[07:02:14] I mean, that's one thing I think I have to say here because you talked about Devcon 1 and you skipped a little bit Devcon 2.
[07:02:20] You said in Devcon 1, Stephan Tual was very concerned how people perceive him and they were very gentle, forgiving and nice to him.
[07:02:28] So he was well received and then he built the DAO community.
[07:02:31] I was super worried to go to Devcon 2 because this was after the DAO hack.
[07:02:36] I was like seriously thinking someone, they might beat me up there like around the corner, there are some people like, I kind of almost destroyed Ethereum with the DAO hack and so much attention to it and all the money lost for some people or like the time of crowdsale gone.
[07:02:51] It depends on how you feel it.
[07:02:53] So.
[07:02:53] But when I went to Devcon 2, people were so nice forgiving.
[07:02:57] Basically hugging me when I was giving the talk there.
[08:03:00] And the only thing I didn't like was the foundation telling me I was not allowed to speak about the DAO, which was like, what?
[08:03:06] Like I'm speaking here to the Ethereum community.
[08:03:08] Well, how can I not speak about the DAO?
[08:03:10] And so I talked about a pretty boring talk about security.
[08:03:14] And I think every second talk was about security at Devcon 2.
[08:03:17] It was just about how we get those smart contracts secure.
[08:03:20] So I gave a rather boring talk, but in the end I just said, well, thank you for your understanding.
[08:03:25] And it was hard time and so on.
[08:03:27] And they were like somewhat.
[08:03:28] They've been standing ovations.
[08:03:30] I remember becoming emotional because this was.
[08:03:32] I did not expect this.
[08:03:34] I really expected like, guy, you messed up Ethereum.
[08:03:37] Like we almost lost it all.
[08:03:39] So I think this just speaks to the Ethereum community, how they treated Stephan, how they treated me.
[08:03:44] Even though mistakes were made, honest mistakes, at least from what I can tell.
[08:03:48] This is such a great community of really nice people who really want to change the world, capable and also now financially capable of really doing things.

**SPEAKER_00:**
[08:03:57] I was watching that video quite recently actually and and yeah, it was quite cut off a little bit.
[09:04:02] You know, it was quite a long ovation there and and yeah, you could certainly see that emotion in you.
[09:04:08] And that's when we first met actually was in Shanghai for Devcon 2.
[09:04:12] I remember was was on the sidelines there in that main, main conference hall and yeah, it was lovely to see that, that's for sure.
[09:04:20] Okay.

**SPEAKER_02:**
[09:04:21] Yeah, I think good notes.
[09:04:22] Just.
[09:04:22] Bob, you were the one who tried to impose half hour to hour rule.
[09:04:26] We're at a solid 120 right here.

**SPEAKER_00:**
[09:04:28] Me the other time, maybe we, you know, we've reached a, you know, a good kind of end point, I guess.
[09:04:34] So what, what happened after Blockchains, LLC for you then?

**SPEAKER_01:**
[09:04:38] So because of time, I keep it short.
[09:04:40] So, yes, we got bought by Jeffrey Berns, Blockchains, LLC at the time again, the reason for this being he want to build a new city in the desert.
[09:04:48] He want to do all on IoT, all on Ethereum from scratch.
[09:04:52] And as a developer, dream building from scratch on a green field on top of Ethereum with our Tech and I felt comfortable in the beginning.
[09:05:00] In the end I felt like we need to release stuff and there were some voices at the company which didn't want to release until like a very, very big product was done.
[09:05:08] For many reasons that didn't happen.
[09:05:09] I don't want to get into like that too much.
[09:05:12] So after two years I left Blockchains.
[09:05:15] Back then it was called Inc.
[09:05:16] They made a change in their name and I did for six months.
[09:05:20] I did really nothing.
[09:05:21] I forced myself to do nothing which was great after so much stressful years.
[09:05:26] And then I started a venture studio called Kopos Ventures where we tried out many different ideas.
[09:05:32] We had EM3 which was a decentized messaging protocol.
[09:05:36] Gashawk.
[09:05:37] You can save transaction costs on Ethereum.
[09:05:39] What else did we have?
[09:05:41] So we have some domain name stuff but we didn't release it at the end.
[09:05:44] But the biggest one was Tokenize.it and this was me being you built something for German.
[09:05:51] For now, German startups in the end we want to do it all over Europe and we just tokenizing their shares and do fundraising.
[09:05:58] So in summary it's like a Web3-based AngelList for Europe.
[10:06:03] It's the one sentence description for Americans also to understand, you know AngelList it's a great tool for business angel investing.
[10:06:10] You want to do the same for Europe, for all countries there and build it on on chain.
[10:06:15] So tokenizing all those shares and enable private as well as public fundraising.
[10:06:20] So some called legal ICOs if you want but also for private fundraising.
[10:06:24] Our customers currently we have more than maybe a good, good way to end end this.
[10:06:29] We have now more than 400 investments from more than 320 business angels and more than 50 companies.
[10:06:36] Those are traditional German GmbHs raising from super current conservative business angels and doing it completely on chain.
[10:06:45] They're paying in stable coins getting their tokenized shares.
[10:06:48] India non custodial wallet, they're all getting a Gnosis Safe wallet from us using Privy for login.
[10:06:55] So we build it as intended and we get normal people to use it.
[10:06:59] For me this is kind of a dream come true because I'm out of I love the Web3 bubble.
[11:07:03] I love this community, I love to work inside there.
[11:07:06] But for me Tokenize is a way to make this technology available where it belongs like to startups and investors outside of our Web3 bubble.
[11:07:15] And I'm super, super happy that I could keep up those values that they have complete platform is non custodial.
[11:07:22] They have their safe on Ethereum holding their tokens, paying stable coins.
[11:07:26] So I'm Very happy to see this over the next years.
[11:07:29] You want to basically roll out this all over Europe and become.
[11:07:32] Yes.
[11:07:33] The Web3-based AngelList for Europe.
[11:07:35] That's the goal.

**SPEAKER_00:**
[11:07:37] Fantastic.
[11:07:38] Hope to see you@Devcon 8.

**SPEAKER_01:**
[11:07:40] Me too.
[11:07:41] I'm looking forward to it and as of now, and I don't intend any change, stick to Ethereum.
[11:07:46] I love the community I continue building and try to get a lot of people using it.

**SPEAKER_00:**
[11:07:51] Have you been to every Devcon?

**SPEAKER_01:**
[11:07:52] Yes, I said yes, I've been to every Devcon.
[11:07:55] The last one was actually the first song that I didn't give a talk and also went to every EthCC except of one where there was Covid.
[12:08:01] There was a reason they couldn't come.
[12:08:03] But yes, I'm actually I intend to continue to come to every Devcon.
[12:08:07] It's like you meet the people like Thrift Queen, Lefteris, of course, Vitalik and many others.
[12:08:12] It's just a sweet spirit there.
[12:08:14] Nice community.
[12:08:15] Love seeing how it all grows.
[12:08:17] Listen to those exciting talks.
[12:08:19] I mean it's for tokenizer.
[12:08:21] It's not as relevant.
[12:08:22] It's not like our customers or it's a tech.
[12:08:24] Of course.
[12:08:25] We're just doing an ERC-20 tokens on Ethereum.
[12:08:28] It's super easy.
[12:08:29] No deep tech.
[12:08:31] Sometimes I miss doing deep tech, but.
[12:08:33] Well, I just enjoy being there, seeing what it all what all happened and remembering those magic days.
[12:08:39] And just like only once in a lifetime or two times in a lifetime, you have this.
[12:08:44] This moment where everything comes together.
[12:08:46] The right time, the right place, the right people.
[12:08:49] This certainly where those like one and a half years I worked for Ethereum, but definitely like the prime of my career in terms of who I work with, what we accomplished, the impact we had on the world and this sweet cypherpunk spirit there and what we did there.
[13:09:02] It was really great.
[13:09:03] I always sometimes get emotional thinking about this and meeting those people again at Devcon.

**SPEAKER_00:**
[13:09:08] Fantastic.
[13:09:09] Well, thank you for all your contributions to that success.

**SPEAKER_01:**
[13:09:12] Likewise.

**SPEAKER_00:**
[13:09:13] All the best.
[13:09:14] Okay.
[13:09:15] Oh, just one more.
[13:09:16] Where can we find you?

**SPEAKER_01:**
[13:09:18] You can find me usually on Twitter for the Ethereum people.
[13:09:21] @ChrJentzsch, of course.
[13:09:23] I have a complicated name.
[13:09:24] Not many vocals in there, but you find it.
[13:09:27] Or of course on LinkedIn.
[13:09:28] Actually from my company.
[13:09:30] I'm more active on LinkedIn, which I was never before, but that's what we get our clients.
[13:09:34] Let's Tokenize.it.
[13:09:35] Yeah, but usually you can find me on Twitter.
[13:09:37] Follow me there on LinkedIn.

**SPEAKER_00:**
[13:09:39] Excellent.
[13:09:40] Okay, thanks so much.
[13:09:41] Have a great day.

**SPEAKER_02:**
[13:09:42] Thank you.

**SPEAKER_01:**
[13:09:43] You too.
[13:09:44] That's great talking to you by.