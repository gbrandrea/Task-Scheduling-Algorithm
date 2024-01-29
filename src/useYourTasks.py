import Task
import algorithms.search as algorithm
tasks_manager = Task.Task()
print("Now we will be using your very own tasks!\n")
while True:
    # Set task-related information with user input
    tasks_manager.set_tasks()
    tasks_manager.set_resources()
    tasks_manager.set_task_duration()
    tasks_manager.set_task_resource()
    tasks_manager.set_task_dependencies()
    alg=0
    while alg not in ['1', '2']:
        alg=input("Select '1' to use the Branch and Bound algorithm or '2' to use the A* algorithm:")
    alg = int(alg)
    if alg==1:
        print(algorithm.branchBound(tasks_manager.get_tasks(),tasks_manager.get_resources(),tasks_manager.get_task_duration(),
                              tasks_manager.get_task_resource(),tasks_manager.get_task_dependencies()))
    if alg==2:
        print(algorithm.branchBound(tasks_manager.get_tasks(),tasks_manager.get_resources(),tasks_manager.get_task_duration(),
                              tasks_manager.get_task_resource(),tasks_manager.get_task_dependencies()))
    # Get user input to decide whether to continue or exit
    user_input = input("Enter 'exit' or '0' to stop, or press Enter to continue creating tasks: ")

    # Check if the user wants to exit the loop
    if user_input.lower() in ['exit', '0']:
        break

