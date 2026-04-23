**[00:21] SPEAKER_01:** Hey, everyone. We are live and we are here with two of my favorite people in the blockchain space. I would say I guess we could say we're old friends, even though we're not that old.

**[00:35] SPEAKER_00:** It feels like it now, right?

**[00:37] SPEAKER_01:** It definitely does. So we're talking about building enterprise blockchain with Microsoft. And just to set the context for everyone, STRATO, Block Apps and Microsoft have had a really long relationship. It goes all the way back to 2015, when Microsoft was building out the blockchain layer of Azure. They found us to be their partner, and that became the first major partnership of the Ethereum ecosystem, which we launched back at Devcon 1. Unfortunately, York had to miss that, but was instrumental in making it happen. Since then, in an industry with huge amounts of turnover and change, I'm talking to two people who have been building from the beginning and are still building today. So I want to give you guys a little bit of your bio, even though I know you're uncomfortable with it, but it was really hard to actually narrow the accomplishments you guys have done over the last 11 years. So I'm going to start with you, Kieren. Kieren is founder and president and CEO of Block Apps. He's one of the early Ethereum contributors, working on the Haskell implementation and head of Ethereum's cryptocurrency research group. He founded Block Apps, launched the category of blockchain as a service with Microsoft, and kickstarted enterprise adoption of Ethereum without requiring deep protocol experience. He's a founding member of the Enterprise Ethereum Alliance. Wow, this is quite a lot of stuff. And under his leadership, Block Apps became the only blockchain platform available across all major cloud providers and built the first RWA projects for Fortune 500 companies, consortiums, and governments. Block Apps' latest project is STRATO, which is bringing DeFi to hard assets such as precious metals. So that's Kieren, and now I'm on to you, York.

**[02:36] SPEAKER_02:** That's amazing, by the way.

**[02:39] SPEAKER_01:** Okay, York Rhodes the Third is the co-founder of blockchain at Microsoft. So York co-founded the blockchain work at Microsoft all the way back in 2015, the same year he brought Block Apps onto Azure. Over the decade that followed, he built some of the most consequential enterprise blockchain deployments in the world. His team's work on the Microsoft cloud supply chain used blockchain to digitize industries across many industries. Today, York is Director of Traceability at Microsoft, focusing on improving labor compliance across global supply chains, is the co-founder of the X402 Foundation, which is building the standard for agentic commerce on crypto, and he is also a professor at NYU and co-founder at the NYU Ethical Tech Lab. I got through it, but that's a lot of stuff, and that's like the tip of the iceberg of the achievements.

**[03:42] SPEAKER_02:** I was going to say there's like a couple other things in there that we won't have time to talk about, like the BASE protocol and...

**[03:49] SPEAKER_01:** Yeah, exactly. I didn't even include that. You were one of the founding board members of the EEA. But so let's go right back to 2015. And I'll start with you, York. You co-founded the blockchain work at Microsoft, and when you were evaluating back in 2015, how did you choose Ethereum and how did you choose to work with us? What were those conversations?

**[04:17] SPEAKER_02:** So I went down this rabbit hole myself and just through my personal research, I arrived at Ethereum after just navigating through like, where are the smart people? What are they doing? It has to be more than Bitcoin. And that sort of got me to, okay, this is pretty interesting from a tech stack engineering perspective. And actually Marley Gray, who I co-founded the blockchain work with in 2015, had been working closely with ConsenSys already and you guys. And we divided up the work essentially in August of 2015. I took all of the partner relationships so he could focus on his financial services customers where he was already seeing some traction from some of the ones that were leaning in more deliberately. I mean, that's also kind of amazing, like where we are now at this point.

By the way, I knew I was early in the market. I had done innovation waves prior to this. I knew in 2015 that I was going to do this for eight to ten years at least. And so I was very deliberate in changing my LinkedIn immediately when I realized this is the next foundation wave that I'm going to be on. And it's been quite a roller coaster ride, as you guys know, but fun ride to be on. So yeah, I mean, at that time there was no other thing to look at really.

**[06:04] SPEAKER_01:** Not to name names, but other large organizations decided to build their own or do something in that direction. You guys really interestingly took that community approach by going to Ethereum.

**[06:17] SPEAKER_02:** Yeah, I mean, so that was also very much like where in 2014 Microsoft pivoted very much towards open source and seeing the value proposition of open source. And so one of the internal conversations that we had was, where do we want to spend our energy? Should we spend our energy trying to build a new blockchain from the ground up, or should we just embrace the ecosystem, which is something that Microsoft's always been good at, from the first time I was at Microsoft in 1992 to the current day? And that seemed like the most logical thing to do. There's a lot of interesting organizations and it was a vibrant community even in those early days. And I think in the first year after I brought one of my full-time engineering colleagues on board in early 2016, before we shipped Visual Studio Code extension for Ethereum development, we probably interviewed about 175 companies that year that were just in this very ecosystem in 2016, just looking for other interesting partners to partner with.

**[07:31] SPEAKER_01:** Yeah, that's awesome. So Kieren, take us back to that moment on your side. We were a very small team, five, six people still. We were still in ConsenSys. Microsoft said they want to work with us, but we had to really gear up toward making this happen very quickly. What did that require of you and the team?

**[07:56] SPEAKER_00:** Yeah, well, if I recall correctly, this is 2015 and we were announcing in London, let's say October, November, something like that, at Devcon 1. Everything was under wraps until then. Devcon 1 almost didn't happen. That's a different story for everybody. But there were some interesting times early on, and Ethereum looked anything but inevitable at that time. I guess I would say what we did really helped solidify its position from having good, strong organic momentum at that time to being a household name. So yeah, we got in touch with the team, we got spun up on the Azure infrastructure, and it took a minute to understand what an enterprise IT deployment looks like then. And it's quite different now, I'm sure, but there are...

**[09:01] SPEAKER_02:** It's a lot easier now.

**[09:02] SPEAKER_00:** It's a lot easier. The big thing was to get the software deployed at that time. Docker hadn't even really caught on at all.

**[09:15] SPEAKER_02:** Well, one of my colleagues, by the way, was responsible for the Docker Microsoft partnership.

**[09:22] SPEAKER_00:** Oh yeah. It's hard to think back. I mean, we were just running binaries at that time, primarily. So we did actually get a Windows Server build through, but most of the time we targeted Linux. And I think one of the big innovations Satya made at that time, to York's point, was the sort of operating system almost moved into the hardware. The cloud is one big giant operating system, if you will. And then Linux became almost, they became virtual machines sitting on top of that giant operating system. And it all kind of worked cleanly together. So mostly what we had to do just translated over and amounted to sort of packaging, putting things together, etc. And I did a live demo, and we made fun of the Brits a little bit because the Internet was not so good during the live demo. So I was very worried. We had a dividend demo set up where we named Marley as one of the recipients of cash disbursement. And that all went really great. And I think almost immediately, the next day, we saw a mild jump in the Microsoft stock price that can't certainly be attributed to the announcement, but...

**[10:51] SPEAKER_01:** Most of the Ethereum price.

**[10:55] SPEAKER_00:** Yes, that too. And just phone calls from big system integrators, banks, etc. We saw, yeah, maybe it took another couple weeks to get on the marketplace, but something like 200 companies at least launched instances, from medium to large. Typically there were a handful of startup types, but a lot of banks, etc. So it was symbiotic. I think Microsoft had all the customers, and especially, it's an interesting thing where big profitable corporate organizations are both often more conservative but more able to invest in innovation. They've just got retained profits to be able to deploy. So yeah, it's funny to see gigantic companies and it opened a whole lot of doors where you're getting pulled into meetings in midtown Manhattan that the Big Four set up and you're like, okay, this is cool, I'm 25.

**[12:02] SPEAKER_02:** Kieren, do you remember working on the DTCC?

**[12:06] SPEAKER_00:** Oh man, that one was a doozy. That was quite a... yeah, quite the organization there.

**[12:14] SPEAKER_01:** I mean, one thing I kind of want to touch on, because you have startup experience and you think of this giant corporation, but it really felt like startup. We were kind of two startups and Ethereum itself was a startup. So how did the teams work together? Do you remember any times when you had moments when you were like, oh, this is crazy, or this could be the start of a longer relationship?

**[12:46] SPEAKER_02:** I mean, one of the reasons I came back to Microsoft was because of Satya Nadella. And I really appreciated his embracement of open source and also how he was thinking about changing the culture of the company. And one of the phrases that he used a lot was, people should have a growth mindset. And this is really directed at enterprise employees at Microsoft and beyond. But growth mindset was two words that I very much could stretch the definition of, like, allow me to do the things that I thought needed to be done, which was really the intent of the words, and that it was trying to get people to speak up and do the things that you think need to be done. And so Marley and I did that. And we had a lot of, in some ways we had permission, but we also had to be willing to take that risk. And it's also one of the reasons why I was very deliberate. I knew, regardless of what anyone told me, that this would be definitely my next innovation wave. And so I was like, that's what I'm doing. I'm going to put that on my resume and on my LinkedIn publicly, and literally did it that August, because I just knew. And so for me, it was, we're doing this because I had had to make a decision like, am I going to stay at Microsoft and push boulders up the hill for a long time, or am I going to go jump into the ecosystem? And I had just returned to Microsoft recently, and so that was a very deliberate choice as well. And so I didn't want to just jump ship because all of a sudden there was this other interesting thing that was exciting and fun. And yeah, it was a bumpy journey. I mean, there were certainly times when people had called me up screaming and saying, we're talking to a major client here, what the hell are you guys doing?

**[14:48] SPEAKER_01:** Well, what do you remember from the early collaboration that we had with Microsoft? Kieren, I mean, you talked about DTCC, but there was a lot of...

**[14:59] SPEAKER_00:** I don't know if those NDAs expire or not.

**[15:01] SPEAKER_02:** Some of those are lifetime.

**[15:04] SPEAKER_00:** That one was hefty, right? We put a lot of energy together and that one was intense.

**[15:13] SPEAKER_02:** Oh, it's like an early layer two implementation, effectively.

**[15:17] SPEAKER_01:** Yeah.

**[15:17] SPEAKER_02:** I mean, it was like we had to do it to get scale. And if you look at what DTCC is doing now, if you squint, it doesn't look all that different.

**[15:28] SPEAKER_00:** Yeah. And to that end, so I can't recall who set up this meeting. It was with a big Latin bank, and might have been... I think the gentleman who said is not so good.

**[15:46] SPEAKER_02:** Was that in Brazil maybe?

**[15:52] SPEAKER_00:** Yes. I'm trying to keep it vague because, again, I don't know...

**[15:56] SPEAKER_02:** Yeah.

**[15:57] SPEAKER_00:** The state of all of the names and so on. But I remember, yeah, we were at Microsoft offices in Midtown, maybe on like a Friday. And I did some live coding exercise. I think Victor was there, but maybe Slazas was there, James as well. And I think you were there too, York, though I am not certain. It could have been like a Marley being in town one. And we sort of talked about some workflow within the bank.

**[16:26] SPEAKER_02:** Right. Yeah, I do remember that, actually.

**[16:28] SPEAKER_00:** Yeah. And we kind of coded it up and showed, we had at that time a little app generator just to kind of get people going, show them ideas quickly. It was like, yeah, can we get this going on Monday? We're like, oh, yeah.

**[16:41] SPEAKER_02:** But then imagine if we had Claude Code. How far...

**[16:47] SPEAKER_00:** But the feeling, it was a funny thing between this tremendous urgency...

**[16:51] SPEAKER_01:** But then it...

**[16:52] SPEAKER_00:** Yeah, real intensity coming out of these organizations. There was excitement, there was fear. I remember at the... we had a meeting, this one you weren't involved with, York, but kind of similar feeling with a different innovative big Latin bank, during the DAO hack. And we could talk about nothing but the DAO hack, even though we were kind of going through, talking about all the enterprise settlement use cases, etc. But it's taken some time, right? And we had been, Microsoft too, us heavily on the consortium permission side, serving all manner of... and that's still there, but much less. The corporate energy has just shifted towards, can I use this in practice? And we've got multinationals moving pretty good volumes of stables around the world finally. It's gotten boring. And it's gone from this, like with the cloud, "I'll never put my data on someone else's computer." There's been a pretty strong acceptance of the kind of public chain format, I would say, with still contexts in which the enterprise won't put data out there. But people act now as if, of course, it was always going to end up like the Internet and everything would interconnect. But really the customers would just absolutely refuse and demand the most lockdown flavor possible at that time. And yeah, I think...

**[18:29] SPEAKER_02:** Certainly in the early days. It's just, to your point, fear and unknown, which is very common in almost any innovation wave. It's like, how is this going to impact me? Should I be paying attention to this? How is this different than how I think? And I think frankly, for engineers before the AI wave, this fusion of cryptography with digital value and coding together scared the living shit out of traditional engineers. And a lot of traditional engineers who didn't go into finance made a choice not to go into finance because they didn't like the value thing. Right? And so you had a lot of engineering trepidation as well, in addition to just conservative corporation trepidation. And so it was a lot. I think what we did, and whether it was right or wrong, I think what we were trying to do, certainly from a philosophy perspective, was it's an early market, we need to help people get comfortable with it. The only way they're going to do that is if they're not being exposed, essentially. And that was really, I think, the intent, at least from my perspective, in the early journey of trying to enable these cloud spin-up infrastructure. Long term, I was always a huge believer that the value case of distributed decentralized governance, censorship resistance, credible neutrality were the thing that in the end would win. And I think that is what you see now with banking, where they're like, okay, well, if I'm going to put my value somewhere, it has to have credible neutrality.

**[20:21] SPEAKER_01:** Yeah. And on that point, there's been this, people are talking like RWAs are a new thing, but really we were doing supply chain projects where we were tokenizing real world assets back from the beginning. And York, I know you guys in the Microsoft cloud supply chain won a Gold Alexander Hamilton Treasury Award for a project. If you could talk a little bit about that project.

**[20:52] SPEAKER_02:** Yeah, yeah, absolutely.

**[20:54] SPEAKER_01:** Of all the other blockchain enterprise projects that failed.

**[20:58] SPEAKER_02:** Yeah. So this was a project that I started as a collaboration with the cloud hardware supply chain team in probably around 2017, 2018. And the theory was, how do we get better traceability effectively in our high-value assets in our cloud supply chains? And so we were... the early project essentially started with like nine key suppliers that were known suppliers. And so we brought them into essentially a distributed system on an Ethereum tech stack called Quorum, which was what the Enterprise Ethereum Alliance sort of started with as the preferred tech template.

**[21:50] SPEAKER_01:** Yes, I remember. We put in a lot of work on that stack.

**[21:53] SPEAKER_02:** Yeah. And so this project basically became a foundation for infrastructure in our supply chain. And the goal that was published in a Gartner Award that we also got for the same project earlier than the Alexander Hamilton Treasury Award was specifically, we believe that there was a $50 million ROI per year on getting better visibility to the data underlying all these assets. And before we even did that calculation, we started working with the Microsoft finance teams and treasury to basically get financial controls around what we were doing in the supply chain by leveraging the signal we were getting out of this blockchain infrastructure. And that gave us a wholly different ROI, which was based on cost of capital. Because we had the signal from every transition point of these high-value assets, we were able to actually transition to a just-in-time payment mechanism based on that signal. And that's where effectively the Alexander Hamilton Award came from. Because cost of capital on cloud infrastructure is very high. And I think the typical number that people use as a SWAG is like 11% of capital. So if you can recover cash in hand on the types of volumes that you're doing in a cloud provider year over year, the cost of capital benefits are quite substantial.

**[23:36] SPEAKER_01:** That's amazing. And Kieren, we worked on a bunch of really the first RWA tokenization projects too. How do you think that affected our product and how we had to evolve STRATO to meet those needs?

**[23:52] SPEAKER_00:** Well, let me continue on memory lane for a little bit. I'm trying to remember exactly where this was. We went to something like Microsoft Sales Kickoff, talked about the BHP case.

**[24:04] SPEAKER_01:** Yep, yep.

**[24:05] SPEAKER_00:** I think it was in New York.

**[24:07] SPEAKER_01:** I think that was in... I think that was in Redmond, actually.

**[24:11] SPEAKER_00:** It could have been in Redmond. We went, we've been, what, four times to Redmond, something like that over the years? I can't quite recall.

**[24:17] SPEAKER_01:** Well, when I lived in Vancouver, I'd make that drive.

**[24:20] SPEAKER_00:** Yeah, you would drive. It's easier. And so I think for a little bit the BHP Billiton case was way out ahead. So yeah, this was BHP Billiton, often the world's largest mining company by market cap, probably is right now, but I haven't checked today.

**[24:37] SPEAKER_01:** We should say physical resources.

**[24:39] SPEAKER_00:** Physical mining. Yes, physical. They're not mining Bitcoin, maybe a little bit now, who knows. They have, of course, big commodity trading desks. So after this project I was told that everyone started buying and trading ETH. But so yeah, we did deploy on Azure, BHP being a big Azure customer, and it was much earlier but much as York described, a traceability mechanism for their core sampling. So basically when they drill into the earth, they assess viability by sampling, and that tells them where to invest. And these samples go through a pretty complex supply chain, maybe not quite at a data center level. They're a long-lived asset that's very valuable, that touches lots of different parties, and that's what you find.

**[25:29] SPEAKER_02:** Yeah, so just tune in, billions of dollars valuable.

**[25:32] SPEAKER_00:** Yeah, exactly.

**[25:33] SPEAKER_01:** Yeah, exactly.

**[25:34] SPEAKER_00:** And so, actually a bunch of people who worked on this went on to do NFTs. So there were the Trium and the Euler Beats project at ConsenSys. The founders of SuperRare were on our side working on that and then continued on into NFTs. We stayed sort of on the corporate side for a long time but continued to deploy very similar infrastructure in agriculture, oil and gas, etc. But to my knowledge, it really was the first — we're not banks moving representations of dollars or ETH around kind of use case. It was the first one that contemplated something physical at that scale. So yeah, and it's infused everything. I mean, I think we still have, in part even before, we always had a... okay, we know this tech is going to be big. How do we make it accessible? Who do we make it accessible to? We had the thesis early on that businesses were going to be first, and we were right in a way. Early Internet, right, who did really well — people sold databases to Internet companies, etc.

**[26:52] SPEAKER_02:** And I think one of the guys from BHP Billiton went, I think he started a gaming company also. I forgot his name, I think.

**[27:01] SPEAKER_00:** Yeah, I'm blanking too. But yes, there was a whole, it really created a lot of... that one big deployment. So yeah, it's... I mean, this has always been our focus, the rubber meeting the road on the technology where kind of normal people can get into it, touch it and feel it. And so yeah, I mean, we still do metals now, and I guess this is after they've been mined, and focus...

**[27:29] SPEAKER_02:** Yeah, we should talk about where you're getting your raw materials from.

**[27:32] SPEAKER_01:** Yeah, yeah, exactly.

**[27:35] SPEAKER_00:** There's a lot of interest also in tokenized proved reserve curves. We haven't done anything with it yet, but I hear a lot in the market about it too. But yeah, it's been the thread the whole time. We've been kind of bridge builders focusing on adoption. How do we get the technology in the right hands in a tangible manner that people understand well?

**[27:57] SPEAKER_01:** And on that note, tokenized bonds are very exciting right now. York, you did one of the first big tokenized bond projects with the World Bank blockchain bond. What did the team have to do to create that and be a first mover in that sort of area?

**[28:20] SPEAKER_02:** Great question. Just one second. So that project was very specifically done by the World Bank, from the World Bank treasury specifically. So that was actually kind of a cool project to be able to work with the treasury of the World Bank. And the reason they did it was because they have a philosophy that they can catalyze the market and help the market understand that there's something interesting. And in this case it had to do with blockchain that can be a value proposition down the road. And obviously we're seeing that now from a financial markets perspective. And so they were working as the... basically the way the World Bank treasury works is they'll mandate a bond, and they were working with Australia as a geography that had better regulatory posture. So they were very specific in terms of their work with Commonwealth Bank of Australia. Commonwealth Bank of Australia basically built the full tech stack on Google Cloud, and World Bank production cloud was Azure, Microsoft's cloud. And so they asked me to do two things. One, help them get a production implementation running on Microsoft cloud, and two, do a full tech stack pen testing, security, all the way down to the smart contract. So it was probably one of the earliest smart contract audits as well, surprisingly. But basically I pulled in some security folks who knew how to do full tech stack infrastructure security testing, front end security testing. And then Kale actually did most of the smart contract auditing by hand. I think there were about 24 smart contracts in there. We were using OpenZeppelin obviously, and the... I think she was the treasurer of the World Bank, really amazing woman. She is now at Oxford University in the UK. And she basically told the team, well, this was like, I think we started working with them in May, and she was like, well, we're going to go live in August, just so you're aware. And so it's basically like a sprint from whenever we started to essentially get to August 1st with confidence that we were going to be able to do this. And I actually had to teach one of the wonderful guys who actually took the lesson very well. I think his name was Peter, who was doing infrastructure work at the World Bank. And I was like, dude, you cannot deploy this manually. The world does not work that way. You want to be able to put it in a pipeline and have it redeployable. So I also taught them how to do full CI/CD pipelines so that they had a tech stack which they could tear down, stand up...

**[31:22] SPEAKER_00:** Re...

**[31:22] SPEAKER_02:** Stand up. Right. Keep it working. So that was part of it as well, which was also, I guess, added bonus. But yeah, so I think it launched August 14th in 2018. It basically was an entire bond. The entire... it was a private blockchain built on an Ethereum stack, but it was distributed governance, obviously, among the parties. And as I mentioned, like 24 smart contracts that represented the entire bond and all of the positions on the bond, the investments, the sales and everything. It was all essentially a fully abstract digital asset. That was... if the blockchain went away, that was it. It was gone. There was no other record. There was a reference in Bloomberg terminals that it existed, but that you had to go to the ledger.

**[32:17] SPEAKER_01:** Right.

**[32:17] SPEAKER_02:** In order to... the blockchain ledger, in order to see the details. Great project.

**[32:23] SPEAKER_01:** Yeah. I mean, but all of those elements are still in play today, right? So that's why...

**[32:28] SPEAKER_02:** Yes.

**[32:29] SPEAKER_01:** I think it's just exciting that we were trying to figure out these early components and how to make it work. And we see them being reused in all kinds of different ways.

**[32:39] SPEAKER_02:** Yeah. I mean, also, the funny thing is, like, 2018 when the treasury was envisioning this with Commonwealth Bank of Australia and we were envisioning it and we're signing up for this work, you're like in a startup mode. You're like, yeah, I'll do it, sounds great. Like you have no idea what it's going to entail, but you're going to get there.

**[33:07] SPEAKER_01:** I think that is the key element. When you're doing something that is so blue sky, it's like, well, I think we can do that, but not really sure.

**[33:18] SPEAKER_02:** Yeah, I think we can put a blockchain into production that has a hundred million dollar bond on it for the World Bank. Yeah, sure. In 2018. Yeah.

**[33:28] SPEAKER_00:** Well, the funny thing, right, there's such a big push to get it through once. And if you get it through once, you could probably do a whole lot more too. On the back end, you just kind of hit the button a couple more times.

**[33:43] SPEAKER_01:** So Kieren, a lot of this enterprise work on the Block Apps side we were talking about was done as that kind of company. And now our new project is STRATO, focused on DeFi for hard assets like precious metals. What was the thinking behind the evolution from the enterprise work to more of a DeFi hard asset platform?

**[34:05] SPEAKER_00:** Yeah, I was going to say there is actually a continuous thread. It kind of went in two phases. So there was our kind of corporate NFT-ish consortium thread. You have interesting corporate assets moving across companies in a supply chain, actually some digital or digital with a physical linkage, some the majority physical with a serial number, that kind of thing. And we sort of realized, especially with the pandemic, there was a big slowdown in innovative corporate efforts in IT, I would say. People were scrambling to get Zoom set up and that kind of consumed all the oxygen for some time. And so there was a good maybe year there where everything was... projects continued but were slowed. Then the market kind of came back some. But also I would say the huge run-up in crypto asset values in the early 2020s started to pull some of the oxygen out of the air. For instance, folks were paying Starbucks to use their products in reasonable amounts.

**[35:23] SPEAKER_02:** Right.

**[35:24] SPEAKER_00:** And so the, let's charge a bunch of people subscriptions for this consortium model got harder because everyone wanted to do the opposite. They wanted to pay the corporate so that the token would go up and so on.

**[35:38] SPEAKER_02:** Yeah, there was definitely a lot of brand trading.

**[35:51] SPEAKER_00:** So the first set of continuity is like, okay, let's just focus on the assets. So maybe there was always also this problem of, am I going to join your blockchain, you're going to join mine. They could do consortia together. But it was just a hard lot of setup, right? Like legal documents, they all had to be kind of the same. It was just excruciating. So it's like, okay, what if we just had the blockchain up? How would that work? And we did find... so we then just focused on asset tokenization still with the NFT flavor. So carbon offsets were very big. In fact, all of those big corporates at that time, in part there was some top-down pressure to do so, were buying offsets kind of as just part of their corporate citizenship. Folks like BlackRock were telling them to do it. The SEC strongly intimated that they should think about their footprint and all that sort of thing. All these things were much more intense in Europe but happened here also in the US. So offsets were interesting.

And there was that kind of big wave. Some of it's surviving today, but collectibles, Pokémon cards... we did actually a lot of collectible shoes. We had a fair amount of volume in collectible shoes. And precious metals we sort of stumbled upon. It was just an idea and it really worked well. There was a lot of demand for precious metals. And at first we thought people would want to buy and sell them, and they do, but what they really want is credit against them. So we kind of bolted that on our more NFT flavor of our product. But it was not perfectly smooth, and we spent then the better part of the year kind of replatforming to the more DeFi-native flavor. And it's really worked. The deposits are kind of going up. And if you think about it, the set of collateral assets in the real world is just much larger than what exists on chain. People have been saying this for a long time and the question is, will they come on chain? And why and how? And I think the answer is actually the machinery of DeFi, or some version of it, is really magical. You can just create value not from nothing, but like MakerDAO invented the idea — you put some ETH in and you can borrow a synthetic dollar against it quickly, no questions asked, modest interest rate. And if you set things up the right way, it really behaves like a dollar. That's kind of amazing. If you take that insight and you carry it through — okay, what about Treasuries? That's what Circle and Tether really do. They're tokenized Treasuries. They just don't... the user doesn't hold the Treasuries directly and therefore doesn't get the yield. What about other assets? And so great business.

**[39:03] SPEAKER_01:** Yeah, yeah.

**[39:06] SPEAKER_00:** Some are hard. If they're very unique, like homes, it's a little challenging, you have to assess them. But gold and silver, they've been money for as long as there's been money. So it's been kind of like a real winner for us. And we do lots of other stuff too. So we have some of the X stocks now owned by Kraken. They're the tokenizer on the platform. We take ETH, we'll take DeFi-native Bitcoin. It's really any good liquid asset that you want to keep — we extend credit against. And this has been, there's just tremendous demand for this. So kind of a meandering journey. But again, the whole time, just like, what are people going to use? What do they want, really?

**[39:53] SPEAKER_01:** Exactly. Well, and on that note, I want to just touch base. We've talked a lot about the historical perspective, but what is exciting you most about the future of the blockchain space? York, I know you're working on X402 too, bringing together AI and crypto. What are the most exciting developments happening in the blockchain crypto space now?

**[40:19] SPEAKER_02:** Well, I think, first of all, what's amazing about the crypto community is they lean into risk and lean into innovation. And so it's not surprising to me at all that this community has been working with things like OpenClaw and all of the variants of that. And also, I don't have any real data, but it feels like it's a natural thing for people to be leaning into this innovation wave of AI and agents. I think the X402 Foundation, being in the Linux Foundation, was really smart because it's a great place to have that sort of neutrality around the software stack. We've seen that with a number of the other stacks in the Linux Foundation, like Besu, for example. And that was really, to me, it was an inflection point of a lot of different standards, quote unquote, "standards" forming. If you think about what were the standards in the AI space, we really started with MCPs, right? Then you started with the commerce protocols like Google's commerce protocol, which wasn't necessarily... it was really aligned to how Google thinks about commerce. Not a bad protocol, but another protocol. And then you had MPP, which does something different, and X402, but also A2A. So there's all of a sudden this proliferation of what seems like a bit of a spaghetti-against-the-wall standards in both the commerce space and the AI space, some of which are really valuable. Like obviously MCP is extremely valuable in terms of the utility that it provides. And then X402 is a natural connection point between digital payment mechanisms — stablecoins and crypto — and can support legacy payment vehicles if there's a way to do that in a cost-effective, non-human-intervention way.

And to me, that's an exciting moment because I think it's also sort of foretelling the... and there's quite a few people who are writing about this. Including, I don't know if you watch the Nate B. Jones podcast sometimes. He's clearly recognized that this agentic wave is the thing, and that agents that are autonomous need a mechanism to pay for things. And how does that happen? And so I think one of the things that he calls out, actually quite interestingly, in a recent podcast that he did in the last month, specific to this, is that if you look at the companies that sort of independently had this realization, it's a combination of Cloudflare, Google, Coinbase. And all of them were sort of independently racing towards the same place. Not surprisingly, Cloudflare and Coinbase are part of the X402 Foundation, as well as Google actually, and Microsoft and Amazon, logically. Yeah. I mean, that to me, that's exciting. AI in general is exciting. I mean, I've been coding for the first time in a long time and that is like, I feel like I'm in the beginning of my career again.

**[43:46] SPEAKER_00:** Right.

**[43:46] SPEAKER_02:** That's just where we are. It's like this fascinating unlock for people who have knowledge of how to build and ideas and now have this tool that gives you this unlimited resource, in some ways. It's just an amazing time to be in the market.

**[44:06] SPEAKER_01:** Yeah. And Kieren, what are you excited about? Future ones?

**[44:10] SPEAKER_00:** Oh, man. Well, let me touch quickly on York's comment. I'll bring it home. So one thing that's very interesting about agents, especially the latest models and good harnesses, they have this way of routing through... like, I give the agent a goal, and sometimes you find it go in there and start editing config files and yada yada yada, and you kind of turn around and you're like, whoa, whoa, whoa, that wasn't quite what I intended. You did... they didn't need to log in as root and... They have this way of breaking containment a little bit. Right? And they still have a hard time with captchas. I'm sure they're going to get there. But sometimes I have my OpenClaw, it sends some emails for me from time to time. It has a very low limit credit card, believe it or not. But the Internet has been set up to be very bot-unfriendly, and now we may want the Internet to be somewhat bot-friendly. And so yeah, crypto just works now. You can get through things like... in fact, websites should just start taking a couple of fractions of a penny in stables instead of requiring that captcha if they don't want to be DDoS'd. And I think we'll see something like that.

**[45:33] SPEAKER_02:** Right.

**[45:33] SPEAKER_00:** The... it is this, there's this tremendous... once in a while I do pilot our product, like move money with agents. I don't do it often, give them temporary credentials and so on. But it's one of the altogether strangest times in history. Maybe the strangest. And very exciting. But bringing it back to us, we're getting to feel like, a few years ago there was true believers and hope and "we're all in this together." And now it's getting to be a competitive, mature industry that's serious. And I think we still have 10 or 100x adoption to go from here. Maybe not... I'm not speaking about market caps and prices and all that sort of thing. And this is maybe the good part. There's a lot of fun from the early days, but there's a whole lot ahead of us. I remember, York, you were a question in 2014, 2015 when we first started circling, and 2015 when we started going, we thought we were too late. Probably a lot more ahead.

**[46:52] SPEAKER_02:** No, no, I agree with you. Like, this is an exciting time. I think the Internet's changing and this technology is at a really interesting inflection point in that happening. So yeah, it may get a little more boring, but I think it's actually just the start of the boring.

**[47:15] SPEAKER_01:** Yeah. On that note, and on behalf of the community, I want to thank you both for continuing to build and drive these efforts. I think, having the front row seat, I know how hard it's been to get to where we're at, and like you said, there's still a long way to go. Where can we find out about your work and what you're doing? York, where can we learn about all the interesting things you're working on?

**[47:39] SPEAKER_02:** Yeah, I mean, I would say I've been posting more deliberately on LinkedIn than others, but I also post on X still under York Rhodes, and the only... you'll see me there. York Rhodes. And on LinkedIn, the same thing. Although just make sure it's the Third, because my son is in the industry as well.

**[48:04] SPEAKER_01:** Yes. And Kieren, where can people find out about all the things you're doing?

**[48:09] SPEAKER_00:** Yep. So STRATO Nexus for the project, app.stratonexus for the app. And I'm KJamesLubin on Twitter, probably most active, a little bit of LinkedIn. We have a Telegram too that folks can join.

**[48:25] SPEAKER_01:** Okay, well, thank you very much for joining, and I know we're overtime already, but thank you for your time today.

**[48:31] SPEAKER_00:** Great to see you virtually, York. See you soon, I hope.