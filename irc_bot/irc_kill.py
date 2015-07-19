
#need to redo this for multiprocess

def kill(ircsock, chan):
    ircsock.send("PRIVMSG " + chan + " :Goodbye cruel world\n")
    sys.exit(1)
