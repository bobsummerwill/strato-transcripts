**SPEAKER_00:**
[1.9s] Okay, welcome, everyone .
[1.9s] We have a very special and very timely topic today .
[1.9s] Privacy on chain and the rise of zcash .
[1.9s] And we sort of have a special guest today .
[1.9s] So I'm Victor Wong .
[1.9s] I am founder and chief product officer at blockapps .
[1.9s] I'll get to our normal guests, but today we have .
[1.9s] Jim, do you want to give us a quick intro?

**SPEAKER_01:**
[29.5s] Yeah.

**SPEAKER_02:**
[29.7s] I'm also .
[29.7s] I've known Victor and Kieran for years .
[29.7s] I'm one of the founders of BlockApps and CTO.

**SPEAKER_00:**
[37.5s] And you're here in particularly because I would call you a zcash expert, having written your own zcash client.

**SPEAKER_02:**
[48.0s] Well, I think I'm more aspirational at this point in time .
[48.0s] I mean, the way I learn about things is I try to.

**SPEAKER_01:**
[57.3s] How many more expert people do you think there are on, say, zcash in particular on the planet?

**SPEAKER_02:**
[65.2s] No, the problem that I have is that I was sort of halfway in the learning process last year .
[65.2s] So the way I learned about things is I try to, like, write .
[65.2s] Write a client for it .
[65.2s] So I was doing that, but then we got pulled in different directions .
[65.2s] I got to the point where I had sort of replicated the actual client that could connect .
[65.2s] It would bring the data in .
[65.2s] It would bring the proofs in .
[65.2s] But just about when I was getting to the good parts, that's when .
[65.2s] When we moved on to other things.

**SPEAKER_00:**
[94.1s] Well, I'm gonna put the number.

**SPEAKER_01:**
[97.0s] Answer my own question between like, 10 and 100, maybe 10.

**SPEAKER_00:**
[102.2s] I would say there .
[102.2s] There's definitely less than 20 people who have written their own Zcash clients .
[102.2s] Probably.

**SPEAKER_01:**
[107.9s] Well, yeah, there's probably some core contributors .
[107.9s] I imagine there's more than a handful into zcash .
[107.9s] But, you know, when Jim says non expert, he .
[107.9s] You know, it's like there are .
[107.9s] Let's say, yes, I'll expand the range 5 to 100 people who understand Zcash better on the planet .
[107.9s] Big, big, big range there .
[107.9s] But we're talking about pretty small numbers and absolute terms, so.

**SPEAKER_00:**
[133.1s] Yeah, yes, exactly .
[133.1s] I would say if Jim's not an expert, I don't know what even expert means .
[133.1s] Anyways .
[133.1s] Karen, do you want to do a quick intro of yourself before?

**SPEAKER_01:**
[143.2s] Certainly .
[143.2s] I'm our CEO .
[143.2s] Been on these before .
[143.2s] By the way, Vic, you're letting Jim off the hook, calling him a special guest .
[143.2s] He has to do this all the time now with our, you know, continued in the public press .
[143.2s] So special in the future.

**SPEAKER_00:**
[159.9s] Special today .
[159.9s] Today is special, but it's the first of many.

**SPEAKER_03:**
[164.6s] Let's just say that I was looking through the .
[164.6s] The the prior videos Jim has never appeared on one of our own spaces .
[164.6s] He's only been on early days of.

**SPEAKER_01:**
[177.3s] Okay, there you go.

**SPEAKER_02:**
[179.0s] Oh no, you found out but it.

**SPEAKER_00:**
[181.3s] Won'T be special soon .
[181.3s] Bob, by the way, since you've spoken up, can you do give a quick intro to yourself?

**SPEAKER_03:**
[187.2s] So hi, I'm .
[187.2s] I'm Bob, I'm head of ecosystem and yeah been doing a lot of .
[187.2s] A lot of spaces.

**SPEAKER_00:**
[195.9s] Yeah so I, I think you know to level set because I think there's a lot of misunderstanding about what privacy is.

**SPEAKER_01:**
[206.2s] What.

**SPEAKER_00:**
[206.5s] How would you define blockchain privacy and why do you think it's important?

**SPEAKER_03:**
[211.7s] Who's that a question for?

**SPEAKER_00:**
[213.7s] Could be for anyone .
[213.7s] Whoever wants to go Karen, you want.

**SPEAKER_01:**
[216.4s] To kick us off so and for the .
[216.4s] I assume that the viewer is pretty deep in the space but I'll bring it down to a fairly low technical level .
[216.4s] So blockchains are great .
[216.4s] They let you move digitally scarce value from party to party .
[216.4s] And the way that this is typically done is that you've got a big address which is almost but not quite a public key and you sort of sign a message that says I Kieran, but it's not Kirin because it's this address .
[216.4s] Send three Bitcoin to Bob and it doesn't say Bob .
[216.4s] It's another address you don't quite know either of those parties are .
[216.4s] However you've got the address forever .
[216.4s] And often it is the case that you can piece together what happened based on that address .
[216.4s] So say you're on a centralized Exchange which has KYC'd .
[216.4s] It knows how to associate you to maybe withdrawal address .
[216.4s] It may not know down the line but if you start to get a bunch of data points you can kind of piece together who sent what to whom and you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone and it's not .
[216.4s] While it's a cryptographic technology, it's not necessarily a private technology .
[216.4s] This has been a problem both in the consumer setting just for .
[216.4s] People don't like this .
[216.4s] Satoshi makes a comment, I believe in the white paper saying that obviously to prevent the double spend problem which basically is just that to ensure that Bitcoin can't be created or destroyed except by the agreed mechanism .
[216.4s] Obviously you need to know the whole history and so he sees the problem as intrinsic .
[216.4s] But some technologies come out later that maybe calls that into question that we'll talk about .
[216.4s] It's also an enterprise problem so we can talk separately about our experience there .
[216.4s] Sort of what the enterprises Want is kind of the same as what the public blockchain people want, except with selective visibility .
[216.4s] So they want to say you're doing like a .
[216.4s] On chain stock trade, which is actually now starting to happen .
[216.4s] You sort of want to know the other party has the stock .
[216.4s] You don't necessarily want to know who the other party is, but you want to know that they acquired that stock legitimately .
[216.4s] And then when you get it, you want to be able to pass it on legitimately in the same way .
[216.4s] And then there's sometimes this extra requirement that like, the regulator can see everything, you know, so you, you want sort of like a unlinkability of balance to person or company, but also this mass preservation property that I was talking about can't create or destroy assets .
[216.4s] They have to be acquired legitimately and so on .
[216.4s] So it's a perennial problem and closer to solved and, you know, but we can go into that shortly.

**SPEAKER_00:**
[410.1s] Yeah, Bob, did you want to add anything to that?

**SPEAKER_03:**
[411.9s] Yeah, Yes .
[411.9s] I mean, going back to those Bitcoin, you know, beginnings in the Bitcoin white paper, you know, it, it just talks about severing identity from transactions, but, but really that's just Sudan pseudonymous, you know, not, not anonymous .
[411.9s] And I think a lot of people didn't understand that differentiation back in those early days .
[411.9s] And it's like, oh, bitcoin's private, untrackable, you know, digital money .
[411.9s] But, you know, very rapidly you have blockchain analytics coming in, you know, looking for correlations and patterns .
[411.9s] And it's like, yeah, that's .
[411.9s] You're not getting a lot of security, you know, even if you're not reusing addresses, just, just sort of normal things that people would do .
[411.9s] There's, there's lots of correlations and you know, you can get unmasked that way .
[411.9s] But yeah, Satoshi did talk a bit about zero knowledge .
[411.9s] I can't remember who raised it .
[411.9s] Somebody raised it early and, and he was like, yeah, you know, that would be interesting if we could do that .
[411.9s] But, but it was just like a lot of that cryptography, you know, just didn't, hadn't happened, you know, so Zcash started in 2016, and it was only around that kind of time or a little before that you started having, you know, these, these papers on, on Snark Constructions and going through all these different kind of rounds .
[411.9s] So, yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path .
[411.9s] You know, they are an immutable public ledger forever .
[411.9s] Ethereum .
[411.9s] Even worse because it's an account model .
[411.9s] So you're, you are reusing the addresses all the time, right ?
[411.9s] And if your address is unmasked, you are forever doxxed .
[411.9s] That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars and out of a known address of his, which probably not desired.

**SPEAKER_00:**
[545.4s] And you guys have been talking about Satoshi, but Jim, I remember, I think it's like early at like 2014, Vitalik was talking like, he was like, ZK, Snark will fix all of this at some point in time .
[545.4s] Do you remember that?

**SPEAKER_02:**
[560.2s] Well, I mean, like, I think we went through a learning process about privacy .
[560.2s] And that's sort of like we're understating this right now .
[560.2s] Maybe it's because we put a lot of time and effort into some privacy solutions that technically worked but were a business failure, I think is fair to say .
[560.2s] And so the audience can learn from our failed mistakes in the past right now .
[560.2s] But we sort of built .
[560.2s] So we had heard years ago about zk, but we sort of just, I don't know, at the time, looked into it and said like, oh, this looks like overly complicated .
[560.2s] You can get privacy through these other means .
[560.2s] And we ended up building a system that, that allowed for sort of like quick spin up of, of private chains that everything was sort of like in a, an encrypted tunnel .
[560.2s] And you could, you could have like these chains completely secure .
[560.2s] Nobody else would see what was happening there .
[560.2s] But, but long story short, you know, slow learning process, we, we found out that customers want everything .
[560.2s] And to the point that it made it worthless, we would go into enterprise .
[560.2s] We would say, oh, you can set up these private channels with others .
[560.2s] And they love that because they could sort of control that and they could control who goes in there .
[560.2s] But then once everything was going through these private channels, then they wanted to be able to transfer from private chain to private chain .
[560.2s] And that's where everything started to fall apart .
[560.2s] Getting things back onto the main chain became sort of this extra complicated system .
[560.2s] And at the same time, customers wanted to have full flexibility in having extensions to solidity where you could just name a chain and send some money from chain A to chain B .
[560.2s] And really the only way to make that stuff work is you have to go back to zk .
[560.2s] So ZK is overly complicated, but it is necessary .
[560.2s] And so we started looking at that again .
[560.2s] But I think the safe thing to do is start with a proven technology .
[560.2s] And zcash had been around for years and nobody had stolen money .
[560.2s] And this is just sort of like a subset of zk, but it's kind of a cool thing .
[560.2s] You can build what they call tumblers of money, throw a bunch of money in and then the money that you put into the tumbler is, you know how much went in but, but the ownership is completely scrambled up and at any time you can go and transfer money from within the tumbler from one user to another, but only the users who did the transferring and got the money know what was there, but nobody else can see what's happening .
[560.2s] So again like you have these systems of multiple users with lots of money, but you don't know who owns a percentage of the money.

**SPEAKER_00:**
[745.4s] Yeah .
[745.4s] Actually before we even go that far, can we talk just like what is ZK and how does it work and why is it an important part of the solution?

**SPEAKER_01:**
[753.8s] I want to pull back for also a second .
[753.8s] I remember, I think there was an Ethereum meetup in New York .
[753.8s] I'm not sure if either of you guys were there .
[753.8s] I think I spoke at it maybe and there was also a zcash I think presentation there .
[753.8s] And it was at that time taking seven minutes to generate the ZK proofs .
[753.8s] So you wanted to make a transaction you'd like, did this thing, it took seven minutes and then the verification was kind of fast .
[753.8s] Once you had it and you sent it to the network, things could go on .
[753.8s] But the usability was not there in those days .
[753.8s] This is part of the reason we weren't gonna tell our enterprise customers like oh yeah, let's, let's ZK everything .
[753.8s] You know, even if we had it all integrated nicely, there's a lot of devil in the details and it was unbelievably slow for a while and I think it's fixed.

**SPEAKER_00:**
[807.2s] But yeah, well, it's complicated.

**SPEAKER_01:**
[809.9s] I mean this is what I was.

**SPEAKER_02:**
[810.8s] Trying to say before is like I have like sort of nuts and bolts experience of what's going on in zcash .
[810.8s] But the more complicated world of zero knowledge, that's my aspirational part right now .
[810.8s] I can sort of see pieces moving within there but, but would hesitate to speak more broadly on this except let's say that, that, that it is more complicated than any of the like for instance, Ethereum client implementation stuff that we were doing back in the day.

**SPEAKER_00:**
[844.3s] Yeah, yeah .
[844.3s] It can get pretty high level summary of what zero knowledge is like .
[844.3s] I think very few people understand.

**SPEAKER_01:**
[850.8s] I, I, I have a good layman example .
[850.8s] Okay .
[850.8s] I think and Jim can correct me .
[850.8s] So I, I did want to take a theoretical cryptography class and the example they bring up is the CEO problem, so to speak .
[850.8s] So you've got two CEOs and they're high ego guys, you know, and they want to know do you stand up.

**SPEAKER_00:**
[873.8s] From experience, Kieran, or.

**SPEAKER_01:**
[875.2s] Yeah, I'm not speaking about myself .
[875.2s] They want to know who has the most between the two, but they don't want to know how much money, they merely want to know which one has more .
[875.2s] And you would think that there wouldn't really be a way to create a scheme in which they could learn that information and nothing else .
[875.2s] But there actually is .
[875.2s] Again, this is almost 10 years ago now, so I may be describing the example incorrectly, but yeah, that's like a case where you might want zero knowledge .
[875.2s] Similarly, like an ID check at a bar, you're leaking all your personal info when you hand the ID to the bouncer, to your home address, your full name, your date of birth, etc .
[875.2s] So you may want to prove to the bar that you're over 21 without handing any other info over .
[875.2s] Basically I think this is the general setting that it ends up at .
[875.2s] Jim .
[875.2s] Do I .
[875.2s] You want to take that and run with it ?
[875.2s] Correct it?

**SPEAKER_00:**
[946.3s] Yeah.

**SPEAKER_02:**
[946.8s] So this is when you first look up zero knowledge .
[946.8s] There are lots of little examples like this that are all pretty cool .
[946.8s] And what's really happening in zcash is that what you're trying to do is pass money from person A to person B .
[946.8s] And person A wants to prove to person B that they have the money and that it was actually transferred, but without giving away the amount of money that person A has .
[946.8s] Or without person A learning how much that person B has .
[946.8s] Just that you know, that the state before was that you had the amount and that the state after is that it was transferred over .
[946.8s] And then also no one else in the world can know this .
[946.8s] So you're proving sort of the important parts but not others .
[946.8s] But zero knowledge could get pretty complicated too because when you start looking into it, there are a lot of one off examples like you're talking about that you can sort of see a solution to .
[946.8s] But the problem comes about in trying to come up with sort of a generic solution where you can almost just compile any amount of code into some ZK proof and then run that for anything .
[946.8s] I don't remember because it's been about a year now, but, but in Zero cash there were multiple, multiple zero knowledge proofs in there for various aspects .
[946.8s] If I, you know, I might be making up some of the details here, but I think there was like one proof was like to show that you had more than such and such money before the transfer .
[946.8s] I might have it slightly off, but there were multiple of these zero knowledge algorithms in there .
[946.8s] But put together they allowed for the, for the full sort of transfer of money within the tumbler .
[946.8s] And each one sort of had been worked out independently of each other using a more generic system where they compiled certain algorithms in there, let me add .
[946.8s] So making it generic can get really.

**SPEAKER_01:**
[1061.7s] Complicated terminology for the listener that you heard that I barely remember .
[1061.7s] So snarks and Starks were a thing that Vitalik was talking about a lot and still does .
[1061.7s] So it's like succinct, non interactive arbitrary something computation .
[1061.7s] I can't remember.

**SPEAKER_03:**
[1084.4s] Like but basically interactive proof.

**SPEAKER_01:**
[1087.6s] Yes, but what's the whole acronym ?
[1087.6s] But so there is a way I think to take an arbitrary computation and to prove that it has a certain result without revealing like the intermediate states and so on .
[1087.6s] But it's not computationally feasible .
[1087.6s] Like or it's just so slow that if you try to do it that way it becomes very difficult .
[1087.6s] So I believe just, just tying back to Jim's point, like you could try to do this in a generality .
[1087.6s] Like I can verify like the evm .
[1087.6s] Like I can verify there are these zkevms like I verify any computation that comes out of this thing .
[1087.6s] And I think the problem with them has been performance .
[1087.6s] And so the zcash people, I guess had to decompose every little step into specific circuits .
[1087.6s] Right .
[1087.6s] Like or .
[1087.6s] Yeah, it's very, very low level programming thinking in the ZK world .
[1087.6s] Like literally they're circuits that you end up compiling and so on and so forth.

**SPEAKER_03:**
[1153.2s] So yeah, zcash at the moment is onto it.

**SPEAKER_01:**
[1155.3s] Yeah.

**SPEAKER_02:**
[1155.8s] And sort of by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one Tumblr problem without going any more in depth than that .
[1155.8s] So this isn't like in the dream world .
[1155.8s] You would take any Ethereum contract and compile it somehow as a something zero knowledge and then prove that, that you had run the, the full contract .
[1155.8s] That's something that at the time, at least so far in the world as it is, I, I didn't want to get into it or have us get into it as a company, but just to have these tumblers in place, I think that solves a lot of.

**SPEAKER_00:**
[1196.1s] Yeah, Bob, you were saying something.

**SPEAKER_03:**
[1198.0s] Yeah .
[1198.0s] So zcash is onto its fourth round of different cryptography .
[1198.0s] So I forget what they're called sapling something else or onto Orchard now .
[1198.0s] But I mean that's been now over the course of nearly a decade .
[1198.0s] You know, each time you've got another sort of two years worth of leading edge advancement and yeah like talking about that performance thing .
[1198.0s] So something which I think has been a key piece in zcash price appreciation recently has been the arrival of a functional mobile wallet .
[1198.0s] So that's called Zashi, which is made by the electric coin company .
[1198.0s] But you're basically at the point where you can run that proof on your phone .
[1198.0s] So something which used to be laptop 7 minutes is now phone second .
[1198.0s] So what you've seen if you look at the size of these shielding pools, where these pools are effectively like, you know, all of these things are all, you know, mixed and hidden together .
[1198.0s] Right .
[1198.0s] The, the more that you've got in a pool, the more you know, the more unlinkable you are if you have a, you know, if you do something simple like ring signatures where you just whatever .
[1198.0s] I think Monero's got 16 transactions that get all joined together .
[1198.0s] So you can trace through that to a degree .
[1198.0s] But if you've got hundreds or thousands or millions of people in that same pool, it's effectively completely anonymous at that point .
[1198.0s] But if you look at the stats of usage of these particular pools, are you seeing what proportion of the money supply has been shielded versus being transparent ?
[1198.0s] I guess that's another thing to say, right ?
[1198.0s] Is, is Bitcoin is transparent, you know, so same, same with Ethereum .
[1198.0s] But then they, they, they use the world word shielded to talk about, you know, that you are within this anonymity set .
[1198.0s] So these earlier rounds, you know, you had a bit of use but not a ton of use .
[1198.0s] But right now I can't find the view .
[1198.0s] But it, but it was something like about 4 or 5 million of the 21 million were within that shielding pool .
[1198.0s] So you know, a significant chunk of it is shielded now which was never the case in the past .
[1198.0s] You know I remember on etc at some point we were looking at whether we were going to bring over the pre compiles to do with some of the curves .
[1198.0s] I don't know if you remember that happened in Ethereum at some point .
[1198.0s] One of the Blake curves I think went into the pre compile and we were talking about whether we were going to do that or not .
[1198.0s] And really talking about gas limit as well .
[1198.0s] How gas expensive would operations be using these things even ?
[1198.0s] And the stats at that time were it's like maybe 2% of transactions on Zcash were shielded, something like that .
[1198.0s] It's basically not being used at all functionally .
[1198.0s] Pretty much identical to Bitcoin but Probably a lot of end users going, yeah, I'm using zcash, I'm private .
[1198.0s] It's like, yeah, you're not at all .
[1198.0s] You are getting zero benefit at all .
[1198.0s] But yeah, that's really happening now .
[1198.0s] And I think it's just these rounds and rounds and years and years of research and then implementation of those .
[1198.0s] An engineering effort and it's like, hey, it works now.

**SPEAKER_00:**
[1436.7s] Well, from your standpoint, Jim, like, is it a technological advancement that zcash has created or is it just simply that these tumblers have gotten big enough that they offer real privacy ?
[1436.7s] Do you know what I mean?

**SPEAKER_02:**
[1453.9s] It's, I mean any of these things are technological advancements, but I mean, you want to have the tumblers big enough so that, that you have some amount of anonymity within there .
[1453.9s] If it's a tumbler of one person, then it's not much of a Tumblr.

**SPEAKER_01:**
[1473.1s] I need to interject .
[1473.1s] I have a crypto friend who was, was texting about 30 seconds ago about whether I like Zcash at this price .
[1473.1s] This is a pre recorded podcast .
[1473.1s] So, you know, well, I guess it'll run on Wednesday, November 12, but very timely .
[1473.1s] You know, I think it's sort of like again, this is the old crypto joke where like when your dentist and realtor friends start asking you about Ripple and Cardano, time to unwind your positions a little bit .
[1473.1s] You know, it's the zcash meta .
[1473.1s] I don't know, like, maybe that means there's room to run, maybe, maybe it's tops.

**SPEAKER_00:**
[1512.7s] But, well, as they say, it's like catching a falling knife, right ?
[1512.7s] Like, you know, trying to figure out the, the peak of the market .
[1512.7s] I, I, okay, like we've talked about kind of how zcash works and it uses ZK in these sort of very specific areas and it's not, you know, programmable generally .
[1512.7s] Now obviously there's a lot of talk in the ethereum world about ZKEVMs .
[1512.7s] Do you guys have any thoughts on that ?
[1512.7s] And like, you know how those work ?
[1512.7s] Because, you know, at what point do we get like, is it truly impossible to get full programmability ?
[1512.7s] Or do you know, is that something.

**SPEAKER_01:**
[1554.4s] That is just getting closer from a market perspective ?
[1554.4s] I think they're mostly ZKAVMs have been used for scaling as opposed to privacy .
[1554.4s] Even there you tend to see some amount of specificity .
[1554.4s] Like I think I mentioned on a podcast before, I'm, you know, friend acquaintances with the lighter CEO and lighter uses .
[1554.4s] Lighter is like the L2 version of hyper liquid, if you will, or where they do perps and they do zero knowledge matching off chain but you know, it actually works and it gets written to Ethereum which is pretty cool and supposedly they're achieving really high throughputs this way .
[1554.4s] It's not necessarily privacy tech at all .
[1554.4s] I ran into some of the Aztec folks in Singapore that seems trending .
[1554.4s] General purpose still on testnet but not full evm .
[1554.4s] It's like a restricted UTXO type language of sorts I believe .
[1554.4s] I think there's probably not being nearly as expert as Jim, who I'll defer to in a second not being an expert .
[1554.4s] I think it will be .
[1554.4s] There's no intrinsic reason you can't make it full EVM or full Rust or JavaScript or whatever .
[1554.4s] But probably there will be a tremendous amount of optimization that would have to happen to make that happen .
[1554.4s] So you probably see special purpose for a while.

**SPEAKER_03:**
[1648.1s] I saw that and now I'm blanking on the name .
[1648.1s] The ZK tech that was happening under the Polygon banner with Jordi Balina and I can't remember the name of the project now they posted within the last few months that they were real time ZK proving Mainnet now but you know, it was with a battery of GPUs .
[1648.1s] It was not a thing that you would be doing yourself .
[1648.1s] But yeah, that full proving is, you know, is possible, possible .
[1648.1s] But yeah, you, you, you have that optimization to, to be done .
[1648.1s] But I mean I think, I think that's where things are going to end up that you've had this sort of improvement where starting at Bitcoin, it's like well how are we going to prove, you know, get to global consensus and, and solve the double spend problem ?
[1648.1s] Well it, it's by publishing all of the details and then we're going to have redundant state machines running in parallel .
[1648.1s] Right .
[1648.1s] And that's the answer .
[1648.1s] We know that works .
[1648.1s] It was like what's Satoshi did the big ugly thing but it worked and it made this stuff possible that had never been possible before, but it is, you know, it's an incredibly big, ugly, expensive way of doing that .
[1648.1s] And then I think just over time it's like okay, well having things public was sort of a requirement for that consensus model .
[1648.1s] But that was never intentional .
[1648.1s] Like having them all as a public ledger like that, that's not a positive feature .
[1648.1s] Now if you look at the cypherpunk culture that many of these people were coming out of, yeah, it's, it's private, unstoppable money .
[1648.1s] Like yeah, no, it wouldn't be public .
[1648.1s] So I Saw that, yeah .
[1648.1s] Within weeks of bitcoin starting, Hal Finney said, you know, looking at ways of improving anonymity in bitcoin .
[1648.1s] So that was January 2009 .
[1648.1s] You know, that was a cypherpunk's obvious first reaction is, yeah, this is cool now, but yeah, we should have privacy as well .
[1648.1s] And I think we're sort of getting to that point of the tech has become good enough to, to solve that without broadcasting everything to everyone.

**SPEAKER_00:**
[1809.3s] Yeah .
[1809.3s] Jim, what, what do you think, like, you know, on the sort of general programmability ZK front?

**SPEAKER_02:**
[1816.3s] I wish I had more, you know, hands on experience with general zk .
[1816.3s] I see a lot of people very excited by it and maybe in a way that makes me skeptical because it seems like a cool toy, but I am open to them working great .
[1816.3s] And so I don't want to make a strong, firm stance at the moment on them, but they would be great if they work.

**SPEAKER_00:**
[1848.0s] Yeah .
[1848.0s] It seems like the approach to Karen's point is like find specific areas where you can create circuits and apply them and optimize for those and then expand that over time .
[1848.0s] It's really about nailing those initial use cases.

**SPEAKER_02:**
[1868.5s] And that's why I was drawn to that, because if you really narrow it down to something really simple, then I think you can do it .
[1868.5s] Well.

**SPEAKER_01:**
[1877.7s] I've heard that people even maybe compile the specific circuits and then optimize like you kind of write them with the general tool .
[1877.7s] Some people do, I don't know .
[1877.7s] And then you kind of like, like, okay, I got the circuit for the specific thing, but then I got to make it like work, you know.

**SPEAKER_00:**
[1893.5s] Yeah, I think compiling a circuit is still pretty very like computational intensive .
[1893.5s] But it's way more, but it's way less for most circuits once the circuit is compiled .
[1893.5s] It's way less to do the proof, which is, you know, and you got to continue to push that down, but I think the ratio is very large .
[1893.5s] Okay, well, I think we are at time, you know, where can we find you ?
[1893.5s] Jim, I'm going to start with you.

**SPEAKER_02:**
[1926.0s] Where can you find me?

**SPEAKER_00:**
[1927.5s] Yes, people, I hear more and learn more about Jim, which I, you know, please speak up .
[1927.5s] Ask Jim, where can, where they find you?

**SPEAKER_02:**
[1937.1s] I do have a Twitter handle .
[1937.1s] What is my Twitter handle ?
[1937.1s] I can't remember, but probably J .
[1937.1s] Hermo.

**SPEAKER_00:**
[1942.2s] I guess it's jam .
[1942.2s] She probably try to check.

**SPEAKER_01:**
[1946.1s] Hold on.

**SPEAKER_02:**
[1946.8s] Yeah.

**SPEAKER_00:**
[1949.1s] But whatever it is, you should post more often .
[1949.1s] Okay.

**SPEAKER_02:**
[1952.2s] I, I Twitter .
[1952.2s] I like wake up one day and remember that Twitter exists .
[1952.2s] And then I Twitter, I tweet a lot and then .
[1952.2s] Then I forget about it for a couple.

**SPEAKER_00:**
[1960.8s] Sorry, it's J for months like J.

**SPEAKER_01:**
[1963.1s] H O in the chat .
[1963.1s] I don't know if we can all see that the studio chat.

**SPEAKER_00:**
[1967.7s] But yeah, so .
[1967.7s] So yes, you can find them at J Hermuz.

**SPEAKER_01:**
[1973.9s] Karen, where can people find Hermes?

**SPEAKER_00:**
[1976.4s] Oh, Jamsheed Hermos.

**SPEAKER_01:**
[1977.8s] Yeah, I'm on X Rubin .
[1977.8s] I'm also on substack trying to, you know, I have a couple old medium posts that I've linked from there .
[1977.8s] I'm getting a little bit into a substack rhythm .
[1977.8s] It'll probably be infrequent but at least of moderate to high quality .
[1977.8s] Also kjameslubin Substack I think for now maybe I'll change the URL and link it in the show notes when we start .
[1977.8s] Assuming we do show notes and you.

**SPEAKER_00:**
[2010.4s] Can find me on xicforwang .
[2010.4s] Bob has posted why I explained before in my handle .
[2010.4s] You can also find us on Telegram at the Strom Mercado Group .
[2010.4s] Just go to our website@straumercada.com and that will point you to Telegram .
[2010.4s] And Bob, where can people find you and what can people expect next week?

**SPEAKER_01:**
[2031.8s] Don't close it out, Bob .
[2031.8s] You're the resident zcash shill .
[2031.8s] One year from now, zcash price or market cap or both?

**SPEAKER_03:**
[2040.9s] I think it will be in the top 10.

**SPEAKER_01:**
[2043.8s] Top 10.

**SPEAKER_03:**
[2044.8s] It's been very close and the primary reason is privacy is a big need and it solved it, right ?
[2044.8s] It's not some future promise like it works .
[2044.8s] Right now there's a mobile app, people are using it .
[2044.8s] You know, you've got like a 10 year, near 10 year history of, you know, top brainiacs working on this .
[2044.8s] Lots of credibility .
[2044.8s] So you know, I think it's great and then I'm looking forward to smart contracts with that kind of level as well .
[2044.8s] Just one more thing to mention .
[2044.8s] I couldn't remember Jordy's project Zisk .
[2044.8s] So that was .
[2044.8s] That's a spinoff group now from Polygon led by Jordi Balena and they announced real time proving of mainnet blocks that was announced at FCC this year .
[2044.8s] So proving a block in 7 1/2 to 12 seconds .
[2044.8s] So just under block time .
[2044.8s] However, it requires 24 very high powered GPUs or 48 more consumer spec .
[2044.8s] So you've got a rack.

**SPEAKER_00:**
[2120.9s] There we go .
[2120.9s] And Bob, with that prediction, where can we find you and can you give us a preview of what people can expect next week?

**SPEAKER_03:**
[2128.2s] Absolutely, yes .
[2128.2s] So I'm Bob Summerwill .
[2128.2s] Summer like the season .
[2128.2s] W I L L so on everything with that name .
[2128.2s] And yes .
[2128.2s] So next week we will have an early days of Ethereum interview with Christoph Jens, formerly of .
[2128.2s] Of FDEV, so was hired in September 2014 into that Berlin office, worked on testing, cross client testing and then later on slock it with their smart locks and the creation of the Dao, which was probably, you know, Ethereum's first killer app .
[2128.2s] Until killing.

**SPEAKER_00:**
[2171.5s] Killing in many different ways .
[2171.5s] Yes, by doing that .
[2171.5s] Or you can say birthing because etc came out of that.

**SPEAKER_03:**
[2179.6s] Correct .
[2179.6s] Right.

**SPEAKER_00:**
[2181.6s] Okay .
[2181.6s] Well, that's time .
[2181.6s] Thank you very much for joining us and we look forward to seeing you next week .
[2181.6s] Take care.

**SPEAKER_01:**
[2187.7s] Thanks, everybody.
