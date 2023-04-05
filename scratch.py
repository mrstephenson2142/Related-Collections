import xml.etree.ElementTree as ET

items = [
    {"url": "https://txarchives.org/ttusw/finding_aids/01423.xml", "title": "Pecos River Compact Commission (Texas) Records, 1979."},
    {"url": "https://txarchives.org/ttusw/finding_aids/20284.xml", "title": "Public Information Photograph Collection, 1923-1977."},
    {"url": "http://oralhistory.swco.ttu.edu/index.php?title=Wilson,_Mrs_J_C_1975-09-24", "title": "Mrs. J. C. Wilson oral history interview [abstract, sound recording], September 24, 1975."},
    {"url": "http://oralhistory.swco.ttu.edu/index.php?title=Couch,_Mr_and_Mrs_Joseph_E_and_Mrs_J_C_Wilson_1975-09-24", "title": "Mr. and Mrs. Joseph E. Couch and Mrs. J. C. Wilson oral history interview [abstract, sound recording], September 24, 1975."}
]

# create root element
root = ET.Element("items")

# add item elements with extref subelements


for item in items:
    
    # Skip empty items
    
    item_elem = ET.SubElement(root, "item")
    extref_elem = ET.SubElement(item_elem, "extref", {"xmlns:xlink": "http://www.w3.org/1999/xlink", "xlink:type": "simple", "xlink:show": "new", "xlink:actuate": "onRequest", "xlink:href": item["url"]})
    extref_elem.text = item["title"]

# convert to string and print
output = ET.tostring(root, encoding="unicode")
output = output.replace("</item><item>", "</item>\n\n<item>")
output = output.replace("<items>", "")
output = output.replace("</items>", "")
print(output.replace("</item><item>", "</item>\n\n<item>"))

# write output to file
with open("output.xml", "w") as outfile:
    outfile.write(formatted_output)