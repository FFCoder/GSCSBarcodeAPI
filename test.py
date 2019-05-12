from blabel import LabelWriter

label_writer = LabelWriter("test.html", default_stylesheets=("test.css",), items_per_page=30)
records= [
]
for i in range(1,30):
    records.append(dict(sample_id="LR"+str(i).zfill(2)+"GVDY", sample_name="Sample " + str(i)))

label_writer.write_labels(records, target='qrcode_and_label.pdf')