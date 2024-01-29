import queue
import numpy as np

def branchBound(tasks=0, resources=0, task_duration=[], task_resource=[], task_dependencies=[]):
    # Queue to store possible paths
    queuee = queue.Queue()
    current_path = []
    best_path = []
    best_time = 0

    # Initializing current and best paths with NaN
    for i in range(0, len(task_duration)):
        current_path.append(np.nan)
        best_path.append(np.nan)
    queuee.put(current_path)

    while not queuee.empty():
        current_path = queuee.get()
        # Expand the current path
        if not expand_path(current_path, queuee, task_duration, task_resource, resources, task_dependencies):
            # Find the highest time in the current path
            highest_time = max(current_path[i] + task_duration[i] if not np.isnan(current_path[i]) else 0 for i in
                               range(len(current_path)))
            # Update the best path if a faster one is found
            if np.isnan(best_path[0]) or best_time > highest_time:
                best_path = current_path
                best_time = highest_time

    return best_path

def expand_path(path=[], queuee=queue.Queue(), task_duration=[], task_resource=[], resources=0, task_dependencies=[]):
    path_copy = path.copy()
    max_time = 0
    latest_end_time = 0
    is_expanded = False

    # Find the highest time and latest end time in the path
    for i in range(len(path)):
        if path[i] + task_duration[i] > latest_end_time:
            max_time = path[i]
            latest_end_time = path[i] + task_duration[i]

    for i in range(len(path)):
        if np.isnan(path[i]):
            explored_times = []
            is_expanded = True
            path_copy[i] = max_time

            # Check dependencies and resources before adding the new path to the queue
            if (check_dependencies(path_copy, task_duration, task_dependencies) and
                    check_resources(path_copy, task_duration, task_resource, resources)):
                queuee.put(path_copy.copy())

            explored_times.append(max_time)

            for j, j_duration in enumerate(path):
                if not np.isnan(j_duration) and j_duration + task_duration[j] > max_time:
                    new_time = j_duration + task_duration[j]
                    if explored_times.count(new_time) == 0:
                        path_copy[i] = new_time
                        # Check dependencies and resources before adding the new path to the queue
                        if (check_dependencies(path_copy, task_duration, task_dependencies) and
                                check_resources(path_copy, task_duration, task_resource, resources)):
                            queuee.put(path_copy.copy())
                    explored_times.append(new_time)

            path_copy[i] = np.nan

    return is_expanded

def check_dependencies(path=[], task_duration=[], task_dependencies=[]):
    # Check that there are no unresolved dependencies between any two tasks
    for t1, t2 in task_dependencies:
        if not np.isnan(path[t2 - 1]) and (np.isnan(path[t1 - 1]) or path[t1 - 1] + task_duration[t1 - 1] > path[t2 - 1]):
            return False
    return True

def check_resources(path=[], task_duration=[], task_resource=[], resources=0):
    # Check resources
    for i in range(len(path)):
        if not np.isnan(path[i]):
            r = task_resource[i]
            for j in range(len(path)):
                if not np.isnan(path[j]) and j != i:
                    if path[j] <= path[i] < path[j] + task_duration[j]:
                        r += task_resource[j]
            if r > resources:
                return False
    return True

def heuristic(path=[], dependencies=[], durations=[], resources=[]):
    remaining_durations = []
    max_duration = 0

    for i in range(len(dependencies)):
        if i < len(resources) and i not in path:
            remaining_durations.append(durations[i] / resources[i])
            max_duration = max(max_duration, durations[i])

    total_completion_time = max_duration + sum(remaining_durations)
    return total_completion_time

def aStarAlgorithm(tasks=0, resources=0, task_duration=[], task_resource=[], task_dependencies=[]):
    # Create a priority queue to store possible paths with their cost values
    queuee = queue.PriorityQueue()
    current_path = []
    best_path = []
    best_time = 0

    # Initialize current and best paths with NaN
    for i in range(0, len(task_duration)):
        current_path.append(np.nan)
        best_path.append(np.nan)

    # Initialize the queue with the initial path and its cost value
    queuee.put((0, current_path))

    while not queuee.empty():
        f_value, current_path = queuee.get()
        g_value = f_value - heuristic(current_path,task_dependencies,task_duration,task_resource)
        # Check if all tasks have been executed and return the current path if so
        if all_executed(current_path, task_duration, task_resource, resources, task_dependencies):
            return current_path
        # Expand the current path using the A* method
        if not expand_path_A(current_path, queuee, task_duration, task_resource, resources, task_dependencies, g_value):
            # Find the highest time in the current path
            highest_time = max(current_path[i] + task_duration[i] if not np.isnan(current_path[i]) else 0 for i in
                               range(len(current_path)))
            # Check if all tasks have been executed and return the current path if so
            if all_executed(current_path, task_duration, task_resource, resources, task_dependencies):
                return current_path
            # Update the best path if a faster one is found
            if np.isnan(best_path[0]) or best_time > highest_time:
                best_path = current_path
                best_time = highest_time

    return best_path

def expand_path_A(path=[], queuee=queue.PriorityQueue(), task_duration=[], task_resource=[], resources=0, task_dependencies=[], g_value=0):
    path_copy = path.copy()
    max_time = 0
    latest_end_time = 0
    is_expanded = False

    # Find the highest time and latest end time in the path
    for i in range(len(path)):
        if path[i] + task_duration[i] > latest_end_time:
            max_time = path[i]
            latest_end_time = path[i] + task_duration[i]

    for i in range(len(path)):
        if np.isnan(path[i]):
            explored_times = []
            is_expanded = True
            path_copy[i] = max_time

            # Check dependencies and resources before adding the new path to the queue
            if (check_dependencies(path_copy, task_duration, task_dependencies) and
                    check_resources(path_copy, task_duration, task_resource, resources)):
                new_f_value = g_value + task_duration[i] + heuristic(path_copy,task_dependencies,task_duration,task_resource)
                queuee.put((new_f_value, path_copy.copy()))

            explored_times.append(max_time)

            for j, j_duration in enumerate(path):
                if not np.isnan(j_duration) and j_duration + task_duration[j] > max_time:
                    new_time = j_duration + task_duration[j]
                    if explored_times.count(new_time) == 0:
                        path_copy[i] = new_time
                        # Check dependencies and resources before adding the new path to the queue
                        if (check_dependencies(path_copy, task_duration, task_dependencies) and
                                check_resources(path_copy, task_duration, task_resource, resources)):
                            new_f_value = g_value + new_time + heuristic(path_copy,task_dependencies,task_duration,task_resource)
                            queuee.put((new_f_value, path_copy.copy()))
                    explored_times.append(new_time)

            path_copy[i] = np.nan

    return is_expanded

def all_executed(current_path=[],task_duration=[],task_resource=[],resources=0,task_dependencies=[]):
    res=True
    for i in range(len(current_path)):
        if np.isnan(current_path[i]):
            res=False
    if not check_resources(current_path,task_duration,task_resource,resources):
        res=False
    if not check_dependencies(current_path,task_duration,task_dependencies):
        res=False
    return res
