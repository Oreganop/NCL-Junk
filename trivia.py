import socket
from time import sleep
import csv
from collections import OrderedDict

with open('trivia.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    triviaCSV = list(reader)

triviaDict = {}
for line in triviaCSV:
    triviaDict[line[0]] = line[1:]

OrderedDict(sorted(triviaDict.items(), key=lambda t: (-len(t[0]), t[0])))

buf = 1024
msg = "REDACTED\r\n"

def open_sock():
    TCP_IP = 'REDACTED'
    TCP_PORT = 9090
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    data = s.recv(1024)
    print('['+data+']')
    s.sendall('d8d7ca1e337f6bfd83fe2cd3d2b75e1c\r\n')
    return s, 0

s, questionCounter = open_sock()

while(True):
    data = s.recv(1024)
    print('['+data+']')
    if( 'That\'s the wrong answer...' in data ):
        s.close()
        s, questionCounter = open_sock()
        quit()
        continue
    else:
        msg = ''
        for i, (state, trivia) in enumerate(triviaDict.iteritems()):
            if data.find('fun fact') != -1:
                try: 
                    print 'found trivia'
                    print 'on state '+ state+ ': '+ trivia[8]
                    if data.find(trivia[8][:25]) != -1 and trivia[8] != '':
                        msg = state
                        print trivia[8]
                        print 'Choosing '+msg
                        break
                    else:
                        pass
                except:
                    pass
            elif data.find(state) != -1 or data.find(trivia[2]) != -1: 
                print 'Found '+state
                if data.find("What is the capital") != -1:
                    msg = trivia[2]
                    print 'Choosing '+msg
                    break
                elif data.find("has been the state capital of") != -1:
                    msg = trivia[3]
                    print 'Choosing '+msg
                    break
                elif data.find("established") != -1:
                    msg = trivia[1]
                    print 'Choosing '+msg
                print 'Found '+trivia[2]
                if data.find('municipal') != -1:
                    msg = trivia[5]
                    print 'Choosing '+msg
                    break
                if data.find('metropolitan') != -1:
                    msg = trivia[6]
                    print 'Choosing '+msg
                    break
                if data.find('which') != -1:
                    msg = state
                    print 'Choosing '+msg
            elif data.find(trivia[0]) != -1:
                msg = state
                print 'Choosing '+msg
                break
        if msg == '':
            msg = raw_input()
        msg = msg + '\r\n'
    questionCounter += 1
    print("Sending "+msg)
    s.sendall(msg)
    last_data = data
