import time

def action(ircsock, chan, nick, msg):
    try:
        ircsock.send("PRIVMSG " + chan + " :Perhaps just a moment's rest...\n")
        time_ts = msg.split('.sleep ')[1]
        time.sleep(int(time_ts))
        ircsock.send("PRIVMSG " + chan + " :Is the coffee ready yet?\n")
    except:
        ircsock.send("PRIVMSG " + chan + " :I can't sleep, too much caffeine\n")
