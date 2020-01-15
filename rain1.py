
import pygame, sys, random, time
from pygame.locals import *
pygame.init()                                 # pygame 초기화
pygame.display.set_caption("rain")            # 제목 달기
screen = pygame.display.set_mode((640, 480))  # 스크린 사이즈 지정. (가로(X) , 세로(Y)) 
clock = pygame.time.Clock()                   # 시계함수
raindrop_spawn_time=0


class Raindrop:
	def __init__(self):                   # 시작의 뜻. 
		self.x = random.randint(0, 640)   # 0에서 640중에서 렌덤하게 사용. 
		self.y = -5

	def move(self):                       # y 좌표만 이동. 
		self.y += 7
	
	def draw(self):
		pygame.draw.line(screen,(150,150,150), (self.x, self.y),(self.x, self.y+5),5)   # 화면, 색, 위치, 굵기.
		

raindrops = []



while 1:
	clock.tick(60)                     # 1초에 60번
	for event in pygame.event.get():   # 게임 루프를 도는 동안 일어나는 일을 감지 
		if event.type == pygame.QUIT:  # 버튼이 눌렸는지 확인. QUIT = X 이이콘 
			sys.exit()                 # 프로그램 종료

	raindrops.append(Raindrop())
	screen.fill((255,255,255))         # 스크린에 색칠하기. ()로 숫자를 묶는것은 튜플입니다.
	for raindrop in raindrops:
		raindrop.move()
		raindrop.draw()
    
	pygame.display.update()    
    



