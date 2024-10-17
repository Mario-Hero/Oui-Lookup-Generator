#!/usr/bin/python
# -- coding: utf-8 --**
import os.path
import sys
import requests


INSERT_CODE_SYMBOL = '***insert_point***'
IEEE_URL = 'https://standards-oui.ieee.org/oui/oui.txt'
SAVE_PATH = './oui.txt'
OUTPUT_FOLDER = './output/'

def download_oui():
    print('downloading')
    response = requests.get(IEEE_URL)
    if response.status_code == 200:
        print('writing')
        with open(SAVE_PATH, 'wb') as oui:
            oui.write(response.content)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the language you need to generate,")
        print("such as cpp, rust, python")
        sys.exit(1)
    language = sys.argv[1].strip().lower()
    if not os.path.exists(SAVE_PATH):
        download_oui()
    oui_data = dict()
    with open(SAVE_PATH, 'r') as f:
        f.readline()
        f.readline()
        f.readline()
        line = f.readline()
        while line:
            if not line.startswith('	') and line.strip() and line[2] != '-':
                line = line.strip()
                data = line.split('	')
                mac = int(data[0][0:6], 16)
                compony = data[-1].strip()
                # print(mac)
                # print(compony)
                oui_data[mac] = compony
            line = f.readline()
    for mac, compony in oui_data.items():
        print(mac, compony)
    template_file = ''
    output_file = ''
    insert_code = ''
    if language == 'cpp' or language == 'c++':
        template_file = 'template.cpp'
        output_file = 'output.cpp'
        insert_code = '   std::unordered_map<int, std::string> oui_data;\n'
        for mac, compony in oui_data.items():
            insert_code += f'   oui_data[{mac}] = \"{compony}\";\n'
    elif language == 'rust':
        template_file = 'template.rs'
        output_file = 'output.rs'
        insert_code = '    let mut oui_data = HashMap::new();\n'
        for mac, compony in oui_data.items():
            insert_code += f'    oui_data.insert({mac}, \"{compony}\".to_string());\n'
    if not os.path.exists(OUTPUT_FOLDER):
        os.mkdir(OUTPUT_FOLDER)
    with open(template_file, 'r') as template:
        with open(OUTPUT_FOLDER + output_file, 'w') as output:
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
