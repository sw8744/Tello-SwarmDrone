from Commands import tello

# 명령어는 tello.명령어() 형식으로 사용, 명령어의 구문은 기존 구문과 차이가 거의 없음
try:
    tello.start()
    tello.takeoff()
    tello.forward(100)
    tello.check("battery")
    tello.end()
except KeyboardInterrupt:
    print('\n . . .\n')
    print("Exit")
