def action(ircsock, chan, nick, msg):
    try:
        suggestion = msg.split('suggest ')[1]
    except:
           sendmsg(chan, "Sorry, please add a space between your command and the suggestion")  
    
    ircsock.send("PRIVMSG " + chan + " :Thanks " + nick + " for your suggestion. Alex will be notified\n")
    with open("irc_suggestions.txt", "a+") as sugg_file:
        sugg_file.write(suggestion + '\n')
