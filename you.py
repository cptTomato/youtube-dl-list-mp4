#import operating system for commands
import os

#reading links from list.txt
data = open("list.txt", "a")

#getting links from list.txt
for line in daten:
    y = (line.rstrip())
    # download the videos
    os.system("sudo youtube-dl -f mp4 " + y)

data.close()
