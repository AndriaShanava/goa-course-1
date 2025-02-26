def int_list_to_string(int_list):

str_list = [str(num) for num in int_list]
    

return " ".join(str_list)


numbers = [1, 2, 3, 4, 5]
result = int_list_to_string(numbers)
print(result)  # Output: "1 2 3 4 5"