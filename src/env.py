from os import path

PPM = 16  # pixels per meter
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS

'''width and height'''
WIDTH = 1000
HEIGHT = 700
TILE_WIDTH = 540  # 大小
TILE_HEIGHT = 540

'''tile-base'''
TILESIZE = 16
TILE_LEFTTOP = 16, 16  # pixel
GRIDWIDTH = (TILE_WIDTH + TILE_LEFTTOP[0]) / TILESIZE
GRIDHEIGHT = (TILE_HEIGHT + TILE_LEFTTOP[1]) / TILESIZE

'''sensor set trans'''
sensor_trans = ((1, 0),
                (0, 1),
                (-1, 0),
                (0, -1))

'''environment data'''
FPS = 30

'''color'''
BLACK = (0, 0, 0)
WHITE = "#F5F5F5"
RED = "#ff0000"
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GREY = (140, 140, 140)
BLUE = (30, 60, 205)
LIGHT_BLUE = (33, 161, 241)
BROWN = (199, 178, 153)
PINK = (255, 105, 180)
MEDIUMPURPLE = (147, 112, 219)

'''object size'''
car_size = (50, 40)

'''data path'''
ASSET_IMAGE_DIR = path.join(path.dirname(__file__), "../asset/image")
IMAGE_DIR = path.join(path.dirname(__file__), 'image')
SOUND_DIR = path.join(path.dirname(__file__), '../asset/sound')

'''image'''
BG_IMG = "bg_img.png"
BG_URL = 'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/bg_img.png'
BG_PATH = path.join(ASSET_IMAGE_DIR, BG_IMG)
INFO_NAME = "info.png"
INFO_URL = 'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/info.png'

LOGO = "logo.png"
LOGO_URL = 'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/logo.png'

TMF_LOGO = "TMFlogo.png"
TMF_LOGO_URL = 'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/TMFlogo.png'
ENDPOINT_IMG = "endpoint.png"
ENDPOINT_URL = f'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/{ENDPOINT_IMG}'
ENDPOINT_PATH = path.join(ASSET_IMAGE_DIR, ENDPOINT_IMG)

CHECKPOINT_IMG = "checkpoint.png"
CHECKPOINT_URL = f'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/{CHECKPOINT_IMG}'
CHECKPOINT_PATH = path.join(ASSET_IMAGE_DIR, CHECKPOINT_IMG)
CHECKPOINT2_IMG = "checkpoint_2.png"
CHECKPOINT2_URL = f'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/{CHECKPOINT2_IMG}'
CHECKPOINT2_PATH = path.join(ASSET_IMAGE_DIR, CHECKPOINT2_IMG)

CARS_NAME = ["car_01.png", "car_02.png", "car_03.png", "car_04.png", "car_05.png", "car_06.png", ]
CARS_URL = ['https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/car_01.png',
            'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/car_02.png',
            'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/car_03.png',
            'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/car_04.png',
            'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/car_05.png',
            'https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/main/asset/image/car_06.png'
            ]

'''map_file'''
PRACTICE_MAPS = ["level_1.json", "level_2.json", "level_3.json", "level_4.json", "level_5.json", "level_6.json"]
NORMAL_MAZE_MAPS = ["normal_map_1.json", "normal_map_2.json", "normal_map_3.json", "normal_map_3.json",
                    "normal_map_3.json", "normal_map_3.json"]
MOVE_MAZE_MAPS = ["move_map_1.json", "move_map_2.json", "move_map_3.json", "move_map_4.json", "move_map_4.json",
                  "move_map_4.json"]
BG_COLOR = "#8493B1"
