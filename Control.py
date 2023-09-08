import threading
import socket
import sys
import time
import platform

# 드론과의 연결 설정
host = ''
port = 9000
locaddr = (host, port)

# UDP 통신을 위한 소켓 설정
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 드론의 IP와 포트 설정
tello_address = ('192.168.10.1', 8889)

# 소켓 통신 시작
sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\nExit . . .\n')
            break


print('\r\n\r\nTello Python3 Beta 1.0.\r\n')

print('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print('end -- quit program.\r\n')

# 통신을 위한 쓰레드 생성
recvThread = threading.Thread(target=recv)
recvThread.start()

# 드론에게 명령어를 사용한다는 명령어 전달
string = "command"
sent = sock.sendto(string.encode("utf-8"), tello_address)

while True:
    try:
        python_version = str(platform.python_version())
        version_init_num = int(python_version.partition('.')[0])
        # print (version_init_num)
        if version_init_num == 3:
            msg = input("")

        if not msg:
            break

        if 'end' in msg:
            print('...')
            sock.close()
            break

    # 임의의 명령어 테스트, 만일 임의로 명령어를 제작할 시 다음과 같이 진행하면 됨.
        # if msg == 'test':
            # print('test success') # 명령어 성공 시 출력
            # string = "forward 250" # 명령어 설정
            # sent = sock.sendto(string.encode("utf-8"), tello_address) # 드론에게 명령어 전달
            # continue

        # 드론에게 명령어 전달
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print('\n . . .\n')
        sock.close()
        break