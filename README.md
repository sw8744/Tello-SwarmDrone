# Tello Swarm Drone Project
> 이 프로젝트는 인천과학고등학교 공학 동아리인 Plutonium과 정보 동아리인 Raibit이 협력하여 진행하는 드론 편대비행 프로젝트입니다.

## 1. 이 프로그램의 원리
이 프로그램은 Socket 통신을 이용하여 드론과 Python을 연결합니다. 그래서 UDP 통신을 통한 명령어를 Tello 드론에게 입력하여 드론이 명령을 수행하도록 합니다.

명령어는 다음과 같습니다.
![](https://i.ibb.co/p30hs0p/commands.png)

## 2. 이 프로그램의 구성
이 프로그램은 기존 프로그램과 달리, 더 편리하게 Tello Drone에 코딩할 수 있도록 설계되었습니다.

기존의 명령어를 작성하고, 기체에 보내는 일련의 과정을 함수 하나로 집약시켰습니다.
```
from Commands import tello
tello.start() # 드론과 연결 시작
tello.takeoff() # 이륙
tello.forward(n) # 전진
tello.back(n) # 후진
tello.left(n) # 좌로 이동
tello.right(n) # 우로 이동
tello.up(n) # 상승
tello.down(n) # 하강
tello.cw(n) # 시계 회전
tello.ccw(n) # 반시계 회전
tello.land() # 착륙
tello.flip() # 드론 회전
tello.end() # 드론과 연결 종료
tello.check(str) # 드론 상태 확인 / str = battery, time, speed
```
