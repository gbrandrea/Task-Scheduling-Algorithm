#we import all the algorithms
import algorithms.search as alg
#now the tasks
import examples.ex06 as ap1
import examples.ex07 as ap2
import examples.ex10 as ap3
import examples.ex15 as ap4
#In this area, we will be testing the results for the Branch and Bound algorithm. We will use the 6, 7 and 10 tasks example
print(alg.branchBound(ap1.get_tasks(),ap1.get_resources(),ap1.get_task_duration(),ap1.get_task_resource(),ap1.get_task_dependencies()))
print(alg.branchBound(ap2.get_tasks(),ap2.get_resources(),ap2.get_task_duration(),ap2.get_task_resource(),ap2.get_task_dependencies()))
print(alg.branchBound(ap3.get_tasks(),ap3.get_resources(),ap3.get_task_duration(),ap3.get_task_resource(),ap3.get_task_dependencies()))
#In this area, we will be testing the results for the A* algorithm. We will use the 6, 7 and 10 tasks example
print(alg.aStarAlgorithm(ap1.get_tasks(),ap1.get_resources(),ap1.get_task_duration(),ap1.get_task_resource(),ap1.get_task_dependencies()))
print(alg.aStarAlgorithm(ap2.get_tasks(),ap2.get_resources(),ap2.get_task_duration(),ap2.get_task_resource(),ap2.get_task_dependencies()))
print(alg.aStarAlgorithm(ap3.get_tasks(),ap3.get_resources(),ap3.get_task_duration(),ap3.get_task_resource(),ap3.get_task_dependencies()))
#For more than 10 tasks, the system doesn't work as well as for the previous examples, so sometimes it takes so long that it doesn't even run
print(alg.aStarAlgorithm(ap4.get_tasks(),ap4.get_resources(),ap4.get_task_duration(),ap4.get_task_resource(),ap4.get_task_dependencies()))
print(alg.branchBound(ap4.get_tasks(),ap4.get_resources(),ap4.get_task_duration(),ap4.get_task_resource(),ap4.get_task_dependencies()))