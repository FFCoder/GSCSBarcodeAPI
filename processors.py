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
        values = dataframe.get_values()
        
    except:
        print("Unknown Exception: Failed to load spreadsheet.")
        return False
    
    for record in values:
        aTag = record[0]
        model = record[1]
        location = record[2]

        tempAsset = Asset()
        tempAsset.Asset_Tag = aTag
        tempAsset.Model = model
        tempAsset.Location = location

        assets.append(tempAsset)

        label_writer = LabelWriter(templateFile, default_stylesheets=(stylesheet))
        label_writer.write_labels(assets, target="export.pdf")
    return True
    
writeLabels("export.xlsx","template.html","style.css")