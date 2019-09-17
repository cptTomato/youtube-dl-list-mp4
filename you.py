data = open("list.txt", "a")
import os

for line in daten:
    y = (line.rstrip())
    os.system("sudo youtube-dl " + y)

data.close()
