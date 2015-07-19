##  This is a python module for fortune telling. It is designed
##  to be imported into an irc chat bot. Designed and coded by
##  Alex Tyler, this code is free to use and modify as long as
##  it is not for profit.
import random


fortune_list = ["The fortune you seek is in another irc channel",
                "A dubious friend may be an enemy in camouflage",
                "A friend asks only for your time not your money",
                "A golden egg of opportunity falls into your lap this month",
                "Try the mushu pork",
                "A starship ride has been promised to you by the galactic wizard",
                "You have a heart as big as Texas",
                "Fortune not found? Abort, Retry, Ignore",
                "Help! I am being held prisoner in an irc client",
                "Never forget a friend. Especially if he owes you",
                "Someone will invite you to a Karaoke party",
                "You will receive a fortune cookie",
                "Accept that some days you're the pigeon, and some days you're the statue",
                "Don't fry bacon in the nude",
                "Don't sweat the petty things and don't pet the sweaty things",
                "When everything's coming your way, you're in the wrong lane",
                "Always keep your words soft and sweet, just in case you have to eat them",
                "You can always find happiness at work on Friday",
                "Two days from now, tomorrow will be yesterday",
                "You are cleverly disguised as responsible adult"
                "Tomorrow at breakfast, listen carefully: do what rice krispies tell you to",
                "You will soon have an out of money experience",
                "Practice safe eating. Always use condiments",
                "Indecision is key to flexibility",
                "The best year round temperature is a warm heart and a cool head",
                "Two days from now tomorrow will be yesterday",
                "SSoorrrryy,, dduupplleexx sswwiittcchh oonn",
                "Keep your goals away from the trolls",
                "People don't care how much you know until they know how much you care",
                "Our brightest blazes of happiness are commonly kindled by unexpected sparks",
                "Perhaps you've been focusing on others too much",
                "People may doubt what you say but they will believe what you do",
                "Digital circuits are made from analog parts",
                "People have great respect for you",
                "You will become your parents",
                "If opportunity doesn't knock try installing a doorbell",
                "Our deeds determine us much as we determine our deeds",
                "The greatest risk is not taking one",
                "Adversity is the parent of virtue",
                "Now is the time to try something new",
                "The man on top of the mountain did not fall there",
                "Conquer your fears or they will conquer you",
                "Give a man a match and he'll be warm for a minute, set a man on fire and he'll be warm for the rest of his life",
                "War doesn't determine who is right, only who is left",
                "Everyone is entitled to be stupid but somme abuse that priviledge",
                "A train station is where a train stops, a bus station where a bus stops, and on your desk there is a work station",
                "You can't be late until you show up",
                "The secret to creativity is to know how to hide your sources",
                "Never interrupt your opponent when he is making a mistake",
                "Love is like pi - natural, irrational, and very important",
                "You may look like you are doing nothing but you are actively waiting for your problems to go away",
                "The master of language often says nothing",
                "You'll find no life lessons from an irc bot",
                "You are unique, jus tlike everybody else",
                "It might be time to find a new favorite color",
                "Don't listen to a fortune, make your own future"]

def fortune(ircsock, chan, nick):
    nick_fortune = random.choice(fortune_list)
    ircsock.send("PRIVMSG " + chan + " :" + nick + ", " + nick_fortune + "\n")
