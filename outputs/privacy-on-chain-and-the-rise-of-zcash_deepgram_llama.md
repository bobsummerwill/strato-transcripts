**SPEAKER_00:**
[00:00] Okay.
[00:02] Welcome, everyone.
[00:04] We have a very special and very timely topic today, privacy on chain and the rise of Zcash.
[00:08] And we sort of have a special guest today.
[00:11] So I'm Victor Wong.
[00:13] I am founder and chief product officer at BlockApps.
[00:16] I'll get to our normal guest, but today, we have Jim.
[00:20] Do you wanna give us a quick intro?

**SPEAKER_01:**
[00:22] Yeah.
[00:24] I'm also I've known Victor and Kieran for years.
[00:27] I'm one of the founders of BlockApps and CTO.

**SPEAKER_00:**
[00:31] And you're here in particular because I would call you a Zcash expert having written your own Zcash client.

**SPEAKER_01:**
[00:36] Well, I I I think I'm I'm more aspirational at this point in time.
[00:40] I mean, the way I learn about things is I try to write a client for it.
[00:44] So I was I was doing that, but then we got pulled in different directions.
[00:48] I got to the point where I had sort of replicated the actual client that could connect.
[00:52] It would bring the data in.
[00:54] It would bring the proofs in.
[00:56] But just about when I was getting to the good parts, that's when when we moved on to other things.

**SPEAKER_00:**
[01:00] Well, we're gonna put the number at between, like, 10 and a 100.
[01:04] May maybe 10.
[01:06] I would say there there's definitely less than 20 people who have written their own Zcash clients, probably.
[01:11] Well, yeah.
[01:13] Yeah.
[01:15] There's probably some core contributors.

**SPEAKER_02:**
[01:17] I imagine there's more than a handful into Zcash.
[01:20] But, you know, when Jim says non-expert, he you know, it's like, there are let's say yes.
[01:24] I'll I'll expand the range.
[01:26] Five to a 100 people who understand Zcash better on on the planet.
[01:30] Big, big, big range there, but we're talking about pretty small numbers in absolute terms.
[01:34] So Yeah.
[01:36] Yes.
[01:38] Exactly.
[01:40] I say

**SPEAKER_00:**
[01:42] if Jim's not an expert, I don't know what even expert means.
[01:46] Anyways, Karen, do you want to give a quick intro of yourself before we certainly.

**SPEAKER_02:**
[01:49] I'm our CEO.
[01:51] Been on these before.
[01:53] By the way, Vicky, we're letting Jim off the hook, calling him a special guest.
[01:57] He has to do this all the time now with our, you know, continued in the public press.
[02:01] So Okay.

**SPEAKER_00:**
[02:03] Special now.
[02:05] Not special in the future.
[02:07] Special today.
[02:09] Today is special, but it's the first of many.
[02:12] Let's just say that.
[02:14] I was looking through the the

**SPEAKER_03:**
[02:16] the prior videos.
[02:18] Jim has never appeared on one of our own spaces.
[02:21] He's only been on early days of the year.
[02:24] Okay.

**SPEAKER_00:**
[02:26] Older drinks.
[02:28] Well, there you go.
[02:30] Oh, no.
[02:32] You found out.
[02:34] But it won't be special soon.
[02:36] Bob, by the way, since you've spoken up, can you give that quick intro to yourself?
[02:40] So hi.
[02:42] I'm I'm Bob.
[02:44] I'm head of ecosystem.

**SPEAKER_03:**
[02:46] And, yeah, been doing a lot of a lot of spaces.

**SPEAKER_00:**
[02:49] Yeah.
[02:51] So I I think, you know, to level set because I think there's a lot of misunderstanding about what privacy is.
[02:55] What how would you define blockchain privacy and why do you think it's important?

**SPEAKER_03:**
[02:58] Who's that question for?

**SPEAKER_00:**
[03:00] Could be for anyone.
[03:02] Whoever wants to go.
[03:04] Karen, you want us to kick us off?
[03:07] Okay.
[03:09] I'll take it.
[03:11] So

**SPEAKER_02:**
[03:13] and for the I assume that the viewer is pretty deep in the space, but I'll I'll I'll bring it down to a fairly low technical level.
[03:18] So blockchains are great.
[03:20] They let you move digitally scarce value from party to party.
[03:24] And the way that this is typically done is that you've got a big address, which is almost, but not quite a public key,
[03:30] and you sort of sign a message that says, I, Kiran, but it's not Kiran because it's this address,
[03:35] send, you know, 3 ether to Bob, and it doesn't say Bob.
[03:40] It's another address.
[03:42] You don't quite know who either of those parties are.
[03:45] However, you've got the address forever,
[03:48] and often it is the case that you can piece together what happened based on that address.
[03:53] Let's say you're on a centralized exchange, which has KYC'd.
[03:57] It knows how to associate you to maybe a withdrawal address.
[04:01] It may not know down the line,
[04:03] but if you start to get a bunch of data points, can kind of piece together who sent what to whom,
[04:08] and you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone.
[04:14] And it's not while it's a cryptographic technology, it's not necessarily a private technology.
[04:19] And this has been a problem both in the consumer setting just for you know, people don't like this.
[04:24] Satoshi makes a comment, I believe, in the white paper saying that,
[04:28] you know, obviously, to prevent the double spend problem, which basically just is just that
[04:33] to ensure that it can't I mean, can't be created or destroyed except by the agreed mechanism.
[04:38] Obviously, you need to know the whole history.
[04:41] And so he sees the problem as intrinsic,
[04:44] but some technologies come out later that maybe calls that into question that that we'll, talk about.
[04:50] It's also an enterprise problem.
[04:52] So we can we can talk separately about our experience there.
[04:56] Sort of what the enterprises want is kind of the same as what the public blockchain people want except with selective visibility.
[05:02] So they wanna say you're doing, like, a on-chain stock stock trade, which is actually now starting to happen.
[05:08] You sorta wanna know the other party has the stock.
[05:11] You don't necessarily wanna know who the other party is,
[05:14] but you you wanna know that they acquired that stock legitimately.
[05:18] And then when you get it, you wanna be able to pass it on legitimately in the same way.
[05:22] And then there's sometimes this extra requirement that, like, the regulator can see everything.
[05:27] You know?
[05:29] So you you want sort of, like, a unlinkability of balance to person or company,
[05:34] but also this mass preservation property that I was talking about can't create or destroy assets.
[05:40] They have to be acquired legitimately and and so on.
[05:44] So it's a perennial problem and closer to solved, you know, but we we can go into that shortly.
[05:50] Yeah.
[05:52] Bob, did you wanna add anything to that?

**SPEAKER_03:**
[05:54] Yeah.
[05:56] So, I mean, going back to those Bitcoin, you know, beginnings in the Bitcoin white paper,
[06:01] you know, it it it just talks about severing identity from transactions.
[06:06] But but really, that's just pseudo pseudonymous, you know, not not anonymous.
[06:12] And I think a lot of people didn't understand that differentiation back in those early days,
[06:17] and it's like, oh, Bitcoin's private, untrackable, digital money.
[06:22] But, you know, very rapidly, you have blockchain analytics coming in,
[06:27] you know, looking for correlations and patterns and it's like, yeah,
[06:32] that's you're not getting a lot of security, you know, even if you're not reusing addresses, just just normal things that people would do.
[06:38] There's there's lots of correlations and, you know, you can get unmasked that way.
[06:43] But, yeah, Satoshi did talk a bit about zero knowledge.
[06:47] I can't remember who raised it.
[06:49] Somebody raised it early,
[06:51] and and he was like, yeah.
[06:53] You know, that would be interesting if we could do that.
[06:56] But but it was just like a lot of that cryptography, you know, just didn't hadn't happened.
[07:01] You know?
[07:03] So Zcash started in 2016
[07:06] and it was only around that kind of time or a little before that you started having,
[07:11] you know, these these papers on on stock constructions
[07:15] and going through all these different kind of rounds.
[07:19] So, yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path.
[07:24] You know, they are in a mutable public ledger forever.
[07:29] Ethereum even worse because it's an account model.
[07:33] So you're you are reusing the addresses all the time.
[07:37] Right?
[07:39] And if your address is unmasked, you are forever doxed.
[07:43] That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address of his,
[07:50] which is probably not desired.

**SPEAKER_00:**
[07:53] Well and I I you know, you guys have been talking about Satoshi.
[07:57] But, Jim, I remember I think it's, like, earlier at, like, 2014.
[08:02] Vitalik was talking like he was like, z k snark will fix all of this at some point in time.
[08:08] Do you remember that at all?
[08:11] Well,

**SPEAKER_01:**
[08:13] I mean, like, I think we went through a learning process about privacy,
[08:17] and and and that's sort of, like, we're we're understating this right now.
[08:22] May maybe it's because we put a lot of time and effort into some privacy solutions that technically worked,
[08:28] but were a business failure, I think, is fair to say.
[08:33] And, so so, you know, the audience can learn from our our, like, sort of failed mistakes in the past right now.
[08:40] But, we sort of built so we had heard years ago of about CK, but we sort of just I I don't know.
[08:47] At the time, into it and said, like, oh, this looks like overly complicated.
[08:53] You can get privacy through these other means.
[08:57] And we ended up building a system that that allowed for sort of, like, quick spin up of private chains
[09:03] that everything was sort of, like, in an encrypted tunnel,
[09:07] and you could you could have, like, these chains completely secure.
[09:12] Nobody else would see what was happening there.
[09:15] But but long story short, you know, slow learning process.
[09:20] We we found out that customers want everything
[09:24] and and to the point that it made it worthless.
[09:28] Like, they we would go into enterprise.
[09:31] We would say, like, oh, you can set up these private channels with others.
[09:36] And they love that because they could sort of control that,
[09:40] and they could control who goes in there.
[09:43] But then once everything was going through these private channels,
[09:47] then they wanted to be able to, like, transfer from private chain to private chain,
[09:52] and that's where everything started to fall apart.
[09:56] And getting things back onto the main chain became sort of this extra complicated system.
[10:02] And at the same time, customers wanted to have, like, full flexibility
[10:07] in having, like, extensions to, solidity where where you could just, like, name a chain and send some money from chain a to chain b.
[10:14] And, really, the only way to make that stuff work is you have to go back to z k.
[10:20] So z k is overly complicated,
[10:23] but it is necessary.
[10:25] And and so so we started looking at that again,
[10:29] but I think, like, the safe thing to do is start with a a proven technology.
[10:34] And Zcash had been around for years and and nobody had stolen money.
[10:40] And this is just sort of like a subset of of ZK, but it's it's it's kind of a cool thing.
[10:46] You can you can build what they call tumblers of money.
[10:50] You throw a bunch of money in,
[10:53] and then the money that you put into the tumbler is you know how much went in,
[10:58] but but the ownership is completely scrambled up.
[11:02] And at any time, you can go and and transfer money from within the tumbler from one user to another,
[11:08] But only the users who did the transferring and got the money know what was there,
[11:13] but nobody else can see what's happening.
[11:17] So, again, like, you have these systems of multiple users with lots of money,
[11:22] but you don't know who owns percentage of of the money.

**SPEAKER_00:**
[11:25] Yeah.
[11:27] Actually, before we even go that far, can we talk just, like, what is ZK and how does it work,
[11:32] and why is it an important part of the solution?
[11:36] I I wanna pull back for also a a second.

**SPEAKER_02:**
[11:39] I remember I think there was an Ethereum meetup in New York.
[11:43] I'm not sure if either of guy you guys were there.
[11:46] I think I spoke at it, maybe.
[11:49] And there was also a Zcash, I think, presentation there.
[11:53] And it was, at that time, taking seven minutes to generate the ZK proofs.
[11:59] So Yes.
[12:01] Yeah.
[12:03] Wanted to make a transaction.
[12:05] You'd like, did this thing.
[12:07] It took seven minutes,
[12:09] and then the verification was kinda fast.
[12:12] Once you had it and you sent it to the network, things could go on, you know,
[12:17] but the usability was not there in those days.
[12:21] This is part of the reason we weren't, like, gonna tell our enterprise customers, like, oh, yeah.
[12:26] Let's let's z k everything.
[12:29] You know, even if we had it all integrated nicely,
[12:32] there's a lot of devil in the details.
[12:35] I know it was unbelievably

**SPEAKER_01:**
[12:37] slow for a while, and I think it's fixed.
[12:40] But Yeah.
[12:42] I know.
[12:44] Well, it's complicated.
[12:46] I mean, this is what I was trying to to say before.
[12:50] It's like, have, like, sort of nuts and bolts experience of what's going on in Zcash.
[12:55] But the more complicated world of zero knowledge,
[12:59] that that's my aspirational part right now.
[13:02] I can sort of see pieces moving within there,
[13:05] but but would hesitate to speak more broadly on this.
[13:09] Except let's say that that that it is more complicated than any of the, like, for instance, Ethereum client implementation stuff that we're doing back the day.
[13:17] Yeah.
[13:19] Yeah.
[13:21] Can you give a high-level summary of what zero knowledge is?
[13:25] Like, I think very few people understand.

**SPEAKER_02:**
[13:28] I I have a good layman example Okay.
[13:31] I think, and Jim can correct me.
[13:34] So I I did want to take a theoretical cryptography class,
[13:38] and the example they bring up is the CEO problem, so to speak.
[13:42] So we got two CEOs,
[13:45] and they're high ego guys.
[13:47] You know?
[13:49] And they wanna know
[13:51] who has the most between the two.
[13:54] But they don't wanna know how much money.
[13:57] They merely wanna know which one has more.
[14:00] And you would think that there wouldn't really be a way to create a scheme
[14:04] in which they could learn that information and nothing else,
[14:08] but there actually is.
[14:11] I and, again, this is, almost ten years ago now, so I may be describing the example incorrectly.
[14:17] But, yeah, that's that's like a case where you might want zero knowledge.
[14:22] Similarly, like, you know, like an ID check-in a bar.
[14:26] You're leaking all your personal info when you hand the ID to the bouncer,
[14:31] your home address, your full name, your date of birth, you know, etcetera.
[14:37] So you may wanna prove to the bar that you're 21 without handing any other info over,
[14:43] basically.
[14:45] I think this is the general setting that that it ends up at.
[14:49] Jim, do I you wanna take them, run with it, correct it?
[14:53] Yeah.

**SPEAKER_01:**
[14:55] So this is when you first look up zero knowledge, there are lots of little examples like this.
[14:59] They're all pretty cool.
[15:01] But and and what what's really happening in Zcash is that what you're trying to do is
[15:06] pass money from person a to person b.
[15:10] And person a wants to prove to person b that they have the money and that it was actually actually transferred,
[15:16] but without giving away the amount of money that person a has or without person a learning how much that person b has.
[15:23] Just that, you know, that the state before was that that you had the amount and that the state after is that it was transferred over.
[15:30] And then also no one else in the world can can know this.
[15:34] So you're you're you're proving sort of the important parts, not others.
[15:40] Zero knowledge could get pretty complicated too because when when you start looking into it,
[15:46] there are a lot of one-off examples, like like you're talking about, that you sort of see a solution to.
[15:52] But the problem comes about in trying to come up with a sort of a generic solution where you can almost just compile any any amount of code into some z k proof and then and then run that for anything.
[16:02] I don't remember because it's been about a year now, but but in zero cash, there were multiple multiple zero knowledge proofs in there for various aspects.
[16:12] If I were I you know, I'm I'm I might be making up some of the details here,
[16:17] but I think there was, like, one proof was, like, to show that you had more than such and such money before the transfer.
[16:24] I I might have it slightly off, but that there were multiple of these zero knowledge algorithms in there.
[16:31] But put together, they allowed for the for the full sort of transfer of of money within the tumbler.
[16:38] And each one sort of had been worked out independently of each other using a more generic system where they compiled certain certain algorithms in there.
[16:47] Let me Does that make sense?
[16:50] So making a generic can get really complicated.

**SPEAKER_02:**
[16:53] Terminology for the list listener that you've heard that I barely remember.
[16:58] So snarks and starks were a thing that Vitalik was talking about a lot and still does.
[17:03] So it's like succinct, noninteractive, arbitrary, something compute I can't remember.
[17:10] Like but basically interactive proof.
[17:13] Yes.
[17:15] But what's the whole acronym?
[17:18] But so there is a way, I think, to take an arbitrary computation and to prove that it has a certain result without revealing, like, the intermediate states and so on.
[17:28] But it's not computationally feasible.
[17:32] Like or it's it's just so slow that if you try to do it that way, it becomes very difficult.
[17:38] So I believe just just tying back to Jim's point.
[17:42] Like, you could try to do this in a generality.
[17:46] Like, I can like, the EVM.
[17:49] Like, I can verify there is z k EVMs.
[17:52] Like, I can verify any computation that comes out of this thing.
[17:56] And I think the problem with them has been performance.
[18:00] And so the Zcash people, I guess, had to decompose every little step into specific z circuits.
[18:07] Right?
[18:09] Like or Yeah.
[18:11] Yeah.
[18:13] So, yeah, it's very, very low-level programming thinking in the the ZK world.
[18:19] Like, literally, there's there's circuits that you end up compiling and and and so on and so forth.

**SPEAKER_01:**
[18:23] So, yeah, Zcash at the moment is onto it today.
[18:27] And and sort of by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one tumbler problem without going any more in-depth than that.
[18:37] So this isn't like like, in the dream world, you would take any, like, Ethereum contract and pilot somehow as a as a, you know, something zero knowledge and then prove that that that you had run the the full contract.
[18:49] That's something that, at the time, at at least so far in the the world as it is, I I didn't wanna get into it or or have us get into the company.
[18:58] But just to have these tumblers in place, I think that solves a lot of

**SPEAKER_03:**
[19:01] Yeah.
[19:03] So, Zcash is onto its fourth round of different cryptography.
[19:08] So I forget what they're called, sapling something else.
[19:12] We're onto Orchard now.
[19:15] But but, I mean, that's been now over the course of nearly a decade.
[19:20] You know, each time you've got another sort of two years worth of leading edge advancement.
[19:26] And and, yeah, like, talking about that performance thing.
[19:31] So it's something which I think has been a key piece in in Zcash price appreciation recently has been the arrival of a functional mobile wallet.
[19:41] So that's called Zashi, which is made by the electric coin company.
[19:46] But you're basically at the point where you can run that proof on your phone.
[19:51] So something which used to be laptop seven minutes is now phone second.
[19:58] So what you've seen, if you look at the size of these shielding pools where these pools are effectively like, you know, all of these things are all, you know, mixed and hidden together.
[20:09] Right?
[20:11] The the more that you've got in a pool, the more, you know, and and the more unlinkable you are.
[20:18] If you have a you know, if you if you do something simple like ring signatures where you just whatever sick I think, Monero has got 16 transactions that that, you know, get all joined together.
[20:30] So you can trace through that to a degree.
[20:34] But if you've got, you know, hundreds or thousands or millions of people in that same pool, you know, it's it's effectively, you know, completely anonymous at that point.
[20:45] But if you look at the stats of usage of these particular pools, are you seeing what proportion of the money supply has been shielded versus being transparent?
[20:56] I guess that's just another thing to say, right, is is Bitcoin is transparent, you know, so same same with Ethereum, but then they they they use the world word shielded to talk about, you know, that you are within this anonymity set.
[21:09] So these earlier rounds, you know, you had a bit of use, but not a ton of use.
[21:14] But right now, I can't find the view, but it but it was something like about four or 5,000,000 of the 21,000,000 were within that shielding pool.
[21:26] So, you know, a significant chunk of it is shielded now, which was never the case in the past.
[21:32] You know?
[21:34] I remember on ETC at some point, we were looking at whether we were gonna bring over the precompiles to do with some of the curves.
[21:41] You know?
[21:43] I don't know if you remember that happened in Ethereum at some point, but one of the like curves, I think, went into the precompile.
[21:50] And we were talking about whether we were gonna, like, do that or not.
[21:54] And really, talking about gas limit as well, you know, like, how how gas expensive would operations be using these things even.
[22:02] And the stats at that time were, you know, it's like maybe 2% of transactions on the cash were shielded, something like that.
[22:11] You know, it's basically, like, not being used at all, you know, functionally pretty much identical to Bitcoin.
[22:18] But probably a lot of venues is going, yeah, I'm using Zcash.
[22:23] I'm private.
[22:25] It's like, yeah, you cannot not at all.
[22:28] It's you're getting zero benefit at all.
[22:31] But, yeah, that's that's really happening now.
[22:34] And I think it's just, you know, these rounds and rounds of years and years of research and then implementation of those and engineering effort, and it's like, hey.
[22:44] It works now.

**SPEAKER_00:**
[22:46] Well, I just curious from from your standpoint, Jim, like, is it a technological advancement that has created, or is it just simply that these tumblers have gotten big enough that they offer real privacy?
[22:55] Do you know what I mean?

**SPEAKER_01:**
[22:58] It's I mean, any of these things are technological advancements.
[23:01] But, I mean, you wanna have the tumblers big enough so that that you have some amount of anonymity within there.
[23:07] It's not like if it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_02:**
[23:11] I I need to interject.
[23:13] I I have a crypto friend who was texting about thirty seconds ago about whether I like CCash at this price.
[23:19] This is a prerecorded podcast.
[23:22] So, you know, well, I guess it'll it'll run on Wednesday, November 12.
[23:28] But, very timely, you know, I think.
[23:31] It's sort of like I again, there's there's the old crypto joke where, like, when your dentist and realtor friends start asking you about Ripple and Cardano, it's time to unwind your positions a little bit.
[23:41] You know?
[23:43] But it's the Zcash meta.
[23:46] I don't know.
[23:48] Like, maybe that means there's room to run.
[23:51] Like, maybe maybe it's tops.

**SPEAKER_00:**
[23:54] But Well, as they say, it's like catching a falling knife.
[23:58] Right?
[24:00] Like, you know, like Yeah.
[24:02] Trying to figure out the the peak of the market.
[24:06] I I okay.
[24:08] Like, we've talked about kind of how zCatch works,
[24:12] and it uses z k in these sort of very specific areas.
[24:17] And it's not, you know, programmable generally.
[24:21] Now, obviously, there's a lot of talk in the Ethereum world about z k EVMs.
[24:27] You guys have any thoughts on that and, like, you know, how those work?
[24:32] Because, you know, at what point do we get like, is it truly impossible to get full programmability,
[24:38] or do you know, is that something that is just getting closer?

**SPEAKER_02:**
[24:41] From a market perspective,
[24:43] I think they're mostly z k AVMs have been used for scaling as opposed to privacy.
[24:49] Even there, you tend to see some amount of specificity.
[24:53] Like, think I I mentioned on a podcast before, I'm, you know, friend acquaintances with the lighter CEO,
[24:59] and lighter uses lighter is like the l two version of Hyperliquid,
[25:04] if you will, where they they do perks and they do zero knowledge matching off chain,
[25:10] but you know it actually works and it gets written to Ethereum,
[25:15] which is pretty cool.
[25:17] And, supposedly, they're achieving really high throughputs this way.
[25:22] It's not necessarily privacy tech at all.
[25:26] I ran into some of the Aztec folks in Singapore,
[25:30] and it seems trending general purpose still on test net,
[25:35] but not fully VM.
[25:38] It's like a restricted UTXO type language of sorts, I believe.
[25:43] So I think there's probably not being nearly as expert as Jim, who I'll defer to in a second,
[25:50] not being an expert,
[25:52] I think it will be there's no intrinsic reason you can't make it fully VM or full rust or some, you know, JavaScript or whatever.
[26:01] But, probably, there will be a tremendous amount of optimization that would have to happen to make that happen.
[26:09] So you probably see special purpose for a while.

**SPEAKER_03:**
[26:12] I saw that and now I'm blanking on the name.
[26:16] The the ZK tech that was happening under the Polygon banner with,
[26:22] and I can't remember the the the name of the project now.
[26:28] They posted it within the last few months that they were real-time ZK proving mainnet now.
[26:35] But, you know, it was with a battery of of GPUs.
[26:40] It was not a thing that you would be doing yourself.
[26:44] But but, yeah, that that full proving is, you know, is possible.
[26:50] But, yeah, you you you have that optimization to to be done.
[26:55] But, I mean, I think I think that's where things are gonna end up that you've had this sort of improvement where starting at Bitcoin,
[27:02] it's like, well, how are we gonna prove, you know, get to global consensus and and solve the double spend problem?
[27:10] Well, it it's by publishing all of details,
[27:14] and then we're gonna have, you know, redundant state machines running in parallel.
[27:20] Right?
[27:22] And that's that's the answer we know that works.
[27:26] It was like, what's you know you know, like, Satoshi did the big ugly thing,
[27:32] but it worked and it made this stuff possible that had never been possible before.
[27:38] But it is, you know, it's it's an incredibly big, ugly, expensive way of doing that.
[27:44] And then I think just over time, it's like, okay.
[27:48] Well, having things public was sort of a requirement for that consensus model,
[27:54] but that was never intentional, like, having them all as a public ledger.
[28:00] Like, that that's not a positive feature.
[28:04] Now if you look at the cyberpunk culture that many of these people were coming out of,
[28:10] yeah, it's it's private unstoppable money.
[28:14] Yeah, no, it wouldn't be public.
[28:17] So I saw that,
[28:19] yeah.
[28:21] Within weeks of Bitcoin starting,
[28:24] how funny said, you know, looking at ways of improving anonymity in Bitcoin.
[28:30] So that was January 2009.
[28:34] You know, that was a cypherpunks obvious first reaction is, yeah, this is cool now.
[28:41] But, yeah, we should have privacy as well.
[28:45] And I think we're sort of getting to that point of the the tech has become good enough to to solve that without broadcasting everything to everyone.

**SPEAKER_00:**
[28:53] Yeah.
[28:55] Jim, what what do you think?
[28:58] Like, you know, on the sort of general programmability ZK front.

**SPEAKER_01:**
[29:01] I wish I had more, you know, hands-on experience with general ZK.
[29:06] I see a lot of people very excited by it.
[29:10] And maybe in a way that makes me skeptical because it seems like a cool toy.
[29:15] But I am open to them working great.
[29:19] And so I don't I don't wanna make us a a a strong firm stance at the moment on them,
[29:25] but, but they would be great if they work.

**SPEAKER_00:**
[29:28] Yeah.
[29:30] I I I it seems like the approach to Karen's point is, like, find specific areas where you can, you know, create circuits and apply them and optimize for those and then expand that over time.
[29:40] You know?
[29:42] Like, it's it's really about kind of, like, you know, nailing those initial use cases Then the using the dispatch approach.

**SPEAKER_01:**
[29:48] And that's why I was drawn to that because because Yeah.
[29:52] If you if you really narrow it down to something really simple,
[29:56] then I think you can do it well.

**SPEAKER_02:**
[29:59] I've heard that people even maybe compile the specific circuits and then optimize.
[30:04] Like, you kinda write them with the general tool.
[30:08] Some people do.
[30:10] I don't know.
[30:12] And then you kind of, like like, okay.
[30:15] I got the circuit for the specific thing, but then I gotta make it, like, work.
[30:20] You know?
[30:22] Yeah.
[30:24] Maybe

**SPEAKER_00:**
[30:26] I think compiling a circuit is still pretty very, like, computational intensive,
[30:32] but it's way more but it's way less for most circuits, once a circuit is compiled, it's way less to do the proof,
[30:40] which is you know?
[30:42] And you you gotta continue to push that down, but I think the ratio is very large.
[30:48] Okay.
[30:50] Well, I think we are out of time.
[30:53] You know, where can we find you, Jim?
[30:56] I'm gonna start with you.
[30:58] Where can find me?
[31:00] Yes.
[31:02] People wanna hear more and learn more about Jim, which I you know, please speak up.
[31:08] Ask him where can where they find you.

**SPEAKER_01:**
[31:11] I do have a Twitter handle.
[31:14] What is my Twitter handle?
[31:17] I can't remember.
[31:20] But

**SPEAKER_00:**
[31:22] probably j or model.
[31:25] I I guess it's probably.

**SPEAKER_02:**
[31:28] I'm gonna try to check.
[31:30] Hold on.
[31:32] Yeah.

**SPEAKER_01:**
[31:34] But whatever it is, you should post more often than it.
[31:38] Okay.
[31:40] I I I Twitter and spurge.
[31:43] Is.
[31:45] I, like, wake up one day and remember that Twitter exists,
[31:50] and then I twitter I tweet a lot, and then then I forget about that for a couple of weeks.
[31:57] It's j h

**SPEAKER_02:**
[31:59] o in the the chat.
[32:01] I I don't know if we can all see that, the studio chat.
[32:05] But Yeah.

**SPEAKER_00:**
[32:07] So so,

**SPEAKER_01:**
[32:09] yes, you can find him at j h e r m a s.
[32:14] Karen, where can people find Hermas.

**SPEAKER_00:**
[32:17] Yeah.
[32:19] Oh, j h e r m a s.

**SPEAKER_02:**
[32:22] Yeah.
[32:24] I'm on x k g Ruben.
[32:28] I'm also on Substack trying to, you know I'm, like, a couple old medium posts that I've linked from there.
[32:36] I I'm I'm getting a little bit into a Substack rhythm.
[32:41] I'll it'll probably be infrequent, but at least of moderate to high quality.
[32:47] Also, k james lubin dot Substack, I think, for now.
[32:54] Maybe I'll change the URL.
[32:58] Yeah.
[33:00] And link it in the in the show notes when we start assuming we do show notes.

**SPEAKER_00:**
[33:04] And you can find me on x at vic four Wang.
[33:09] Bob has posted why I explained before in my handle.
[33:14] You can also find us at on Telegram at the Straum Mercado Group.
[33:20] Just go to our website at straummercado.com,
[33:25] and that will point you to Telegram.
[33:29] And, Bob, where can people find you,
[33:32] and what can people expect next week?
[33:36] Don't close it out, Bob.
[33:38] You're the resident Zcash shill.
[33:41] One year from now, Zcash price or market cap or both?

**SPEAKER_02:**
[33:45] price or market cap or both?

**SPEAKER_03:**
[33:48] I I think it will be in the top 10.
[33:51] Top 10.
[33:53] It's been it's been very close.
[33:56] And the primary reason is privacy is a big need,
[34:01] and it solved it.
[34:04] Right?
[34:06] It's not some future promise.
[34:09] Like, it works right now.
[34:12] There's a mobile app.
[34:15] People are using it.
[34:18] You know?
[34:20] You've got, like, a ten-year near ten-year history of, you know, top brainiacs working on this.
[34:28] Lots of credibility.
[34:31] So, you know, I think it it it's great.
[34:35] And then I'm looking forward to smart contracts with with that kind of level as well.
[34:42] Just one more thing to mention.
[34:45] I couldn't remember Jordy's project, Zisk.
[34:50] So that was that's a spin-off group now from Polygon,
[34:55] led by Jordi, Baylina, and they announced real-time proving of mainnet blocks that was announced at FCC this year.
[35:05] So proving a block in seven and a half to twelve seconds,
[35:11] so just under block time.
[35:15] However, it requires 24 very high-powered GPUs or 48 more consumer spec.
[35:23] So you've got a rack.

**SPEAKER_00:**
[35:26] There you go.
[35:28] And Bob, with that prediction, where can we find you,
[35:32] and can you give us a preview of what people can expect next week?
[35:37] Absolutely.
[35:39] Yes.
[35:41] So I'm I'm Bob Summerwill, summer like the season, w I l l.

**SPEAKER_03:**
[35:45] So on, on everything with with that name.
[35:49] And, yes, so next week, we will have an early days of Ethereum interview,
[35:54] with Christophe YenSys, formerly of f dev.
[35:59] So he was hired in September 2014 into that Berlin office,
[36:04] worked on testing cross-line testing,
[36:08] and then later on, with with their smart locks and the creation of the DAO,
[36:14] which is probably, you know, Ethereum's first killer app until we're killing

**SPEAKER_00:**
[36:20] Killing in many different ways.
[36:23] Yes.
[36:25] We're doing that.
[36:27] Or Or or you can say birthing because ETC came out of that.
[36:33] Correct.
[36:35] Right.
[36:37] Okay.
[36:39] Well, that's time.
[36:41] Thank you very much for joining us,
[36:44] and we look forward to seeing you next week.
[36:48] Take care.
[36:50] Thanks, everybody.