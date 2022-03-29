import pandas as pd
from collections import defaultdict
pd.set_option("display.max_rows", None, "display.max_columns", None)


def plate():
    print("""1.	Display spreadsheet in dictionary format
2.	Remove line feed and excessive space charactersS
3.	Change text case (for all columns)
4.	Change text case for a specified column
5.	Check for duplicated rows
6.	Delete a row
7.	Delete a column
8.	Update a cell
9.	Sort rows by column value
10.	Check (and optionally change) column value(s)
11.	Save cleaned data to CSV file
12.	Quit""")


def function_1():
    count_f1 = 1
    dd = defaultdict(list)
    print_list = df.to_dict('records', into=dd)
    for items in print_list:
        print(f"{count_f1} : {items}")
        count_f1 = count_f1 +1


def function_2():
    name_list = df.columns.values.tolist()
    space=' '

    for name in name_list:
        df[name] = df[name].str.strip()
        df[name] = df[name].str.split()
        df[name] = df[name].str.join(space)

    function_1()

def function_3():
    print("""1.Title case
2. lower case
3.UPPER CASE
4.Sentence Case
""")


    while True:
        try:
            function = input('Enter the number corresponding to the case change required:')

            function = int(function)
            name_list = df.columns.values.tolist()

            for name in name_list:

                if function == 1:
                    df[name] = df[name].str.title()


                if function == 2:
                    df[name] = df[name].str.lower()

                if function == 3:
                    df[name] = df[name].str.upper()

                if function == 4:
                    df[name] = df[name].str.capitalize()



            function_1()
            break


        except:
            print('invalid/error input,please enter again')



def function_4():
    print("""1.Title case
2. lower case
3.UPPER CASE
4.Sentence Case
""")
    name_list = df.columns.values.tolist()
    print(name_list)

    while True:
        try:
            name = input('Enter column name for case change')  # you request name
            function = int(input('Enter the number corresponding to the case change required:'))

            if function == 1:
                df[name] = df[name].str.title()

            if function == 2:
                df[name] = df[name].str.lower()

            if function == 3:
                df[name] = df[name].str.upper()

            if function == 4:
                df[name] = df[name].str.capitalize()

            function_1()

            break

        except:
            print('invalid/error input(s),please enter again')


def function_5():
    count = []
    for index, row in df.iterrows():
        for new_index, new_row in df.iterrows():
            if index!=new_index and row.equals(new_row) and index not in count and new_index not in count:
               print(f"{index} and {new_index} are same")
               count.append(index)
               count.append(new_index)

def function_6():
    function_1()

    while True:
        try:
            row_to_delete = int(input('Enter the number of the row to delete:'))
            dd = defaultdict(list)
            print_list = df.to_dict('records', into=dd)
            print(print_list[row_to_delete-1])

            confirm = input('Confirm to delete the following row ("y" for yes otherwise for no)')

            if confirm == 'y':
                df.drop([row_to_delete], inplace=True)
                print(f"Row {row_to_delete} has been remove")
                function_1()
                break

            else:
                return  # don't know it work or not

        except:
            print('invalid/error input(s),please enter again')


def function_7():
    while True:
        try:
            function_1()
            column_delete = input('Enter to name of column to delete:')
            confirm = input('Confirm to delete the mentioned column ("y" for yes otherwise for no)')
            col_one_list = df[column_delete].tolist()

            if confirm == 'y':
                for items in col_one_list:
                    print(f"{items} has been deleted")
                df.drop([column_delete], axis=1, inplace=True)
                function_1()
                break

            else:
                return

        except:
            print('invalid/error input(s),please enter again')


def function_8():
    while True:
        try:
            name_list = df.columns.values.tolist()
            row_to_update = int(input('Enter the number of row to update:'))
            dd = defaultdict(list)
            print_list = df.to_dict('records', into=dd)
            print(print_list[row_to_update-1])
            coloumn_to_update = input('Enter the name of column to update:')

            while coloumn_to_update not in name_list:
                print('Please enter vaild column name:')
                coloumn_to_update = input('Enter the name of column to update:')

            new_cell_value = input('Enter new cell value')
            print(
                f"the cell velue of row {row_to_update} is going to updated from {df.at[row_to_update, coloumn_to_update]} to {new_cell_value}")

            comfirm = input('Confirm to delete the mentioned cell ("y" for yes otherwise for no)')

            if comfirm == 'y':
                df.at[row_to_update, coloumn_to_update] = new_cell_value  ######## modify
                function_1()
                break

        except:
            print('invalid/error input(s),please enter again')



def function_9():
    name_list_1 = df.columns.values.tolist()
    print(name_list_1)
    coloumn_to_sort = input('Enter the name of column to sort the list:')

    while coloumn_to_sort not in name_list_1:
        print('Please enter valid column name:')
        coloumn_to_sort = input('Enter the name of column to update:')

    df.sort_values(by=[coloumn_to_sort],inplace=True)
    function_1()


def function_10():
    name_list_1 = df.columns.values.tolist()
    print(name_list_1)

    while True:
        try:
            input_name = input('Enter the name of column to display:')  # column name
            print(df[input_name].value_counts())  # can't be shown properly
            break

        except:
            print('Please enter valid column to display')


    need_some_change = input('Need more change? ("y" for yes otherwise for no)')

    while True:
        try:
            while need_some_change == 'y':
                which_want_change_value = input('Enter the value in the column to change')
                change_value = input('Enter the new value:')

                list_of_index = df.index[df[input_name] == which_want_change_value].tolist()

                for index in list_of_index:
                    df.at[index, input_name] = change_value

                print(df[input_name].value_counts())
                need_some_change = input('Need more change? ("y" for yes otherwise for no)')

            break

        except:
            print('invalid/error input(s),please enter again')



def function_11():
    while True:
        try:
            create_name = input('Enter Name of CSV file to create')
            location_for_save = input('Enter location for saving this document:')
            df.to_csv(f"{location_for_save}\{create_name}.csv", index=False)
            print('Save successfully')
            break


        except:
            print('incorrect/invalid location, please enter again')


########################################################################CSV open and loop part#################################################################################
while True:
  try:
    address = input('file location:')
    df = pd.read_csv(address)
    df.index = df.index + 1
    break

  except:
    print('Please enter correct location')


plate()
while True:
    try:
        excute_function = int(input('Enter number to choose function to execute:'))
        break

    except:
        print('incorrect/invalid location, please enter again')



while excute_function != 12:

    if excute_function == 1:
        function_1()

    if excute_function == 2:
        function_2()

    if excute_function == 3:
        function_3()

    if excute_function == 4:
        function_4()

    if excute_function == 5:
        function_5()

    if excute_function == 6:
        function_6()

    if excute_function == 7:
        function_7()

    if excute_function == 8:
        function_8()

    if excute_function == 9:
        function_9()

    if excute_function == 10:
        function_10()

    if excute_function == 11:
        function_11()

    plate()

    while True:
        try:
            excute_function = int(input('Enter number to choose function to execute :'))
            break

        except:
            print('incorrect/invalid location, please enter again')

if excute_function == 12:
    exit()