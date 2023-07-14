# Table Writer for Prj Granite
A python script to write an E2E and log table in SQL

## How to download
1. Using the green Code button in github, download ZIP
2. Unzip that file in any desired directory
3. Navigate using cd to the tableWriter.py file using a command-line interface (CLIs include Terminal, Powershell, etc)

## How to run
Run the following command in a terminal.

`python TableCreator.py` or `python TableCreator.py -nopk`

###### You may have to replace python with python3.

The `-nopk` argument will turn off creating the **p**rimary **k**ey index for the E2E table.

## Output
The script will a SQL query for the E2E and log tables. It will print to the console and **save in your clipboard.**