#!/usr/bin/python
# -*- coding: utf8 -*-

board_visible = list("________")
board = ['A', 'B', 'C', 'D'] * 2

flipped = []

while True:
    print " "+" ".join(board_visible)
    print " 0 1 2 3 4 5 6 7"

    if len(flipped) == 2:
        a, b = [board[i] for i in flipped]
        if a != b:
            for i in flipped:
                board_visible[i] = "_"
        flipped = []

    user_input = raw_input(" : ")

    if user_input == 'q':
        break

    if user_input.isdigit():
        idx = int(user_input)
        if idx < len(board):
            if board_visible[idx] != "_":
                print " ! you cant turn this card"
                continue
            board_visible[idx] = board[idx]
            flipped.append(idx)
            continue
    
    print(" ! wrong input")
