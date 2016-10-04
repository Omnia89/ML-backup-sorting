import xml.etree.ElementTree as ET
import os.path

class moneylover_parser:

    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            print('Error: file doesn\'t exists')
            return []
        extension = os.path.splitext(file_path)
        if extension != '.mxl':
            print('Error: wrong file extension')
            return []
        self.file_path = file_path
        print('File imported')

    def simplifyMXL(self, destination_path):

        root = ET.parse(self.file_path)
        first_node = root.getroot()
        
        self.destination_path = destination_path + '/extracted_mxl/'

        for table_node in first_node:
            if table_node.tag == 'table':
                extractTable(self,table_node)

        return True

    def extractTable(self, table_node):
        if not table_node[0][0].tag == 'row':
            print('Warning: no rows found for table node named: ' + table_node.attrib['name'])
            return False

        table_name = table_node.attrib['name']
        output_file = open(self.destination_path + table_name, 'w')
        
        
        text_row = ''

        for col_name in table_node[0]:
            text_row += col_name.attrib['name'] + ';'
        text_row = text_row[:-1] + '\n'

        output_file.write(text_row)
        
        for column in table_node:
            text_row = ''
            for line in column:
                text_row += (line.text if line.text else 'Null') + ';'
            text_row = text_row[:-1] + '\n'
            output_file.write(text_row)

        output_file.close()
        print('Info: exported table named: ' + table_node.attrib['name'])
        return True