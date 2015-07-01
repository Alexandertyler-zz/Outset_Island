import socket
import time
import random

server = "chat.norse-data.com"
channel = "#appliance"
botnick = "shitty_bot-alex"

bad_words = ["fuck", "shit", "cunt", "bitch", "ass", "asshole", "dick", "fucked"] 


def ping(response):
    ircsock.send("PONG "+ response+"\n")
    
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

def print_help(chan):
   ircsock.send("PRIVMSG " + chan + " :How can I be of assistance? My current functions include .roll and .help\n") 

def verify():
    while 1:
        ircmsg = ircsock.recv(2048)
        ircmsg.strip('\n\r')
        print(ircmsg)

        if ircmsg.find("PING :") != -1:
            response = ircmsg.split("PING ")[1]
            ping(response)
            return

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Developed by Cyberdyne Systems\n")
ircsock.send("NICK " + botnick +"\n")

verify()

joinchannel(channel)

while 1:
    ircmsg = ircsock.recv(2048)
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)

    if ircmsg.find(":Hello "+ botnick) != -1:
        hello()

    if ircmsg.find("PING :") != -1:
        response = ircmsg.split("PING ")[1]
        ping(response)

    if ircmsg.find(' PRIVMSG ') != 1:
        nick = ircmsg.split('!')[0][1:]
        chan = ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
        msg = ircmsg.split(' PRIVMSG ')[-1].split(' :')[1]
        print nick, chan, msg
        
        if msg == '.roll':
            roll(chan, nick)

        if msg == '.help':
            print_help(chan)

        
        
        """
        for word in bad_words:
            if word in msg:
                sendmsg(channel, "~~Language Please~~")
                break
        """
