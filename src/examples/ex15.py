tasks = 15
resources = 28
task_duration = [5, 3, 1, 1, 5, 2, 2, 8, 9, 1,
                 4, 2, 4, 1, 1]
task_resource = [8, 5, 1, 7, 1, 4, 1, 4, 5, 1,
                 7, 11, 1, 6, 1]
task_dependencies = [(1, 4), (2, 5), (3, 9), (3, 13), (4, 11), (4, 15), (5, 6), (5, 7),
                     (5, 14), (6, 8), (6, 10), (10, 12)]


def get_tasks():
    return tasks


def get_resources():
    return resources


def get_task_duration():
    return task_duration


def get_task_resource():
    return task_resource


def get_task_dependencies():
    return task_dependencies
