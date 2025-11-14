**SPEAKER_02:**
[00:00] Okay, recording is in pro—uh, is in progress, it says. So hello, everybody. Today, delighted to have Christoph Jentzsch with us.
[00:08] We did attempt to record this, Christoph and I, two weeks ago, but I forgot to press the record button, so we spoke for an hour or so and then it was not recorded.
[00:16] So this is round two. So hello, Christoph. How are you?

**SPEAKER_00:**
[00:20] Hi, Rob. Nice to meet you again.
[00:23] I'm doing good. I hope you too. Thanks for the invitation.

**SPEAKER_02:**
[00:26] Fantastic, yeah. So Christoph and I, our paths crossed for the first time way back—
[00:32] back in 2015 when I was trying to do C++ Ethereum on my smartwatch.
[00:36] And this was around the time that Christoph was still at the Ethereum Foundation.
[00:39] And then I think I crossed paths a number of times since—and Kieran’s too. Indeed.
[00:44] So, Christoph, what were you doing with your life before you found Ethereum and joined this crazy journey?

**SPEAKER_00:**
[00:50] So the journey started in 2013.
[00:53] I was doing my PhD in theoretical physics, actually about self-organizing systems—like six months in mathematical biology and other things.
[01:01] So I was studying systems which have local rules and global behavior.
[01:05] And I came across Bitcoin, which is just a small set of local rules and a global behavior as a currency.

[01:10] But the reason I came across this was I was looking for cheap GPUs—like graphics cards—and the Bitcoin miners were selling their GPU mining rigs to get some FPGAs and later ASICs.
[01:20] And so that's how I got into Bitcoin mining.

[01:23] I bought my first Bitcoin, got into this bubble, read everything I could about it.
[01:28] Then I came across the white paper from Vitalik in early 2014, something like January or February, in some Bitcoin forum.
[01:35] And I was already totally in love with the idea of Bitcoin being a decentralized currency and all the characteristics and features of it.

[01:42] And this white paper by Vitalik—if you read it again—it's almost a prophecy. Except for NFTs, everything's in there: DAOs, ENS—domain name systems—and all of that.
[01:53] So for me, it opened up this option of building applications with the same characteristics as Bitcoin, but not just a currency—everything else.

[02:02] Then I started reading everything about it.
[02:05] In 2014, in summer—the crowd sale was in 2014, right? So around that time I watched a video from Gavin Wood at some conference in the Nordics.
[02:14] He talked about Ethereum—I loved it. He said he wanted to open an office in Berlin and was looking for C++ developers.
[02:21] I was a C++ developer. In theoretical physics, it's 90% software development.
[02:26] I said, well, I want to do this.

[02:29] So I took my parental leave time, plus some vacation time, and paused my PhD for like three to six months and said, I will return after I'm done.
[02:37] I thought this was just a short project. They raised money, maybe six, maybe twelve or eighteen months, and then it’s over.
[02:44] When I started, I thought about maybe three to six months, and then I’d go back to my PhD.

[02:49] So I worked there with Ethereum—with Gavin Wood—it was a great time.
[02:54] And then I just decided to stay. It was so exciting.

**SPEAKER_02:**
[02:57] So you never got to be a doctor?

**SPEAKER_00:**
[02:59] No, I'm not a doctor.
[03:01] I did not finish my PhD, although I only had six months left, which was kind of a pity.
[03:06] I worked for three years on that.

[03:08] But I also had, at the time, I think four or five kids. I needed some money.
[03:12] I didn't get much money as a PhD student, so I did software development as a side hustle basically.

[03:17] So when I got this project, I said, well, let's do this for two or three months as part of my parental leave time, and then I can return.
[03:23] And then I decided to really interrupt my PhD. I thought I will maybe return one year later, because I thought the foundation would eventually run out of money.

[03:31] Because they’re not making any profits—they just raised donations, then they'll spend them—then it’s over. Then I can continue my PhD. That was originally the plan.
[03:40] Just came different.

[03:42] I mean, I guess it's never too late, right?

[03:45] I actually sometimes think about it—that I should return.
[03:48] It's just so much to learn again.
[03:50] I'm right now doing Tokenize It. I'm basically working on tokenizing German companies.
[03:55] It works very well.

[03:56] And so currently I'm not planning on getting back anytime soon.

**SPEAKER_02:**
[04:00] No, because—I mean, famously—you had, you know, Dr. Gavin Wood and Dr. Christian Reitwiessner as well.
[04:06] And I think there were a couple of other PhDs as well.

**SPEAKER_01:**
[04:09] There was definitely.
[04:11] I also dropped out of mine.
[04:13] I was actually in mathematical physics too. Interesting. Similar background.

**SPEAKER_00:**
[04:17] It's actually the same.
[04:18] Like theoretical physics—it's the mathematical part of physics.
[04:22] I enjoyed it very much.
[04:23] I did thermodynamics and statistics, mostly software development.
[04:27] It was really fun.

**SPEAKER_01:**
[04:30] Well, by the way, Jim is trying to join.
[04:32] I don't know if there's anything that needs happening. He’s getting some browser issues.

**SPEAKER_02:**
[04:35] Yeah, yeah. Well, he'll pop up and we can add him.
[04:38] Or if he's... I'll say then—then never mind.

[04:42] So Christoph, in terms of, you know, getting hired into fdev—and I'm sorry if I just missed it—so...

**SPEAKER_00:**
[04:47] How did that happen? Did you meet Gav at a meetup?

[04:51] Yes, I actually listened only to his talk. It was an online thing.
[04:54] And I actually just wrote him an email and said, "Look, I would love to join Ethereum. I love what you're doing."
[05:00] He invited me to meet him in Kreuzberg, Berlin, which again is about a two-hour train from here.
[05:06] So I went up there, met him.

[05:08] I remember the first conversation—he was talking about all the stuff they were going to build and said, "Well, what can you do?"
[05:13] I just asked him, "What's the most complicated stuff you have right now? Give me a complicated task. I’ll somehow figure it out."

[05:20] So he talked about the Ethereum Virtual Machine, which needed some testing.
[05:24] So I just picked working on testing the Ethereum Virtual Machine, or writing tests for it.

[05:29] Back at the time, I actually had no real idea what he was talking about.
[05:33] Meaning, of course, I did understand on the white paper level—I did understand what Ethereum was about.

[05:38] But Gavin had this skill of writing the Yellow Paper, which is still an incredible work. Like, it's such a great specification—different from Bitcoin, really having a specification so multiple clients could be built.
[05:49] And in there, he defined the Ethereum Virtual Machine.

[05:52] I think I read the paper six or seven times. I felt like I was one out of—I don't know—10 or 20 people in the world at the time who really understood the Yellow Paper.
[06:00] I did corrections to it. I have some pull requests actually in the Yellow Paper GitHub repo.
[06:05] Added missing definitions and stuff like that.

[06:08] Then what I mostly did was writing tests according to the specification,
[06:11] which then were—with the help of the C++ client, because this was his team.
[06:15] So I was working also on the C++ code base.

[06:18] And so Geth, PyEthereum, also the JavaScript version, and what else did we have?
[06:21] Like the Haskell client and others.

[06:23] I was basically using my tests to see if they implemented the EVM—also the state transitions and block creation—correctly.

**SPEAKER_02:**
[06:30] Yeah.
[06:31] So, I mean, just to have some timeline for the viewers.

(Transcript continues ...)