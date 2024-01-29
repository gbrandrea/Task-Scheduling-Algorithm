class Task:
    def __init__(self):
        self.tasks = 0
        self.resources = 0
        self.task_duration = []
        self.task_resource = []
        self.task_dependencies = []

    def set_tasks(self):
        try:
            self.tasks = int(input("Enter the number of tasks: "))
            if self.tasks < 1:
                raise ValueError("Number of tasks should be a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
            self.set_tasks()

    def set_resources(self):
        try:
            self.resources = int(input("Enter the number of resources: "))
            if self.resources < 1:
                raise ValueError("Number of resources should be a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
            self.set_resources()

    def set_task_duration(self):
        try:
            self.task_duration = list(map(int, input("Enter task durations separated by space: ").split()))
            if len(self.task_duration) != self.tasks:
                raise ValueError("Number of task durations should match the total number of tasks.")
            if any(duration < 1 for duration in self.task_duration):
                raise ValueError("Task duration should be a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
            self.set_task_duration()

    def set_task_resource(self):
        try:
            self.task_resource = list(map(int, input("Enter task resources separated by space: ").split()))
            if len(self.task_resource) != self.tasks:
                raise ValueError("Number of task resources should match the total number of tasks.")
            if any(resource < 1 for resource in self.task_resource):
                raise ValueError("Task resource should be a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
            self.set_task_resource()

    def set_task_dependencies(self):
        try:
            dependencies_str = input("Enter task dependencies as pairs (e.g., '1 4, 2 3'): ")
            dependencies_list = [tuple(map(int, pair.split())) for pair in dependencies_str.split(',')]
            self.task_dependencies = dependencies_list
            # Additional validation logic for dependencies can be added if needed
        except ValueError as e:
            print(f"Error: {e}")
            self.set_task_dependencies()

    def get_tasks(self):
        return self.tasks

    def get_resources(self):
        return self.resources

    def get_task_duration(self):
        return self.task_duration

    def get_task_resource(self):
        return self.task_resource

    def get_task_dependencies(self):
        return self.task_dependencies