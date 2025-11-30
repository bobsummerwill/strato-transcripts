**[00:00] SPEAKER_03:** You've been live for real.

**[00:02] SPEAKER_00:** We are live, yes.

**[00:04] SPEAKER_03:** We're live and we're live. So maybe this won't be so meaningful for the rest of you, but it is the 5th of November today, which in the UK is a very famous day of the calendar because it's Bonfire Night or Guy Fawkes Night, celebrating the... burning at the stake, I guess, of Guy Fawkes, who was the guy who tried to blow up the parliament in the mid-17th century. Oh, the *V for Vendetta* guy. *V for Vendetta*, so that's based on that.

**[00:30] SPEAKER_00:** I mean, the poem says "Remember, remember" right in the first line.

**[00:34] SPEAKER_03:** That's right. So basically the deal there was that I guess annually you had like the King giving the speech in front of the Parliament. So you had basically the royalty and all of the elite sitting in the hall. They like stuffing barrels of gunpowder underneath, but it was discovered at the last minute. So then there you go. You now have burning of Guy Fawkes in effigy on Bonfire Nights to celebrate that it didn't happen. And yeah, so you have a, you know, like a doll or whatever that's the guy that you put on the fire. So anyway, happy Bonfire Night, everybody. Happy Bonfire Night. We should probably introduce Michael because he's a special guest.

**[01:10] SPEAKER_00:** Absolutely. Yes. I guess he's a guest. I mean, we'll make him a regular, I assume, but yeah, guys see me on the Telegram. Michael, do you want to introduce yourself quickly?

**[01:21] SPEAKER_01:** Yeah. I work on the sales side of the team. I'm going to be introducing the app today to you guys and I hope you're excited.

**[01:28] SPEAKER_00:** Well, you work sales, you're a dev, you're a front-end dev, you do a bunch of different stuff on the team.

**[01:34] SPEAKER_03:** Got the moves. Let me just kick off. Hi. Hello, everybody. Welcome, welcome. So we did it. We launched V2. It happened. How does that feel, man? I think Bob, you may not be as tired, you know. Oh, oh, he's gone away. Okay. He's frozen. He was filming.

**[01:52] SPEAKER_00:** Yes. Well, there are a lot of sleepless nights and working through weekends. Oh, you are back.

**[02:00] SPEAKER_02:** He was back. It was my problem. Okay. Yeah, it started spinning everything for a second, and then you all came back.

**[02:07] SPEAKER_03:** Yeah. Take it. So how's V2 being live? How does that feel?

**[02:11] SPEAKER_02:** Much better than before. You know, it's still... never it's a funny thing. Do you ever feel good for like a sustained period? I think not. But extremely happy that it's live. I think it would be maybe interesting for the audience to go into a little bit of like what it is and also why it took so long. So we, through the end of 2024, started to realize that there was a lot of demand for DeFi type features. So basically, Marketplace version one—Mercata version one, if you will—was more NFT-ish. We had interesting and exotic things that might be numbered and a breadth of them. So this was, we have carbon offsets trading on there, whiskey barrels. Michael moved a lot of collectible shoes through the system. So truly, you know, fairly unique, at least down to having a serial number or sometimes very unique stuff. So there was occasional one-of-ones on there. We dipped our toes into the art market a little bit with some collabs. And also more financialized stuff, too. So the metals in particular being something that we've had for a long time. And we kind of saw the most demand for the most financialized items. And it sort of led us to realize what people want from this technology. I mean, one way or another, I think in the course of the company, obviously we did very enterprise stuff, a lot in the supply chain, and that kind of actually led very naturally to the unique item focus. And but you know, often everything in the blockchain space pulls back to some sort of financialization and we kind of decided to stop resisting this impulse as the market seemed to be demanding it. So we released... The other thing we realized is that in some ways, so you know, say your goal is to tokenize everything. Like you want all manner of real-world value to be on-chain existing alongside truly digital native assets like Bitcoin, ETH, and so on. What would get the world to do that? And we thought the answer was making liquid trading markets where they didn't exist prior. And that is definitely still part of it. But I think it is more about debt than it is about selling or transacting. Right. And so we kind of on Mercata version one created a mechanism whereby you could borrow against collateral. It was sort of primitively done, but you could do it within the system and it got great uptake. And then we said, all right, let's just make this stuff a little more DeFi. And it just turned out that we were not expecting to do a relaunch. In fact, we were bringing folks on through Q1 and Q2 and TVL was rising and more loan volumes and all that sort of thing. But we realized that we were hitting the limits of the system pretty quickly and that it would be just, that we needed to at least change some of the way the internals worked. So we did a listing of our gold token with a small exchange. It was a good experience to work with them, but they had a hard time dealing with things as they are—as they were rather—and found that just everyone wants the ERC-20 style. And that to make the capabilities sort of show the best of DeFi, it was like a huge, huge effort that turned into a full relaunch, which was never the goal at the outset. You know, happy to be on the other side of it. The system is definitely way better. It's a little bit different. There are some areas where we kind of took a shortcut on version one that made it kind of easy, and we've gone and made it, say, more decentralized now, which is definitely better, but there could be like rough edges around it. As a for instance, we often had fixed pricing on Mercata version one or pure spot pricing, and we have swap pools now, which is great in that they let the market determine the price and get third-party liquidity in and so forth. But then there's just more variability on the any given trait execution. And so though these things will all sort of work themselves out over time. But huge effort. It's way better, way better. But we ended up in more of a different place than I intended at the outset. Let me just throw it over to, say, Victor just on all this.

**[06:35] SPEAKER_00:** Yeah, I think the thing is that really, I think our core insight was really if you think about how people in the real world really accumulate wealth, it's really through like, small accumulation over time of interest. You know, like think about a savings account, a retirement account, all these things. People aren't like day trading constantly, right? So what we realized is that it wasn't enough to simply be able to buy new exotic—or not even exotic, but tokenize things in the real world—but really to turn those into things that were revenue generating for you individually and earning over time. So it should be able to have multiple ways except for trading to earn things. And we realized that DeFi had kind of answered this, but it did it in a way that was too complicated for the vast majority of people to understand. I mean, it was only a year ago that Vitalik himself was like, "someone needs to explain to me where DeFi yields are coming from," right? Like if he couldn't understand it, how could the rest of the world kind of get into it? And we wanted to build a system that would allow the rest of the world to really kind of get those DeFi earning potentials. And I think there were two things that really came out of it. One is that we had to kind of combine the pool of assets to not just be about real-world assets, liquid real-world assets, which we started with, but we also had to bring in high-quality crypto assets. And then the second thing is that we had to offer different paths of earning. Like you could be able to put some of those assets into a liquidity pool that you would lend out to other people and get interest on that. You would be able to go into swap pools and see when their price is different. You should be able to earn directly if you put some of your things into a savings account that people can offer. So basically, V2 offers all of those paths for users, which we're really, really excited about.

**[08:24] SPEAKER_03:** Yeah, I mean, the point you were saying about trading specifically, Victor, you know, sort of a stat I've repeatedly said parroting from a prior project was that only about 5% of people who try and day trade actually make a profit. Yeah, most people are terrible, absolutely terrible at trading because you just end up trading your emotions, right? And you're just scared at the wrong time and you're not brave at the right time. And it's very, very easy to put yourself in a worse position. So, you know, having passive yield is absolutely a big need for a huge amount of people.

**[09:00] SPEAKER_00:** Yeah, I was really surprised that even in the crypto world, the amount of people that had exposure to DeFi was relatively small. I mean, I think people didn't understand how well established those patterns have gotten. It's funny that Vitalik has just woken up to this after like last year saying "I didn't understand." He said the future of Ethereum is going to be based on low-risk DeFi, right? So that's what we're talking about.

**[09:25] SPEAKER_03:** Well, EF are using DeFi themselves now, finally. For like 10 years, they were just like market dumping to raise funds. And it's like, you know, the thing that's kind of got built here because of Ethereum is...

**[09:40] SPEAKER_00:** Well, and the world fundamentally, to Kieran's point, runs on credit, right? And DeFi has really solved the collateralized lending component in a way that is so seamless. Like, where else can you get a loan in like minutes, right? Place where you could do that in a reliable fashion. And I think it does it in a way that allows it to be much more transparent than, say, typical financial institutions. Right. So the people that are benefiting from those loans are the other users, which is really exciting, I think, to us.

**[10:10] SPEAKER_03:** So I mean, how would you say V2 is different than existing, you know, other big-name DeFi protocols?

**[10:18] SPEAKER_02:** Yeah, it very much has a point-click philosophy. I think if you look at the app today, which Michael will show you, there are still details bleeding through that we will eventually kind of smooth out as appropriate. You know, you need the user to know what they're doing but not quite know how it's happening, if you will. Give them the right amount of rope, etc. But it is much easier than other takes on how to do it, in my opinion. You've got to do sort of the one wallet connect if you use the bridge-in path. So the probably easiest way into our system is to take some USDC and mint some of our stable token USDST. You can also go in with ETH, for instance. And then you'll be granted some vouchers which will give you gas on bridge-in. Once that's happened, you're in this sort of pleasant, let's say, essentially gas-free playground where you point and click like a normal Web2 app. And this philosophy extends further. So at the moment, we have just four swap pools set up, which we've seeded and others have with some liquidity. We'll expand this over time, for sure. And eventually, we'll go to sort of like a permissionless listing structure, if you will. The reason we've kept it small to date is just to, one, make sure everything is working, but kind of give you a little bit of a little less rope than the other platforms out there. So like if you go to Uniswap, for instance, you'll find the top pool is usually the top pool by volume. You can sort it by TVL if you want. And that tends to direct people's attention to whatever is trading right now, right? And the wildly variable APRs, APYs, etc., kind of encourage like an aping in sort of behavior. Our message is kind of more like: yeah, get into whichever assets you prefer, maybe borrow conservatively and just kind of keep accumulating over time basically. And so, you know, it's not quite at a Vanguard level, but kind of more of a "set it, forget it, be conservative, keep growing" attitude that should show through within the system while still having flexibility. I guess I would say batteries included. There are actually two borrowing paths within the system. So once you have collateral, you can mint our stablecoin at a moderate interest rate. And you can then put that into swap pools, you can put that into lending pools, and so on. Or you could just kind of go into the secondary market, which is a little bit more flexible in certain ways. So that would be swapping directly, lending pool, etc. So I think we always... we don't aspire to the same ends, but look at projects like Hyperliquid, where it's an Alt-L1, which means you've got control over the fees. The latency of the system is very good as compared with most Ethereum stuff. Let's say it's fast confirmations that are irreversible and that sort of thing. And it just gives you the latitude to make the user experience as good as possible, which will be a continual battle, but it's been a real step function change from both our old stuff and what's out there today.

**[13:20] SPEAKER_03:** Well, should we take a look? Let's take a look. Let's take a look.

**[13:25] SPEAKER_01:** Oh, I guess I'm off. All right. Share my screen. Okay, everybody see my screen?

**[13:32] SPEAKER_00:** Yes. Great.

**[13:34] SPEAKER_01:** So we're going to start with bridging in tokens. There's two ways to do it. The normal bridge. Well, first you have to connect your wallet, of course, using MetaMask here. There's two ways to do it. If you want to bridge in ETH or any kind of like wrapped Bitcoin, PaxG, I think we have something else. I forgot. You bridge it into this. If you want to bridge in stables, I would go through the convert feature that will mint on bridge. So we're going to bridge in USDC. This is the testnet, by the way, if you want to try it out. Just go to this link. And if you want to get some test USDC, Aave has some test faucets for USDC and USDT. But let's bridge in like $100 maybe. Let's do USDC, get USDT. Bridge it in. Confirm, confirm. Minting. So I bridged them in before just because this is a bit of a process, but you could also check the status here. Takes a little bit for the server to update there, but there's an earlier one I did that completed. So let's just assume that it's already in here.

**[14:38] SPEAKER_00:** The delays are not on the Mercata side. It's pretty much instantaneous. It's on the, you know, Ethereum Sepolia side.

**[14:46] SPEAKER_01:** Yep. So we're going to swap some right now. Let's swap some USDT. Let's do like, I don't know, 10. Let's get some ETHST swap. And also gas is used through USDST on our app as well. Similar to similar to Hyperliquid actually.

**[15:05] SPEAKER_03:** And what do you pay? What do you pay? What are you paying as an all transaction?

**[15:10] SPEAKER_01:** It depends on the transactions, but some are one cent to three cents, depending on what it is. If it's three cents, it's probably like three transactions in there.

**[15:19] SPEAKER_02:** Yes.

**[15:20] SPEAKER_01:** Yeah. Usually like I believe a transfer... No, not a transfer. A bridging is two transactions, if I'm not mistaken.

**[15:27] SPEAKER_02:** Although, yes, if you bridge in, you get minted vouchers. So the vouchers just give you free transactions one-to-one with the cents, I suppose.

**[15:35] SPEAKER_01:** Yep. Vouchers you can track here as well. And it's a cool little widget. Anyway, so I swapped some assets.

**[15:42] SPEAKER_03:** And vouchers, just to clarify, so that's kind of a little nice hack of getting past the, oh my God, I haven't got any ether for gas on this chain at this time, right?

**[15:52] SPEAKER_00:** Yeah, exactly. It's an onboarding thing, right? Like without... one big limitation on love chains, right? Like you can't even do your first transactions on most of them until you have the native token, right? So it allows us to bring people on without requiring that.

**[16:08] SPEAKER_01:** Yep. So we've done the swaps. We're going to add some liquidity.

**[16:13] SPEAKER_00:** I just want to mention, if you can go back to the stock, one really important thing with our system is it allows you to see sort of like the exchange rates internally, but also like the global exchange rate. That's where you see the exchange spot right under there. So that's the global, right? This is something we learned from two of our trading contests. So where are like, you know, the arbitrage opportunities you can see from these two things directly, instead of having to go somewhere else to figure it out.

**[16:40] SPEAKER_02:** It's been funny on the live system. So for those who have used DEXs, you find if there's not that much liquidity, you can definitely push the price as reported and provided by the DEX off of the true market price. And here we're combining a couple different data sources to get the spot price and that's just coming through an oracle really. Here it's just a reminder the spot price is used for the health calculations when you borrow. And the reason you want to do that is, you know, someone could do a big trade on one of the pools and manipulate that price and then liquidate someone or etc.

**[17:12] SPEAKER_00:** As we saw very recently with the Balancer attack.

**[17:15] SPEAKER_02:** Yeah, yeah, yeah. So... But it's also just a reminder to get good execution. So, for those who go try this, if you do it on the live net, just make sure, you know, don't do huge trades on there just yet because liquidity is still coming in both from us and externals to make sure you get good execution.

**[17:33] SPEAKER_01:** Yep. And yeah, just the pool is not really relevant to the Oracle price, but yeah, everyone should keep that in mind as well. Anyway, we'll get back to the pool. So these are the lending pools that contribute to the borrow lending, which we'll get to in a little bit, but I can deposit a hundred in here and then it should admit me some M USDST tokens, which is my pool token. That's represented of my lending pool contribution. I believe that is in these non-earnings right here. I am a good... so let's also contribute some money to the swap pool so you can earn APY. Let's see what looks juicy right now. The silver, wow.

**[18:14] SPEAKER_02:** Silver trains.

**[18:16] SPEAKER_01:** Looking for my deposit. And we are deposited and we're earning APY.

**[18:23] SPEAKER_03:** And you're depositing both SylvST and USDST?

**[18:27] SPEAKER_02:** That's right. When you input to a swap pool, you need to put in both pairs. And we have two modes here. It's probably just better to use the A and B mode. But you can do a single-sided liquidity add. But what it does is it does a swap so that you have an equal amount of the other one. And then it deposits it.

**[18:45] SPEAKER_03:** That's the convenience if you wanted to get into it, but you haven't got the right stuff.

**[18:49] SPEAKER_01:** That's correct. The button's right here for everybody that wants to do it single-sided if they choose to do so. Let's see, what are we going to do? Let's do some borrowing. So I'm going to supply my whole ETH stack, 14 bucks. All of it.

**[19:04] SPEAKER_02:** Don't do it all. Do all of it. He'll be okay on the gas, though.

**[19:09] SPEAKER_01:** So I have, let's see, I have $14. I'll hide some of these. $14.90 here. Because the LTV, I believe, is about 75%. I have $11.

**[19:22] SPEAKER_02:** We tend to match the market.

**[19:24] SPEAKER_01:** You don't need to go all the way up to the LTV, but let's go all the way anyway.

**[19:28] SPEAKER_00:** I would flag. This is risky.

**[19:30] SPEAKER_01:** I would recommend people... my hope that always be careful your health factor.

**[19:34] SPEAKER_00:** Once you hit one, you can get liquidated, but we can also... I recommend going with the eighty percent basically.

**[19:42] SPEAKER_01:** Yeah, we can always just repay it. And it will show update here. Buyer's remorse at instant and refund. Overall, that's the app. It's kind of a combination of Uniswap and Aave for you guys more familiar with Web3. If you guys have any questions or if you want a deeper walkthrough, feel free to message me on Telegram and we can hop on to Zoom.

**[20:06] SPEAKER_02:** But there you go, guys. Also, for the gold and silver bugs out there, we take physical deposits in addition to supporting some of the popular... Well, actually, there's no so far as I know, there's no really popular silver token other than ours. But, you know, we'll take PaxG right now and soon the Tether Gold coin as well. And that can drive your borrowing power within the system. You can borrow and then turn around and lend CDP path and that will make your gold into a productive asset.

**[20:38] SPEAKER_03:** I hadn't thought that there weren't other silver tokens. That's a good thing.

**[20:42] SPEAKER_02:** I looked what there's—they're very small to the extent that they're out there.

**[20:46] SPEAKER_00:** I mean, there are a bunch of gold tokens at this point. A lot of gold. Yeah.

**[20:50] SPEAKER_03:** So, yeah. So that was that.

**[20:54] SPEAKER_02:** I have one more comment, actually. It's been kind of fun. So the prod system, you know, it's been online for a couple days. And that, you know... The most trading has been on the ETH pool because it's been volatile, right? Sorry if anyone's gotten hurt out there in the last 24 hours or so. Michael likes to get liquidated, I know. So that's manifested very quickly on our system and it's where a lot of the trading is and it's still very much beta mode, but we have enough people that we're starting to see the pool prices actually converge to the spot price because if it doesn't, there's an ARB in there. So get in early, don't put crazy amounts in because these systems become pretty efficient over time. But when it's not, there's money to be made. And finally, I will say for those of you who are holders of Kata points, mostly from V1 or contest participation, we're going to monitor the system for a little bit, just make sure everything is working and so on, and then start to work towards the V2 points program. So not imminent, but coming.

**[21:58] SPEAKER_03:** Excellent. Because I've seen a number of people asking that question.

**[22:02] SPEAKER_00:** And I was just going to add, like, if you want to try it out now, you can just go to our updated website at stratomercada.com and click launch app. One of the big efforts that we're going to is to improve the UX. So if anyone has any suggestions, please join our Telegram community and send us messages there. We'd love to hear from you. We're actively trying to improve it and, you know, achieve our goal of like mainstreaming DeFi.

**[22:28] SPEAKER_03:** And Colin there says, "the whole platform works perfectly, just waiting on the rendering of the front page to be visible for me." That's a friend, Crypto Tarzan, who was having the issue of seeing his Kata that we're hiding under the non-earning assets.

**[22:42] SPEAKER_00:** Yeah, just click that arrow button. Yes, and you'll see.

**[22:45] SPEAKER_03:** That's the sneaky arrows. When I do that, I get the old stuff. I think I've got some whiskey barrel bits in there and some other little...

**[22:52] SPEAKER_02:** You get a whiskey barrel? Those are real. They're trading. Did you really?

**[22:56] SPEAKER_03:** I got some fraction. Okay. I believe so. Right, right. That's cool. I recall a lot. Yeah, they're still lurking there.

**[23:04] SPEAKER_02:** I know some people have exited those. They are, no pun intended, kind of illiquid, but there's been a little bit of whiskey barrel trading, so we should discuss offline.

**[23:14] SPEAKER_03:** Holders are not being rugged.

**[23:16] SPEAKER_02:** The whiskey's still out there. You get the physical delivery at the end. Maybe not if it's fractionalized.

**[23:22] SPEAKER_03:** At the end of the rail bed.

**[23:23] SPEAKER_02:** That's right.

**[23:24] SPEAKER_03:** Making delivery. Okay. Well, is there anything else anyone wanted to cover or we can wrap it up?

**[23:29] SPEAKER_00:** No, we just look forward to... we look forward to you guys trying it and giving us whatever input and we're really excited for you to see this. And you know, we're still gonna evolve a lot. Things have been moving quickly and we'll continue to be moving quickly on it. So exciting times for us.

**[23:46] SPEAKER_03:** So, yeah, just to head to stratomercata.com. So, S-T-R-A-T-O-M-E-R-C-A-T-A.com. stratomercata.com. And you've got the app there and all the information.

**[24:02] SPEAKER_02:** Launch button in the top right. Then we'll do another landing page, which we have to, of course, eliminate as well. It's better that this thing is up. But, yes, this, you know... Sometimes you have to just make a choice and launch it. But yes, in time.

**[24:16] SPEAKER_03:** Well, didn't I say if you're not embarrassed a bit about the things that you release, then you release too late?

**[24:21] SPEAKER_00:** For sure. Absolutely. Yeah. We do. We're strong advocates.

**[24:25] SPEAKER_02:** It's great, though. It's like a teenager. You're like, "I love this child, but you're still getting on my nerves a little bit."

**[24:32] SPEAKER_00:** You can say that as a non-parent.

**[24:34] SPEAKER_02:** As a parent, I can do that as a parent.

**[24:37] SPEAKER_00:** They never get... it's just love.

**[24:39] SPEAKER_02:** They're perfect. They never get on your nerves? Never. They definitely get on your nerves. You're lying to me. You're lying to the internet.

**[24:46] SPEAKER_03:** Children are never frustrating. Never.

**[24:49] SPEAKER_00:** They're just perfect. They're balls of joy. That's it. Non-stop. Thank you, everyone.

**[24:54] SPEAKER_03:** Cheers, everyone. Have a good week.