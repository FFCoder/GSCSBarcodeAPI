from blabel import LabelWriter
import pandas
import sys

values = ""

class Asset(object):
    Asset_Tag = ""
    Model = ""
    Location = ""
    def __str__(self):
        return "<Asset> %s" % self.Asset_Tag

def writeLabels(excelFile, templateFile, stylesheet=None):
    assets = list()
    try:
        dataframe = pandas.read_excel(excelFile,dtype='str')
        
    except:
        print("Unknown Exception: Failed to load spreadsheet.")
        return False

        records = dataframe.to_dict(orient='record')
        label_writer = LabelWriter(templateFile, default_stylesheets=(stylesheet))
        label_writer.write_labels(assets, target="export.pdf")
    return True
    
writeLabels("export.xlsx","template.html","style.css")