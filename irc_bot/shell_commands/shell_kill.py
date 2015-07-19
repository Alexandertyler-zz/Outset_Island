import sys

def action(connection):
    connection.send('kill')
    connection.close()
    sys.exit(1)
