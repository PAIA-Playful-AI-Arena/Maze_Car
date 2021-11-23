# Maze Car

## 遊戲簡介
想要訓練屬於自己的迷宮自走車嗎？

想要跟朋友來場刺激的競賽嗎？

帶上你的自走車往終點衝刺吧！
![](https://i.imgur.com/ymZZMyO.png)


## 遊戲版本：
`3.1.4`

## 更新：
修正感測器變化量與座標變化量不符之問題。


## 遊戲玩法

此遊戲為迷宮自走車模擬遊戲，遊戲過程中玩家控制一台配備有三或五個超聲波感測器的車子，並運用正確的邏輯，讓車子可以最快的走出迷宮。

## 遊戲規則

遊戲最多可以六個人同時進行，目前共有三種遊戲模式。

✔小試身手模式：官方提供10個不同難度的基礎關卡，玩家可以透過關卡的遞進逐漸學習如何控制自走車通過不同的地形。

🚗經典迷宮模式：玩家可以選擇不同的地圖，目標為抵達迷宮終點，遊戲將記錄不同玩家完成迷宮所花費的時間，並根據速度快慢給出排名與積分。

🚧移動迷宮模式：相較於單純的迷宮，此模式中的地圖配有動態的牆壁，提高迷宮難度。與迷宮模式相同，將根據不同玩家的速度提供排名。

## 遊戲物件


### 座標系統
使用Box2D的座標系統，單位為cm，每公分換算為4像素，原點在迷宮區域的左上角，x 正方向為向右，y 正方向為向上。

### 遊戲區域

1000 \* 700 像素。

### 遊戲物件
- 自走車
    ![](https://i.imgur.com/srSifjm.png)

    50 \* 50 px大小的矩形

    遊戲開始時，所有玩家初始位置皆相同。

    遊戲過程中玩家可以收到自走車的中心點座標，作為位置的判斷。

    玩家透過控制雙輪的馬達轉速決定車子的行為，馬達轉速介於-225~255。若回傳值超過馬力範圍則視為已255的馬力正轉或逆轉，例如：回傳左輪馬力300、右輪馬力-400，則實際轉速等同於左輪255、右輪-255。

    車子顏色：1P:紅色; 2P:綠色; 3P:藍色; 4P:黃色; 5P:棕色; 6P:粉紅色。

- 終點

    50 \* 50 px大小的矩形

    每個關卡設置1個終點作為過關目標。

    遊戲過程中玩家可以收到終點的左上角座標，並且不會移動(數值不變)，作為位置的判斷。

- 檢查點

    40 \*40 px大小的矩形
