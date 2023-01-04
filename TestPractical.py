from Agent import Action, Agent
from datetime import datetime
from enum import Enum, IntEnum

task = int(input("Pick a task: "))


testAgent1 = Agent.perform_action(task)

d1 = datetime(year = 2020, month = 2, day = 25, hour = 15, minute = 55, second = 59)

print("My shcedule for the day is exactly at : " + str(d1))

print(testAgent1)
