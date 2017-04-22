from microbit import *
import music
# the 5x5 grid
grid = []
# nested for loops, variable scopes
for j in range(5):
    row = []
    for i in range(5):
        row.append(0)
    grid.append(row)
 
"""grid = [[0 for i in range(5)] for j in range(5)]"""
 
# converting grid to microbit image
grid_img = []
for row in grid:
    grid_img.append("") # empty string
    for light in row:
        # grid_img[len(grid_img) - 1] += str(light)
        # string concatenation, list index targeting
        grid_img[-1] += str(light) # [-1] is the last element, [-2] is second last and so on
                                   # [-len(grid_img)] is the first element
grid_img = ':'.join(grid_img)
 
grid_img = ':'.join([''.join([str(light) for light in row]) for row in grid])
 
# microbit set_pixel function
# display.set_pixel(x,y,int(brightness))
while True:
    """for i in range(0,5):
       sleep(200)
       for x in range(0,5):
           for y in range(0,5):
               display.set_pixel(x,y,abs(x-i)+abs(y-i))"""
    notes = list("cdefgab")
    octaves = list("1234")
    song = []
    for i in range(4):
        for j in range(4):
            for k in range(j,j+4):
                song.append(notes[k]+octaves[3-i])
        for j in range(4):
            for k in range(3-j,7-j):
                song.append(notes[k]+octaves[3-i])
    for i in range(4):
        for j in range(4):
            for k in range(j,j+4):
                song.append(notes[k]+octaves[i])
        for j in range(4):
            for k in range(3-j,7-j):
                song.append(notes[k]+octaves[i])
    music.set_tempo(ticks=4,bpm=60)
    music.play(song, pin=pin0, wait=True, loop=False)
