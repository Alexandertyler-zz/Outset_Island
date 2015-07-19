import sys

def action(ircsock, chan):
    ircsock.send("PRIVMSG " + chan + " :Goodbye cruel world\n")
    sys.exit(1)
