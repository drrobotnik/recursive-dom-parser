import argparse
import fnmatch
import os
import sys
from bs4 import BeautifulSoup

matches = []
elements = {}

parser = argparse.ArgumentParser(description='scrape files and parse doms')

parser.add_argument('--path', help='path of files')
parser.add_argument('--element', help='dom element type')

args = parser.parse_args()

for root, dirnames, filenames in os.walk(args.path):
    for filename in fnmatch.filter(filenames, '*.html'):
        matches.append(os.path.join(root, filename))

def walker(soup):
    if soup.name is not None:
        for child in soup.children:
            childName = str(child.name)
            if childName != 'None':
                if childName not in elements:
                    elements[childName] = [child]
                else:
                    elements[childName].append(child)
                walker(child)

for file in matches:
    data = open(file)
    soup = BeautifulSoup(data, 'lxml')
    walker(soup)

storelen = len(elements[args.element])
nodupes = list(set(elements[args.element]))

sorted = sorted(nodupes, key=len)

for element in sorted:
    print element

