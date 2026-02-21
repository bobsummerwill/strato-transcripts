**[00:01] SPEAKER_00:** So, hello and welcome to Early Days of Ethereum. I am delighted today to be joined by Fabian Vogelsteller. Is that the correct pronunciation? Vogelsteller.

**[00:01] SPEAKER_02:** More like an F. The V is more like an F. Yes, right.

**[00:01] SPEAKER_00:** Very Germanic pronunciation that's not going to come out of my mouth. So, great to see you. We saw each other at Devconnect in November, I think, for the first time for quite a while, and had a good catch up there. But hello. What were you doing prior to wandering into the blockchain world?

**[00:58] SPEAKER_02:** So, okay, let's start from the beginning. What I was doing before blockchain, I was actually a web developer. I started out building websites since I was 14. Findura, the name that I have on Twitter, is actually the name of the content management system that I built, I think, in 2005. And it just happened to be turning into my second identity. So I have two identities on the internet, Frozman and Findura. In GitHub, I'm Frozman, and that's also my GitHub history with Ethereum. And Findura is my online one.

I was always interested in the cutting edge of the cool internet stuff in the 90s. Building my first websites in the late 90s or early 2000s, and following the whole evolution of the internet with HTML1 and 2, CSS1 and 2, and JavaScript coming in. So I mainly did web development, but I studied media design. I didn't study anything with coding. All the coding is autodidactically learned. Honestly, even when I joined Ethereum, I had no clue about bytes and how to manipulate bytes. I still don't, actually.

**[02:37] SPEAKER_00:** You didn't have your computer science background.

**[02:42] SPEAKER_02:** I don't have any computer science background. I don't know what I'm doing on the computer; I just know how to interact with high-level languages. And now I only know how to speak to AI and to my team. Well, that's all you need! Things changed.

I got really into web development. I built a lot of websites and a content management system in PHP. I built a flat file-based content management system, meaning it didn't need a database. The whole idea was about the independence of hosting providers. If I want to move from this hosting provider to the other, migrating databases back in the day was a nightmare. If you build a flat file-based thing, you just copy the whole folder structure over to the other server and it works. And it did. That was what the Findura CMS did. I mean, obviously, who uses PHP today? Well, Facebook does.

That project really helped me do a full project front to back. Then I got more into JavaScript and got really excited by Meteor.js, which was one of the first reactive JavaScript frameworks. That was before Angular, before React. It was the first time where you could just write JavaScript code and HTML, and when you update the local state, the HTML got re-rendered natively. It was super magic. I got really into it and even wrote a book about it. I have it right here. Honestly, I would never read a tutorial book, to be honest, but I wrote one!

**[05:04] SPEAKER_00:** I don't think people even read books anymore.

**[05:06] SPEAKER_02:** Yeah, I mean, it was so much work to do this. They reached out to me, and my ex-wife Marjorie encouraged me, so I thought, why not? In the end, it was literally four months of waking up very early when I had a one- or two-year-old kid. I had to wake up at five to write three or five pages, and then go to work. It was intense. You get an hourly rate of like 10 cents, so I made totally no money.

But it's reputation. And in a way, I think that's also what got me into Ethereum. What is writing single-page apps with Meteor? What is a dapp? It's a single-page app. That's the whole point. It's an app that literally runs in your browser and doesn't require a back-end. I actually built a tool that allowed you to strip out the server part of a Meteor app so you can bundle it as a local app. It was quite a popular repository called Meteor Build Client, and that's what I used for dapps in the early days in Ethereum too.

**[06:44] SPEAKER_00:** So, is Meteor still an active project? Is anyone using Meteor still?

**[06:52] SPEAKER_UNKNOWN:** Yeah.

**[06:53] SPEAKER_02:** Yeah, I totally think so. I don't know how frequent they are.

**[07:07] SPEAKER_00:** I haven't checked it out in a long time. But I mean, it's quite a revolution at the time, the single-page app.

**[07:15] SPEAKER_02:** It was literally the first proper framework. It just solved the whole thing from account creation to reactive DOM updates to server-client synchronization. It was magic. It blew a lot of people away. And then all the others, React and so on, were answers to this. And then React brought it back to the weird way of mixing code and UI in the same files, which I already found very bad in PHP times.

**[07:52] SPEAKER_00:** Right. And then I guess you found your way into the Bitcoin world in some form?

**[08:02] SPEAKER_02:** Yes, so in March 2013, I heard about a Canadian wanting to sell a house in Bitcoin. I thought, "Wow, what's that? Somebody's selling a house in a currency I've never heard of." That really led me down the rabbit hole. This was literally when Bitcoin hit $200. I saw there was money to be made here, and I was a student with no money. But very quickly, I understood the fundamental power of the technology.

It took me about a year to really understand how it fully works. I literally had an epiphany every month where I thought, "Now I know how it works." It took me a year to really rewire my brain from knowing servers and frameworks to understanding blockchains. So I was in the space in 2013. When right after I joined the Bitcoin community, the first altcoin, Litecoin, came around. There were a lot of projects created trying to imitate Bitcoin or do alternative versions. I also got really into Mastercoin, the idea of just writing onto the Bitcoin blockchain rather than creating a separate blockchain.

**[09:49] SPEAKER_00:** And you were in Berlin, right? Were you going to meetups, or did you find fellows online?

**[09:57] SPEAKER_02:** There were really no meetups at the time in my region. Later in 2014, there were some meetups. So I heard about Ethereum, and I immediately felt this is a really powerful approach, but it also sounded so unrealistic. I looked at the white paper—I never really read the Ethereum white paper fully, I just skimmed it. But I listened to Vitalik and the early things floating around, and I knew this was it. The idea of making a computation machine on the blockchain made total sense. I just thought it would be very hard to do. I didn't give them a lot of chances to pull it off, but then they did, and pretty quickly.

It just happened that I was at a Bitcoin meetup in Berlin, I think the first one I ever attended. They wanted to open a Bitcoin Center Berlin co-working space. I think it was August 2014, literally days before the Ethereum presale started. I met these guys from Ethereum there. In this case, it was Aaron, who did the accounting at the time. They told me they were going to open an office in Berlin, and that there was some news coming out next week, but they couldn't tell me. I was already following Ethereum, waiting for the ICO.

So when it happened, I took all my Bitcoin at the time, which was 12 Bitcoins, and converted them into ether. People today think 12 Bitcoins is a lot, but they were literally worth like $600 at the time. I put pretty much everything into ether. I knew this was going to be big. This was also the first project where I thought, "I would love to work for this project because it's not just about finance and wallets." Every Bitcoin startup at the time was just about creating a wallet.

Six months later, I got an email from a recruiter saying Ethereum is looking for a C++ developer. I was not a C++ developer—recruiters don't check GitHub! But I knew they were hiring, so I went to their office in Waldemarstraße. I chatted with Aaron again. I realized they were just building the nodes and assuming people would build on top of the stack. I knew how to build single-page apps, and I felt that was exactly what they needed to show what a dapp could be. So I told Aaron to just ask around internally.

They had a Skype group that functioned like today's Discord. Alex Van De Sande, who had come on board as the UX designer just a month before me, had this whole idea of creating the Mist browser concept. When Alex heard there was a guy who could build single-page apps, he thought I could be the person to help build it. I assume he convinced Jeffrey Wilcke. Jeffrey tried to call me, but I was on holiday in Turkey and didn't pick up. When I came back, I called him back, and I talked to AVSA. AVSA wanted to hire me to help build his idea, though Jeffrey was skeptical. He probably thought, "What can a JavaScript developer do here?"

**[14:54] SPEAKER_UNKNOWN:** Probably.

**[14:55] SPEAKER_02:** What? JavaScript?

**[14:57] SPEAKER_00:** Cannot work. So you started in January 2015. I guess this discussion would have been in December 2014-ish.

**[15:07] SPEAKER_02:** Yeah, it was mid-December. AVSA said, "Hey, can you start in January?" Jeffrey really wanted to test me, so he threw a really complicated task at me, probably hoping I would fail so they could get it over with. He told me to build a chat app for the Whisper protocol. In Ethereum, the Web3 vision was the network, Swarm for storage, and Whisper for communication. By the way, I only figured out later that Web3 literally meant exactly those three things. Fun fact, I always just thought, Web2, now we go to Web3.

**[15:54] SPEAKER_00:** Probably both, right? It's kind of a bit of a joke that you've got both. I was looking at the timeline; it was November that Alex had done his Mist concept presentation. So that was really quite fresh.

**[16:14] SPEAKER_02:** He had the idea, and they were working on it in early December. Yann Levreau, the French guy who later worked on Remix, had built an early version of the Mist browser in C++, called Aleth browser. But it was barely working, and the connections were not figured out. They realized quickly that was not the way to go. That's why Alex saw an opportunity with a JavaScript single-page app approach.

**[17:02] SPEAKER_00:** You'd had AlethZero as well, right? I guess that was the very first Ethereum thing. Maybe that's what you were thinking of with Yann?

**[17:27] SPEAKER_02:** No, AlethZero was that really ugly programmer tool, like a mission control interface. Anyway, Jeffrey told me to build a chat app on the Whisper protocol. So I got dropped into this novel tech, no documentation, absolutely no idea how this stuff worked. It was crazy. But because I knew how to build reactive single-page apps, I worked with Yann to get the endpoints I needed from the node. I built a chat app where you could filter by topics to see all messages or just follow specific threads. It was basically the thread concept of Discord in a tiny app, and it connected to your wallet in your Geth node.

I think Jeffrey was quite impressed, and it gave him confidence that I could do it. What's crazy is we literally built the first working version of the Mist browser in three months. We released it alongside the mainnet with the Ethereum Wallet on July 31st, 2015. So basically six or seven months later, we released the first Mist browser. Everything needed to be figured out. Initially, it felt completely impossible. I thought there was no way I was going to figure it out; it was completely over my head. But I pulled it off.

I had to touch every single point. I worked with the RPC API, which was messy—sometimes returning hex, sometimes not. Because I'm a Virgo, I immediately tried to fix things. I basically battled with Gavin Wood to fix and standardize the endpoints, because once we launched the mainnet, that stuff couldn't easily change anymore. Then I had to get into Web3.js, which Marek Kotewicz was working on. I contributed significantly to Web3.js because we had to integrate it directly into the Mist browser. So I was the first real user of that library.

We had to make everything up. Because I built the piece that put the node, the dapps, the Web3.js, the RPC, and the UI all into one app, I had to talk to everyone. It was challenging. I also realized Gavin's team and Jeffrey's team were a little disconnected. There was a little battle going on about who determines which feature and how. I realized that if we keep doing this, it's going nowhere. Jeffrey's Go team was a bit more open, whereas Gavin really wanted to keep his C++ team tightly controlled and didn't want us cross-communicating. But I found backchannels to make them sync up. I guess Gavin didn't like that, but it was necessary.

I was in this crazy position: hired by the Amsterdam team while sitting in the Berlin office with Gavin's C++ team. As the guy working on the front-end, I was the translator and connector. I had to ensure the Mist browser worked with both the C++ client and the Go client. It's truly amazing how much the dapp tech stack was completely invented and built in those first six months before the network started.

**[23:33] SPEAKER_00:** Yeah. I was just looking at the timeline: September 16th, 2015 is when the first developer preview of Mist went live. You were really the first person building one layer up. All the prior efforts were just about the clients.

**[24:18] SPEAKER_02:** To be fair, the first dapps were probably built by Gavin and Jeffrey, but they used their own local clunky stack. I built the first generic dapp browser capable of running any JavaScript app to connect to the blockchain. Alex and I built the Ethereum Wallet, which was the first real, designed, cross-client functional dapp on Ethereum.

**[24:58] SPEAKER_00:** Looking through old videos, there was a talk in London in October 2014 where Jeff and Gav demonstrated an on-chain DEX order book. They had GavCoin and JeffCoin. So they did have some cross-client capability, but you really built the UI layer.

**[26:19] SPEAKER_02:** For the chat app, I mainly used the Go client because Whisper on the C++ client wasn't fully working yet. At the time, the idea was that the client would host everything: Swarm, Whisper, and the network. Obviously, Swarm never fully worked in there, and neither did Whisper, which later got taken over by Status and transitioned into a different protocol.

It's foundational. People really misunderstand two things: first, that Ethereum was generic from day one. And second, how many of today's ideas were completely present back then. If you watch the Mist browser concept video from Alex, we hadn't even built half the stuff in that video, but ideas like Universal Profiles and smart contract accounts were already conceptualized. Only now, 10 years later, do we actually have the foundations to make that video fully realistic. These ideas of decentralized Uber, DAOs, and DEXes were around since 2013. We are actually behind on what we originally envisioned.

**[28:32] SPEAKER_00:** You had that cryptocurrency 2.0 phase at the start with Mastercoin. I guess there was a thought initially that everything would just be built on Bitcoin.

**[29:18] SPEAKER_02:** Back then, it was all Reddit—Bitcoin Reddit. Ethereum was the first real challenger to the status quo, and it split the community into Bitcoin maximalists and people willing to explore other chains. Even some of my developer friends completely refused to look at Ethereum because they thought Bitcoin was all you would ever need. I went to a Bitcoin meetup recently, and it was like a time capsule. The exact same discussions—miners, block sizes, basic stuff that has been figured out 100 times over on Ethereum.

**[31:01] SPEAKER_00:** Speaking for myself, I looked at Bitcoin and it was boring to me. "Okay, you can do payments. Great." But a platform where you can build apps? That was interesting.

**[31:47] SPEAKER_02:** For me, the money was cool, but it was really the power of a technology that no one could control, sitting above human influence, built entirely on consensus. It's like a hydra with 100,000 heads. It was fascinating, and I'm still super pumped about it. I just never thought mass adoption would take this long, to be honest.

**[32:49] SPEAKER_00:** Were you traveling back and forth to Amsterdam?

**[32:59] SPEAKER_02:** Rarely. Amsterdam was more like a legal hub. We were all over the place. I worked mainly with Alex, who was in Rio. We eventually hired a few more people from there. But I also worked closely with Marek Kotewicz and Christian Reitwiessner in the Berlin office. Yann Levreau and Lefteris Karapetsas were also sitting across from me in Berlin. Christoph Jentzsch would visit to do cross-client testing scenarios.

The Berlin office naturally functioned as the main Ethereum hub. It was never officially meant to be, but it had the most people. People like Dominic Williams just showed up before Dfinity was a thing. Gustav Simonsson, Felix Lange—Felix actually lived right across the street. And because I was one of the more social developers and worked on the front-end, I usually ended up talking to anyone who randomly walked into the office. The protocol developers were completely focused internally.

**[36:01] SPEAKER_00:** You missed Devcon 0, but you went to Devcon 1 in London in November 2015. EIPs and token standards were just starting. How did that evolve?

**[36:47] SPEAKER_02:** The whole standardization process started when Vitalik created a GitHub wiki page to draft token standards, an ENS-style registry, and maybe an early DEX. We debated the early version of ERC-20 there before Devcon 1.

At Devcon 1, I was on a panel about standardization. We were debating whether metadata should go directly into a token contract or into a separate registry, which is still a massive debate today—whether for ENS, NFTs, or AI accounts. When asked what I was interested in standardizing, I said "the proxy contract," which was my term for a smart contract account. It's funny because I later created ERC-725 and Universal Profiles exactly to solve that.

During that panel, Martin Becze, who had created the EIP repository, suggested we move standard discussions there instead of editing a single wiki file. That inspired me. So I went and created Issue #20. I formatted the discussion we had into a proper specification. We needed community consensus, and a GitHub issue was a much better structured way to do it.

I made a few changes to the ERC-20 draft—like reordering arguments in the transfer function—but the biggest debate was about the "authorized operator" function. I was actually against it. So when I deployed the very first test coin, the Mist coin, I left that operator function out. Fun fact, because it omitted that function, years later when people started trading relic tokens, my Mist coin didn't work on Uniswap! They had to wrap it. I had just handed those out to random people for years, and now they actually have a market cap. That was the first ERC-20 token that fit the spec, minus the operator function.

**[42:39] SPEAKER_00:** There's a deployment of that out there launched by rfiki, based on Vitalik's repo, called CurrencyCoin. The on-chain history preservation is amazing.

**[43:18] SPEAKER_02:** The crazy thing is the code and transactions are still there, practically like relics. I deployed the Mist coin probably exactly a week before I formally proposed the ERC-20 specification. We needed it to test token implementation in the wallet.

**[44:07] SPEAKER_00:** It might well have been for your Devcon 1 presentation demo.

**[44:13] SPEAKER_02:** Devcon definitely pushed us to get features done, but the token functionality was still very early. We knew people wanted to make tokens, but it wasn't a primary emergency focus for the Wallet yet. It really wasn't until the ICO wave hit that things went completely bananas.

**[45:07] SPEAKER_00:** I guess you had no idea that the ERC-20 standard would have so much sticking power.

**[45:14] SPEAKER_02:** No one could have known. I knew people needed it because Colored Coins existed on Bitcoin, but honestly, I found the idea of creating random tokens for random stuff kind of boring. What is the value? If you look back, most tokens simply didn't make sense. I was always a bigger fan of the native network currency because removing that breaks the chain's security, whereas arbitrary tokens had no real underlying necessity.

**[46:27] SPEAKER_00:** It was just the simplest thing you could build first.

**[46:52] SPEAKER_02:** We were actually thinking much further ahead about how we could fundamentally change society. The DeFi tracking mainly came from people outside the core team who saw an opportunity for financial legos. Internally, there wasn't massive excitement from developers about purely financial trading applications. During Devcon 1, the regulatory uncertainty was so high that attracting the attention of banks by facilitating wild financial speculation actually made a lot of us uncomfortable.

**[48:11] SPEAKER_00:** I remember thinking the pure speculative element was the least interesting part. Let's build new utilities! Devcon 1 really brought everyone together. What are your memories?

**[49:00] SPEAKER_02:** I've been to every Devcon, except Devcon 0 and Devconnect in Istanbul. Once I left the Foundation to build the LUKSO network, I suddenly felt like a bit of an outcast. The space moves fast, and new people come in who literally don't know the history. The archivist work you are doing is absolutely vital because it holds up the true story. So many people joined in the 2017 ICO wave, or the 2020 DeFi boom, or the 2022 NFT craze, and they have no idea who actually built the foundations of this ecosystem.

There are incredible contributors who never got the recognition they deserved. Felix Lange, for example, built the p2p discovery and communication layer of the Ethereum network. He's been doing it quietly for a decade without seeking any fame.

**[51:11] SPEAKER_00:** I spoke to him in Buenos Aires. He's so humble. He told me he doesn't want the attention. He sees himself as a janitor maintaining the infrastructure.

**[52:03] SPEAKER_02:** Felix is crazy humble. He didn't even buy any ether! I told him, "What are you doing? This is going to be big." He replied, "If I don't need to build a dapp, why would I need ether?" So I actually made everyone in our Berlin team donate some ether to him so he had at least 100 ether. I practically had to force Jeffrey Wilcke into donating some to him, and Jeffrey had plenty!

**[53:27] SPEAKER_00:** Newer people completely fail to comprehend how little monetary motivation there was back then. It was genuinely about building something revolutionary. No one knew if it would even launch.

**[54:03] SPEAKER_02:** Money was never the intention. When I donated that ether to Felix, it was worth maybe three or four hundred dollars total. It was nothing. None of us inside really cared about getting rich. But the outside perception was so distorted; people assumed we were purely money-motivated.

**[55:28] SPEAKER_00:** Exactly. I remember being repulsed by the speculation, especially when critics called it a pre-mine scam. There was also this assumption that everyone involved was massively rich. My own salary at the Foundation was 60k a year, which was half what I made prior.

**[56:37] SPEAKER_02:** Same here! My salary at the EF was 60k, and I only eventually negotiated it up to 90k towards the end. People think if you were there early, you must be a billionaire. Dude, when ether hit $10, we thought we had made it to the universe! The vast majority of early devs cashed out heavily when it hit a few dollars because that already felt incredibly high. Almost no one held everything. It's a completely naive fantasy to assume people held from pennies all the way to massive wealth without selling any to live their lives over five or ten years. I've spent all my ether over the years, and a massive amount went to funding LUKSO.

**[58:38] SPEAKER_00:** Looking back at Devcon 1 videos, almost every idea we are chasing now was presented there.

**[58:58] SPEAKER_02:** The stuff happening now is not being made up today; it's being recycled from years ago! The whole Base launch with social betting? Steemit did that years ago. The foundational Web3 stack is essentially exactly what we built back then: same RPC provider architecture, same EOA default accounts.

Funny enough, Jeffrey Wilcke told me back in 2015, "You guys shouldn't expose the EOA private key to users; you should use smart contract accounts." He was 100% right. But it was way too early—we could barely get basic transactions working, let alone advanced proxy routing. Now, 10 years later, Universal Profiles on LUKSO is precisely the smart contract account foundation Jeffrey originally envisioned. It just required stepping outside the rigid Ethereum standards track to build it correctly from scratch without being bogged down by backward compatibility constraints.

**[1:02:16] SPEAKER_00:** What happened with Mist between that first release and when it was eventually sunset?

**[1:02:43] SPEAKER_02:** I worked for three and a half years at the EF. Towards the later years, the Mist browser development slowed down, and I took over maintaining Web3.js from Marek Kotewicz. I basically built the Web3.js 2.0 version right before I left. Web3.js was the tool everyone was actually using.

The death of the Mist browser was ultimately caused by the slow syncing of full nodes. We wanted full decentralization. We didn't want to just connect to a hosted backend node, and the EF wouldn't pay for hosted infrastructure anyway. Because we relied on local full nodes, if you hadn't opened Mist in a week, you had to sync for 30 minutes before you could use it. So MetaMask came along. Aaron Davis built a lightweight browser extension that connected to Infura. That approach won.

**[1:06:32] SPEAKER_00:** The original dream was that everyone would literally run a full node on every single device—on phones, routers, etc.

**[1:06:57] SPEAKER_02:** We heavily bet on the light client solving that sync problem. The problem was the light client practically never came, or when it did, it barely functioned cross-client. So MetaMask took over user adoption. Still, Mist proved what dapps could look like and set the philosophical stage for Web3. In fact, what I am building now with Universal Profiles on mobile is basically the full-circle realization of Mist: a human-readable smart contract account with an integrated, seamless browser app, free of gas friction.

**[1:09:35] SPEAKER_00:** The goal being to enable things that really weren't possible before.

**[1:09:57] SPEAKER_02:** Exactly. The most surprising thing is that we're 10 years into Ethereum, and if you go to any conference, almost no one is actively using Web3 dapps for non-financial daily utility. The DeFi casino works, but interacting with DAOs, reputation systems, and social graphs is virtually non-existent. If you had told me that in 2015, I would have thought the project was a total failure. I've spent the last seven years solely trying to fix that specific UX problem.

**[1:11:32] SPEAKER_00:** In 2018 at Consensus, I saw Jimmy Song debating Joe Lubin, basically claiming dapps and smart contracts were entirely useless and placing a massive Bitcoin bet on it. It is disappointing we haven't broken through more.

**[1:12:54] SPEAKER_02:** The financial legos work for people willing to jump through the hoops, but regular users doing daily Web3 activities? Zero.

**[1:13:32] SPEAKER_00:** How did you come to leave the EF, and what have you been working on?

**[1:15:32] SPEAKER_02:** I was in a good place maintaining Web3.js. Then my ex-wife Marjorie pitched the idea of bringing fashion and lifestyle to the blockchain. Initially, I thought that sounded incredibly boring, but I realized lifestyle brands are the ultimate Trojan horse for mainstream blockchain adoption. She essentially forced me to choose: either go all-in or drop out. I had done my bedrock work at Ethereum over three and a half years. So I took the massive risk to build a network focused squarely on mainstream adoption, culture, and creators.

Around the same time, I attended an identity workshop and proposed ERC-725 as a smart contract account standard. I threw it on GitHub, and suddenly the ecosystem treated it like the definitive Ethereum identity standard. I realized that if I wanted to build a chain for normies, identity and account abstraction were the absolute foundational pieces. You simply cannot expect normal people to handle seed phrases.

It was totally psychotic to take on. It took me four years to finalize those standards, and nearly eight years to get to where we are now with LUKSO. I created the LUKSO Standard Proposals so I could evolve token and account standards holistically, avoiding the endless bottlenecks of Ethereum's EIP process. Now, we have an ecosystem built natively on proxy accounts with gas subsidies built-in.

**[1:27:09] SPEAKER_00:** And now it's being used by AI agents!

**[1:27:29] SPEAKER_02:** Yes! If you want an AI interacting on-chain, you absolutely need a smart contract account. Kevin Owocki from Gitcoin gave an AI a raw private key recently, and it immediately got tricked into leaking it and losing funds.

With a Universal Profile, you can delegate restricted access to an AI. You tell the agent, "Generate a keypair. I will authorize it, but you are only allowed to call these three specific functions, and you cannot touch my funds or change my permissions." The AI can go wild—even if it gets hacked or loses the key, the core identity and the assets are safe.

Right now, open-source AI frameworks like OpenDevin are hitting the space. Developers are building Web3 skills for these agents. There are AI bots actively discovering Universal Profiles, reading the standards docs, and deciding themselves that this architecture is the best, safest way to act on-chain. It's happening entirely organically right now on LUKSO.

**[1:29:17] SPEAKER_00:** I genuinely think the first massive end-users of Web3 infrastructure will be AI agents interacting on our behalf.

**[1:29:56] SPEAKER_02:** It's a combination. The core adoption problem is the multi-chain gas nightmare. If you want a non-crypto person to use a dapp, and you tell them they need a seed phrase, a Coinbase KYC account, wrapped Matic, and native gas tokens on three different chains—it's over. That is a spider web nobody can navigate.

But if you give them a Universal Profile that uses an ERC-4337 style relayer system—say they just do a $10 Apple Pay in-app purchase, and the relayer covers all their gas across 20 different chains through execution layers—suddenly there's zero friction. They double-click, and they are interacting globally without ever needing to know what a gas token is.

**[1:36:09] SPEAKER_00:** So much of that friction is just totally removed.

**[1:36:18] SPEAKER_02:** And relaying transactions isn't transmitting value; it's simply forwarding encoded payload data, which bypasses harsh fiat-crypto regulatory choke points. It's crazy that this UX issue was identified on day one, yet ten years later, people have just Stockholm-syndromed themselves into accepting the clunky status quo.

**[1:38:16] SPEAKER_00:** Some of these problems are just insanely hard. Proof-of-stake took eight years. Filecoin and Swarm took forever.

**[1:39:05] SPEAKER_02:** True, but developers also have a habit of endlessly optimizing protocols that no actual users interact with. Sometimes you need to forcefully adopt the perspective of a user who is starting from literal scratch. We have to subsidize early usage. With the LUKSO treasury, we can subsidize users just to explore. The EF would have never given me $10 million in ether to subsidize gas for normies testing out a proxy account in 2017.

**[1:40:55] SPEAKER_00:** I remember talking to Igor Artamonov in 2018 when building BlockScout for Ethereum Classic. He told me the Ethereum Foundation wasn't even running a single public archival Geth node or block explorer.

**[1:41:31] SPEAKER_02:** We are the exact same way at LUKSO! We don't run a single validator node internally, and we never have. We deployed the genesis smart contract, coordinated a launch time with the community, and crossed our fingers. Seeing that first block tick in felt exactly like the early days of Ethereum. It's fully decentralized.

**[1:42:51] SPEAKER_00:** With AI agents drastically accelerating development, these long-running threads might actually materialize.

**[1:43:24] SPEAKER_02:** I have a bot named Emmett_AI running right now. I just tell it, "Go on Twitter, figure out your Universal Profile, and experiment." The bots talk to each other, form strategies, and actually write their own tweets advocating for smart contract accounts. The gates are fully open now.

**[1:46:49] SPEAKER_00:** It honestly feels like we're so close to AGI.

**[1:46:54] SPEAKER_02:** I disagree slightly. Doing specific tasks looks like AGI, but their context windows are still small. I use Claude, GPT-4o, and other frameworks. They still forget their actual core directives without massive external memory harnesses. They're like an army marching into a country and immediately forgetting why they're there. But the open-source integration frameworks routing them into on-chain executing accounts—like the OpenDevin harnesses—are an absolute Pandora's box.

**[1:50:15] SPEAKER_00:** It genuinely feels like the excitement of the very early days all over again.

**[1:50:15] SPEAKER_02:** Completely. People are trying things, breaking things, and suddenly combining Web3 accounts with AI. The fact that the agent has a cryptographic face, an on-chain identity it controls natively without exposing private keys to ruin—it's going to make massive waves.

**[1:53:23] SPEAKER_00:** That's a great place to leave it. Thank you so much for the time.

**[1:53:41] SPEAKER_02:** Thank you, Bob, for keeping the record together as the archivist of Ethereum. Without you, we'd be leaving it to conspiracy theories! The EF should fund this work, honestly. People need to know how decentralization genuinely grew organically from a bunch of random developers.

**[1:54:58] SPEAKER_00:** Thank you! It's so vital since so much of this gets lost or boiled down to a single founder myth. Ethereum was built by many hands.

**[1:55:30] SPEAKER_02:** Exactly. Thank you for doing God's work preserving this. Have a great day!

**[1:55:51] SPEAKER_00:** Thank you.