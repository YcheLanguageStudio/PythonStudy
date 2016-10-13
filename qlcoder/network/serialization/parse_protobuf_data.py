import task_pb2
import sys

task = Task_pb2.Task()
f = open("task.data", "rb")
task.ParseFromString(f.read())
print task
f.close()
