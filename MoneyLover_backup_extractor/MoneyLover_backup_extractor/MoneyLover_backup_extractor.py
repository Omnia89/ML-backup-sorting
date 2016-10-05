import xml.etree.ElementTree as ET
import os.path
#test = moneylover_parser('C:/Users/flavi/Downloads/test.mlx')
#test.simplifyMXL('C:/Users/flavi/Downloads/test')
class moneylover_parser:

    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            print('Error: file doesn\'t exists')
            return
        extension = os.path.splitext(file_path)
        if extension[1] != '.mlx':
            print('Error: wrong file extension')
            return

        self.file_path = file_path
        self.destination_path = os.path.split(self.file_path)[0] + '/extracted_mxl/'
        
        root = ET.parse(self.file_path)
        self.first_node = root.getroot()

        print('File imported')        

    def extraxtAll(self, destination_path = None):
        
        if destination_path != None:
            self.destination_path = destination_path if destination_path[-1:] == '/' else destination_path + '/'
        else:
            self.destination_path = os.path.split(self.file_path)[0] + '/extracted_mxl/'

        for table_node in self.first_node:
            if table_node.tag == 'table':
                self.extractTable(table_node.attrib['name'])

        return True

    def extractTable(self, table_name):
        if not self.destination_path:
            print('Error: no destination path given')
            return False

        if not table_name:
            print('Error: no table name given')
            return False

        find_node = self.first_node.findall('.//table[@name="' + table_name + '"]')
        table_index = self.first_node.getchildren().index(find_node[0])
        table_node = self.first_node[table_index]

        if not len(list(table_node)):
            print('Warning: no rows found for table node named: ' + table_name)
            return False

        if not os.path.exists(self.destination_path):
            os.makedirs(self.destination_path)

        output_file = open(self.destination_path + table_name + '.csv', 'w', encoding='utf-8')
        
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
