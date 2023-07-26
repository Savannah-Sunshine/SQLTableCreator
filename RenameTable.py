import platform
import subprocess

def copy_to_clipboard(text):
    system = platform.system()
    if system == "Windows": # WINDOWS
        subprocess.run(['clip'], input=text.strip().encode('utf-16'), check=True)
    elif system == "Darwin": # MAC
        subprocess.run(['pbcopy'], input=text.strip().encode('utf-8'), check=True)
    else:
        raise NotImplementedError("Clipboard not supported on this platform.")


def getInputList(list):
    inputList = input().upper()
    if inputList == '':
        return list
    list.append(inputList.replace('_LOG',''))
    return getInputList(list)


#######################################################################################



# Create alter schema statement
output_alter_schema = "ALTER SESSION SET CURRENT_SCHEMA = WDAY_PREP; \n\n"






# Input all columns w/ datatypes, ignore any that begin with MSA
print("\nPlease enter all table names to change.")
print("Enter an empty line to finish writing.")
table_name_list = getInputList([])


output_rename_tables = ''
for table_name in table_name_list:
    output_rename_tables += 'ALTER TABLE ' + table_name + '_LOG\n' \
                            'RENAME TO LOG_' + table_name + ';\n\n'

# Print
print('\033[1;37m' + 'Your SQL statements:' + '\033[1;36m')
print('\033[1;36m' + output_alter_schema + output_rename_tables)

# Save to clipboard
print('\033[1;34mText copied to clipboard\033[0m')
copy_to_clipboard(output_alter_schema + output_rename_tables)
