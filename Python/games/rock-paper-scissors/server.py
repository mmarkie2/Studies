import socket
import pickle
from _thread import *
from game import Game


def threaded_client(conn, p, gameId, games):
    global idCount
    conn.send(str.encode(str(p)))

    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == 'reset':
                        game.reset_went()
                    elif data != 'get':
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print('Connection lost')
    try:
        del games[gameId]
        print('Closing Game ', gameId)
    except:
        pass

    idCount -= 1
    conn.close()


def main():
    global idCount

    server = '192.168.0.122'
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        print(e)

    s.listen(2)
    print('Waiting for connection, Server Started')

    connected = set()
    games = {}
    idCount = 0

    while True:
        conn, addr = s.accept()
        print('Connected to: ', addr)

        idCount += 1
        p = 0
        gameId = (idCount - 1) // 2
        if idCount % 2 == 1:
            games[gameId] = Game(gameId)
            print('Creating a new game...')
        else:
            games[gameId].ready = True
            p = 1

        start_new_thread(threaded_client, (conn, p, gameId, games))

main()
