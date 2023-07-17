# Table Writer for Prj Granite
A python script to write an E2E and log table in SQL

## How to download
1. Using the green Code button in github, download ZIP
2. Unzip that file in any desired directory
3. Navigate to the UpdateTable.py file using a command-line interface (CLIs like Terminal, Powershell, Command Prompt, or an IDE's terminal)

## How to run UpdateTable
Run the following command.

`python UpdateTable.py -sql` or `python UpdateTable.py -columns`
###### You may have to replace python with python3.

### Arguments:
- `-sql` Input data by copying columns from the auto-generated table. You can copy the MSA columns, but they will be ignored.

![img.png](/images/img.png)
- `-columns` Program's default behaviour. Input data using sql developer's columns, copying both lines. Some terminals will not put spaces between columns, breaking this program.

![img_1.png](/images/img_1.png)

## Output
The script will write a SQL query. It will print to the console and **save in your clipboard.**

<details>
  <summary>SQL Table Creater</summary>

## How to run TableCreator
`python TableCreator.py` or `python TableCreator.py -nopk`

The `-nopk` argument will turn off creating the **p**rimary **k**ey index for the E2E table.
</details>