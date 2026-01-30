**[00:01] SPEAKER_00:** We’re live.

**[00:01] SPEAKER_01:** For real.

**[00:03] SPEAKER_02:** We are live.

**[00:04] SPEAKER_03:** Yes, we’re live.

**[00:05] SPEAKER_01:** And we’re live.

**[00:09] SPEAKER_00:** So maybe this won’t be so meaningful for the rest of you, but it is the 5th of November today, which in the UK is a very famous day of the calendar because it’s Bonfire Night, or Guy Fawkes Night, celebrating the burning at the stake, I guess, of Guy Fawkes, who was the guy who tried to blow up the Parliament in the mid-17th century.

**[00:43] SPEAKER_03:** Oh, the V for Vendetta guy.

**[00:47] SPEAKER_00:** Based on that.

**[00:49] SPEAKER_02:** I mean, the poem, right, says “Remember, remember…” right in the first line, right?

**[00:55] SPEAKER_00:** That’s right. So basically the deal there was that, I guess annually you had the king giving the speech in front of the Parliament, so you had basically the royalty and all of the elite sitting in the hall. They were stuffing barrels of gunpowder underneath, but it was discovered at the last minute. So then there you go. You now have burning of Guy Fawkes in effigy on Bonfire Night to celebrate that it didn’t happen. And yeah, so you have a doll or whatever. That’s the guy that you put on the fire. So anyway, happy Bonfire Night, everybody.

**[01:44] SPEAKER_03:** Happy Bonfire Night.

**[01:46] SPEAKER_02:** We should probably introduce Michael because he’s a special guest.

**[01:50] SPEAKER_01:** Absolutely, yes. I guess he’s a guest. I mean, we’ll make him a regular, I assume, but—

**[01:58] SPEAKER_02:** Yeah.

**[01:58] SPEAKER_03:** See me on the Telegram.

**[02:00] SPEAKER_02:** Michael, do you want to introduce yourself quickly?

**[02:02] SPEAKER_03:** Yeah, yeah. I work on the sales side of the team. I’m going to be introducing the app today to you guys, and I hope you’re excited.

**[02:09] SPEAKER_02:** Well, you work sales, you’re a dev, you’re a front-end dev. You do a bunch of different stuff on the team.

**[02:16] SPEAKER_01:** Yeah.

**[02:16] SPEAKER_00:** Got the moves.

**[02:18] SPEAKER_02:** Yes. Sorry, go ahead.

**[02:21] SPEAKER_00:** Let me just kick off. Hi. Hello, everybody. Welcome, welcome. So we did it. We launched V2. It happened. How does that feel, man?

**[02:34] SPEAKER_01:** I think, Bob, you may not be as tired, you know—

**[02:41] SPEAKER_02:** Oh, he’s gone away. Okay. He’s frozen. He was filming. Yes, well, there were a lot of sleepless nights and working for weekends. Oh, you are back.

**[02:58] SPEAKER_03:** It was back. It was—

**[03:00] SPEAKER_01:** It was my problem. Okay. Yeah, it started spinning everything for a second, and then I—and you all came back. Yeah. Second.

**[03:12] SPEAKER_00:** So how’s V2 being live?

**[03:14] SPEAKER_02:** How’s that feel?

**[03:16] SPEAKER_01:** Much better than before. You know, it’s still—it’s a funny thing. Do you ever feel good for a sustained period? I think not, but extremely happy that it’s live.

I think it would be maybe interesting for the audience to go into a little bit of what it is, and also why it took so long. So we, to the end of 2024, we started to realize that there was a lot of demand for DeFi-type features. So basically Marketplace version 1, or Mercada version 1, if you will, was more NFT-ish. We had interesting and exotic things that might be numbered, and a breadth of them. So we have carbon offsets trading on there, whiskey barrels. Michael moved a lot of collectible shoes through the system. So truly, fairly unique, at least down to having a serial number, or sometimes very unique stuff. So there are occasional one-of-ones on there. We dipped our toes into the art market a little bit with some collabs, and then more financialized stuff too, so the metals in particular being something that we’ve had for a long time.

We kind of saw the most demand for the most financialized items, and it sort of led us to realize what people want from this technology. I mean, one way or another, I think in the course of the company, obviously we did very enterprise stuff a lot in the supply chain, and that kind of actually led very naturally to the unique-item focus. But often everything in the blockchain space pulls back to some sort of financialization, and we kind of decided to stop resisting this impulse, as the market seemed to be demanding it.

So we released—another thing we realized is that in some ways, say your goal is to tokenize everything, like you want all manner of real-world value to be on-chain, existing alongside truly digital-native assets like Bitcoin, ETH, and so on. What would get the world to do that? And we thought the answer was making liquid trading markets where they didn’t exist prior. And that is definitely still part of it, but I think it is more about debt than it is about selling or transacting, right?

And so we kind of, on Marketplace version 1, created a mechanism whereby you could borrow against collateral. It was sort of primitively done, but you could do it within the system, and it got great uptake. And then we said, all right, let’s just make this stuff a little more DeFi. And it just turned out that we were not expecting to do a relaunch. In fact, we were bringing folks on through Q1 and Q2, and TVL was rising, and more loan volumes and all that sort of thing. But we realized that we were hitting the limits of the system pretty quickly, and that we needed to at least change some of the way the internals worked.

We did a listing of our gold token with a small exchange. It was a good experience to work with them, but they had a hard time dealing with things as they were, and found that everyone wants the ERC-20 style, and that to make the capabilities show the best of DeFi, it was a huge, huge effort that turned into a full relaunch. That was never the goal at the outset, but happy to be on the other side of it. The system is definitely way better. It’s a little bit different.

There are some areas where we kind of took a shortcut on version 1 that made it kind of easy, and we’ve gone and made it more decentralized now, which is definitely better. But there could be rough edges around it. As a for instance, we often had fixed pricing on Marketplace version 1, or pure spot pricing, and we have swap pools now, which is great, in that they let the market determine the price and get third-party liquidity in and so forth. But then there’s just more variability on any given trade execution. These things will all sort of work themselves out over time. But huge effort. It’s way better, way better. We ended up in more of a different place than I intended at the outset. Let me just throw it over to say Victor, just on all this.

**[08:56] SPEAKER_02:** Yeah, I think the thing is that really, I think our core insight was: if you think about how people in the real world really accumulate wealth, it’s through small accumulation over time of interest. Think about a savings account, a retirement account—all these things. People aren’t day trading constantly, right?

So what we realized is that it wasn’t enough to simply be able to buy new exotic—or not even exotic—but tokenized things in the real world, but really to turn those into things that were revenue-generating for you individually, and earning over time. So you should be able to have multiple ways, except for trading, to earn things. And we realized that DeFi had kind of answered this, but it did it in a way that was too complicated for the vast majority of people to understand.

I mean, it was only a year ago that Vitalik himself was like, someone needs to explain to me where DeFi yields are coming from, right? If he couldn’t understand it, how could the rest of the world kind of get into it? And we wanted to build a system that would allow the rest of the world to really get those DeFi earning potentials.

And I think there were two things that really came out of it. One is that we had to kind of combine the pool of assets to not just be about real-world asset—liquid real-world assets—which we started with, but we also had to bring in high-quality crypto assets. And then the second thing is that we had to offer different paths of earning. Like you should be able to put some of those assets into a liquidity pool that you would lend out to other people and get interest on that. You should be able to go into swap pools and see when their prices are indifferent. You should be able to earn directly if you put some of your things into a savings account that people could offer. So basically V2 offers all of those paths for users, which we’re really, really excited about.

**[11:16] SPEAKER_00:** Yeah, I mean the point you were saying about trading specifically, Victor—you know, a stat I’ve repeatedly said, parroting from a prior project, was that only about 5% of people who try and day trade actually make a profit. Most people are terrible, absolutely terrible at trading because you just end up trading your emotions, right? You’re scared at the wrong time, and you’re not brave at the right time, and it’s very, very easy to put yourself in a worse position. So having passive yield is absolutely a big need for a huge amount of people.

**[11:59] SPEAKER_02:** Yeah. And I was really surprised that even in the crypto world, the amount of people that had exposure to DeFi was relatively small. I think people didn’t understand how well-established those patterns have gotten. It’s funny that Vitalik has just woke up to this after last year saying, “I didn’t understand,” and then he said, “The future of Ethereum is going to be based on low-risk DeFi,” right?

**[12:28] SPEAKER_00:** So that’s using DeFi themselves now, finally.

**[12:32] SPEAKER_02:** Exactly.

**[12:34] SPEAKER_00:** For like 10 years they were just market dumping to raise funds. And it’s like, you know, the thing that’s kind of got built here because of Ethereum.

**[12:44] SPEAKER_02:** Well, and the world fundamentally, to Kieren’s point, runs on credit, right? That’s—and DeFi has really solved the collateralized lending component in a way that is so seamless. Where else can you get a loan in minutes, right? It’s hard to think of any other place where you could do that in a reliable fashion.

And I think it does it in a way that allows it to be much more transparent than typical financial institutions, right? So the people that are benefiting from those loans are the other users, which is really exciting, I think, to us.

**[13:23] SPEAKER_00:** So I mean, how would you say V2 is different than existing other big-name DeFi protocols?

**[13:34] SPEAKER_01:** Yeah, it very much has a point-click philosophy. I think if you look at the app today, which Michael will show you, there are still details bleeding through that we will eventually kind of smooth out as appropriate. You need the user to know what they’re doing, but not quite know how it’s happening, if you will. Give them the right amount of rope, etc. But it is much easier than other takes on how to do it, in my opinion.

Like, you’ve got to do the one wallet connect. If you use the bridge-in path, probably the easiest way into our system is to take some USDC and mint some of our stable token, USDST. You can also go in with ETH, for instance, and then you’ll be granted some vouchers, which will give you gas on bridge-in. Once that’s happened, you’re in this sort of pleasant, essentially gas-free playground where you point and click like a normal Web2 app.

And this philosophy extends further. So at the moment we have just four swap pools set up, which we’ve seeded, and others have, with some liquidity. We’ll expand this over time for sure, and eventually we’ll go to a permissionless listing structure, if you will. The reason we’ve kept it small to date is just to, one, make sure everything is working, but give you a little less rope than the other platforms out there.

So if you go to Uniswap, for instance, you’ll find the top pool is usually the top pool by volume. You can sort it by TVL if you want. And that tends to direct people’s attention to whatever is trading right now. And the wildly variable APRs, APYs, etc. kind of encourage an aping-in sort of behavior. Our message is kind of more like: yeah, get into whichever assets you prefer, maybe borrow conservatively, and just kind of keep accumulating over time, basically. And so, it’s not quite at a vanguard level, but kind of more of a set it, forget it, be conservative, keep growing attitude that should show through within the system while still having flexibility.

So—and it’s, I guess I would say, batteries included. There are actually two borrowing paths within the system. So once you have collateral, you can mint our stablecoin at a moderate interest rate, and you can then put that into swap pools, you can put that into lending pools, and so on. Or you could just kind of go into the secondary market, which is a little bit more flexible in certain ways. So that would be swapping directly, lending pool, etc.

So I think we always—we don’t aspire to the same ends, but look at projects like Hyperliquid where it’s an alt L1, which means you’ve got control over the fees. The latency of the system is very good as compared with most Ethereum stuff—fast confirmations that are irreversible. And that thing just gives you the latitude to make the user experience as good as possible, which will be a continual battle. But it’s been a real step-function change from both our old stuff and what’s out there today.

**[17:36] SPEAKER_00:** Well, should we take a look?

**[17:37] SPEAKER_01:** Let’s take a look.

**[17:38] SPEAKER_02:** Let’s take a look.

**[17:39] SPEAKER_03:** I guess I’m up. All right, share my screen.

**[17:51] SPEAKER_02:** Okay.

**[17:55] SPEAKER_03:** Okay, everybody see my screen?

**[17:57] SPEAKER_02:** Yes.

**[17:58] SPEAKER_00:** Great.

**[17:58] SPEAKER_03:** So we’re going to start with bridging in tokens. There’s two ways to do it: the normal bridge—well, first you have to connect your wallet, of course, using MetaMask here. There’s two ways to do it. If you want to bridge in ETH or any kind of like Wrapped Bitcoin, PAXG—I think we have something else, forgot—but you bridge it in through this.

If you want to bridge in stables, I would go through the convert feature that will mint on bridge-in. So we’re going to bridge in USDC. This is the testnet, by the way. If you want to try it out, just go to this link. And if you want to get some test USDC, Aave has some test faucets for USDC and USDT.

But let’s bridge in like 100 bucks maybe. Let’s do USDC, get USDT, bridge it in. Confirm, confirm minting. So I bridged them in before, just because this is a bit of a process. But you could also check the status here. It takes a while for the—takes a little bit for the server to update there. But you’ll see earlier when I did that: completed. So let’s just assume that it’s already in here.

**[19:11] SPEAKER_02:** We should be clear the delays are not on the Mercada side. Pretty much instantaneous. It’s on the Ethereum Sepolia side.

**[19:20] SPEAKER_03:** Yep. So we’re going to swap some right now. Let’s swap some USDT. Let’s do like, I don’t know, 10. Let’s get some eST. Swap. And also gas is used through USDST on our app as well, similar to Hyperliquid, actually.

**[19:44] SPEAKER_00:** And what do you pay? What do you pay? What are you paying?

**[19:47] SPEAKER_03:** As normal transaction—it depends on the transactions—but some are $0.01 to $0.03 depending on what it is.

**[19:55] SPEAKER_01:** If it’s $0.03, it’s probably three transactions in there.

**[19:58] SPEAKER_03:** Yes. Yeah, yeah. Usually, I believe a transfer—no, not a transfer. A bridge-in is two transactions, if I’m not mistaken.

**[20:10] SPEAKER_01:** Although, yes. If you bridge in, you get minted vouchers. So the vouchers just give you free transactions one-to-one with the cents, I suppose. Yep.

**[20:20] SPEAKER_03:** Vouchers you can track here as well, in this cool little widget. Anyway, so I swapped some assets and—

**[20:28] SPEAKER_00:** Vouchers, just to clarify: so that’s kind of a little nice hack of getting past the “Oh my God, I haven’t got any ether for gas on this chain at this time.”

**[20:44] SPEAKER_03:** Right, exactly.

**[20:46] SPEAKER_02:** It’s an onboarding thing, right? The one big limitation on a lot of chains, right, is you can’t even do your first transactions on most of them until you have the native token, right? Allows us to bring people on without requiring that.

**[21:03] SPEAKER_03:** Yep. So we’ve done the swaps. We’re going to add some liquidity to the—

**[21:07] SPEAKER_02:** Michael, I just want to mention, if you can go back to the swap. One really important thing with our system is it allows you to see sort of the exchange rates internally, but also the global exchange rate. That’s where you see the exchange spot right under there. So that’s the global, right? This is something we learned from two of our trading contests. So where are the arbitrage opportunities? You can see from these two things directly instead of having to go somewhere else to figure.

**[21:39] SPEAKER_01:** All right, it’s been funny on the live system. For those who have used DEXes, you find if there’s not that much liquidity, you can definitely push the price as reported and provided by the DEX off of the true market price. And in here we’re combining a couple different data sources to get the spot price, and that’s just coming through an oracle, really. Here it’s just a reminder.

The spot price is used for the health calculations when you borrow, and the reason you want to do that is, you know, someone could do a big trade on one of the pools and manipulate that price and then liquidate someone, or etc., as we saw very recently with the Balancer attack.

But it’s also just a reminder to get good execution. So for those who go try this, if you do it on the live net, just make sure: don’t do huge trades on there just yet, because liquidity is still coming in both from us and externals to make sure you get good execution.

**[22:55] SPEAKER_03:** Yep. And yeah, just the pool is not really relevant to the oracle price, but yeah, everyone should keep that in mind as well. Anyway, we’ll get back to the pool.

So these are the lending pools that contribute to the borrow lending, which we’ll get to in a little bit. But I can deposit 100 in here, and I will. It should mint me some mUSDST tokens, which is my pool token that’s representative of my lending pool contribution. I believe that is in these non-earning right here. I am again.

So let’s also contribute some money to the swap pool so you can earn APY. See what looks juicy right now—the silver. Wow.

**[23:39] SPEAKER_01:** Silver trades.

**[23:41] SPEAKER_03:** So I’m going to confirm my deposit. And we are deposited, and we’re earning.

**[23:55] SPEAKER_00:** APY, and you’re depositing both SILVERST and USDST?

**[24:02] SPEAKER_03:** That’s right.

**[24:03] SPEAKER_01:** When you input to a swap pool, you need to put in both pairs. And we have two modes here. It’s probably just better to use the A and B mode, but you can do a single-sided liquidity add. But what it does is it does a swap so that you have an equal amount of the other one, and then it deposits it. So yeah, and it’s a convenience if you—

**[24:27] SPEAKER_00:** If you wanted to get into it but you haven’t got the right stuff.

**[24:30] SPEAKER_01:** That’s correct.

**[24:31] SPEAKER_03:** Yeah, yeah. The button’s right here for everybody that wants to do it single-side if they choose to do so.

And let’s see, what are we going to—let’s do some borrowing. So I’m going to supply my whole eST stack, 14 bucks, all of it.

**[24:49] SPEAKER_00:** Don’t do it all.

**[24:49] SPEAKER_03:** Do all of it.

**[24:53] SPEAKER_01:** On the gas though, it will be—

**[24:56] SPEAKER_03:** So I have—let’s see, I have $14. Oh, we gotta hide some of these. 14.90 here. Because the LTV, I believe, is about 75%. I have $11.

**[25:09] SPEAKER_01:** We tend to match the market. You don’t need to go all the way up to the LTV, but let’s—

**[25:14] SPEAKER_03:** Let’s go all the way.

**[25:17] SPEAKER_02:** I vote this is risky. I would recommend people—we’re going to see some—

**[25:26] SPEAKER_03:** My whole—always be careful. Your health factor: once you hit 1, you can get liquidated. But we can also—

**[25:32] SPEAKER_02:** I recommend going with 50%.

**[25:35] SPEAKER_03:** Basically, we could always just repay it and it should update here.

**[25:41] SPEAKER_00:** Buyer’s remorse, instant refund.

**[25:44] SPEAKER_03:** Overall, that’s the app. It’s kind of a combination of Uniswap and Aave. For you guys more familiar with Web3, if you guys have any questions or you want a deeper walkthrough, feel free to message me on Telegram and we can hop onto Zoom. But there you go, guys.

**[25:58] SPEAKER_01:** Yeah. Also, for the gold and silver bugs out there, we take physical deposits in addition to supporting some of the popular—well, actually, there’s no—so far as I know, there’s no really popular silver token other than ours. But we’ll take PAXG right now, and soon the Tether Gold coin as well. And that can drive your borrowing power within the system. You can borrow and then turn around and lend, CDP path, and that will make your gold into a productive asset.

**[26:36] SPEAKER_00:** I hadn’t thought that there weren’t other silver tokens. That’s a good—

**[26:39] SPEAKER_01:** I looked. They’re very small, to the extent that they’re out there.

**[26:45] SPEAKER_02:** I mean, there are a bunch of gold tokens at this point.

**[26:47] SPEAKER_01:** A lot of gold, yeah.

**[26:53] SPEAKER_00:** So yeah, so that was that.

**[26:57] SPEAKER_01:** I have one more comment, actually. It’s been kind of fun. So the prod system, you know, it’s been online for a couple days, and the most trading has been on the ETH pool because it’s been volatile, right? Sorry if anyone’s gotten hurt out there in the last 24 hours or so. Michael likes to get liquidated, I know.

But so, you know, that’s manifested very quickly on our system, and it’s where a lot of the trading is. And it’s still very much beta mode. But we have enough people that we’re starting to see the pool prices actually converge to the spot price, because if it doesn’t, there’s an arb in there. So, you know, get in early. Don’t put crazy amounts in, but because these systems become pretty efficient over time, but when it’s not, there’s money to be made.

And finally, I will say for those of you who are holders of Kata points, mostly from V1 or contest participation, we’re going to monitor the system for a little bit, just make sure everything’s working and so on, and then start to work towards the V2 points program. Not imminent, but coming.

**[28:23] SPEAKER_03:** Excellent.

**[28:24] SPEAKER_00:** Because a number of people asking that.

**[28:26] SPEAKER_02:** Question I was just going to add: if you want to try it out now, you can just go to our updated website at stratomercada.com and click Launch App.

One of the big efforts that we’re going to do is to improve the UX. So if anyone has any suggestions, please join our Telegram community and send us messages there. We’d love to hear from you. We’re actively trying to improve it and achieve our goal of—

**[28:56] SPEAKER_00:** Mainstreaming DeFi. And Colin there says the whole platform works perfectly, just waiting on rendering of the front page to be visible. For me, that’s a friend—a friend, Crypto Tarzan—who was having the issue of seeing his Kata that were hiding under the non-earning assets.

**[29:20] SPEAKER_02:** Yeah, just click that arrow button. Yes.

**[29:23] SPEAKER_00:** And you’ll see—that’s the sneaky arrows. When I do that, I get the old stuff. I think I’ve got some whiskey barrel bits in there and some other little—

**[29:38] SPEAKER_01:** You get a whiskey barrel. Those are real. They’re trading.

**[29:42] SPEAKER_00:** I got some fraction—

**[29:45] SPEAKER_01:** Did you really? Okay.

**[29:47] SPEAKER_00:** I believe so.

**[29:47] SPEAKER_01:** Right, right. That’s cool pieces.

**[29:51] SPEAKER_00:** So yeah, they’re still lurking.

**[29:55] SPEAKER_01:** I guess, yeah, we should. I know some people have exited those. They are, no pun intended, kind of illiquid. But there’s been a little bit of whiskey barrel trading, so we should discuss—

**[30:09] SPEAKER_00:** Offline holders are not being rugged. The whiskey—

**[30:15] SPEAKER_01:** You know, you get the physical delivery at the end. Maybe not if it’s fractionalized at the—

**[30:23] SPEAKER_00:** End of the rail bed.

**[30:26] SPEAKER_01:** That’s right.

**[30:27] SPEAKER_00:** Making delivery. Okay. Well, is there anything else anyone wanted to cover, or we can wrap it up.

**[30:34] SPEAKER_02:** No, we just look forward to you guys trying it and giving us whatever input. We’re really excited for you to see this. And we’re still going to evolve a lot. Things have been moving quickly and will continue to be moving quickly on it. So, exciting times for us.

**[30:52] SPEAKER_00:** So yeah, just head to stratomercada.com—so S T R A T O M E R C A D A dot com, stratomercada.com—and you’ve got the app there and all.

**[31:08] SPEAKER_01:** The information in the top right. Then the people do another landing page, which we of course eliminate as well. It’s better that this thing is up. But yes, sometimes you have to just make a choice and launch it. But yes, in time.

**[31:26] SPEAKER_00:** Well, don’t I say: if you’re not embarrassed a bit about the things that you release, then you release too late, for sure.

**[31:34] SPEAKER_02:** Absolutely. Yeah. We are strong advocates of the great stuff.

**[31:38] SPEAKER_01:** It’s like a child, like a teenager. You’re like, “I love this child,” but you still get on my nerves a little bit.

**[31:47] SPEAKER_02:** You can say that as a non-parent. As a parent, they never get—it’s just love.

**[31:54] SPEAKER_00:** They’re perfect.

**[31:55] SPEAKER_01:** They never get on your nerves.

**[31:57] SPEAKER_00:** Never.

**[31:57] SPEAKER_01:** They definitely get on your nerves. You’re lying to me, you’re lying to the internet.

**[32:03] SPEAKER_00:** Children are never frustrating.

**[32:04] SPEAKER_02:** Never. They’re balls of joy. That’s it. Thank you.

**[32:14] SPEAKER_00:** Cheers, everyone.

**[32:15] SPEAKER_01:** Everyone have a good.