import os

start="../TextFiles/test.txt"
final="../test.txt"

if os.path.exists(start):
    os.rename(start,final)