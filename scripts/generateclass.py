from PIL import Image

class Generate:
    def __init__(self, sz, c1, c2):
        self.sz = sz
        self.c1 = c1
        self.c2 = c2
        self.board = Image.new('RGB', (sz*18,sz*18), color=self.c2)
        self.frames = [self.board]

    def paint1(self, r, c):
        #paint pattern 1 (6x6). [r][c] is the reference point.
        #top
        self.board.putpixel((r+2, c+1), self.c1)
        self.board.putpixel((r+3, c+1), self.c1)
        #left
        self.board.putpixel((r+1, c+2), self.c1)
        self.board.putpixel((r+1, c+3), self.c1)
        #right
        self.board.putpixel((r+4, c+2), self.c1)
        self.board.putpixel((r+4, c+3), self.c1)
        #bottom
        self.board.putpixel((r+2, c+4), self.c1)
        self.board.putpixel((r+3, c+4), self.c1)
    def paint2(self, r, c):
        #paint pattern 2 (6x6).
        for i in range(1,5):
            self.board.putpixel((r+2, c+i), self.c1)
            self.board.putpixel((r+3, c+i), self.c1)
    def paint3(self, r, c):
        #paint pattern 3 (6x6).
        for i in range(2,4):
            self.board.putpixel((r+2, c+i), self.c1)
            self.board.putpixel((r+3, c+i), self.c1)

    def paint_pattern(self, r, c, N):
        #paint pattern 1,2,3 (18x18).
        if N == 1:
            for i in range(0, 13, 6):
                for j in range(0, 13, 6):
                    self.paint1(r+i, c+j)
        elif N == 2:
            for i in range(0, 13, 6):
                for j in range(0, 13, 6):
                    self.paint2(r+i, c+j)
        elif N == 3:
            for i in range(0, 13, 6):
                for j in range(0, 13, 6):
                    self.paint3(r+i, c+j)
        
    def paint_board(self):
        for i in range(1,self.sz+1):
            for j in range(1, self.sz+1):
                if i%2 != 0 and j%2 != 0:
                    self.paint_pattern((i-1)*18, (j-1)*18, 1)
                elif i%2 !=0 and j%2 == 0:
                    self.paint_pattern((i-1)*18, (j-1)*18, 3)
                elif i%2 == 0 and j%2 != 0:
                    self.paint_pattern((i-1)*18, (j-1)*18, 2)
                new_frame = self.board.copy()
                self.frames.append(new_frame)

    def generatePNG(self):
        self.paint_board()
        return self.board
    
    def generateGIF(self):
        self.paint_board()
        return self.frames
