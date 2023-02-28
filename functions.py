def printfinancialyear(year, month):

    if month >= 4 and month <= 12:
        print("The financial year is " + str(year))
    elif month >= 1 and month <= 3:
        print("The financial year is " + str(year - 1))
    else:
        print("Incorrect month")


def append_prime_even(prime_num, even_num):

    for each_element in even_num:
        prime_num.append(each_element)

    print(prime_num)



def find_larg_secLarg_small(num_list):

    num_list.sort()
    print("Largest number is " + str(num_list[-1]))
    print("Second largest number is " + str(num_list[-2]))
    print("Smallest number is " + str(num_list[0]))


def remove_sec_occur(list1, pop_num, occur_num):
    i = 0
    list2 = []

    for number in list1:
        if number == pop_num:
            i = i + 1
            if i != occur_num:
                list2.append(number)
        else:
            list2.append(number)

    print(list2)

def del_val_list(num_list, delete_index_list):

    for del_num in delete_index_list:
        if del_num in num_list:
            index_value = num_list.index(del_num)
            num_list.pop(index_value)

    print(num_list)

def rev_string(string_var):

    rev_string = string_var[::-1]
    return rev_string

def is_two_vowels(passed_rev_val):

    vowels = ["a" ,"e" ,"i" ,"o" ,"u"]
    found_vowels = []

    for alphabet in passed_rev_val:
        if alphabet in vowels:
            found_vowels.append(alphabet)

    if len(found_vowels) >= 2:
        print(found_vowels)
        print("True")
    else:
        print("False")


def divisible_of_seven(num_list):

    for number in num_list:
        if (number % 7) == 0:
            print(number)

def fun_upp_lower(passed_string):

    final_string = ""
    for i in range(len(passed_string)):
        if i % 2 == 0:
            final_string = final_string + passed_string[i].upper()
        else:
            final_string = final_string + passed_string[i].lower()

    print(final_string)









