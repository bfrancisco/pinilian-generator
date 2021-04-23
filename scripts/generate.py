from PIL import Image

def paint1(r, c):
    #paint pattern 1 (6x6). [r][c] is the reference point.
    #top
    board.putpixel((r+2, c+1), c1)
    board.putpixel((r+3, c+1), c1)
    #left
    board.putpixel((r+1, c+2), c1)
    board.putpixel((r+1, c+3), c1)
    #right
    board.putpixel((r+4, c+2), c1)
    board.putpixel((r+4, c+3), c1)
    #bottom
    board.putpixel((r+2, c+4), c1)
    board.putpixel((r+3, c+4), c1)
def paint2(r, c):
    #paint pattern 2 (6x6).
    for i in range(1,5):
        board.putpixel((r+2, c+i), c1)
        board.putpixel((r+3, c+i), c1)
def paint3(r, c):
    #paint pattern 3 (6x6).
    for i in range(2,4):
        board.putpixel((r+2, c+i), c1)
        board.putpixel((r+3, c+i), c1)

def paint_pattern(r, c, N):
    #paint pattern 1,2,3 (18x18).
    if N == 1:
        for i in range(0, 13, 6):
            for j in range(0, 13, 6):
                paint1(r+i, c+j)
    elif N == 2:
        for i in range(0, 13, 6):
            for j in range(0, 13, 6):
                paint2(r+i, c+j)
    elif N == 3:
        for i in range(0, 13, 6):
            for j in range(0, 13, 6):
                paint3(r+i, c+j)
    
def paint_board():
    for i in range(1,size+1):
        for j in range(1, size+1):
            if i%2 != 0 and j%2 != 0:
                paint_pattern((i-1)*18, (j-1)*18, 1)
            elif i%2 !=0 and j%2 == 0:
                paint_pattern((i-1)*18, (j-1)*18, 3)
            elif i%2 == 0 and j%2 != 0:
                paint_pattern((i-1)*18, (j-1)*18, 2)
            new_frame = board.copy()
            frames.append(new_frame)

size = int(input("Size:")) # asks for size
c1 = tuple([int(i) for i in input("Pattern Color:").split()])
c2 = tuple([int(i) for i in input("Background Color:").split()])
fname = input("File name:")
frames = []
board = Image.new('RGB', (size*18,size*18), color=c2) # make a size*18 x size*18 grid
frames.append(board)
paint_board()
#print(len(frames))
inp = int(input("Save as:\n[1]PNG\n[2]GIF\n"))
if inp==1:
    board.save(fname + ".png", format='PNG')
    print("PNG created!")
elif inp==2:
    frames[0].save(fname + ".gif", format='GIF', save_all=True, append_images=frames[1:], duration=100, loop=0)
    print("GIF created!")