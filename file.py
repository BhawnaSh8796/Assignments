
import os
import datetime

def modified_time_of_file():

    file_name = input("Enter the file name ")
    if os.path.exists(file_name):

        last_modi_time = os.path.getmtime(file_name)
        creation_time = os.path.getctime(file_name)

        m_time = datetime.datetime.fromtimestamp(last_modi_time)
        print(m_time)

        c_time = datetime.datetime.fromtimestamp(creation_time)
        print(c_time)

    else:
        print("File does not exists {}".format(file_name))


def print_student_details():

    file_name = input("Enter file name: ")
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            # Reading all lines from file
            for lines in file:
                lines = lines.rstrip()

                if file_name == 'student_comma.dat':
                    # Spliting the lines by comma
                    word_list = lines.split(',')
                elif file_name == 'student_double_semi.dat':
                    # Spliting the lines by double semi colon
                    word_list = lines.split(';;')
                else:
                    # Spliting the lines by semi colon
                    word_list = lines.split(';')
                print(word_list[0] + " " + word_list[1])
    else:
        print("File name {} not found".format(file_name))

def print_file_details():

    file_name = input("Enter the file name ")
    num_line = 0

    if os.path.exists(file_name):

        print('File Name is: ' + file_name)
        file_size = os.path.getsize(file_name)
        print("File size is: ", file_size, " bytes")
        get_time = os.path.getmtime(file_name)
        mod_time = datetime.datetime.fromtimestamp(get_time)
        print("Modified time is: ", mod_time)
        with open(file_name, 'r') as file:
            for line in file:
                num_line = num_line + 1

        file_open = open(file_name, 'r')
        data = file_open.read()
        no_of_char = len(data)
        file_open.close()

        print("Number of lines: ", num_line)
        print("Number of characters: ", no_of_char)

def main():

    # 1. Convert each modified time to normal datetime. clue - use module datetime
    modified_time_of_file()

    # 2. Print Student data from all three files - student_comma.dat, student_double_semi.dat and student_semi.dat
    print_student_details()

    # 3. Print file properties of program
    # File name
    # No of lines
    # No of characters
    # File size
    # Most recent modification time
    print_file_details()

if __name__ == '__main__':
    main()






