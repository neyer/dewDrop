# dewDrop
## A Formal Language for Social Networks


# What

  dewDrop is a simple formal language for use on social networks. 

  Anyone can make statements in dewDrop, and anyone can aggregate those statements to reach conclusions using all the knowledge of their social graph. Only the people you trust - directly or transitively - will have their statements weighted when you build conclusions.

Think wikipedia, with a different article for each user, depending upon who that user trusts. Anyone can add statements, but which of those statements you use to form conclusions is up to you.  People who trust you will use your statements; people who don't may not.

# Why

  There are many difficulties involved when discussing things in a group. Even when everyone involved means well and cares about the same goal, arguments quickly arise.
   
  Often, not everyone means well. Online harrassment is a serious problem. Sensitive discussions about important topics are easily derailed by trolls. In addition to runining the experience of a person discussing anything online, trolls can claim to be a member of any group or support any ideology, giving a non-affiliated group a bad name through false flag techniques. 

  Mob mentalities seize hold of "the villian of the moment", and no person has any incentive to stick up for someone who is the 'bad guy du jour' of the crowd, regardless of whether or not all claims are merited.

## Separate Opinions, one Truth
  
  It's impossible to resolve an argument without finding common ground. dewDrop provides a meaningful social common ground, because the 'Truth' in dewDrop is nothing more than 'a record of things which have been said.' 

  Two people debating about important matters can disagree about all kinds of things - but they can't possibly disagree about _the fact that they are talking._ 

## Encourage Cooperation through Record Keeping

  If I have a history of trying to be conciliatory, trying to understand other people's perspectives, trying to find common ground and relate to them - you are probably more interested in talking to me than if I don't have such a history.

  Right now, it is possible to signal these things to others - that you are conciliatory, polite, and that you admit when you have erred. But there is no way you can verify these signals. 

"You just don't want to admit that you are wrong" carries a lot of weight when it comes from someone with a long track record of apologizing for wrongs, directed at someone who has no such record. It carries no weight as a charge when leveled the other way - a person who has a history of apologizing for wrongs big and small is much more trustworthy when they stick to their guns.

## No Single Perspective is Authoritative

If you read that last sentence, you may think I'm wrong - you may not trust people who always apologiez, because you think it means they are weak. Fine - that's entirely up to you - with a public record of who has said what, when, you can go through records and ignore people who behave in _any_ way you don't like. 

Nothing is forced on anyone.

## A Flawed Version of this System Already Exists

  People _already_ judge each other based upon the words of their friends and colleagues. They do this using heuristics, and the judgements are rarely nuanced. The system at work today provides no incenetive for public apology. There is no track record of statements to see who agrees with and disagrees with who. There is no way to see whose statemens contradict themselves, and how frequently. 

  By speaking in a formal language, it's possible to combine million of statements made by different people and come to solid conclusions about beliefs which are contradictory, and how much weight we should put on a stranger's words -

  So if you don't like the idea that people can speak on your behalf, or they can make false claims about you to mislead others - these things _already happen_ and the mechanisms in dewDrop make it possible for a person to actual defend themselves against them.

  Without dewDrop, If a subject of public opinion is attacked by a thousand nameless faces with baseless charges, the best that subject of public opinion can do is say nothing. The friends and people who know this person will still trust them - although a few will wonder - and the general public will either be temporarily roused by the mob, or ignore it.

 With dewDrop, those making the baseless charges can just be denied, with the subject issuing a DISTRUST statement. Anyone who trusts the subject can now immediately know to distrust those issuing the baseless claims - as well as anyone who trusted them.

  dewDrop allows the company you keep to reflect on you, and you on them.  Without dewDrop, this already happens, but to a very limited degree, and without solid data. That is perhaps the best argument for using a system like this - all of the problems it entails already exist and happen in the world today, and few of its benefits it are present.


# Benefits

  The following is a short list of things we can accomplish:

 * Block users who are marked as trolls by enough people i trust
 * Incentivize people to admit they have erred - a public record of you apologizing shows you try to right your wrongs
 * Find out how many self-identified republicans support gay marriage 
 * Find out how many self-identified muslims support ISIS
 * Find beliefs you have yourself that contradict each other
 * Evaluate how integrated a person's trust network is. Someone who has thousands of peopl who trust him, and none of them trust each other, is a very differnet kind of person who is trustled by a much smaller number of people who all trust each other.

  Nobody is perfect. This is a known fact. With a public record of the times we have offended people, a person can show that work to obtain forgiveness, and succeed in doing so.  At present, without a formal language or agreed upon record, people have little incentive to apologize when they've offended someone, and no way of knowing if they are dealing with a troll who wants to annoy them, or a caring person who has either misspoken or been misunderstood.

  People who have a record of apologizing when they offend others, and seeking forgiveness for doing so - those are people much more worth talking to. dewDrop can help us find each other.

# More Details
  The language can be determined by simple regular expresisons. The primitives are keyworks, hashtags, and urls. A simple parser is implemented in `parser.py`. This is the complete specification for version 1 of the dewDrop language.

## General syntax
  All dewdrop messages can begin with any text; the dewDrop portion starts with #ddv2 to identify it as a dewDrop message. The next token should be a one of the verb keywords of the language. The remaining tokens following the verb should be nouns upon which the verb operates.

    .* #ddv2 <VERB> <NOUN> [<NOUN> [<NOUN>]]

 Most Nouns will be URLS - A user can be referred to with the URL of their social media account. If a dewDrop statement is made on twitter, the '@userName' syntax will be assumed to refer to that person on twitter.  You can also speak about a user account at another site - like a reddit user, a facebook user, an email address, a telephone number... any protocol you wish. 

  The first noun contains the predicate of the statement. The secound noun is assumed to be the speaker if empty, and refers to the subject. The third noun refers to the speaker if not present, and refers to a person who the speaker issues the statement on behalf of. 

  The verbs are: "ISA, NOTA, AGREE, DISAGREE, TRUST, DISTRUST, SAME, HURT, SORRY, FORGIVE, THANKS". 
  They are explained below:

## Group Membership
    .* #ddv2 ISA (HASHTAG) [URL [URL]]
    .* #ddv2 NOTA (HASHTAG) [URL [URL]]


Groups in dewdrop are represented by hashtags. A person can claim to be a member of a group with the 'ISA' verb, and claim not to be a member with the 'NOTA' verb. For example, the sentence

    #ddv2 ISA #democrat

Means "The speaker of this sentence claims to be a member of the #democrat group."  Any group you want to identify with can be used as a hashtag.  This way, discussions around social movements, say "#yesAllWomen", can involve people stating their identification with principles of the group. If I choose to leave a group  - either becuase their values have changed, or I have - I can ussue a 'NOTA' statement:

    #ddv2 NOTA #vegetarian

A person can also make statements about other people.  I can claim that Ralph Nader is a #greeparty member:

    #ddv2 ISA #greeparty @RalphNader

If my friend hears a speech, where Barack Obama claims that Ralph Nader is a doodoo head, he can say this:

  #ddv2 ISA #doodoohead @RalphNader @BarackObama


## Statement Agreement
    .* #ddv2 AGREE (URL) (AGREER) (SPEAKER)
    .* #ddv2 DISAGREE (URL) (AGREER) (SPEAKER)

  Agreement in dewDrop can be signalled with the AGREE verb.  Disagreement can be signaled with the DISAGREE verb.  A Person can agree with any URL they wish. I might agree with another statement someone has made by agreeing with the url of that statement:

    #ddv2 AGREE https://twitter.com/MarkPNeyer/status/525766862949199873  
 
 I can also agree with a supreme court decision by 'agreeing' with a news article about the supreme court decision, or the wikipedia page. 

  When a discussion evolvs to a certain point, must likely a hashtag will be created to represent the movement. At that point, people who agree with one 'side'  of the discussion will issue a 'group membership' statement. The point of 'agremeent' statements is primarily to allow people to agree or disagree with other people's statements.

 Suppose Alice, who supports marriage equality, issues a statement:

    @Alice: #ddv2 AMA #LGBTAlly

Now, suppose Bob says:

    @Bob: you said there's no such thing as bisexual #ddv2 NOTA #LGBTAlly @Alice

Bob's statement is equivalent to him saying:

    @Bob: #dd1 DISAGREE https://twitter.com/ALICE/status/1234

Assuming that the url above is the url of Alice's original tweet

  So now suppose more self-identified members of the  group #LGBTAlly weigh in on the discussion. Some may issue AGREE statements with @Alice, and some may issue @AGREE statements with Bob.  A discussion will happen, and either the #LGBTAlly group will  integrate itself, and come to a conclusion, or else it won't and people who can't agree will stop associating under the same banner.

  Suppose that discussion resolves itself, with @Alice agreeing that bisexuality is a natural  thing, too. She may issue statements like this:

    @Alice: you were right about accepting bisexuality #ddv2 SORRY @Bob

Bob may now issue these statements:

    @Bob: it's all good #ddv2 FORGIVE @Alice https://twitter.com/Bob/status/100
    @Bob: #ddv2 AGREE https://twitter.com/Alice/status/1234

The first statement links up Bob's FORGIVE statemenet to his HURT statement. This allows questions to be asked like - how many unforgiven offenses has this person issued, and how many have they recieved?


As a result of this exchange, the '#LGBTAlly' has increased its integrity; the self-identified members of the group are largely in agreement with each other about what constitutes group membership, AND they have successfully resolved a conflict between two members.  The world is better off! Hooray!

  
## Trust and Distrust
    .* #ddv2 TRUST (URL) [URL [URL]]
    .* #ddv2 DISTRUST (URL) [URL [URL]]

  At lower layer than disagreement is trust. I can disagree with someone, but still believe they are honestly expressing their belief. Users in dewdrop have the ability to state trust and distrust in statements or other users with the 'TRUST/DISTRUST' verbs.
  
  A statement of trust is not a statement of agreement. My mother my say she supports 'traditional marriage' - and although i disagree with her on this, I trust that this is an honest representation of her beliefs.  If someone else comes along and says "I believe all black people are criminals" - I will disagree with this statement. I will only _disrust_ the statement if I have reason to believe that this person is trolling, or does not really believe the thing they are saying.

In a healthy discussion about unpleasant topics, people will disagree. Otherwise there'd be no discussion. It's really not possible to have a healthy discussion with someone you distrust. I suspect dewDrop users will make less frequent use of the 'DISTRUST' verb; it will be used primarily to block trolls. 

If i say I distrust someone, all of my friends can see that, and may know to stay away from that person and to ignore their messages.

The opposite statement - TRUST - implies that the person i am speaking about is an honest, genuine person. I don't agree with everyone my mom says, but I trust her. I want people who trust me to extend that trust to her - I don't expect them to agree with her, but I would be very surprised if anyone thought she were a troll.

People who are concerned about trolling or being victimized online can follow the TRUST statements issued by their friends to whatever extent they feel comfortable with. Someone who feels comfortable online may say "I'll accept messages from any users whom I can reach through a TRUST-path of length 4 or less."  Someone who feels less comfortable or is more worried about harassment can block or ignore users with a TRUSt-path length of more than 2 - implying they are willing to speak to trusted friends of trusted friends, but not anyone else.

  The 'TRUST' statements allow us to protect each other from trolls.  Anyone is free to disregard these statements, of course - but if I know I can talk to a lot of interesting people following only trusted links from friends, and I know that accepting messages from random strangers puts me at risk of serious harassment - I should have the freedom to choose whom I wish to associate with. 

  I can speak about others' trust or distrust using the three-part syntax. The first URL is the person who is [dis]trustd. The second is the one who does the trust/distrust. The third is a description url; my reasoning for linking the two.

## Same Identity

    .* #ddv2 SAME (URL) (URL) [URL]

  This statement may seem small at first, but it actually gives dewDrop a lot of power. It's used to link identities together - so that I can say "this facebook account is the same as this twitter acount", this email address belongs to this account, etc. If @Eve creates a fake account @Fred so she can troll people, and I'm  certain it's @Eve pulling the strings, I can make this statement public: 

    @Bob: #ddv2 SAME @Eve @Fred

People who trust me and are mad at @fred for trolling will not be made at @eve.  The standard mechanism for resoving these disputes applies; people who know @eve may disagree, @fred will probably disagree as well. If there are trusted friends involved that know both of us, they may want to step in to resolve this dispute. If there are no trusted friends, maybe we're all just better off not talking to one another. 


  The 'SAME' statement also allows for a unified sense of personhood to emerge from  multiple social media accounts. I can make a statement about my friend on facebook, and his twitter followers will be able to make sense of the same statement.

  As in other statements, the last parameter can let me assert that another person is saying two statements are the same.


## Hurt, Apology, Forgiveness

    .* #ddv2 HURT(URL)[ (URL)[ (URL)]]
    .* #ddv2 FORGIVE (URL)[ (URL)[ (URL)]]
    .* #ddv2 SORRY (URL)[ (URL)[ URL]]

  People upset each other. This happens, and its part of the world. By keeping a record of those we have upset, and those who we've forgiven, we can all help each other get a better gauge of who and how we are. If I run into a stranger on twitter who really upsets me, and I see from his record that a few friends of friends been upset by this guy, but for every single one, he's apologized and they've forgiven him - it suggets that he may be worth talking to. If someone else has offended far fewer people, but has never apologized or been forgiven - it suggests that his offense to me isn't going to change, and I should probably ignore him.

  The syntax for 'hurt' is :
  #ddv2 HURT (person who did the offense) (person who felt offended) (person making the statement)

  
  The syntax for 'forgive' is:
  #ddv2 FORGIVE (person who is being forgiven) (person doing the forgiving) (person making the statement)

  #ddv2 SORRY (person who is being apologized to) (person who is issuing the apology) (person making the statement)

In all of these, if there is only one argument given, it the value of the second argument corresponds to the person issuing the statement.

  So, If @bob simply wants to say "@Alice has offended me" he can do this

    @Bob: #ddv2 HURT @Alice

  Which is equivalent to this

    @Bob: #ddv2 HURT @Alice @Bob

  Perhaps bob thinks Alice has offended his mother. Then he might say this:

    @Bob #ddv2 HURT @Alice @BobsMama

  If there wre a specific tweet Alice had written, say with address 'http://t.co/123', he might state:

    @Bob #ddv2 HURT @Alice @Bob http://t.co/123


  Maybe alice didn't realize that this was a problem. She might start by immediately apologizing to show good faith:

    @Alice i'm not sure what happened lets talk  #ddv2 SORRY @Bob

  And then she and Bob talk a while, until they found out that Alice made a joke about potato farming, and bob's mother was eaten by a potato. At the end of the conversation, bob says


    @Bob: most people don't know the danger of spuds #ddv2 FORGIVE @alice
    @Bob: i know i overreacted a bit #ddv2 THANKS @alice

 
  And now everyone feels better! Hooray!

  The FORGIVE syntax also allows a person to state their belief that person A has forgiven person B.  The last 'url' field in 'FORGIVE' is a description field. it can be used to explain why the speaker thinks person A forgives person B.


## Thanks

  dewDrop members can say thanks to each other. Isn't that cool? A user who's gotten lots of 'thanks' from friends of friends is probably trustworthy  - but again, that is up to you to decide. The point of dewDrop is merely to give people the ability to speak formally, in a way that there statements can be aggregated into a collective whole. You'll no longer be a drop in the ocean, but an edge in a proof.  Thanks!
  
    .* #ddv2 THANKS (URL)[ (URL)[  (URL)]

  The 'THANKS' syntax follows the same pattern as FORGIVE or HURT. A single url means that the speaker is saying they feel thankful to the identity at that url. Two Urls means the speaker is saying "preson A thanks person B". Three urls mean "person A thanks person B, here are details". 

# warning
  
  I have no idea how this will turn out, but i have some intuition. Suppose you shorted bitcoins in 2010, selling 10,000 bitcoins you didn't for $0.10 apiece. You'd earn yourself a profit of $1,000 - and if you didn't pay them back, you'd be $3,000,000 in debt today. I really think this kind of network could change the world. If you defect against people trying to make the world better, by trolling us - you are standing in the way of human progress. We are building a record book that essentially blocks trolls from the public discourse  - is trolling that group of people really a good idea?

