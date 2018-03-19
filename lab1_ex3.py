# EXERCISE 3 TOOdo LIST (OPTIONAL)
# Given a list of tasks (i.e., actions that the user wants to do in the future)
# implement a todo_manager program to perform four actions:
# 1. insert a new task (a string of text);
# 2. remove a task (by typing its content, exactly);
# 3. show all existing tasks;
# 4. close the program.
# At startup, the program shows a menu with the 4 options and, for each choice, performs
# the requested action. After the action (except action 4), the program returns to the
# prompt for actions.

end = False
print("Hi I'm your todo_manager program")
list = []
while end == False :
    print("Please insert the number corresponding to the action you want to perform:")
    print(" 1. Insert a new task;","\n","2. Remove a task;","\n","3. Show all the tasks;","\n","4. Close the program.")
    choice = input()
    var = int(choice)
    if var == 1:
        print("New task:")
        task = input()
        list.append(task)
    elif var == 2:
        print("Task to eliminate:")
        task = input()
        if task in list:
            list.remove(task)
        else:
            print("Task not in your list!")
    elif var == 3:
        print("Tasks TODO:")
        for task in list:
            print(task)
    elif var == 4:
        end = True
    else:
        print("Range accepted is 1-4")