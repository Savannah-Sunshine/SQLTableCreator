# Table Writer for Granite
A python script to write an E2E and log table in SQL

### How to download
1. Using the green Code button in github, download ZIP
2. Unzip that file in any desired directory
3. Navigate using cd to the tableWriter.py file using a command-line interface (CLIs include Terminal, Powershell, etc)

### How to run
Run the following command in a terminal.

`python TableCreator.py`

You may have to replace the python command with python3.

Include `-nopk` as an argument if you don't want to create a **p**rimary **k**ey index for the E2E table: `python TableCreator.py -nopk`

### Output
It will paste a SQL query for the E2E and log tables to the console and **in your clipboard.**