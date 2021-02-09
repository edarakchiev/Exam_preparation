def list_manipulator(*args):
    num_list = args[0]
    first_command = args[1]
    second_command = args[2]
    parameter = args[3:]
    if first_command == "add":
        if second_command == "beginning":
            parameter = reversed(parameter)
            for el in parameter:
                num_list.insert(0, el)
            return num_list
        elif second_command == "end":
            for el in parameter:
                num_list.append(el)
            return num_list

    elif first_command == "remove":
        if second_command == "beginning":
            if parameter:
                num = int(parameter[0])
                num_list = num_list[num:]
                return num_list
            else:
                num_list = num_list[1:]
                return num_list

        elif second_command == "end":
            if parameter:
                num = int(parameter[0])
                num_list = num_list[:-num]
                return num_list
            else:
                num_list = num_list[:-1]
                return num_list







print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))