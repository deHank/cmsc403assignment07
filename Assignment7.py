import sys
from sys import argv
import shapely
import tkinter as tk
from rectpack import newPacker
class CustomCanvas:
    #assigning parameters for custom canvas using tk
    def __init__(self, height: int, width: int):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(height = height, width = width)
        self.canvas.pack()
        self.root.mainloop()

class Rectangle:
    def __init__(self, height: int, width: int, x: int = 0, y: int = 0):
        self.height = height #setting it's own height and width
        self.width = width
        self.x = x
        self.y = y
def pack(allRec: list, canvasSize: int):
  #Creating new packer object
  shapePacker = newPacker()

  for shape in allRec:
    #adding each rectangle and its paramters
    shapePacker.add_rect(shape.width, shape.height, shape)

  shapePacker.pack()

  packedRects = []
  for shape in shapePacker.rect_list():
    x, y = shape.x, shape.y
    #creating a new Rectangle object, and appending it to packedRects
    packedRects.append(Rectangle(shape.width, shape.height,x, y))
  return packedRects

def main():
  file = sys.argv[1] #file path
  with open(file, 'r') as f:
      #since it is int,int: splitting with the , results in tuple (int int)
      canvasParam = tuple(f.readline().split(',')) #first line in file will be canvas args
      recsize = [tuple(map(int, line.split(','))) for line in f] #each line is going to be an arg for a rect
      #so I split the rec, store the args in a list of tuples so i can iterate thru it later

  #creating the canvas, using * to unpack tuple
  myCanvas = CustomCanvas(*canvasParam)

  #iterating thru all of our rectangle arguments that we tupled
  rectangles = [Rectangle(*arguments) for arguments in recsize]

if __name__ == '__main__':
  main()