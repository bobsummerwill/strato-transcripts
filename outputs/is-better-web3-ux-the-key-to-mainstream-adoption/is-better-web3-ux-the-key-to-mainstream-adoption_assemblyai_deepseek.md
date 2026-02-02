**[00:01] SPEAKER_00:** We are live.

**[00:04] SPEAKER_01:** Are we live?

**[00:05] SPEAKER_00:** We are live. Yes.

**[00:06] SPEAKER_02:** So Streamyard says.

**[00:14] SPEAKER_03:** You guys have an intro you like to do.

**[00:17] SPEAKER_00:** Yeah, well, first.

**[00:18] SPEAKER_03:** Here we go.

**[00:19] SPEAKER_01:** Here we go. Yeah, there we are.

**[00:23] SPEAKER_00:** Go ahead, Bob.

**[00:25] SPEAKER_01:** So hello, everybody. I guess we're ready to go. Today we have a special guest with us. It's the first time that you and I have met, Brian, but you are very familiar to all of my colleagues here as an ex block app sir.

**[00:47] SPEAKER_03:** Yeah, Crypto X.

**[00:50] SPEAKER_00:** You are never an ex block app sir. You're always part of Team Block, the alumni network. Yes, exactly.

**[00:57] SPEAKER_03:** Yeah, yeah, yeah. You guys gave me my first opportunity to work in Ethereum back in 2017, which feels like ages ago and I mean, it is ages ago.

**[01:06] SPEAKER_02:** Lifetime.

**[01:07] SPEAKER_00:** Yeah.

**[01:08] SPEAKER_03:** Yeah. So thank you guys for that. Happy to be on here. It's always great seeing you guys around and talking about one of my favorite topics.

**[01:16] SPEAKER_01:** Welcome. So welcome back. Would you like to introduce yourself and talk a little bit about what Pistachio is?

**[01:24] SPEAKER_03:** Yeah, sure. So, Brian Smokovich, B Smokes ETH on Twitter. We're building Pistachio Fi. It's a mobile-first neo bank built entirely on crypto rails meant to provide premium savings with premium security and the whole concept of better UX. Right? Like I will get to the question in the moment of is UX the key to mainstream adoption? But I wanted to really just build something that I think self-custody is really important to me and really important to a lot of people about why we originally got into the space. But the UX for a lot of these apps was just always so terrible. Right? And so I wanted to be the change that I wanted to see in the world and decided to just say screw it and build my own, basically taught myself UI design in order to begin this in the beginning and then built it literally by willing Pistachio into existence and many iterations of building the app. And now we're at a point where I feel very blessed that we've been publicly recognized by many Ethereum talking heads in the sense of being recognized for our UX and what we've been designing and building and doing things in a way to just bring more people on chain.

**[02:57] SPEAKER_01:** I see that the number you said was 18 versions in five months.

**[03:04] SPEAKER_03:** Oh, we've pushed out several beyond since that tweet, probably at least three or four. So yeah, we ship a lot. It's a lot of just talking to users and finding what's broken, what's wrong. I'll stand at a conference and literally stand over people's shoulders as they download the app and watch every little tap. Right? Like, oh, the focus is wrong, the focus is not beyond the keyboard in this instance, or the search is showing the wrong things. That's the thing about UX, you design something and you build it, right? And then it's of course going to be bugged. Everything is always bugged, right? We go through rigorous testing, but when it goes into somebody's very specific use case because they touch certain things in a certain way and that's what triggered this one bug, or it's on a certain app or operating system or phone, it behaves in a certain way. And then when you see the person use it, you're like, oh, there's a big button there, right? They're going to press it, they're going to press it, and then they don't press it. And you're like, why did they not press the very clear call to action that I made? So the only real way you can track things through tools like Mixpanel and AppsFlyer is to see the UX flows, but you're going to miss all the little details of every single user interaction. Being able to watch and categorize that and implement that is a big portion of what I think makes our app more successful.

**[04:36] SPEAKER_02:** Let me ask maybe a slightly controversial question. So if you think about FinTech 1.0 companies, I would say they greatly improved the UX on the legacy financial system. It looks way better, works better, it's not nearly as much of a mess as the Schwab interface or what have you. This worked significantly. Maybe Robinhood is the best example. But I think that's like the baseline expectation. But is it sort of like the totality of UX? Because I think one of the challenges in crypto is there's stuff that's bleeding through that's complicated or scary and all of that too. For my understanding, I think you guys are multi-chain, but inheriting all of the problems from the layers below too. How do you think about that?

**[05:33] SPEAKER_03:** There's a lot to fix. I think you're right that Robinhood is sort of that shining example of fintech generational UX UI of making things easy, fast, gamified in a way. I really love Venmo as an example. I think Venmo is a very good example of really good UX but not really being good UI. The UI of Venmo is almost antiquated, but the UX is done beautifully. They approached it from a user problem, like what is the user problem? It's sending money. Right? You open the app, it's got this big send button and it's so simple to just a few clicks to send money to someone and then withdraw it to their bank. So they honed in on that very specific UX without caring so much about how sexy the UI is. With Web3 UX, we have an entirely different set of problems that go very deep just to get to parity with traditional finance and fintech. When it comes to Web3, especially with Ethereum, we have gas to worry about, token approvals to worry about, multi-chain to worry about, bundled transactions if there are multiple transactions. Luckily, all of these things now have solutions. Between 4337 and 7072, there are ways to implement Paymasters, bundle transactions together, do zaps. Not everyone does all of these things together. It's like Pistachio 5, we do all of this, right? We do it all together, all in one go. One thing we don't do, for example, is within Web3 gaming, there's this concept of session keys. If I'm going to have a game, do I then have to sign every single transaction for everything that gets written to the blockchain? No, you just do a session key. You sign once as you sign into the game or app, sign a session key that extends for that period of your gaming session. That abstracts away that problem. So it takes a lot for a Web3 company to get to parity on all these things. There are ways to solve it all. It's just a matter of does the app creator understand all these things? Are they aware of all these things? Do they care enough to do all these things? Some major apps or wallets, I love Rabby, I'm a big Rabby user, but they still don't have 7072 implemented. There's a lot of big players that still don't have these available UX implementations live and integrated into their apps.

**[08:36] SPEAKER_00:** I'm curious, Brian. To reveal some background, when you were working for us, you were a sales guy. How did you teach yourself about UX and product design? I'm glad you joined the dark side, but what got you there and made you feel like this is something you can take on?

**[08:59] SPEAKER_03:** I've always really loved the product side. I think I had a natural ability to be a salesperson, I love to chat and create rapport, and that's very important for sales and marketing. But at the end of the day, I really just had a knack for the product side. Once I realized it and started doing it, it was a natural calling. When you find something you really like, you don't really know that you really like it until you're doing it and knee-deep in it. Suddenly, I'm spending 12 to 15 hour days working on a website just because I'm obsessed with doing this and improving it. When I was learning UX UI, I took some courses, but a lot of it was trial and error. A big part of it was having my own thing. I'm sure Kieren can relate to this, once it’s yours, there's a different obsession that comes with it. Rather than just working for someone and getting equity options and a paycheck, truly owning something and being aligned with it, if I kill this, I get monetarily incentivized just because I killed it and it's my baby. I think that shines a lot in being a founder and growing your own application. I have an obsession with talking to users and understanding what makes it better, the perfectionist in me of seeing something wrong and needing to smooth it over. All of that has aggregated and led me to where I am today.

**[11:14] SPEAKER_00:** One benefit of being in the space so long is we've worked with some great people and could always see you had that entrepreneurial spirit. It's interesting it’s come on this path. One challenging thing about UX for people from pure technical backgrounds is the ability to listen when people say, hey, this is wrong, or I don't understand this. That seems to be a big hurdle a lot of truly technical people can’t get over sometimes.

**[11:48] SPEAKER_03:** It comes down to empathy. UX is just empathy brought to life. You need to put yourself in your user's shoes and empathize with their frustrations, which should frustrate you. If it's going to piss them off, it should piss you off that it's not good enough. If you don't have that empathy, you're not going to care enough to fix it. You should be pissed if a user is going to be pissed.

**[12:36] SPEAKER_02:** Who do you see your target user as? There's full-on normies, crypto natives, but I'm absolutely interested in age ranges. It's hard to define exactly the bucket, but they probably are crypto friendly.

**[13:06] SPEAKER_03:** Normally, we are normie friendly. You can invite your family without fear of throwing them to the wolves of volatility, risk, perps, scams, rug pulls. But my ideal user is probably between 25 to 55, crypto inclined, in crypto for some time, large amounts of funds on chain, want to not need to offboard crypto into the bank, want a high-quality self-custodial, high-security, highly convenient mechanism in their pocket, value convenience, security, privacy, and have funds that if they're going to risk off into stables, can easily earn safe, curated, high-quality yield at least double US treasuries without being exposed to equities and can spend or transfer money very quickly. Just talking to a lot of people, that seems to be the bread and butter of a customer user base who can put five figures into my app, preferably at least 50 grand into six figures, and trust Pistachio's security mechanism due to the due diligence and effort we’ve put into protecting our users. But also if you want to invite friends, family, make it easy to get on chain, this is the easiest way.

**[15:18] SPEAKER_00:** Why do you think the UX has been so bad in Web3 for so long?

**[15:28] SPEAKER_03:** I think it's a large disconnect between people building and people talking to users. I talk to a lot of founders and frequently audit people’s UX UIs and give feedback. People build MVP fast, want to build something, but it's a hard chicken-and-egg problem. How do I talk to users if I don’t have anything for them to use? So they build in a direction of building a product first, then getting users. Realistically, they should build the product while talking to potential users, finding people who have the problem. You need to find friends who have that problem, if not, keep going out there and find people who have this problem. If you don’t find people who have this problem, you're creating a solution in search of a problem instead of finding people willing to test what you're doing and show them the earliest iterations. Figure out if this is confusing, good, bad, really solving the core problem. Luckily, I think a lot of builders create companies because they encounter problems in their earlier careers or usages. For example, maybe you work in a B2B company, you're a founder, and you face a pain point, so you create a company to solve that problem. Same with B2C, loving crypto, trying apps, dogfooding apps led me to creating what I'm doing. I would dogfood apps and think, this isn’t good enough. That's the main reason creators or app builders try to create something cool, add vanity, trace a trend because they see where money's flowing right now, like how many perps companies are there trying to get money because VCs are flowing to that narrative. They're pulled in different directions instead of going back to the core of what problem they want to solve.

**[19:12] SPEAKER_00:** My theory is in the first phase of Web3, we were trying to solve technical problems, make it work at all. The people who did those things succeeded, but those people who solve super hard technical problems are not UX people. They think more about solving technical problems, and that's where the shift is happening. I think you've caught it at the right time.

**[19:51] SPEAKER_03:** I think there are more engineers these days who are more design-savvy, hybrid engineers, full-stack engineers intrigued in design because they built their own thing from scratch and were forced to design, as opposed to straight backend engineers.

**[20:16] SPEAKER_02:** I code again occasionally because AI has gotten so good. If it has a template, it's not good at UX from scratch, but if it has something to work from, I’m like no, just generate a component like this and do this, and it usually gets it right within a couple times. The iteration cycle is so much less painful than it used to be.

**[20:38] SPEAKER_03:** Absolutely.

**[20:40] SPEAKER_00:** In my Web2 startups and mobile startups, I realized as CTO of first startups, by turning step three into step one, I could 10x the usage overnight, but it's a totally different mode of thinking than how am I going to get the code out the door.

**[21:05] SPEAKER_03:** The infrastructure didn’t exist for a while. I remember vividly at the block apps office, Vic said mobile Web3 sucks. It was true for a long time because the infrastructure needed to bring Web3 to mobile didn't exist. This last bear cycle of crypto, VC funding went to infrastructure. It's still not good enough, but it's improving. Libraries, SDKs compatible with React Native or native mobile languages make it easier for developers to take and build and integrate because we can’t build everything from scratch. As a bootstrap company, we need good docs, SDKs, APIs, hardened stuff we can use without banging our heads against the wall trying to integrate because it doesn’t work.

**[22:28] SPEAKER_00:** At the time, some Ethereum devs said they have a mobile solution, run a node on your phone. I was like do you know battery life is important to me? Last of the day.

**[22:49] SPEAKER_01:** This is where I started.

**[22:50] SPEAKER_00:** Remember you tried to run it on a Watch Man 2050 smartwatch.

**[22:56] SPEAKER_01:** My first project was getting CPP Ethereum running on a smartwatch. It didn’t but GE worked on a smartwatch because the chain was small, kind of workable. At the time, we thought we’d have light client running soon, same with desktop. Mist had an embedded node, thought it’d get optimized 10x, 100x.

**[23:34] SPEAKER_03:** Yeah.

**[23:36] SPEAKER_00:** Never built a mobile app before.

**[23:38] SPEAKER_01:** Obviously, you’re gonna run inside every router, be OS level service.

**[23:46] SPEAKER_03:** Building a mobile app sucks. It’s hard.

**[23:53] SPEAKER_00:** That’s like a nightmare.

**[23:57] SPEAKER_03:** That was the easy part. Building a Web3 app multi-chain on multiple operating systems, the amount of edge cases is a nightmare. That’s been the hardest part. We launched June, May-June, and hardened the app all summer discovering and smoothing edge cases.

**[24:26] SPEAKER_01:** I see you launched on Android too. Congratulations.

**[24:30] SPEAKER_03:** Thank you. Publically at least. We always soft release before, but Android took months longer than Apple because Apple standardizes everything works on every device. Android, optimize back to Android 12 to cover 90% use cases, Android 11 and below still runs 10% of the world, optimize hardware for base-level Android devices, lightweight app for cheap devices. Different screen types, edge-to-edge display on React Native Expo didn’t work well. People launch apps on different devices don’t use Expo, native to each device, no good libraries on Expo for edge-to-edge display until two months ago. My CTO wants to launch a publicly available repo to help with all these hardships we went through.

**[26:19] SPEAKER_00:** At my last mobile company, to make sure things worked on iOS ran two devices, simulator, table of Android devices tested configurations. Probably 10,000 devices.

**[26:36] SPEAKER_01:** More than 10,000.

**[26:43] SPEAKER_00:** TVs and tablets.

**[26:43] SPEAKER_00:** What was the biggest challenge you faced evolving to founder?

**[27:08] SPEAKER_03:** The biggest challenge evolves over time, as I level up, the challenges get bigger. Early days, aligning people with my vision, disconnect interpretation between vision in my head and theirs. Learning UX UI design to put it into Figma and show them this is what I want got my CTO on board who loved the idea. Next challenge, architectural solution vendor selection. Knew what chain I wanted to work on, multi-chain, be robust multi-chain app with account abstraction smart accounts, infrastructure available limited. Worry about key storage, recovery, keep people safe, vendors at each part of stack understanding Web3 deeply tradeoffs vendors bring, price unfunded, budget scalable long-term, modular vertical stack vendor lock-in. Ripped vendors out who weren't performant enough, delivery setback longer build time. Two-person team, me and CTO longest time, hired second full-time engineer last month.

**[29:49] SPEAKER_00:** Awesome. Every step new challenge, but excited working hard. Exciting hear where you get with project in general.

**[30:11] SPEAKER_03:** Thank you.

**[30:11] SPEAKER_01:** When are we ready for normies?

**[30:24] SPEAKER_03:** Ready now. Pistachio onboarding smooth, easy, no seed phrases, no worries phone stolen, recover programmatically securely no hacks. Next wave alpha ability send bank transfers from on-chain account to specific chain accounts worldwide cheap, solves pain. Better Web3 UX not key mainstream adoption, better UX key app adoption Robinhood big but need fundamental problem pain solved ability send on-chain transaction arrive ACH transfer SEPA US Mexico for $1, significant pain solved common apps Dollar App Felix $3 flat fee expensive send small amounts $100 3% fee high, our ability $50,000 for $1 banking rails or keep onchain Pistachio peer-to-peer transactions free ready normies now increase use cases app solve painful expensive pains way do it.

**[33:03] SPEAKER_00:** Good note.

**[33:04] SPEAKER_01:** Thank you very much.

**[33:06] SPEAKER_03:** Guys for having me.

**[33:11] SPEAKER_02:** Catch up at international events.

**[33:16] SPEAKER_03:** Yeah, perfect. If you’re going to EthHam Brazil or DevConnect, I’ll be at both.

**[33:22] SPEAKER_00:** Definitely see you there. Share details about your talk.

**[33:29] SPEAKER_03:** Yeah, absolutely. Take care.

**[33:32] SPEAKER_01:** Thanks so much.

**[33:34] SPEAKER_03:** Thanks. Great meeting you Bob.

**[33:36] SPEAKER_01:** You too. Cheers, bye.