# 🎮 Hand Gesture Controlled Tower of Hanoi

An interactive **Tower of Hanoi game** controlled using **hand
gestures** via your webcam.\
Built using **Python**, **OpenCV**, **MediaPipe**, and **Tkinter**, this
project lets you pick, move, and drop disks simply by performing a
**pinch gesture** (index finger + thumb touching).

------------------------------------------------------------------------

## ✨ Features

-   🖐️ **Hand gesture control** using MediaPipe\
-   🧱 Real-time **disk grabbing & dropping** with pinch detection\
-   🎥 Webcam-based gesture tracking\
-   🧠 Fully working **Tower of Hanoi logic**\
-   📊 Move counter to track attempts\
-   🏆 Win detection with on-screen celebration\
-   🎨 Graphical UI rendered using OpenCV\
-   🎚 Choose any number of disks (minimum 3)

------------------------------------------------------------------------

## 📁 File Structure

-   `main.py` -- Entire game code (hand tracking + game logic + UI
    rendering)\
-   `README.md` -- Documentation for the project

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python\
-   OpenCV\
-   MediaPipe\
-   Tkinter\
-   Math utilities

------------------------------------------------------------------------

## 🚀 Getting Started

``` bash
1. Clone the repository : git clone https://github.com/your-username/hand-gesture-hanoi.git

2. Install dependencies : 
   pip install opencv-python mediapipe

3. Run the game :
   python main.py
```

------------------------------------------------------------------------

## 🎮 How to Play

-   ✋ Show your hand in front of the camera\
-   🤏 **Pinch (Index + Thumb)** near the top disk to **pick it up**\
-   Move your hand to another rod\
-   🤏 Pinch again to **release the disk**\
-   Repeat until all disks move to the **Destination** rod

------------------------------------------------------------------------

## 📌 Controls

  Action      Gesture/Key
  ----------- ---------------
  Pick disk   Pinch gesture
  Drop disk   Pinch gesture
  Quit game   Press `Q`

------------------------------------------------------------------------

## 📱 Responsive Experience

The game dynamically adjusts movement based on your hand's position and
webcam input---no mouse or keyboard required during gameplay.

------------------------------------------------------------------------

## 🧠 Game Goal

Move the entire stack of disks from the **Source Rod → Destination Rod**
following these rules:

1.  Only **one disk** can be moved at a time\
2.  Only the **topmost disk** can be picked\
3.  A **larger disk cannot be placed** over a smaller one

------------------------------------------------------------------------

## 🏆 Winning

When all disks are correctly placed on the destination rod, a **YOU
WIN!** message appears.
