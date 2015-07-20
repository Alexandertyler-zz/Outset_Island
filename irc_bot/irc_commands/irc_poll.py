import time

def action(ircsock, chan, nick, msg):
    poll_values = msg.split(".poll ")
    ircsock.send("PRIVMSG " + chan + " :" + nick + " has started a poll. Use .vote to submit your opinion. Poll will be open for one minute. Topic - '" + poll_values[1] + "'\n")

    start = time.time()
    poll_results = {}
    voters = []
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
                new_chan = ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
                new_nick = ircmsg.split('!')[0][1:]
                new_msg = ircmsg.split(' PRIVMSG ')[-1].split(' :')[1]
                poll_results, voters = parse_votes(new_chan, new_nick, new_msg, poll_results, voters)
        except:
            if (time.time()-start) >= 60:
                break
    ircsock.send("PRIVMSG " + chan + " :Thanks for voting! Here are your results:\n")

    for entry in poll_results:
        ircsock.send("PRIVMSG " + base_chan + " :    " + entry + " ~ " + str(poll_results[entry]) + "\n")

def parse_votes(chan, nick, msg, poll_results, voters):
    if msg.startswith(".vote"):
        if nick not in voters:
            option = msg.split(".vote ")[1]
            if option.lower() in poll_results:
                poll_results[option.lower()] += 1
            else:
                poll_results[option.lower()] = 1
            voters.append(nick)
        else:
            ircsock.send("PRIVMSG " + nick + " :You can only vote once per poll\n")

    return poll_results, voters
