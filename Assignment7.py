import sys
from sys import argv
import shapely
import tkinter as tk
from rectpack import newPacker, PackingMode, PackingBin, SORT_AREA
class CustomCanvas:
    #assigning parameters for custom canvas using tk
    def __init__(self, height: int, width: int):
        self.root = tk.Tk()
        self.root.title("testCanvas")
        self.canvas = tk.Canvas(self.root, height = height, width = width)
        self.canvas.pack()

    #helped method to create a rectangle and display it
    def displayRects(self, rectangles):
        for shape in rectangles:
            self.canvas.create_rectangle(shape.x, shape.y, shape.x + shape.width, shape.y + shape.height, fill='blue',
                                    outline='black')
        self.root.mainloop()


class Rectangle:
    def __init__(self, height: int, width: int, x: int = 0, y: int = 0):
        self.height = height #setting it's own height and width
        self.width = width
        self.x = x
        self.y = y
def pack(allRec, canvasSize):
  #Creating new packer object
  height, width = canvasSize
  shapePacker = newPacker()

  for shape in allRec:
    #adding each rectangle and its paramters
    shapePacker.add_rect(shape.width, shape.height, rid=shape)

  #Packing
  shapePacker.add_bin(width, height)
  shapePacker.pack()

  #packedRects = []
  #Assining the x and y coordinates for each shape
  #packer will put the rect at shape[5] for each iterable
  #so we must go to shape[5] to modify rect atrributes
  for shape in shapePacker.rect_list():
    shape[5].x = shape[1]
    shape[5].y = shape[2]
        #creating a new Rectangle object, and appending it to packedRects
#    packedRects.append(Rectangle(shape.width, shape.height, x, y))
  return allRec

def main():
  file = sys.argv[1] #file path
  with open(file, 'r') as f:
      #since it is int,int: splitting with the , results in tuple (int int)
      canvasParam = tuple(map(int, f.readline().split(','))) #first line in file will be canvas args
      recsize = [tuple(map(int, line.split(','))) for line in f] #each line is going to be an arg for a rect
      #so I split the rec, store the args in a list of tuples so i can iterate thru it later

  #creating the canvas, using * to unpack tuple
  myCanvas = CustomCanvas(*canvasParam)

  #iterating thru all of our rectangle arguments that we tupled
  rectangles = [Rectangle(*arguments) for arguments in recsize]

  #calling for rectangles to be packed
  packedRects = pack(rectangles, canvasParam)

  #for shape in packedRects:
  #    myCanvas.canvas.create_rectangle(shape.x, shape.x, shape.x+shape.width, shape.y+shape.height, fill='blue',outline='black')

  #calling for helper method to display rects
  myCanvas.displayRects(packedRects)


if __name__ == '__main__':
  main()