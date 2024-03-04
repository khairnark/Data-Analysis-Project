import xml.etree.ElementTree as ET
import csv

def extract_tags(element, path='', result=[]):
    index = 1
    for child in element:
        current_path = f"{path}/{child.tag}[{index}]" if path else f"{child.tag}[{index}]"
        result.append((current_path, child.text))
        result = extract_tags(child, current_path, result)
        index += 1
    
    return result

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Path', 'Value'])
        writer.writerows(data)

tree = ET.parse('MISMO3.4 (4).xml')
root = tree.getroot()
tags_and_paths = extract_tags(root)
write_to_csv(tags_and_paths, 'MISMO.csv')
