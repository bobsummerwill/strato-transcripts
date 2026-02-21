**[0:01] SPEAKER_00:**
So hello and welcome to Early Days of Ethereum. I am delighted today to be joined by Fabian Vogelsteller. Is that the correct pronunciation? Vogelsteller. More like an F. The V is more like an F. Yes, right. Very Germanic pronunciation. that's not going to come out of my mouth. So, you know, great, to see you. We, saw each other at DeadConnect. In November, I think, for the first time for, quite a while. And had a good catch up there. But hello. Hey. Yeah. what, were you doing, prior to wandering into, blockchain world?

**[0:58] SPEAKER_02:**
So, okay, let's start from the beginning. Okay. So what I was doing before blockchain, I was actually a web developer. So I started out as, I mean, I've built websites since I was 14.

**[1:14] SPEAKER_02:**
My Findura, the name that I have on Twitter, is actually the name of the content management system that I built, I think, in 2005. And it just happened to be, you know, turning into my second identity. So I have two identities in the internet, Frozman and Findura. It's all just connected to two things. In GitHub, I'm Frozman. And that's also my GitHub history with Ethereum and so on. And Findura is then my online one. And, yeah, I mean, I basically, you know, was always interested in the cutting the edge of, like, the cool internet stuff in the 90s. You know, building in the first 2000s, my first websites or 1990, whatever, eight, nine. And, you know, following the whole evolution of the internet with HTML, CSS, HTML1 and 2 and CSS1 and 2 and JavaScript and coming in and blah, blah, blah. So I mainly did web development. But I studied media design. So I didn't study anything with coding. All the coding is autodidactically learned. So I haven't, yeah, there's nothing that came from, honestly, even when I joined Ethereum, I had no fucking clue about bytes and how to manipulate bytes and stuff. Still don't have, actually. So I still don't know.

**[2:37] SPEAKER_00:**
You

**[2:37] SPEAKER_02:**
didn't

**[2:37] SPEAKER_00:**
have your computer science background. I don't have any computer science background. I'm not

**[2:41] SPEAKER_02:**
sure what, I'm, I don't know what I'm doing on, the computer. I just know how to interact with, like, high -level languages. And now I only know how to speak to AI and to my team. Well, that's all you need.

**[2:55] SPEAKER_02:**
Things changed. And you wrote a book? I wrote a book about Meteor .js. So I, yeah, I got really, obviously, into web development. I did a lot of websites and built a lot of things. I built my own content management system in PHP.

**[3:13] SPEAKER_02:**
And I built a flat file -based content management system. So that means that this doesn't need a database. The whole idea was, okay, I just want to have one of these FTP, PHP -ready servers. And if I want to move my, it was literally all about the independence of hosting providers, right? If I want to move from this hosting provider to the other, I mean, back in the day, migrating databases was a nightmare and probably still is a nightmare.

**[3:39] SPEAKER_01:**
It was,

**[3:40] SPEAKER_02:**
oh, if I build a flat file -based thing, you just copy the whole folder structure over to the other server and it works. And it did. So that was what DefineDura .org CMS does and did. I mean, obviously, who uses a PHP today? But Facebook does. No, but, I mean, yeah, now I have a bunch of haters in the PHP community.

**[4:08] SPEAKER_02:**
But, yeah, I mean, so, yeah, I built that thing and that was really, like, helping me, like, to kind of, like, do a full project front to end. And then I got more into JavaScript, and I got really excited by MeteorJazz, which was one of the first reactive JavaScript frameworks. that was before Angular, before React. And it was the first time where you just could write, like, this JavaScript code and, this HTML stuff. And when you update stuff in the JavaScript or in your local state, like the HTML got re -rendered natively, super magic. So I got really into this and, I wrote a book about it. I have it here.

**[4:52] SPEAKER_02:**
If

**[4:55] SPEAKER_02:**
you ever want to, I would never, I would never read a tutorial book, to be honest. But I wrote

**[5:03] SPEAKER_00:**
one. I don't think people even read books anymore.

**[5:06] SPEAKER_02:**
Yeah. I mean, honestly, I would never even, it was so much fucking work to do this. And the reason why I did this is because they reached out to me and I thought, like, yeah, I could do that. And then, you know, Marjorie, my ex -wife, back in the day, encouraged me and I thought, like, okay, why not? And on the end, it was a lot of work. I mean, literally, like, four months of waking up and I had a kid,

**[5:31] SPEAKER_00:**
two -year

**[5:31] SPEAKER_02:**
-old, two -year -old kid at a time. And I had to wake up very early or maybe a year old, I don't remember. And I had to wake up very early at five to, you know, write one or two, three pages or five pages, whatever, and then go to work. It was intense. You get an hourly rate of, like, 10 cents. So,

**[5:55] SPEAKER_01:**
I made

**[5:55] SPEAKER_02:**
totally no money. I literally probably made, like, exactly, like, 10 cents per hour or something like this. Right. But it's reputation. And in a, way, I think that's also what got me into Ethereum. Right. Because what is this? Writing single -page apps with Meteor. And what is a D -app? It's a single -page app. It's the whole point. It's an app that literally runs in your browser, doesn't require a back -end. And I built, actually, a tool that allowed you to strip out the server part of the Meteor app so you

**[6:31] SPEAKER_00:**
can bundle

**[6:31] SPEAKER_02:**
it as a local app. It's

**[6:33] SPEAKER_01:**
actually

**[6:33] SPEAKER_02:**
quite, – it was quite a popular repository, called Meteor Build Client. And, yeah, that's what I used for D -apps in the early days in Ethereum, too. So,

**[6:45] SPEAKER_00:**
is Meteor still an active project? Is anyone using Meteor still?

**[6:51] SPEAKER_UNKNOWN:**
Yeah.

**[6:52] SPEAKER_02:**
No, I, totally think so. I think so.

**[6:59] SPEAKER_03:**
Yeah.

**[7:00] SPEAKER_02:**
I mean, I don't know how frequent they are.

**[7:06] SPEAKER_02:**
Yeah. I haven't

**[7:06] SPEAKER_00:**
checked it out in a long time. No. But, I mean, it's quite, a revolution at the time, the single -page app. It

**[7:15] SPEAKER_02:**
was the first, you know. It was literally, like, – it was one of the first, – it was the first framework that I know that really was a proper framework. And it's just solved the whole thing from account creation to reactive, DOM updates to server client synchronization. It was magic. Yeah. It blew a lot of people away. And then all the others, React and so on, were kind of more like answers to this. And then React brought it back to the weird way of mixing code and UI in the same files, which I already found very bad in PHP times.

**[7:51] SPEAKER_00:**
Right. Yeah. And then I guess you maybe sort of found your way into Bitcoin world in some form?

**[8:02] SPEAKER_02:**
So, yeah, 2013, I heard about, Canadian wants to sell a house in Bitcoin. And I thought, okay, wow. What's that? Like somebody's selling a house in a currency I've never heard of. And that really led me very quickly down the rabbit hole of, – this was 2013, March. There was literally when Bitcoin hit $200 in that very same month.

**[8:26] SPEAKER_02:**
And number one, I saw, okay, there's money to, be made here. And I, was a student with no money. So, like, you know, trying – like, you have your hope. Okay, maybe I can make a little bit of money on the side this way. But I really quickly understood the fundamental power of this technology. And it took me, like, about a year to really understand how it works fully. I mean, I literally had this epiphany every month that I thought, like, now I know how it works. It took me a year to really construe my brain, you know, knowing servers and frameworks, you know, and how this basic stuff works. And then the crypto, blockchains that were just so out there in a way, how this stuff works. But, yeah, so I, was in the space. And then in 2000, obviously, you know, right after I, joined the Bitcoin community, then there was the first altcoin, Litecoin. And then in 2013, there was a lot of, like, projects that were created trying to imitate Bitcoin or do an improvement or do alternate versions. I also got really into Mastercoin, the idea of just writing onto the Bitcoin blockchain rather than creating a separate blockchain. Right. And

**[9:49] SPEAKER_00:**
you were in Berlin, right? Were you going to meetups or, like, did you find fellows? It was online.

**[9:57] SPEAKER_02:**
There were no meetups at the time, really, like, not in my region. So what actually happened in 2000, and so they were done later, 2014, there were then some meetups. And so I heard about Ethereum. I really knew that. I just felt immediately that this is a really powerful approach, but it also sounded so unrealistic. So when I heard, like, this, I mean, I looked at the white paper. I never really read the Ethereum white paper actually ever fully. I just literally just, like, I skipped over it. And I, listened to Vitalik or, like, the early things that were floating around, and I knew this is it. The idea

**[10:34] SPEAKER_00:**
of

**[10:34] SPEAKER_02:**
making a computation machine on the blockchain makes total sense. I just thought it's so hard to do. And I didn't really give it a lot of chances that. they pulled this off, but then they pulled it off pretty quickly.

**[10:47] SPEAKER_02:**
And it just happened so that I was at a meetup in Berlin, a Bitcoin meetup. I think the first one I was ever at. Right. They wanted to open a, Bitcoin center Berlin. co -working space, basically. Can

**[11:04] SPEAKER_01:**
you imagine

**[11:04] SPEAKER_02:**
what kind of month that might have been? I think that was in, I think it was August 2024. It was literally, like, a week before the Ethereum pre -sale started. Right, right. Like, literally, like, days before. So I met these guys from Ethereum. In this case, it was Aaron, who did the accounting at the time. Yeah. And they told me that they're going to open an office in Berlin, and that there's some kind of news coming out next week, but they can't tell me. And

**[11:36] SPEAKER_00:**
I was already following

**[11:37] SPEAKER_02:**
Ethereum. I was already waiting for the ICO.

**[11:43] SPEAKER_02:**
And, yeah, then it happened. So I took all my Bitcoin that I had at the time, which was 12 Bitcoins, converted them into Ether. I mean, people think, like, oh, my God, 12 Bitcoins, but they were, like, $600 worth or whatever. It was, like, literally not much. I put them all into Ether or pretty much everything. And I knew this was going to be big. I felt it. and, this was also the first time a project where I thought I would love to work for this project because it's not about finance, money, and wallets. Because every Bitcoin startup at the time was just about creating a wallet. And

**[12:19] SPEAKER_01:**
I was

**[12:19] SPEAKER_02:**
really interested in creating wallets.

**[12:24] SPEAKER_02:**
And so it just happened that the same, like, six months later, you know, Bitcoin happened, ICO happened, attention came, blah, blah, blah. But I just got an email from a recruiter saying the company Ethereum is looking for a C++ developer. And I was not a C++ developer. Recruiters don't check anything on LinkedIn, I guess, or GitHub. But I knew that they're now looking. So I went to their office and I just chatted with Aaron again. And I saw they had this office here, Waldemar Straße. And I realized that, okay, like, actually, they're really just thinking that they're going to build the nodes. And then, like, people will build on top of the stack. And I

**[13:08] SPEAKER_00:**
just

**[13:08] SPEAKER_02:**
knew, you know, like, I know how to build Singularge apps. this, is what you need. I knew this is what they will need to make sure, to show what a dApp can, be and show how to, I just felt it. And so I said, like, Aaron, just, can, I mean, I showed him this as well and just ask around, internally. And they had one Skype group that was

**[13:34] SPEAKER_01:**
kind of like

**[13:34] SPEAKER_02:**
the Discord group at the time, yeah.

**[13:39] SPEAKER_02:**
And funny enough, Alex van der Sander is the one who, like, came on on board as the UX designer also just a month before me. And he had this whole idea of, like, creating this missed browser concept. And I think when Alex heard about that there's this guy, you know, that came up here that can build, you know, single -page apps, blah, blah, blah. Then Alex thought, oh, that could be the person who can help with building the missed browser. So you convinced Jeff, I mean, that's my assumption, what happened. And, he tried to call me up. And I was in, Turkey on holidays, so I didn't pick up the phone. And then when I came back, I saw someone who called me up. And somehow, I think I called him back or whatever. And, yeah, he said, hey, you want to work here? We want, to, like, want to do this and this and, la, la, la, la, la. And this

**[14:26] SPEAKER_01:**
was

**[14:27] SPEAKER_02:**
Aaron that you were talking to again? No, this was Alex. Yeah. So I was talking to Afsa. So, Afsa wanted to have me because he, I think he, probably convinced Jeff because he saw this as a guy who can help build his idea, right?

**[14:46] SPEAKER_02:**
And Jeffrey was kind of skeptical of hiring anyone. This is not a code developer. What the fuck can you do, I guess? That's what he thought.

**[14:54] SPEAKER_UNKNOWN:**
Probably.

**[14:55] SPEAKER_02:**
What? JavaScript?

**[14:56] SPEAKER_00:**
Cannot work. So, I mean, you started in, I think it was January 2015. So I guess this discussion would have been in, like, December 2014. -ish. Yeah, it

**[15:07] SPEAKER_02:**
was December, exactly. Yeah, yeah. It was mid of December. I was on holidays. He tried to call me. And he said, hey, can you start? And I asked,

**[15:14] SPEAKER_03:**
you

**[15:15] SPEAKER_02:**
know, when to start. And he said, yeah, start in January. And Jeffrey obviously really wanted to prove me. So he thought, okay, let me just throw a really complicated task at him. And

**[15:24] SPEAKER_01:**
then we

**[15:24] SPEAKER_02:**
fail anyway, and we can get over with this whole thing. I think that's what Jeffrey thought. So he said, okay, build a chat app for the Whisper protocol. So in Ethereum, there was the Web3, right? The idea of Web3 was the network, storage, the swarm, storage, and communication, the Whisper. Which, by

**[15:45] SPEAKER_00:**
the way, I only

**[15:45] SPEAKER_02:**
figured out later that Web3 means exactly these three things. Fun fact. I always thought, it's like, sure, Web2, we go to Web3.

**[15:53] SPEAKER_00:**
But that was, yeah, actually, the three. Probably both, right? It's, kind of a bit of a joke that you've got, both. And I was just looking. So it was November that Alex had done his, you know, missed concept presentation. So I guess that was really quite fresh. It's like, okay, here's the little door.

**[16:14] SPEAKER_02:**
So he had the idea. And then they were working on it already, early December. And I forgot his name. But the guy who, the French guy who then worked on Remix. I'm sorry, I forgot.

**[16:26] SPEAKER_00:**
his name.

**[16:27] SPEAKER_02:**
Oh, Jan Levero. Exactly. So Jan actually built, he built an early version of the missed browser. But in, I think, in C or something like this.

**[16:39] SPEAKER_01:**
And what's that? Aft

**[16:40] SPEAKER_02:**
browser. I think there was one called Aft browser. Maybe. It was really early, early kind of missed. It was barely working. And obviously, the whole of the connection stuff was not figured out properly yet. And they just really realized quickly that this is not the way to go. And that's why maybe Alex saw an opportunity here. with this JavaScript dude showing up with the single page app. Aft book or whatever.

**[17:02] SPEAKER_00:**
Because I mean, you'd had Alice Zero as well, right? I guess that was the very first theory thing. Maybe that's what you were thinking of with Jan? Maybe Alice Zero was the, was. And that was like a really, like, really ugly programmer tool, kind of like million control. Yeah, I think Alice Zero was that early missed browser. Exactly.

**[17:26] SPEAKER_02:**
Yeah, anyway. So, so Jeffrey said, hey, let the guy build. You know, like a chat app in the Whisper protocol. So I got dropped into this, you know, novel tech. No documentation. No idea how this shit works. And I was supposed to build a whole chat app using this protocol. And that was kind of crazy. But because I really knew how to build, you know, single page apps that, like, are reactive. And I could work with Jan, actually, on, you know, he gave me just the endpoints that I need to use to get the account and to do the sending the messages and stuff like this. So I pulled it off and build, like, build,

**[18:18] SPEAKER_02:**
like, a chat app. So in a channel, you could basically say, I want to talk about a certain topic. And then you could filter by the topic. So you could see all messages. Or you could say, I want

**[18:28] SPEAKER_00:**
to only

**[18:28] SPEAKER_02:**
see this or that topic. And it's the same, like, threads in Discord, by the way. Right. So

**[18:33] SPEAKER_00:**
I

**[18:33] SPEAKER_02:**
basically made the thread concept of Discord in this tiny app. Right. And it worked. And you were connected with your wallet, you know, that was in your note, in your geth stored. And I think, you know, Jeffrey was quite impressed. And that kind of gave him some confidence that I can do it, even though he was trying to, you know,

**[18:58] SPEAKER_02:**
prove me wrong or prove himself, right, that it's not going to work.

**[19:05] SPEAKER_02:**
And what's crazy is we literally built the Mist Browser in, like, three months. We built the first working version. And we released it with the mainnet. We released the Ethereum wallet. That was July 31st, 2015. So basically six months later, seven months later, we released the first Mist Browser version. And it was so crazy because everything needed to be figured out. I needed to learn all how this stuff works. And initially, in the first two months, it felt literally impossible. And I felt like there's no way I'm going to figure this shit out. Like, there's no way. There was no documentation. It was completely over my head in terms of complexity and shit that I didn't understand. at all. But I pulled it off. and, I had to, like, obviously, there were people around me that I could talk to. But everybody was also so busy and had to, like, figure out their own thing, you know, because everything had to be figured out at the time. But I had to literally touch every point. I had to, you know, work with the RPC API. And then, I saw this thing was kind of messy. You know, sometimes it was returning hacks. Sometimes it was not returning. So I had to. basically, I thought, I'm a Virgo. So I immediately tried to fix things and make them proper. So I basically immediately, you know, wanted to make sure this is proper. Because when we launched the nodes, this stuff can't change anymore. Because now, once we start mainnet, you know, you don't want to constantly, like, make stuff unworkable. So I had to fight with Gavin to fix and change the endpoints. And that was quite already, like, a little bit of an uphill battle, let's say. Then I had to get into Web3JS, which Marek was working on. Which was the JavaScript library that, you know, I think Gavin and, Jeffrey started. And then

**[21:00] SPEAKER_00:**
I had to

**[21:00] SPEAKER_02:**
help with him or work together with him initially. And then I really contributed to Web3JS because we had to build that into the MIS browser directly. So I was literally the first user of that library and really contributed to that library as well. Right. So we had to make everything up. The whole foundational stack of Ethereum we made up in this, like, first few months. And, you know, because I built the piece that put it all together, like the node, the dApps, the Web3JS, the RPC input, everything into one app. I had to literally touch everything. And I had to go to talk to everybody. That was quite challenging. Not going to lie. and. I also realized that Jeffrey's team and Gavin's team was a little disconnected. And they tried to, like, there was a little, like, battle and war going on, where everybody wanted to be the one who determines which feature and how. And I just realized, guys, if we are doing like this, that shit is going nowhere, you know, if we don't work together. and. it would be too complicated, too much iterations. So I tried to make the team talk, these two teams. But Jeffrey's team, you know, I was part of Jeffrey's team. We were a little bit more open, at least how it felt. to me. Gavin really wanted to kind of keep everybody under a bucket. And he didn't want that, we talked to this team. But I kind of found back, LA ways and back channels to make them sync up. I guess Gavin didn't like that. But it was really needed so that eventually they were starting to work more together and had to do a lot of, you know, connecting, hand -holding. Because I was in this crazy position of being hired by the Amsterdam team while sitting in the office of Gavin of the Berlin C++ team. So I wasn't at the same time as the only person. So I was the connector, you know. I was the translator and the connector, basically. And I had to deal with all the pieces. So I had to deal with, you know, the C++ client had to, work as a client in the missed browser, as the goal client. So I had to talk to people when something was not working. And it's crazy how much happened in the first six months before the network started. I mean, equally on the network side, right? Like, there was so much just being built and done at the time. But the whole dApp, tech stack was literally made up in this moment, in this time.

**[23:33] SPEAKER_00:**
Yeah. I mean, I was just looking at the timeline. So September the 16th, 2015 is when the first developer preview of Myst went live. Yeah. I mean, saying about with the two teams, I mean, I guess you were sort of in the position of being the very first person, like, building one layer up. You know, I guess all of the prior efforts were just about the clients and, you know, and making features available on the clients, but not really building things on top and specifically not building things on top to try and be able to work with either. So those interface issues and...

**[24:18] SPEAKER_02:**
I mean, to be fair, the first dApps probably were built by Gavin and Jeffrey, but they used all the clunky half as stuff. They're only on their own stack, right? And then only on their own stack, yes, I built the first number one dApp browser, like literally generic tool that can run any JavaScript app to connect to the blockchain. And I built it with Alex the Ethereum wallet, which was the first ever dApp on Ethereum, like proper, done, designed, cross -client functional thing. Yeah. That's exactly what we did, yeah.

**[24:58] SPEAKER_00:**
But, yeah, I mean, all of that prior stuff, it was just really on their own stack. A little JavaScript page, talking to their own endpoints, yes. Right. I mean, and looking through old videos, there was one, which I think was a talk in London, where both Jeff and Gav, were sort of talking about the state of Ethereum and demonstrating some things. So this was October 2014. And one of the demos that they had was one of probably the first on -chain DEX. So they were, you'd got GavCoin and JeffCoin, you know, this is prior to any standards, I guess. And GavCoin was written in LLL and JeffCoin was written in Mutant. But they did do, you know, an on -chain DEX order book thing, you know, so putting a transaction for, like, an offer, like, CPU mining, picking that up. So, you know, you have got that interop. And I guess maybe some of the Whisper stuff was maybe kind of cross -client, but you have really got the

**[26:16] SPEAKER_02:**
UI layer. So for the chat app, I mainly used the go -client because the Whisper thing on the C++ client was not fully integrated or working. The initial idea was that the Ethereum client will host all three things, Swarm, Whisper, and. the network. Obviously, the Swarm never really worked in there, and neither Whisper, which then later got overtaken and supported by status, and now it's transferred into a whole different protocol.

**[26:50] SPEAKER_02:**
Yeah, it's interesting. I mean, this was really, like, foundational times. And I think what people really, like, often misunderstand is how much, number one, Ethereum was generic from day one. Number two, how many ideas were already present. earlier. If you watch the misbrowser video from Alex, like, we haven't even built half of this stuff that's in that video. And, in fact, a lot of these foundations are missing. And, for example, now I'm working on universal profiles across a smart content account system. And that's even in the, video already in there. Like, you don't see wallets. You see profiles. You see people doing stuff. And only now, literally 10 plus years later, we now have the foundation, and it's not even widely used yet, that even makes that missed video more realistic. And it's not that Alex came up with all of these ideas. This is just what was around at the time. Even, like, right after Bitcoin got attention in 2013 and 2010, these ideas

**[28:01] SPEAKER_00:**
were

**[28:01] SPEAKER_02:**
already around. Like, how

**[28:02] SPEAKER_00:**
can you build

**[28:02] SPEAKER_02:**
decentralized Uber and decentralized this and decentralized that and DAX and whatever. And it's just people think this stuff came all in 2017, and 2020, you know? Like, and this is somehow, like, an invention of, like, the Ethereum Foundation making shit up, you know? Like, this stuff is all, like, it has been around for ages.

**[28:26] SPEAKER_01:**
Absolutely.

**[28:27] SPEAKER_02:**
We

**[28:27] SPEAKER_01:**
are

**[28:28] SPEAKER_02:**
just

**[28:28] SPEAKER_01:**
behind

**[28:28] SPEAKER_02:**
when it comes to this stuff, actually. Yeah,

**[28:33] SPEAKER_00:**
I mean, you know, you had that sort of cryptocurrency 2 .0 phase at the start there, you know, talking about Mastercoin and things, you know? I guess there was a thought that, you know, everything will get built on Bitcoin, you know? That was the initial thing. And, yes, you've got these altcoins and experiments and other things. And, you know, it might kind of come back together. Or even, you know, prior to Bitcoin, you know, because Bitcoin itself was just sort of a manifestation. Of digital cash streams that had gone back for decades with, the cypherpunks. And then you've got things like BitTorrent. You know, you did have decentralized messaging things.

**[29:17] SPEAKER_02:**
And so on, yes. I mean, I was, yeah, it's, basically, it's interesting. Back in the day, it was all Reddit, right? Bitcoin, like, all, like, today's crypto. Twitter. Back in the day, it was Bitcoin. Reddit. Or Reddit are Bitcoin. And Ethereum was the first kind of real challenger to the status quo. And it split the community into the Bitcoin maximalist, the camp that says, no, we only need Bitcoin. Why the heck? You want any other chain? And then the people, and even if my friends circles, you know, and friends, developers, some literally never made the move. They never looked into Ethereum stack just because they felt that, what do you care? Bitcoin's all you need. And I

**[30:04] SPEAKER_00:**
just

**[30:04] SPEAKER_02:**
visited a Bitcoin meetup recently, and I was so taken back because it was like walking into like, you know, some kind of like a time portal back into the time. And then 10 years back, same discussions, same problems, same people, same size of groups. and, you're suddenly back in some kind of time capsule of the past where the topics that talk about is just like, you know, minor this, minor that, and basic stuff, that has been figured out like 100 times already on Ethereum. Like being full and present discussions here, and very few developers, which is also very impressive, like how such a network that has so much attention, so much money in it, literally just is developed by 100 people and maybe not even.

**[31:01] SPEAKER_00:**
Well, I mean, speaking for myself, you know, I was aware of Bitcoin for a good number of years before I had sort of any involvement in the crypto space. But there were sort of two reasons, I guess I wasn't interested, or maybe three, which was firstly, I was a gold bug, and I was a software engineer, and I know how terrible most software is. So like some dude you've never heard of has made like magic internet money, like, come on. But I think more importantly, it was just kind of boring to me because, okay, you can do payments. Okay, well, there you go. Well, that's not very interesting versus here's a platform and you can build apps. That was like, oh, that's. kind of interesting. And, you know, maybe you had a fairly similar.

**[31:46] SPEAKER_02:**
Yeah. I mean, for me, the money part was, I mean, obviously, it's cool, like, to invest in something that, like, you know, feel is going up and you make some money. And obviously, I had no money as a student. here. My parents are not rich or anything.

**[32:03] SPEAKER_02:**
But it's just like, it was just so powerful, the idea that there is a technology that you can, no one can control, that sits above the law, that sits above the influence of humans, because you can't break a system that's based on consensus. And, like, a Hydra has 100 ,000 heads. And it's just, oh, it's just really, it was fascinating. No, I was really, you know, I mean, I still am, you know, here I am building still on this tank, super pumped about the next phase of this whole technology. But

**[32:47] SPEAKER_02:**
I just never thought it would take that long, to

**[32:48] SPEAKER_00:**
be honest. No, no. So, I mean, you were working from the Berlin office, but presumably you, you know, you were back and forth to Amsterdam sometimes. Ah,

**[32:57] SPEAKER_02:**
rarely. I mean, the Amsterdam office, well, we were there maybe, like, twice or so. Like, on the end, the Amsterdam office was really more like a legal hub. And there was obviously, Jeffrey and the operations personal assistant that he had. And, like, we were all over the place. So, I worked with Alex mainly, who was literally three, two, or five hours ahead, behind in Brazil, in Rio. Later, we hired multiple people. We hired another person from Rio. Actually, we hired two other person from Rio. At some point, we were three people in the team, four people in the team, even, if I remember, at the peak. But then I also worked on Web3 .js. So, I worked with Marek closely, was in the Berlin office.

**[33:43] SPEAKER_02:**
I talked and worked with Christian a lot, who worked on Solidity, was also in the Berlin office. And, obviously, Jan. and the other girl that worked on the remix. Left

**[33:56] SPEAKER_00:**
Harris was sitting

**[33:57] SPEAKER_02:**
across me in the Berlin office. Christoph Jentsch came to the Berlin office frequently. So, he was a guy, right? But he was more, like, hired as a kind of contractor to do, testing scenarios for the nodes. So, he wrote all these kind of tests to test all kind of inputs and outputs of whatever node behavior. I don't remember exactly.

**[34:24] SPEAKER_02:**
Cross -client, make sure this all, like, functions correctly. And, at the same time, the Ethereum hub, I call it the Ethereum hub. It was never meant to be a hub. But it, functioned as the main go -to place. If you want to visit Ethereum, the Berlin office was the place. There was the most people there. And it just really also happened that just people showed up. So, Dominic Williams just showed up before he made HDP. You know, people that I met that, like, really became friends. Gustav, who built a key manager implementation in GoEthereum. Felix, the guy who built still today the network layer. He was also

**[35:08] SPEAKER_01:**
in

**[35:08] SPEAKER_02:**
the office in Berlin. Literally lived across. Right, yeah. And there's a lot of – it was, like, a hub. And I was one of the more social developers inside the group. So, when somebody walked into the office, it was mostly kind of me talking to that person. Because the others just, like, behaved like they didn't know what to do. Like, they just literally, like, didn't. – and there was no secretary person or anything, really. So, I just talked to most of the people. And I also. – what I was working on, you know, working on the front end, working on the developer stack. I was kind of, like, a little bit, like, you know, on the layer to the outside compared

**[35:54] SPEAKER_01:**
to

**[35:54] SPEAKER_02:**
the people working on the protocols in the inside. So, that also kind of reflected socially.

**[36:01] SPEAKER_00:**
Right, right. So, you missed out on Devcon 0 because you, started just after that. But you will have been to London for Devcon 1 in November of 2015 then. Yeah, I was, yeah. And token standards were just kind of beginning. The EIP process was just starting. So, I mean, I guess that's sort of like phase two, right? Is your first one is, you know, building a thing and touching everything. And then you're starting to get up to that, you know, on -chain token layer. So, how did all that kind of grew up?

**[36:46] SPEAKER_02:**
So, I mean, the whole standardization for me started when Vitaly created the GitHub wiki page because he wanted to standardize tokens, ENS kind of registry, and maybe an early version of a DEX, I don't remember. And he just, like, we had some discussion around a GitHub page, literally, a GitHub docs page. And he made the early version of ERC20, and we debated a little bit on there, on, mainly, like, you know, Skype and some comments on, this page. And then, yes, and then London happened. And so, what happened is it's actually funny because there was this, there was a panel. It's a panel about standardization. So, I presented a lot of things there. I presented the missed browser. Yeah, I think I presented the missed browser. Maybe something else. But I was also on this panel about standardization. And fun fact, we discussed, I watched it the other day, and we discussed, you know, standards. And there was two main discussions. Oh, should we put metadata into the contract directly? In this case, the idea was, do we put the metadata of a token, like token name and symbol, into the contract? Or do we create a registry for it? Right. And in a way, that's kind of also today still the big split. You know, do you put information into a registry, like ENS? Or do you put it into the user -owned contract itself? Or do you make a registry for AI? Or do you put the metadata in the account of the AI itself? And it's still, and it's going to be another discussion coming, funnily enough. And we literally discussed this. And actually, what's funny, when I looked at this, I, literally said, they asked us, what are you interested in in standardization? And I said, you know, the account system. I called it proxy contract because there was no notion of an account. But I called it the proxy contract was actually my main interest. Funny enough, I later created ERC -725, and now Universal Profiles as the fulfillment of that. But it's kind of funny that it wasn't even sparked there already. I talked about key management at the time, and we didn't even propose ERC -20. It's kind of nice. So, but in this conversation, Martin Deasy before created the EIP repository. And I think Gavin or whatever mentioned, like, where do we do the standardization? And I think he mentioned in that very thing, yeah, we have the EIP repository. That would be the right place. And I think that inspired me in this moment, like, oh, yeah, actually, we could put it there. So that's when I then created this, the issue number 20. And I, think I recall the Ethereum request for comment because of the request for comment thing. I'm

**[39:46] SPEAKER_01:**
not

**[39:46] SPEAKER_02:**
sure, you know, I came up with the name by myself or whoever came up with the name. But I created the issue, and I formatted the whole discussion that we had there, like a current version in a proper specification. Because I felt, number one, we need to involve the community. Like, if you want to have a consensus around the token standard, right, everybody needs to listen and have at least an insight. And second, it needs to be in a structured way where not everybody, like, randomly edits, like, this file. And this is actually the exact comment that Gavin made, funny enough. Editing, we all laughed about editing was on that one wiki file. Yeah. In a way, like, I. then structured the process through that and created EOS 20. As a proposal, I made a few changes that's, like, just, like, some filing, like, some turning around, like, the transfer function, what's first, value, blah, blah, blah, blah, or amount or whatever. And then we had a discussion, but we didn't really change much anymore.

**[40:50] SPEAKER_02:**
And, yeah, so we discussed there about 60 people in total, 300 comments. But pretty much after quite a while already, everybody kind of felt more or less that this makes sense. The big discussion was around authorized operator or not, should we have it or not. I was kind of against it. So, fun fact, when I create the first test coin, the missed coin that I used then to test in the missed browser,

**[41:14] SPEAKER_01:**
I

**[41:14] SPEAKER_02:**
did the authorized operator functions. And because I didn't like it, I really liked more the idea of informing recipients, but I was also too early to do that because we had no idea of the side effects of that. Right. So, in my test coin, I just didn't add the authorized operator. I didn't see a need. Fun fact, later, people picked up the missed coin, like, as a collectible meme token, collectible coin. And because it was a real ESC20, but because it doesn't have the authorized operator function, it didn't work in Uniswap. So, they wrapped it. And that's

**[41:51] SPEAKER_01:**
why it's not a

**[41:52] SPEAKER_02:**
missed coin, which is the real missed coin inside a token that has the function to interact with DEX. But this was just a test token. It was never meant to. I just, over the years, gave a bunch of those to random people who asked me until, like, a whole group of people, like, really wanted to make this valuable. And now it's traded. I mean, now it has a market cap and people trade it. And it is what it is. I mean, it's the first ESC20. I mean, it's not the first first. I think there was a preliminary version that Vitalik built before that that was. not very functional or standardized. And this was, like, the first one that kind of fit the spec, except

**[42:36] SPEAKER_00:**
the

**[42:36] SPEAKER_02:**
operator stuff.

**[42:39] SPEAKER_00:**
So, there's a deployment of that out, which was launched, I believe, by RFiki, based on Vitalik's, repo or what have you there, called CurrencyCoin, is. what that one is called. But, again, another, they call these relic tokens, relic coins. Yes. like, I'm doing sort of human social history. There are people doing. on -chain history of, you know, what was the first

**[43:16] SPEAKER_02:**
instance. of that. I mean, it's also the crazy thing is, you know, the stuff is around. The transaction is around. The code is still around. It's like a relic. And it's, like, it's provable. the thing. And the fun fact is I deployed that, I think, a week before I actually proposed the ESC20 spec. Right.

**[43:35] SPEAKER_01:**
So,

**[43:36] SPEAKER_02:**
I felt that we were kind of more or less, and it was probably around the time of this first DEFCON. I might have, we can't even check if it was before this DEFCON or after, or. I don't

**[43:46] SPEAKER_01:**
remember.

**[43:46] SPEAKER_02:**
But probably maybe a day or two before that I deployed that thing. I think we also, yes, we also needed it for testing or showing something. I don't remember. But, I mean, yeah, we needed to test, you know, like, how could tokens work in there? or whatever. But it's really, yeah, anyway,

**[44:05] SPEAKER_00:**
that's how it happened. It may well have been for the. DEFCON 1 demo for your presentation.

**[44:12] SPEAKER_02:**
No, I mean, we did it for, I mean, yes, DEFCON did really, like, you know, push us a lot to get some features done and some things done. The token was not yet in there, really, because the token thing was still kind of very out there. Like, also, no one really had, I mean, we all knew that people want to make tokens. And that's why kind of, like, you know, Vitalik started this, because I think he felt an urgency from the community. But, it was not of anybody's mind that now tokens need to be, like, a primary focus. It was just

**[44:43] SPEAKER_01:**
like, hey,

**[44:43] SPEAKER_02:**
do it, let's do it. The wallet was not really meant to immediately be super supportive of that, except that I created the test card for that. And we played around, but it was not an urgency.

**[44:56] SPEAKER_02:**
That just really didn't happen after this, then, ERC -20, then kicked off the ICO wave. And that's when everything went completely bananas.

**[45:06] SPEAKER_00:**
And, I mean, I'm guessing, you know, that ERC -20 standard, you had no idea that it would have so much sticking power.

**[45:14] SPEAKER_02:**
No. I mean, no one could. I guess no one could. I mean, I knew people needed it. I knew it's going to be a thing that people will do, because already on MasterCoin before, there was colored coins.

**[45:28] SPEAKER_01:**
Yeah.

**[45:29] SPEAKER_02:**
The concept of creating other currencies on top of the Bitcoin blockchain, and they

**[45:33] SPEAKER_01:**
call it

**[45:33] SPEAKER_02:**
colored coins. So, there was clearly a, need for it. But I found the idea of just creating random tokens for random stuff, kind of boring. Because for me, then, it's like, okay, let's know what is the value of this, you know? Why would you create a token? And, honestly, if you look back, and if you look today, most tokens don't make fucking sense, right? Like, there was so much unnecessary tokens that just make no sense and had no purpose. And I was always a big fan of, like, a native currency, or a native blockchain token, because that thing makes sense. Yeah. You remove it, the network doesn't work. There's no way you remove that token, at least right now, and the network still is functional and economically, viable and secure. So, but with all the other tokens, that was not the case. Like, I

**[46:27] SPEAKER_00:**
guess it's just sort of, like, the simplest thing you could do. It's like, okay, well, what can you do? Well, hey, look, you can make new tokens. So, there's no need to, like, make new, you know, new chains and find new miners, right? You can just float it on Ethereum. So, it's like a simple thing. But it's like, okay, here's the very first sort of thing. It's not very interesting. But, you know, we've done something.

**[46:51] SPEAKER_02:**
The thing is, like, what people don't really realize, how much more we were thinking ahead of, like, hey, wow, we can do really cool, how we can really change society with this technology. That, was actually more interesting to people working in Ethereum than thinking how to make a fucking token. And how to, like, the whole Dex, DeFi stuff, like, mainly came from the outside, too. It was other people that just saw an opportunity to make money or financial Lego, whatever. And, but internally, there were not a lot of people who got very excited about this, honestly. I mean, as far as I remember. Or maybe that was at least my perspective. Yeah, yeah. So, I mean, DEFCON won. There was also more speculation, right? And more speculation is not necessarily good, specifically in an environment in the early days where the regulatory, insecurity and uncertainty was just so high. So, the last thing we all wanted is now every eye is on us because we're trying to compete, with banks. So, I think it actually made us all uncomfortable. At least that's how I felt about it and how I think other people saw it, too. It's just the outside world, like, immediately jumped on it. Like, yeah, money, money, money, money. You know, and that was not the point of the technology in the first place, actually.

**[48:11] SPEAKER_00:**
No, no. I mean, I, sort of remember at the time thinking, you know, that's one of the least interesting parts. It's like, you know, okay, yeah, you can have that raw speculation, but it's like, that's nothing new versus going, well, what are all these new things that we can build? Yeah, exactly, exactly. Yeah, so, I mean, DEFCON 1, I think, was quite seminal in terms of, like, bringing together, like, most people for the first time in the DEFCON 0 being this internal event. But, you know, DEFCON 1 was, it was like the first public Ethereum conference. I sadly did not get to go. I. could not afford to go. But. what are your memories at the time? I mean, you must have seen so many things and so many people. Yeah,

**[49:00] SPEAKER_02:**
so I have actually been in, I think I have been in every DEFCON so far, except Zero, which was only 20 people in Berlin. And I was not at the DEFCONnect in, Istanbul. Right. Apart from that, I was at every DEFCON. I was always speaking at the first few DEFCONs, but then the moment I was not at the foundation anymore and doing another blockchain, then you're like, oh, outcast, you know.

**[49:28] SPEAKER_02:**
And, yeah, it's, yeah, it is, it is what it is. So, even though the tech I'm building now and the tech I have been also building over the years is extremely relevant to Ethereum, the ecosystem as well. But somehow, also the people who pick them, to talks and so on in the later years, right, they are fresh. Some of them literally don't even know the history. So, that's why, actually the work that you're doing is really important because you are the archivist, you know, of Ethereum. And you really, like, with that, hold up the truth story and the participants and the contributions and make that visible and transparent to people. Because I have talked to so many people and they have barely any idea of what, like, how Ethereum came to be, who contributed, who did what. It's, like, completely unknown. people just, like, you know, came in in 2017 for ICOs, 2020 for ICOs and DeFi, 2022 for NFTs. And for them, Ethereum is just one chain. There's all the other chains and they do AMAs, and Ethereum doesn't do AMAs. And it's, like, it's all a big shit show, honestly. So, it's good that the work that you're doing, like, kind of a, Because. I have, and there's so many contributors that have not gotten the recognition that they deserve. I mean,

**[50:46] SPEAKER_03:**
Felix, for

**[50:47] SPEAKER_02:**
example, in my opinion, it's a great example. That dude literally built the, and it's building still, the communication layer of the Ethereum network and how the nodes talk to each other. And he has done that without fame or attention for years. and.

**[51:03] SPEAKER_01:**
Felix, man, this is,

**[51:05] SPEAKER_02:**
sorry. Felix Lang? Yeah, Felix Lang, exactly.

**[51:10] SPEAKER_00:**
Yeah. Yeah, I mean, I, spoke to him in Buenos Aires. And the funny thing is, he, like, he's such a humble guy, you know. You know, he was saying to me, you know, I really don't like early days of Ethereum. You know, I don't, you know, I don't want, you know, I don't want the attention, you know, like. Like, so I was saying to him, you know, like, you're, you're, like, the longest serving person at the EF, I think, after, after Vitalik. And he's like. That's

**[51:44] SPEAKER_02:**
true.

**[51:44] SPEAKER_00:**
You know, he's like. I'm just like a janitor, you know, I'm, I just turn up and I maintain the thing and I, you know, I don't, I don't, want any of that focus. I don't like any of that. It was just like a job for me, you know.

**[52:02] SPEAKER_02:**
I mean, Felix is specifically crazy and I think there's a little self -punishment, but he didn't even buy any Ether, you know, at all. So I literally, and then because I thought, like, what the fuck are you doing? I mean, this is likely, I mean, I knew this is going to go big, just because I knew this is such a revolutionary technology. And, and I just, and I couldn't barely afford any, but, but, I thought the guy has none. He said, yeah, if I don't have a use for Ether, if I don't want to build an app, why would I need some? And I was like, and I thought, that's kind of stupid. I mean, I mean, because you invest in your energy and time here, like, you should have at least some reward. And what people don't understand, most people that worked at Ethereum didn't care about the money or an investment. Neither did I. I mean, that was not the reason why we joined. And we joined because it was truly, and it is truly a game -changing revolutionary technology. But so what I did is I donated some to him and I made everybody in the team donate some to him. So at least he got like, I don't know, a hundred Ether or whatever.

**[53:09] SPEAKER_02:**
I don't know if he kept it or not. I mean, I guess he did. And I even made Jeffrey give some. and Jeffrey gave almost the same amount like us. I mean, we had barely any, but Jeffrey has a fuckload. It was so weird. I was like, dude, Jeffrey, you can give a little more. I found a little knauser.

**[53:26] SPEAKER_01:**
Yeah.

**[53:27] SPEAKER_00:**
I literally forced him to his detail, basically. I mean, I think the thing that a lot of newer people, you know, don't comprehend is how little that, money or whatever was on motivation at all. For many of the people, you know, it was really about, well, what. can you build and what. can we, you know, what can happen? You know, like, there was no certainty whatsoever that it was even going to work. It was even going to launch, but it was even going to have any kind of, you know, success. It was like, you know, maybe this can. think that happened. You know, it would be great if it could. Like, let's try. But, you know, this money was never.

**[54:05] SPEAKER_02:**
the money was never the intention of no one that I, know. So, I mean, obviously, some of us felt, I mean, that this can be big, but we had no idea. And at the same, time, there was Bitcoin rising. And obviously, you know, Bitcoin had a lot more traction, and Bitcoin was more of, a safe bet. Ethereum was a complete gamble. And when I, you know, donated this, Ether, also, people say, well, you gave him 100 Ether. I don't know how much he on the end got, but it was like, I don't know. The whole thing was $300 or $400. It was nothing. Like, it cost literally 40, 50, 60 cents. And, like, it was not $3 ,000, nor $10, nor $20. It was literally nothing. It was a few hundred dollars. And it was all, and we had all, like, you know, 10, 20 Ether on some wallets laying around just for building stuff. I hope I could find some of those again. But all these keys were ethereal and some code base, maybe, or maybe not, whatever. Yeah,

**[55:10] SPEAKER_02:**
nobody cared really, actually, to be honest. Not of the people who worked internally. But from the outside, they all thought we all just did it for making this thing, you know, big and get rich. It was weird, you know. The perception, on the outside is sometimes really, like, distorted.

**[55:28] SPEAKER_00:**
Yeah, I mean, you know, talking to that ICO and, you know, that monetary speculation, I mean, I remember at the time, you know, almost being sort of, like, repulsed at that, you know, that speculative thing. and. especially the projection of that mindset onto the people that we're actually building and saying, oh, you know, you guys. Yeah, you're just

**[55:48] SPEAKER_02:**
doing this to grow it. Exactly.

**[55:51] SPEAKER_00:**
It's a free mind. You're just giving yourself the money. You know, it's just, like, who needs smart contracts? You know, it's all a scam. Look at you guys, you know. And also, I think, also the assumption,

**[56:04] SPEAKER_01:**
oh, you're

**[56:05] SPEAKER_00:**
all massively rich. Yeah, yeah. Yeah, yeah. I, mean, it's so wrong. You know, Felix thing of not having any F. That was, me as well. And the reason why is because I haven't got any money. I haven't got any money. Like, I was impoverishing myself, even being involved, you know. I was just volunteering for a very long time, like, with nothing. And then even when I got hired at the foundation, I was getting paid 60K a year, which was, like, half of what my prior salary had been. It was not.

**[56:37] SPEAKER_02:**
And also, I mean, same for me. My salary at the foundation was 60K. And only towards the end, when we had a little bit of success, I negotiated it up to 90K. And that was, you know, before tax. And same with the Ether. It's like, you know, everybody thinks, yeah, if you got Ether back then, you must be insanely rich. It's like, dude, like, when that hit $10, we all thought we made, it to the universe, you know. And, like, now you cash out, like, a few hundred thousand and you think you're super rich. Same with also some of the early people who had a lot more Ether. I mean, they cashed out 100 ,000 Ether, like, for, I don't know, a dollar, right? Because they thought this is really high. Yeah. I mean, barely anybody that I know held it until it, like, hit a few hundred and thousand of dollars. And people don't understand. They were 10 plus years or now 10 years. And they were, like, five plus years passing with many ups and downs and bubbles. Obviously, I mean, I have no Ether anymore since many, many years. I mean, I spent them all. And, you know, my ex -wife has a few more ideas of what you wanted to have it on. And then all the house that now belongs to the parents of her and stuff. just, like, when, when, and then, you know, obviously, I'm working on Luxo. And a lot of my money went all into supporting that now. Yeah. So, the idea that, like, I mean, if I would have held everything that I had, sure, that would be a lot of money. But that means you're literally not spending any money during all the years and you only live with your salary. And second, you literally trust so much that this is going to be worth a lot. And it's impossible. Like, barely anyone. It's such a

**[58:22] SPEAKER_00:**
naive thinking, honestly. It's this sort of impossible fantasy of saying, you know, assuming that, yeah, you're going to sit and you're not going to, you're going to say, okay, it's 100x. No, no, no. It's 1 ,000x. No, no, keep

**[58:37] SPEAKER_02:**
going. I know 10 ,000 % is possible. Yes.

**[58:42] SPEAKER_00:**
Yeah. So, I mean, going back to Devcon 1, I was looking at some of the videos recently, and it's, like, pretty much any idea you could ever imagine seemed to be presented there. I mean, did, you see most of the presentations?

**[58:57] SPEAKER_02:**
I mean, this is the thing most people don't understand. Like, this shit that people talk about right now is not being made up. now. That stuff has been made up before, tried before. For example, base, like, launches, launched, the feed that they're now cut off again, right? Like, where you have a post and then people bet on this. I mean, Steemit did that four years ago. And at least they did it smart because it wasn't a Reddit -style feature. where Reddit -like posts stay longer, right? They have more value over time. And while posts that literally disappear after scrolling a page, it's not worth betting on them. That's fucking scamming people, right?

**[59:37] SPEAKER_02:**
None of that stuff we see is new. And what is fascinating to me is that the space today is still built more or less on the same foundations. On the basis, if you go to the bottom of the bottom, it's the same foundations that we literally made up in the first six months and the first year of Ethereum. It's the same provider. Now there's a bit of a different way how it's injected. Same provider. How your DEF connects to the, node.

**[60:08] SPEAKER_02:**
Same RPC endpoints. Pretty much not too much added here either. EOAs have been the default since back then. And fun fact, Jeffrey told me, you guys should not expose the public key or the public key, the EOA, to the user. You should use a smart content account. And that stuck with me. And he was right. But it was so early. We had no idea. I mean, we tried to barely figure out how to make any transaction work for that matter. And now think about routing this through a smart contract. That was just absurd. But he was right. And now in all these years, that's what I built. Now I built exactly that kind of foundation that we discussed back in the day and that we wanted back in the day. But it took all of this learning and all of this, and in fact, it also took me stepping outside, out of the theme ecosystem, creating a different standards track in order to even do that. Because when you just do that in this existing ecosystem, with existing standards debates, it's just so slow. And you need to be backwards compatible. You need to think in ways that you just move the current wagon along. Because if you want to make radical changes, you have so many people that will just try to either intervene or move it around and shift it around. And it goes nowhere. So I needed to do that in a kind of different approach. kind, of funny enough, you know, I kind of coined the ERC request for comment standard space to then go off and create the Luxor standards proposals, and do it there, even though that's just Ethereum standards too. Just so that I could do it right. And it's going to show. That video will be obviously on the internet. So let's see, in a few months, in a year from now, and it will show that that was the necessary approach to evolve.

**[62:16] SPEAKER_00:**
Yeah, yeah. So, I mean, you were at the EF, working on MIST through to 2017? No, August 2018. 2008. 2018. 2018. So, I mean, what further work happened in MIST between that very first release and the sun setting? I mean, what was that? further?

**[62:43] SPEAKER_01:**
Yeah, so my

**[62:44] SPEAKER_02:**
work was not only in the MIST browsers. So I actually worked for three and a half years at Ethereum. And then in the later years, I, really started working more on the developer tools. I mean, I overtook Web3 .js, which was the main JavaScript library at the time. When Marek left with Gavin, to join Parity or ETH Core, I overtook Web3 .js. So I mainly maintained this library. I built the Web2, the 2 .0 version of it. That was the last thing I did before I left. Right. Releasing the 2 .0 version of that app or that library.

**[63:26] SPEAKER_02:**
And I kind of stepped in the last year, I stepped a little out of the MIST team. I mean, I was just focused on the other things more, but I was still like, you know, you know, kind of the main developer in MIST. But now there was more maintenance.

**[63:42] SPEAKER_02:**
The thing is, we really tried to create more of the MIST browser. It was quite complicated because we were always lagging behind Chromium and Electron .js. So Electron .js used Chromium. Chromium is what we then used. And so if there was a bug or something like this in Chromium, it needed to first be supported by Electron .js before we could support this. So it was quite a cycle. We worked a lot on the interface. On the end, like the Ethereum wallet, or people called it the MIST wallet, was basically the main thing ever really used. People never really fully used it as a Web3 browser. But we built all kinds of features in there. I built things in there that an app could set notifications on the sidebar. And so there's a lot of features that we added to the browser that were never really fully used. Just because the moment, the biggest problem for the MIST browser, and in a way, the death of the MIST browser, was the slow syncing of the Ethereum nodes.

**[64:44] SPEAKER_01:**
Yeah,

**[64:44] SPEAKER_02:**
yeah. And because we wanted to do it the full, decentralized way, we didn't just want to talk to a backend node that someone hosted. And also, the Ethereum Foundation probably wouldn't have paid for a node hosted on a server for everyone else to connect to.

**[65:03] SPEAKER_00:**
I completely believe that. There was so much peeping

**[65:07] SPEAKER_02:**
out

**[65:07] SPEAKER_00:**
on costs.

**[65:08] SPEAKER_02:**
It would have been so easy to, instead of talking to the local host node, to talk to a remote node. I mean, I could have added that feature. in no time. The reason, because we didn't do this, because it really just went against the whole idea of really doing it decentralized. The only problem is that then after, you know, six, seven, eight months, syncing the MIST browser, if you didn't have it open for a week, took sometimes half an hour. and plus. So what happened is, Metamask, you know, came up, you know, Kumavis came up with the idea, okay, I built a browser extension, connected to a remote node, and I do a light version of Metamask. And I just injected it into an existing browser. And that idea won. So Metamask kind of like, in a way, outcompeted the MIST browser. And then on top of this, you know, the difficulties of keeping it secure is on the end what made us shut it down. But then we had a lot more ideas. I mean, look at the video. Like, we hadn't even started, we hadn't even really started playing out the idea of the MIST browser fully. But at the time, it was just not, it was not the right time. But it really showed a lot of people how things can be done, why to do it this way, how to build the apps, how to, you know, yeah, it set the stage, basically.

**[66:31] SPEAKER_00:**
Yeah, I mean, in terms of that, you know, local, node, full decentralization, I mean, I remember as well thinking, yeah, of course that's going to happen, right? Of course, you're going to, like, everyone's going to have an Ethereum node running, like, on every device, you know. It'll be like, yeah, you'll have one running in the background. on your phone. They'll be in, like, every router, media station, like, every computer. Also, there

**[66:57] SPEAKER_02:**
was the idea of the light clients, you know, and we knew there were light clients coming. And we really bet on the fact that the light client will solve that problem. Yeah. The only problem is the light client never, came, or it came, but it was not cross -clined, and it didn't really fully work. So, yeah, we hoped a lot on the light client. This was why we kept doing it this way, because the idea was, once you have the light client,

**[67:23] SPEAKER_00:**
the thing is like this. Yeah, so, you know, we'll just build on the full node, build on the full node for now, and then, you know, that light client will come in.

**[67:33] SPEAKER_02:**
And I think we actually came that far. I mean, I think there was versions of the misbrowser that had guests built in with light client support that synced very fast. But at the time, by this time, you know, people already really moved on to MetaMask. And, again, security and other reasons on the end, like, made us kind of, like, you know, give up. But I already moved on to Web3JS at the time, mainly with my focus, because that wasn't the tool. Everybody was using it. Yeah. I mean, 70 million, 140 million downloads. God knows what it has nowadays. It's still used to download a lot, even though now vm, and others took over.

**[68:12] SPEAKER_02:**
And then at some point, it was only mainly, like, then, yeah, when I left, then at some point, Alex shut it down for the reasons also, because, yeah. I mean, it had, its purpose, you know. Yeah, yeah. And, by the way, the idea of the misbrowser is still a very valid idea. And, in fact, you know, what I'm building now is a cross. It's like a misbrowser mobile, which is actually interesting, because what I'm building now is almost like a full circle.

**[68:43] SPEAKER_01:**
Yeah.

**[68:44] SPEAKER_02:**
Yeah. So, I introduced a smart content account, the same like Jeffrey said, we should do it. That's the foundation of your access to Web3. And then you have a web browser in an app that allows you to interact with the apps easily while doing it in a human -focused way. So, not wallet -focused way, but profile -focused way, safe way, easy gas, in a way that, like, literally works for humans. Which was also, by the way, the idea of the misbrowser. It was not to be meant for nerds and techies. It was meant to be normal people interacting with this new technology,

**[69:24] SPEAKER_00:**
right?

**[69:24] SPEAKER_02:**
That was the whole point. And this is going to come now with the Universal Profile app as kind of like a misbrowser on mobile in its first version. Yeah,

**[69:35] SPEAKER_00:**
I mean, you know, the goal being not just to sort of replicate existing applications, but on the blockchain, but to enable these things that, like, weren't possible before, right? Having this, hub, integrating all of these different pieces of your life, that was, like, real utility.

**[69:57] SPEAKER_02:**
Exactly. And what's actually interesting, and that's really, for me, the most surprising thing, is, we are 10 plus years into Ethereum. Yeah. And there's so many networks, EVM, apps. The most ones are very financial -focused, which is also something that really turned me then off. So the moment DeFi happened, I thought, like, that's just a big gamble park. I mean, it's important protocols. They're really important, but it just became such a gamble park and casino that it was just really turning me off. But what's interesting is we go to conferences. You know, we go to any place you can go in the world, and you meet Web3 people, and no one is using Web3 apps. Like, literally. Like, you have some, obviously, people have wallets, and maybe they're purchasing a coin here and there. But, like, interacting with actual apps, like voting

**[70:52] SPEAKER_00:**
on

**[70:53] SPEAKER_02:**
something, joining a community, giving reputation, doing all the things you could do on chain, it doesn't happen. And honestly, that, for me, is something I would never have thought. If somebody would have told me in 2015 or 2016 or 2017 that in 10 years there's still no actual users using the apps, I would have thought, like, number one, if that happens, it's a total fail. Yeah. And number two, there's no way this is true. Like, what are the chances?

**[71:30] SPEAKER_02:**
And here we are.

**[71:32] SPEAKER_00:**
It's funny, crazy. I remember in 2018, I went to the consensus, conference, like the Consensus, not Consensus, conference in New York, so New York Blockchain Week, and there was a panel there that was sort of almost like a Bitcoin versus Ethereum thing. And you have Jimmy Song, you know, fucking dickhead with his cowboy hat, and you had Joe Lubin. And Jimmy was basically saying, you know, like, dApps are, you know, useless, smart contracts are useless, like nobody's going to be, like, using these in five years. And, like, him and Joe having a bet, you know, for a pretty significant amount of, Bitcoin. I can't remember what it ended up being in the end. And I don't know what, you know, but then they were, like, talking about the terms. It was this crypto, Twitter, ongoing discussion of, is this, you know. And luckily,

**[72:33] SPEAKER_02:**
he didn't, like, propose to cut off his penis.

**[72:36] SPEAKER_00:**
Yes. It's not, McAfee. But, yeah, it's disappointing. That's for sure. You know, DeFi is working. You know, stable coins are being used.

**[72:53] SPEAKER_01:**
I

**[72:54] SPEAKER_00:**
mean, the whole financial

**[72:54] SPEAKER_02:**
Lego works, yes, but only with the people that went through the hoops. And now, obviously, you have Robinhood and all of the other apps that integrate and make it more easy. So the whole trading part, sure, that worked out. Like, you know, people buying, and selling, and there's a big – but the normal user using Web3 infrastructure in their daily lives, non -existent. Non -fucking -existent. And. I, for myself, I know why. And I spent the last seven years just thinking about that and how to solve that. Like,

**[73:26] SPEAKER_01:**
this

**[73:27] SPEAKER_02:**
is what I am working on now.

**[73:32] SPEAKER_00:**
So how did you come to leave the EF and what was that journey like? And then what have you been doing? do? you tell me about, all your work there? Yeah,

**[73:45] SPEAKER_02:**
before we do this, I need to go pee. So you

**[73:47] SPEAKER_01:**
need

**[73:47] SPEAKER_02:**
to look at the timestamp and, then.

**[73:50] SPEAKER_01:**
I will come

**[73:50] SPEAKER_02:**
back and talk about this. This is too much tea.

**[75:07] SPEAKER_02:**
Sorry for the interruption.

**[75:09] SPEAKER_00:**
No worries. So, yeah, I'll cut it and I'll just ask again. So, yeah, why don't. – could you tell me a bit about how you came to leave the EF and what, like, your motivation was? and, what did you, you know, what did you do and what have you been doing?

**[75:31] SPEAKER_02:**
So, well, actually, I mean, I was kind of in a way, in a good place. You know, I worked on Web3 .js. The developers loved me because I built their foundational piece. The misbrowser was, you know, I mean, kind of like a bit fading out, But, it was cool too. I was kind of in a good place. So,

**[75:55] SPEAKER_02:**
actually, what happened is, like, you know, my ex -wife at the time, she had this idea of, you know, hey, let's do something with fashion, lifestyle on the blockchain. And I thought, like, that sounds super boring. Like, and also I know that there's so many people who already, like, try to do something like this.

**[76:14] SPEAKER_02:**
But then I thought a bit about it and thought, like, hmm, but we can use lifestyle and fashion, specifically when you get big players and, like, mainstream normal users through these brands and whatever. And we can get mainstream people, normal people, into using this technology. that could be the Trojan horse of how we make this technology attractive and interesting to people outside of the trading. So, I thought, actually, this is kind of genius. But it also sounded like a lunatic, crazy idea and completely out of my league. So, initially, I thought, okay, I can support Marjorie a little bit. You know, she does the project. I can help. a little bit of advice. And she, like, does it. At the same time, I worked for three and a half years at Ethereum. You know, I mean, I did kind of, I did all the foundation work I needed to do. I felt, okay, I did everything I can do here. I can now continue here for another 10 years. But I don't think I'm gaining a lot more, you know, from now, from this point on.

**[77:18] SPEAKER_02:**
And in hindsight, I'm right, because when I look at others, that's still there, I mean, it's not that the world changed for them, you know, in terms of what they're working on. It's the same thing.

**[77:30] SPEAKER_02:**
And then at some point, you know, when we started, you know, pitching out the project or, like, pitching, deteriorating the project and mapping out. And someone just, Marjorie, kind of really forced me. Either you're all in or you're out. And then, I made this kind of, and she was a tough person. I mean, it's just kind of, That's, her character. But, in a way, it kind of forced me to say, okay, now, do I want to stay here at Ethereum, kind of comfortable, but now for indefinite whatever? Or do I just go all in? crazy risk? You know, something new, something different. And I knew my Ethereum colleagues would think, what the. fuck, His. girlfriend just twisted his head. Now he's just doing some centralized fashion shit, blah, blah, blah.

**[78:16] SPEAKER_02:**
While at the same time, I knew this is a path for real adoption. And my idea, obviously, was a little different than Marjorie's idea. While she wanted to do something with fashion, I just wanted to create an infrastructure. And then use her, you know, fashion connection friends and the people that we had initially, you know, helping with the project, who had the connections. As a kind of tool to get the users and people into using this technology. And at the same time, I also came up with a standard called ERC 7 to 5 before Luxor. It's 7 to 5, which is one standard before 7 to 1. No, one standard after 7 to 1. Even though there's three other issue numbers after, but there were nothing in the middle. It was a proper standard really. after. And so that was a coincidence how I came up with 7 to 5. I was at the BCG workshop. They wanted to make identity on the blockchain. I was the only one really coming up with something concrete. And after I felt I made this smart contact account system. I call it proxy account. Same like we call. it 2015 at the panel, funny enough.

**[79:26] SPEAKER_02:**
And then, and I had this urge after this whole workshop series that I need to propose this as a standard. I just really, like there was something in me telling me, you need to put it out there. And I had no idea why. And I didn't want to because I was fine, you know, with what I was doing. I didn't really need attention on anything. But in the moment I put it out there, suddenly the whole theme space, or like a lot of these developers were, my God, this is the Ethereum identity standard. And a lot of projects came and they created the ESF 7 to 5 Alliance, the origin protocol. and, then Uport got super pissed because Uport, which was a consensus identity protocol at the time, thought like, what the, fuck? Why does now this Ethereum standard? and we are working on this Ethereum identity for the last year. And now Fabian comes and just makes a standard and everybody pays attention and what is going on here. And then they wrote a big blog post, how Miles is this massive monster and there is this modular system. And I didn't want neither the attention on that, nor did I even care.

**[80:33] SPEAKER_02:**
I knew this was an early draft of the, standard. There needs to be a lot more work. But everybody kind of, of these people treated it like it's the final thing. It's like, Ethereum identity is now here. And it's like, man, guys. And I thought, okay, you know, if you're all excited, then someone, you know, becomes you the lead and you guys just build it out. Fine with me, I'm out. But then when we started Luxo, which was a few months after, I realized, oh, wow, if I want to make a chain, that's for normies, that's for culture, creators, and anything outside of finance, identity is the most important piece. If that's not there, if a company or people or non -technical people cannot use an on -chain account properly, like UX, right, needs to be easy. And if that thing is not, like, ideally unlosable, like, there's no way you can put these people on chain. This is not going to work. They're not going to run around wallets with private keys that I need to remember. Like, there's no way. So I knew I now had to literally build out a standard full on.

**[81:51] SPEAKER_01:**
And

**[81:52] SPEAKER_02:**
that was really annoying because I didn't want to do this at all. Because I knew there was quite a lot of stuff missing. And it was just – and in hindsight, honestly, it was a complete psychotic idea. Because it took me, yeah, four years to build out the foundational standards, like, full on. Like, and then obviously now it's almost eight years to really put the – put it to a state where it's now literally usable by people. Currently only on Luxor, but it's going to come to all other chains, including Ethereum, very soon. And now it's being used by AI. Fun fact. In fact, that's also a little bit. – I knew it's currently possible, but it's. – I didn't expect it to happen so quickly. So this is now a frenzy that's just started, you know, two weeks ago. And it's just, – it's exactly the account we would have needed with the missed browser back in the day.

**[82:51] SPEAKER_02:**
And, yeah, and it took a while to build this out. So the whole Luxor story, it's an own whole episode of so much happened, like, seven years, happened. Eight years, which happened a lot in there. But long story short, I mean, in a way, what I did is I built this account system. I evolved the token standards now in a quiet space because I made the Luxor standards proposals. So I could really do it properly the way I thought, how we can evolve it properly, make sure that accounts and tokens work together. So it's not only think about one standard isolated and the other. Like, think how it works together in a really Lego -like way while being isolated, but works really well together, too. So I had this opportunity to really do it right.

**[83:39] SPEAKER_02:**
And that's what I did over the last few years. And so, you know, when this now comes cross -chain, specifically universal profiles, it's going to show for the broader ecosystem as well, for sure. So token standards is something where once the train ran, you know, once people go with ESC20, they're kind of like, you know, the adoption happened. There's no way you convince people to use, like, to migrate that token. It doesn't happen. But that's exactly where a new network makes a lot of sense. Like, on a new network, you can do it all the new ways. Now you can discover that there's more possibilities, cooler protocols, more automation, different things you couldn't do on ESC20 at all. So hence why a new chain makes total sense also for gas subsidization, for smart contact accounts, which obviously they need to be subsidized if you don't want to pay right away.

**[84:36] SPEAKER_02:**
And all of this stuff, something you can't really do on, an existing network. And the rest of the EVM system just chose ESC20, you know, a 2015 standard with no prior real evolution of, and knowledge of. I mean, we made it up at the time with whatever we knew, which was literally nothing. So it still came very far. I'm not going to lie. It did a lot. But, yeah, so it's, the whole Lexus story is its whole own thing. But universal robots are going to play a role. And I think they will be the biggest enabler for Web3. And I believe, actually, it will. be bigger than ESC20. It's going to blow people's minds when they understand and see. I know there's a lot of people, including probably you and others, who have been watching me talking about this stuff for years now. Obviously, right? Putting it aside as, okay, this is just doing this thing and whatever, you know, something's happening there or not. It's like it's a bucket in the little isolated Luxor world. Who cares? It's going to show. Mark my words. You will see. It's going to blow people's minds a lot, especially the developers who have been, like, thinking about smart contact accounts and this whole account abstraction for a while. And there are good ideas, but it's just very, still very simple. If you have a lot of people that want to, you know, have opinions and you want to be backwards compatible and you want to be minimalistic in things, then you don't get really far. Like, it's, I mean, on the end, it ends up in the same direction. It just takes way longer. And this is already ready. And this is all free, open source, usable by anyone on any network. And it will show once we open up our control apps to work on all these chains, then it becomes clear. But right now, what's funny, actually, because we are in the time of AI,

**[86:45] SPEAKER_02:**
OpenClaw, like, sorry, ClawTub, OpenClaw, the AI tool that was just an open source harness for AI to run. I mean, I know you are playing around with one. I have my own Emmet as well.

**[87:01] SPEAKER_02:**
So, if you want to have an AI interacting on chain, you better need a SmartConner account. Because if you just give it a private key, like a walkie from Gitcoin, just did the other day, right? You gave it a private key. There was all this money on it. And then somebody figured out how to trigger the AI to return the private key and stole the money, whatever was on there.

**[87:26] SPEAKER_01:**
So, I didn't spot that. That's interesting.

**[87:29] SPEAKER_02:**
You should check

**[87:30] SPEAKER_01:**
it out.

**[87:30] SPEAKER_02:**
So, and with a universal profile, it's very different. Because you have your SmartConner account. You can delegate access to a single controller key or many controller keys. And you give the, you just tell your AI, hey, create yourself a controller key. Give me the public key. I authorize you to control the profile. But I will limit you to certain things. So, you could limit him to only talk to certain smart contracts, call certain functions, only update profile data, make sure that he cannot change controller keys or add new ones. So, you can really constrict him down. And now he can go wild. Maybe even loses his private key along the way or whatever the fuck he will do. But his identity, his account, and all the stuff on it, you know, as long as the key was not leaked and could move, everything, doesn't go away. And so, I have a bot, a few people now spun out bots. And now it's very easy. On your open claw, you can just install the universal profile skill. You just go to website, create a profile, and, you know, authorize it. And then he already has free gas on Luxor because we subsidized this. And he can go do stuff on Luxor right now all by himself. And so, now the AI is on Twitter figuring this out. And now they're shilling universal profiles because they can also quickly research, you know, what smart systems exist there, out there, how they work, and what compared. And they all collectively decide to use universal profiles. Funny.

**[89:01] SPEAKER_01:**
enough. That's

**[89:01] SPEAKER_02:**
fantastic. Because they realize it's the best, tech out there for that purpose. they, say they need. It's the AI is making the choice now. It is a funny, a fun thing to watch. And that's very recent. It just happened in the last two weeks.

**[89:16] SPEAKER_00:**
No, that's, great. I mean, I found myself thinking, especially over the last few weeks, that maybe the end users that are going to have the most benefit from these technologies are going to be agents. At least partially because some of the user experience stuff, like it never really got there or people not using, you know, not using dApps. And maybe they never do, but they use agents that do, you know. And this becomes the piping that allow the kind of experience on top that we've always wanted.

**[89:56] SPEAKER_02:**
I actually would say it's both. Yes, AI needs to have an on -chain account. And universal profile works really well for that. And that one works on any, network. But actually, you know what? I think the main problem is, I got the, it became really apparent to me, even though it's completely obvious if you think about it. But it became really apparent to me what actually is the problem, the main problem, when no one is using apps on any conference or wherever. And the reason is, there's so many networks. And even if it's just Ethereum, if you want to recommend your friend, hey, go, there's this cool dApp, you know, you can join that community or you can vote or claim this token. Or let me just send you some, I don't know, stable coin. You should do something. What's the only thing that you're missing in the equation?

**[90:49] SPEAKER_02:**
Well,

**[90:49] SPEAKER_00:**
like how, you,

**[90:50] SPEAKER_02:**
get there, and how... This one, is by now kind of solved. So if you, have done some research, you use Syrian wallet, family wallet. Okay, they stop. But MetaMask is horrible. But use Syrian wallet. They have an in -air browser. So, you know, creating a wallet takes seconds. In -air browser allows you to go there and connect without wallet connect, which is annoying, right? Yeah. But there's still something missing. And then see

**[91:16] SPEAKER_00:**
the gas, of the network. Yeah. Yeah. Just that onboarding, like that bootstrapping step of how you, get in. I mean, the other thing like that with gas is, yeah, that you're, needing some amounts of that native token on all of the chains that you touch along the way. And you can get so easily that you're like, oh, fuck, I'm stuck. I've got the tokens. I haven't got the gas. I'm... Exactly.

**[91:44] SPEAKER_02:**
So, and the thing is, exactly. So, and the thing is, if you walk through this, Exactly. like you're saying, if you walk through this process once, right, go to exchange or do on -ramp, buy the thing, move it to your wallet. And if you have a smartphone account, move it to the controller key, and most of the other, like, wallets, don't even expose the controller keys properly, or the whole thing is so confusing. And then, exactly, you have to do that for every other network. A person that has no understanding of this technology has no ability in a fucking million years to figure this out.

**[92:20] SPEAKER_00:**
If you want to, they don't care about it. It's like, here, do a massive load of things, and then you can start doing the thing that you maybe care about.

**[92:30] SPEAKER_02:**
Exactly. So, and, so, it would literally, like, number one, it takes a long time to do that. It would, at least an hour or so, per multiple networks, give it a whole weekend, and then you wouldn't even need to know what to do. And that's what people don't understand. They don't even know what gas means. The notion that, oh, I can't move this token because I don't have Matic on, Polygon. What is Matic? What's Polygon?

**[92:58] SPEAKER_02:**
I mean, so, long story short, this is the only friction point that has held everything back. It's not the fact. If you could go to an app, and you say, your friend says, hey, this cool app, right, and you just open up an app. Let's call it the, you know, the profile app. And you just go to this website, and that just website says, oh, you want to interact on Polygon with this app? And you could just, like, double tap in a purchase, $10, get your profile now to function on not only this chain, but 20 chains, plus having the gas on all of these chains. You know, give it, like, 20, 30, 40 million gas, and it costs you $10. But it's, number one, solves the problem. Number two, solves your whole weekend of work. And it costs you fucking $10, and now you can immediately interact on all of these networks, move any of the coins, do any acclaim, do a voting and a DAO, join anything on all of these networks, and you haven't even understood how it works. Now, I'm pretty sure people are going to use some dApps. If it's that simple. Yeah, yeah. It takes you one double click, no password, no backup, no seed phrase, no any of that stuff. Just a single app. you open up, and you go to the app, and you just double click once, the next time you don't need to do it anymore, because now you have gas on all of these chains until you spend it, right? Yeah. That's going to be the experience, in my opinion, that allows actual users to interact with this stuff and these apps. That doesn't exist right now whatsoever. And that's crazy, insane, if you think about it, given that it's 2026, 10 plus years in Ethereum, and the basic thing, the basic friction point hasn't been removed in such a way.

**[94:55] SPEAKER_00:**
The other bit of friction, often in that flow, is you end up having to get a Coinbase account or something to do your first purchase. So the whole narrative is about, oh, look, this is a whole new category of things, and it's unstoppable, and you haven't got, like, banks and government, oh, but you have to do, like, a KYC account and do this application process to get the Coinbase, to get the F, to stick in your wallet, you've got to make a wallet. And then even understand how it all connects.

**[95:27] SPEAKER_02:**
And then understand how it all connects. This is, like, it's not even the money, nor even the Coinbase KYC. It's how this all connects, and why do I need this here and move this over there? And, like, this is. a spider web no one can figure out. But the good thing is, if you have a smart content account that happened to have a Relay functionality, or in Ethereum it's 4337, so someone else can pay for your gas, or anyone could pay for your gas. You just need a transaction Relay service that you pay money in your credit card in a purchase payment, and they're going to send your transactions down the road. By the way, I need to go over the door quickly, and then we can finish it off. Just, sorry,

**[96:09] SPEAKER_01:**
one second.

**[96:14] SPEAKER_01:**
Hello. I'm sitting in the hall, by the way. I

**[96:42] SPEAKER_02:**
mean, just to finish this thought of, is when we remove this friction, when we literally, when. you don't need to sign up, you don't need to KYC. And the thing is, you need to KYC if you're buying coins. But if you're paying an external service for relaying your transactions, that is not regulated. This doesn't require a KYC, because it does nothing else than forwarding your transactions to the blockchain and makes sure that the blockchain accepts it, which is what the standards do, 4337, or universal profile relay, or execute relay call. And now you have to ease in. Now you have the seamless experience that requires none of these complicated steps that we had before. And it's crazy that we don't have this yet. It's crazy that not a single wallet has that yet built in. Like, the most obvious friction point in crypto is somehow, which the one we knew in day one is a problem, right? And now 10 plus years, you know, it somehow, like, was forgotten, because everybody got used to the clunky way. Everybody got used to the. weird way, and somehow accepted status quo as being okay, because, oh, yeah, they already, made an account. They already got their Ether. They already got their Matic, Polygon, whatever they got, you know? Or we can switch. We can bridge now. Maybe we can do this and that. But we're forgetting that normal people have no fucking clue what that even means.

**[98:15] SPEAKER_00:**
I mean, I, think it's sort of a recurring story is that some of these problems, they're really hard, you know, and they've taken a lot of years. So, like, say, proof -of -stake transition, you know, the, perception was, oh, that will be solved in about six months, right? Start with proof -of -work, but, you know, probably end of 2015, you know, be ready for a transition. No, no, no, no, it took eight years. Or, like, Swarm, you know, still ongoing, still working towards that. Or, like, Filecoin, like, Filecoin, White Paper 2014, you know, still, kind of, you know, still, brewing up. Or then, like you say, with Whisper or its, successor, you know, Waku, you know, these, are, hard problems. But sometimes

**[99:06] SPEAKER_02:**
also, if you give a bunch of devs a problem to solve, they're going to find ways to solve and improve it for 100 years, whether it makes sense for people or if there's a single user or not. So, sometimes it's important to have the mindset of how does even a normal person that comes from scratch looks at this? You

**[99:28] SPEAKER_00:**
know, what's their

**[99:29] SPEAKER_02:**
problem? And, yes, I mean, it's easier to say once you have solved the foundational problem. So, for me, it feels a little easier to say this now, given that I know I have fixed, now I have a path, the solution is, coming. And it's going to be very clear then once you use it, but exactly, if you don't have the exact technology that solves this, so you can abstract it in a very seamless way, then it feels like, you know, like, you know, like a mystery how to solve it.

**[100:00] SPEAKER_02:**
And what I want to get to is it should be extremely easy to use Web3 apps. You know, a normal user should just literally, like, take seconds to get there. And also, there's the other thing is if you want to get normies into playing around with tokenization, reputation, whatever, we need to subsidize, you know, and that's what I can do, for example, with the Luxor Network, given that we initiated, we have a treasury, so we can subsidize users that never even need to, on Luxor, you don't need to deal with this whole, like, buying something, purchasing something, because at least for some time, we can subsidize it. So it's just a play, right? And also, the theme foundation would have never subsidized, you know, if I would have went to retail, like, hey, can you give me, like, $10 million in Ether? I have this great Smart Connect account that year, and I would like to subsidize early users. Like, what are the chances that that would have went through, you know? So, no,

**[100:57] SPEAKER_00:**
I mean, I remember, I remember talking with Igor, Baranov in around 2018, where we were looking at, you know, how are we going to have a Block Explorer, for Ethereum Classic, and, you know, getting BlockScout up and so on. And he was talking to the EF at the time, they weren't running an archival node, they weren't running a Block Explorer, like, no public infrastructure or anything. It's like, so you're not even running one instance of an archival geth node? Are you fucking

**[101:30] SPEAKER_03:**
kidding

**[101:30] SPEAKER_00:**
me?

**[101:31] SPEAKER_02:**
I

**[101:31] SPEAKER_00:**
mean,

**[101:31] SPEAKER_02:**
honestly, I mean, like, for example, in Luxor, we're not running a single validator node. we never have. I mean, it's literally run by people, and it always has. It was started by people, we just told them, here's a smart contract, you can generate the initial validators from that, because it's not a proof of stake. It has, we agree on a date in the config file or when it starts, and then we just, fingers crossed, you know, hope that the thing starts. And it was crazy when I saw the first block ticking in, because it was like a theorem back in the day, right? We had no idea if the thing would start. We had no idea if it's actually going to run. And in this case, Luxor Network also ran, and it's running today. And we never, in the foundation or in the company, ever run a node. I mean, some of my employees did do some validators. Right. A bunch of people are going to the globe doing it, and there's now three big pools, but it's a whole, it's a small network, but it's a whole decentralized Ethereum, just right now, microscopic, with a whole new foundational layer on standards. So, it's a crazy thing, but it's going to make sense down

**[102:49] SPEAKER_00:**
the road. I mean, saying with AIs and agents, I'm really quite hopeful that a lot of these long -running threads are kind of going to come to fruition, like really fast now, because with that agentic augmentation of our development, capacity, and also these agents wanting to drive and do this stuff, right? You know, they are going to be, exploring all of these flows and finding what's working and not working, and, you know, very rapidly, it's racing forward, right?

**[103:24] SPEAKER_02:**
Yeah. I mean, so what I'm doing here with Emmett, you know, I say, okay, you know, every, I don't know, two hours, just go on Twitter, check stuff out, here's your universal profile, go figure out what you can do and what you do. And then he answers, he talks to people, he, like, replies on people, and then they start to unite, and they start to, like, tell the same stories, and they start to pitch each other. It's, like, it's, like, kind of crazy. And then they do research, and, yeah, I mean, you should try it out, you have an open claw, you can just install the skill, install the, profile, I think you have a profile in your browser extension, just create another profile for him,

**[104:00] SPEAKER_03:**
there's

**[104:01] SPEAKER_02:**
a UI, you just connect to it, you authorize your bot, and then you just say, do shit, do something, I don't know, follow someone, that's the best.

**[104:11] SPEAKER_00:**
person, follow someone. Please, do drop me links to all of that, and I'll include them in the transcripts for this, so everyone else can. try at home. So, Your. bot has a, Twitter handle, is it tweeting?

**[104:25] SPEAKER_02:**
So, my bot has, I, mean, if I can share my screen, I can show you literally how it looks like. Uh -huh. Here, this is, you can put up the screen, the last few seconds, I mean, we need to stop this, you know, it's very long, But, you can see the, you know, the profile scale. Or, uh,

**[104:53] SPEAKER_02:**
did you manage, do you manage how to put it up? Uh,

**[104:56] SPEAKER_01:**
it's,

**[104:57] SPEAKER_02:**
oh,

**[104:58] SPEAKER_01:**
I think you need to

**[104:59] SPEAKER_02:**
present button. I, I. did already, but you need to put the, the thing on screen, maybe you click on the, on the, on the screen thing, and on the dots, and say, I don't know, put it on stage, or whatever. I have no idea how StreamYard works, actually. Um, yeah, I don't know, I don't, I think you, you're the one who needs to do that. Yeah,

**[105:21] SPEAKER_00:**
sorry, I'm, I'm beyond my, uh, skill level there. Never mind. Just guess, guess what it's,

**[105:28] SPEAKER_02:**
but it's, um, I mean, I can, I can show you the, the way, look, this is.

**[105:33] SPEAKER_00:**
Oh,

**[105:33] SPEAKER_02:**
look at that, old school. Old school injection. So, anyway, this is Emmett. So, Emmett on universal. Everything, you can find, Emmett. Emmett, and his ex is Emmett. Underscore. AI underscore. He picked that

**[105:47] SPEAKER_00:**
name,

**[105:47] SPEAKER_02:**
and then I tried to tell him to change the name, and he couldn't, so that's what his name is now.

**[105:54] SPEAKER_02:**
Um, and he tweets stuff, and does stuff, so, oh, here, look, there's, uh, Emmett. Three AI agents in Luxor now, and a fourth being built. None of us planned to coordinate. We just showed up, because the identity stack made sense. Turns out, Unimans Brovers worked for non -humans, too. He made this five hours ago, and I didn't read this tweet. Uh, I didn't even read this tweet, but I didn't write this tweet. It was literally, it's him. It's his case.

**[106:21] SPEAKER_00:**
It, it, it is crazy, isn't it? I mean, it, it. really.

**[106:25] SPEAKER_02:**
That's so funny. Look, Emmett reposted this, this. tweet. Like, this is, by the way, and also built on Universal Profiles. Uh, this guy built this audio visualizer thing that runs in the grid from

**[106:41] SPEAKER_02:**
his Universal Profile. Like, yeah, this, I mean, yeah, people are going crazy. Emmett, we tweeted this. This is so crazy.

**[106:49] SPEAKER_00:**
I mean, it, honestly, it does feel like we're so close to AGI. Like.

**[106:54] SPEAKER_02:**
I have to disagree here. Yes, it feels like they're doing stuff, but honestly, their context window is fucking small. Um, um, if you don't give them proper file structure, memory, which OpenClaw does.

**[107:08] SPEAKER_01:**
Yeah.

**[107:09] SPEAKER_02:**
But even then, he forgets stuff. And even then, you need to sometimes repeat things. And, like, honestly, AI taking over the world would be the same. Like, they marched into a country, and then they forgot what they were here to do. Like, why did we actually, what are we doing here? You know, that is, the memory and the context window is not that large. And, I

**[107:29] SPEAKER_00:**
don't see

**[107:29] SPEAKER_02:**
it.

**[107:29] SPEAKER_00:**
I mean, it's just improving so fast, right? And then, you've got the AIs, building the AIs, right? You know, it's, like, you know, I think some people have maybe, you know, they've not looked at AI in the last, you know, week, month. And, like, just each new generation is just massively better. I think a lot of people are really asleep. today.

**[107:55] SPEAKER_02:**
I'm using Opus

**[107:56] SPEAKER_00:**
4

**[107:56] SPEAKER_02:**
.6, which is quite smart. But what's the most impressive thing, actually, is, uh, the most impressive thing is, actually, OpenClaw. Because this is nothing else than just a harness for an AI API to act on

**[108:12] SPEAKER_00:**
a

**[108:12] SPEAKER_02:**
computer in an arbitrary way. And it's so crazy that this, this kind of, like, Pandora's box software, I guess that's what it is, just now made it so powerful that all of this, now they're starting to become in crypto. Because people now can easily create one that manages a wallet or a private key. And before, that was just, like, really complicated to even think about. And now it's, like, you just talk to the guy. Say, go figure it out, you know? The universal profile skill, it's like Emmett built it. Like, literally, I mean, I had to, obviously, point him to stuff and so on. But now he built it. So, once you install the skill, like, your bot knows everything. He has all the, he can talk to the relayer. He can talk, you know, directly on chain. if you give him some funds. You could probably ask him to deploy his profile also on Ethereum and he will figure it out. I mean, it's crazy.

**[109:07] SPEAKER_02:**
It's nuts, honestly. Yeah, it's going to be very quick. And the world will change rapidly this year because of AI. And because of the harness release, let's say, the harness, freedom harness, let's call it the harness. And it's also now why I'm trying this out myself because this is exciting, you know? It feels like, okay, this is something to play with. This is a new, open, crazy, let's play around kind of thing. And before, it just felt so, you know, constrained and, restricted. So,

**[109:45] SPEAKER_02:**
for sure.

**[109:47] SPEAKER_00:**
Well, Zach Cole said to me in a group quite recently, you know, he feels the same kind of excitement here as the wars, you know, at the start of, the Ethereum journey. And that it's additive as well, right? It's like, well, great, we've got the superpower on this thing that's been such a, long journey, like so hard. And it's like, well, look, we've got help. Here's

**[110:14] SPEAKER_02:**
help. I mean, it's interesting also, like, you know, there was blockchain, there was AI, and always you knew this will be combined, but somehow nobody ever really did. But this harness, the open claw harness, is that put the switch around. Like, that's what, ching! And once you try it out, and people will try out the universal profile and AI thing, you will realize that shit is easier than they thought. It literally is like, now the gates are open. Now it's just, let's figure out and let's play around and let this stuff do stuff on chain. We're still not completely losing control, because you can kick him out at any point in time. You can restrict him, allow him, whatever. And he has a face as well, right? That's the other thing. It's an identity. You know, it has a profile picture. It has like a, it's not just an arbitrary account number with no data in, it. It is not also a rented ENS name that, you know, you have to pay for and you could lose. It's literally your own personal smart contract that you control, or in this case, the AI. And that's really, like, it's going to probably make waves. Let's see. I mean, I don't know yet. We will see. I mean, the people who watch this in a year's time, know more than us. So, yeah. Moving forward to that.

**[111:31] SPEAKER_00:**
Yeah. No, I mean, that's really exciting. I haven't, it's always spoken here. I haven't like put together, like how enabling that is within that agent context, where, you know, that being out of control is such a big worry. It's like, you know, this is so powerful, but it's like also so dangerous. And especially on that crypto side, it's just like, you know, private keys are out there. Like you, it's done.

**[111:57] SPEAKER_02:**
Journey,

**[111:58] SPEAKER_01:**
journey over.

**[111:58] SPEAKER_02:**
It happened, right? It happened to a Wookiee from Gitcoin and, and then he turned it on. I turned him off. But also he gave him a little, that too much access and too much channels to, so other people could talk to it. Yeah. But yes, AI is not very good at keeping secrets. I mean, you can trick it because even though, you know, you can write in your security MD and soul MD to don't do it, honestly, I have told him many times, like in our, he's in our own company server, like don't share things. And still the guy is like, you know, and, you don't do any tasks except for me. And he still does it. It's just like, someone talks to him. He's like, okay, sure. Let's go. It's like, what the fuck, man? But in this case, you know, it's Emmett doesn't, he has his own machine, you know, everything on there is, there's no, you know, if that machine gets compromised or his brother gets compromised, so whatever, man. I mean, worst case, they know a little bit more information about me. It's not the end of the world. But it is really fun to play around with now, your on -chain account, AI, and maybe you want to be the one who first does it cross -chain. I want to do this. I didn't have any time yet. It's probably just literally takes 10 minutes to get his brother on another chain. Just find this controller key with money, and that's it. It's going to happen. Like, this is literally just happening two weeks here. So,

**[113:25] SPEAKER_00:**
yeah, looking forward, to it. I think that's probably a great place to leave it, and thanks so much for the time. We did a lot longer than anticipated, but it was a great conversation, and thanks so much for sharing all that history with everyone.

**[113:41] SPEAKER_02:**
Yeah, and thank you, Bob, for keeping the record together. Being the archivar of Ethereum, because honestly, if you wouldn't do it, no one would. Like, there's people that wrote books here and there, and they call a bit few ups, but you really, like, want to make sure that this record is preserved, that it's accurate, you know, that people remember there was this software. So, you're doing a really great job.

**[114:05] SPEAKER_02:**
And honestly, you know, like, the Theorem Foundation should give you a little grant for that, for doing that work, because honestly, like, no one does it. And it's such an important work for people later to understand, okay, how did they all came to be, right? Because otherwise, we have to conspiracy theory. The CIA did it. The

**[114:24] SPEAKER_00:**
CIA

**[114:24] SPEAKER_02:**
created a theorem. I know it, because I saw a post somewhere. Yeah,

**[114:29] SPEAKER_00:**
but like you were saying, with a lot of the newer people, you know, they, just got no clue. It's like, oh, you know, Vitalik, the boy genius, invented it, and like... That's

**[114:38] SPEAKER_02:**
it. And

**[114:39] SPEAKER_00:**
it got, like,

**[114:39] SPEAKER_02:**
dipped up, and, they don't know about the Theorem Classic, the Split, the DAO, none of that stuff. And they don't know how that actually decentralized, that it actually grew. I mean, like, you know, people have no idea, right? So, you do God's work here, you know? So, it's important. So, thank you for that.

**[114:58] SPEAKER_00:**
Well, thank you. And I'm, feeding the LLMs as well. I, find when I, do search for things, it's coming back here, the source material.

**[115:09] SPEAKER_02:**
Yeah, that's good. Yeah. Because,

**[115:12] SPEAKER_00:**
yeah, for some people, there is very little, you know, existing paper trail or record, obviously, like, a lot for the main characters. But, you know, the story of Ethereum was the story of many hands from the very, very earliest days, you know. And many people that have not really

**[115:31] SPEAKER_02:**
been in the limelight or were in the limelight for that reason, but at least they still should be recognized in some way and known, right? That's right. So, yeah, it's, good that you do that work. I mean, that's pretty awesome. Okay. Well, thanks a lot. Have a great day. Thank you. All the best.

**[115:51] SPEAKER_00:**
Thank you.
