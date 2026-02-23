**[00:01] SPEAKER_01:** Thank you. Thank you.

**[01:02] SPEAKER_00:** Hello.

**[01:32] SPEAKER_01:** Hello.

**[02:15] SPEAKER_00:** Yes.

**[02:45] SPEAKER_01:** Yes.

**[03:05] SPEAKER_00:** So, I guess we're recording now. Okay. I'm Bob Summerwill, recording here at DevCon Prague for Early Days of Ethereum.

**[03:23] SPEAKER_01:** I'm Jakub, and I'm also here.

**[03:28] SPEAKER_00:** Cool. And, you know, we did meet in Bogota for DevCon 6, I think, first time.

**[03:38] SPEAKER_01:** Yes.

**[03:44] SPEAKER_00:** That was, what, 2022, I think. That was a really memorable conference. You introduced yourself. I think we were, I was talking with someone about Florian Glatz.

**[04:01] SPEAKER_01:** Yeah.

**[04:04] SPEAKER_00:** And talking about the old days. And you just jumped in because you know Florian. And we got talking.

**[04:13] SPEAKER_01:** Yes.

**[04:16] SPEAKER_00:** And now here we are two years later in Prague.

**[04:22] SPEAKER_01:** Yes.

**[04:25] SPEAKER_00:** So, could you introduce yourself? Who are you? What do you do?

**[04:32] SPEAKER_01:** Yeah. So my name is Jakub. I'm from Czech Republic. I'm a software engineer, been working on Ethereum since like 2016. I used to work for some companies, but now I'm independent, doing my own things. But I'm still in the ecosystem.

**[04:57] SPEAKER_00:** Cool.

**[05:01] SPEAKER_01:** Yeah.

**[05:04] SPEAKER_00:** So, I know you from your work on things like GasNow and BlockPI, I think.

**[05:14] SPEAKER_01:** Yes.

**[05:17] SPEAKER_00:** Can you tell me about those projects?

**[05:21] SPEAKER_01:** Sure. So, GasNow was a gas price oracle that we built. It was a service that suggested gas prices for users, based on the current network congestion. And it was quite popular for a while. It was used by many applications.

**[05:44] SPEAKER_00:** Yes.

**[05:47] SPEAKER_01:** But then we had to shut it down because of the Merge, because it was not needed anymore, because EIP-1559 changed how gas pricing works.

**[06:00] SPEAKER_00:** Right.

**[06:03] SPEAKER_01:** And then we built BlockPI, which is a scalable RPC infrastructure. So, instead of just providing gas price suggestions, we provide a full RPC endpoint that people can use to interact with the network.

**[06:21] SPEAKER_00:** Okay.

**[06:24] SPEAKER_01:** And it's more scalable than some of the existing solutions.

**[06:29] SPEAKER_00:** Cool.

**[06:32] SPEAKER_01:** Yeah.

**[06:35] SPEAKER_00:** So, I know you also do a lot of work on MEV and Flashbots and stuff like that.

**[06:45] SPEAKER_01:** Yes. So, I'm part of the Flashbots research team. I'm working on MEV-related research.

**[06:55] SPEAKER_00:** Okay.

**[06:58] SPEAKER_01:** And trying to make the blockchain ecosystem a better place, I guess.

**[07:04] SPEAKER_00:** Right. And I think you also have some involvement in the MEV roast, right?

**[07:11] SPEAKER_01:** Yes, we organize the MEV roast, which is a fun event at DevCon, where we roast MEV, but also discuss serious topics around it.

**[07:24] SPEAKER_00:** Right. So, let's talk about your journey. How did you get into Ethereum? What was your path to getting involved?

**[07:36] SPEAKER_01:** So, I discovered Bitcoin in 2013, I think. I was interested in cryptography and all that. I read the Bitcoin whitepaper. I was fascinated by the technology. But I didn't get involved immediately. I was just following from afar.

**[08:00] SPEAKER_00:** Okay.

**[08:03] SPEAKER_01:** Then in 2016, I discovered Ethereum, and I thought it was really interesting because it allowed for programmable money and smart contracts. So, I started learning Solidity and building dapps.

**[08:20] SPEAKER_00:** Right.

**[08:23] SPEAKER_01:** And I built a few projects, nothing too big, but just to learn.

**[08:29] SPEAKER_00:** What kind of projects?

**[08:32] SPEAKER_01:** I built a simple betting dapp, a decentralized exchange prototype, things like that. Just to learn how things work.

**[08:45] SPEAKER_00:** Okay.

**[08:48] SPEAKER_01:** And then I got a job at a company that was building on Ethereum, and I've been working in the ecosystem ever since.

**[08:57] SPEAKER_00:** Right.

**[09:00] SPEAKER_01:** Yeah.

**[09:03] SPEAKER_00:** So, you mentioned you were interested in cryptography. How important is cryptography knowledge for Ethereum developers?

**[09:14] SPEAKER_01:** I think it's useful to understand the basics. Like, how public key cryptography works, how hashing works, what elliptic curves are. But you don't need to be a cryptographer to build on Ethereum. There are many libraries that abstract away the complex parts.

**[09:36] SPEAKER_00:** Right.

**[09:39] SPEAKER_01:** But having a deeper understanding helps you make better decisions, especially when it comes to security.

**[09:46] SPEAKER_00:** Definitely.

**[09:49] SPEAKER_01:** Yeah.

**[09:52] SPEAKER_00:** So, let's talk about MEV. What is MEV, and why is it such a big deal?

**[10:01] SPEAKER_01:** So, MEV stands for Maximal Extractable Value. It's the value that can be extracted from the blockchain by reordering, inserting, or censoring transactions. It's a concept that was introduced by the Flashbots research.

**[10:20] SPEAKER_00:** Okay.

**[10:23] SPEAKER_01:** And it's a big deal because it affects the fairness and the user experience of Ethereum. If someone can front-run your transactions, you might get a worse price or your transaction might fail.

**[10:38] SPEAKER_00:** Right.

**[10:41] SPEAKER_01:** And it also creates centralization pressures because only those with the infrastructure can extract MEV.

**[10:49] SPEAKER_00:** So, what are the solutions to MEV?

**[10:55] SPEAKER_01:** There are several approaches. One is to make it harder to extract MEV through protocol changes, like encrypted mempools. Another is to capture MEV and redistribute it, like through Flashbots Auction. And there's also application-level solutions, like using batch auctions or private transactions.

**[11:23] SPEAKER_00:** Okay.

**[11:26] SPEAKER_01:** But it's a complex problem, and there's no silver bullet.

**[11:32] SPEAKER_00:** Right.

**[11:35] SPEAKER_01:** Yeah.

**[11:38] SPEAKER_00:** So, what do you think the future of MEV looks like?

**[11:44] SPEAKER_01:** I think we're moving towards a world where MEV is more democratized. With the rise of MEV-boost and PBS, more validators can capture some of the value. But there's still a lot of work to be done to make it fair.

**[12:08] SPEAKER_00:** Right.

**[12:11] SPEAKER_01:** And I think encrypted mempools will play a big role in the future, but it's technically challenging.

**[12:20] SPEAKER_00:** Okay.

**[12:23] SPEAKER_01:** Yeah.

**[12:26] SPEAKER_00:** So, let's switch gears. What are you most excited about in Ethereum right now?

**[12:35] SPEAKER_01:** I'm excited about the progress on Layer 2 solutions. I think they're really scaling Ethereum while maintaining security. And I'm also excited about account abstraction and ERC-4337, which could make onboarding new users much easier.

**[12:56] SPEAKER_00:** Right.

**[12:59] SPEAKER_01:** And of course, the continued research into PBS and danksharding.

**[13:06] SPEAKER_00:** Okay.

**[13:09] SPEAKER_01:** Yeah.

**[13:12] SPEAKER_00:** So, what advice would you give to someone who wants to get into Ethereum development?

**[13:20] SPEAKER_01:** I would say start building something. Don't get stuck in tutorial hell. Pick a project and build it. You'll learn much faster by doing. And don't be afraid to ask questions. The community is very helpful.

**[13:38] SPEAKER_00:** Right.

**[13:41] SPEAKER_01:** And read the specs. Read the EIPs. Understanding the core protocols is really important.

**[13:49] SPEAKER_00:** Definitely.

**[13:52] SPEAKER_01:** Yeah.

**[13:55] SPEAKER_00:** So, what's next for you? What are you working on?

**[14:02] SPEAKER_01:** I'm continuing my work on BlockPI, trying to make it more reliable and scalable. And I'm doing research on MEV. And I'm also exploring some new ideas around decentralized infrastructure.

**[14:20] SPEAKER_00:** Cool.

**[14:23] SPEAKER_01:** Yeah.

**[14:26] SPEAKER_00:** Well, thanks for talking with me, Jakub. This has been great.

**[14:32] SPEAKER_01:** Thanks for having me, Bob. It was fun.

**[14:37] SPEAKER_00:** Yeah. And to everyone watching, thank you for tuning in to Early Days of Ethereum.

**[14:44] SPEAKER_01:** Yes. Thanks.

**[14:47] SPEAKER_00:** We'll see you at the next one.

**[14:51] SPEAKER_01:** Bye.

**[14:54] SPEAKER_00:** Bye.