**[00:08] SPEAKER_00:** With me is Kevin Wood, he's a co founder of Ethereum. Um, let me explain what uh, I'll try to explain what Ethereum does. Uh, it's a smart contract platform based on the blockchain technology. It has a cryptocurrency which is called Ether. Uh, it's much more than Bitcoin. Uh, it's different. Please explain.

**[00:30] SPEAKER_01:** Um, Ether is different and Ethereum, the network that Ether sits on, is different, um, in that it can host other software. So other software. With other software you can do various bits of functionality that you can't for example achieve with Bitcoin. Examples of this sort of functionality are things like identity systems, things like um, insurance payouts based on certain, um, outcomes, things like management, um, of permissions for data, whether data is allowed to be accessed or not. Um, and so um, in reality, um, Ethereum can manage all of these kinds of things based upon the notion of smart contracts. So smart contracts are these programs that sit on Ethereum and do these things and in some sense they replicate some of the notions of real world contracts, but in the electronic and the digital space.

**[01:23] SPEAKER_00:** Okay, so uh, what is the practical use of a smart contract? Give me an example please.

**[01:30] SPEAKER_01:** Um, an example would be where a particular service is offered, um, and payment is required for the service, but the payment can be guaranteed once the service is done. So for example, suppose we set up a sort of Uber, um, whereby what I say is, well, if my GPS coordinate changes to this GPS coordinate, which is say if I arrive at my destination, um, then whoever else's GPS coordinate accompanies me on that, on that way would get some payout, perhaps 15 ether or $15 worth of ether. Uh, and that would be automated, which means that whoever gave me a lift would be guaranteed of being paid if and only if they delivered me to my destination.

**[02:14] SPEAKER_00:** That's a smart contract.

**[02:16] SPEAKER_01:** That could be done as well.

**[02:17] SPEAKER_00:** Okay. And um, it's getting bigger and bigger and bigger. Astronomical rise of uh, percentage plus 1300% in the last year. Right. How do you explain that?

**[02:32] SPEAKER_01:** Um, I think people are starting to realize that agreements between people, which is to say contracts, it's possible to digitize these and when you do digitize them, then there's an awful lot of potential, um, opportunity opened and now people are starting to understand that this opportunity exists and it's real. As they see applications being developed and I think these, by seeing the applications developed, by seeing the pure developer hours put into the system, they're starting to realize that there's something there. And um, they Want a share of its.

**[03:10] SPEAKER_00:** Give me some more examples of what is happening.

**[03:13] SPEAKER_01:** Um, so one of the more interesting ones is something called a prediction market. So this is an idea that you can make predictions about the future and you can be paid if you bet on the right side. So it relies on a few things. Firstly, it relies on the notion of payment. So if I make a prediction, it's very important that I put real value in so I can pay into the market just as I can receive back from the market. So that has to be there. Uh, also importantly is the idea that the truth eventually sort of comes out. Because if there's no way of determining whether I bet in the right way or the wrong way, there's no way of paying out based on that, is there? Um, and second and thirdly, it must all be automated. So this prediction market must exist in an automated fashion so that whenever anybody, um, can uses it, it actually just works without anyone else having to actually make it work. Um, because ultimately, um, you never really want to, um, have to trust a particular third party in order to do this, much in the same way as with Bitcoin, you don't really want to have trust the third party to make sure that you can actually, uh, remove your money.

**[04:20] SPEAKER_00:** It's just if we do business, it's just you and me.

**[04:23] SPEAKER_01:** That's right.

**[04:26] SPEAKER_00:** Um, okay. Um, now there's a problem, uh, with the Ethereum. Somehow 50 or 60 million dollars disappeared, right? What happened?

**[04:39] SPEAKER_01:** So, um, there are a few things to explain about this. The first thing is that the problem isn't with Ethereum itself, but the problem is with one of these applications with one of these smart contract. So the smart contracts are not built into Ethereum. Ethereum exists sort of on a lower level and these software run on the higher level. So it's like saying, well, this website's broken and it's not saying the same thing as the Internet's broken. So Ethereum's like the Internet, it just sort of works. But yes, one of the websites, as it were, that sits on Ethereum, um, broke. This website was called the dao, okay? Now the DAO was envisioned as some sort of mechanism so that people could pay in Ether and this Ether could be used to sponsor projects. And if the projects ended up becoming profitable, people would be able to make some of those profits back. Um, and what happened was, um, due to a technical flaw in this, the Dao, in this piece of software, in this website that sits on top of Ethereum, um, someone was able to attack it and to drain about a third of the money that the DAO had managed to collect into a child dao. So into a sort of. Into a kind of an offspring of the same. The same sort of thing, but an offspring. Now, the reality is that the money is still sitting there. So we know precisely where it is. We can see it in the system. There's a balance. It's big. It's bigger than it should be.

**[05:58] SPEAKER_00:** But there's a different owner.

**[06:00] SPEAKER_01:** But there's a different owner. And at the moment, the owner is unable to withdraw it. So due to safeguards in the dao, um, it sits at about 39 days before the owner can withdraw it. And so we have this time in order to see, to determine whether we're going to do something about it or whether we're just going to let it go.

**[06:18] SPEAKER_00:** The question is, who's right? Uh, it should be determined in the smart contract. So what went wrong in the smart contract?

**[06:28] SPEAKER_01:** So what effectively happened was, let's suppose you're the smart contract and I'm the attacker. What happened was that the attacker said to the smart contract, right, well, I want to do my own smart contract and I want you to give it the money.

**[06:44] SPEAKER_00:** Yeah.

**[06:45] SPEAKER_01:** So you say, uh, okay, sure, let me just. I'll pass you the money into your, into your child, the one that's yours, your SMART contract. And then I'll just update my records. And you say, oh, actually, before you update your records, I'm going to start again. I'm going to say, right, I'd like to withdraw my money into this child SMART contract. And you say, oh, yeah, sure, um, I'll just put your money in the smart contract, and then I'll update my record. And then you say, oh, no, no, no, before you update your records, uh, I want to do that. I want to take my money and put it in this. And so what it's doing is every time you're saying you're putting the money into the smart contract, it's waiting for the money to go in, but it's not waiting to allow you to update your records. Rather, it's interrupting it and then asking it for again. And because you haven't updated your records yet, you still think that there's money that they can draw out. So it's a classic, uh, software engineering bug where the records were updated after and not before the money was given out.

**[07:44] SPEAKER_00:** I understand. So it is a hack. Yes. Um, but this is. This is terrible. This is an attack on the trust liability of the system. This is what everybody is afraid of.

**[07:58] SPEAKER_01:** So fundamentally it's an attack on the, on the dao, so on the um, dao itself. So the notion that people are able to place money into this smart contract and the money will not go except by these rules, will not be used except by these rules. Yes, it's uh, an attack on the dao and it's an attack on uh, the integrity of the dao and it's using the fact that the dao is a smart contract and that nobody can alter um, how it's interpreted. And if the interpret, if this, if this software is wrong, then the interpretation is wrong and people are uh, understandably um, annoyed, um, understandably concerned that uh, you know, hold on, where is this money being going now? The question really is what can we do about it?

**[08:42] SPEAKER_00:** Right, what can you do about it?

**[08:44] SPEAKER_01:** So the people behind the authors of the dao, and I'd like to make it absolutely clear I had nothing to do with a dao, I am a co, founder of Ethereum. The underlying level, uh, I have nothing to do with the dao. Um, the authors of the dao, they're powerless. In effect they're powerless, um, at least without the help of the community who maintain collectively the Ethereum um, ecosystem, the Ethereum machine, the Ethereum computer, the thing that this sits on. So the question is whether the community will do anything about it because it requires the community to be of one mind to come together and form a consensus about what must be done before anything can be done.

**[09:28] SPEAKER_00:** But that's what you have to contract for.

**[09:30] SPEAKER_01:** So the contract provides a base like a default consensus. So as long as the community doesn't sort of intervene, uh, as it were, as long as it doesn't form another different consensus, then everything is fine. But in principle the power lies with the people. If the people don't like the way the contract's operating, they have the power to change it.

**[09:50] SPEAKER_00:** Okay, could it be a clash between say the code and the contract?

**[09:58] SPEAKER_01:** So the clash is really between whether the um, people's expectations, both those who, obviously the ones that place money in the dao, ether in the dao, and those who um, who in some, you know, maintain the Ethereum uh, network. So the stakeholders of Ethereum, it's really the clashes whether they, those people agree or disagree with the ramifications of the contract, which is to say giving the attacker this.

**[10:24] SPEAKER_00:** Yeah, probably they'll disagree.

**[10:25] SPEAKER_01:** What do you think at this point? Um, at this point the jury's out and I think over the next day or two we're Going to find out what the sentiment is of these stakeholders and whether they really want to do anything against it or not.

**[10:40] SPEAKER_00:** But this is an important case, right?

**[10:43] SPEAKER_01:** Uh, I think it's about the most important case in crypto economics since the birth of Bitcoin.

**[10:51] SPEAKER_00:** So what if this goes wrong? What does that mean?

**[10:54] SPEAKER_01:** Um, what would you say is wrong?

**[10:56] SPEAKER_00:** It could go wrong if the 60, 50 or 60 million would not be recovered. Okay, so that would be wrong, right?

**[11:05] SPEAKER_01:** Well, this is the thing. So Ethereum is fundamentally a consensus network, which means right and wrong is determined by the will of the people, by the consensus that the people behind it decide. Now, in this instance, people really do have a decision. They can say, well, honestly, this contract had a book, had a flaw, but it was nonetheless well defined. And the attacker, they did drain against people's expectations, but those expectations were flawed, just as the code was flawed and the attacker is in some sense utilizing what was fair, this, this fair flaw that he found. So there is an argument to be made for the fact that the system is executing correctly. Um, now of course there's also the argument that, well, hold on, expectations, wide expectations were that this contract was going to do this and it doesn't do that. And so, you know, I expect that, uh, that it will be altered to do at least what I, what I think it's going to do, what I thought it was going to do.

**[12:04] SPEAKER_00:** But then you could say there's something wrong in the contract or in the code, which is about the same as the contract. Right? Um, so what is the most important thing? The code or the contract?

**[12:20] SPEAKER_01:** So in this sense the contract is the code. So because it's a smart contract, it's defined only in terms of code.

**[12:29] SPEAKER_00:** But a contract should be written down in just plain language, right? So that you and I understand what.

**[12:35] SPEAKER_01:** We agree in the world of smart contracts, it's written down in computer code.

**[12:39] SPEAKER_00:** So that's where the clash is, right? This is where the problem occurs. We don't understand what we are signing for.

**[12:49] SPEAKER_01:** We, the, well, the signatures that were done were digital signatures, not any other kinds of signatures, of course. And um, what did those digital signatures mean? Well, you have to view it in the wider context of the system that they were submitted to, which is, um, you know, a very well defined smart contract execution system that will, will not be, well, will not easily be intervened with except by a consensus of the community. Uh, um, and it will execute the contract, the code, um, blindly. And that's what it did. And so in some sense the signatures give Authority to the floor and therefore to the attack.

**[13:33] SPEAKER_00:** Um, why did you invented uh, the Ethereum? Why? What was the thought behind it? Was it making money or was it building a community? What was the idea behind it?

**[13:46] SPEAKER_01:** Providing people with a piece of technology that would allow them to have um, barrierless agreements between each other and without having to go to a third party to engage. That's why.

**[14:00] SPEAKER_00:** Was that because you wanted to make a lot of money?

**[14:03] SPEAKER_01:** No, because I thought it was very important technology that needed to be developed.

**[14:07] SPEAKER_00:** Did you make a lot of money on it?

**[14:09] SPEAKER_01:** Um, not as much as some others.

**[14:14] SPEAKER_00:** Not as much as some others. Okay, uh, would you like to explain that?

**[14:21] SPEAKER_01:** Um, something went the other way? I suppose it was um, in some sense it didn't take the route of what you would normally expect a technological venture to take. Um, the route was um, Done in a much more inclusive environment where the people normally in a technological thing, venture there's maybe two or three people that take in some sense the lion's share subtracting from later employees and ah, of course equity, um, sales. But generally there's two or three people. And that really wasn't the case with Ethereum. With Ethereum it was always meant to be a very inclusive system both in terms of how the um, how any of the sort of potential um, tokens were shared out, um, and in sense of, and of course in the sense of you know, who's allowed to help build it and um, um, who would, who could develop on it, you know, how we can bring as many other projects in to help make this a success.

**[15:37] SPEAKER_00:** So some people took more money out of it than you did. Are you disappointed in those people?

**[15:44] SPEAKER_01:** For me it was always about getting this project out into the open and seeing it used.

**[15:48] SPEAKER_00:** Do you think it will survive the problems it has right now? Um, the original idea.

**[15:58] SPEAKER_01:** I think these problems will eventually be a. I hope there'll be a very clear lesson to the future users of Ethereum and I do think it will survive. To the future users of Ethereum and other smart contract systems which I don't think are going away, um, as to how to um, firstly in the case of the dao, what not to do and secondly into how the community manages this problem, um, hopefully of how to, how to, how to form governments, how to form consensus even in the face of a widespread concern that what happened wasn't the expectation.

**[16:45] SPEAKER_00:** Thank you very much.

**[16:46] SPEAKER_01:** You're welcome. Thank you.

