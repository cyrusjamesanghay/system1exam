#array
data_list = []

# Define functions para sa main menu sir
def show_all_data():
    if data_list:
        print("Current Data:")
        for index, data in enumerate(data_list, start=1):
            #Ang f nga imong nakita sa print statement, nga mag-una sa string, kay usa ka f-string (formatted string literal), usa ka feature nga gipaila sa Python 3.6. Ang f-string nagpasabot nga ang string nga gisulat sa sulod sa f"..." syntax mag-allow sa expression evaluation ug variable substitution.
            print(f"{index}. {data}")
    else:
        print("No data available.")

def add_single_data():
    item = input("Enter data to add: ")
    data_list.append(item)
    print("Data added successfully.")

def add_multiple_data():
    #Ang split() maghimo og split base sa usa ka separator o delimiter nga imong ispecify, o kung wala, mag-split siya sa default nga whitespace (mga espasyo, tabs, ug newlines)
    items = input("Enter multiple data separated by commas: ").split(',')
    for item in items:
        data_list.append(item)
    print("Multiple data items added successfully.")

def delete_data():
    show_all_data()
    try:
        index = int(input("Enter the index of data to delete: ")) - 1 
        if 0 <= index < len(data_list):
            data_list.pop(index)
            print("Data deleted successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")
#nag gamit mea ug clear kay if e delete sa user iyahang data mawala sya hehe
def delete_all_data():
    data_list.clear()
    print("All data deleted successfully.")

def update_data():
    show_all_data()
    try:
        #(-1)gigamit sya aron i-adjust ang input nga gihatag sa user kay sa kasagara (o arrays) magsugod sa index 0 (zero-based indexing).
        index = int(input("Enter the index of data to update: ")) - 1
        if 0 <= index < len(data_list):
            new_data = input("Enter new data: ")
            data_list[index] = new_data
            print("Data updated successfully.")
        else:
            print("Invalid index.")
    #ang except sir is ginagamit sa error handling o pag-handle sa mga exceptions.        
    except ValueError:
        print("Invalid input. Please enter a number.")

# para ma balik ang main menu hantud mag exit ang user
def main_menu():
    #Ang purpose aning while ug true sir is mura syag loop btaw sir kay mag balik2 raman sya sa menu sir
    while True:
        print("Menu")
        print("Press [1] SHOW ALL DATA")
        print("Press [2] ADD SINGLE DATA")
        print("Press [3] ADD MULTIPLE DATA")
        print("Press [4] DELETE")
        print("Press [5] DELETE ALL DATA")
        print("Press [6] UPDATE DATA")
        print("Press [0] EXIT")
        
        choice = input("Enter your choice: ")
        
        #nag gamit mea ug match-case para sa main menu
        match choice:
            case '1':
                show_all_data()
            case '2':
                add_single_data()
            case '3':
                add_multiple_data()
            case '4':
                delete_data()
            case '5':
                delete_all_data()
            case '6':
                update_data()
            case '0':
                print("Exit the program.")
                break
            case _:
                print("Invalid choice. Please select a valid option.")

# para mo run na among ge buhat sir hihi
main_menu()