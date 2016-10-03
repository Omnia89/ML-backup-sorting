import xml.etree.ElementTree as ET
import os.path


def simplifyMXL(mxl_file, destination_path):
    if not os.path.isfile(mxl_file):
        print('Error: file doesn\'t exists')
        return False
    extension = os.path.splitext(mxl_file)
    if extension != '.mxl':
        print('Error: wrong file extension')
        return False

    root = ET.parse(mxl_file)
    first_node = root.getroot()
    
    for table_node in first_node:
        if table_node.tag = 'table':
            pass

    return True

def extractTable(table_node, detination_path):
    if not table_node[0][0].tag = 'row':
        print('Warning: no rows found for table node named: ' + table_node.attrib['name'])
        return False

    #stringa per la riga

    #primo ciclo per i nomi colonna

    #ciclo tutto

    return True