import sys

def action(ircsock, chan, nick, msg):
    ircsock.send("PRIVMSG " + chan + " :Goodbye cruel world\n")
    sys.exit(1)
