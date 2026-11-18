import xml.etree.ElementTree as ET

SAMPLE = "<rss><channel><item><title>Hello RSS</title></item></channel></rss>"

def extract_titles(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    return [el.text for el in root.findall(".//item/title") if el.text]

if __name__ == "__main__":
    print(extract_titles(SAMPLE))
