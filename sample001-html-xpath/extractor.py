import csv

import xml.etree.ElementTree as ET

class Extractor:
    def execute(self):
        print("Start")

        xml_content = self._load_xml('words.xml')
        if xml_content:
            print("XML content loaded successfully.")
        else:
            print("Failed to load XML content.")

        parsed_data = self._parse_xml(xml_content)
        if parsed_data:
            print("XML content parsed successfully.")
        else:
            print("Failed to parse XML content.")

        if parsed_data:
            self._save_to_csv(parsed_data, 'output.csv')


    def _load_xml(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def _parse_xml(self, xml_content) -> dict:
        print("Parsing XML content...")
        try:
            root = ET.fromstring(xml_content)
            data = {}
            for child in root:
                deu = child[0][0][1][0].text
                eng = child[0][0][1][1].text
                data[deu] = eng
                print(f"Parsed: {deu} -> {eng}")
            return data
        except ET.ParseError as e:
            print(f"XML parsing error: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    def _save_to_csv(self, data: dict, file_path: str):
        try:
            with open('output.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)
                writer.writerow(['German', 'English'])
                for deu, eng in data.items():
                    writer.writerow([deu, eng])
            print("Data saved to output.csv successfully.")
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}")