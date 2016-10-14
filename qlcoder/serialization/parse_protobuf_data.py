import task_pb2
import sys

task = task_pb2.Task()
f = open("task.data", "rb")
task.ParseFromString(f.read())
print task

# for ele in task.answer.values:
#     print ele

f.close()
