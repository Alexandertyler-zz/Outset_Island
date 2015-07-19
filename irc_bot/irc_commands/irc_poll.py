

def poll(ircsock, base_chan, nick, msg):
    poll_values = msg.split(".poll ")
    ircsock.send("PRIVMSG " + base_chan + " :" + nick + " has started a poll. Use .vote to submit your opinion. Poll will be open for one minute. Topic - '" + poll_values[1] + "'\n")

    start = time.time()
    poll_results = {}
    voters = []
    ircsock.settimeout(3)
    while 1:
        try:
            if (time.time()-start) >= 60:
                break

            ircmsg = ircsock.recv(2048)
            ircmsg = ircmsg.strip('\n\r')

            if ircmsg.find("PING :") != -1:
                response = ircmsg.split("PING ")[1]
                ping(response)

            if ircmsg.find(' PRIVMSG ') != 1:
                chan = ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
                nick = ircmsg.split('!')[0][1:]
                msg = ircmsg.split(' PRIVMSG ')[-1].split(' :')[1]
                print chan, nick, msg
                poll_results, voters = parse_votes(chan, nick, msg, poll_results, voters)
        except:
            if (time.time()-start) >= 60:
                break

    ircsock.settimeout(None)
    ircsock.send("PRIVMSG " + chan + " :Thanks for voting! Here are your results:\n")

    for entry in poll_results:
        ircsock.send("PRIVMSG " + base_chan + " :    " + entry + " ~ " + str(poll_results[entry]) + "\n")
