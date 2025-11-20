import cv2
import mediapipe as mp
import math
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()
while True:
    try:
        NUM_DISKS = int(simpledialog.askstring("Tower of Hanoi", "Enter number of disks (3 or more):"))
        if NUM_DISKS >= 3:
            break
        else:
            messagebox.showerror("Invalid Input", "Please enter a number 3 or more.")
    except:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        continue

WIDTH, HEIGHT = 1000, 700
ROD_X = [250, 500, 750]
ROD_Y = 600

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

COLORS = [(255, 0, 0), (0, 255, 0), (0, 128, 255), (128, 0, 255), (255, 255, 0), (0, 255, 255)]

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def draw_rods(frame):
    for i in range(3):
        cv2.rectangle(frame, (ROD_X[i] - 5, ROD_Y - 250), (ROD_X[i] + 5, ROD_Y), (150, 150, 150), -1)
        cv2.rectangle(frame, (ROD_X[i] - 80, ROD_Y), (ROD_X[i] + 80, ROD_Y + 15), (100, 100, 100), -1)
        label = ["Source", "Auxiliary", "Destination"][i]
        cv2.putText(frame, label, (ROD_X[i] - 50, ROD_Y + 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

def draw_disks(frame):
    for i in range(3):
        for j, size in enumerate(rods[i]):
            w = size * 15 + 40
            x1 = ROD_X[i] - w
            x2 = ROD_X[i] + w
            y = ROD_Y - (j + 1) * 25
            color = COLORS[size % len(COLORS)]
            cv2.rectangle(frame, (x1, y), (x2, y + 20), color, -1)
            cv2.putText(frame, f"{size}", (ROD_X[i] - 10, y + 17), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

def get_rod_index(x):
    for i in range(3):
        if abs(x - ROD_X[i]) < 70:
            return i
    return None

def game_loop():
    global rods, holding, held_disk, held_from, pinch_active, move_count

    cap = cv2.VideoCapture(0)
    rods = [[i for i in range(NUM_DISKS, 0, -1)], [], []]
    holding = False
    held_disk = None
    held_from = None
    pinch_active = False
    move_count = 0
    win_shown = False

    while True:
        ret, img = cap.read()
        if not ret:
            break

        img = cv2.flip(img, 1)
        frame = cv2.resize(img, (WIDTH, HEIGHT))
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        index_tip, thumb_tip = None, None

        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
                h, w, _ = frame.shape
                index_tip = (int(hand.landmark[8].x * w), int(hand.landmark[8].y * h))
                thumb_tip = (int(hand.landmark[4].x * w), int(hand.landmark[4].y * h))

                if index_tip and thumb_tip:
                    d = distance(index_tip, thumb_tip)
                    cv2.circle(frame, index_tip, 8, (255, 255, 255), -1)
                    cv2.circle(frame, thumb_tip, 8, (255, 255, 255), -1)

                    if d < 35:
                        if not pinch_active:
                            pinch_active = True
                            if not holding:
                                rod_idx = get_rod_index(index_tip[0])
                                if rod_idx is not None and rods[rod_idx]:
                                    held_disk = rods[rod_idx].pop()
                                    held_from = rod_idx
                                    holding = True
                            else:
                                rod_idx = get_rod_index(index_tip[0])
                                if rod_idx is not None:
                                    if not rods[rod_idx] or rods[rod_idx][-1] > held_disk:
                                        rods[rod_idx].append(held_disk)
                                        move_count += 1
                                    else:
                                        rods[held_from].append(held_disk)
                                    held_disk = None
                                    holding = False
                    else:
                        pinch_active = False

        if holding and index_tip:
            w = held_disk * 15 + 40
            x1 = index_tip[0] - w
            x2 = index_tip[0] + w
            y = index_tip[1]
            color = COLORS[held_disk % len(COLORS)]
            cv2.rectangle(frame, (x1, y), (x2, y + 20), color, -1)

        draw_rods(frame)
        draw_disks(frame)

        cv2.putText(frame, f"Moves: {move_count}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        cv2.putText(frame, "Pinch to Grab/Release Disk", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        if len(rods[2]) == NUM_DISKS:
            cv2.putText(frame, " YOU WIN! ", (300, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 8)
            if not win_shown:
                win_shown = True

        cv2.imshow("Tower of Hanoi - Hand Controlled", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

game_loop()
