import xml.etree.ElementTree as ET

tree = ET.parse("recipes.xml")
root = tree.getroot()

print(f'The root has the tag {root.tag}')
print(f'The recipe was published in {root.attrib["published"]}')

def print_element(element):
    print(element.tag)
    if element.text and not element.text.isspace():
        print(element.text)

    for child in element:
        print_element(child)

print_element(root)