import os.path
from pypdf import PdfReader


reader = PdfReader ("TMP/Test_doc.pdf")

#print(reader.pages)
#print(reader.pages[1].extract_text())
#assert "Tarantool" in reader.pages[1]

print(os.path.getsize("TMP/Test_doc.pdf"))
assert os.path.getsize("TMP/Test_doc.pdf") > 0