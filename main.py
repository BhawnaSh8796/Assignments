import functions

def main():

    #print financial year
    year = int(input("Please enter year "))
    month = int(input("Please enter month "))
    functions.printfinancialyear(year, month)

    #append even list with prime list
    prime_num = [2, 3, 5]
    even_num = [4, 6, 8]
    functions.append_prime_even(prime_num, even_num)

    # 1.Find largest/second largest /Smallest
    # [1,3,5,8]
    num_list = [1, 3, 5, 8]
    functions.find_larg_secLarg_small(num_list)

    # 2.list1= [1,2,1,1,4,5 ] .
    # Remove 2nd occurrence of 1 using pop
    list1 = [1,2,1,1,4,5 ]
    pop_num = 1
    occur_num = 2
    functions.remove_sec_occur(list1, pop_num, occur_num)

    # 3. list1 = [1, 4, 10, 30, 60, 70, 80 , 100]
    # delete_index_list = [3, 7, 4] .
    # Delete using pop
    list1 = [1, 4, 10, 30, 60, 7, 70, 80, 100, 3]
    delete_index_list = [3, 7, 4, 70]
    functions.del_val_list(list1, delete_index_list)

    #4. print reverse of a string
    string_var = "Hello"
    rev_string_val = functions.rev_string(string_var)
    print(rev_string_val)

    #5. print true if reverse string have more than two vowels else false
    functions.is_two_vowels(rev_string_val)

    #6. #Print all the numbers which are divisible by 7
    num_list = [1,7,14,21,22,34]
    functions.divisible_of_seven(num_list)

    #7. Change odd characters to uppercase and even to lowercase in a string.
    _my_string_ = "jktechtraining"
    functions.fun_upp_lower(_my_string_)


if __name__ == '__main__':
    main()



