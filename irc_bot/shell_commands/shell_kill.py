import sys

def action(client):
    client.send('.kill')
    client.close()
    sys.exit(1)
