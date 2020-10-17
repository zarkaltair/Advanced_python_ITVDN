from xml.etree import ElementTree as ET


tree = ET.parse('data/test.xml')
root = tree.getroot()

children = root.getchildren()

for student_data in children:
    print('PK: ', student_data.attrib)
    for child in student_data:
        print(f'{child.tag} {child.text}')

root = ET.Element('record')
for i in range(10):
    sub_element = ET.SubElement(root, f'value{i}')
    sub_element.text = str(i * 10)

print(ET.dump(root)) # only for dev/trace

data = [
    {'x':10, 'y': 29, 'z': 90},
    {'x':11, 'y': 28, 'z': 91},
    {'x':12, 'y': 27, 'z': 92},
    {'x':13, 'y': 26, 'z': 93},
    {'x':14, 'y': 25, 'z': 94}
]

root = ET.Element('records')

for item in data:
    record = ET.SubElement(root, 'record')
    for key, value in item.items():
        e = ET.SubElement(record, key)
        e.text = str(value)

