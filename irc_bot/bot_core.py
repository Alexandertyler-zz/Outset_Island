import socket
import time
import random
import sys
from os import listdir

import importlib

#importing tools for the subprocess launched to handle the irc client
from multiprocess import Process, Pipe
from multiprocess.connection import Listener, Client

ignore_list = []

def parse_commands(chan, nick, msg):
    print chan, nick, msg

    if chan == botnick:
        chan = nick

    if nick in ignore_list:
        return

    if msg.startswith('.roll'):
        roll(chan, nick, msg)

    if msg == '.notepad':
        notepad(chan)

    if msg.startswith(".suggest"):
        try:
            suggestion = msg.split('.suggest ')[1]
            suggest(chan, nick, suggestion)
        except:
           sendmsg(chan, "Sorry, please add a space between your command and the suggestion") 


    if msg == '.help':
        print_help(nick)

    if msg == '.fortune':
        irc_fortune.fortune(chan, nick)

    if msg.startswith(".8ball"):
        irc_8ball.eightball(chan, nick)
    
    if msg.startswith(".ignore"):
        if nick == 'alex':
            user = msg.split('.ignore ')[1]
            ignore(chan, user)
   
    if msg.startswith(".sleep"):
        sleep(chan, msg)

    if msg.startswith(".poll"):
        poll(chan, nick, msg)


def ping(response):
    ircsock.send("PONG "+ response+"\n")


def ignore(chan, user):
    if not user in ignore_list:
        ignore_list.append(user)
    ircsock.send("PRIVMSG " + chan + " :Due to high levels of spam in the vicinity, " + user + " will be ignored\n") 


def sendmsg(chan, msg):
    ircsock.send("PRIVMSG " + chan + " :" + msg +"\n")


def joinchannel(ircsock, chan):
    print "Joining channel", chan
    ircsock.send("JOIN  " + chan + "\n")


def hello(newnick):
    ircsock.send("PRIVMSG " + channel + " :Hello!\n")


def roll(chan, nick, msg):
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


def suggest(chan, nick, suggestion):
    ircsock.send("PRIVMSG " + chan + " :Thanks " + nick + " for your suggestion. Alex will be notified\n")
    with open("irc_suggestions.txt", "a+") as sugg_file:
        sugg_file.write(suggestion + '\n')

def sleep(chan, msg):
    try:
        ircsock.send("PRIVMSG " + chan + " :Perhaps just a moment's rest...\n")
        time_ts = msg.split('.sleep ')[1]
        time.sleep(int(time_ts))
        ircsock.send("PRIVMSG " + chan + " :Is the coffee ready yet?\n")
    except:
        ircsock.send("PRIVMSG " + chan + " :I can't sleep, too much caffeine\n")

def poll(base_chan, nick, msg):
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

def parse_votes(chan, nick, msg, poll_results, voters):
    if msg == ".kill":
        suicide(chan)

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

    

def print_help(nick):
   ircsock.send("PRIVMSG " + nick + " :How can I be of assistance? My current functions include:\n")
   ircsock.send("PRIVMSG " + nick + " :    .poll - start a poll that will run for a minute. Vote with .vote\n")
   ircsock.send("PRIVMSG " + nick + " :    .roll - roll a random number 1-100, d6, d20, or coin\n")
   ircsock.send("PRIVMSG " + nick + " :    .webex - get the webex credentials for the appliance team\n")
   ircsock.send("PRIVMSG " + nick + " :    .suggest - suggest a command you would like and I'll notify alex for you\n")
   ircsock.send("PRIVMSG " + nick + " :    .help - print this list of commands\n")
   ircsock.send("PRIVMSG " + nick + " :    .kill - emergency escape from the irc client, use sparingly please\n")
   ircsock.send("PRIVMSG " + nick + " :    .fortune - get your fortune for the day\n")
   ircsock.send("PRIVMSG " + nick + " :    .8ball - ask and you shall recieve an answer from the magic 8ball\n")
   ircsock.send("PRIVMSG " + nick + " :    .sleep - specify an amount of seconds you would like me to sleep for\n")
   ircsock.send("PRIVMSG " + nick + " :I'm still a work in progress so my commands will be updated all the time. Check back later for more options!\n")

def suicide(chan):
    ircsock.send("PRIVMSG " + chan + " :Goodbye cruel world\n")
    sys.exit(1)

def verify(ircsock):
    waiting_to_verify = True
    while waiting_to_verify:
        ircmsg = ircsock.recv(2048)
        ircmsg.strip('\n\r')
        print(ircmsg)

        if ircmsg.find("PING :") != -1:
            response = ircmsg.split("PING ")[1]
            ping(response)
            waiting_to_verify = False


def login_routine(server, port, bot_nick, channel):
    #handle defaults for server, port, and nickname
    #default channel is to not join one
    if not server:
        server='127.0.0.1'
    if not port:
        port=6667
    if not bot_nick:
        bot_nick='a-bot'

    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server, port))
    ircsock.send("USER "+ bot_nick +" "+ bot_nick +" "+ bot_nick +" :Developed by Cyberdyne Systems\n")
    ircsock.send("NICK " + bot_nick +"\n")

    ircsock.setblocking(0)

    #need to figure out case for verify
    #verify(ircsock)

    if channel:
        joinchannel(ircsock, channel)

    return ircsock, server, port, bot_nick, channel


def load_irc_commands():
    irc_dict = {}
    modules = [f for f in listdir('irc_commands') if f.startswith('irc')]
    for f_name in modules:
        module = f_name.split('.py')[0]
        command = module.split('irc_')[1]

        #import the module for the first time
        importlib.import_module('irc_commands.' + module)
        
        #store the module into our shell commands dictionary
        irc_dict[command]=module

    return irc_dict


def load_shell_commands():
    shell_dict = {}
    modules = [f for f in listdir('shell_commands') if f.startswith('shell')]
    for f_name in modules:
        module = f_name.split('.py')[0]
        command = module.split('shell_')[1]

        #import the module for the first time
        importlib.import_module('shell_commands.' + module)
        
        #store the module into our shell commands dictionary
        shell_dict[command]=module

    return shell_dict
    
#the main irc connection loop
#handles all irc communication
#communicates with main process via listener
def irc_loop(ircsock, bot_nick, channel, client):
    irc_dict = load_irc_commands()
    
    while 1:
        #check for console commands
        if client.poll():
            shell_command = client.recv()
            valid_shell = irc_dict.get(shell_command)
            if valid_shell:
                module = getattr(__import__('irc_commands'), valid_shell)
                module.action(ircsock, channel, 'shell', '')

        try:
            ircmsg = ircsock.recv(2048)
            ircmsg = ircmsg.strip('\n\r')

            if ircmsg.find("PING :") != -1:
                response = ircmsg.split("PING ")[1]
                ping(response)

            if ircmsg.find(' PRIVMSG ') != 1:
                chan = ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
                nick = ircmsg.split('!')[0][1:]
                msg = ircmsg.split(' PRIVMSG ')[-1].split(' :')[1]
        
                if msg.startswith('.'):
                    irc_command = msg.split(' ')[0]
                    irc_command = irc_command.split('.')[1]
                    valid_irc = irc_dict.get(irc_command)
                    if valid_irc:
                        module = getattr(__import__('irc_commands'),  valid_irc)
                        module.action(ircsock, channel, nick, msg)

        except:
            continue


#our main loop that the user interacts with
#has its own set of commands for controlling the bot or the script
def shell_loop(ircsock, channel, listener):
    connection = listener.accept()

    #using this method so I can reload it later if need be
    shell_dict = load_shell_commands()

    while 1:
        command = raw_input('irc_bot: ') 

        valid = shell_dict.get(command)
        if valid:
            module = getattr(__import__('shell_commands'), valid)
            module.action(connection)

        #connection.send('test')
        


if __name__ == "__main__":

    server = raw_input('Enter server: ')
    port = raw_input('Enter port: ')
    bot_nick = raw_input('Enter bot nick: ')
    channel = raw_input('Enter channel: ')

    ircsock, server, port, bot_nick, channel = login_routine(server, port, bot_nick, channel)
   
    #information for inter-process communication
    address = ('localhost', 2424)
    listener = Listener(address)
    client = Client(address)

    #two processes, one for console one for the irc channel
    irc = Process(target=irc_loop, args=(ircsock, bot_nick, channel, client))
    irc.start()

    #launch into the shell loop for interactive commands
    shell_loop(ircsock, channel, listener)
