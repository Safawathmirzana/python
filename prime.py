# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17T3Yy4Vd54llKO31QtEPpy7op9mEX6Yt
"""

string = input("Enter the numbers: ")
original_list = [int(x) for x in string.split()]
new_list = [x for x in original_list if x % 2 != 0]
print("New List:", new_list)

