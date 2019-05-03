import barcode


class BarcodeGenerator(object):
    def __init__(self):
        self.base = barcode.get_barcode_class('code_128')
    def generate(txt):
        
