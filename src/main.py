import tkinter
from tkinter import messagebox

"""counter"""

turn = 0

gb1t = " "
gb2t = " "
gb3t = " "
gb4t = " "
gb5t = " "
gb6t = " "
gb7t = " "
gb8t = " "
gb9t = " "

"""functions"""


def winner(I):

  if gb1t == I and gb2t == I and gb3t == I:
    return True
  elif gb4t == I and gb5t == I and gb6t == I:
    return True
  elif gb7t == I and gb8t == I and gb9t == I:
    return True
  elif gb1t == I and gb4t == I and gb7t == I:
    return True
  elif gb2t == I and gb5t == I and gb8t == I:
    return True
  elif gb3t == I and gb6t == I and gb9t == I:
    return True
  elif gb1t == I and gb5t == I and gb9t == I:
    return True
  elif gb3t == I and gb5t == I and gb7t == I:
    return True

  else:

    return False


def isFull():
  if gb1t != " " and gb2t != " " and gb3t != " " and gb4t != " " and gb5t != " " and gb6t != " " and gb7t != " " and gb8t != " " and gb9t != " ":
    return True
  else:
    return False


def checkScore():
  if isFull():
    gover = messagebox.showinfo("GAME OVER", "Board is full")
  elif winner("X"):
    gover = messagebox.showinfo("GAME OVER", "Player 1 wins!")
  elif winner("O"):
    gover = messagebox.showinfo("GAME OVER", "Player 2 wins!")


def XO_gb1():
  global gb1t, turn
  if gb1t == " ":
    if turn % 2 == 0:
      player1.config(bg="#87CEEB")
      player2.config(bg="#448EE4")
      gb1t = "X"

    elif turn % 2 == 1:
      player1.config(bg="#448EE4")
      player2.config(bg="#87CEEB")
      gb1t = "O"
  else:
    pass
  turn += 1
  gb1.config(text=gb1t)
  checkScore()


def XO_gb2():
  global gb2t, turn
  if gb2t == " ":
    if turn % 2 == 0:
      player1.config(bg="#87CEEB")
      player2.config(bg="#448EE4")
      gb2t = "X"
    elif turn % 2 == 1:
      player1.config(bg="#448EE4")
      player2.config(bg="#87CEEB")
      gb2t = "O"
  else:
    pass
  turn += 1
  gb2.config(text=gb2t)
  checkScore()


def XO_gb3():
  global gb3t, turn
  if gb3t == " ":
    if turn % 2 == 0:
      player1.config(bg="#87CEEB")
      player2.config(bg="#448EE4")
      gb3t = "X"
    elif turn % 2 == 1:
      player1.config(bg="#448EE4")
      player2.config(bg="#87CEEB")
      gb3t = "O"
  else:
    pass
  turn += 1
  gb3.config(text=gb3t)
  checkScore()


def XO_gb4():
  global gb4t, turn
  if gb4t == " ":
    if turn % 2 == 0:
      player1.config(bg="#87CEEB")
      player2.config(bg="#448EE4")
      gb4t = "X"
    elif turn % 2 == 1:
      player1.config(bg="#448EE4")
      player2.config(bg="#87CEEB")
      gb4t = "O"
  else:
    pass
  turn += 1
  gb4.config(text=gb4t)
  checkScore()


def XO_gb5():
  global gb5t, turn
  if gb5t == " ":
    if turn % 2 == 0:
      player1.config(bg="#87CEEB")
      player2.config(bg="#448EE4")
      gb5t = "X"
    elif turn % 2 == 1:
      player1.config(bg="#448EE4")
      player2.config(bg="#87CEEB")
      gb5t = "O"
  else:
    pass
  turn += 1
  gb5.config(text=gb5t)
  checkScore()


def XO_gb6():
  global gb6t, turn
  if gb6t == " ":
    if turn % 2 == 0:
      player1.config(bg="#87CEEB")
      player2.config(bg="#448EE4")
      gb6t = "X"
    elif turn % 2 == 1:
      player1.config(bg="#448EE4")
      player2.config(bg="#87CEEB")
      gb6t = "O"
  else:
    pass
  turn += 1
  gb6.config(text=gb6t)
  checkScore()


def XO_gb7():
  global gb7t, turn
  if gb7t == " ":
    if turn % 2 == 0:
      player1.config(bg="#87CEEB")
      player2.config(bg="#448EE4")
      gb7t = "X"
    elif turn % 2 == 1:
      player1.config(bg="#448EE4")
      player2.config(bg="#87CEEB")
      gb7t = "O"
  else:
    pass
  turn += 1
  gb7.config(text=gb7t)
  checkScore()


def XO_gb8():
  global gb8t, turn
  if gb8t == " ":
    if turn % 2 == 0:
      player1.config(bg="#87CEEB")
      player2.config(bg="#448EE4")
      gb8t = "X"
    elif turn % 2 == 1:
      player1.config(bg="#448EE4")
      player2.config(bg="#87CEEB")
      gb8t = "O"
  else:
    pass
  turn += 1
  gb8.config(text=gb8t)
  checkScore()


def XO_gb9():
  global gb9t, turn
  if gb9t == " ":
    if turn % 2 == 0:
      player1.config(bg="#87CEEB")
      player2.config(bg="#448EE4")
      gb9t = "X"
    elif turn % 2 == 1:
      player1.config(bg="#448EE4")
      player2.config(bg="#87CEEB")
      gb9t = "O"
  else:
    pass
  turn += 1
  gb9.config(text=gb9t)
  checkScore()


"""FUNCTIONS END"""

window = tkinter.Tk()
window.title("TicTacToe")
window.geometry("500x500")

player1 = tkinter.Button(text="Player 1: X", bg="#87CEEB")
player2 = tkinter.Button(text="Player 2: O", bg="#448EE4")

player1.pack(pady=20)
player2.pack(pady=0)
"""GAMEBOARD"""

gb1 = tkinter.Button(text=gb1t, bg="#800000", command=XO_gb1, fg="White")
gb2 = tkinter.Button(text=gb2t, bg="#800000", command=XO_gb2, fg="White")
gb3 = tkinter.Button(text=gb3t, bg="#800000", command=XO_gb3, fg="White")
gb4 = tkinter.Button(text=gb4t, bg="#800000", command=XO_gb4, fg="White")
gb5 = tkinter.Button(text=gb5t, bg="#800000", command=XO_gb5, fg="White")
gb6 = tkinter.Button(text=gb6t, bg="#800000", command=XO_gb6, fg="White")
gb7 = tkinter.Button(text=gb7t, bg="#800000", command=XO_gb7, fg="White")
gb8 = tkinter.Button(text=gb8t, bg="#800000", command=XO_gb8, fg="White")
gb9 = tkinter.Button(text=gb9t, bg="#800000", command=XO_gb9, fg="White")

gb1.place(x=170, y=200, width=50, height=50)
gb2.place(x=220, y=200, width=50, height=50)
gb3.place(x=270, y=200, width=50, height=50)
gb4.place(x=170, y=250, width=50, height=50)
gb5.place(x=220, y=250, width=50, height=50)
gb6.place(x=270, y=250, width=50, height=50)
gb7.place(x=170, y=300, width=50, height=50)
gb8.place(x=220, y=300, width=50, height=50)
gb9.place(x=270, y=300, width=50, height=50)

window.update()
