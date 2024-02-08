'''
This is the main file of the pingpong game.
'''
import tkinter as tk
from game import Game
def main():
    root = tk.Tk()
    root.title("PingPong Game")
    game = Game(root)
    game.start()
    root.mainloop()
if __name__ == "__main__":
    main()