'''
This file contains the Game class which manages the game logic.
'''
import tkinter as tk
from paddle import Paddle
from ball import Ball
class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="black")
        self.canvas.pack()
        self.paddle = Paddle(self.canvas)
        self.ball = Ball(self.canvas, self.paddle)
    def start(self):
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.paddle.move_paddle)
        self.canvas.bind("<KeyRelease>", self.paddle.stop_paddle)
        self.ball.move_ball()
        self.paddle.update()
    def update(self):
        print("update paddle1")
        self.canvas.move(self.paddle.paddle, self.paddle.x_speed, 0)
        paddle_pos = self.canvas.coords(self.paddle.paddle)
        if paddle_pos[0] < 0:
            self.paddle.x_speed = 0
        elif paddle_pos[2] > 800:
            self.paddle.x_speed = 0
        self.canvas.after(10, self.update) # The bug is here, just init position once.
class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.paddle = self.canvas.create_rectangle(0, 0, 100, 10, fill="pink")
        self.canvas.move(self.paddle, 350, 380)
        self.x_speed = 0
    def move_paddle(self, event):
        if event.keysym == "Left":
            self.x_speed = -2
        elif event.keysym == "Right":
            self.x_speed = 2
        self.update()    
    def stop_paddle(self, event):
        # print("Stop paddle")
        self.x_speed = 0
        self.update() # Append refresh logic
    def update(self):
        print("Update paddle position")
        self.canvas.move(self.paddle, self.x_speed, 0)
        paddle_pos = self.canvas.coords(self.paddle)
        if paddle_pos[0] < 0:
            self.x_speed = 0
        elif paddle_pos[2] > 800:
            self.x_speed = 0
class Ball:
    def __init__(self, canvas, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.ball = self.canvas.create_oval(0, 0, 20, 20, fill="white")
        self.canvas.move(self.ball, 390, 190)
        self.x_speed = 2
        self.y_speed = -2
    def move_ball(self):
        self.canvas.move(self.ball, self.x_speed, self.y_speed)
        ball_pos = self.canvas.coords(self.ball)
        paddle_pos = self.canvas.coords(self.paddle.paddle)
        if ball_pos[1] <= 0:
            self.y_speed = 2
        elif ball_pos[3] >= 400:
            self.y_speed = -2
        elif ball_pos[0] <= 0 or ball_pos[2] >= 800:
            self.x_speed = -self.x_speed
        elif ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and ball_pos[3] >= paddle_pos[1]:
            self.y_speed = -2
        self.canvas.after(10, self.move_ball)