import sys
import pygame

from settings import Settings
from ship import Ship
class AlienInvasion :
    """게임 자원과 동작을 전체적으로 관리하는 클래스 """
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #배경색 설정
        self.bg_color = (230,230,230)


    def run_game(self):
        """게임의 루프 시작"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #루프를 반복 할 때마다 화면을 다시 그린다.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #가장 최근 그린 화면을 표시
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()