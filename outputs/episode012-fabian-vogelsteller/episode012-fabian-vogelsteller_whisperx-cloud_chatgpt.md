**[00:01] SPEAKER_00:** So, hello and welcome to Early Days of Ethereum. I’m delighted today to be joined by Fabian Vogelsteller. Is that the correct pronunciation? Vogelsteller? More like an F—the V is more like an F. Yes, right. Very Germanic pronunciation that’s not going to come out of my mouth. So, great to see you. We saw each other at Devconnect in November, I think, for the first time for quite a while, and had a good catch-up there. But hello. Hey. Yeah. What were you doing prior to wandering into the blockchain world?

**[00:58] SPEAKER_02:** So, okay, let’s start from the beginning. Okay. So what I was doing before blockchain: I was actually a web developer. I started out as—I mean, I’ve built websites since I was 14. My Findura, the name that I have on Twitter, is actually the name of the content management system that I built, I think, in 2005. And it just happened to turn into my second identity. So I have two identities on the internet: Frozeman and Findura. It’s all just connected to two things. On GitHub, I’m Frozeman, and that’s also my GitHub history with Ethereum and so on. And Findura is then my online one.

And yeah, I mean, I basically was always interested in the cutting edge of the cool internet stuff in the 90s. Building in the early 2000s my first websites—or 1998, 1999—and following the whole evolution of the internet with HTML, CSS, HTML 1 and 2 and CSS 1 and 2, and JavaScript coming in, and blah, blah, blah. So I mainly did web development. But I studied media design, so I didn’t study anything with coding. All the coding is autodidactically learned. So there’s nothing that came from—honestly, even when I joined Ethereum, I had no fucking clue about bytes and how to manipulate bytes and stuff. Still don’t have, actually. So I still don’t know.

**[02:37] SPEAKER_00:** You didn’t have your computer science background. I don’t have any computer science background.

**[02:42] SPEAKER_02:** I’m not sure what I’m doing on the computer. I just know how to interact with high-level languages. And now I only know how to speak to AI and to my team. Well, that’s all you need. Things changed.

And you wrote a book? I wrote a book about Meteor.js. So I got really into web development. I did a lot of websites and built a lot of things. I built my own content management system in PHP. And I built a flat-file-based content management system. So that means this doesn’t need a database. The whole idea was: okay, I just want to have one of these FTP, PHP-ready servers, and if I want to move my—it was literally all about the independence of hosting providers, right? If I want to move from this hosting provider to the other—back in the day, migrating databases was a nightmare, and probably still is a nightmare. It was: if I build a flat-file-based thing, you just copy the whole folder structure over to the other server, and it works. And it did. So that was what DefineDura.org CMS does and did. I mean, obviously, who uses PHP today? But Facebook does. No, but I mean—yeah, now I have a bunch of haters in the PHP community.

But yeah, I built that thing, and that was really helping me to do a full project front to end. And then I got more into JavaScript, and I got really excited by Meteor.js, which was one of the first reactive JavaScript frameworks—before Angular, before React. And it was the first time where you just could write JavaScript code and this HTML stuff, and when you update stuff in the JavaScript or in your local state, the HTML got re-rendered natively—super magic. So I got really into this and I wrote a book about it. I have it here. If you ever want to—I would never read a tutorial book, to be honest. But I wrote one.

**[05:04] SPEAKER_00:** I don’t think people even read books anymore.

**[05:06] SPEAKER_02:** Yeah. I mean, honestly, I would never even—it was so much fucking work to do this. And the reason why I did this is because they reached out to me, and I thought: yeah, I could do that. And then Marjorie, my ex-wife back in the day, encouraged me, and I thought: okay, why not? And in the end, it was a lot of work. Literally four months of waking up—and I had a kid, two-year-old, at the time. Or maybe a year old, I don’t remember. And I had to wake up very early at five to write one or two, three pages or five pages, whatever, and then go to work. It was intense. You get an hourly rate of like 10 cents. So I made totally no money. I literally probably made exactly like 10 cents per hour or something like this.

But it’s reputation. And in a way, I think that’s also what got me into Ethereum, right? Because what is this? Writing single-page apps with Meteor. And what is a dapp? It’s a single-page app. It’s the whole point. It’s an app that literally runs in your browser, doesn’t require a backend. And I built a tool that allowed you to strip out the server part of the Meteor app so you can bundle it as a local app. It was quite popular—a repository called Meteor Build Client. And yeah, that’s what I used for dapps in the early days in Ethereum too.

**[06:44] SPEAKER_00:** So, is Meteor still an active project? Is anyone using Meteor still?

**[06:52] SPEAKER_UNKNOWN:** Yeah.

**[06:53] SPEAKER_02:** No, I totally think so. I think so.

**[06:59] SPEAKER_03:** Yeah.

**[07:01] SPEAKER_02:** I mean, I don’t know how frequent they are. Yeah.

**[07:07] SPEAKER_00:** I haven’t checked it out in a long time. No. But I mean, it’s quite a revolution at the time, the single-page app.

**[07:15] SPEAKER_02:** It was the first, you know. It was literally—one of the first. It was the first framework that I know that really was a proper framework. And it just solved the whole thing from account creation to reactive DOM updates to server-client synchronization. It was magic. Yeah. It blew a lot of people away. And then all the others—React and so on—were kind of more like answers to this. And then React brought it back to the weird way of mixing code and UI in the same files, which I already found very bad in PHP times.

**[07:52] SPEAKER_00:** Right. Yeah. And then I guess you maybe sort of found your way into Bitcoin world in some form?

**[08:02] SPEAKER_02:** So, yeah, 2013, I heard about Canadians wanting to sell a house in Bitcoin. And I thought: okay, wow. What’s that? Like, somebody’s selling a house in a currency I’ve never heard of. And that led me very quickly down the rabbit hole. This was March 2013. That was literally when Bitcoin hit $200 in that very same month.

And number one, I saw: okay, there’s money to be made here. And I was a student with no money. So you have your hope: okay, maybe I can make a little bit of money on the side this way. But I really quickly understood the fundamental power of this technology. And it took me about a year to really understand how it works fully. I literally had this epiphany every month that I thought: now I know how it works. It took me a year to really contort my brain—knowing servers and frameworks and how this basic stuff works—and then crypto and blockchains were just so out there in the way how this stuff works.

But yeah, I was in the space. And then obviously, right after I joined the Bitcoin community, there was the first altcoin, Litecoin. And then in 2013, there were a lot of projects created trying to imitate Bitcoin or do an improvement or do alternate versions. I also got really into Mastercoin: the idea of just writing onto the Bitcoin blockchain rather than creating a separate blockchain.

**[09:49] SPEAKER_00:** And you were in Berlin, right? Were you going to meetups, or did you find fellows? Was it online?

**[09:57] SPEAKER_02:** There were no meetups at the time, really, not in my region. So what actually happened: later, 2014, there were then some meetups. And so I heard about Ethereum. I really knew—I just felt immediately that this is a really powerful approach, but it also sounded so unrealistic.

So when I looked at the white paper—I never really read the Ethereum white paper actually ever fully. I literally just skipped over it. And I listened to Vitalik and the early things that were floating around, and I knew: this is it. The idea of making a computation machine on the blockchain makes total sense. I just thought it’s so hard to do, and I didn’t really give it a lot of chances that they’d pull this off. But then they pulled it off pretty quickly.

And it just happened so that I was at a meetup in Berlin, a Bitcoin meetup—I think the first one I was ever at. They wanted to open a Bitcoin Center Berlin coworking space, basically. Can you imagine what kind of month that might have been? I think that was in August 2014. It was literally a week before the Ethereum presale started. Like, literally days before.

So I met these guys from Ethereum. In this case, it was Aaron, who did the accounting at the time. And they told me that they’re going to open an office in Berlin, and that there’s some kind of news coming out next week, but they can’t tell me. And I was already following Ethereum. I was already waiting for the ICO. And yeah, then it happened.

So I took all my Bitcoin that I had at the time, which was 12 Bitcoins, converted them into Ether. People think: oh my God, 12 Bitcoins, but they were like $600 worth or whatever. It was literally not much. I put them all into Ether—pretty much everything. And I knew this was going to be big. I felt it.

And this was also the first time a project where I thought I would love to work for this project because it’s not about finance, money, and wallets. Because every Bitcoin startup at the time was just about creating a wallet. And I was really interested in creating wallets.

So it just happened that six months later—ICO happened, attention came, blah, blah, blah—but I got an email from a recruiter saying the company Ethereum is looking for a C++ developer. And I was not a C++ developer. Recruiters don’t check anything on LinkedIn, I guess, or GitHub. But I knew that they’re now looking. So I went to their office and I chatted with Aaron again. I saw they had this office here, Waldemarstraße. And I realized: okay, they’re really just thinking that they’re going to build the nodes, and then people will build on top of the stack.

And I just knew: I know how to build single-page apps. This is what you need. I knew this is what they will need—to make sure, to show what a dapp can be, and show how to—so I said: Aaron, just ask around internally. And they had one Skype group that was kind of like the Discord group at the time.

And funny enough, Alex van de Sande is the one who came on board as the UX designer also just a month before me. And he had this whole idea of creating this Mist browser concept. And I think when Alex heard about there’s this guy that came up here that can build single-page apps, then Alex thought: oh, that could be the person who can help with building the Mist browser.

So you convinced Jeff—I mean, that’s my assumption what happened. And he tried to call me up. And I was in Turkey on holidays, so I didn’t pick up the phone. And then when I came back, I saw someone called me, and somehow I called him back or whatever. And he said: hey, you want to work here? We want to do this and this.

And this was Aaron that you were talking to again? No, this was Alex. So I was talking to Alex. So Alex wanted to have me because I think he probably convinced Jeff because he saw this as a guy who can help build his idea, right? And Jeffrey was kind of skeptical of hiring anyone. This is not a code developer—what the fuck can you do, I guess. That’s what he thought.

**[14:54] SPEAKER_UNKNOWN:** Probably.

**[14:55] SPEAKER_02:** What, JavaScript?

**[14:57] SPEAKER_00:** Cannot work. So, I mean, you started in, I think it was January 2015. So I guess this discussion would have been in December 2014-ish.

**[15:07] SPEAKER_02:** Yeah, it was December, exactly. Mid-December. I was on holidays, he tried to call me. And he said: hey, can you start? And I asked when to start, and he said: start in January.

And Jeffrey obviously really wanted to prove me. So he thought: okay, let me just throw a really complicated task at him, and then he’ll fail anyway, and we can get over with this whole thing. I think that’s what Jeffrey thought. So he said: okay, build a chat app for the Whisper protocol.

So in Ethereum, there was the Web3, right? The idea of Web3 was the network, storage—Swarm storage—and communication—Whisper. Which, by the way, I only figured out later that Web3 means exactly these three things. Fun fact. I always thought it’s like: sure, Web2, we go to Web3.

**[15:54] SPEAKER_00:** But that was—yeah, actually, the three. Probably both, right? It’s kind of a bit of a joke that you’ve got both. And I was just looking—so it was November that Alex had done his Mist concept presentation. So I guess that was really quite fresh. It’s like: okay, here’s the little door.

**[16:14] SPEAKER_02:** So he had the idea. And then they were working on it already early December. And I forgot his name, but the French guy who then worked on Remix. Sorry, I forgot his name.

Oh, Yann Levreau. Exactly. So Yann actually built an early version of the Mist browser, but in—I think in C or something like this.

**[16:40] SPEAKER_01:** And what’s that?

**[16:40] SPEAKER_02:** An “Aleth” browser? I think there was one called Aleth browser, maybe. It was really early kind of Mist. It was barely working. And obviously, the whole connection stuff was not figured out properly yet. And they realized quickly that this is not the way to go. And that’s why maybe Alex saw an opportunity here with this JavaScript dude showing up with the single-page app.

**[17:02] SPEAKER_00:** Because, I mean, you’d had AlethZero as well, right? I guess that was the very first Ethereum thing. Maybe that’s what you were thinking of with Yann? Maybe AlethZero was the—was. And that was like a really ugly programmer tool, kind of like a million control. Yeah, I think AlethZero was that early Mist browser. Exactly.

**[17:27] SPEAKER_02:** Yeah, anyway. So Jeffrey said: let the guy build a chat app in the Whisper protocol. So I got dropped into this novel tech—no documentation, no idea how this shit works—and I was supposed to build a whole chat app using this protocol. That was kind of crazy.

But because I really knew how to build single-page apps that are reactive, I could work with Yann on—he gave me the endpoints that I need to use to get the account and to send the messages and stuff like this. So I pulled it off and built a chat app. In a channel, you could basically say: I want to talk about a certain topic, and then you could filter by the topic. So you could see all messages, or you could say: I only want to see this or that topic. And it’s the same like threads in Discord, by the way. So I basically made the thread concept of Discord in this tiny app. And it worked.

And you were connected with your wallet that was in your node, in your geth store. And I think Jeffrey was quite impressed, and that gave him some confidence that I can do it, even though he was trying to prove me wrong.

And what’s crazy is we literally built the Mist browser in like three months. We built the first working version, and we released it with the mainnet. We released the Ethereum Wallet—that was July 31st, 2015. So basically six months later, seven months later, we released the first Mist browser version.

And it was so crazy because everything needed to be figured out. I needed to learn how this stuff works. And initially, in the first two months, it felt literally impossible. And I felt like there’s no way I’m going to figure this shit out. There was no documentation. It was completely over my head in terms of complexity and shit I didn’t understand at all. But I pulled it off.

And I had to—obviously, there were people around me that I could talk to. But everybody was also so busy and had to figure out their own thing, because everything had to be figured out at the time. But I had to literally touch every point.

I had to work with the RPC API, and then I saw this thing was kind of messy. Sometimes it was returning hex, sometimes it was not returning. So I had to basically—I'm a Virgo—so I immediately tried to fix things and make them proper. I immediately wanted to make sure this is proper. Because when we launch the nodes, this stuff can’t change anymore. Because once we start mainnet, you don’t want to constantly make stuff unworkable.

So I had to fight with Gavin to fix and change the endpoints. That was already an uphill battle. Then I had to get into Web3.js, which Marek was working on, which was the JavaScript library that I think Gavin and Jeffrey started. And then I had to help with him or work together with him initially. And then I contributed to Web3.js because we had to build that into the Mist browser directly. So I was literally the first user of that library and really contributed to that library as well.

So we had to make everything up—the whole foundational stack of Ethereum we made up in the first few months. And because I built the piece that put it all together—the node, the dapps, Web3.js, the RPC input, everything into one app—I had to literally touch everything, and I had to talk to everybody. That was quite challenging, not going to lie.

And I also realized that Jeffrey’s team and Gavin’s team was a little disconnected. There was a little battle and war going on where everybody wanted to be the one who determines which feature and how. And I realized: guys, if we are doing like this, that shit is going nowhere if we don’t work together. It would be too complicated, too many iterations.

So I tried to make the teams talk—these two teams. But Jeffrey’s team—I was part of Jeffrey’s team—we were a little bit more open, at least how it felt to me. Gavin really wanted to keep everybody under a bucket, and he didn’t want that we talked to this team. But I found back-channel ways to make them sync up. I guess Gavin didn’t like that. But it was needed so that eventually they started to work more together.

And I had to do a lot of connecting, hand-holding, because I was in this crazy position of being hired by the Amsterdam team while sitting in the office of Gavin’s Berlin C++ team. So I was the connector. I was the translator and the connector, basically. And I had to deal with all the pieces.

So I had to deal with: the C++ client had to work as a client in the Mist browser, as the go client. So I had to talk to people when something was not working.

It’s crazy how much happened in the first six months before the network started. Equally on the network side—there was so much being built and done at the time. But the whole dapp tech stack was literally made up in this moment, in this time.

**[23:33] SPEAKER_00:** Yeah. I mean, I was just looking at the timeline. So September the 16th, 2015 is when the first developer preview of Mist went live. Yeah. I mean, saying about the two teams, I guess you were sort of in the position of being the very first person building one layer up. You know, I guess all of the prior efforts were just about the clients and making features available on the clients, but not really building things on top—and specifically not building things on top to try and be able to work with either. So those interface issues and—

**[24:18] SPEAKER_02:** I mean, to be fair, the first dapps probably were built by Gavin and Jeffrey, but they used all the clunky half-ass stuff. Only on their own stack, right? And then only on their own stack.

Yes, I built the first number one dapp browser—a literally generic tool that can run any JavaScript app to connect to the blockchain. And I built it with Alex, the Ethereum Wallet, which was the first ever dapp on Ethereum—properly done, designed, cross-client functional thing. Yeah. That’s exactly what we did.

**[24:58] SPEAKER_00:** But yeah, I mean, all of that prior stuff, it was just really on their own stack. A little JavaScript page talking to their own endpoints, yes.

Right. I mean, and looking through old videos, there was one—which I think was a talk in London—where both Jeff and Gav were talking about the state of Ethereum and demonstrating some things. So this was October 2014. And one of the demos that they had was one of probably the first on-chain DEX. So they were— you’d got GavCoin and JeffCoin. This is prior to any standards, I guess. And GavCoin was written in LLL, and JeffCoin was written in Mutan. But they did do an on-chain DEX order book thing, putting a transaction for an offer, CPU mining, picking that up. So you have got that interop. And I guess maybe some of the Whisper stuff was maybe kind of cross-client. But you have really got the UI layer.

**[26:19] SPEAKER_02:** So for the chat app, I mainly used the go client because the Whisper thing on the C++ client was not fully integrated or working. The initial idea was that the Ethereum client will host all three things: Swarm, Whisper, and the network. Obviously, Swarm never really worked in there, and neither Whisper—which then later got overtaken and supported by Status, and now it’s transferred into a whole different protocol.

Yeah, it’s interesting. This was really foundational times. And I think what people often misunderstand is how much, number one, Ethereum was generic from day one. Number two, how many ideas were already present earlier.

If you watch the Mist browser video from Alex, we haven’t even built half of this stuff that’s in that video. And in fact, a lot of these foundations are missing. For example, now I’m working on universal profiles across a smart contract account system. And that’s even in the video already. You don’t see wallets. You see profiles. You see people doing stuff. And only now, literally 10-plus years later, we now have the foundation—and it’s not even widely used yet—that even makes that Mist video more realistic.

And it’s not that Alex came up with all of these ideas. This is just what was around at the time. Even right after Bitcoin got attention in 2013 and 2014, these ideas were already around. Like, how can you build decentralized Uber and decentralized this and decentralized that and DEX and whatever. And people think this stuff came all in 2017 and 2020. And this is somehow an invention of the Ethereum Foundation making shit up. This stuff has been around for ages.

**[28:27] SPEAKER_01:** Absolutely.

**[28:28] SPEAKER_02:** We are just behind when it comes to this stuff, actually.

**[28:32] SPEAKER_00:** Yeah, I mean, you had that cryptocurrency 2.0 phase at the start there, talking about Mastercoin and things. I guess there was a thought that everything will get built on Bitcoin. That was the initial thing. And yes, you’ve got these altcoins and experiments and other things, and it might kind of come back together. Or even prior to Bitcoin, because Bitcoin itself was just sort of a manifestation of digital cash streams that had gone back for decades with the cypherpunks. And then you’ve got things like BitTorrent. You did have decentralized messaging things.

**[29:18] SPEAKER_02:** And so on, yes. Basically, it’s interesting. Back in the day, it was all Reddit, right? Bitcoin—today’s crypto Twitter—back in the day it was Bitcoin Reddit, or r/Bitcoin. And Ethereum was the first kind of real challenger to the status quo. And it split the community into the Bitcoin maximalists: the camp that says, no, we only need Bitcoin. Why the heck would you want any other chain? And then the people—even in my friend circles, friends developers—some literally never made the move. They never looked into the Ethereum stack just because they felt that Bitcoin’s all you need.

And I just visited a Bitcoin meetup recently, and I was so taken aback because it was like walking into some kind of time portal back into the time—10 years back—same discussions, same problems, same people, same size of groups. And you’re suddenly back in some kind of time capsule of the past where the topics they talk about are like miner this, miner that, and basic stuff that has been figured out 100 times already on Ethereum. Full and present discussions there. And very few developers, which is also very impressive: how such a network that has so much attention, so much money in it, literally is developed by 100 people—and maybe not even.

**[31:01] SPEAKER_00:** Well, I mean, speaking for myself, I was aware of Bitcoin for a good number of years before I had any involvement in the crypto space. But there were sort of two reasons I guess I wasn’t interested—or maybe three—which was: firstly, I was a gold bug, and I was a software engineer, and I know how terrible most software is. So like some dude you’ve never heard of has made magic internet money—come on.

But I think more importantly, it was just kind of boring to me because: okay, you can do payments. Okay, well, there you go. Well, that’s not very interesting, versus here’s a platform and you can build apps. That was like: oh, that’s kind of interesting. And maybe you had a fairly similar—

**[31:47] SPEAKER_02:** Yeah. For me, the money part was—obviously, it’s cool to invest in something that you feel is going up and you make some money. And I had no money as a student. But it was just so powerful, the idea that there is a technology that no one can control, that sits above the law, that sits above the influence of humans—because you can’t break a system that’s based on consensus. Like a Hydra has 100,000 heads. It was fascinating. I still am. Here I am building still on this stack, super pumped about the next phase of this whole technology. But I just never thought it would take that long, to be honest.

**[32:49] SPEAKER_00:** No, no. So, I mean, you were working from the Berlin office, but presumably you were back and forth to Amsterdam sometimes?

**[32:59] SPEAKER_02:** Rarely. The Amsterdam office—we were there maybe twice or so. In the end, the Amsterdam office was really more like a legal hub. And there was obviously Jeffrey and the operations/personal assistant that he had. And we were all over the place.

So I worked with Alex mainly, who was literally two or five hours behind in Brazil, in Rio. Later, we hired multiple people. We hired another person from Rio. Actually, we hired two other people from Rio. At some point we were three people in the team, four people in the team even, if I remember, at the peak.

But then I also worked on Web3.js, so I worked with Marek closely, who was in the Berlin office. I talked and worked with Christian a lot, who worked on Solidity, also in the Berlin office. And obviously Yann and the other girl that worked on Remix—Lefteris was sitting across me in the Berlin office.

Christoph Jentzsch came to the Berlin office frequently. He was more hired as a contractor to do testing scenarios for the nodes. So he wrote all these tests to test all kind of inputs and outputs of node behavior. I don’t remember exactly—cross-client, make sure this all functions correctly.

And at the same time, the Berlin office functioned as the main go-to place. If you want to visit Ethereum, the Berlin office was the place. There were the most people there. And people just showed up. Dominic Williams just showed up before he made DFINITY. People I met that became friends. Gustav, who built a key manager implementation in Go Ethereum. Felix, the guy who built—still today—the network layer. He was also in the office in Berlin. Literally lived across.

It was like a hub. And I was one of the more social developers inside the group. So when somebody walked into the office, it was mostly me talking to that person, because the others behaved like they didn’t know what to do. There was no secretary person or anything.

And what I was working on—front end, developer stack—I was a little bit on the layer to the outside compared to the people working on the protocols in the inside. So that also reflected socially.

**[36:01] SPEAKER_00:** Right, right. So you missed out on Devcon 0 because you started just after that, but you will have been to London for Devcon 1 in November of 2015 then. Yeah, I was. And token standards were just kind of beginning. The EIP process was just starting. So I guess that’s sort of like phase two, right? Your first one is building a thing and touching everything. And then you’re starting to get up to that on-chain token layer. So how did all that kind of grow up?

**[36:47] SPEAKER_02:** So the whole standardization for me started when Vitalik created the GitHub wiki page because he wanted to standardize tokens, ENS kind of registry, and maybe an early version of a DEX—I don’t remember. And we had some discussion around a GitHub page—literally a GitHub docs page. And he made the early version of ERC-20, and we debated a little bit—mainly on Skype and some comments on this page.

And then London happened. And it’s actually funny because there was a panel about standardization. I presented a lot of things there—I presented the Mist browser, I think. Maybe something else. But I was also on this panel about standardization.

And fun fact: we discussed—I watched it the other day—we discussed standards. There were two main discussions. One: should we put metadata into the contract directly? In this case, the idea was: do we put the metadata of a token—token name and symbol—into the contract? Or do we create a registry for it? And in a way, that’s kind of also today still the big split. Do you put information into a registry, like ENS, or do you put it into the user-owned contract itself?

And it’s going to be another discussion coming, funnily enough. We literally discussed this. And actually, what’s funny, when I looked at this, I literally said—they asked us: what are you interested in in standardization? And I said: the account system. I called it proxy contract because there was no notion of an account. But I called it the proxy contract, which was actually my main interest. Funny enough, I later created ERC-725, and now Universal Profiles as the fulfillment of that. But it’s funny that it was sparked there already.

I talked about key management at the time, and we didn’t even propose ERC-20. It’s kind of nice.

So in this conversation, Martin Becze created the EIP repository. And I think Gavin mentioned: where do we do the standardization? And I think he mentioned: yeah, we have the EIP repository; that would be the right place. That inspired me: oh yeah, actually, we could put it there.

So that’s when I created the issue number 20. And I think I called it “Ethereum Request for Comment” because of the Request for Comments thing. I’m not sure if I came up with the name by myself or whoever came up with the name. But I created the issue and formatted the whole discussion that we had there into a proper specification.

Because I felt: number one, we need to involve the community. If you want to have a consensus around the token standard, everybody needs to listen and have at least an insight. And second, it needs to be in a structured way where not everybody randomly edits this file. And this is actually the exact comment that Gavin made, funny enough: editing—we all laughed about editing—on that one wiki file.

So I structured the process through that and created ERC-20. As a proposal, I made a few changes—some filing, turning around the transfer function, what’s first: value, blah, blah, blah, or amount, whatever. And then we had a discussion, but we didn’t really change much anymore.

So we discussed there about 60 people in total, 300 comments. But pretty much after a while already, everybody felt more or less that this makes sense. The big discussion was around authorized operator or not—should we have it or not. I was kind of against it.

Fun fact: when I created the first test coin, the Mist coin that I used to test in the Mist browser, I did the authorized operator functions. And because I didn’t like it, I really liked more the idea of informing recipients, but I was also too early to do that because we had no idea of the side effects of that.

So in my test coin, I didn’t add the authorized operator. I didn’t see a need.

Fun fact: later, people picked up the Mist coin as a collectible meme token. And because it was a real ERC-20, but because it doesn’t have the authorized operator function, it didn’t work in Uniswap. So they wrapped it. And that’s why it’s not a Mist coin, which is the real Mist coin inside a token that has the function to interact with DEXs. But this was just a test token. It was never meant to.

I just, over the years, gave a bunch of those to random people who asked me, until a whole group of people really wanted to make this valuable. And now it’s traded. Now it has a market cap, and people trade it. It is what it is. It’s the first ERC-20.

I mean, it’s not the first-first. I think there was a preliminary version that Vitalik built before that that was not very functional or standardized. And this was the first one that kind of fit the spec—except the operator stuff.

**[42:39] SPEAKER_00:** So there’s a deployment of that out, which was launched, I believe, by “rFiki,” based on Vitalik’s repo, called CurrencyCoin, is what that one is called. But again, another—they call these relic tokens, relic coins. Yes. Like I’m doing sort of human social history. There are people doing on-chain history of what was the first instance of that.

**[43:18] SPEAKER_02:** I mean, it’s also the crazy thing: the stuff is around. The transaction is around. The code is still around. It’s like a relic. And it’s provable.

And the fun fact is I deployed that, I think, a week before I actually proposed the ERC-20 spec. So I felt that we were kind of more or less—and it was probably around the time of this first Devcon. We can check if it was before Devcon or after, I don’t remember. But probably a day or two before that I deployed that thing.

We also needed it for testing or showing something. I don’t remember. But we needed to test how tokens work in there. Anyway, that’s how it happened.

**[44:07] SPEAKER_00:** It may well have been for the Devcon 1 demo for your presentation.

**[44:13] SPEAKER_02:** No, I mean, we did it for—Devcon did really push us to get some features done and some things done. The token was not yet in there really, because the token thing was still kind of very out there. Also, no one really had— I mean, we all knew people want to make tokens, and that’s why Vitalik started this, because I think he felt an urgency from the community.

But it was not on anybody’s mind that now tokens need to be a primary focus. It was just: hey, do it, let’s do it. The wallet was not meant to immediately be super supportive of that, except that I created the test card for that. And we played around, but it was not an urgency.

That just really happened after ERC-20 kicked off the ICO wave, and that’s when everything went completely bananas.

**[45:07] SPEAKER_00:** And I’m guessing, you know, that ERC-20 standard, you had no idea that it would have so much sticking power.

**[45:14] SPEAKER_02:** No. No one could. I guess no one could. I knew people needed it. I knew it’s going to be a thing that people will do, because already on Mastercoin before, there was Colored Coins. The concept of creating other currencies on top of the Bitcoin blockchain—they called it Colored Coins. So there was clearly a need for it.

But I found the idea of just creating random tokens for random stuff kind of boring. For me, it’s like: okay, what is the value of this? Why would you create a token? And honestly, if you look back—and if you look today—most tokens don’t make fucking sense. There were so many unnecessary tokens that just make no sense and had no purpose.

And I was always a big fan of a native currency, or a native blockchain token, because that thing makes sense. You remove it, the network doesn’t work. There’s no way you remove that token—at least right now—and the network still is functional and economically viable and secure. But with all the other tokens, that was not the case.

**[46:27] SPEAKER_00:** Like, I guess it’s just sort of the simplest thing you could do. It’s like: okay, well, what can you do? Well, hey, look, you can make new tokens. So there’s no need to make new chains and find new miners, right? You can just float it on Ethereum. So it’s like a simple thing. But it’s like: okay, here’s the very first sort of thing. It’s not very interesting. But, you know, we’ve done something.

**[46:52] SPEAKER_02:** The thing is: what people don’t realize is how much more we were thinking ahead: hey, wow, we can do really cool—how we can really change society with this technology. That was actually more interesting to people working in Ethereum than thinking how to make a fucking token.

And how to—like, the whole DEX/DeFi stuff mainly came from the outside too. It was other people that saw an opportunity to make money, or financial Lego, whatever. But internally, there were not a lot of people who got very excited about this, honestly—as far as I remember. Or at least that was my perspective.

And Devcon 1, there was also more speculation. And more speculation is not necessarily good, specifically in an environment in the early days where the regulatory insecurity and uncertainty was so high. The last thing we wanted is every eye on us because we’re trying to compete with banks. I think it made us uncomfortable. At least that’s how I felt about it and how I think other people saw it too. The outside world immediately jumped on it: money, money, money. And that was not the point of the technology in the first place.

**[48:11] SPEAKER_00:** No, no. I sort of remember at the time thinking that’s one of the least interesting parts. It’s like, okay, yeah, you can have that raw speculation, but that’s nothing new versus: what are all these new things that we can build?

Yeah, exactly. So, Devcon 1 I think was quite seminal in terms of bringing together most people for the first time, Devcon 0 being this internal event. But Devcon 1 was the first public Ethereum conference. I sadly did not get to go; I could not afford to go. But what are your memories at the time? You must have seen so many things and so many people.

**[49:00] SPEAKER_02:** Yeah, so I have actually been in—I think I have been in every Devcon so far, except 0, which was only 20 people in Berlin. And I was not at Devconnect in Istanbul. Apart from that, I was at every Devcon.

I was always speaking at the first few Devcons, but then the moment I was not at the Foundation anymore and doing another blockchain, then you’re like: oh, outcast. And it is what it is. Even though the tech I’m building now, and the tech I have been building over the years, is extremely relevant to Ethereum and the ecosystem as well. But somehow, also the people who pick talks in the later years—they are fresh. Some of them literally don’t even know the history.

So that’s why the work that you’re doing is really important, because you are the archivist of Ethereum. You hold up the true story and the participants and the contributions and make that visible and transparent to people. Because I have talked to so many people and they have barely any idea of how Ethereum came to be, who contributed, who did what. It’s completely unknown.

People came in in 2017 for ICOs, 2020 for DeFi, 2022 for NFTs. And for them, Ethereum is just one chain. There’s all the other chains, and they do AMAs, and Ethereum doesn’t do AMAs. And it’s all a big shit show, honestly.

So it’s good that the work that you’re doing preserves this, because there are so many contributors that have not gotten the recognition they deserve. Felix, for example, is a great example. That dude literally built—and is still building—the communication layer of the Ethereum network and how the nodes talk to each other. And he has done that without fame or attention for years.

Felix—man—sorry. Felix Lange? Yeah, Felix Lange, exactly.

**[51:11] SPEAKER_00:** Yeah. Yeah, I spoke to him in Buenos Aires. And the funny thing is, he’s such a humble guy. He was saying to me: I really don’t like Early Days of Ethereum. I don’t want the attention. I don’t want any of that focus.

So I was saying to him: you’re like the longest serving person at the EF, I think, after Vitalik. And he’s like—

**[51:44] SPEAKER_02:** That’s true.

**[51:45] SPEAKER_00:** He’s like: I’m just like a janitor. I just turn up and I maintain the thing, and I don’t want any of that. It was just like a job for me.

**[52:03] SPEAKER_02:** I mean, Felix is specifically crazy. I think there’s a little self-punishment. He didn’t even buy any Ether at all. So I literally—because I thought: what the fuck are you doing? I knew this is likely going to go big because it’s such a revolutionary technology. And I could barely afford any, but I thought: the guy has none. He said: if I don’t have a use for Ether—if I don’t want to build an app—why would I need some?

And I thought: that’s kind of stupid. Because you invest your energy and time here; you should have at least some reward. And what people don’t understand: most people that worked at Ethereum didn’t care about the money or an investment. Neither did I. That was not the reason why we joined. We joined because it was truly—and it is truly—a game-changing revolutionary technology.

So what I did is I donated some to him, and I made everybody in the team donate some to him. So at least he got like—I don’t know—100 Ether or whatever. I don’t know if he kept it or not, but I guess he did. And I even made Jeffrey give some, and Jeffrey gave almost the same amount like us. We had barely any, but Jeffrey had a fuckload. It was so weird. I was like: dude, Jeffrey, you can give a little more. I found him a little knauser.

**[53:27] SPEAKER_01:** Yeah.

**[53:28] SPEAKER_00:** I literally forced him to, basically.

I mean, I think the thing that a lot of newer people don’t comprehend is how little that money was on motivation at all for many of the people. It was really about: what can you build and what can happen? There was no certainty whatsoever that it was even going to work, that it was even going to launch, that it was even going to have any kind of success. It was like: maybe this can be a thing that happened. It would be great if it could. Let’s try.

**[54:03] SPEAKER_02:** But you know, this money was never the intention of anyone that I know. Obviously, some of us felt this can be big, but we had no idea.

At the same time, there was Bitcoin rising, and Bitcoin had a lot more traction and was more of a safe bet. Ethereum was a complete gamble.

And when I donated this Ether—also people say: well, you gave him 100 Ether. It cost literally 40, 50, 60 cents. It was nothing. It was a few hundred dollars. And we had 10, 20 Ether on some wallets laying around just for building stuff. I hope I could find some of those again. But all these keys were ethereal and in some codebase, maybe or maybe not.

Nobody cared, actually, to be honest—not the people who worked internally. But from the outside, they all thought we all just did it for making this thing big and get rich. It was weird. The perception on the outside is sometimes really distorted.

**[55:28] SPEAKER_00:** Yeah, I mean, talking to that ICO and that monetary speculation, I remember at the time almost being repulsed at that speculative thing. And especially the projection of that mindset onto the people that were actually building and saying: oh, you guys—

**[55:48] SPEAKER_02:** Yeah, you’re just doing this to grow it. Exactly.

**[55:51] SPEAKER_00:** It’s a free mine. You’re just giving yourself the money. It’s just like: who needs smart contracts? It’s all a scam. Look at you guys.

And also the assumption: oh, you’re all massively rich.

**[56:37] SPEAKER_02:** Yeah. It’s so wrong. Felix not having any ETH—that was me as well. The reason why is because I didn’t have any money. I was impoverishing myself even being involved. I was volunteering for a very long time with nothing. And then even when I got hired at the Foundation, I was getting paid 60K a year, which was like half of what my prior salary had been.

**[56:37] SPEAKER_02:** And also, same for me. My salary at the Foundation was 60K. And only towards the end, when we had a little bit of success, I negotiated it up to 90K. And that was before tax.

And same with the Ether: everybody thinks if you got Ether back then, you must be insanely rich. Dude, when that hit $10, we all thought we made it to the universe. And now you cash out a few hundred thousand and you think you’re super rich.

Same with some of the early people who had a lot more Ether: they cashed out 100,000 Ether for a dollar because they thought this is really high.

Barely anybody that I know held it until it hit a few hundred or thousand dollars. People don’t understand: there were 10 years, and five-plus years passing with many ups and downs and bubbles.

I have no Ether anymore since many years. I spent them all. My ex-wife has a few more—she had her own ideas of what she wanted to have it on. And then the house that now belongs to the parents of her and stuff. And I’m working on LUKSO, and a lot of my money went into supporting that now.

So the idea that—if I would have held everything that I had, sure, that would be a lot of money. But that means you’re not spending any money during all the years and you only live with your salary. And second, you literally trust so much that this is going to be worth a lot. It’s impossible. Barely anyone—

**[58:22] SPEAKER_00:** It’s such a naive thinking, honestly. It’s this impossible fantasy of saying: assuming that, yeah, you’re going to sit and you’re not going to—okay, it’s 100x. No, no, no. It’s 1,000x. No, no, keep going.

**[58:38] SPEAKER_02:** I know 10,000% is possible. Yes.

**[58:42] SPEAKER_00:** Yeah. So, going back to Devcon 1, I was looking at some of the videos recently and it’s like pretty much any idea you could ever imagine seemed to be presented there. Did you see most of the presentations?

**[58:58] SPEAKER_02:** This is the thing most people don’t understand: this shit that people talk about right now is not being made up now. That stuff has been made up before, tried before.

For example, Base launches the feed that they’re now cut off again, right? Where you have a post and then people bet on this. Steemit did that four years ago. And at least they did it smart because it wasn’t a Reddit-style feature where posts stay longer and have more value over time. Posts that literally disappear after scrolling a page—it’s not worth betting on them. That’s fucking scamming people.

None of that stuff we see is new. And what is fascinating to me is that the space today is still built more or less on the same foundations. On the basis—if you go to the bottom of the bottom—it’s the same foundations that we literally made up in the first six months and the first year of Ethereum.

It’s the same provider—now there’s a bit of a different way how it’s injected—same provider. How your dapp connects to the node. Same RPC endpoints. Pretty much not too much added here either. EOAs have been the default since back then.

And fun fact: Jeffrey told me: you guys should not expose the public key—the EOA—to the user. You should use a smart contract account. And that stuck with me. And he was right. But it was so early. We had no idea. We tried to barely figure out how to make any transaction work. And now think about routing this through a smart contract—that was absurd. But he was right. And now in all these years, that’s what I built.

Now I built exactly that kind of foundation that we discussed back in the day and that we wanted back in the day. But it took all of this learning.

And in fact, it took me stepping outside of the Ethereum ecosystem, creating a different standards track in order to even do that. Because when you do that in this existing ecosystem with existing standards debates, it’s slow. You need to be backwards compatible. You need to think in ways that you just move the current wagon along. If you want to make radical changes, you have so many people that will intervene, and it goes nowhere.

So I needed to do that in a different approach. Kind of funny: I coined the ERC Request for Comment standard space, then went off and created the LUKSO Standards Proposals and did it there—even though that’s just Ethereum standards too—just so I could do it right.

And it’s going to show. That video will be on the internet. So let’s see in a few months, in a year from now: it will show that that was the necessary approach to evolve.

**[1:02:16] SPEAKER_00:** Yeah, yeah. So, you were at the EF working on Mist through to 2017?

**[1:02:16] SPEAKER_02:** No, August 2018. 2018.

**[1:02:16] SPEAKER_00:** So what further work happened in Mist between that very first release and the sunsetting? What was that further—

**[1:02:43] SPEAKER_02:** Yeah, so my work was not only in the Mist browser. I worked for three and a half years at Ethereum. And then in the later years, I really started working more on the developer tools.

I overtook Web3.js, which was the main JavaScript library at the time. When Marek left with Gavin to join Parity or Ethcore, I overtook Web3.js. So I mainly maintained this library. I built the 2.0 version of it. That was the last thing I did before I left—releasing the 2.0 version of that library.

And in the last year, I stepped a little out of the Mist team. I was focused on the other things more, but I was still kind of the main developer in Mist. But now there was more maintenance.

We tried to create more of the Mist browser. It was complicated because we were always lagging behind Chromium and Electron. Electron used Chromium, Chromium is what we then used. So if there was a bug in Chromium, it needed to first be supported by Electron before we could support this. It was a cycle.

We worked a lot on the interface. In the end, the Ethereum Wallet—or people called it the Mist Wallet—was basically the main thing ever really used. People never really fully used it as a Web3 browser. But we built all kinds of features in there. I built things where an app could set notifications on the sidebar. There were a lot of features that we added to the browser that were never really fully used.

The biggest problem for the Mist browser, and in a way the death of the Mist browser, was the slow syncing of the Ethereum nodes.

**[1:04:44] SPEAKER_01:** Yeah, yeah.

**[1:04:45] SPEAKER_02:** And because we wanted to do it the full decentralized way, we didn’t just want to talk to a backend node that someone hosted. And also the Ethereum Foundation probably wouldn’t have paid for a node hosted on a server for everyone else to connect to.

**[1:05:04] SPEAKER_00:** I completely believe that. There was so much penny-pinching out on costs.

**[1:05:09] SPEAKER_02:** It would have been so easy, instead of talking to the localhost node, to talk to a remote node. I could have added that feature in no time. The reason we didn’t do this is because it really went against the whole idea of doing it decentralized.

The problem is: syncing the Mist browser—if you didn’t have it open for a week—took sometimes half an hour plus. So what happened is MetaMask—Kumavis came up with the idea: okay, I built a browser extension connected to a remote node, and I do a light version of MetaMask. And I just inject it into an existing browser. And that idea won. So MetaMask kind of outcompeted the Mist browser.

And then on top, the difficulties of keeping it secure is what made us shut it down. But we had a lot more ideas. Look at the video: we hadn’t even started playing out the idea of the Mist browser fully. But at the time, it was not the right time.

But it really showed a lot of people how things can be done, why to do it this way, how to build the apps, how to—yeah, it set the stage.

**[1:06:32] SPEAKER_00:** Yeah. In terms of that local node, full decentralization, I remember thinking: yeah, of course that’s going to happen, right? Of course everyone’s going to have an Ethereum node running on every device. It’ll be like: you’ll have one running in the background on your phone. They’ll be in every router, media station, every computer.

**[1:06:57] SPEAKER_02:** Also, there was the idea of the light clients. And we knew there were light clients coming. And we really bet on the fact that the light client will solve that problem.

The only problem is the light client never came, or it came but it was not cross-client and it didn’t fully work. So we hoped a lot on the light client. This was why we kept doing it this way, because the idea was: once you have the light client, the thing is like this.

**[1:07:25] SPEAKER_00:** Yeah, so we’ll just build on the full node for now, and then that light client will come in.

**[1:07:33] SPEAKER_02:** And I think we came that far. I think there were versions of the Mist browser that had geth built in with light client support that synced very fast. But by that time, people already moved on to MetaMask. And again, security and other reasons in the end made us give up.

But I already moved on to Web3.js at the time as my main focus, because that was the tool everybody was using. 70 million, 140 million downloads—God knows what it has nowadays. It’s still used a lot, even though now Ethers and others took over.

And then when I left, Alex shut it down for the reasons also. It had its purpose.

And by the way, the idea of the Mist browser is still a very valid idea. In fact, what I’m building now is like a Mist browser mobile. It’s interesting because what I’m building now is almost like a full circle.

**[1:08:44] SPEAKER_01:** Yeah.

**[1:08:45] SPEAKER_02:** I introduced a smart contract account—the same like Jeffrey said we should do it. That’s the foundation of your access to Web3. And then you have a web browser in an app that allows you to interact with the apps easily while doing it in a human-focused way. Not wallet-focused, but profile-focused. Safe way. Easy gas. In a way that literally works for humans.

Which was also the idea of the Mist browser. It was not meant for nerds and techies. It was meant to be normal people interacting with this new technology. That was the whole point.

And this is going to come now with the Universal Profile app as kind of a Mist browser on mobile in its first version.

**[1:09:35] SPEAKER_00:** Yeah. The goal being not just to replicate existing applications on the blockchain, but to enable these things that weren’t possible before. Having this hub, integrating all these different pieces of your life—that was real utility.

**[1:09:57] SPEAKER_02:** Exactly. And what’s actually interesting—and for me, the most surprising thing—is we are 10-plus years into Ethereum, and there’s so many networks, EVM apps. Most are very financial-focused, which really turned me off.

The moment DeFi happened, I thought: that’s a big gamble park. Important protocols, but it became such a casino that it turned me off.

But what’s interesting is: we go to conferences, you meet Web3 people, and no one is using Web3 apps. Literally. People have wallets, and maybe they’re purchasing a coin here and there. But interacting with actual apps—voting, joining a community, giving reputation, doing all the things you could do on-chain—it doesn’t happen.

If somebody would have told me in 2015 or 2016 or 2017 that in 10 years there’s still no actual users using the apps, I would have thought: number one, if that happens, it’s a total fail. And number two, there’s no way this is true. And here we are.

**[1:11:32] SPEAKER_00:** It’s funny, crazy. I remember in 2018, I went to the Consensus conference—New York Blockchain Week—and there was a panel there that was almost like a Bitcoin versus Ethereum thing. You have Jimmy Song, fucking dickhead with his cowboy hat, and you had Joe Lubin. And Jimmy was basically saying: dapps are useless, smart contracts are useless, nobody’s going to be using these in five years. And him and Joe having a bet for a pretty significant amount of Bitcoin. I can’t remember what it ended up being. And I don’t know what—

It was this crypto Twitter ongoing discussion of: is this—

**[1:12:33] SPEAKER_02:** And luckily he didn’t propose to cut off his penis.

**[1:12:36] SPEAKER_00:** Yes. It’s not McAfee. But yeah, it’s disappointing, that’s for sure. DeFi is working. Stablecoins are being used.

**[1:12:54] SPEAKER_02:** The whole financial Lego works, yes, but only with the people that went through the hoops. Now you have Robinhood and other apps that integrate and make it more easy. So the trading part, sure, that worked out. People buying and selling.

But the normal user using Web3 infrastructure in their daily lives: non-existent. Non-fucking-existent. And I know why, and I spent the last seven years thinking about that and how to solve that. This is what I am working on now.

**[1:13:32] SPEAKER_00:** So how did you come to leave the EF, and what was that journey like? And then what have you been doing? Tell me about all your work there.

**[1:13:43] SPEAKER_02:** Yeah, before we do this, I need to go pee. So you need to look at the timestamp and then I will come back and talk about this. This is too much tea. Sorry for the interruption.

**[1:15:09] SPEAKER_00:** No worries. So, yeah, I’ll cut it and I’ll just ask again. So, yeah, could you tell me a bit about how you came to leave the EF, what your motivation was, what did you do, and what have you been doing?

**[1:15:32] SPEAKER_02:** So, well, actually, I was kind of in a good place. I worked on Web3.js. The developers loved me because I built their foundational piece. The Mist browser was kind of fading out, but it was cool too. So I was in a good place.

What happened is: my ex-wife at the time, she had this idea: let’s do something with fashion, lifestyle on the blockchain. And I thought: that sounds super boring. And I know so many people already try to do something like this. But then I thought a bit about it: hmm, but we can use lifestyle and fashion—specifically when you get big players and mainstream normal users through these brands—and we can get mainstream people into using this technology that could be the Trojan horse of how we make this technology attractive and interesting to people outside of trading. So I thought: actually, this is kind of genius. But it also sounded like a lunatic, crazy idea and completely out of my league.

So initially, I thought: okay, I can support Marjorie a little bit. She does the project; I can help a little with advice. At the same time, I worked for three and a half years at Ethereum. I did all the foundation work I needed to do. I felt: okay, I did everything I can do here. I can continue here for another 10 years, but I don’t think I’m gaining a lot more from now.

And in hindsight, I’m right. When I look at others still there, it’s not that the world changed for them in terms of what they’re working on. It’s the same thing.

And then at some point, when we started mapping out the project, Marjorie kind of forced me: either you’re all in or you’re out. She’s a tough person. That’s her character. But it forced me to decide: do I want to stay here at Ethereum comfortable, indefinite? Or do I go all-in crazy risk, something new, something different?

And I knew my Ethereum colleagues would think: what the fuck, his girlfriend just twisted his head, now he’s doing some centralized fashion shit. While at the same time, I knew this is a path for real adoption.

My idea was different than Marjorie’s. While she wanted to do something with fashion, I wanted to create an infrastructure. And then use her fashion connections—friends, people that we had initially helping with the project—like a tool to get users and people into using this technology.

And at the same time, I also came up with a standard called ERC-725 before LUKSO. It’s 725, which is one standard after 721. Even though there’s three other issue numbers after, but there were nothing in the middle. It was a proper standard after.

And it was a coincidence how I came up with 725. I was at the BCG workshop. They wanted to make identity on the blockchain. I was the only one really coming up with something concrete. And I made this smart contract account system. I called it proxy account, same like we called it 2015 at the panel, funny enough.

And I had this urge after this workshop series that I need to propose this as a standard. There was something in me telling me: you need to put it out there. I had no idea why. I didn’t want to because I was fine with what I was doing. I didn’t need attention.

But the moment I put it out there, suddenly the whole Ethereum space—or a lot of these developers—were like: my God, this is the Ethereum identity standard. A lot of projects came and they created the ERC-725 Alliance, Origin Protocol. And then uPort got super pissed because uPort—which was a ConsenSys identity protocol at the time—thought: what the fuck? Why does now this Ethereum standard— we are working on this Ethereum identity for the last year, and now Fabian comes and just makes a standard and everybody pays attention.

And they wrote a big blog post about how this is a massive monster and there is this modular system. And I didn’t want the attention on that, nor did I even care. I knew this was an early draft of the standard. There needs to be a lot more work. But people treated it like it’s the final thing: Ethereum identity is now here. And it’s like: man, guys. I thought: if you’re all excited, then someone becomes the lead and you guys build it out. Fine with me, I’m out.

But then when we started LUKSO, which was a few months after, I realized: oh wow, if I want to make a chain that’s for normies, for culture, creators, and anything outside of finance, identity is the most important piece. If that’s not there—if a company or people or non-technical people cannot use an on-chain account properly—UX needs to be easy. And if that thing is not ideally unlosable, there’s no way you can put these people on-chain. This is not going to work. They’re not going to run around wallets with private keys they need to remember. There’s no way.

So I knew I now had to build out a standard full-on. That was really annoying because I didn’t want to do this at all. I knew there was quite a lot of stuff missing.

And in hindsight, it was a complete psychotic idea, because it took me four years to build out the foundational standards full-on. And now it’s almost eight years to put it to a state where it’s literally usable by people. Currently only on LUKSO, but it’s going to come to all other chains, including Ethereum, very soon. And now it’s being used by AI. Fun fact. I knew it’s possible, but I didn’t expect it to happen so quickly. This frenzy started two weeks ago.

And it’s exactly the account we would have needed with the Mist browser back in the day. It took a while to build this out.

So the whole LUKSO story is its own episode—seven, eight years. But long story short: I built this account system. I evolved the token standards in a quiet space because I made the LUKSO Standards Proposals, so I could do it properly the way I thought we can evolve it properly—make sure that accounts and tokens work together. Not just think about one standard isolated and the other, but think how it works together in a Lego-like way while being isolated but working well together.

So I had the opportunity to do it right. And that’s what I did over the last few years. And when this now comes cross-chain—specifically Universal Profiles—it’s going to show for the broader ecosystem as well.

Token standards: once the train ran, once people went with ERC-20, adoption happened. There’s no way you convince people to migrate that token. It doesn’t happen.

That’s exactly where a new network makes sense. On a new network, you can do it all the new ways. Now you can discover there’s more possibilities, cooler protocols, more automation, different things you couldn’t do on ERC-20 at all. Hence why a new chain makes sense—also for gas subsidization for smart contract accounts, which they need to be subsidized if you don’t want to pay right away.

All of this stuff you can’t really do on an existing network. And the rest of the EVM system just chose ERC-20, a 2015 standard with no real evolution and knowledge. We made it up at the time with whatever we knew, which was literally nothing. So it still came very far. It did a lot.

But Universal Profiles are going to play a role. I think they will be the biggest enabler for Web3. And I believe it will be bigger than ERC-20. It’s going to blow people’s minds.

I know there’s a lot of people, including probably you, who have been watching me talk about this stuff for years, putting it aside as: okay, this is just doing this thing in an isolated LUKSO world. It’s going to show. Mark my words. It’s going to blow people’s minds, especially developers who have been thinking about smart contract accounts and account abstraction for a while.

There are good ideas, but it’s still very simple. If you have a lot of people who want opinions and you want backwards compatibility and minimalism, you don’t get far. It ends up in the same direction, it just takes way longer.

This is ready. It’s free, open source, usable by anyone on any network. It will show once we open up our control apps to work on all these chains.

But right now, what’s funny: because we are in the time of AI