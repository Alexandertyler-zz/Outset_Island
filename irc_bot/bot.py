import socket
import time
import random
import sys

server = "chat.norse-data.com"
channel = "#appliance"
botnick = "shitty_bot-alex"

bad_words = ["fuck", "shit", "cunt", "bitch", "ass", "asshole", "dick", "fucked"]

def parse_commands(chan, nick, msg):
    print chan, nick, msg

    if msg == '.roll':
        roll(chan, nick)

    if msg.startswith(".suggest"):
        try:
            suggestion = msg.split('.suggest ')[1]
            suggest(chan, nick, suggestion)
        except:
           sendmsg(chan, "Sorry, please add a space between your command and the suggestion") 


    if msg == '.help':
        print_help(chan)

    if msg == '.kill':
        suicide(chan)

    if msg == 
     
    
    for word in bad_words:
        if word in msg:
            sendmsg(channel, "~~Language Please~~")
            break
    

def ping(response):
    ircsock.send("PONG "+ response+"\n")
    

def introduction(chan):
    ircsock.send("PRIVMSG " + chan + " :Hello world! I am Alex's work in progress irc_bot.\n")
    print_help(chan) 


def sendmsg(chan, msg):
    ircsock.send("PRIVMSG " + chan + " :" + msg +"\n")


def joinchannel(chan):
    print "Joining channel", chan
    ircsock.send("JOIN  " + chan + "\n")


def hello(newnick):
    ircsock.send("PRIVMSG " + channel + " :Hello!\n")


def roll(chan, nick):
    rand_num = random.randint(1, 6)
    ircsock.send("PRIVMSG " + chan + " :" + nick + " has rolled a " + str(rand_num) + '\n')


def suggest(chan, nick, suggestion):
    ircsock.send("PRIVMSG " + chan + " :Thanks " + nick + " for your suggestion. Alex will be notified\n")
    with open("irc_suggestions.txt", "a+") as sugg_file:
        sugg_file.write(suggestion + '\n')


def print_help(chan):
   ircsock.send("PRIVMSG " + chan + " :How can I be of assistance? My current functions include:\n")
   ircsock.send("PRIVMSG " + chan + " :    .roll - roll a random number between 1 and 6\n")
   ircsock.send("PRIVMSG " + chan + " :    .suggest - suggest a command you would like and I'll notify alex for you\n")
   ircsock.send("PRIVMSG " + chan + " :    .help - print this list of commands\n")
   ircsock.send("PRIVMSG " + chan + " :    .kill - emergency escape from the irc client, use sparingly please\n")
   ircsock.send("PRIVMSG " + chan + " :I'm still a work in progress so my commands will be updated all the time. Check back later for more options!\n")

def suicide(chan):
    ircsock.send("PRIVMSG " + chan + " :Goodbye cruel world\n")
    sys.exit(1)

def verify():
    while 1:
        ircmsg = ircsock.recv(2048)
        ircmsg.strip('\n\r')
        print(ircmsg)

        if ircmsg.find("PING :") != -1:
            response = ircmsg.split("PING ")[1]
            ping(response)
            return

try:
    channel = '#' + str(sys.argv[1])
except:
    print "No channel specified, defaulting to #appliance"


ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Developed by Cyberdyne Systems\n")
ircsock.send("NICK " + botnick +"\n")

verify()
joinchannel(channel)
introduction(channel)

while 1:
    ircmsg = ircsock.recv(2048)
    ircmsg = ircmsg.strip('\n\r')

    if ircmsg.find(":Hello "+ botnick) != -1:
        hello()

    if ircmsg.find("PING :") != -1:
        response = ircmsg.split("PING ")[1]
        ping(response)

    if ircmsg.find(' PRIVMSG ') != 1:
        chan = ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
        nick = ircmsg.split('!')[0][1:]
        msg = ircmsg.split(' PRIVMSG ')[-1].split(' :')[1]
        
        parse_commands(chan, nick, msg)
