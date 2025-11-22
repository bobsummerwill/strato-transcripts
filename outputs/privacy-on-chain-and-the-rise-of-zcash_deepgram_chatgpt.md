**SPEAKER_00:**
[00:00] Okay.
[00:02] Welcome, everyone.
[00:05] We have a very special and very timely topic today: privacy on-chain and the rise of Zcash.
[00:12] And we sort of have a special guest today.
[00:15] So I'm Victor Wong.
[00:18] I am founder and chief product officer at BlockApps.
[00:22] I'll get to our normal guests, but today, we have Jim.
[00:26] Do you want to give us a quick intro?

**SPEAKER_01:**
[00:29] Yeah.
[00:30] I've known Victor and Kieran for years.
[00:32] I'm one of the founders of BlockApps and CTO.

**SPEAKER_00:**
[00:37] And you're here in particular because I would call you a Zcash expert, having written your own Zcash client.

**SPEAKER_01:**
[00:41] Well, I think I'm more aspirational at this point in time.
[00:45] I mean, the way I learn about things is I try to—

**SPEAKER_02:**
[00:48] What's that?
[00:49] How many more expert people do you think there are on, say, Zcash in particular, on the planet?

**SPEAKER_01:**
[00:54] No.
[00:55] The problem that I have is that I was sort of halfway in the learning process last year.
[01:00] So the way I learn about things is I try to write—write a client for it.
[01:04] So I was doing that, but then we got pulled in different directions.
[01:07] I got to the point where I had sort of replicated the actual client that could connect.
[01:12] It would bring the data in.
[01:14] It would bring the proofs in.
[01:16] But just about when I was getting to the good parts, that's when we moved on to other things.
[01:21] Well, we're going to put the number—

**SPEAKER_00:**
[01:24] Answer my other question.
[01:26] Put the number at between, like, 10 and 100.
[01:29] Maybe 10.
[01:31] I would say there's definitely less than 20 people who have written their own Zcash clients, probably.
[01:35] Well, yeah.
[01:36] Yeah.
[01:37] There's probably some core contributors.

**SPEAKER_02:**
[01:39] I imagine there's more than a handful into Zcash.
[01:42] But, you know, when Jim says non-expert, you know, it's like, there are—let's say, yes.
[01:46] I'll expand the range.
[01:48] Five to 100 people who understand Zcash better on the planet.
[01:52] Big, big, big range there, but we're talking about pretty small numbers in absolute terms.
[01:56] So yeah.
[01:57] Exactly.
[01:59] I say—

**SPEAKER_00:**
[02:00] If Jim's not an expert, I don't know what "expert" even means.
[02:04] Anyway, Kieran, do you want to give a quick intro of yourself before we—

**SPEAKER_02:**
[02:08] Certainly.
[02:09] I'm our CEO.
[02:10] Been on these before.
[02:12] By the way, Vicky, we're letting Jim off the hook, calling him a special guest.
[02:15] He has to do this all the time now with our, you know, continued—in the public press.
[02:19] So—

**SPEAKER_00:**
[02:21] Special now.
[02:22] Not special in the future.
[02:23] Special today.
[02:25] Today is special, but it's the first of many.
[02:28] Let's just say that.
[02:30] I was looking through the—

**SPEAKER_03:**
[02:32] The prior videos.
[02:34] Jim has never appeared on one of our own spaces.
[02:37] He's only been on early days of the year.

**SPEAKER_00:**
[02:41] Older drinks.
[02:42] Well, there you go.
[02:43] Oh, no.
[02:45] You found out.
[02:46] But it won't be special soon.
[02:48] Bob, by the way, since you've spoken up, can you give that quick intro to yourself?
[02:52] So hi.
[02:53] I'm Bob.
[02:54] I'm head of ecosystem.

**SPEAKER_03:**
[02:57] And, yeah, been doing a lot of—a lot of spaces.

**SPEAKER_00:**
[03:00] Yeah.
[03:01] So, I think, you know, to level set—because I think there's a lot of misunderstanding about what privacy is.
[03:07] How would you define blockchain privacy, and why do you think it's important?

**SPEAKER_03:**
[03:13] Who's that question for?

**SPEAKER_00:**
[03:16] Could be for anyone.
[03:18] Whoever wants to go.
[03:19] Kieran, you want to kick us off?
[03:21] Okay.
[03:22] I'll take it.
[03:24] So—

**SPEAKER_02:**
[03:26] And for the—I assume that the viewer is pretty deep in the space, but I'll bring it down to a fairly low technical level.
[03:32] So blockchains are great.
[03:34] They let you move digitally scarce value from party to party.
[03:37] And the way that this is typically done is that you've got a big address, which is almost, but not quite, a public key.
[03:45] And you sort of sign a message that says, I, Kieran—but it's not Kieran because it's this address—send, you know, 3 Bitcoin to Bob, and it doesn't say Bob; it's another address.
[03:56] You don't quite know who either of those parties are.
[03:59] However, you've got the address forever.
[04:03] And often it is the case that you can piece together what happened based on that address.
[04:09] Let's say you're on a centralized exchange, which has KYC'd.
[04:13] It knows how to associate you to maybe a withdrawal address.
[04:18] It may not know down the line, but if you start to get a bunch of data points, you can kind of piece together who sent what to whom, and you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone.
[04:31] And while it's a cryptographic technology, it's not necessarily a private technology.
[04:37] And this has been a problem both in the consumer setting—just for, you know, people don't like this.
[04:42] Satoshi makes a comment, I believe in the white paper, saying that, you know, obviously, to prevent the double spend problem—which basically just is just that, to ensure that it can't, I mean, can't be created or destroyed except by the agreed mechanism—obviously, you need to know the whole history.
[04:59] And so he sees the problem as intrinsic, but some technologies come out later that maybe call that into question, that we'll talk about.
[05:09] It's also an enterprise problem.
[05:11] So we can talk separately about our experience there.
[05:14] Sort of what the enterprises want is kind of the same as what the public blockchain people want except with selective visibility.
[05:22] So they want to—say you're doing an on-chain stock trade, which is actually now starting to happen.
[05:28] You sort of want to know the other party has the stock.
[05:31] You don't necessarily want to know who the other party is, but you want to know that they acquired that stock legitimately.
[05:37] And then when you get it, you want to be able to pass it on legitimately in the same way.
[05:41] And then there's sometimes this extra requirement that, like, the regulator can see everything.
[05:46] You know?
[05:47] So you want sort of, like, an unlinkability of balance to person or company, but also this mass preservation property that I was talking about—you can't create or destroy assets.
[05:57] They have to be acquired legitimately and so on.
[06:02] So it's a perennial problem and closer to solved, you know, but we can go into that shortly.
[06:07] Yeah.
[06:08] Bob, did you want to add anything to that?

**SPEAKER_03:**
[06:12] Yeah.
[06:14] So, I mean, going back to those Bitcoin, you know, beginnings—in the Bitcoin white paper,
[06:19] you know, it just talks about severing identity from transactions.
[06:24] But really, that's just pseudo, pseudonymous, you know, not not anonymous.
[06:29] And I think a lot of people didn't understand that differentiation back in those early days, and it's like, "Oh, Bitcoin's private, untrackable, you know, digital money."
[06:41] But, you know, very rapidly you had blockchain analytics coming in, you know, looking for correlations and patterns, and it's like, "Yeah, you're not getting a lot of security," you know, even if you're not reusing addresses—just normal things that people would do.
[06:53] There's lots of correlations and, you know, you can get unmasked that way.
[06:58] But, yeah, Satoshi did talk a bit about zero knowledge.
[07:02] I can't remember who raised it.
[07:04] Somebody raised it early, and he was like, "Yeah, you know, that would be interesting if we could do that."
[07:09] But, but it was just—like, a lot of that cryptography just didn't—hadn't happened, you know?
[07:16] So Zcash started in 2016, and it was only around that kind of time or a little before that you started having, you know, these papers on on snark constructions, and going through all these different kind of rounds.
[07:28] So, yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path, you know, they are an immutable public ledger forever.
[07:36] Ethereum even worse because it's an account model, so you are reusing the addresses all the time.
[07:41] Right? And if your address is unmasked, you are forever doxed.
[07:46] That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address of his, which is probably not desired.

**SPEAKER_00:**
[07:56] Well—and, you know, you guys have been talking about Satoshi.
[08:00] But, Jim, I remember—I think it was, like, earlier at, like, 2014.
[08:04] Vitalik was talking—like, he was like, "zkSNARK will fix all of this at some point in time."
[08:10] Do you remember that at all?

**SPEAKER_01:**
[08:11] Well, I mean, I think we went through a learning process about privacy, and that's sort of, like, we're understating this right now.
[08:18] Maybe it's because we put a lot of time and effort into some privacy solutions that technically worked, but were a business failure, I think is fair to say.
[08:27] So, you know, the audience can learn from our sort of failed mistakes in the past right now.
[08:31] But, we sort of built—so we had heard years ago about zk—but we sort of just—I don't know, at the time, looked into it and said, "Oh, this looks, like, overly complicated.
[08:40] You can get privacy through these other means."
[08:43] And we ended up building a system that allowed for sort of quick spin-up of private chains, that everything was sort of in an encrypted tunnel.
[08:51] And you could have, like, these chains completely secure.
[08:54] Nobody else would see what was happening there.
[08:57] But long story short, slow learning process.
[09:00] We found out that customers want everything—and to the point that it made it worthless.
[09:08] Like, we would go into enterprise, we would say, "Oh, you can set up these private channels with others."
[09:12] And they loved that because they could sort of control that, and they could control who goes in there.
[09:16] But then once everything was going through these private channels, they wanted to be able to, like, transfer from private chain to private chain, and that's where everything started to fall apart.
[09:25] And getting things back onto the main chain became sort of this extra complicated system.
[09:30] And at the same time, customers wanted to have, like, full flexibility in having, like, extensions to Solidity, where you could just, like, name a chain and send some money from chain A to chain B.
[09:44] And, really, the only way to make that stuff work is you have to go back to zk.
[09:49] So zk is overly complicated, but it is necessary.
[09:55] So we started looking at that again, but I think the safe thing to do is start with a proven technology.
[10:01] And Zcash had been around for years and nobody had stolen money.
[10:05] And this is just sort of like a subset of zk, but it's kind of a cool thing.
[10:10] You can build what they call tumblers of money.
[10:13] You throw a bunch of money in, and then the money that you put into the tumbler—you know how much went in, but the ownership is completely scrambled up.
[10:20] And at any time, you can go and transfer money from within the tumbler from one user to another, but only the users who did the transferring and got the money know what was there, but nobody else can see what's happening.
[10:32] So, again, you have these systems of multiple users with lots of money, but you don't know who owns what percentage of the money.

**SPEAKER_00:**
[10:41] Yeah.
[10:42] Actually, before we even go that far, can we talk just, like, what is zk and how does it work, and why is it an important part of the solution?
[10:52] I want to pull back for also a second.

**SPEAKER_02:**
[10:55] I remember I think there was an Ethereum meetup in New York.
[10:58] I'm not sure if either of you guys were there.
[11:01] I think I spoke at it, maybe.
[11:03] And there was also a Zcash, I think, presentation there.
[11:07] And it was, at that time, taking seven minutes to generate the zk proofs.
[11:13] So, yes, yeah.
[11:15] Wanted to make a transaction.
[11:17] You'd, like, did this thing.
[11:18] It took seven minutes, and then the verification was kind of fast.
[11:22] Once you had it and you sent it to the network, things could go on, you know, but the usability was not there in those days.
[11:29] This is part of the reason we weren't, like, going to tell our enterprise customers, like, "Oh, yeah—let's zk everything."
[11:35] You know, even if we had it all integrated nicely, there's a lot of devil in the details.
[11:40] I know it was unbelievably—

**SPEAKER_01:**
[11:41] Slow for a while, and I think it's fixed.
[11:43] But yeah, I know.
[11:44] Well, it's complicated.
[11:46] I mean, this is what I was trying to say before.
[11:48] It's like, I have, like, sort of nuts and bolts experience of what's going on in Zcash.
[11:53] But the more complicated world of zero knowledge—that's my aspirational part right now.
[11:59] I can sort of see pieces moving within there, but I would hesitate to speak more broadly on this.
[12:06] Except, let's say that it is more complicated than any of the, for instance, Ethereum—

**SPEAKER_00:**
[12:11] Client implementation stuff that we were doing back in the day.
[12:14] Yeah, yeah.
[12:15] Can you give a high-level summary of what zero knowledge is?
[12:18] Like, I think very few people understand.

**SPEAKER_02:**
[12:20] I have a good layman example, I think, and Jim can correct me.
[12:23] So I did once take a theoretical cryptography class, and the example they bring up is the CEO problem, so to speak.
[12:31] So we've got two CEOs, and they're high-ego guys, you know?
[12:35] And they want to know—

**SPEAKER_00:**
[12:36] Do you stand up from experience, Kieran?
[12:38] Or—yeah.

**SPEAKER_02:**
[12:39] Yeah.
[12:40] Let's think about myself.
[12:41] They want to know who has the most between the two.
[12:45] But they don't want to know how much money—they merely want to know which one has more.
[12:52] And you would think that there wouldn't really be a way to create a scheme in which they could learn that information and nothing else, but there actually is.
[13:00] And again, this is almost ten years ago now, so I may be describing the example incorrectly.
[13:06] But, yeah, that's like a case where you might want zero knowledge.
[13:10] Similarly, you know, like an ID check in a bar.
[13:13] You're leaking all your personal info when you hand the ID to the bouncer: your home address, your full name, your date of birth, etc.
[13:21] So you may want to prove to the bar that you're 21 without handing any other info over, basically.
[13:27] I think this is the general setting that it ends up at.
[13:31] Jim, do you want to take that and run with it, correct it?
[13:34] Yeah.

**SPEAKER_01:**
[13:35] So this is—when you first look up zero knowledge, there are lots of little examples like this.
[13:40] They're all pretty cool.
[13:42] But what's really happening in Zcash is that what you're trying to do is pass money from person A to person B.
[13:51] And person A wants to prove to person B that they have the money and that it was actually transferred, but without giving away the amount of money that person A has, or without person A learning how much person B has.
[14:03] Just that, you know, that the state before was that you had the amount, and that the state after is that it was transferred over.
[14:10] And then also no one else in the world can know this.
[14:13] So you're proving sort of the important parts, not others.
[14:17] Zero knowledge could get pretty complicated too, because when you start looking into it, there are a lot of one-off examples, like you're talking about, that you sort of see a solution to.
[14:27] But the problem comes about in trying to come up with a sort of generic solution where you can almost just compile any amount of code into some zk proof, and then run that for anything.
[14:37] I don't remember, because it's been about a year now, but in Zerocash, there were multiple—multiple zero-knowledge proofs in there for various aspects.
[14:47] If I remember—you know, I might be making up some of the details here, but I think there was one proof that was to show that you had more than such and such money before the transfer.
[14:55] I might have it slightly off, but there were multiple of these zero-knowledge algorithms in there.
[15:01] But put together, they allowed for the full sort of transfer of money within the tumbler.
[15:07] And each one sort of had been worked out independently of each other, using a more generic system where they compiled certain algorithms in there.
[15:17] Does that make sense?
[15:18] So making it generic can get really complicated.

**SPEAKER_02:**
[15:21] Terminology for the listener that you've heard, that I barely remember.
[15:25] So SNARKs and STARKs were a thing that Vitalik was talking about a lot and still does.
[15:31] So it's like "Succinct Non-Interactive Argument of Knowledge," basically interactive proof—yes.
[15:37] But what's the whole acronym?
[15:39] But so there is a way, I think, to take an arbitrary computation and to prove that it has a certain result without revealing, like, the intermediate states and so on.
[15:49] But it's not computationally feasible—or, it's just so slow that if you try to do it that way, it becomes very difficult.
[15:55] So I believe, just tying back to Jim's point, you could try to do this in a generality—like, the EVM.
[16:01] Like, I can verify—there are zkEVMs.
[16:05] Like, I can verify any computation that comes out of this thing.
[16:09] And I think the problem with them has been performance.
[16:12] And so the Zcash people, I guess, had to decompose every little step into specific zk circuits, right?
[16:18] Like—or—yeah.
[16:20] Yeah.
[16:21] So, yeah, it's very, very low-level programming thinking in the zk world.
[16:27] Like, literally, there are circuits that you end up compiling, and so on and so forth.

**SPEAKER_01:**
[16:32] So, yeah, Zcash at the moment is onto its day, and by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one tumbler problem without going any more in-depth than that.
[16:45] So this isn't—like, in the dream world, you would take any Ethereum contract and compile it somehow as, you know, something zero-knowledge, and then prove that you had run the full contract.
[16:58] That's something that, at least at the time—at least so far in the world as it is—I didn't want to get into it or have us get into, as a company.
[17:08] But just to have these tumblers in place, I think that solves a lot of—

**SPEAKER_03:**
[17:13] Yeah.
[17:14] Bob, you were saying something?
[17:15] Yeah.
[17:16] So Zcash is onto its fourth round of different cryptography.
[17:20] So I forget what they're called—Sapling, something else.
[17:22] We're onto Orchard now.
[17:24] But that's been now over the course of nearly a decade.
[17:28] Each time you've got another sort of two years' worth of leading-edge advancement.
[17:33] And, yeah, like, talking about that performance thing—so it's something which I think has been a key piece in Zcash price appreciation recently—has been the arrival of a functional mobile wallet.
[17:46] So that's called Zashi, which is made by the Electric Coin Company.
[17:50] But you're basically at the point where you can run that proof on your phone.
[17:55] So something which used to be laptop, seven minutes, is now phone, seconds.
[17:59] So what you've seen, if you look at the size of these shielding pools—where these pools are, effectively, like, you know, all of these things are all mixed and hidden together, right?
[18:09] The more that you've got in a pool, the more, you know, unlinkable you are.
[18:14] If you have—you know, if you do something simple like ring signatures, I think Monero has got 16 transactions that get all joined together.
[18:22] So you can trace through that to a degree.
[18:25] But if you've got hundreds or thousands or millions of people in that same pool, you know, it's effectively completely anonymous at that point.
[18:34] But if you look at the stats of usage of these particular pools, you're seeing what proportion of the money supply has been shielded versus being transparent.
[18:44] I guess that's just another thing to say, right, is—Bitcoin is transparent, same with Ethereum, but then they use the word "shielded" to talk about, you know, that you are within this anonymity set.
[18:54] So these earlier rounds, you had a bit of use, but not a ton of use.
[18:58] But right now—I can't find the view, but it was something like about four or five million of the 21 million were within that shielding pool.
[19:09] So, you know, a significant chunk of it is shielded now, which was never the case in the past.
[19:15] You know?
[19:16] I remember on ETC at some point, we were looking at whether we were going to bring over the precompiles to do with some of the curves.
[19:22] You know?
[19:23] I don't know if you remember that happened in Ethereum at some point, but like one of the curves, I think, went into the precompile.
[19:28] And we were talking about whether we were going to do that or not.
[19:30] And really, talking about gas limit as well—how gas-expensive would operations be using these things even.
[19:37] And the stats at that time were, it's like maybe 2% of transactions on Zcash were shielded, something like that.
[19:45] You know, it's basically, like, not being used at all—functionally pretty much identical to Bitcoin.
[19:53] But probably a lot of venues going, "Yeah, I'm using Zcash. I'm private."
[19:57] It's like, yeah—you know, you're not, not at all.
[20:00] You're getting zero benefit at all.
[20:02] But yeah, that's really happening now.
[20:04] And I think it's just, you know, these rounds and rounds of years and years of research and then implementation of those, and engineering effort, and it's like, "Hey. It works now."

**SPEAKER_00:**
[20:15] Well, I'm just curious from your standpoint, Jim—like, is it a technological advancement that has created [this], or is it just simply that these tumblers have gotten big enough that they offer real privacy?
[20:27] Do you know what I mean?

**SPEAKER_01:**
[20:29] It's—I mean, any of these things are technological advancements.
[20:32] But, I mean, you want to have the tumblers big enough so that you have some amount of anonymity within there.
[20:38] It's not like if it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_02:**
[20:42] I need to interject.
[20:43] I have a crypto friend who was texting about thirty seconds ago about whether I like Zcash at this price.
[20:48] This is a prerecorded podcast.
[20:50] So, you know, well, I guess it'll run on Wednesday, November 12.
[20:56] But, very timely, you know, I think.
[20:58] It's sort of like—again, there's the old crypto joke where, like, when your dentist and realtor friends start asking you about Ripple and Cardano, it's time to unwind your positions a little bit.
[21:07] You know?
[21:08] But it's the Zcash meta.
[21:10] I don't know.
[21:11] Like, maybe that means there's room to run.
[21:14] Like, maybe—maybe it's tops.

**SPEAKER_00:**
[21:17] Well, as they say, it's like catching a falling knife.
[21:20] Right? Like, you know—trying to figure out the peak of the market.
[21:24] I—okay.
[21:26] Like, we've talked about kind of how Zcash works, and it uses zk in these sort of very specific areas.
[21:34] And it's not, you know, programmable generally.
[21:36] Now, obviously, there's a lot of talk in the Ethereum world about zkEVMs.
[21:41] Do you guys have any thoughts on that and, like, you know, how those work?
[21:45] Because, you know, at what point do we get—like, is it truly impossible to get full programmability, or is that something that is just getting closer?

**SPEAKER_02:**
[21:53] From a market perspective, I think mostly zkEVMs have been used for scaling as opposed to privacy.
[22:01] Even there, you tend to see some amount of specificity.
[22:05] Like, I think I mentioned on a podcast before, I'm, you know, friend/acquaintances with the Lighter CEO, and Lighter uses—Lighter is like the L2 version of Hyperliquid, if you will, where they do PERKs and they do zero-knowledge matching off-chain, but you know, it actually works and it gets written to Ethereum, which is pretty cool.
[22:27] And, supposedly, they're achieving really high throughputs this way.
[22:31] It's not necessarily privacy tech at all.
[22:34] I ran into some of the Aztec folks in Singapore, and it seems trending general-purpose, still on testnet, but not fully VM; it's like a restricted UTXO-type language of sorts, I believe.
[22:47] So I think there's probably—not being nearly as expert as Jim, who I'll defer to in a second—not being an expert, I think it will be, there's no intrinsic reason you can't make it fully VM or full Rust or, you know, JavaScript or whatever.
[23:02] But, probably, there will be a tremendous amount of optimization that would have to happen to make that happen.
[23:07] So you probably see special purpose for a while.

**SPEAKER_03:**
[23:10] I saw—that—and now I'm blanking on the name.
[23:12] The zk tech that was happening under the Polygon banner with—and I can't remember the name of the project now.
[23:20] They posted it within the last few months that they were real-time zk proving on mainnet now.
[23:25] But, you know, it was with a battery of GPUs.
[23:29] It was not a thing that you would be doing yourself.
[23:33] But, yeah, that full proving is, you know, possible.
[23:36] But, yeah, you have that optimization to be done.
[23:40] But, I mean, I think that's where things are going to end up—that you've had this sort of improvement where, starting at Bitcoin, it's like, "Well, how are we going to prove, you know, get to global consensus and solve the double-spend problem?"
[23:54] Well, it's by publishing all of the details, and then we're going to have, you know, redundant state machines running in parallel.
[24:00] Right?
[24:01] And that's the answer we know that works.
[24:04] It was like, Satoshi did the big ugly thing, but it worked and it made this stuff possible that had never been possible before.
[24:12] But it is, you know, it's an incredibly big, ugly, expensive way of doing that.
[24:18] And then I think just over time, it's like, okay, well, having things public was sort of a requirement for that consensus model, but that was never intentional—like, having them all as a public ledger.
[24:32] That's not a positive feature.
[24:34] Now if you look at the cypherpunk culture that many of these people were coming out of, yeah, it's private, unstoppable money.
[24:41] Yeah, no, it wouldn't be public.
[24:43] So I saw that, yeah, within weeks of Bitcoin starting—how Finney said, you know, looking at ways of improving anonymity in Bitcoin.
[24:54] So that was January 2009.
[24:57] You know, that was a cypherpunks' obvious first reaction: "Yeah, this is cool now, but, yeah, we should have privacy as well."
[25:04] And I think we're sort of getting to that point—the tech has become good enough to solve that without broadcasting everything to everyone.

**SPEAKER_00:**
[25:13] Yeah.
[25:14] Jim, what do you think, like, you know, on the sort of general programmability zk front?

**SPEAKER_01:**
[25:19] I wish I had more, you know, hands-on experience with general zk.
[25:23] I see a lot of people very excited by it.
[25:26] And maybe in a way that makes me skeptical, because it seems like a cool toy.
[25:30] But I am open to them working great.
[25:33] And so I don't want to make a strong, firm stance at the moment on them—but they would be great if they work.

**SPEAKER_00:**
[25:41] Yeah.
[25:42] I—it seems like the approach, to Kieran's point, is, like, find specific areas where you can, you know, create circuits and apply them and optimize for those and then expand that over time.
[25:54] You know?
[25:55] Like, it's really about kind of, like, you know, nailing those initial use cases, then using the dispatch approach.

**SPEAKER_01:**
[26:00] And that's why I was drawn to that, because—yeah, if you really narrow it down to something really simple, then I think you can do it well.

**SPEAKER_02:**
[26:07] I've heard that people even maybe compile the specific circuits and then optimize.
[26:11] Like, you kind of write them with the general tool—some people do, I don't know—and then you kind of, like, "Okay, I got the circuit for the specific thing, but then I gotta make it, like, work."
[26:21] You know?
[26:22] Yeah.
[26:23] Maybe—

**SPEAKER_00:**
[26:24] I think compiling a circuit is still pretty computationally intensive, but it's way more—but it's way less for most circuits, once a circuit is compiled, it's way less to do the proof, which is—you know?
[26:35] And you gotta continue to push that down, but I think the ratio is very large.
[26:39] Okay.
[26:40] Well, I think we are out of time.
[26:42] You know, where can we find you, Jim?
[26:45] I'm going to start with you.
[26:46] Where can—find me?
[26:48] Yes.
[26:49] People want to hear more and learn more about Jim, which I—you know, please speak up.
[26:54] Ask him where they can find you.

**SPEAKER_01:**
[26:56] I do have a Twitter handle.
[26:59] What is my Twitter handle?
[27:02] I can't remember.
[27:03] But—

**SPEAKER_00:**
[27:04] Probably jhermas or something.
[27:05] I guess it's probably—

**SPEAKER_02:**
[27:07] I'm going to try to check.
[27:08] Hold on.
[27:09] Yeah.

**SPEAKER_01:**
[27:10] But whatever it is, you should post more often than I do.
[27:13] Okay.
[27:14] I Twitter in spurts.
[27:17] I, like, wake up one day and remember that Twitter exists, and then I tweet a lot, and then forget about it for a couple of weeks.
[27:25] It's jhermas—

**SPEAKER_02:**
[27:26] O— in the chat.
[27:27] I don't know if we can all see that, the studio chat.
[27:29] But—yeah.

**SPEAKER_00:**
[27:31] So—

**SPEAKER_01:**
[27:32] Yes, you can find him at @jhermas.
[27:34] Kieran, where can people find—Hermas?

**SPEAKER_00:**
[27:36] Yeah.
[27:37] Oh, @jhermas.

**SPEAKER_02:**
[27:39] Yeah.
[27:40] I'm on X @kgruben.
[27:42] I'm also on Substack, trying to, you know—I'm, like, a couple old Medium posts that I've linked from there.
[27:46] I'm getting a little bit into a Substack rhythm.
[27:51] It'll probably be infrequent, but at least of moderate to high quality.
[27:55] Also, kjameslubin.substack, I think, for now.
[27:59] Maybe I'll change the URL.
[28:01] Yeah.
[28:02] And link it in the show notes when we start, assuming we do show notes.

**SPEAKER_00:**
[28:06] And you can find me on X at @vic4wang.
[28:09] Bob has posted why, I explained before, in my handle.
[28:13] You can also find us on Telegram at the Straum Mercado Group.
[28:17] Just go to our website at straummercado.com, and that will point you to Telegram.
[28:22] And, Bob, where can people find you, and what can people expect next week?
[28:27] Don't close it out, Bob.
[28:28] You're the resident Zcash shill.
[28:30] One year from now, Zcash—

**SPEAKER_02:**
[28:32] Price or market cap or both?

**SPEAKER_03:**
[28:33] I think it will be in the top 10.
[28:36] Top 10.
[28:37] It's been—it's been very close.
[28:39] And the primary reason is privacy is a big need, and it solved it.
[28:44] Right?
[28:45] It's not some future promise.
[28:47] Like, it works right now.
[28:49] There's a mobile app.
[28:50] People are using it.
[28:52] You know?
[28:53] You've got a near ten-year history of, you know, top brainiacs working on this.
[29:00] Lots of credibility.
[29:01] So, you know, I think it's great.
[29:03] And then I'm looking forward to smart contracts with that kind of level as well.
[29:09] Just one more thing to mention—I couldn't remember Jordi's project, ZKStack.
[29:15] So that's a spin-off group now from Polygon, led by Jordi Baylina, and they announced real-time proving of mainnet blocks—that was announced at EthCC this year.
[29:27] So proving a block in seven and a half to twelve seconds—so just under block time.
[29:32] However, it requires 24 very high-powered GPUs or 48 more consumer-spec.
[29:38] So you've got a rack.

**SPEAKER_00:**
[29:40] There you go.
[29:41] And, Bob, with that prediction, where can we find you, and can you give us a preview of what people can expect next week?
[29:47] Absolutely, yes.
[29:49] So I'm Bob Summerwill—summer, like the season, W I L L.

**SPEAKER_03:**
[29:54] So, on everything with that name.
[29:57] And, yes, so next week, we will have an early days of Ethereum interview with Christoph Jentzsch, formerly of—of f dev.
[30:06] So he was hired in September 2014 into that Berlin office, worked on testing, cross-client testing, and then later on, with their smart locks and the creation of The DAO, which is probably, you know, Ethereum's first killer app until we were killing—

**SPEAKER_00:**
[30:20] Killing in many different ways.
[30:22] Yes, we're doing that.
[30:23] Or you could say birthing, because ETC came out of that.
[30:26] Correct, right.
[30:27] Okay.
[30:28] Well, that's time.
[30:29] Thank you very much for joining us, and we look forward to seeing you next week.
[30:33] Take care.
[30:34] Thanks, everybody.