**SPEAKER_00:**
[00:01] Okay. Welcome, everyone.
[00:03] We have a very special and very timely topic today, privacy on-chain and the rise of Zcash.
[00:10] And we sort of have a special guest today.
[00:12] So I'm Victor Wong.
[00:14] I am founder and chief product officer at BlockApps.
[00:17] I'll get to our normal guest, but, today, we have Jim.
[00:19] Do you wanna give us a quick intro?

**SPEAKER_01:**
[00:21] Yeah. I'm also—I've known Victor and Kieran for years.
[00:25] I'm one of the founders of BlockApps and CTO.

**SPEAKER_00:**
[00:28] And you're here in particularly because I would call you a Zcash expert having written your own Zcash client.

**SPEAKER_01:**
[00:33] Well, I I I think I'm I'm more aspirational at this point in time.
[00:37] I mean, the way I learn about things is I try to—

**SPEAKER_02:**
[00:39] How many more expert people do you think there are on, say, Zcash in particular on the planet?

**SPEAKER_01:**
[00:43] No. The problem that I have is that I I was I was sort of halfway in the learning process last year.
[00:48] So the way I learn about things is I try to, like, write write a client for it.
[00:52] So I was I was doing that, but then we got pulled in different directions.
[00:55] I got to the point where I had sort of replicated the actual client that could connect.
[00:58] It would bring the data in.
[01:00] It would bring the proofs in.
[01:01] But just about when I was getting to the good parts, that's when when we moved on to other things.

**SPEAKER_00:**
[01:05] Well, we're gonna put the number—answer my other question.
[01:08] Put the number at between, like, 10 and a 100.
[01:10] May maybe 10.
[01:12] I would say there there's definitely less than 20 people who have written their own Zcash clients, probably.
[01:16] Well, yeah. Yeah. There's probably some core contributors.

**SPEAKER_02:**
[01:18] I imagine there's more than a handful into Zcash.
[01:21] But, you know, when Jim says non-expert, you know, it's like, there are—let's say yes.
[01:26] I'll I'll expand the range.
[01:27] Five to a 100 people who understand Zcash better on on the planet.
[01:31] Big, big, big range there, but we're talking about pretty small numbers in absolute terms.
[01:35] So yeah. Yes. Exactly.

**SPEAKER_00:**
[01:37] I say if Jim's not an expert, I don't know what even expert means.
[01:40] Anyways, Kieran, do you want to give a quick intro of yourself before we—

**SPEAKER_02:**
[01:42] Certainly. I'm our CEO. Been on these before.
[01:45] By the way, Victor, we're letting Jim off the hook, calling him a special guest.
[01:48] He has to do this all the time now with our, you know, continued—in the public press.
[01:52] So okay.

**SPEAKER_00:**
[01:52] Special now. Not special in the future. Special today.
[01:56] Today is special, but it's the first of many.
[01:58] Let's just say that.

**SPEAKER_03:**
[02:00] I was looking through the the the prior videos.
[02:02] Jim has never appeared on one of our own Spaces.
[02:05] He's only been on early days of the year. Okay.

**SPEAKER_00:**
[02:07] Older drinks. Well, there you go. Oh, no. You found out.
[02:11] But it won't be special soon.
[02:14] Bob, by the way, since you've spoken up, can you give a quick intro to yourself?

**SPEAKER_03:**
[02:17] So hi. I'm I'm Bob. I'm head of ecosystem.
[02:20] And, yeah, been doing a lot of a lot of Spaces.

**SPEAKER_00:**
[02:23] Yeah. So I I think, you know, to level-set because I think there's a lot of misunderstanding about what privacy is.
[02:29] What how would you define blockchain privacy and why do you think it's important?

**SPEAKER_03:**
[02:32] Who's that question for?

**SPEAKER_00:**
[02:34] Could be for anyone. Whoever wants to go.
[02:36] Kieran, you want to kick us off? Okay. I'll take it.

**SPEAKER_02:**
[02:38] So and for the—I assume that the viewer is pretty deep in the space, but I'll I'll I'll bring it down to a fairly low technical level.
[02:44] So blockchains are great. They let you move digitally scarce value from party to party.
[02:50] And the way that this is typically done is that you've got a big address, which is almost, but not quite a public key, and you sort of sign a message that says, I, Kieran, but it's not Kieran because it's this address, send, you know, three Bitcoin to Bob, and it doesn't say Bob.
[03:04] It's another address.
[03:05] You don't quite know who either of those parties are.
[03:07] However, you've got the address forever, and often it is the case that you can piece together what happened based on that address.
[03:15] Let's say you're on a centralized exchange, which has KYC'd.
[03:19] It knows how to associate you to maybe a withdrawal address.
[03:23] It may not know down the line, but if you start to get a bunch of data points, you can kind of piece together who sent what to whom, and you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone.
[03:36] And it's not—while it's a cryptographic technology, it's not necessarily a private technology.
[03:41] And this has been a problem both in the consumer setting just for, you know, people don't like this.
[03:46] Satoshi makes a comment, I believe, in the white paper saying that, you know, obviously, to prevent the double-spend problem, which basically just is just that to ensure that it can't—I mean, can't be created or destroyed except by the agreed mechanism.
[04:03] Obviously, you need to know the whole history.
[04:05] And so he sees the problem as intrinsic, but some technologies come out later that maybe calls that into question that that we'll talk about.
[04:12] It's also an enterprise problem.
[04:14] So we can we can talk separately about our experience there.
[04:16] Sort of what the enterprises want is kind of the same as what the public blockchain people want except with selective visibility.
[04:24] So they wanna say you're doing, like, a on-chain stock trade, which is actually now starting to happen.
[04:29] You sorta wanna know the other party has the stock.
[04:31] You don't necessarily wanna know who the other party is, but you you wanna know that they acquired that stock legitimately.
[04:37] And then when you get it, you wanna be able to pass it on legitimately in the same way.
[04:41] And then there's sometimes this extra requirement that, like, the regulator can see everything. You know?
[04:46] So you you want sort of, like, a unlinkability of balance to person or company, but also this mass preservation property that I was talking about—can't create or destroy assets.
[04:55] They have to be acquired legitimately and and so on.
[04:59] So it's a perennial problem and closer to solved, you know, but we we can go into that shortly.
[05:04] Yeah. Bob, did you wanna add anything to that?

**SPEAKER_03:**
[05:05] Yeah. So, I mean, going back to those Bitcoin, you know, beginnings in the Bitcoin white paper, you know, it it it just talks about severing identity from transactions.
[05:17] But but really, that's just pseudonymous, you know, not not anonymous.
[05:22] And I think a lot of people didn't understand that differentiation back in those early days, and it's like, oh, Bitcoin's private, untrackable, you know, digital money.
[05:31] But, you know, very rapidly, you have blockchain analytics coming in, you know, looking for correlations and patterns and it's like, yeah, that's—you're not getting a lot of security, you know, even if you're not reusing addresses, just just normal things that people would do.
[05:46] There's there's lots of correlations and, you know, you can get unmasked that way.
[05:50] But, yeah, Satoshi did talk a bit about zero-knowledge.
[05:53] I can't remember who raised it. Somebody raised it early, and and he was like, yeah. You know, that would be interesting if we could do that.
[06:01] But but it was just like a lot of that cryptography, you know, just didn't—hadn't happened. You know?
[06:08] So Zcash started in 2016 and it was only around that kind of time or a little before that you started having, you know, these these papers on on SNARK constructions and going through all these different kind of rounds.
[06:22] So, yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path.
[06:27] You know, they are an immutable public ledger forever.
[06:30] Ethereum even worse because it's an account model.
[06:33] So you're you are reusing the addresses all the time. Right?
[06:36] And if your address is unmasked, you are forever doxed.
[06:40] That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address of his, which is probably not desired.

**SPEAKER_00:**
[06:49] Well and I I you know, you guys have been talking about Satoshi.
[06:52] But, Jim, I remember I think it's, like, earlier at, like, 2014.
[06:57] Vitalik was talking like he was like, ZK-SNARKs will fix all of this at some point in time.
[07:01] Do you remember that at all?

**SPEAKER_01:**
[07:02] Well, I mean, like, I think we went through a learning process about privacy, and and and that's sort of, like, we're we're understating this right now.
[07:10] Maybe it's because we put a lot of time and effort into some privacy solutions that technically worked, but were a business failure, I think, is fair to say.
[07:18] And, so so, you know, the audience can learn from our our, like, sort of failed mistakes in the past right now.
[07:23] But, we sort of built—so we had heard years ago of about ZK, but we sort of just I I don't know.
[07:31] At the time, looked into it and said, like, oh, this looks like overly complicated.
[07:35] You can get privacy through these other means.
[07:37] And we ended up building a system that that allowed for sort of, like, quick spin up of private chains that everything was sort of, like, in a an encrypted tunnel, and you could you could have, like, these chains completely secure.
[07:49] Nobody else would see what was happening there.
[07:51] But but long story short, you know, slow learning process.
[07:54] We we found out that customers want everything and and to the point that it made it worthless.
[08:04] Like, they we would go into enterprise.
[08:05] We would say, like, oh, you can set up these private channels with others.
[08:08] And they love that because they could sort of control that, and they could control who goes in there.
[08:12] But then once everything was going through these private channels, then they wanted to be able to, like, transfer from private chain to private chain, and that's where everything started to fall apart.
[08:20] And getting things back onto the main chain became sort of this extra complicated system.
[08:26] And and at the same time, customers wanted to have, like, full flexibility in having, like, extensions to, Solidity where where you could just, like, name a chain and send some money from chain A to chain B.
[08:39] And, really, the only way to make that stuff work is you have to go back to ZK.
[08:43] So ZK is overly complicated, but it is necessary.
[08:49] And and so so we started looking at that again, but I think, like, the safe thing to do is start with a a proven technology.
[08:56] And Zcash has been around for years and and nobody had stolen money.
[09:00] And this is just sort of like a subset of of ZK, but it's it's it's kind of a cool thing.
[09:04] You can you can build what they call tumblers of money.
[09:06] You throw a bunch of money in, and then the money that you put into the tumbler is—you know how much went in, but but the ownership is completely scrambled up.
[09:16] And at any time, you can go and and transfer money from within the tumbler from one user to another, but only the users who did the transferring and got the money know what was there, but nobody else can see what's happening.
[09:27] So, again, like, you have these systems of multiple users with lots of money, but you don't know who owns percentage of of the money.

**SPEAKER_00:**
[09:34] Yeah. Actually, before we even go that far, can we talk just, like, what is ZK and how does it work, and why is it an important part of the solution?
[09:41] I I wanna pull back for also a a second.

**SPEAKER_02:**
[09:43] I remember I think there was an Ethereum meetup in New York.
[09:45] I'm not sure if either of guy you guys were there.
[09:47] I think I spoke at it, maybe.
[09:49] And there was also a Zcash, I think, presentation there.
[09:54] And it was, at that time, taking seven minutes to generate the ZK proofs.
[10:00] So yes.
[10:01] Yeah. If you wanted to make a transaction.
[10:03] You'd like, do this thing. It took seven minutes, and then the verification was kinda fast.
[10:07] Once you had it and you sent it to the network, things could go on, you know, but the the usability was not there in those days.
[10:13] This is part of the reason we weren't, like, gonna tell our enterprise customers, like, oh, yeah.
[10:17] Let's let's ZK everything.
[10:18] You know, even if we had it all integrated nicely, there's a lot of devil in the details.

**SPEAKER_01:**
[10:22] I know it was unbelievably slow for a while, and I think it's fixed.
[10:25] But yeah.
[10:26] I know. Well, it's complicated.
[10:28] I mean, this is what I was trying to to say before.
[10:30] It's like, I have, like, sort of nuts-and-bolts experience of what's going on in Zcash.
[10:34] But the more complicated world of zero-knowledge, that that's my aspirational part right now.
[10:40] I can sort of see pieces moving within there, but but would hesitate to speak more broadly on this.
[10:46] Except let's say that that that it is more complicated than any of the, like, for instance, Ethereum client implementation stuff that we were doing back in the day.

**SPEAKER_00:**
[10:52] Yeah. Yeah. Can you give a high-level summary of what zero-knowledge is?
[10:56] Like, I think very few people understand.

**SPEAKER_02:**
[10:57] I I have a good layman example, I think, and Jim can correct me.
[11:02] So I I did want to take a theoretical cryptography class, and the example they bring up is the CEO problem, so to speak.
[11:10] So we got two CEOs, and they're high-ego guys. You know? And they wanna know—

**SPEAKER_00:**
[11:15] Does that stem from experience, Kieran? Or yeah.

**SPEAKER_02:**
[11:17] Yeah. Let's think about myself.
[11:19] They wanna know who has the most between the two.
[11:22] But they don't wanna know how much money.
[11:24] They merely wanna know which one has more.
[11:27] And you would think that there wouldn't really be a way to create a scheme in which they could learn that information and nothing else, but there actually is.
[11:37] I and, again, this is almost ten years ago now, so I may be describing the example incorrectly.
[11:42] But, yeah, that's that's like a case where you might want zero-knowledge.
[11:45] Similarly, like, you know, like an ID check in a bar.
[11:48] You're leaking all your personal info when you hand the ID to the bouncer, your home address, your full name, your date of birth, you know, etcetera.
[11:56] So you may wanna prove to the bar that you're 21 without handing any other info over, basically.
[12:02] I think this is the general setting that that it ends up at.
[12:05] Jim, do I you wanna take them, run with it, correct it?
[12:07] Yeah.

**SPEAKER_01:**
[12:08] So this is when you first look up zero-knowledge, there are lots of little examples like this.
[12:12] They're all pretty cool.
[12:14] But and and what what's really happening in Zcash is that what you're trying to do is pass money from person A to person B.
[12:21] And person A wants to prove to person B that they have the money and that it was actually actually transferred, but without giving away the amount of money that person A has or without person A learning how much that person B has.
[12:33] Just that, you know, that the state before was that that you had the amount and that the state after is that it was transferred over.
[12:39] And then also no one else in the world can can know this.
[12:42] So you're you're you're proving sort of the important parts, not others.
[12:46] Zero-knowledge could get pretty complicated too because when when you start looking into it, there are a lot of one-off examples, like like you're talking about, that you sort of see a solution to.
[12:55] But the problem comes about in trying to come up with a sort of a generic solution where you can almost just compile any any amount of code into some ZK proof and then and then run that for anything.
[13:06] I don't remember because it's been about a year now, but but in Zcash, there were multiple multiple zero-knowledge proofs in there for various aspects.
[13:14] If I were I you know, I'm I'm I might be making up some of the details here, but I think there was, like, one proof was, like, to show that you had more than such and such money before the transfer.
[13:22] I I might have it slightly off, but that there were multiple of these zero-knowledge algorithms in there.
[13:27] But put together, they allowed for the for the full sort of transfer of of money within the tumbler.
[13:33] And each one sort of had been worked out independently of each other using a more generic system where they compiled certain certain algorithms in there.
[13:42] Let me Does that make sense? So making a generic can get really complicated.

**SPEAKER_02:**
[13:46] Terminology for the listener that you've heard that I barely remember.
[13:50] So SNARKs and STARKs were a thing that Vitalik was talking about a lot and still does.
[13:56] So it's like succinct, non-interactive, argument... something. I can't remember. Like but basically interactive proof. Yes. But what's the whole acronym?
[14:06] But so there is a way, I think, to take an arbitrary computation and to prove that it has a certain result without revealing, like, the intermediate states and so on.
[14:18] But it's not computationally feasible.
[14:20] Like or it's it's just so slow that if you try to do it that way, it becomes very difficult.
[14:27] So I believe just just tying back to Jim's point.
[14:31] Like, you could try to do this in a generality.
[14:33] Like, I can—like, the EVM. Like, I can verify—there is ZK-EVMs.
[14:37] Like, I can verify any computation that comes out of this thing.
[14:40] And I think the problem with them has been performance.
[14:43] And so the Zcash people, I guess, had to decompose every little step into specific ZK circuits.
[14:51] Right? Like or Yeah. Yeah.
[14:54] So, yeah, it's very, very low-level programming thinking in the the ZK world.
[14:58] Like, literally, there's there's circuits that you end up compiling and and and so on and so forth.

**SPEAKER_01:**
[15:03] So, yeah, Zcash at the moment is focused on that today.
[15:05] And and sort of by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one tumbler problem without going any more in-depth than that.
[15:13] So this isn't like—like, in the dream world, you would take any, like, Ethereum contract and pilot somehow as a as a, you know, something zero-knowledge and then prove that that that you had run the the full contract.
[15:23] That's something that, at the time, at at least so far in the the world as it is, I I didn't wanna get into it or or have us get into the company.
[15:30] But just to have these tumblers in place, I think that solves a lot of—

**SPEAKER_03:**
[15:32] Yeah. So Zcash is onto its fourth round of different cryptography.
[15:37] So I forget what they're called, Sapling, something else. We're onto Orchard now.
[15:42] But but, I mean, that's been now over the course of nearly a decade.
[15:45] You know, each time you've got another sort of two years worth of leading-edge advancement.
[15:51] And and, yeah, like, talking about that performance thing.
[15:54] So it's something which I think has been a a key piece in in Zcash price appreciation recently has been the arrival of a functional mobile wallet.
[16:05] So that's called Zashi, which is made by the Electric Coin Company.
[16:10] But you're basically at the point where you can run that proof on your phone.
[16:13] So something which used to be laptop seven minutes is now phone a second.
[16:20] So what you've seen, if you look at the size of these shielding pools where these pools are effectively like, you know, all of these things are all, you know, mixed and hidden together.
[16:30] Right? The the more that you've got in a pool, the more, you know, and and the more unlinkable you are.
[16:36] If you have a you know, if you if you do something simple like ring signatures where you just—whatever—I think, Monero has got 16 transactions that that, you know, get all joined together.
[16:47] So you can trace through that to a degree.
[16:51] But if you've got, you know, hundreds or thousands or millions of people in that same pool, you know, it's it's effectively, you know, completely anonymous at that point.
[17:01] But if you look at the stats of usage of these particular pools, are you seeing what proportion of the money supply has been shielded versus being transparent?
[17:11] I guess that's just another thing to say, right, is is Bitcoin is transparent, you know, so same same with Ethereum, but then they they they use the world word shielded to talk about, you know, that you are within this anonymity set.
[17:25] So these earlier rounds, you know, you had a bit of use, but not a ton of use.
[17:29] But right now, I can't find the view, but it but it was something like about four or 5,000,000 of the 21,000,000 were within that shielding pool.
[17:39] So, you know, a significant chunk of it is shielded now, which was never the case in the past.
[17:45] You know? I remember on ETC at some point, we were looking at whether we were gonna bring over the precompiles to do with some of the curves.
[17:52] You know? I don't know if you remember that happened in Ethereum at some point, but one of the like curves, I think, went into the precompile.
[17:58] And we were talking about whether we were gonna, like, do that or not.
[18:01] And really, talking about gas limit as well, you know, like, how how gas expensive would operations be using these things even.
[18:08] And the stats at that time were, you know, it's like maybe 2% of transactions on Zcash were shielded, something like that.
[18:16] You know, it's basically, like, not being used at all, you know, functionally pretty much identical to Bitcoin.
[18:22] But probably a lot of venues is going, yeah, I'm using Zcash.
[18:25] I'm private. It's like, yeah, you know, you cannot—not at all.
[18:28] It's you're getting zero benefit at all.
[18:30] But, yeah, that's that's really happening now.
[18:32] And I think it's just, you know, these rounds and rounds of years and years of research and then implementation of those and engineering effort, and it's like, hey.
[18:41] It works now.

**SPEAKER_00:**
[18:42] Well, I just curious from from your standpoint, Jim, like, is it a technological advancement that has created, or is it just simply that these tumblers have gotten big enough that they offer real privacy?
[18:54] Do you know what I mean?

**SPEAKER_01:**
[18:55] It's I mean, any of these things are technological advancements.
[18:58] But, I mean, you wanna have the tumblers big enough so that that you have some amount of anonymity within there.
[19:04] It's not like if it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_02:**
[19:07] I I need to interject.
[19:08] I I have a crypto friend who was texting about thirty seconds ago about whether I like Zcash at this price.
[19:15] This is a prerecorded podcast.
[19:17] So, you know, well, I guess it'll it'll run, on Wednesday, November 12.
[19:22] But, very timely, you know, I think.
[19:25] It's sort of like—again, there's there's the old crypto joke where, like, when your dentist and realtor friends start asking you about Ripple and Cardano, it's time to unwind your positions a little bit.
[19:35] You know? But it's the Zcash meta.
[19:37] I don't know. Like, maybe that means there's room to run.
[19:40] Like, maybe maybe it's tops. But—

**SPEAKER_00:**
[19:43] Well, as they say, it's like catching a falling knife.
[19:45] Right? Like, you know, like—
[19:46] Yeah. Trying to figure out the the peak of the market.
[19:49] I I okay. Like, we've talked about kind of how Zcash works, and it uses ZK in these sort of very specific areas.
[19:57] And it's not, you know, programmable generally.
[20:00] Now, obviously, there's a lot of talk in the Ethereum world about ZK-EVMs.
[20:05] You guys have any thoughts on that and, like, you know, how those work?
[20:08] Because, you know, at what point do we get—like, is it truly impossible to get full programmability, or do you know, is that something that is just getting closer?

**SPEAKER_02:**
[20:17] From a market perspective, I think they're mostly ZK-EVMs have been used for scaling as opposed to privacy.
[20:23] Even there, you tend to see some amount of specificity.
[20:26] Like, I think I I mentioned on a podcast before, I'm, you know, friend acquaintances with the dYdX CEO, and dYdX uses—dYdX is like the L2 version of Hyperliquid, if you will, where they they do perps and they do zero-knowledge matching off-chain, but you know it actually works and it gets written to Ethereum, which is pretty cool.
[20:47] And, supposedly, they're achieving really high throughputs this way.
[20:50] It's not necessarily privacy tech at all.
[20:53] I ran into some of the Aztec folks in Singapore, and it seems trending general purpose still on testnet, but not fully VM.
[21:03] It's like a restricted UTXO-type language of sorts, I believe.
[21:07] So I think there's probably—not being nearly as expert as Jim, who I'll defer to in a second, not being an expert, I think it will be—there's no intrinsic reason you can't make it fully VM, or full Rust, or some, you know, JavaScript or whatever.
[21:23] But, probably, there will be a tremendous amount of optimization that would have to happen to make that happen.
[21:28] So you probably see special purpose for a while.

**SPEAKER_03:**
[21:30] I saw that—and now I'm blanking on the name.
[21:34] The the ZK tech that was happening under the Polygon banner with, and I can't remember the the the name of the project now.
[21:42] They posted it within the last few months that they were real-time ZK proving on mainnet now.
[21:47] But, you know, it was with a battery of of GPUs.
[21:50] It was not a thing that you would be doing yourself.
[21:53] But but, yeah, that that full proving is, you know, is possible.
[21:57] But, yeah, you you you have that optimization to to be done.
[22:00] But, I mean, I think I think that's where things are gonna end up that you've had this sort of improvement where starting at Bitcoin, it's like, well, how are we gonna prove, you know, get to global consensus and and solve the double-spend problem?
[22:12] Well, it it's by publishing all of details, and then we're gonna have, you know, redundant state machines running in parallel.
[22:19] Right? And that's that's the answer we know that works.
[22:21] It was like, what's, you know you know, like, Satoshi did the big ugly thing, but it worked and it made this stuff possible that had never been possible before.
[22:29] But it is, you know, it's it's an incredibly big, ugly, expensive way of doing that.
[22:33] And then I think just over time, it's like, okay.
[22:35] Well, having things public was sort of a requirement for that consensus model, but that was never intentional, like, having them all as a public ledger.
[22:45] Like, that that's not a positive feature.
[22:47] Now if you look at the cypherpunk culture that many of these people were coming out of, yeah, it's it's private unstoppable money.
[22:56] Yeah, no, it wouldn't be public.
[22:57] So I saw that, yeah.
[23:00] Within weeks of Bitcoin starting, Hal Finney said, you know, looking at ways of improving anonymity in Bitcoin.
[23:08] So that was January 2009.
[23:11] You know, that was a cypherpunks obvious first reaction is, yeah, this is cool now.
[23:16] But, yeah, we should have privacy as well.
[23:18] And I think we're sort of getting to that point of the the tech has become good enough to to solve that without broadcasting everything to everyone.

**SPEAKER_00:**
[23:26] Yeah. Jim, what what do you think?
[23:28] Like, you know, on the sort of general programmability ZK front.

**SPEAKER_01:**
[23:31] I wish I had more, you know, hands-on experience with general ZK.
[23:36] I see a lot of people very excited by it.
[23:39] And maybe in a way that makes me skeptical because it seems like a cool toy.
[23:43] But I am open to them working great.
[23:46] And so I don't I don't wanna make us a a a strong firm stance at the moment on them, but, but they would be great if they work.

**SPEAKER_00:**
[23:54] Yeah. I I I it seems like the approach to Kieran's point is, like, find specific areas where you can, you know, create circuits and apply them and optimize for those and then expand that over time.
[24:06] You know? Like, it's it's really about kind of, like, you know, nailing those initial use cases Then the using the Zcash approach.

**SPEAKER_01:**
[24:12] And that's why I was drawn to that because because yeah.
[24:14] If you if you really narrow it down to something really simple, then I think you can do it well.

**SPEAKER_02:**
[24:18] I've heard that people even maybe compile the specific circuits and then optimize.
[24:23] Like, you kinda write them with the general tool.
[24:25] Some people do. I don't know.
[24:26] And then you kind of, like like, okay.
[24:28] I got the circuit for the specific thing, but then I gotta make it, like, work. You know? Yeah. Maybe—

**SPEAKER_00:**
[24:32] I think compiling a circuit is still pretty very, like, computational intensive, but it's way more—but it's way less for most circuits, once a circuit is compiled, it's way less to do the proof, which is you know?
[24:43] And you you gotta continue to push that down, but I think the ratio is very large.
[24:47] Okay. Well, I think we are out of time.
[24:50] You know, where can we find you, Jim?
[24:52] I'm gonna start with you.
[24:53] Where can find me? Yes.
[24:54] People wanna hear more and learn more about Jim, which I you know, please speak up. Ask him where can where they find you.

**SPEAKER_01:**
[25:00] I do have a Twitter handle. What is my Twitter handle?
[25:03] I can't remember. But—

**SPEAKER_00:**
[25:04] Probably @jhermo. I I guess it's probably.

**SPEAKER_02:**
[25:06] I'm gonna try to check. Hold on. Yeah.

**SPEAKER_01:**
[25:08] But whatever it is, you should post more often in it.
[25:10] Okay. I I I Twitter in spurts.
[25:12] Is . I, like, wake up one day and remember that Twitter exists, and then I twitter—I tweet a lot, and then then I forget about that for a couple of weeks.

**SPEAKER_02:**
[25:19] It's j h o in the the chat. I I don't know if we can all see that, the studio chat. But yeah.

**SPEAKER_01:**
[25:22] So so, yes, you can find him at @jhermo.
[25:25] Karen, where can people find—

**SPEAKER_00:**
[25:27] @jhermo. Yeah. Oh, @jhermo.

**SPEAKER_02:**
[25:29] Yeah. I'm on X @kgrubin.
[25:32] I'm also on Substack trying to, you know—I'm, like, a couple old medium posts that I've linked from there.
[25:38] I I'm I'm getting a little bit into a Substack rhythm.
[25:40] I'll it'll probably be infrequent, but at least of moderate to high quality.
[25:44] Also, kjameslubin.substack, I think, for now.
[25:49] Maybe I'll change the URL. Yeah.
[25:51] And link it in the in the show notes when we start—assuming we do show notes.

**SPEAKER_00:**
[25:55] And you can find me on X at @vic4wang.
[25:58] Bob has posted why I explained before in my handle.
[26:01] You can also find us at on Telegram at the Stratum Mercato Group.
[26:05] Just go to our website at stratummercato.com, and that will point you to Telegram.
[26:10] And, Bob, where can people find you, and what can people expect next week?
[26:14] Don't close it out, Bob. You're the resident Zcash shill.
[26:16] One year from now, Zcash price or market cap or both?

**SPEAKER_03:**
[26:19] I I think it will be in the top 10.
[26:22] Top 10. It's been it's been very close.
[26:25] And the primary reason is privacy is a big need, and it solved it.
[26:30] Right? It's not some future promise.
[26:32] Like, it works right now. There's a mobile app.
[26:34] People are using it. You know?
[26:36] You've got, like, a ten year—near ten year history of, you know, top brainiacs working on this.
[26:42] Lots of credibility.
[26:44] So, you know, I think it it it's great.
[26:47] And then I'm looking forward to smart contracts with with that kind of level as well.
[26:52] Just one more thing to mention.
[26:54] I couldn't remember Jordi's project, Zisk.
[26:57] So that was—that's a spin-off group now from Polygon, led by Jordi Baylina, and they announced real-time proving of mainnet blocks that was announced at EthCC this year.
[27:10] So proving a block, in seven and a half to twelve seconds, so just under block time.
[27:17] However, it requires 24 very high-powered GPUs or 48 more consumer-spec.
[27:26] So you've got a rack.

**SPEAKER_00:**
[27:27] There you go. And Bob, with that prediction, where can we find you, and can you give us a preview of what people can expect next week?

**SPEAKER_03:**
[27:34] Absolutely. Yes. So I'm I'm Bob Summerwill, summer like the season, w i l l.
[27:39] So on, on everything with with that name.
[27:42] And, yes, so next week, we will have an early days of Ethereum interview, with Christoph Jentzsch, formerly of of ETH dev.
[27:54] So he was hired in September 2014 into that Berlin office, worked on testing—cross-client testing, and then later on, with with their smart locks and the creation of The DAO, which is probably, you know, Ethereum's first killer app until we're killing—

**SPEAKER_00:**
[28:13] Killing in many different ways.
[28:14] Yes. We're doing that.
[28:16] Or or you can say birthing because ETC came out of that.
[28:18] Correct. Right.
[28:20] Okay. Well, that's time.
[28:21] Thank you very much for joining us, and we look forward to seeing you next week.
[28:25] Take care. Thanks, everybody.