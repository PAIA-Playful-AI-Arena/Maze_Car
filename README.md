# **Maze Car**

<img src="https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Maze_Car/refs/heads/main/asset/logo.png" alt="logo" width="100"/>

![Maze_Car](https://img.shields.io/github/v/tag/PAIA-Playful-AI-Arena/Maze_Car)
[![Python 3.9](https://img.shields.io/badge/python->3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![MLGame](https://img.shields.io/badge/MLGame->10.4.6a2-<COLOR>.svg)](https://github.com/PAIA-Playful-AI-Arena/MLGame)


在錯綜復雜的棋盤迷宮中，想辦法讓你的AI自走車突破重圍，不會迷失在其之中，走到終點。本遊戲也提供多元的關卡，隨著遊戲難度提升，考驗各位玩家如何在多變的環境下，依然能夠逃出迷宮。

- `遊戲目標` 在時間結束前，抵達終點。

- `失敗條件` 時間結束前，自走車尚未走到終點，即算失敗。

<br />


# 更新內容(4.0.1)
1. 更新遊戲物件尺寸
2. 新增計分機制
3. 開放使用者匯入自定義關卡
---

# 啟動方式

- 直接啟動 [main.py](https://github.com/PAIA-Playful-AI-Arena/Maze_Car/blob/main/main.py) 即可執行

# 遊戲參數設定

```python
# main.py

game = MazeCar.MazeCar(user_num=1, map_num=4,map_file=None, time_to_play=200, sound='off')
```

- `user_num`：玩家數量，最多可以6個玩家同時進行同一場遊戲。
- `map_num`：選擇要執行的地圖編號，不同的模式中，地圖不會共用編號。
- `map_file`：可匯入自定義的地圖路徑，使用此設定會覆蓋掉地圖設定。
- `time_to_play`：遊戲結束時間，單位為FPS，時間到會強制結束遊戲。
- `sound`：可輸入"on"或是"off"，控制是否播放遊戲音效。

## 玩法

- 使用鍵盤 上、下、左、右 (1P)與 Ｗ、Ａ、Ｓ、Ｄ (2P)控制自走車

# 座標系統
![座標系統](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/game-web-readme/dev/maze_car/images/side1.png)
- 使用 `Box2D` 的座標系統，長度單位為 `cm` 。
- `左上角`為原點 (0,0)，`Ｘ軸`向`右`為正，`Y軸`向`上`為正。
- 使用 Tiled 來繪製地圖，地圖一格為 `5cm`。
- 所有座標皆回傳物件`中心點`之座標。
- 每 `1cm` 換算為 `3.2px` 。
# 遊戲物件

<br />

## 自走車

- 彩色長方形搭配輪子和感測器的小車，每台車的顏色不同。
- 自走車 12.5 x 10 cm。
- 提供的座標為中心點的座標。


## 感測器

- 可透過感測器測量距離`車身`到`牆壁`的距離。
- 一台車有 5 個感測器。

## 迷宮地圖

- 迷宮的白色區塊為實牆，自走車需繞道尋找出口。

## 檢查點

- 綠色牌子
- 每通過一個檢查點，系統皆會紀錄時間，在沒有通過終點情況下，就是判斷誰最快通過最多檢查點。
- 檢查點大小 15 x 15 cm。

## 終點

- 紅色牌子，整個迷宮的終點。
- 愈快碰到分數愈高。
- 終點大小 15 x 15 cm。

# 計分機制
1. 每通過一個檢查點、終點得 `1000分`
2. 每多花`一個frame`走到檢查點、終點，扣`1分`
3. `總分 = 檢查點個數x1000 - 花費時間`

---

# 進階說明

## 使用ＡＩ玩遊戲

```bash

python -m mlgame -i  ml/ml_play_template.py ./ --map_num 1 --time_to_play 450

python -m mlgame -i  ml/ml_play_template.py ./ --map_file ./src/map/map_1.json --time_to_play 450
```

## ＡＩ範例
[ＡＩ範例](./ml/ml_play_manual.py)

## 遊戲資訊

- `scene_info` 的資料格式如下

```json
{
  "frame": 215,
  "status": "GAME_PASS",
  "x": 52.47,
  "y": -63.58,
  "angle": 84.98821459719791,
  "R_sensor": 18.2,
  "L_sensor": -1,
  "F_sensor": 43.3,
  "L_T_sensor": 62.8,
  "R_T_sensor": 26.8,
  "end_x": 42.5,
  "end_y": -62.5
}

```

* `frame`：遊戲畫面更新的編號
* `L_T_sensor`：玩家自己車子左前超聲波感測器的值，資料型態為數值，單位是公分。
* `R_T_sensor`：玩家自己車子右前超聲波感測器的值，資料型態為數值
* `L_sensor`：玩家自己車子左邊超聲波感測器的值，資料型態為數值
* `F_sensor`：玩家自己車子前面超聲波感測器的值，資料型態為數值
* `R_sensor`：玩家自己車子右邊超聲波感測器的值，資料型態為數值
* `x`：玩家自己車子的x座標，該座標系統原點位於迷宮左上角，x軸向右為正。
* `y`：玩家自己車子的y座標，該座標系統原點位於迷宮左上角，y軸向上為正。
* `end_x`：終點x座標，該座標系統原點位於迷宮左上角，x軸向右為正。
* `end_y`：終點y座標，該座標系統原點位於迷宮左上角，y軸向上為正。
* `angle`：玩家自己車子的朝向，車子向上為0度，數值`逆時鐘`遞增至360
* `status`： 目前遊戲的狀態
    - `GAME_ALIVE`：遊戲進行中
    - `GAME_PASS`：遊戲通關
    - `GAME_OVER`：遊戲結束

## 動作指令

- 在 update() 最後要回傳一個字典，資料型態如下。
    ```python
    {
            'left_PWM': 0,
            'right_PWM': 0
    }
    ```
    其中`left_PWM`與`right_PWM`分別代表左輪與右輪的馬力，接受範圍為-255~255。


## 遊戲結果

- 最後結果會顯示在console介面中，若是PAIA伺服器上執行，會回傳下列資訊到平台上。

```json
{
  "frame_used": 96,
  "status": "finish",
  "attachment": [
    {
      "player_num": "1P",
      "rank": 1,
      "used_frame": 95,
      "frame_limit": 5000,
      "frame_percent": 1.9,
      "total_checkpoints": 2,
      "check_points": 2,
      "remain_points": 0,
      "pass_percent": 100.0,
      "remain_percent": 0.0,
      "score": 1905
    }
  ]
}

```

- `frame_used`：表示遊戲使用了多少個frame
- `status`：表示遊戲結束的狀態
  - `fail`:遊戲過程出現問題
  - `passed`:單人的情況下，成功走到終點，回傳通過
  - `un_passed`:沒有任何人走到終點，回傳不通過
  - `finish`:多人的情況下，任一人走到終點，回傳完成
- `attachment`：紀錄遊戲各個玩家的結果與分數等資訊
    - `player_num`：玩家編號
    - `rank`：排名
    - `used_frame`：個別玩家到達終點使用的frame數
    - `frame_limit`：該局遊戲所設定的時間上限
    - `frame_percent`：
        ![](https://i.imgur.com/QuI8HmM.png)
    - `total_checkpoints`：該地圖的總檢查點數量
    - `check_points`：玩家通過的檢查點數量
    - `remain_points`：玩家未通過的檢查點數量
    - `pass_percent`：
        ![](https://i.imgur.com/QuMt5Lu.png)

    - `remain_percent`：
        ![](https://i.imgur.com/mym3FVm.png)
    - `score`
      - `總分 = 檢查點個數x1000 - 花費時間`
---

# 地圖製作說明
[地圖製作教學](https://github.com/PAIA-Playful-AI-Arena/Maze_Car/blob/main/map_editor.md)

---
