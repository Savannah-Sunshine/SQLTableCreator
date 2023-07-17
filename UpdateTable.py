import platform
import subprocess
import sys

def copy_to_clipboard(text):
    system = platform.system()
    if system == "Windows": # WINDOWS
        subprocess.run(['clip'], input=text.strip().encode('utf-16'), check=True)
    elif system == "Darwin": # MAC
        subprocess.run(['pbcopy'], input=text.strip().encode('utf-8'), check=True)
    else:
        raise NotImplementedError("Clipboard not supported on this platform.")

def getInputString():
    inputString = input().upper()
    if inputString == '':
        return getInputString()
    return inputString

def getInputList_Column(column_list):
    inputList = input().upper()
    if inputList == '':
        return column_list
    if not inputList.startswith('MSA') : # Else, skip row
        column_list.append(inputList)
    return getInputList_Column(column_list)

def getInputList_SQL(column_list):
    inp = input().upper()
    if inp == '':
        return column_list
    if not inp.startswith('MSA') : # Else, skip row
        inp = inp.replace('ENABLE','').replace('"','').replace('NOT NULL','').replace(',','').strip()
        column_list.append(inp)
    return getInputList_SQL(column_list)

#######################################################################################

# Make sure arguments exist
if len(sys.argv) == 1 :
    print("\033[1;34mPlease include either -sql or -column as an argument. Refer back to the readme for more help.\n")
    exit()

# Get table name
print("\033[1;34mPlease enter the table name")
print("Table Name example: C09_CUSTOMER_PHONE")
table_name = getInputString()



# Create add new column statement
output_add_column = "ALTER SESSION SET CURRENT_SCHEMA = WDAY_PREP; \n\n" \
              'ALTER TABLE ' + table_name + ' ADD msa_active_flag varchar2(1);             \n\n'






# Input all columns w/ datatypes, ignore any that begin with MSA
print("\nPlease enter the column names and datatype. You may include the items that begin with \'MSA\'")
column_list = []
if sys.argv[1].upper() == '-SQL': # when entering sql statements
    print("Example: \"WORKER_ID\" VARCHAR2(254 BYTE) NOT NULL ENABLE,  ")
    print("Enter an empty line to finish writing.")
    column_list = getInputList_SQL([])
else: #when entering columns
    print("\nExample: COUNTRY_CODE    VARCHAR2(254 BYTE)")
    print("Enter an empty line to finish writing.")
    column_list = getInputList_Column([])


# Create all columns for log table
allData = ''
allData_Old = ''
for c in column_list:
    allData += ',\n   ' + c
    allData_Old += ',\n   OLD_' + c
    if 'VARCHAR2' in c:
        allData += ' NOT NULL'


# Create new log table
output_LOG_table = 'CREATE TABLE ' + table_name + '_LOG  \n(' \
                       '\n   MSA_ID NUMBER(*,0) \tGENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 ' \
                       '\n                      \tINCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE  NOT NULL,' \
                       '\n   MSA_LOG_DATE \tTIMESTAMP(6) NOT NULL,' \
                       '\n   MSA_ACTION \t\tVARCHAR2(1 BYTE) NOT NULL,' \
                       '\n   OLD_MSA_ACTIVE_FLAG \tVARCHAR2(1 BYTE)' \
                       +     allData_Old + ',' \
                       '\n   MSA_ACTIVE_FLAG \tVARCHAR2(1 BYTE) NOT NULL'  \
                       +     allData + '\n);\n\n' \
                   '\nCREATE INDEX ' + table_name + '_LOG_SYN ON ' + table_name + '_LOG("MSA_ID"); \n\ncommit;'


# Print
print('\033[1;37m' + 'Your SQL statements:' + '\033[1;36m')
print('\033[1;36m' + output_add_column + output_LOG_table)

# Save to clipboard
print('\033[1;34mText copied to clipboard\033[0m')
copy_to_clipboard(output_add_column + output_LOG_table)
