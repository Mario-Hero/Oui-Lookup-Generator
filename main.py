#!/usr/bin/python
# -- coding: utf-8 --**
import os.path
import sys
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests


INSERT_CODE_SYMBOL = '***insert_point***'
IEEE_URL = 'http://standards-oui.ieee.org/oui/oui.txt'
OUI_TXT_PATH = './oui.txt'
OUTPUT_FOLDER = 'output/'

def download_oui():
    print('downloading')
    response = requests.get(IEEE_URL)
    if response.status_code == 200:
        print('writing')
        with open(OUI_TXT_PATH, 'wb') as oui:
            oui.write(response.content)
    else:
        print('download failed')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the language you need to generate,")
        print("support: cpp, rust")
        sys.exit(1)
    language = sys.argv[1].strip().lower()
    if not os.path.exists(OUI_TXT_PATH):
        download_oui()
    oui_data = dict()
    with open(OUI_TXT_PATH, 'r') as f:
        f.readline()
        f.readline()
        f.readline()
        line = f.readline()
        while line:
            if not line.startswith('	') and line.strip() and line[2] != '-':
                line = line.strip()
                data = line.split('	')
                mac = data[0][0:6]
                # mac = int(data[0][0:6], 16)
                compony = data[-1].strip()
                # print(mac)
                # print(compony)
                oui_data[mac] = compony
            line = f.readline()
    '''
    for mac, compony in oui_data.items():
        print(mac, compony)'''
    template_file = ''
    output_file = ''
    insert_code = ''
    output_folder_2 = ''
    if language == 'cpp' or language == 'c++':
        template_file = 'template.cpp'
        output_file = 'output.cpp'
        output_folder_2 = 'cpp/'
        for mac, compony in oui_data.items():
            mac_digit = int(mac, 16)
            insert_code += f'		case {mac_digit}: return \"{compony}\";\n'
        # insert_code = insert_code[:-2]
        # insert_code += "\n"
    elif language == 'rust':
        template_file = 'template.rs'
        output_file = 'output.rs'
        output_folder_2 = 'rust/'
        for mac, compony in oui_data.items():
            insert_code += f'    \"{mac}\" => \"{compony}\",\n'
    if not os.path.exists(OUTPUT_FOLDER):
        os.mkdir(OUTPUT_FOLDER)
    if not os.path.exists(OUTPUT_FOLDER + output_folder_2):
        os.mkdir(OUTPUT_FOLDER + output_folder_2)
    with open(template_file, 'r') as template:
        with open(OUTPUT_FOLDER + output_folder_2 + output_file, 'w') as output:
            line = template.readline()
            inserting = False
            while line:
                if line.strip().endswith(INSERT_CODE_SYMBOL):
                    output.write(insert_code)
                    line2 = template.readline()
                    while line2:
                        if line2.strip().endswith(INSERT_CODE_SYMBOL):
                            break
                        line2 = template.readline()
                else:
                    output.write(line)
                line = template.readline()
