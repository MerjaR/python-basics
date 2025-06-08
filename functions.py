#Calling a function in function
def execute_many_times(my_function, n: int):
    i =1
    while i <= n:
        my_function()
        i +=1

def check_list(check_function, my_list: list):
    check = False
    j = 0
    for j in range(0, len(my_list)):
        if check_function(my_list[j]):
            check = True
        else:
            check = False
            return check
    
    return check


