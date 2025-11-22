**SPEAKER_00:**
[1.8s] Okay .
[1.8s] Welcome, everyone .
[1.8s] We have a
[5.0s] very special
[6.3s] and very timely
[8.4s] topic today,
[10.2s] privacy
[11.1s] on chain and the rise of Zcash.
[14.4s] And we sort of have a special guest today .
[14.4s] So I'm Victor Wong .
[14.4s] I am founder and
[19.6s] chief product officer at block apps.
[22.4s] I'll get to our normal guest, but, today, we have Jim .
[22.4s] Do you wanna give us a quick intro?

**SPEAKER_01:**
[29.3s] Yeah .
[29.3s] I'm also I've
[31.4s] known Victor and Kieran for years .
[31.4s] I'm one of the founders of block apps
[35.2s] and CTO.

**SPEAKER_00:**
[37.6s] And you're here in particularly
[40.6s] because
[41.7s] I would call you a Zcash expert having written your own Zcash client.

**SPEAKER_01:**
[48.1s] Well, I I I think I'm I'm more aspirational at this point in time .
[48.1s] I mean, the way I learn about things is I try to

**SPEAKER_02:**
[56.9s] What's that ?
[56.9s] More expert people do you think there are on, say, Zcash in particular on the planet?

**SPEAKER_01:**
[65.2s] No .
[65.2s] The problem that I have is that I I was I
[69.5s] was sort of halfway in the learning process last year .
[69.5s] So the way I learned about things is I try to, like, write write a client for it .
[69.5s] So I was I was doing that, but then we got pulled in different directions .
[69.5s] I got to the point where I had sort of replicated the actual client that could connect .
[69.5s] It would bring the
[86.2s] data in .
[86.2s] It would bring the proofs in .
[86.2s] But just about when I was getting to the good parts,
[91.0s] that's when when we moved on to other things.
[94.2s] Well, we're gonna put the number

**SPEAKER_00:**
[97.0s] answer my other question .
[97.0s] Put the number at between, like, 10 and a 100 .
[97.0s] May maybe 10 .
[97.0s] I would say there there's definitely less than 20 people who have written their own Zcash clients, probably .
[97.0s] Well, yeah .
[97.0s] Yeah .
[97.0s] There's probably some core contributors.

**SPEAKER_02:**
[110.5s] I imagine there's more than a handful
[112.9s] into Zcash.
[114.3s] But, you know, when Jim says non expert, he you know, it's like, there are
[120.1s] let's say yes.
[122.0s] I'll I'll expand the range .
[122.0s] Five to a 100 people who understand Zcash better on on the planet .
[122.0s] Big, big, big range there, but we're talking about pretty small numbers in absolute terms .
[122.0s] So Yeah .
[122.0s] Yes .
[122.0s] Exactly .
[122.0s] I say

**SPEAKER_00:**
[135.6s] if Jim's not an expert, I don't know what even expert means .
[135.6s] Anyways,
[139.8s] Karen, do you want to give a quick intro of yourself before we Certainly.

**SPEAKER_02:**
[144.6s] I'm our CEO .
[144.6s] Been on these before .
[144.6s] By the way, Vicky, we're letting Jim off the hook, calling him a special guest .
[144.6s] He has to do this all the time now with our, you know, continued
[155.3s] in the public press .
[155.3s] So Okay.

**SPEAKER_00:**
[158.0s] Special now .
[158.0s] Not special in the future .
[158.0s] Special today .
[158.0s] Today is special, but it's the first of many .
[158.0s] Let's just say that .
[158.0s] I was looking through the the

**SPEAKER_03:**
[167.5s] the prior videos.
[169.6s] Jim has never appeared
[171.5s] on one of our own spaces.
[174.5s] He's only been on early days of the year .
[174.5s] Okay.

**SPEAKER_00:**
[177.8s] Older drinks .
[177.8s] Well, there you go .
[177.8s] Oh, no .
[177.8s] You found out .
[177.8s] But
[181.1s] it won't be special soon .
[181.1s] Bob, by the way, since you've spoken up, can you give that quick intro to yourself ?
[181.1s] So hi .
[181.1s] I'm I'm Bob .
[181.1s] I'm head of ecosystem.

**SPEAKER_03:**
[190.3s] And,
[192.8s] yeah, been doing a lot of a lot of spaces.

**SPEAKER_00:**
[196.0s] Yeah .
[196.0s] So I I think, you know, to level set because I think there's a lot of misunderstanding
[203.3s] about what privacy is.
[206.2s] What how would you define blockchain privacy and why do you think it's important?

**SPEAKER_03:**
[211.7s] Who's that question for?

**SPEAKER_00:**
[213.7s] Could be for anyone .
[213.7s] Whoever wants to go .
[213.7s] Karen, you want us to kick us off ?
[213.7s] Okay .
[213.7s] I'll take it .
[213.7s] So

**SPEAKER_02:**
[219.9s] and for
[221.5s] the I assume that the viewer is pretty deep in the space, but I'll I'll I'll bring it down to a fairly low technical level .
[221.5s] So blockchains are great.
[231.4s] They let you move
[233.4s] digitally scarce value from party to party.
[237.1s] And
[238.3s] the
[240.1s] way that this is typically done is that you've got a big address,
[244.6s] which is almost, but not quite a public key,
[248.1s] and
[249.1s] you sort of sign a message that says, I, Kiran, but it's not Kiran because it's this address,
[254.5s] send, you know, 3 Bitcoin to
[257.1s] Bob, and it doesn't say Bob .
[257.1s] It's another address .
[257.1s] You don't quite know who either of those parties are .
[257.1s] However, you've got the address forever,
[265.3s] and
[266.2s] often it is the case that you can piece together
[269.4s] what happened based on that address .
[269.4s] Let's say you're on a centralized
[273.9s] exchange, which has KYC'd.
[275.9s] It knows
[277.3s] how to associate you to maybe
[280.4s] a withdrawal address.
[282.0s] It may not know down the line,
[285.0s] but if you start to get a bunch of data points, can kind of piece together
[289.7s] who
[290.5s] sent what to whom, and you're actually in an extremely transparent
[295.8s] scenario where everyone's financial
[298.3s] transactions are visible to everyone.
[300.4s] And it's not while it's a cryptographic technology, it's not necessarily a private technology.
[305.9s] And
[306.9s] this has been a problem both in the consumer setting just for you know, people don't like this.
[313.6s] Satoshi makes a comment, I believe, in the white paper saying that,
[318.4s] you know, obviously,
[319.8s] to prevent
[321.1s] the double spend problem, which basically just is just that
[325.4s] to ensure that it can't I mean, can't be created or destroyed except by the
[330.8s] agreed mechanism.
[333.2s] Obviously, you need to know the whole history .
[333.2s] And so he sees the problem as intrinsic,
[337.4s] but some technologies come out later that
[340.2s] maybe calls that into question that that we'll, talk about .
[340.2s] It's also an enterprise problem .
[340.2s] So we can we can talk separately about our experience there .
[340.2s] Sort of what the enterprises want
[352.2s] is
[353.4s] kind of the same as what the public blockchain people want
[357.6s] except with selective visibility.
[359.6s] So they wanna say you're doing, like, a on chain stock stock trade, which is actually now starting to happen.
[366.0s] You sorta wanna know the other party has the stock.
[369.0s] You don't necessarily wanna know who the other party is,
[374.7s] but you you wanna know that they acquired that stock legitimately.
[378.5s] And then when you get it, you wanna be able to pass it on legitimately in the same way .
[378.5s] And then there's sometimes this extra requirement that, like, the regulator can see everything .
[378.5s] You know ?
[378.5s] So you you want sort of, like, a unlinkability of balance to person or company,
[393.6s] but also this mass preservation property that I was talking about can't create or destroy assets .
[393.6s] They have to be acquired
[400.3s] legitimately
[402.3s] and and so on .
[402.3s] So it's a perennial problem and closer to solved, you know, but we we can go into that shortly .
[402.3s] Yeah .
[402.3s] Bob, did you wanna add anything to that?

**SPEAKER_03:**
[413.0s] Yeah .
[413.0s] So, I mean, going back to those Bitcoin, you know, beginnings
[416.5s] in the Bitcoin white paper,
[418.5s] you know, it it it just talks about severing identity
[422.6s] from transactions.
[425.9s] But but really, that's just
[428.7s] pseudo
[429.7s] pseudonymous,
[430.6s] you know, not not anonymous.
[432.9s] And I think a lot of people didn't understand that
[436.5s] differentiation back in those early days, and it's like, oh, Bitcoin's private, untrackable,
[442.7s] you know, digital money.
[446.7s] But, you know, very rapidly, you have blockchain analytics
[449.8s] coming in,
[451.3s] you know, looking for correlations and patterns and it's like, yeah,
[455.5s] that's
[456.6s] you're not getting a lot of security,
[458.8s] you know, even if you're not reusing addresses, just just normal things that people would do .
[458.8s] There's there's lots of correlations and, you know, you can get unmasked that way.
[468.9s] But, yeah, Satoshi did talk a bit about zero knowledge.
[473.1s] I
[474.5s] can't remember who raised it .
[474.5s] Somebody raised it early,
[477.6s] and
[479.1s] and he was like, yeah .
[479.1s] You know, that would be interesting if we could do that.
[483.0s] But but it was just
[485.0s] like a lot of that
[486.9s] cryptography,
[487.9s] you know, just didn't hadn't happened.
[490.7s] You know ?
[490.7s] So Zcash
[492.1s] started in 2016
[494.4s] and it was only around that kind of time or a little before that you started having,
[499.1s] you know, these these papers on
[501.6s] on stock constructions
[503.4s] and
[504.7s] going through all these different kind of rounds.
[507.4s] So, yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path.
[514.0s] You know, they are in a mutable public ledger forever.
[518.8s] Ethereum even worse because it's an account model.
[522.3s] So you're you are reusing the addresses all the time .
[522.3s] Right ?
[522.3s] And
[526.9s] if your address is unmasked, you are forever doxed.
[530.4s] That's happened to
[532.3s] at least one of the ethereum founders who moved hundreds of millions of dollars
[537.1s] out of a known address of his, which is
[541.8s] probably not desired.

**SPEAKER_00:**
[544.6s] Well
[545.4s] and I I you know, you guys have been talking about Satoshi .
[545.4s] But, Jim, I remember
[549.5s] I think it's, like, earlier at, like, 2014.
[552.7s] Vitalik was talking like he was like, z k snark will fix all of this at some point in time .
[552.7s] Do you remember that at all ?
[552.7s] Well,

**SPEAKER_01:**
[560.9s] I mean, like, I think we went through a learning process about privacy, and and and that's sort of, like, we're we're understating this right now .
[560.9s] May maybe it's because we put a lot of time and effort into some privacy solutions that
[574.7s] technically worked,
[576.3s] but were a business failure, I think, is fair to say .
[576.3s] And, so so, you know, the audience can learn from our our, like, sort of failed mistakes in the past right now .
[576.3s] But, we sort of
[589.1s] built so we had heard years ago
[592.2s] of about CK, but we sort of just I I don't know .
[592.2s] At the time, into it and said, like, oh, this looks like overly complicated .
[592.2s] You can get privacy through these other means.
[601.6s] And we ended up building a system that that allowed for sort of, like, quick spin up of
[609.6s] private chains that everything was sort of, like, in a an encrypted tunnel, and you could you could have, like,
[616.9s] these
[618.5s] chains
[619.7s] completely secure .
[619.7s] Nobody else would see what was happening there .
[619.7s] But but long story short, you know, slow learning process.
[626.4s] We we found out that customers
[629.8s] want
[631.4s] everything
[632.5s] and
[633.4s] and
[634.3s] to the point that it made it worthless .
[634.3s] Like, they we would go into enterprise .
[634.3s] We would say, like, oh, you can set up these private channels with others .
[634.3s] And they love that because they could sort of control that, and they could control who goes in there .
[634.3s] But then once everything was going through these private channels, then they wanted to be able to, like, transfer from private chain to private chain, and that's where everything started to fall apart .
[634.3s] And
[657.4s] getting things back onto the main chain became sort of this extra
[662.1s] complicated
[663.0s] system.
[664.3s] And
[665.3s] and
[666.2s] at the same time, customers
[668.4s] wanted to have, like,
[670.9s] full flexibility
[672.4s] in having, like, extensions
[674.9s] to,
[676.4s] solidity where where you could just, like, name a chain and send some money from chain a to chain b .
[676.4s] And, really, the only way to make that stuff work is you have to go back to z k .
[676.4s] So z k is
[686.7s] overly complicated,
[688.0s] but it is necessary.
[689.8s] And
[690.9s] and
[692.6s] so so
[694.6s] we started looking at that again,
[697.3s] but I think, like, the safe thing to do is start with a a proven technology .
[697.3s] And Zcash had been around for years and and nobody had stolen money .
[697.3s] And this is just sort of like a subset of of ZK, but it's it's it's kind of a cool thing .
[697.3s] You can you can build what they call tumblers of money .
[697.3s] You throw a bunch of money in,
[715.2s] and then the money that you put into the tumbler
[719.0s] is
[720.4s] you know how much went in, but but the ownership is completely scrambled up .
[720.4s] And at any time, you can go and and transfer money from within the tumbler from one user to another, But only the users who did the transferring and got the money know
[734.6s] what was there, but nobody else can see what's happening .
[734.6s] So, again, like, you have these systems of multiple users
[740.8s] with lots of money, but you don't know who owns percentage of of the money.

**SPEAKER_00:**
[745.5s] Yeah .
[745.5s] Actually, before we even go that far, can we talk just, like, what is ZK and how does it work, and why is it an important part of the solution ?
[745.5s] I I wanna pull back for also a a second.

**SPEAKER_02:**
[757.6s] I remember I think there was an Ethereum meetup in New York .
[757.6s] I'm not sure if either of guy you guys were there .
[757.6s] I think I spoke at it, maybe.
[765.9s] And
[768.3s] there was also a Zcash,
[770.1s] I think, presentation
[771.7s] there .
[771.7s] And
[773.4s] it was, at that time, taking seven minutes to generate
[777.2s] the ZK proofs .
[777.2s] So Yes .
[777.2s] Yeah .
[777.2s] Wanted to make a transaction .
[777.2s] You'd like, did this thing .
[777.2s] It took seven minutes, and then the verification was kinda fast .
[777.2s] Once you had it and you sent it to the network, things could go on, you know, but the
[791.3s] the usability was not there in those days .
[791.3s] This is part of the reason we weren't, like, gonna tell our enterprise customers, like, oh, yeah .
[791.3s] Let's let's z k everything .
[791.3s] You know, even if we had it all integrated nicely,
[802.7s] there's a lot of devil in the details .
[802.7s] I know it was unbelievably

**SPEAKER_01:**
[805.7s] slow for a while, and I think it's fixed .
[805.7s] But Yeah .
[805.7s] I know .
[805.7s] Well, it's complicated .
[805.7s] I mean, this is what I was trying to to say before .
[805.7s] It's like, have, like, sort of nuts and bolts experience of what's going on in Zcash.
[817.6s] But the more complicated world of zero knowledge,
[821.3s] that that's my aspirational
[823.5s] part right now .
[823.5s] I can sort of see pieces moving within there, but but
[829.4s] would hesitate to speak more broadly
[832.2s] on this .
[832.2s] Except let's say that that that it is more complicated than any of the, like, for instance, Ethereum

**SPEAKER_00:**
[841.3s] client implementation stuff that we're doing back the day .
[841.3s] Yeah .
[841.3s] Yeah .
[841.3s] Can you give a high level summary of what zero knowledge is ?
[841.3s] Like, I think very few people understand.

**SPEAKER_02:**
[851.0s] I I have a good layman example Okay .
[851.0s] I think, and Jim can correct me .
[851.0s] So I I did want to take a theoretical cryptography class,
[860.2s] and
[861.0s] the example they bring up is the CEO problem, so to speak .
[861.0s] So we got two CEOs,
[866.8s] and they're high ego guys .
[866.8s] You know?
[870.9s] And they wanna know

**SPEAKER_00:**
[873.1s] Do stand up from experience, Karen ?
[873.1s] Or yeah.

**SPEAKER_02:**
[876.5s] Yeah .
[876.5s] Let's think about myself .
[876.5s] They
[879.7s] wanna know who has the most between
[882.3s] the two.
[884.7s] But they don't wanna know how much money .
[884.7s] They merely wanna know
[890.6s] which one has more.
[893.1s] And you would think that there wouldn't really be a way to
[897.2s] create a scheme
[899.1s] in which
[900.4s] they could learn that information and nothing else,
[904.2s] but there actually is.
[906.8s] I and, again, this is, almost ten years ago now, so I may be describing the example incorrectly.
[911.9s] But,
[913.1s] yeah, that's that's like a case where you might want zero knowledge .
[913.1s] Similarly, like, you know, like an ID check-in a bar.
[920.2s] You're leaking all your personal info when you hand the ID
[923.6s] to the bouncer,
[925.0s] your home address, your full name, your date of birth, you know, etcetera .
[925.0s] So you may wanna prove to the bar that you're 21
[933.1s] without handing any other info over,
[936.5s] basically .
[936.5s] I think this is the general setting that that it ends up at .
[936.5s] Jim, do I you wanna
[943.8s] take them, run with it, correct it ?
[943.8s] Yeah.

**SPEAKER_01:**
[946.8s] So this is
[948.3s] when you first look up zero knowledge, there are lots of little examples like this .
[948.3s] They're all pretty cool.
[955.4s] But and and what what's really happening in Zcash is that what you're trying to do is
[961.7s] pass money from person a to person b.
[964.9s] And person a wants to prove to person b that they have the money and that it was actually actually transferred, but without giving away the amount of money that person a has or without
[973.5s] person a learning how much that person b has .
[973.5s] Just that, you know, that the state before was that that you had the amount and that the state after is that it was transferred over .
[973.5s] And then also no one else in the world can can know this .
[973.5s] So you're you're you're proving sort of the important parts, not others.
[990.4s] Zero knowledge could get pretty
[992.5s] complicated too because when when you start looking into it, there are a lot of one off examples, like like you're talking about, that you sort of see a solution to .
[992.5s] But the problem comes about in trying to come up with a sort of a generic solution where you can almost just compile any any amount of code into some z k proof and then and then run that for anything.
[1013.9s] I don't remember because it's been about a year now, but but in zero cash, there were multiple
[1019.5s] multiple zero knowledge proofs in there for various aspects .
[1019.5s] If I were I you know, I'm I'm I might be making up some of the details here, but I think there was, like, one proof was, like, to show that you had more than such and such money before the transfer.
[1032.8s] I I might have it slightly off, but that there were multiple of these zero knowledge
[1038.9s] algorithms in there .
[1038.9s] But
[1041.2s] put together, they allowed for the for the full sort of transfer of of money within the Tumblr.
[1047.6s] And each one sort of had been worked out independently of each other using a more generic
[1053.6s] system where they compiled certain certain algorithms in there .
[1053.6s] Let me Does that make sense ?
[1053.6s] So making a generic can get really complicated.

**SPEAKER_02:**
[1063.1s] Terminology for the list listener that you've heard that I barely remember .
[1063.1s] So snarks and starks
[1070.7s] were a thing that
[1073.3s] Vitalik was talking about a lot and still does .
[1073.3s] So it's like succinct,
[1078.4s] noninteractive,
[1080.7s] arbitrary,
[1081.9s] something
[1083.0s] compute I can't remember .
[1083.0s] Like but basically interactive proof.
[1087.6s] Yes .
[1087.6s] But what's the whole acronym ?
[1087.6s] But so there is a way, I think, to take an arbitrary computation
[1094.3s] and
[1095.2s] to prove that it has a certain result without revealing,
[1098.5s] like, the intermediate
[1100.6s] states and so on.
[1102.8s] But it's not computationally feasible.
[1105.5s] Like or it's it's just so slow
[1107.8s] that if you try to do it that way,
[1110.4s] it
[1111.5s] becomes very difficult.
[1113.3s] So I believe
[1114.6s] just just tying back to Jim's point .
[1114.6s] Like, you could try to do this in a generality .
[1114.6s] Like, I can like, the EVM .
[1114.6s] Like, I can verify there is z k EVMs .
[1114.6s] Like, I can verify any computation that comes out of this thing .
[1114.6s] And I think the problem with them has been performance.
[1128.2s] And so the Zcash people, I guess, had to decompose
[1132.7s] every little step
[1134.2s] into specific
[1136.8s] z circuits .
[1136.8s] Right ?
[1136.8s] Like or Yeah .
[1136.8s] Yeah.
[1141.8s] So, yeah, it's very, very low level programming thinking in the the ZK world .
[1141.8s] Like, literally, there's there's circuits that you end up compiling and and and so on and so forth.

**SPEAKER_01:**
[1153.2s] So, yeah, Zcash at the moment is onto it today .
[1153.2s] And and sort of by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one Tumblr problem without going any more in-depth than that .
[1153.2s] So this isn't like like, in the dream world, you would take any, like, Ethereum contract and pilot somehow as a as a, you know, something zero knowledge and then prove that that that
[1179.3s] you had run the the full contract.
[1182.0s] That's something that,
[1184.7s] at the time, at at least so far in the the world as it is, I I didn't wanna get into it or or have us get into the company .
[1184.7s] But just to have these tumblers in place, I think that solves a lot of

**SPEAKER_03:**
[1196.1s] Yeah .
[1196.1s] Bob, you were saying something ?
[1196.1s] Yeah .
[1196.1s] So Zcash is onto its fourth round of different cryptography.
[1203.9s] So I forget what they're called, sapling something else .
[1203.9s] We're onto Orchard now.
[1209.5s] But but, I mean, that's been now over the course of nearly a decade.
[1214.9s] You know, each time you've got another sort of two years worth of
[1218.7s] leading edge advancement.
[1222.0s] And
[1223.7s] and, yeah, like, talking about that performance thing .
[1223.7s] So it's something
[1227.8s] which I think has been a
[1229.6s] a key piece in in Zcash price appreciation
[1233.1s] recently
[1234.2s] has been
[1235.6s] the arrival of a functional mobile wallet.
[1239.2s] So that's called Zashi, which is made by the
[1243.9s] electric coin company.
[1245.5s] But you're basically at the point where you can run that proof on your phone.
[1250.3s] So something which used to be laptop
[1252.8s] seven minutes
[1254.2s] is now phone
[1256.3s] second.
[1259.0s] So
[1260.3s] what you've seen, if you look at the size of these
[1263.7s] shielding pools
[1265.4s] where these pools are effectively like, you know, all of these things are all,
[1270.1s] you know, mixed and hidden together .
[1270.1s] Right ?
[1270.1s] The the more that you've got in a pool, the more,
[1275.7s] you know, and and the more unlinkable you are .
[1275.7s] If you have a you know, if you if you do something simple like ring signatures where you just
[1283.9s] whatever sick I think, Monero has got 16 transactions
[1287.3s] that that, you know, get all joined together .
[1287.3s] So
[1291.8s] you can
[1293.2s] trace through that
[1296.1s] to a degree.
[1297.4s] But if you've got, you know, hundreds or thousands or millions
[1302.1s] of people in that same pool, you know, it's it's effectively,
[1306.4s] you know, completely
[1308.3s] anonymous at that point .
[1308.3s] But if you look at the stats of usage
[1313.3s] of these particular pools,
[1315.9s] are you seeing what proportion of the money supply
[1319.5s] has been shielded versus being transparent?
[1323.1s] I guess that's just another thing to say, right, is is Bitcoin is transparent,
[1327.6s] you know, so
[1329.2s] same same with Ethereum,
[1331.2s] but then they they they use the world word shielded to talk about, you know, that you are within this
[1337.6s] anonymity set.
[1339.6s] So these earlier rounds, you know, you had a bit of use, but not a ton of use.
[1345.9s] But right now,
[1349.1s] I can't find the view, but it but it was something like about four or 5,000,000
[1354.4s] of the 21,000,000
[1356.2s] were within that shielding pool .
[1356.2s] So, you know, a significant chunk
[1360.8s] of it is shielded now,
[1363.2s] which was never the case in the past .
[1363.2s] You know?
[1366.6s] I remember on ETC at some point, we were looking at whether we were gonna bring over the precompiles to do with some of the curves .
[1366.6s] You know ?
[1366.6s] I don't know if you remember that happened in Ethereum at some point, but one of the like curves, I think, went into the precompile.
[1381.5s] And we were talking about whether we were gonna, like, do that or not.
[1386.3s] And really, talking
[1387.9s] about gas limit as well, you know, like, how how gas expensive would operations be using these things even.
[1395.1s] And the stats at that time were, you know, it's like maybe
[1398.2s] 2% of transactions
[1399.9s] on the cash were shielded, something like that.
[1402.7s] You know, it's basically,
[1404.2s] like, not being used at all,
[1407.0s] you know, functionally pretty much identical
[1409.4s] to Bitcoin.
[1410.8s] But probably a lot of venues is going, yeah, I'm using Zcash .
[1410.8s] I'm private .
[1410.8s] It's like, yeah, you know, you cannot not at all .
[1410.8s] It's you're getting zero benefit at all.
[1421.5s] But, yeah, that's that's really happening now .
[1421.5s] And I think it's just, you know, these rounds and rounds of years and years of research
[1428.6s] and then implementation of those and engineering effort, and it's like,
[1433.0s] hey .
[1433.0s] It works now.

**SPEAKER_00:**
[1436.7s] Well, I just curious from from your standpoint, Jim, like, is it a technological
[1441.8s] advancement that has created, or is it just simply that these tumblers have gotten big enough that they offer
[1448.5s] real privacy?
[1450.0s] Do you know what I mean?

**SPEAKER_01:**
[1453.9s] It's I mean, any of these things are technological advancements.
[1458.9s] But, I mean, you wanna have the tumblers big enough so that that you have
[1464.7s] some amount of anonymity within there .
[1464.7s] It's not like if it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_02:**
[1473.1s] I I need to interject .
[1473.1s] I I have a crypto friend who was texting
[1478.6s] about thirty seconds ago about whether I like CCash at this price.
[1483.0s] This is a prerecorded podcast .
[1483.0s] So, you know, well, I guess it'll it'll run, on Wednesday,
[1489.3s] November 12.
[1491.1s] But,
[1491.9s] very timely, you know, I think.
[1494.4s] It's sort of like I again, there's there's the old crypto joke where, like, when your dentist and realtor friends start asking you about Ripple and Cardano, it's time to unwind your positions a little bit .
[1494.4s] You know ?
[1494.4s] But it's the Zcash meta .
[1494.4s] I don't know .
[1494.4s] Like, maybe that means there's room to run .
[1494.4s] Like, maybe maybe
[1511.5s] it's tops.

**SPEAKER_00:**
[1512.8s] But
[1513.8s] Well, as they say, it's like catching a falling knife .
[1513.8s] Right ?
[1513.8s] Like, you know, like Yeah .
[1513.8s] Trying to figure out the the peak of the market.
[1522.4s] I I okay .
[1522.4s] Like, we've talked about kind of how zCatch works,
[1527.3s] and it uses
[1528.9s] z k in these sort of very specific areas .
[1528.9s] And it's not, you know, programmable generally.
[1535.1s] Now,
[1536.2s] obviously, there's a lot of talk in the Ethereum world about z k EDMs.
[1540.8s] You guys have any thoughts on that and, like, you know, how those work ?
[1540.8s] Because, you know,
[1547.2s] at what point do we get like, is it truly impossible to get full programmability,
[1553.0s] or do you know, is that something that is just getting closer?

**SPEAKER_02:**
[1557.4s] From a market perspective,
[1559.2s] I think they're mostly z k AVMs have been used for scaling as opposed to privacy.
[1566.3s] Even there, you tend to see some amount of specificity .
[1566.3s] Like,
[1570.7s] think I I mentioned on a podcast before, I'm, you know, friend acquaintances with the lighter CEO,
[1576.4s] and lighter uses
[1580.3s] lighter is like the l two version of Hyperliquid,
[1583.1s] if you will, where they they do perks and they do zero knowledge matching
[1587.5s] off chain, but you know it actually works and it gets written to Ethereum,
[1592.5s] which is pretty cool .
[1592.5s] And, supposedly, they're achieving really high throughputs this way .
[1592.5s] It's not necessarily privacy tech at all.
[1599.9s] I ran
[1601.6s] into some of the Aztec folks in Singapore, and it seems
[1606.7s] trending general purpose still on test net,
[1610.2s] but not fully VM .
[1610.2s] It's like a restricted UTXO type language of sorts, I believe.
[1616.8s] So
[1617.8s] I think there's probably
[1619.6s] not being nearly as expert as Jim, who I'll defer to in a second,
[1623.9s] not being an expert,
[1626.3s] I think it will be there's no intrinsic reason you can't make it
[1631.4s] fully VM or full
[1634.6s] rust or some, you know, JavaScript or whatever.
[1637.9s] But,
[1638.8s] probably, there will be a tremendous
[1641.0s] amount of optimization that would have to happen to make that happen .
[1641.0s] So you probably see special purpose for a while.

**SPEAKER_03:**
[1648.1s] I saw
[1650.4s] that
[1651.8s] and now I'm blanking on the name.
[1654.3s] The the ZK tech that was happening under the Polygon
[1658.4s] banner
[1659.7s] with,
[1664.6s] and I can't remember the the the name of the project now .
[1664.6s] They posted it within the last few months that they were real time ZK proving
[1672.8s] mainnet now.
[1675.4s] But, you know, it was with a battery of of GPUs.
[1678.8s] It was
[1680.7s] not a thing that you would be doing yourself.
[1684.2s] But but, yeah, that that full proving is, you know, is
[1689.0s] possible.
[1690.6s] But, yeah, you you you have that optimization to to be done.
[1695.4s] But, I mean, I think I think that's where things are gonna end up that you've had this
[1702.5s] sort of
[1704.3s] improvement where starting at Bitcoin, it's like, well, how are we gonna prove,
[1709.0s] you know, get to global consensus and and solve the double spend problem?
[1714.0s] Well, it it's by publishing all of details,
[1717.3s] and then we're gonna have, you know, redundant
[1723.2s] state machines running in parallel .
[1723.2s] Right ?
[1723.2s] And that's that's the answer we know that works.
[1728.2s] It was like, what's
[1729.7s] you know you know, like, Satoshi did the big ugly thing,
[1733.5s] but it worked and it made this stuff possible that had never been possible before.
[1738.2s] But it is, you know, it's it's an incredibly big, ugly, expensive way of doing that.
[1744.1s] And then I think just over time, it's like, okay .
[1744.1s] Well,
[1749.3s] having things public
[1751.3s] was sort of a requirement for that consensus model,
[1756.0s] but that was never intentional,
[1758.2s] like, having them all as a public ledger .
[1758.2s] Like, that that's not a positive feature.
[1763.3s] Now if you look at the cyberpunk
[1766.2s] culture that many of these people were coming out of,
[1769.3s] yeah, it's it's private unstoppable money.
[1772.2s] Yeah, no, it wouldn't be public.
[1774.1s] So I saw that,
[1775.9s] yeah .
[1775.9s] Within weeks
[1778.4s] of Bitcoin starting,
[1780.7s] how funny
[1782.9s] said, you know, looking at ways of improving anonymity
[1785.9s] in Bitcoin .
[1785.9s] So that was January
[1788.3s] 2009.
[1789.7s] You know, that was a cypherpunks obvious
[1792.2s] first reaction is, yeah, this is cool now.
[1795.6s] But, yeah, we should have privacy as well .
[1795.6s] And I think we're sort of getting to that point of the the tech has become
[1802.8s] good enough to to solve that without
[1806.5s] broadcasting everything to everyone.

**SPEAKER_00:**
[1809.3s] Yeah .
[1809.3s] Jim, what what do you think ?
[1809.3s] Like, you know, on the sort of general programmability
[1814.3s] ZK front.

**SPEAKER_01:**
[1816.3s] I wish I had more,
[1818.1s] you know, hands on experience with general ZK.
[1823.2s] I see a lot of people very excited by it.
[1828.0s] And
[1828.9s] maybe in a way that makes me skeptical because it seems like a cool toy.
[1833.9s] But I am open to them working great.
[1837.5s] And
[1838.8s] so I don't I don't wanna make us a a a strong
[1842.6s] firm stance at the moment on them, but, but they would be great if they work.

**SPEAKER_00:**
[1848.0s] Yeah .
[1848.0s] I I I it seems like the approach to Karen's point is, like,
[1852.1s] find specific areas where you can, you know, create circuits and apply them and optimize for those and then expand
[1859.5s] that over time .
[1859.5s] You know ?
[1859.5s] Like, it's it's really about kind of, like, you know, nailing those initial use cases Then the using the dispatch approach.

**SPEAKER_01:**
[1868.5s] And that's why I was drawn to that because because Yeah .
[1868.5s] If you if you really narrow it down to something really simple,
[1874.9s] then I think you can do it well.

**SPEAKER_02:**
[1877.6s] I've heard that people even maybe compile
[1880.5s] the specific circuits and then optimize .
[1880.5s] Like, you kinda write them with the general tool .
[1880.5s] Some people do .
[1880.5s] I don't know .
[1880.5s] And then you kind of, like like, okay .
[1880.5s] I got the circuit for the specific thing, but then I gotta make it, like, work.
[1893.1s] You know ?
[1893.1s] Yeah .
[1893.1s] Maybe

**SPEAKER_00:**
[1895.4s] I think compiling a circuit is still pretty very, like,
[1899.5s] computational intensive,
[1901.0s] but it's way more but it's way less for most circuits, once a circuit is compiled, it's way less to do the proof,
[1908.6s] which is you know ?
[1908.6s] And you you gotta continue to push that down, but I think the ratio is very large.
[1916.2s] Okay .
[1916.2s] Well, I think we are out of time.
[1920.1s] You know, where can we find you, Jim ?
[1920.1s] I'm gonna start with you.
[1926.1s] Where can find me ?
[1926.1s] Yes .
[1926.1s] People wanna hear more and learn more about Jim, which I you know, please speak up .
[1926.1s] Ask him where can where they find you.

**SPEAKER_01:**
[1937.2s] I do have a Twitter handle .
[1937.2s] What is my Twitter handle ?
[1937.2s] I can't remember .
[1937.2s] But

**SPEAKER_00:**
[1941.2s] probably j or model .
[1941.2s] I I guess it's probably.

**SPEAKER_02:**
[1945.2s] I'm gonna try to check .
[1945.2s] Hold on .
[1945.2s] Yeah.

**SPEAKER_01:**
[1949.1s] But whatever it is, you should post more often than it .
[1949.1s] Okay .
[1949.1s] I I I Twitter and spurge .
[1949.1s] Is .
[1949.1s] I, like, wake up one day and remember that Twitter exists, and then I twitter I tweet a lot, and then then I forget about that for a couple of weeks .
[1949.1s] It's j h

**SPEAKER_02:**
[1963.5s] o in the the chat .
[1963.5s] I I don't know if we can all see that, the studio chat .
[1963.5s] But Yeah.

**SPEAKER_00:**
[1969.9s] So so,

**SPEAKER_01:**
[1971.4s] yes, you can find him at j Hermas .
[1971.4s] Karen, where can people find Hermas.

**SPEAKER_00:**
[1976.3s] Yeah .
[1976.3s] Oh, j Hermas.

**SPEAKER_02:**
[1977.9s] Yeah .
[1977.9s] I'm on x k g Ruben.
[1981.6s] I'm also on Substack
[1983.5s] trying to, you know I'm, like, a couple old medium posts that I've linked from there .
[1983.5s] I I'm I'm getting a little bit into a Substack rhythm .
[1983.5s] I'll it'll probably be infrequent, but at least of moderate to high quality.
[1996.7s] Also, k james lubin
[1999.1s] dot substack, I think, for now .
[1999.1s] Maybe I'll change the URL.
[2003.0s] Yeah.
[2004.1s] And link it in the in the show notes when we start assuming we do show notes.

**SPEAKER_00:**
[2010.0s] And you can find me on x at vic four Wang.
[2014.0s] Bob has posted why I explained before in my handle.
[2017.9s] You can also find us at on Telegram at the Straum Mercado Group.
[2022.6s] Just go to our website at straummercado.com,
[2026.2s] and that will point you to Telegram .
[2026.2s] And, Bob, where can people find you, and what can people expect next week ?
[2026.2s] Don't close it out, Bob .
[2026.2s] You're the resident Zcash shill .
[2026.2s] One year from now, Zcash

**SPEAKER_02:**
[2038.3s] price or market cap or both?

**SPEAKER_03:**
[2041.0s] I I think it will be in the top 10 .
[2041.0s] Top 10 .
[2041.0s] It's been it's been very close.
[2046.9s] And
[2048.1s] the primary reason is
[2050.9s] privacy is a big need, and it solved it .
[2050.9s] Right ?
[2050.9s] It's not some future promise .
[2050.9s] Like, it works right now .
[2050.9s] There's a mobile app .
[2050.9s] People are using it .
[2050.9s] You know ?
[2050.9s] You've got, like, a ten year near ten year history of,
[2063.6s] you know, top brainiacs
[2065.1s] working on this .
[2065.1s] Lots of credibility.
[2067.6s] So,
[2068.4s] you know, I
[2069.8s] think it it it's great .
[2069.8s] And then I'm looking forward
[2073.2s] to
[2074.3s] smart contracts with with that kind of level as well .
[2074.3s] Just one more thing to mention .
[2074.3s] I couldn't remember Jordy's project,
[2081.6s] Zisk.
[2083.3s] So that was that's a
[2085.9s] spin off group now from Polygon,
[2088.4s] led by Jordi,
[2089.9s] Baylina, and they announced
[2092.1s] real time proving of mainnet blocks that was announced at FCC this year.
[2097.8s] So proving a block,
[2101.5s] in seven
[2103.0s] and a half to twelve seconds, so just under block
[2106.4s] time.
[2107.3s] However,
[2108.4s] it requires
[2110.3s] 24
[2111.7s] very high powered GPUs
[2113.6s] or 48
[2115.4s] more consumer spec.
[2117.5s] So you've got a rack.

**SPEAKER_00:**
[2121.1s] There you go .
[2121.1s] And
[2122.7s] Bob, with that prediction, where can we find you, and can you give us a preview of what people can expect next week ?
[2122.7s] Absolutely .
[2122.7s] Yes .
[2122.7s] So I'm I'm Bob Summerwill, summer like the season, w I l l.

**SPEAKER_03:**
[2135.2s] So on, on everything with with that name.
[2138.7s] And, yes, so next week,
[2141.4s] we will have an early days of Ethereum interview,
[2145.0s] with Christophe YenSys,
[2147.4s] formerly of
[2148.5s] of
[2149.5s] f dev.
[2150.6s] So he was hired in September 2014 into that Berlin office,
[2154.7s] worked on
[2156.2s] testing cross line testing,
[2158.5s] and then later on,
[2160.1s] with
[2161.1s] with their smart locks and the creation of the DAO,
[2165.0s] which is probably,
[2166.1s] you know, Ethereum's first killer app
[2169.2s] until we're killing

**SPEAKER_00:**
[2171.1s] Killing in many
[2172.8s] different ways .
[2172.8s] Yes .
[2172.8s] We're doing that.
[2176.2s] Or Or or you can say birthing because ETC came out of that .
[2176.2s] Correct .
[2176.2s] Right.
[2180.9s] Okay.
[2182.2s] Well, that's time .
[2182.2s] Thank you very much for joining us, and we look forward to seeing you next week .
[2182.2s] Take care .
[2182.2s] Thanks, everybody.
