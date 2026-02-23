**[00:01] SPEAKER_03:** So, hello and welcome to ETHDenver 2026. Here recording for Early Days of Ethereum with Zoltan Felfoldi. How do you pronounce your name?
**[00:11] SPEAKER_01:** Zoltan.
**[00:12] SPEAKER_03:** Zoltan, there you go. Anyway, yeah, I was working out that you're the third longest-serving person at the Ethereum Foundation, right? After Vitalik and then Felix.
**[00:34] SPEAKER_01:** Felix, and then me. Yeah, I haven't checked this fact yet, but honestly, yeah.
**[00:44] SPEAKER_03:** Sounds great. So, you're a very long-time member of the Geth team. But what were you doing before you started at the Foundation? What was your background, and how did you find your way into the blockchain world?
**[00:58] SPEAKER_01:** Well, before Ethereum, I was working on different types of projects. I first started at a Hungarian software company, a classic software company. We sold software in boxes—like floppy disks in boxes on shelves. Yeah, five and a quarter-inch floppies.
**[01:15] SPEAKER_03:** Three and a half-inch floppies, yeah.
**[01:17] SPEAKER_01:** Yeah, but maybe I was exaggerating a little. By that time, it was mostly CDs. Anyway, at that company, I worked on computer graphics, like a ray-tracing engine for architectural software. I also worked on electronic circuit simulation and design. It was around 2011 when I first heard about Bitcoin, and around 2012, I realized it was probably a big thing. I first heard about Ethereum early 2014, a few months after the initial paper was published. I started contributing around November 2014 and officially joined the Ethereum Foundation in March 2015.
**[02:02] SPEAKER_03:** Did you hear about it through Danny and Victor or some other way?
**[02:10] SPEAKER_01:** I heard about it through Danny and Victor's friend circle. Victor came to Hungary and explained Ethereum to me. I started with my ideas and explained why I thought it wouldn't work. He said, "You seem to have a good understanding. Why don't you come work on it?"
**[02:52] SPEAKER_03:** Right. Was it Swarm that you started with?
**[02:59] SPEAKER_01:** Yes, Swarm was part of the initial trinity of base technologies for Ethereum—the storage layer for dApps. It made sense at the time, but the problem space turned out to be more complex. I started contributing to Swarm first and wrote the first 500 lines of code for it.
**[04:02] SPEAKER_03:** I remember Victor mentioning around May 2014 when he first heard about the trinity concept—Ethereum as compute, Swarm as decentralized storage, and Whisper as messaging. There was that famous diagram with Whisper going around the edge.
**[04:51] SPEAKER_01:** That's correct. I wasn't at Devcon Zero yet, but I heard about the idea even before Ethereum. Danny told me about this hash-based chunk storage idea, and it made total sense as a fit for Ethereum. He pitched it at Devcon Zero and later hired me to work on it.
**[05:40] SPEAKER_03:** So, you were hired into EF Dev shortly after Devcon Zero?
**[05:51] SPEAKER_01:** Yes, correct. I first met the Geth team in Amsterdam in February 2015. I was unhired at that point, but Jeff Wilcke saw my contributions and hired me on the spot.
**[06:40] SPEAKER_03:** So, you went to Amsterdam unhired but came back hired. That plane ticket was a good investment. Did they have office space at that point?
**[06:56] SPEAKER_01:** They did have an Amsterdam office, mostly for Jeff because he lived there. It was a small office, and later, it was closed. I went to Berlin a lot after I was hired because the Geth team was centered there.
**[07:27] SPEAKER_03:** Bas was also an Amsterdam person, right? Bas van der Sluis?
**[07:41] SPEAKER_01:** Yes, Bas was there for a short time. Jeff left after a while and started his own company, developing games or something.
**[07:57] SPEAKER_03:** ETH Labs was another one. Do you know anything about ETH Labs?
**[08:20] SPEAKER_01:** I've heard the name but didn't know what it did. Jeff started working with J.P. Morgan back then, and big banks were very interested in Ethereum. Jeff went to work on Quorum for a while.
**[09:56] SPEAKER_03:** I suspect Jeff didn't tell Ming about his work with J.P. Morgan. He probably did it on his own without communication with the EF.
**[10:34] SPEAKER_01:** He probably couldn't share all the details due to non-disclosure agreements.
**[10:54] SPEAKER_03:** I remember Jeff saying he found it interesting because consensus was happening as smart contracts—pluggable consensus pulled into the app layer. Gav also did some proof-of-authority stuff on the C++ side before Clique.
**[14:44] SPEAKER_01:** Jeff left around February 2017. Peter Szilagyi took over as team lead, and Jeff focused on his own projects, like Grid Games.
**[15:37] SPEAKER_03:** Grid Games, building a particular game, but it seems to have ceased. Jeff is unknown off in the world somewhere.
**[15:52] SPEAKER_01:** That's pretty much all I know about him. We tried to invite him to events, but he had enough of the EF and Ethereum.
**[16:36] SPEAKER_03:** When Ming came in, she did legal tidy-up and cut spending significantly. By the mainnet release in 2015, nearly all the money was gone.
**[17:01] SPEAKER_01:** Yes, they spent it very fast. Devcon One was postponed because of that. Jeff said we had to take pay cuts, but once ETH reached $2, our salaries went back to normal. ETH reached $10 in early 2016, and despite turbulent times, we survived.
**[18:18] SPEAKER_03:** I heard that at the worst point, there were only four months of runway left. The C++ team was hit hard by the cuts. I was hired in February 2016, around the same time as Greg Colvin and Pavel were rehired.
**[19:55] SPEAKER_01:** Devcon One was amazing compared to today's Devcons. It was small—300 people—but prestigious, held in an old bank building in London. Big banks and Microsoft were there. It was a serious step up in public appearance.
**[22:20] SPEAKER_03:** Looking back at Devcon One videos, every use case was presented—many concepts too early, but perhaps possible now. Nick Szabo also did a keynote. Was that the first time you met people from Berlin, like Christoph Jentzsch and Lefteris Karapetsas?
**[23:00] SPEAKER_01:** I met some at Devcon One and others in Berlin.
**[23:39] SPEAKER_03:** Was Devcon One your first Ethereum-related visit to London, or did you attend meetups earlier?
**[24:23] SPEAKER_01:** No meetups before, but I visited London with my old software company and met Victor.
**[25:22] SPEAKER_03:** Victor had seen Gav talk in London in early February 2014, right after the Miami launch. Gav pulled Victor on board soon after.
**[25:51] SPEAKER_01:** Yes, Gav wrote the Yellow Paper and developed the C++ client.
**[26:38] SPEAKER_03:** The first time I saw your name was about the light client. I was trying to get Ethereum ARM Linux cross-builds running on my smartwatch. You were plunged into the light client problem.
**[27:36] SPEAKER_01:** Jeff hired me to work on the light client protocol. I designed LES, but it didn’t make sense over devp2p. I’m still focused on trustless chain access and am working on a Trustless Execution Layer API.
**[28:36] SPEAKER_03:** Were you involved with Portal?
**[28:42] SPEAKER_01:** Portal was Piper Merriam’s project. LES was a nice first experiment, but Portal used UDP and different topologies. I think it was canceled prematurely, especially for chain data.
**[31:59] SPEAKER_03:** Do you think proofs are the silver bullet for scaling?
**[32:24] SPEAKER_01:** Statelessness allows higher scaling, but the state tree still needs to be maintained. State expiry might help, but scaling a thousand times will be a huge infrastructural centralization issue.
**[36:04] SPEAKER_03:** Why don’t people run nodes unless they are validators or running businesses?
**[36:47] SPEAKER_01:** We’re stuck with JSON-RPC API that doesn’t provide proofs because it was meant for local use. Scaling didn’t work as initially imagined.
**[39:00] SPEAKER_03:** The assumption that everyone would run their own node didn’t happen.
**[39:11] SPEAKER_01:** The light client protocol worked, but incentivizing it in a decentralized way was hard.
**[42:51] SPEAKER_03:** Filecoin’s white paper was also in 2014. Whisper went for a while, and now there’s Waku. Status drove a lot of that work.
**[44:06] SPEAKER_01:** Jared Hope was eagerly waiting for a fully functional client.
**[45:18] SPEAKER_03:** When they first saw MetaMask at Devcon One, they didn’t want a browser extension talking to a trusted endpoint.
**[46:15] SPEAKER_01:** Decentralized infrastructure will be forced by scaling. As long as MetaMask to Infura works, it’s the standard way.
**[48:50] SPEAKER_03:** Raiden was meant to be Lightning for Ethereum.
**[52:08] SPEAKER_01:** The Geth team has been consistently around 10 people. The team culture has always been good.
**[56:08] SPEAKER_03:** Multiple clients were a basic decision for Ethereum to separate specification from implementation.
**[58:08] SPEAKER_01:** Scaling won’t happen just with L1. Layer 2 solutions like state channels and Raiden have struggled with adoption.
**[59:41] SPEAKER_03:** Thank you for your work on Geth over the years. Geth remains the backbone of Ethereum.
**[59:41] SPEAKER_00:** Thank you.