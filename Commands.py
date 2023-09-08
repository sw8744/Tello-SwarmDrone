import socket
import threading

host = ''
port = 9000
locaddr = (host, port)

# UDP 통신을 위한 소켓 설정
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 드론의 IP와 포트 설정
tello_address = ('192.168.10.1', 8889)

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\nExit . . .\n')
            break



class tello:
    @staticmethod
    def start():
        recvThread = threading.Thread(target=recv)
        recvThread.start()
        sock.bind(locaddr)
        print('Start Tello Drone')
        string = "command"
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def takeoff():
        string = "takeoff"
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def land():
        string = "land"
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def forward(distance):
        string = "forward " + str(distance)
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def back(distance):
        string = "back " + str(distance)
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def left(distance):
        string = "left " + str(distance)
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def right(distance):
        string = "right " + str(distance)
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def up(distance):
        string = "up " + str(distance)
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def down(distance):
        string = "down " + str(distance)
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def cw(angle):
        string = "cw " + str(angle)
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def ccw(angle):
        string = "ccw " + str(angle)
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def flip(direction):
        string = "flip " + str(direction)
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def speed(speed):
        string = "speed " + str(speed)
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def check(value):
        string = str(value) + "?"
        sent = sock.sendto(string.encode("utf-8"), tello_address)

    @staticmethod
    def end():
        sock.close()
        print('Close Tello Drone')