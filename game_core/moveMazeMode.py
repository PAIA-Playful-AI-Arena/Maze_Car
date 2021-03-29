import time
import Box2D

from .maze_imformation import Move_Maze_Size, Move_Maze, Normal_Maze_Size
from .maze_wall import Move_Wall
from .car import Car
from .gameMode import GameMode
from .env import *
import pygame
# from .maze_wall import Wall


class MoveMazeMode(GameMode):
    def __init__(self, user_num: int, maze_no, time, sound_controller):
        super(MoveMazeMode, self).__init__()
        self.game_end_time = time  # int, decide how many second the game will end even some users don't finish game
        self.ranked_user = []  # pygame.sprite car
        self.ranked_score = {"1P": 0, "2P": 0, "3P": 0, "4P": 0, "5P": 0, "6P": 0}  # 積分
        pygame.font.init()
        self.status = "GAME_PASS"
        self.is_end = False
        self.result = []
        self.x = 0
        self.maze_id = maze_no - 1
        self.size = 4 / Move_Maze_Size[self.maze_id]
        self.start_pos = (22, 3)

        '''set group'''
        self.car_info = []
        self.cars = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.worlds = []
        self._init_world(user_num)
        self._init_car()
        self._init_maze(self.maze_id)
        self.eliminated_user = []
        self.user_time = []
        self.wall_information = []

        '''sound'''
        self.sound_controller = sound_controller

        '''image'''
        self.info = pygame.image.load(path.join(IMAGE_DIR, info_image))

    def update_sprite(self, command):
        '''update the model of game,call this fuction per frame'''
        self.car_info = []
        self.frame += 1
        self.handle_event()

        self._is_game_end()
        self.walls.update()
        self.wall_information = []
        for wall in self.walls:
            for info in wall.wall_info:
                self.wall_information.append(info)
        for car in self.cars:
            car.update(command["ml_" + str(car.car_no + 1) + "P"])
            self.car_info.append(car.get_info())
            self._is_car_arrive_end(car)
            car.detect_distance(self.frame, self.wall_information)
        for world in self.worlds:
            world.Step(TIME_STEP, 10, 10)
            world.ClearForces()
        if self.is_end:
            self.running = False

    def detect_collision(self):
        super(MoveMazeMode, self).detect_collision()
        pass

    def _print_result(self):
        if self.is_end and self.x == 0:
            for user in self.ranked_user:
                self.result.append(str(user.car_no + 1) + "P:" + str(user.end_time) + "s")
                self.ranked_score[str(user.car_no + 1) + "P"] = user.score
            print("score:", self.ranked_score)
            self.x += 1
            print(self.result)
        pass

    def _init_world(self, user_no: int):
        for i in range(user_no):
            world = Box2D.b2.world(gravity=(0, 0), doSleep=True, CollideConnected=False)
            self.worlds.append(world)
        pass

    def _init_car(self):
        if Move_Maze_Size[self.maze_id] == 3:
            self.start_pos = (16, 3)
        elif Move_Maze_Size[self.maze_id] == 4:
            self.start_pos = (22, 3)
        elif Move_Maze_Size[self.maze_id] == 5:
            self.start_pos = (28, 3)
        elif Move_Maze_Size[self.maze_id] == 6:
            self.start_pos = (34, 3)
        for world in self.worlds:
            self.car = Car(world, self.start_pos, self.worlds.index(world), self.size)
            self.cars.add(self.car)
            self.car_info.append(self.car.get_info())
            pass

    def _init_maze(self, maze_no):
        for world in self.worlds:
            for wall in Move_Maze[maze_no]:
                maze_wall = Move_Wall(world, wall["vertices_init"], self.size, wall["is_move"], velocity=wall["velocity"],
                                 vertices_end=wall["vertices_end"])
                self.walls.add(maze_wall)
        pass

    def _is_game_end(self):
        if self.frame > FPS * self.game_end_time or len(self.eliminated_user) == len(self.cars):
            for car in self.cars:
                if car not in self.eliminated_user and car.status:
                    car.end_time = round(time.time() - self.start_time)
                    self.eliminated_user.append(car)
                    self.user_time.append(car.end_time)
                    car.status = False
            self.is_end = True
            self.rank()
            self._print_result()
            self.status = "GAME OVER"
        pass

    def _is_car_arrive_end(self, car):
        if car.status:
            if car.body.position[1] > 6 * Move_Maze_Size[self.maze_id] + 1:

                car.end_time = round(time.time() - self.start_time)
                self.eliminated_user.append(car)
                self.user_time.append(car.end_time)
                car.status = False
        pass

    def draw_bg(self):
        '''show the background and imformation on screen,call this fuction per frame'''
        super(MoveMazeMode, self).draw_bg()
        self.screen.fill(BLACK)
        self.screen.blit(self.info, pygame.Rect(507, 20, 306, 480))
        if self.is_end == False:
            self.draw_time(time.time())
        pass

        '''畫出每台車子的資訊'''
        self._draw_user_imformation()

    def drawWorld(self):
        '''show all cars and lanes on screen,call this fuction per frame'''
        super(MoveMazeMode, self).drawWorld()
        for wall in self.walls:
            vertices = [(wall.body.transform * v) * PPM * self.size for v in wall.box.shape.vertices]
            vertices = [(v[0], HEIGHT - v[1]) for v in vertices]
            pygame.draw.polygon(self.screen, WHITE, vertices)

        self.cars.draw(self.screen)
        pass

    def _draw_user_imformation(self):
        for i in range(6):
            for car in self.cars:
                if car.car_no == i:
                    if i % 2 == 0:
                        if car.status:
                            self.draw_information(self.screen, YELLOW, "L:" + str(car.sensor_L) + "cm", 600,
                                                  178 + 20 + 94 * i / 2)
                            self.draw_information(self.screen, RED, "F:" + str(car.sensor_F) + "cm", 600,
                                                  178 + 40 + 94 * i / 2)
                            self.draw_information(self.screen, LIGHT_BLUE, "R:" + str(car.sensor_R) + "cm", 600,
                                                  178 + 60 + 94 * i / 2)
                        else:
                            self.draw_information(self.screen, WHITE, str(car.end_time) + "s",
                                                  600, 178 + 40 + 94 * (i // 2))

                    else:
                        if car.status:
                            self.draw_information(self.screen, YELLOW, "L:" + str(car.sensor_L) + "cm", 730,
                                                  178 + 20 + 94 * (i // 2))
                            self.draw_information(self.screen, RED, "F:" + str(car.sensor_F) + "cm", 730,
                                                  178 + 40 + 94 * (i // 2))
                            self.draw_information(self.screen, LIGHT_BLUE, "R:" + str(car.sensor_R) + "cm", 730,
                                                  178 + 60 + 94 * (i // 2))
                        else:
                            self.draw_information(self.screen, WHITE, str(car.end_time) + "s",
                                                  730, 178 + 40 + 94 * (i // 2))

    def rank(self):
        while len(self.eliminated_user) > 0:
            for car in self.eliminated_user:
                if car.end_time == min(self.user_time):
                    self.ranked_user.append(car)
                    self.user_time.remove(car.end_time)
                    self.eliminated_user.remove(car)
        for i in range(len(self.ranked_user)):
            if self.ranked_user[i].end_time == self.ranked_user[i - 1].end_time:
                if i == 0:
                    self.ranked_user[i].score = 6
                else:
                    for j in range(1, i + 1):
                        if self.ranked_user[i - j].end_time == self.ranked_user[i].end_time:
                            if i == j:
                                self.ranked_user[i].score = 6
                            else:
                                pass
                            pass
                        else:
                            self.ranked_user[i].score = 6 - (i - j + 1)
                            break
            else:
                self.ranked_user[i].score = 6 - i