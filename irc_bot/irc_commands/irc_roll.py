import random

def action(ircsock, chan, nick, msg):
    if 'd6' in msg:
        rand_num = random.randint(1, 6)
    elif 'd20' in msg:
        rand_num = random.randint(1, 20)
    elif 'coin' in msg:
        rand_num = random.randint(1, 2)
        if rand_num == 1:
            rand_num = 'heads'
        else:
            rand_num = 'tails'
    elif 'joint' in msg:
        rand_num = 'fatty, be sure to share'
    elif 'sushi' in msg:
        rand_num = 'california roll, extra wasabi please'
    else:
        rand_num = random.randint(1, 100)

    ircsock.send("PRIVMSG " + chan + " :" + nick + " has rolled a " + str(rand_num) + '\n')
