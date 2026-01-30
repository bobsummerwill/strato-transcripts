**[00:01] SPEAKER_03:** You've been live for real.

**[00:03] SPEAKER_00:** We are live, yes.

**[00:05] SPEAKER_03:** We're live and we're live. So maybe this won't be so meaningful for the rest of you, but it is the 5th of November today, which in the UK is a very famous day of the calendar because it's Bonfire Night or Guy Fawkes Night, celebrating the burning at the stake of Guy Fawkes, who was the guy who tried to blow up the parliament in the mid 17th century. Oh, the "V for Vendetta" guy. "V for Vendetta," so that's based on that.

**[00:49] SPEAKER_00:** I mean, the poem says "remember, remember" right in the first line.

**[00:54] SPEAKER_03:** That's right. So basically, the deal there was that annually you had the King giving the speech in front of the Parliament. So you had the royalty and all of the elite sitting in the hall. They were stuffing barrels of gunpowder underneath, but it was discovered at the last minute. So then there you go. You now have burning of Guy Fawkes in effigy on Bonfire Nights to celebrate that it didn't happen. You have a doll or whatever that's the guy that you put on the fire. So, happy Bonfire Night, everybody. We should probably introduce Michael because he's a special guest.

**[01:59] SPEAKER_00:** Michael, do you want to introduce yourself quickly?

**[02:02] SPEAKER_01:** Yeah. I work on the sales side of the team. I'm going to be introducing the app today to you guys, and I hope you're excited.

**[02:09] SPEAKER_00:** Well, you work sales, you're a dev, you're a front-end dev, you do a bunch of different stuff on the team.

**[02:16] SPEAKER_03:** Got the moves. Let me just kick off. Hi. Hello, everybody. Welcome. So we did it. We launched V2. It happened. How does that feel? I think Bob, you may not be as tired.

**[02:51] SPEAKER_00:** There have been a lot of sleepless nights and working through weekends. Oh, you are back.

**[02:58] SPEAKER_02:** He was back. It was my problem. Okay. Yeah, it started spinning everything for a second, and then you all came back.

**[03:11] SPEAKER_03:** Take it. So how's V2 being live? How does that feel?

**[03:16] SPEAKER_02:** Much better than before. It's still never a funny thing. Do you ever feel good for a sustained period? I think not, but extremely happy that it's live. I think it would be maybe interesting for the audience to go into a little bit of what it is and also why it took so long. We realized through the end of 2024 that there was a lot of demand for DeFi-type features. Basically, Marketplace version one, Mercado version one, if you will, was more NFT-ish. We had interesting and exotic things that might be numbered. We had carbon offsets trading on whiskey barrels. Michael moved a lot of collectible shoes through the system. So truly unique, at least down to having a serial number or sometimes very unique stuff. There were occasional one-of-ones on there. We dipped our toes into the art market a little bit with some collabs. And also more financialized stuff, too, like the medals, which we've had for a long time. We saw the most demand for the most financialized items, and it sort of led us to realize what people want from this technology. In the course of the company, we did very enterprise stuff, a lot in the supply chain, and that kind of actually led very naturally to the unique item focus. But often everything in the blockchain space pulls back to some sort of financialization, and we kind of decided to stop resisting this impulse as the market seemed to be demanding it. We realized that in some ways, if your goal is to tokenize everything, you want all manner of real-world value to be on-chain existing alongside truly digital native assets like Bitcoin and Ethereum. What would get the world to do that? We thought the answer was making liquid trading markets where they didn't exist prior, and that is definitely still part of it, but I think it is more about debt than it is about selling or transacting. On Marketplace version one, we created a mechanism whereby you could borrow against collateral. It was sort of primitively done, but you could do it within the system, and it got great uptake. Then we said all right, let's just make this stuff a little more DeFi. It turned out that we were not expecting to do a relaunch. In fact, we were bringing folks on through Q1 and Q2, and TVL was rising, more loan volumes, and all that sort of thing. But we realized that we were hitting the limits of the system pretty quickly and that we needed to change some of the way the internals worked. So we did a listing of our gold token with a small exchange. It was a good experience to work with them, but they had a hard time dealing with things as they were, and found that just everyone wants the ERC-20 style, and to make the capabilities show the best of DeFi, it was like a huge effort that turned into a full relaunch, which was never the goal at the outset. Happy to be on the other side of it. The system is definitely way better. It's a little bit different. There are some areas where we kind of took a shortcut on version one that made it kind of easy, and we've gone and made it more decentralized now, which is definitely better, but there could be rough edges around it. For instance, we often had fixed pricing on Marketplace version one or pure spot pricing, and we have swap pools now, which is great in that they let the market determine the price and get third-party liquidity in. But then there's more variability on any given trade execution. These things will all sort of work themselves out over time, but it was a huge effort. It's way better, but it's we ended up in more of a different place than I intended at the outset.

**[08:56] SPEAKER_00:** Yeah, I think our core insight was really if you think about how people in the real world really accumulate wealth, it's really through small accumulation over time of interest, like a savings account, a retirement account. People aren't day trading constantly. What we realized is that it wasn't enough to simply be able to buy new exotic or tokenize things in the real world, but really to turn those into things that were revenue generating for you individually and earning over time. So you should be able to have multiple ways except for trading to earn things. We realized that DeFi had kind of answered this, but it did it in a way that was too complicated for the vast majority of people to understand. It was only a year ago that Vitalik himself said someone needs to explain to me where DeFi yields are coming from. If he couldn't understand it, how could the rest of the world kind of get into it? And we wanted to build a system that would allow the rest of the world to really kind of get those DeFi earning potentials. I think there were two things that really came out of it. One is that we had to combine the pool of assets to not just be about real-world assets, liquid real-world assets, which we started with, but we also had to bring in high-quality crypto assets. The second thing is that we had to offer different paths of earning. You could be able to put some of those assets into a liquidity pool that you would lend out to other people and get interest on that. You could go into swap pools and see when their price is different. You should be able to earn directly if you put some of your things into a savings account that people can offer. Basically, V2 offers all of those paths for users, which we're really excited about.

**[11:16] SPEAKER_03:** Yeah, I mean, the point you were saying about trading specifically, Victor, you know, sort of a stat I've repeatedly said parroting from a prior project was that only about 5% of people who try day trading actually make a profit. Most people are terrible at trading because you just end up trading your emotions. You're scared at the wrong time and not brave at the right time, and it's very easy to put yourself in a worse position. So having passive yield is absolutely a big need for a huge amount of people.

**[12:00] SPEAKER_00:** Yeah, I was really surprised that even in the crypto world, the amount of people that had exposure to DeFi was relatively small. People didn't understand how well established those patterns have gotten. It's funny that Vitalik has just woken up to this after last year saying I didn't understand. He said the future of Ethereum is going to be based on low-risk DeFi, right? So that's what we're talking about.

**[12:30] SPEAKER_03:** Well, BEF are using DeFi themselves now, finally. For like 10 years, they were just market dumping to raise funds. The thing that's kind of got built here because of Ethereum is...

**[12:44] SPEAKER_00:** Well, and the world fundamentally, to Kieren's point, runs on credit, and DeFi has really solved the collateralized lending component in a way that is so seamless. Where else can you get a loan in minutes in a reliable fashion? It does it in a way that allows it to be much more transparent than typical financial institutions. The people that are benefiting from those loans are the other users, which is really exciting, I think, to us.

**[13:23] SPEAKER_03:** So how would you say V2 is different than existing other big-name DeFi protocols?

**[13:35] SPEAKER_02:** Yeah, it very much has a point-click philosophy. If you look at the app today, which Michael will show you, there are still details bleeding through that we will eventually smooth out as appropriate. You need the user to know what they're doing but not quite know how it's happening. Give them the right amount of rope, et cetera. But it is much easier than other takes on how to do it, in my opinion. You've got to do sort of the one wallet connect if you use the bridge-in path. The easiest way into our system is to take some USDC and mint some of our stable token USD ST. You can also go in with ETH, for instance, and then you'll be granted some vouchers which will give you gas on bridge-in. Once that's happened, you're in this sort of pleasant, essentially gas-free playground where you point and click like a normal Web2 app. This philosophy extends further. At the moment, we have just four swap pools set up, which we've seeded and others have with some liquidity. We'll expand this over time and eventually go to a permissionless listing structure. The reason we've kept it small to date is to make sure everything is working and give you a little less rope than the other platforms out there. If you go to Uniswap, for instance, you'll find the top pool is usually the top pool by volume. You can sort it by TVL, and that tends to direct people's attention to whatever is trading right now, with wildly variable APRs, APYs, etc., kind of encouraging an "aping in" sort of behavior. Our message is more like, get into whichever assets you prefer, borrow conservatively, and just keep accumulating over time. It's not quite at a Vanguard level, but more of a set-it-and-forget-it, be conservative, keep growing attitude that should show through within the system while still having flexibility. Batteries included, I guess I would say. There are actually two borrowing paths within the system. Once you have collateral, you can mint our stablecoin at a moderate interest rate and then put that into swap pools, lending pools, etc. Or you could go into the secondary market, which is a little bit more flexible in certain ways, like swapping directly, lending pool, etc. We don't aspire to the same ends, but we look at projects like Hyperliquid, where it's an Alt-L1, which means you've got control over the fees. The latency of the system is very good compared with most Ethereum stuff. Fast confirmations that are irreversible, and it just gives you the latitude to make the user experience as good as possible, which will be a continual battle, but it's been a real step function change from both our old stuff and what's out there today.

**[17:36] SPEAKER_03:** Well, should we take a look? Let's take a look. Let's take a look.

**[17:39] SPEAKER_01:** Oh, I guess I'm off. All right. Share my screen. Okay, everybody see my screen?

**[17:57] SPEAKER_00:** Yes. Great.

**[17:58] SPEAKER_01:** So we're going to start with bridging in tokens. There's two ways to do it. The normal bridge. Well, first you have to connect your wallet, of course, using MetaMask here. There's two ways to do it. If you want to bridge ETH or any kind of wrapped Bitcoin or PaxG, you bridge it into this. If you want to bridge in stables, I would go through the convert feature that will mint on bridge. So we're going to bridge in USDC. This is the testnet, by the way, if you want to try it out. Just go to this link. And if you want to get some test USDC, Aave has some test faucets for USDC and USDT. Let's bridge in $100 maybe. Let's do USDC, get USDT. Bridge it in. Confirm, confirm. Minting. So I bridged them in before just because this is a bit of a process, but you could also check the status here. Takes a while for the server to update, but there's an earlier one I did that completed. So let's assume it's already in here.

**[19:12] SPEAKER_00:** The delays are not on the Mercada side. It's pretty much instantaneous. It's on Ethereum Sopolia side.

**[19:20] SPEAKER_01:** Yep. So we're going to swap some right now. Let's swap some USDT. Let's do like 10. Let's get some EFST swap. Gas is used through USDST on our app as well. Similar to Hyperliquid actually.

**[19:44] SPEAKER_03:** And what do you pay? What are you paying as an all transaction?

**[19:49] SPEAKER_01:** It depends on the transactions, but some are one cent to three cents, depending on what it is. If it's three cents, it's probably like three transactions in there.

**[19:59] SPEAKER_02:** Yeah.

**[20:10] SPEAKER_01:** Usually, bridging is two transactions.

**[20:19] SPEAKER_02:** Although, yes, if you bridge in, you get minted vouchers. The vouchers give you free transactions one-to-one with the cents, I suppose.

**[20:28] SPEAKER_01:** Yep. Vouchers you can track here as well. It's a cool little widget. Anyway, so I swapped some assets.

**[20:45] SPEAKER_00:** Yeah, exactly. It's an onboarding thing. Without it, one big limitation on chains is you can't even do your first transactions on most of them until you have the native token. So it allows us to bring people on without requiring that.

**[21:03] SPEAKER_01:** Yep. So we've done the swaps. We're going to add some liquidity.

**[21:07] SPEAKER_00:** I just want to mention, if you can go back to the stock, one really important thing with our system is it allows you to see sort of like the exchange rates internally, but also the global exchange rate. That's where you see the exchange spot right under there. So that's the global. This is something we learned from two of our trading contests, where arbitrage opportunities you can see from these two things directly, instead of having to go somewhere else to figure it out.

**[21:39] SPEAKER_02:** It's been funny on the live system. For those who have used DEXs, if there's not that much liquidity, you can definitely push the price as reported and provided by the DEX off of the true market price. Here we're combining a couple of different data sources to get the spot price, and that's just coming through at Oracle really. It's just a reminder the spot price is used for the health calculations when you borrow. The reason you want to do that is someone could do a big trade on one of the pools and manipulate that price and liquidate someone.

**[22:27] SPEAKER_00:** As we saw very recently with the Balancer attack.

**[22:30] SPEAKER_02:** Yeah, yeah, yeah. But it's also just a reminder to get good execution. So for those who go try this, if you do it on the live net, just make sure don't do huge trades on there just yet because liquidity is still coming in both from us and externals to make sure you get good execution.

**[22:55] SPEAKER_01:** Yep. And yeah, just the pool is not really relevant to the Oracle price, but everyone should keep that in mind as well. Anyway, we'll get back to the pool. These are the lending pools that contribute to the borrow lending, which we'll get to in a little bit, but I can deposit a hundred in here and then I will admit some M USDST tokens, which is my pool token representing my lending pool contribution. I believe that is in these non-earnings right here. So let's also contribute some money to the swap pool so you can earn APY. Let's see what looks juicy right now. The silver wow.

**[23:38] SPEAKER_02:** Silver trains.

**[23:42] SPEAKER_01:** Looking for my deposit. And we are deposited and we're earning APY.

**[23:56] SPEAKER_03:** And you're depositing both Sylv ST and USD ST?

**[24:02] SPEAKER_02:** That's right. When you input to a swap pool, you need to put in both pairs. We have two modes here. It's probably just better to use the A and B mode. But you can do a single-sided liquidity add. What it does is it does a swap so that you have an equal amount of the other one, and then it deposits it.

**[24:23] SPEAKER_03:** That's the convenience if you wanted to get into it, but you haven't got the right stuff.

**[24:31] SPEAKER_01:** That's correct. The button's right here for everybody that wants to do it single-sided if they choose to do so. Let's see, what are we going to do? Let's do some borrowing. So I'm going to supply my whole ETH stack, 14 bucks. All of it. Don't do it all. Do all of it.

**[24:51] SPEAKER_02:** He'll be okay on the gas, though.

**[24:56] SPEAKER_01:** So I have $14.90 here. Because the LTV is about 75%, I have $11.

**[25:09] SPEAKER_02:** We tend to match the market.

**[25:11] SPEAKER_01:** You don't need to go all the way up to the LTV, but let's go all the way anyway.

**[25:18] SPEAKER_00:** I would flag. This is risky.

**[25:21] SPEAKER_01:** I would recommend people always be careful with their health factor.

**[25:28] SPEAKER_00:** Once you hit one, you can get liquidated, but we can also, I recommend going with the anti-personal basically.

**[25:36] SPEAKER_01:** Yeah, we can always just repay it. Overall, that's the app. It's kind of a combination of Uniswap and Aave for you guys more familiar with Web3. If you have any questions or want a deeper walkthrough, feel free to message me on Telegram and we can hop on to Zoom.

**[25:58] SPEAKER_02:** But there you go, guys. Also, for the gold and silver bugs out there, we take physical deposits in addition to supporting some of the popular... Well, actually, there's no so far as I know, there's no really popular silver token other than ours. But we'll take PaxG right now and soon the Tether gold coin as well. That can drive your borrowing power within the system. You can borrow and then turn around and lend CDP path, and that will make your gold into a productive asset.

**[26:36] SPEAKER_03:** I hadn't thought that there weren't other silver tokens. That's a good thing.

**[26:39] SPEAKER_02:** I looked, they're very small to the extent that they're out there.

**[26:45] SPEAKER_00:** I mean, there are a bunch of gold tokens at this point. A lot of gold.

**[26:53] SPEAKER_03:** So, yeah. So that was that.

**[26:57] SPEAKER_02:** I have one more comment. The prod system has been online for a couple of days, and the most trading has been on the ETH pool because it's been volatile. Sorry if anyone's gotten hurt out there in the last 24 hours or so. Michael likes to get liquidated, I know. That's manifested very quickly on our system, and it's where a lot of the trading is. It's still very much beta mode, but we have enough people that we're starting to see the pool prices actually converge to the spot price because if it doesn't, there's an ARB in there. Get in early, don't put crazy amounts in because these systems become pretty efficient over time. But when it's not, there's money to be made. Finally, I will say for those of you who are holders of Kata points, mostly from V1 or contest participation, we're going to monitor the system for a little bit, make sure everything is working, and then start to work towards the V2 points program. Not imminent, but coming.

**[28:23] SPEAKER_03:** Excellent. Because I've seen a number of people asking that question.

**[28:28] SPEAKER_00:** And I was just going to add, if you want to try it out now, you can just go to our updated website at stradomercada.com and click launch app. One of the big efforts that we're going is to improve the UX. So if anyone has suggestions, please join our Telegram community and send us messages there. We'd love to hear from you. We're actively trying to improve it and achieve our goal of mainstreaming DeFi.

**[28:59] SPEAKER_03:** And Colin there says, the whole platform works perfectly, just waiting on the rendering of the front page to be visible for me. That's a friend, Crypto Tarzan, who was having the issue of seeing his Carter that we're hiding under the non-earning assets.

**[29:21] SPEAKER_00:** Yeah, just click that arrow button. Yes, and you'll see.

**[29:25] SPEAKER_03:** That's the sneaky arrows. When I do that, I get the old stuff, I think. I've got some whiskey barrel bits in there and some other little... You get a whiskey barrel? Those are real. They're trading. I got some fraction.

**[29:45] SPEAKER_02:** Did you really?

**[29:47] SPEAKER_03:** Okay. I believe so. Right, right. That's cool. I recall a lot. Yeah, they're still lurking there.

**[29:55] SPEAKER_02:** I know some people have exited those. They are, no pun intended, kind of illiquid, but there's been a little bit of whiskey barrel trading, so we should discuss offline.

**[30:10] SPEAKER_03:** Holders are not being rugged.

**[30:13] SPEAKER_02:** The whiskey's still out there. You get the physical delivery at the end. Maybe not if it's fractionalized.

**[30:23] SPEAKER_03:** At the end of the rail bed.

**[30:26] SPEAKER_02:** That's right.

**[30:27] SPEAKER_03:** Making delivery. Okay. Well, is there anything else anyone wanted to cover, or we can wrap it up.

**[30:34] SPEAKER_00:** No, we just look forward to you guys trying it and giving us whatever input. We're really excited for you to see this, and we're still going to evolve a lot. Things have been moving quickly, and we'll continue to move quickly on it. Exciting times for us.

**[30:53] SPEAKER_03:** So yeah, just head to stradomercada.com. Launch button in the top right. We'll do another landing page, which we have to eliminate as well. It's better that this thing is up. Sometimes you have to just make a choice and launch it. But yes, in time.

**[31:26] SPEAKER_03:** Well, didn't I say if you're not embarrassed a bit about the things that you release, then you release too late?

**[31:34] SPEAKER_00:** For sure. Absolutely. We're strong advocates.

**[31:39] SPEAKER_02:** It's great, though. It's like a teenager. You're like, I love this child, but you're still getting on my nerves a little bit.

**[31:47] SPEAKER_00:** You can say that as a non-parent.

**[31:49] SPEAKER_02:** As a parent, I can do that as a parent.

**[31:52] SPEAKER_00:** They never get on your nerves? They're perfect. You're lying to me. You're lying to the internet.

**[32:03] SPEAKER_03:** Children are never frustrating. Never.

**[32:05] SPEAKER_00:** They're just perfect. They're balls of joy. That's it. Non-stop. Thank you, everyone.

**[32:14] SPEAKER_03:** Cheers, everyone. Have a good week.