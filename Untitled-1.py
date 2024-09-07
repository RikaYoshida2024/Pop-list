def cuspop(my_list):
    if len(my_list) == 0:
        return None
    last_element=my_list[-1]
    my_list=my_list[:-1]
    return last_element,my_list

my_list = [1, 2, 3, 4, 5]
popped_element,updated_list = cuspop(my_list)
print(f"Popped element: {popped_element}")
print(f"Updated list: {updated_list}")