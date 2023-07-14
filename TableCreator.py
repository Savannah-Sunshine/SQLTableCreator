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
    if inputString != '':
        return getInputString()
    return inputString

def getInputList(column_list):
    inputList = input().upper()
    if inputList == '':
        return column_list
    if not inputList.startswith('MSA') : # Else, skip row
        column_list.append(inputList)
    return getInputList(column_list)

#######################################################################################



print("\033[1;34mPlease enter the table name")
print("Table Name example: C09_CUSTOMER_PHONE")

table_name = getInputString()




# Input all columns w/ datatypes, ignore any that begin with MSA
print("\nPlease enter the column names and datatype. You may include the items that begin with \'MSA\' \nExample: COUNTRY_CODE    VARCHAR2(254 BYTE)")
print("Enter an empty line to finish writing.")

column_list = getInputList([])


# Write all columns for tables
allData = ''
allData_Old = ''
for c in column_list:
    allData += ',\n   ' + c
    allData_Old += ',\n   OLD_' + c
    if 'VARCHAR2' in c:
        allData += ' NOT NULL'


# Write primary key index for the E2E table
pk_index = ''
# if len(sys.argv) == 1 or sys.argv[1].upper() != '-NOPK':
#     print("Please enter all primary key columns, type H for help, C for clear, or enter once you are done.")
#     key_list = getInputList([])
#     for k in column_list:
#
#     pk_index = 'CREATE INDEX ' + table_name + '_E2E_PK ON ' + table_name + '_E2E('+ pk_index + ');'


# Write SQL for tables
output_E2E_table = 'alter session set CURRENT_SCHEMA = WDAY_E2E; \n' \
                  'CREATE TABLE ' + table_name + '_E2E  \n(' \
                       '\n   MSA_ID NUMBER(*,0) \tGENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 ' \
                       '\n                      \tINCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE  NOT NULL,' \
                       '\n   MSA_UPDATED_DT \tTIMESTAMP(6) NOT NULL,' \
                       '\n   MSA_ACTIVE_FLAG \tVARCHAR2(1 BYTE) NOT NULL' \
                       +     allData + '\n);\n' \
                  'CREATE INDEX ' + table_name + '_E2E_SYN ON ' + table_name + '_E2E("MSA_ID");\n' + pk_index + '\n\n'

output_LOG_table = 'CREATE TABLE ' + table_name + '_LOG  \n(' \
                       '\n   MSA_ID NUMBER(*,0) \tGENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 ' \
                       '\n                      \tINCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE  NOT NULL,' \
                       '\n   MSA_LOG_DATE \tTIMESTAMP(6) NOT NULL,' \
                       '\n   MSA_ACTION \t\tVARCHAR2(1 BYTE) NOT NULL,' \
                       '\n   OLD_MSA_ACTIVE_FLAG \tVARCHAR2(1 BYTE)' \
                       +     allData_Old + ',' \
                       '\n   MSA_ACTIVE_FLAG \tVARCHAR2(1 BYTE) NOT NULL'  \
                       + allData + '\n);\n\n' \
                   'CREATE INDEX ' + table_name + '_LOG_SYN ON ' + table_name + '_LOG("MSA_ID"); \n commit;'



# print out to console
print('\033[0m' + 'Your SQL statements:' + '\033[1;36m')
print(output_E2E_table + output_LOG_table)


# copy to clipboard
print('\033[1;34mText copied to clipboard')
copy_to_clipboard(output_E2E_table + output_LOG_table)