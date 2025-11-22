**SPEAKER_02:**
[00:00] Okay. Welcome everyone. We have a very special and very timely topic today: Privacy on-chain and the rise of Zcash. And we sort of have a special guest today. So I'm Victor Wong. I am founder and chief product officer at BlockApps. I'll get to our normal guests, but today we have Jim. Do you want to give us a quick intro?

**SPEAKER_01:**
[00:19] Yeah, I'm also—I've known Victor and Kieran for years. I'm one of the founders of BlockApps and CTO. And you're here in particular because I would call you a Zcash expert, having written your own Zcash client. Well, I think I'm more aspirational at this point in time. I mean, the way I learn about things is I try to—

[00:39] How many more expert people do you think there are on, say, Zcash in particular on the planet? No, the problem that I have is that I was sort of halfway in the learning process last year.

[00:52] So the way I learn about things is I try to, like, write a client for it. So I was doing that, but then we got pulled in different directions. I got to the point where I had sort of replicated the actual client that could connect. It would bring the data in. It would bring the proofs in. But just about when I was getting to the good part, that's when we moved on to other things. Well, we're going to get to that later.

**SPEAKER_03:**
[01:12] Answer my own question, you put the number between like 10 and 100, maybe 10. Oh, I would say there's definitely less than 20 people who have written their own Zcash clients, probably. Well, yeah, there's probably some core contributors. I imagine there's more than a handful into Zcash. But when Jim says non-expert, it's like there are, let's say, yes.

[01:28] I'll expand the range. Five to 100 people who understand Zcash better on the planet. Big, big, big range there, but we're talking about pretty small numbers in absolute terms. Yes, exactly. I would say if Jim's not an expert, I don't know what even expert means. Anyways, Kieran, do you want to give a quick intro of yourself? Certainly.

[01:47] Um, I'm our CEO, been on these before. By the way, Vic, you're letting Jim off the hook calling him a special guest. He has to do this all the time now with our, you know, continued in the public. So special in the future, special today. Today is special, but it's the first of many. Let's just say. I was looking through the prior videos—Jim has never appeared on one of our own spaces.

**SPEAKER_02:**
[02:12] He's only been on early days of his career. Okay. There you go. But it won't be special soon. Bob, by the way, since you've spoken up, can you give a quick intro to yourself?

[02:22] So hi, I'm Bob. I'm head of ecosystem. And yeah, been doing a lot of spaces. Yeah. So I think, you know, to level set, because I think there's a lot of misunderstanding about what privacy is. How would you define blockchain privacy and why do you think it's important? Who's that question for?

**SPEAKER_03:**
[02:40] Could be for anyone, whoever wants to go. Kieran, you want to kick us off? I assume the viewer is pretty deep in the space, but I'll bring it down to a fairly low technical level.

[02:50] So blockchains are great. They let you move digitally scarce value from party to party. The way that this is typically done is that you've got a big address which is almost but not quite a public key and you sort of sign a message that says “I, Kieran”—but it's not Kieran because it's this address—“send three bitcoin to Bob,” and it doesn't say Bob, it's another address. You don't quite know who either of those parties are. However, you've got the address forever.

[03:17] And often it is the case that you can piece together what happened based on that address. So say you're on a centralized exchange which has KYC'd. It knows how to associate you to maybe a withdrawal address. It may not know down the line.

[03:32] But if you start to get a bunch of data points, you can kind of piece together who sent what to whom. And you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone. And while it's a cryptographic technology, it's not necessarily a private technology.

[03:52] And this has been a problem both in the consumer setting, just for, you know, people don't like this. Satoshi makes a comment, I believe, in the white paper saying that—

[04:01] Obviously, to prevent the double spend problem, which basically is just that to ensure that Bitcoin can't be created or destroyed except by the agreed mechanism—obviously, you need to know the whole history. And so he sees the problem as intrinsic. But some technologies come out later that maybe call that into question, which we'll talk about.

[04:21] It's also an enterprise problem, so we can talk separately about our experience there. Sort of what the enterprises want is kind of the same as what the public blockchain people want, except with selective visibility. So they want to say you're doing like an on-chain stock trade—which is actually now starting to happen. You sort of want to know the other party has the stock. You don't necessarily want to know who the other party is,

[04:41] but you want to know that they acquired that stock legitimately. And then when you get it, you want to be able to pass it on legitimately in the same way. And then there's sometimes this extra requirement that the regulator can see everything, you know, so you want sort of an unlinkability of balance to person or company, but also this mass preservation property that we were talking about—can't create or destroy assets; they have to be acquired legitimately,

**SPEAKER_00:**
[05:08] and so on. So it's a perennial problem and closer to solved than, you know, but we can go into that shortly. Yeah. Bob, did you want to add anything to that?

[05:19] Yeah, yes. I mean, going back to those bitcoin, you know, beginnings in the Bitcoin white paper, you know, it just talks about severing identity from transactions.

[05:27] But really, that's just pseudonymous, not anonymous. And I think a lot of people didn't understand that differentiation back in those early days. And it's like, oh, Bitcoin's private, untrackable,

[05:39] you know, digital money, but, you know, very rapidly you had blockchain analytics coming in, you know, looking for correlations and patterns and it's like, yeah, that's, you're not getting a lot of security, you know, even if you're not reusing addresses, just sort of normal things that people would do, there's lots of correlations and, you know, you can get unmasked that way.

[06:00] But yeah, Satoshi did talk a bit about zero knowledge. I can't remember who raised it. Somebody raised it early and he was like, yeah, that would be interesting if we could do that. But it was just like a lot of that cryptography just hadn't happened.

[06:14] You know, Zcash started in 2016 and it was only around that kind of time or a little before that you started having, you know, these papers on SNARK constructions and going through all these different kind of rounds. So, yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path—you know, they are an immutable public ledger forever.

[06:33] Ethereum, even worse, because it's an account model. So you are reusing the addresses all the time, right? And if your address is unmasked, you are forever doxxed. That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address of his, which probably not desired.

**SPEAKER_02:**
[06:54] And I, you know, you guys have been talking about Satoshi, but Jim, I remember, I think it’s like earlier, at like 2014, Vitalik was talking, like, he was like, “ZK-SNARKs will fix all of this at some point in time.” Do you remember that at all?

[07:06] Well, I mean, like, I think we went through a learning process about privacy and that's sort of like, we're understating this right now. Maybe it's because we put a lot of time and effort into some privacy solutions that

**SPEAKER_01:**
[07:16] technically worked, but were a business failure, I think is fair to say. And so, you know, the audience can learn from our, like, sort of failed mistakes in the past right now. But we sort of built—so we had heard years ago about ZK, but we sort of just, I don't know, at the time, looked into it and said like, oh, this looks overly complicated. You can get privacy through these other means. And we ended up building a system that

[07:37] allowed for, sort of like, quick spin-up of private chains, that everything was sort of like in an encrypted tunnel, and you could have like these chains completely secure, and nobody else would see what was happening there. But long story short, you know, slow learning process. We found out that customers want everything and

[08:00] to the point that it made it worthless. Like, we would go into enterprise, we would say like, oh, you can set up these private channels with others. And they loved that because they could sort of control that and they could control who goes in there. But then once everything was going through these private channels, then they wanted to be able to like transfer from private chain to private chain. And that's where everything started to fall apart. And getting things back onto the main chain became sort of this extra complicated system.

[08:28] And at the same time, customers wanted to have like a full flexibility in having like extensions to Solidity, where you could just like name a chain and send some money from chain A to chain B. And really the only way to make that stuff work is you have to go back to ZK. So ZK is overly complicated, but it is necessary. And so,

[08:50] we started looking at that again, but I think like the safe thing to do is start with a proven technology and Zcash had been around for years and nobody had stolen money. And this is just sort of like a subset of ZK, but it's kind of a cool thing. You can build what they call tumblers of money. You throw a bunch of money in and then

[09:12] the money that you put into the tumbler is—you know how much went in, but the ownership is completely scrambled up. And at any time, you can go and transfer money from within the tumbler from one user to another, but only the users who did the transferring and got the money know what was there, but nobody else can see what's happening. So again, you have these systems of multiple users with lots of money, but you don't know who owns a percentage of the money.

**SPEAKER_03:**
[09:36] Yeah, actually, before we even go that far, can we talk just like what is ZK and how does it work and why is it an important part of the solution? I want to pull back for also a second. I remember, I think there was an Ethereum meetup in New York. I'm not sure if either of you guys were there. I think I spoke at it, maybe.

[09:54] There was also a Zcash, I think, presentation there. And it was, at that time, taking seven minutes to generate the ZK proofs. So if you wanted to make a transaction, you did this thing. It took seven minutes. And then the verification was kind of fast. So once you had it and you sent it to the network, things could go on.

[10:13] The usability was not there in those days. This is part of the reason we weren't like going to tell our enterprise customers, like, "Oh yeah, let's ZK everything." You know, even if we had it all integrated nicely, there's a lot of devil in the details—that it was unbelievably slow for a while. And I think it's fixed, but yeah, it's complicated. I mean, what I was trying to say before is like, I have like sort of nuts and bolts experience of what's going on in Zcash.

**SPEAKER_01:**
[10:38] But the more complicated world of zero knowledge, that's my aspirational part right now. I can sort of see pieces moving within there, but would hesitate to speak more broadly on this. Except I'll say that it is more complicated than any of the, like, for instance, Ethereum client implementation stuff that we're doing.

**SPEAKER_03:**
[10:59] Yeah, can you give a high-level summary of what zero knowledge is? I think very few people understand. I have a good layman example, I think. And Jim can correct me. So I did once take a theoretical cryptography class. And the example they bring up is the CEO problem, so to speak. So you've got two CEOs. And they're high ego guys.

[11:18] And they want to know... Do you say that from experience, Kieran? I'm not speaking about myself. They want to know who has the most between the two. But they don't want to know how much money. They merely want to know—

[11:32] which one has more. And you would think that there wouldn't really be a way to create a scheme in which they could learn that information and nothing else. But there actually is.

[11:43] And again, this is almost ten years ago now, so I may be describing the example incorrectly. But yeah, that's like a case where you might want zero knowledge. Similarly, like, you know, like an ID check at a bar, you're leaking all your personal info when you hand the ID to the bouncer—your home address, your full name, your date of birth, etc. So you may want to prove to the bar that you're over 21

**SPEAKER_01:**
[12:07] without handing any other info over, basically. So I think this is the general setting that it ends up at. Jim, do you want to take that and run with it, correct it? Yeah, so when you first look up zero knowledge, there are lots of little examples like this that are all pretty cool. And what's really happening in Zcash is that what you're trying to do is

[12:27] pass money from person A to person B, and person A wants to prove to person B that they have the money and that it was actually transferred, but without giving away the amount of money that person A has, or without person A learning how much that person B has—just that you know that the state before was that you had the amount and that the state after is that it was transferred over. And then also no one else in the world can know this. So you're proving sort of the important parts, but not others. Zero knowledge could get,

[12:56] pretty complicated, too, because when you start looking into it, there are a lot of one-off examples like you're talking about that you can sort of see a solution to. But the problem comes about in trying to come up with sort of a generic solution where you can almost just compile any amount of code into some ZK proof and then run that for anything. I don't remember because it's been about a year now, but in Zerocash, there were multiple zero knowledge proofs in there

[13:22] for various aspects. I might be making up some of the details here, but I think there was one proof was to show that you had more than such and such money before the transfer. I might have it slightly off, but there were multiple of these zero knowledge algorithms in there. But put together, they allowed for the full sort of transfer of money within the tumbler. And each one sort of had been worked out independently of each other.

**SPEAKER_03:**
[13:49] Using a more generic system where they'd compiled certain algorithms in there. If that makes sense. So making it generic can get really complicated. Terminology for the listener that you may have heard that I barely remember. So SNARKs and STARKs were a thing that Vitalik was talking about a lot and still does. So it's like succinct, non-interactive...

[14:06] Arbitrary something, I can't remember. But basically, interactive proof. Yes. But what's the whole acronym? So there is a way, I think, to take an arbitrary computation and to prove that it has a certain result without revealing the intermediate states and so on. But it's not computationally feasible. Or it's just so slow that if you try to do it that way,

[14:26] it becomes very difficult. So I believe, just tying back to Jim's point, like you could try to do this in a generality. Like the EVM—like I can verify, there are these ZK-EVMs. I can verify any computation that comes out of this thing. And I think the problem with them has been performance. And so the Zcash people, I guess, had to decompose every little step into specific circuits, right? Or specific—yeah.

**SPEAKER_01:**
[14:49] It's very low-level programming thinking in the ZK world. Literally, they're circuits that you end up compiling and so on and so forth. So yeah, Zcash at the moment is onto its feet, and sort of by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one tumbler problem without going any more in-depth than that. So this isn't like—

[15:13] Like in the dream world, you would take any Ethereum contract and compile it somehow as something zero knowledge and then prove that you had run the full contract. That's something that, at the time, at least so far in the world as it is, I didn't want to get into it or have us get into the company. But just to have these tumblers in place—I think that solves a lot.

**SPEAKER_00:**
[15:33] Yeah, Bob, you were saying something? Yeah, so Zcash is onto its fourth round of different cryptography. So I forget what they're called—Sapling, something else. We're onto Orchard now. But I mean, that's been now over the course of nearly a decade. Each time, you've got another sort of two years’ worth of leading edge advancement. And...

[15:56] And yeah, like talking about that performance thing. So something which I think has been a key piece in Zcash price appreciation recently has been the arrival of a functional mobile wallet. So that's called Zashi, which is made by the—

[16:14] Electric Coin Company. But you're basically at the point where you can run that proof on your phone. So something which used to be laptop seven minutes is now phone seconds. So what you've seen, if you look at the size of these shielding pools, where these pools are effectively like, you know, all of these things are all

[16:35] you know, mixed and hidden together, right? The more that you've got in a pool, the more, you know, the more unlinkable you are. If you have a, you know, if you do something simple like ring signatures where you're just—whatever, I think Monero's got 16 transactions that, you know, get all joined together. So you can trace through that

[16:57] to a degree, but if you've got hundreds or thousands or millions of people in that same pool, it's effectively completely anonymous at that point. But if you look at the stats of usage

[17:10] of these particular pools, are you seeing what proportion of the money supply has been shielded versus being transparent? I guess that's another thing to say, right? Bitcoin is transparent, so same with Ethereum. But then they use the word "shielded" to talk about that you are within this anonymity set.

[17:27] So these earlier rounds, you had a bit of use, but not a ton of use. But right now—I can't find the view—but it was something like about four or five million of the 21 million were within that shielding pool. So a significant chunk of it is shielded now, which was never the case in the past.

[17:47] I remember on ETC at some point, we were looking at whether we were going to bring over the precompiles to do with some of the curves. I don't know if you remember that happened in Ethereum at some point, but one of the Blake curves, I think, went into the precompile. And we were talking about whether we were going to do that or not. And really talking about gas limit as well. How gas expensive would operations be using these things even?

[18:12] And the stats at that time were, you know, it’s like maybe 2% of transactions on Zcash were shielded, something like that. You know, it's basically like not being used at all, you know, functionally pretty much identical to Bitcoin. But probably a lot of end users going, yeah, I'm using Zcash, I'm private. And it's like, yeah, you know, you're not at all. You're getting zero benefit at all.

**SPEAKER_02:**
[18:36] But yeah, that's really happening now. And I think it's just, you know, these rounds and rounds and years and years of research and then implementation of those and engineering effort. And it's like, hey, it works now. Well, from your standpoint, Jim, like, is it a technological advancement that Zcash has created? Or is it just simply that these tumblers have gotten big enough that they offer real privacy? Do you know what I mean?

**SPEAKER_01:**
[18:57] I mean, any of these things are technological advancements. But, I mean, you want to have the tumblers big enough so that you have some amount of anonymity within there. If it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_03:**
[19:11] I need to interject. I have a crypto friend who was texting about 30 seconds ago about whether I like Zcash at this price. This is a pre-recorded podcast. So, you know, I guess it'll run on Wednesday, November the 12th. But very timely, you know, I think.

[19:26] It's sort of like—again, there's the old crypto joke where like when your dentist and realtor friends start asking you about Ripple and Cardano, it's time to unwind your positions a little bit, you know? But it's the Zcash meta. I don't know, like maybe that means there's room to run, maybe, maybe it’s tops, but—well, as they say, it's like catching a falling knife, right? Like, you know, trying to figure out the peak of the market.

**SPEAKER_02:**
[19:49] We've talked about how Zcash works and it uses ZK in these very specific areas and it's not programmable generally. Now, obviously, there's a lot of talk in the Ethereum world about ZK-EVMs. Do you guys have any thoughts on that and how those work? Because at what point do we get...

**SPEAKER_03:**
[20:04] Is it truly impossible to get full programmability or is that something that is just getting closer? From a market perspective, I think they're mostly ZK-EVMs have been used for scaling as opposed to privacy. Even there, you tend to see some amount of specificity. Like, I think I mentioned on a podcast before, I'm friend acquaintances with the Lighter CEO, and Lighter uses—

[20:27] Lighter's like the L2 version of Hyperliquid, if you will, where they do perps and they do zero knowledge matching off-chain, but you know it actually works and it gets written to Ethereum, which is pretty cool. And supposedly they're achieving really high throughputs this way. It's not necessarily privacy tech at all.

[20:45] Ran into some of the Aztec folks in Singapore, and it seems, trending general purpose—still on testnet, but not fully VM. It's like a restricted UTXO-type language of sorts, I believe. So I think there's probably—not being nearly as expert as Jim, who I'll defer to in a second. Not being an expert, I think it will be—there's no intrinsic reason you can't make it

[21:06] full EVM or full Rust or, you know, JavaScript or whatever, but probably there will be a tremendous amount of optimization that would have to happen to make that happen. So you probably see special purpose for a while. I saw, and now I'm blanking on the name, the ZK tech that was happening under the Polygon

**SPEAKER_00:**
[21:24] banner, with Jordi Baylina, and I can't remember the name of the project now—they posted within the last few months that they were real-time ZK proving mainnet now. But, you know, it was with a battery of GPUs; it was not a thing that you would be doing yourself. But yeah, that full proving is possible, but yeah, you have that optimization to be done. But I mean, I think that’s where things are going to end up, that you’ve had this

[21:54] sort of improvement, where starting at Bitcoin, it's like, well, how are we going to prove—you know, get to global consensus and solve the double spend problem? Well, it's by publishing all the details and then we're going to have, you know, redundant state machines running in parallel, right? And that's the answer. We know that works. It was like, what's—you know, like Satoshi did the big ugly thing,

[22:15] but it worked and it made this stuff possible that had never been possible before. But it is, you know, it's an incredibly big, ugly, expensive way of doing that. And then I think just over time, it's like, OK, well,

[22:27] having things public was sort of a requirement for that consensus model, but that was never intentional. Like, having them all as a public ledger like that—that's not a positive feature. Now, if you look at the cypherpunk culture that many of these people were coming out of—yeah, it's private, unstoppable money. Like, yeah, no, it wouldn't be public. So I saw that, yeah, within weeks

[22:50] of Bitcoin starting, Hal Finney said, you know, looking at ways of improving anonymity in Bitcoin. So that was January 2009. You know, that was a cypherpunk's obvious first reaction is, yeah, this is cool now. But yeah, we should have privacy as well. And I think we're sort of getting to that point—the tech has become good enough to solve that without broadcasting everything to everyone.

**SPEAKER_01:**
[23:14] Yeah, Jim, what do you think, like, you know, on the sort of general programmability ZK front? I wish I had more, you know, hands-on experience with general ZK. I see a lot of people very excited by it. And maybe in a way that makes me skeptical, because it seems like a cool toy. But I am open to them working great.

**SPEAKER_02:**
[23:35] And so I don't want to make a strong, firm stance at the moment on them, but they would be great if they work. Yeah, it seems like the approach to Kieran's point is: find specific areas where you can create circuits and apply them and optimize for those, and then expand that over time. You know, like, it's really about kind of

**SPEAKER_03:**
[23:54] nailing those initial use cases. And that's why I was drawn to that, because if you really narrow it down to something really simple, then I think you can do it well. I've heard that people even maybe compile the specific circuits and then optimize, like you kind of write them with the general tool. Some people do, I don't know. And then you kind of like, like, OK, I got the circuit for the specific thing, but then I got to make it, like, work.

**SPEAKER_02:**
[24:19] Yeah. I think compiling a circuit is still pretty, very computationally intensive, but it's way less. For most circuits, once a circuit is compiled, it's way less to do the proof. You got to continue to push that down, but I think the ratio is very large. Well, I think we are at time.

[24:40] You know, where can we find you, Jim? I'm going to start with you. Where can you find me? Yes. People want to hear more and learn more about Jim, which I, you know—please speak up. Ask Jim where they find you. I do have a Twitter handle. What is my Twitter handle? I can't remember. But probably J—I guess it's Jamsheet, probably. I'm going to try to check. Hold on. Yeah.

[25:05] But whatever it is, you should post more often. OK. I Twitter for years. I like wake up one day and remember that Twitter exists. And then I tweet a lot. And then I forget about it for a couple of weeks. Sorry, it's Jay Hermos. Like J-H-O. I threw it in the chat. I don't know if we can all see that, the studio chat. Yeah. So, yes.

**SPEAKER_03:**
[25:27] You can find him at Jay Hermos. Kieran, where can people find you? Jamshied Hermos. Oh, Jamshied Hermos. Yeah, I'm on X, KJamesLubin. I'm also on Substack, trying to, you know, I have like a couple old Medium posts that I've linked from there. I'm getting a little bit into a Substack rhythm. It'll probably be infrequent, but at least of moderate to high quality. Also KJamesLubin.

[25:51] I think for now, maybe I'll change the URL. Yeah. And link it to me in the show notes when we start assuming we do show notes. And you can find me on X at VicForWong.

**SPEAKER_02:**
[26:06] Bob has posted why—I explained before in my handle. You can also find us on Telegram at the Stroud Mercada group. Just go to our website at stroudmercada.com and that will point you to Telegram. And Bob, where can people find you and what can people expect next week? Don't close it out. Bob, you're the resident Zcash shill. One year from now, Zcash price or market cap or both?

**SPEAKER_00:**
[26:28] I think it will be in the top 10. Top 10. It's been very close. And the primary reason is privacy is a big need and it's solved it, right? It's not some future promise. Like it works right now. There's a mobile app. People are using it. You know, you've got like a 10-year, near 10-year history of privacy.

[26:50] You know, top brainiacs working on this, lots of credibility. So, you know, I think it's great. And then I'm looking forward to smart contracts with that kind of level as well. Just one more thing to mention. I couldn't remember Geordie's project—Zisk.

[27:07] So that was a spinoff group now from Polygon led by Jordi Baylina. And they announced real-time proving of mainnet blocks; that was announced at EthCC this year. So proving a block

[27:22] in seven and a half to 12 seconds. So just under block time. However, it requires 24 very high-powered GPUs or 48 more consumer spec. So you've got a rack. There you go. And Bob, with that prediction, where can we find you? And can you give us a preview of what people can expect next week?

[27:42] Absolutely. Yes. So I'm Bob Summerwill—Summer like the season, W-I-L-L. So on everything with that name. And yes, so next week we will have an early days of Ethereum interview with Christoph Jentz, formerly of

[28:00] of F Dev. So he was hired in September 2014 into that Berlin office, worked on testing, cross-client testing, and then later on Slock.it with their smart locks and the creation of The DAO, which was probably, you know, Ethereum's first killer app until the killing in many different ways, yes.

**SPEAKER_02:**
[28:20] Or you could say birthing, because ETC came out of that. Correct. Right. Okay. Well, that's time. Thank you very much for joining us. And we look forward to seeing you next week. Take care. Thanks, everybody.