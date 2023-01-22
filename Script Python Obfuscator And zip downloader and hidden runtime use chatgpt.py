#Script Python Obfuscator And zip downloader and hidden runtime use chatgpt

#Step 1: Download the Python Obfuscator from the official website.

import urllib.request
url = 'https://pypi.org/project/obfuscator/' 
urllib.request.urlretrieve(url, 'Python_Obfuscator.zip')

#Step 2: Unzip the file and install the Python Obfuscator

import zipfile
zip_ref = zipfile.ZipFile('Python_Obfuscator.zip', 'r')
zip_ref.extractall()
zip_ref.close()

import os
os.system('python Python_Obfuscator/setup.py install')

#Step 3: Create the script to be obfuscated.

script = """
def add_two_numbers(a, b):
  return a + b

def main():
  x = 5
  y = 7
  print(add_two_numbers(x, y))

if __name__ == '__main__':
  main()
"""
 
#Step 4: Obfuscate the script

from obfuscator import Obfuscator
obfuscated_script = Obfuscator().obfuscate(script)

#Step 5: Download the obfuscated script as an anonymous file with hidden runtime

import tempfile

with tempfile.NamedTemporaryFile(mode='w+b', suffix='.py', delete=False) as f:
  f.write(obfuscated_script.encode('utf-8'))
  f.flush()
  os.system('pyinstaller --onefile --noconsole --hidden-import=obfuscator {}'.format(f.name))

#Step 6: Cleanup

os.remove(f.name)
os.remove('Python_Obfuscator.zip')
