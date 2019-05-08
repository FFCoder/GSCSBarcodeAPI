from reportlab.graphics.barcode import code128
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
import sys


class LabelMaker(object):
    """ Base Class for Adding Labels to a PDF. Assumes Letter Paper Size and Portrait Orientation """
    def __init__(self, labelSize, numOfLabels=None, fileName=None):
        if(isinstance(labelSize, tuple) != True):
            raise Exception("Label Size Must be a Tuple!")
            sys.exit(-1)
        if not fileName:
            self.fileName = "labels.pdf"
        else:
            self.fileName = fileName
        self.labelSize = labelSize
        self.numOfLabels = numOfLabels
        self.canvas = canvas.Canvas(self.fileName, pagesize=letter)
        
    def addLabel(self, label):
        ## TODO: Work on this method
        pass

class Label(object):
    def __init__(self):
        pass

