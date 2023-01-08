import glob
from pathlib import Path
import os
import xml.etree.ElementTree as ET
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        for patches in glob.glob(sys.argv[1], recursive=True):
            with open(patches, 'r') as fr:
                string_data = fr.read()
                root = ET.fromstring(string_data)
                ID = root.findall('TitleID/ID')
                for i in ID:
                    out = ('output/xml/{}.xml'.format(i.text))
                    print(out)
                    with open(out, 'w') as fw:
                        fw.write(f'{string_data}')
    else:
        print('path to glob not provided')
