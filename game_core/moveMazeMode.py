import math
import time
import Box2D

from .sound_controller import SoundController
from .tilemap import Map
from .points import *
from .maze_wall import *
from .car import Car
from .gameMode import GameMode
from .env import *
import pygame
# from .maze_wall import Wall

class MoveMazeMode(GameMode):
    def __init__(self, user_num: int, maze_no, time, sound_controller):
        super(MoveMazeMode, self).__init__()
        '''load map data'''
        self.user_num = user_num
        self.maze_id = maze_no - 1
        self.map_file = MOVE_MAZE_MAPS[self.maze_id]
        self.load_data()

        '''group of sprites'''
        self.worlds = []
        self.cars = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.wall_for_update = pygame.sprite.Group()
        self.all_points = pygame.sprite.Group() # Group inclouding end point, check points,etc.

        '''data set'''

        self.wall_info = []
        self.wall_vertices_for_Box2D = []
        self.car_info = []
        self.ranked_user = []  # pygame.sprite car
        self.result = []
        self.eliminated_user = []
        self.user_check_points = []

        self.game_end_time = time  # int, decide how many second the game will end even some users don't finish game
        pygame.font.init()
        self.status = "GAME_PASS"
        self.is_end = False
        self.x = 0
        self._init_world(user_num)
        self.new()
        '''sound'''
        self.sound_controller = SoundController(sound_controller)
        '''image'''
        self.info = pygame.image.load(path.join(IMAGE_DIR, info_image))

    def new(self):
        # initialize all variables and do all setup for a new game
        self.get_wall_info_v("V")
        self.get_wall_info_h("H")
        self.get_wall_info_h("1")
        self.get_wall_info_v("1")
        self.get_wall_info_v("v")
        self.get_wall_info_h("h")
        for wall_vertices in self.wall_vertices_for_Box2D:
            if wall_vertices["type"] == "1":
                for world in self.worlds:
                    wall = Wall(self, wall_vertices["vertices"], world)
                    if self.worlds.index(world) == 0:
                        self.walls.add(wall)
            elif wall_vertices["type"] == "V":
                for world in self.worlds:
                    wall = VerticalMoveWall(self, wall_vertices["vertices"], world, 4, 5)
                    self.wall_for_update.add(wall)
                    if self.worlds.index(world) == 0:
                        self.walls.add(wall)
            elif wall_vertices["type"] == "H":
                for world in self.worlds:
                    wall = HorizontalMoveWall(self, wall_vertices["vertices"], world, 3, 6)
                    self.wall_for_update.add(wall)
                    if self.worlds.index(world) == 0:
                        self.walls.add(wall)
            elif wall_vertices["type"] == "v":
                for world in self.worlds:
                    wall = VerticalMoveWall(self, wall_vertices["vertices"], world, 3, -5)
                    self.wall_for_update.add(wall)
                    if self.worlds.index(world) == 0:
                        self.walls.add(wall)
            elif wall_vertices["type"] == "h":
                for world in self.worlds:
                    wall = HorizontalMoveWall(self, wall_vertices["vertices"], world, 5, -7)
                    self.wall_for_update.add(wall)
                    if self.worlds.index(world) == 0:
                        self.walls.add(wall)

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "P":
                    for world in self.worlds:
                        x, y = (col + (TILE_LEFTTOP[0] / TILESIZE), row + (TILE_LEFTTOP[1] / TILESIZE))
                        self.car = Car(world, (x + TILESIZE / (2 * PPM), - y - TILESIZE / (2 * PPM)),
                                       self.worlds.index(world))
                        self.cars.add(self.car)
                        self.car_info.append(self.car.get_info())
                elif tile == "E":
                    self.end_point = End_point(self,
                                               (col + (TILE_LEFTTOP[0] / TILESIZE), row + (TILE_LEFTTOP[1] / TILESIZE)))
                elif tile == "C":
                    Check_point(self, (col + (TILE_LEFTTOP[0] / TILESIZE), row + (TILE_LEFTTOP[1] / TILESIZE)))

                elif tile == "O":
                    Outside_point(self, (col + (TILE_LEFTTOP[0] / TILESIZE), row + (TILE_LEFTTOP[1] / TILESIZE)))
        # self.pygame_point = [self.car.body.position[0] - (TILE_LEFTTOP[0] + TILE_WIDTH) / 2 / PPM,
        #                      self.car.body.position[1] + HEIGHT / 2 / PPM]
        self.pygame_point = [0,0]

    def update_sprite(self, command):
        '''update the model of game,call this fuction per frame'''
        self.car_info.clear()
        self.frame += 1
        self.handle_event()
        self._is_game_end()
        self.command = command
        self.wall_for_update.update()
        self.wall_info.clear()
        for wall in self.walls:
            vertices = [(wall.body.transform * v) for v in wall.box.shape.vertices]
            self.wall_info.append([vertices[0], vertices[1]])
            self.wall_info.append([vertices[2], vertices[1]])
            self.wall_info.append([vertices[3], vertices[0]])
            self.wall_info.append([vertices[2], vertices[3]])
        for car in self.cars:
            car.update(command["ml_" + str(car.car_no + 1) + "P"])
            car.rect.center = self.trnsfer_box2d_to_pygame(car.body.position)
            self.car_info.append(car.get_info())
            car.detect_distance(self.frame, self.wall_info)


        for point in self.all_points:
            point.rect.x, point.rect.y = self.trnsfer_box2d_to_pygame((point.x + TILESIZE/2/PPM, -point.y - TILESIZE/2/PPM))
        self.all_points.update()
        for world in self.worlds:
            world.Step(TIME_STEP, 10, 10)
            world.ClearForces()
        if self.is_end:
            self.running = False

    def load_data(self):
        game_folder = path.dirname(__file__)
        map_folder = path.join(path.dirname(__file__), "map")
        self.map = Map(path.join(map_folder, self.map_file))

    def _init_world(self, user_no: int):
        for i in range(user_no):
            world = Box2D.b2.world(gravity=(0, 0), doSleep=True, CollideConnected=False)
            self.worlds.append(world)

    def _is_game_end(self):
        if self.frame > FPS * self.game_end_time or len(self.eliminated_user) == len(self.cars):
            print("game end")
            for car in self.cars:
                if car not in self.eliminated_user and car.status:
                    car.end_frame = self.frame
                    self.eliminated_user.append(car)
                    self.user_check_points.append(car.check_point)
                    car.status = False
            self.is_end = True
            self.ranked_user = self.rank()
            self._print_result()
            self.status = "GAME OVER"

    def draw_grid(self):
        for x in range(TILE_LEFTTOP[0], TILE_WIDTH + TILE_LEFTTOP[0], TILESIZE):
            pygame.draw.line(self.screen, GREY, (x, TILE_LEFTTOP[1]), (x, TILE_HEIGHT + TILE_LEFTTOP[1]))
        for y in range(TILE_LEFTTOP[1], TILE_HEIGHT + TILE_LEFTTOP[1], TILESIZE):
            pygame.draw.line(self.screen, GREY, (TILE_LEFTTOP[0], y), (TILE_WIDTH + TILE_LEFTTOP[0], y))
