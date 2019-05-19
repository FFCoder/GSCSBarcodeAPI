import pandas
from blabel import LabelWriter

TEMPLATE_FILE = "template.html"
STYLESHEET = "style.css"
TARGET_FILE = "output.pdf"

# Reads the Excel sheet as a Pandas Dataframe 
dataFrame = pandas.read_excel('export.xlsx', dtype=str)
# Sorts based off of school
sortedDF = dataFrame.sort_values('Location')
# Converting into a Dict for blabel
records = sortedDF.to_dict(orient='record')

label_writer = LabelWriter(TEMPLATE_FILE,default_stylesheets=(STYLESHEET,))

#print(records)
#label_writer.write_labels(records, target=TARGET_FILE)

testDF = sortedDF.head(30)
label_writer.write_labels(testDF.to_dict(orient='record'), target=TARGET_FILE)
