# Truecaller-Python-Tools
Get phone number owner name from truecaller with python
This is a Python script to search phone numbers on Truecaller using the truecallerpy module. Before running the script, make sure that you have installed colorama and truecallerpy modules.

Installation
To install the required modules, run the following command in your terminal:
```sh
pip3 install colorama truecallerpy
```

Usage
1. On Truecaller Android, tap on the 3 line menu on top left then click on setting's.
2. Tap on Privacy Center and then click on Download my data.
3. Now a JSON file is downloaded.
4. Save the JSON file in the same directory as the script and rename it to truecaller.json.
5. Add phone numbers to search in a file named phone.txt. One phone number per line.
6. Run the script using the following command:
```sh
python3 truecaller-scraping.py
```
