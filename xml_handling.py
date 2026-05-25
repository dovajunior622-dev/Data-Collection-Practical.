import xml.etree.ElementTree as ET

# XML Data String
data = """<student>
<name>Ada</name>
<department>Cybersecurity</department>
</student>"""

# Parse XML string
root = ET.fromstring(data)

print("--- XML Parsing Result ---")
print(f"Student Name: {root.find('name').text}") # Output: Ada
print(f"Department: {root.find('department').text}")
