**SPEAKER_00:**
[00:01] Okay, welcome, everyone.
[00:04] We have a very special and very timely topic today: privacy on-chain and the rise of Zcash.
[00:09] And we sort of have a special guest today.
[00:11] So I'm Victor Wong.
[00:13] I am founder and Chief Product Officer at BlockApps.
[00:16] I'll get to our normal guests, but today we have—
[00:19] Jim, do you want to give us a quick intro?

**SPEAKER_01:**
[00:22] Yeah.

**SPEAKER_02:**
[00:23] I'm also—I've known Victor and Kieran for years.
[00:27] I'm one of the founders of BlockApps and CTO.

**SPEAKER_00:**
[00:31] And you're here particularly because I would call you a Zcash expert, having written your own Zcash client.

**SPEAKER_02:**
[00:36] Well, I think I'm more aspirational at this point in time.
[00:39] I mean, the way I learn about things is I try to—

**SPEAKER_01:**
[00:44] How many more expert people do you think there are on, say, Zcash in particular on the planet?

**SPEAKER_02:**
[00:48] No, the problem that I have is that I was sort of halfway in the learning process last year.
[00:53] So the way I learn about things is I try to, like, write—a client for it.
[00:57] So I was doing that, but then we got pulled in different directions.
[01:00] I got to the point where I had sort of replicated the actual client that could connect.
[01:04] It would bring the data in.
[01:06] It would bring the proofs in.
[01:08] But just about when I was getting to the good parts, that's when—we moved on to other things.

**SPEAKER_00:**
[01:13] Well, I'm gonna put the number—

**SPEAKER_01:**
[01:14] Answer my own question—between like, 10 and 100, maybe 10.

**SPEAKER_00:**
[01:18] I would say there—there's definitely less than 20 people who have written their own Zcash clients. Probably.

**SPEAKER_01:**
[01:21] Well, yeah, there's probably some core contributors.
[01:24] I imagine there's more than a handful into Zcash.
[01:26] But, you know, when Jim says non-expert, he—you know, it's like there are—let's say, yes, I'll expand the range 5 to 100 people who understand Zcash better on the planet.
[01:33] Big, big, big range there.
[01:35] But we're talking about pretty small numbers in absolute terms, so—

**SPEAKER_00:**
[01:38] Yeah, yes, exactly.
[01:40] I would say if Jim's not an expert, I don't know what even expert means.
[01:43] Anyways.
[01:44] Kieran, do you want to do a quick intro of yourself before—

**SPEAKER_01:**
[01:47] Certainly.
[01:48] I'm our CEO.
[01:50] Been on these before.
[01:51] By the way, Vic, you're letting Jim off the hook, calling him a special guest.
[01:54] He has to do this all the time now with our, you know, continued in the public press.
[01:57] So special in the future—

**SPEAKER_00:**
[01:59] Special today.
[02:00] Today is special, but it's the first of many.

**SPEAKER_03:**
[02:02] Let's just say that I was looking through the—the prior videos—Jim has never appeared on one of our own spaces.
[02:08] He's only been on early days of—

**SPEAKER_01:**
[02:11] Okay, there you go.

**SPEAKER_02:**
[02:12] Oh no, you found out but it—

**SPEAKER_00:**
[02:13] Won't be special soon.
[02:15] Bob, by the way, since you've spoken up, can you do give a quick intro to yourself?

**SPEAKER_03:**
[02:19] So hi, I'm—I'm Bob, I'm Head of Ecosystem and yeah, been doing a lot of—a lot of spaces.

**SPEAKER_00:**
[02:25] Yeah, so I think, you know, to level set because I think there's a lot of misunderstanding about what privacy is.

**SPEAKER_01:**
[02:29] What—

**SPEAKER_00:**
[02:30] How would you define blockchain privacy and why do you think it's important?

**SPEAKER_03:**
[02:35] Who's that a question for?

**SPEAKER_00:**
[02:36] Could be for anyone.
[02:37] Whoever wants to go. Kieran, you want—

**SPEAKER_01:**
[02:39] To kick us off? So, and for the—I assume that the viewer is pretty deep in the space, but I'll bring it down to a fairly low technical level.
[02:44] So, blockchains are great.
[02:45] They let you move digitally scarce value from party to party.
[02:48] And the way that this is typically done is that you've got a big address which is almost, but not quite, a public key and you sort of sign a message that says I, Kieran—but it's not Kieran, because it's this address—send three Bitcoin to Bob.
[02:57] And it doesn't say Bob.
[02:58] It's another address—you don't quite know who either of those parties are.
[03:01] However, you've got the address forever.
[03:03] And often it is the case that you can piece together what happened based on that address.
[03:07] So say you're on a centralized exchange which has KYC'd—it knows how to associate you to maybe a withdrawal address.
[03:12] It may not know down the line, but if you start to get a bunch of data points you can kind of piece together who sent what to whom and you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone.
[03:23] And it's not—while it's a cryptographic technology, it's not necessarily a private technology.

[03:28] This has been a problem both in the consumer setting—just for people don't like this.
[03:32] Satoshi makes a comment, I believe in the white paper, saying that obviously to prevent the double spend problem—which basically is just to ensure that Bitcoin can't be created or destroyed except by the agreed mechanism—obviously you need to know the whole history and so he sees the problem as intrinsic.
[03:47] But some technologies come out later that maybe call that into question, that we'll talk about.

[03:52] It's also an enterprise problem, so we can talk separately about our experience there.
[03:56] Sort of what the enterprises want is kind of the same as what the public blockchain people want, except with selective visibility.
[04:01] So they want to say, you're doing like an on-chain stock trade, which is actually now starting to happen.
[04:06] You sort of want to know the other party has the stock.
[04:08] You don't necessarily want to know who the other party is, but you want to know that they acquired that stock legitimately.
[04:12] And then when you get it, you want to be able to pass it on legitimately in the same way.

[04:16] And then there's sometimes this extra requirement that, like, the regulator can see everything.
[04:19] You know, so you want sort of like an unlinkability of balance to person or company, but also this mass preservation property that I was talking about: can't create or destroy assets—they have to be acquired legitimately, and so on.
[04:29] So it's a perennial problem and closer to solved and, you know, we can go into that shortly.

**SPEAKER_00:**
[04:34] Yeah, Bob, did you want to add anything to that?

**SPEAKER_03:**
[04:36] Yeah, yes.
[04:38] I mean, going back to those Bitcoin—you know, beginnings—in the Bitcoin white paper, you know, it just talks about severing identity from transactions, but really that's just pseudonymous, you know, not anonymous.
[04:48] And I think a lot of people didn't understand that differentiation back in those early days.
[04:53] And it's like, "Oh, Bitcoin's private, untrackable, you know, digital money."
[04:57] But, you know, very rapidly you have blockchain analytics coming in, you know, looking for correlations and patterns.
[05:02] And it's like, yeah, that's—you're not getting a lot of security, you know, even if you're not reusing addresses, just sort of normal things that people would do.
[05:08] There's lots of correlations and, you know, you can get unmasked that way.

[05:11] But, yeah, Satoshi did talk a bit about zero knowledge.
[05:14] I can't remember who raised it. Somebody raised it early and he was like, "Yeah, you know, that would be interesting if we could do that," but it was just like a lot of that cryptography, you know, just hadn't happened, you know.
[05:25] So Zcash started in 2016, and it was only around that kind of time or a little before that you started having, you know, these papers on SNARK constructions and going through all these different kind of rounds.

[05:36] So, yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path—you know, they are an immutable public ledger forever.
[05:44] Ethereum—even worse because it's an account model.
[05:47] So you are reusing the addresses all the time, right?
[05:50] And if your address is unmasked, you are forever doxxed. That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars in and out of a known address of his, which—probably not desired.

**SPEAKER_00:**
[05:59] And you guys have been talking about Satoshi, but Jim, I remember, I think it's like early—at like 2014, Vitalik was talking like, he was like, "ZK-SNARK will fix all of this at some point in time."
[06:08] Do you remember that?

**SPEAKER_02:**
[06:09] Well, I mean, like, I think we went through a learning process about privacy.
[06:13] And that's sort of like—we're understating this right now. Maybe it's because we put a lot of time and effort into some privacy solutions that technically worked but were a business failure, I think is fair to say.
[06:23] And so the audience can learn from our failed mistakes in the past right now.

[06:27] But we sort of built—so we had heard years ago about zk, but we sort of just—I don't know, at the time, looked into it and said like, "Oh, this looks like overly complicated. You can get privacy through these other means."
[06:38] And we ended up building a system that allowed for sort of quick spin-up of private chains, where everything was sort of like in an encrypted tunnel.
[06:46] And you could have these chains completely secure. Nobody else would see what was happening there.

[06:51] But long story short, you know—slow learning process—we found out that customers want everything.
[06:58] And to the point that it made it worthless, we would go into enterprise. We would say, "Oh, you can set up these private channels with others." And they loved that because they could sort of control that and they could control who goes in there.

[07:11] But then once everything was going through these private channels, then they wanted to be able to transfer from private chain to private chain.
[07:18] And that's where everything started to fall apart.
[07:21] Getting things back onto the main chain became sort of this extra complicated system.
[07:26] And at the same time, customers wanted to have full flexibility in having extensions to Solidity where you could just name a chain and send some money from chain A to chain B.
[07:34] And really the only way to make that stuff work is you have to go back to zk.

[07:38] So zk is overly complicated, but it is necessary.
[07:41] And so we started looking at that again.
[07:43] But I think the safe thing to do is start with a proven technology.
[07:46] And Zcash had been around for years and nobody had stolen money. And this is just sort of like a subset of zk, but it's kind of a cool thing.
[07:52] You can build what they call tumblers of money—throw a bunch of money in and then the money that you put into the tumbler is—you know how much went in, but the ownership is completely scrambled up and at any time you can go and transfer money from within the tumbler from one user to another, but only the users who did the transferring and got the money know what was there, but nobody else can see what's happening.

[08:16] So again, you have these systems of multiple users with lots of money, but you don't know who owns a percentage of the money.

**SPEAKER_00:**
[08:21] Yeah.
[08:22] Actually, before we even go that far, can we talk, just like, what is ZK and how does it work and why is it an important part of the solution?

**SPEAKER_01:**
[08:29] I want to pull back for also a second.
[08:31] I remember—I think there was an Ethereum meetup in New York.
[08:34] I'm not sure if either of you guys were there. I think I spoke at it maybe and there was also a Zcash, I think, presentation there.
[08:39] And it was at that time taking seven minutes to generate the ZK proofs.
[08:43] So you wanted to make a transaction, you'd like, did this thing, it took seven minutes and then the verification was kind of fast.
[08:49] Once you had it and you sent it to the network, things could go on.
[08:52] But the usability was not there in those days.

[08:55] This is part of the reason we weren't gonna tell our enterprise customers like, "Oh yeah, let's ZK everything."
[09:01] You know, even if we had it all integrated nicely, there's a lot of devil in the details and it was unbelievably slow for a while, and I think it's fixed.

**SPEAKER_00:**
[09:08] But, yeah, well, it's complicated.

**SPEAKER_01:**
[09:10] I mean, this is what I was—

**SPEAKER_02:**
[09:11] Trying to say before is, like, I have, like, sort of nuts and bolts experience of what's going on in Zcash.
[09:16] But the more complicated world of zero knowledge—that's my aspirational part right now.
[09:20] I can sort of see pieces moving within there, but would hesitate to speak more broadly on this except, let's say, that it is more complicated than any of the, like, for instance, Ethereum client implementation stuff that we were doing back in the day.

**SPEAKER_00:**
[09:31] Yeah, yeah. It can get—pretty high level summary of what zero knowledge is. Like, I think very few people understand—

**SPEAKER_01:**
[09:38] I have a good layman example.
[09:39] Okay.
[09:40] I think—and Jim can correct me.
[09:42] So I did want to take a theoretical cryptography class, and the example they bring up is the CEO problem, so to speak.
[09:48] So you've got two CEOs and they're high ego guys, you know, and they want to know—

**SPEAKER_00:**
[09:52] From experience, Kieran, or—

**SPEAKER_01:**
[09:54] Yeah, I'm not speaking about myself.
[09:56] They want to know who has the most between the two, but they don't want to know how much money—they merely want to know which one has more.
[10:02] And you would think that there wouldn't really be a way to create a scheme in which they could learn that information and nothing else. But there actually is.
[10:09] Again, this is almost 10 years ago now, so I may be describing the example incorrectly, but yeah, that's like a case where you might want zero knowledge.
[10:15] Similarly, like an ID check at a bar—you're leaking all your personal info when you hand the ID to the bouncer: your home address, your full name, your date of birth, etc.
[10:22] So you may want to prove to the bar that you're over 21 without handing any other info over.

[10:27] Basically I think this is the general setting that it ends up at. Jim, do I—do you want to take that and run with it? Correct it?

**SPEAKER_00:**
[10:34] Yeah.

**SPEAKER_02:**
[10:35] So, this is—when you first look up zero knowledge, there are lots of little examples like this that are all pretty cool.
[10:40] And what's really happening in Zcash is that what you're trying to do is pass money from person A to person B.
[10:45] And person A wants to prove to person B that they have the money and that it was actually transferred, but without giving away the amount of money that person A has, or without person A learning how much person B has—just that, you know, that the state before was that you had the amount and that the state after is that it was transferred over.
[11:00] And then also no one else in the world can know this.

[11:02] So you're proving sort of the important parts but not others.

[11:05] But zero knowledge could get pretty complicated too, because when you start looking into it, there are a lot of one-off examples like you're talking about, that you can sort of see a solution to.

[11:12] But the problem comes about in trying to come up with sort of a generic solution where you can almost just compile any amount of code into some ZK proof and then run that for anything.

[11:21] I don't remember, because it's been about a year now, but in Zerocash there were multiple, multiple zero knowledge proofs in there for various aspects.

[11:29] If I—you know, I might be making up some of the details here, but I think there was like one proof was like to show that you had more than such and such money before the transfer.

[11:37] I might have it slightly off, but there were multiple of these zero knowledge algorithms in there.

[11:40] But put together, they allowed for the full sort of transfer of money within the tumbler.

[11:45] And each one sort of had been worked out independently of each other using a more generic system where they compiled certain algorithms in there.

[11:51] Let me add, so making it generic can get really—

**SPEAKER_01:**
[11:54] Complicated terminology for the listener that you heard, that I barely remember.
[11:58] So SNARKs and STARKs were a thing that Vitalik was talking about a lot, and still does.
[12:03] So it's like "succinct, non-interactive, arbitrary something computation"—I can't remember.

**SPEAKER_03:**
[12:09] But basically interactive proof.

**SPEAKER_01:**
[12:10] Yes, but what's the whole acronym?
[12:12] But so there is a way, I think, to take an arbitrary computation and to prove that it has a certain result without revealing, like, the intermediate states and so on.
[12:22] But it's not computationally feasible—or it's just so slow that if you try to do it that way, it becomes very difficult.

[12:31] So I believe, just tying back to Jim's point, like you could try to do this in generality—like I can verify the EVM, like I can verify—there are these zkEVMs, like I verify any computation that comes out of this thing.
[12:41] And I think the problem with them has been performance.

[12:44] So the Zcash people, I guess, had to decompose every little step into specific circuits, right?
[12:49] Like, or—yeah, it's very, very low-level programming thinking in the ZK world. Like literally they're circuits that you end up compiling and so on and so forth.

**SPEAKER_03:**
[12:58] So yeah, Zcash at the moment is onto its—

**SPEAKER_01:**
[13:00] Yeah—

**SPEAKER_02:**
[13:01] And sort of by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one tumbler problem without going any more in depth than that.

[13:10] So this isn't like in the dream world—you would take any Ethereum contract and compile it somehow as something zero knowledge and then prove that you had run the full contract.
[13:18] That's something that, at the time at least so far in the world as it is—I didn't want to get into it or have us get into it as a company.
[13:26] But just to have these tumblers in place, I think that solves a lot of—

**SPEAKER_00:**
[13:29] Yeah, Bob, you were saying something—

**SPEAKER_03:**
[13:31] Yeah.
[13:32] So Zcash is onto its fourth round of different cryptography.
[13:36] So I forget what they're called—Sapling, something else—they're onto Orchard now.
[13:39] But, I mean, that's been now over the course of nearly a decade.
[13:43] You know, each time you've got another sort of two years’ worth of leading edge advancement.

[13:48] And yeah, like talking about that performance thing.
[13:50] So something which I think has been a key piece in Zcash price appreciation recently has been the arrival of a functional mobile wallet.
[13:57] So that's called Zashi, which is made by the Electric Coin Company.
[14:01] But you're basically at the point where you can run that proof on your phone.
[14:06] So something which used to be laptop—7 minutes—is now phone—seconds.

[14:10] So what you've seen—if you look at the size of these shielding pools, where these pools are effectively like, you know, all of these things are all, you know, mixed and hidden together, right?
[14:19] The more that you've got in a pool, the more—you know, the more unlinkable you are if you have a, you know, if you do something simple like ring signatures, where you just—whatever.
[14:27] I think Monero's got 16 transactions that get all joined together.
[14:31] So you can trace through that to a degree.
[14:33] But if you've got hundreds or thousands or millions of people in that same pool, it's effectively completely anonymous at that point.

[14:41] But if you look at the stats of usage of these particular pools, are you seeing what proportion of the money supply has been shielded versus being transparent?
[14:51] I guess that's another thing to say, right?

[14:54] Bitcoin is transparent, you know, so same with Ethereum.
[14:57] But then they use the word "shielded" to talk about, you know, that you are within this anonymity set.

[15:03] So these earlier rounds—you know, you had a bit of use but not a ton of use.
[15:07] But right now—I can't find the view—but it was something like about 4 or 5 million of the 21 million were within that shielding pool.
[15:16] So, you know, a significant chunk of it is shielded now, which was never the case in the past.

[15:21] You know, I remember on ETC at some point we were looking at whether we were going to bring over the precompiles to do with some of the curves.
[15:27] I don't know if you remember that happened in Ethereum at some point.
[15:31] One of the Blake curves I think went into the precompile, and we were talking about whether we were going to do that or not.
[15:37] And really talking about gas limit as well—how gas expensive would operations be using these things even?

[15:42] And the stats at that time were—it’s like maybe 2% of transactions on Zcash were shielded, something like that.
[15:48] It's basically not being used at all; functionally pretty much identical to Bitcoin.
[15:53] But probably a lot of end users going, "Yeah, I'm using Zcash, I'm private."
[15:56] It's like, "Yeah, you're not at all. You are getting zero benefit at all."
[15:59] But yeah, that's really happening now.
[16:01] And I think it's just these rounds and rounds and years and years of research and then implementation of those—an engineering effort.
[16:09] And it's like, "Hey, it works now."

**SPEAKER_00:**
[16:11] Well, from your standpoint, Jim, like, is it a technological advancement that Zcash has created or is it just simply that these tumblers have gotten big enough that they offer real privacy?
[16:17] Do you know what I mean?

**SPEAKER_02:**
[16:18] It's—I mean, any of these things are technological advancements, but, I mean, you want to have the tumblers big enough so that you have some amount of anonymity within there.
[16:27] If it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_01:**
[16:32] I need to interject.
[16:34] I have a crypto friend who was texting about 30 seconds ago about whether I like Zcash at this price.
[16:40] This is a pre-recorded podcast.
[16:42] So, you know—well, I guess it'll run on Wednesday, November 12, but very timely.
[16:48] You know, I think it's sort of like—again, this is the old crypto joke where, like, when your dentist and realtor friends start asking you about Ripple and Cardano, time to unwind your positions a little bit.
[16:56] You know, it's the Zcash meta.
[16:58] I don't know, like, maybe that means there's room to run, maybe, maybe it's tops.

**SPEAKER_00:**
[17:02] But, well, as they say, it's like catching a falling knife, right? Like, you know, trying to figure out the peak of the market.

[17:08] I—okay, like, we've talked about kind of how Zcash works and it uses ZK in these sort of very specific areas and it's not, you know, programmable generally.

[17:16] Now, obviously, there's a lot of talk in the Ethereum world about zkEVMs.

[17:21] Do you guys have any thoughts on that?
[17:23] And, like, you know, how those work?
[17:25] Because, you know, at what point do we get like—is it truly impossible to get full programmability? Or do you know, is that something—

**SPEAKER_01:**
[17:33] That is just getting closer? From a market perspective, I think they're mostly zkEVMs have been used for scaling as opposed to privacy.
[17:41] Even there, you tend to see some amount of specificity.
[17:44] Like, I think I mentioned on a podcast before, I'm—you know, friend/acquaintances with the Lighter CEO, and Lighter uses—Lighter is like the L2 version of Hyperliquid, if you will, or where they do perps and they do zero knowledge matching off-chain but, you know, it actually works and it gets written to Ethereum, which is pretty cool and supposedly they're achieving really high throughputs this way.
[18:04] It's not necessarily privacy tech at all.
[18:06] I ran into some of the Aztec folks in Singapore—that seems trending.
[18:10] General purpose still on testnet but not full EVM—it's like a restricted UTXO-type language of sorts, I believe.

[18:17] I think there's—probably not being nearly as expert as Jim, who I'll defer to in a second—not being an expert.
[18:23] I think it will be—there's no intrinsic reason you can't make it full EVM or full Rust or JavaScript or whatever.

[18:32] But probably there will be a tremendous amount of optimization that would have to happen to make that happen.
[18:36] So you probably see special purpose for a while.

**SPEAKER_03:**
[18:39] I saw that—and now I'm blanking on the name—the ZK tech that was happening under the Polygon banner with Jordi Baylina, and I can't remember the name of the project now.
[18:47] They posted within the last few months that they were real-time ZK proving mainnet now.
[18:52] But, you know, it was with a battery of GPUs.
[18:55] It was not a thing that you would be doing yourself.
[18:58] But yeah, that full proving is, you know, is possible, possible.
[19:03] But yeah, you have that optimization to be done.

[19:07] But I mean, I think that's where things are going to end up.
[19:10] You've had this sort of improvement where starting at Bitcoin, it's like well, how are we going to prove, you know, get to global consensus and solve the double spend problem?
[19:19] Well, it's by publishing all of the details and then we're going to have redundant state machines running in parallel, right?
[19:25] And that's the answer.
[19:27] We know that works.
[19:29] It was like what Satoshi did—the big ugly thing—but it worked and it made this stuff possible that had never been possible before.

[19:35] But it is, you know, it's an incredibly big, ugly, expensive way of doing that.

[19:39] And then I think just over time, it's like, okay, well, having things public was sort of a requirement for that consensus model, but that was never intentional.

[19:48] Like, having them all as a public ledger like that—that's not a positive feature.
[19:53] Now, if you look at the cypherpunk culture that many of these people were coming out of, yeah, it's, it's private, unstoppable money. Like, yeah, no, it wouldn't be public.

[20:01] So I saw that, yeah, within weeks of Bitcoin starting, Hal Finney said, you know, looking at ways of improving anonymity in Bitcoin.

[20:09] So that was January 2009.
[20:12] You know, that was a cypherpunk's obvious first reaction is, "Yeah, this is cool now, but yeah, we should have privacy as well."
[20:18] And I think we're sort of getting to that point of—the tech has become good enough to solve that without broadcasting everything to everyone.

**SPEAKER_00:**
[20:26] Yeah.
[20:27] Jim, what do you think, like, you know, on the sort of general programmability ZK front?

**SPEAKER_02:**
[20:32] I wish I had more, you know, hands-on experience with general zk.
[20:35] I see a lot of people very excited by it and maybe in a way that makes me skeptical because it seems like a cool toy, but I am open to them working great.
[20:44] And so I don't want to make a strong, firm stance at the moment on them, but they would be great if they work.

**SPEAKER_00:**
[20:48] Yeah.
[20:49] It seems like the approach—to Kieran's point—is like find specific areas where you can create circuits and apply them and optimize for those, and then expand that over time.
[20:57] It's really about nailing those initial use cases.

**SPEAKER_02:**
[21:01] And that's why I was drawn to that, because if you really narrow it down to something really simple, then I think you can do it well.

**SPEAKER_01:**
[21:05] I've heard that people even maybe compile the specific circuits and then optimize, like you kind of write them with the general tool—some people do, I don't know—and then you kind of like, "Okay, I got the circuit for the specific thing, but then I got to make it, like, work," you know.

**SPEAKER_00:**
[21:15] Yeah, I think compiling a circuit is still pretty—very—like computationally intensive.
[21:22] But it's way less for most circuits once the circuit is compiled.
[21:27] It's way less to do the proof, which is, you know, and you've got to continue to push that down, but I think the ratio is very large.

[21:33] Okay, well, I think we are at time.
[21:35] You know, where can we find you?
[21:37] Jim, I'm going to start with you.

**SPEAKER_02:**
[21:39] Where can you find me?

**SPEAKER_00:**
[21:41] Yes, people—I hear—more and learn more about Jim, which I—you know, please speak up.
[21:46] Ask Jim where can—where they find you?

**SPEAKER_02:**
[21:49] I do have a Twitter handle.
[21:51] What is my Twitter handle?
[21:53] I can't remember, but probably J. Hermo.

**SPEAKER_00:**
[21:56] I guess it's Jam.
[21:57] Should probably try to check.

**SPEAKER_01:**
[21:59] Hold on.

**SPEAKER_02:**
[22:00] Yeah.

**SPEAKER_00:**
[22:01] But whatever it is, you should post more often.
[22:04] Okay.

**SPEAKER_02:**
[22:05] I, I Twitter—I like wake up one day and remember that Twitter exists.
[22:10] And then I Twitter—I tweet a lot and then—then I forget about it for a couple—

**SPEAKER_00:**
[22:16] Sorry, it's J for months like J—

**SPEAKER_01:**
[22:19] H O in the chat.
[22:21] I don't know if we can all see that—the studio chat.

**SPEAKER_00:**
[22:23] But yeah, so—so yes, you can find them at J Hermuz.

**SPEAKER_01:**
[22:25] Kieran, where can people find Hermuz?

**SPEAKER_00:**
[22:28] Oh, Jamsheed Hermos.

**SPEAKER_01:**
[22:30] Yeah, I'm on X Rubin.
[22:32] I'm also on Substack, trying to, you know—I have a couple old Medium posts that I've linked from there.
[22:37] I'm getting a little bit into a Substack rhythm.
[22:39] It'll probably be infrequent but at least of moderate to high quality.
[22:43] Also kjameslubin Substack I think, for now—maybe I'll change the URL and link it in the show notes when we start, assuming we do show notes and you—

**SPEAKER_00:**
[22:51] Can find me on X, Victor Wang.
[22:54] Bob has posted why I explained before in my handle.
[22:58] You can also find us on Telegram at the Straum Mercado Group.
[23:02] Just go to our website at straumercado.com and that will point you to Telegram.
[23:07] And Bob, where can people find you and what can people expect next week?

**SPEAKER_01:**
[23:11] Don't close it out, Bob.
[23:13] You're the resident Zcash shill.
[23:16] One year from now, Zcash price or market cap or both?

**SPEAKER_03:**
[23:19] I think it will be in the top 10.

**SPEAKER_01:**
[23:21] Top 10.

**SPEAKER_03:**
[23:23] It's been very close, and the primary reason is privacy is a big need and it solved it, right?
[23:28] It's not some future promise—like, it works.
[23:32] Right now there's a mobile app, people are using it.
[23:35] You've got like a 10-year—near 10-year—history of, you know, top brainiacs working on this.
[23:41] Lots of credibility.

[23:43] So, you know, I think it's great and then I'm looking forward to smart contracts with that kind of level as well.

[23:49] Just one more thing to mention.
[23:51] I couldn't remember Jordi's project—ZK-EVM.
[23:54] So that's a spinoff group now from Polygon led by Jordi Baylina, and they announced real-time proving of mainnet blocks—that was announced at EthCC this year.

[24:03] So proving a block in 7 1/2 to 12 seconds—so just under block time.
[24:09] However, it requires 24 very high powered GPUs or 48 more consumer spec, so you've got a rack.

**SPEAKER_00:**
[24:16] There we go.
[24:17] And Bob, with that prediction, where can we find you and can you give us a preview of what people can expect next week?

**SPEAKER_03:**
[24:22] Absolutely, yes.
[24:24] So, I'm Bob Summerwill—Summer like the season, W I L L—so on everything with that name.

[24:30] And yes, so next week we will have an early days of Ethereum interview with Christoph Jentzsch, formerly of FDEV, so was hired in September 2014 into that Berlin office, worked on testing, cross client testing and then later on Slock.it, with their smart locks and the creation of The DAO, which was probably, you know, Ethereum's first killer app—until killing.

**SPEAKER_00:**
[24:52] Killing in many different ways.
[24:54] Yes, by doing that. Or you can say birthing, because ETC came out of that.

**SPEAKER_03:**
[24:58] Correct. Right.

**SPEAKER_00:**
[24:59] Okay.
[25:00] Well, that's time.
[25:01] Thank you very much for joining us and we look forward to seeing you next week.
[25:05] Take care.

**SPEAKER_01:**
[25:07] Thanks, everybody.