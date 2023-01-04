from datetime import datetime
from enum import Enum, IntEnum

class Action(IntEnum):
    Breakfast = 1
    Lunch = 2
    Dinner = 3
    Sleep = 4
    Gym = 5
    Class = 6
    Church = 7
    Television = 8
    River = 9

class Agent: #agent class

  def __init__(self, initialstate):
       self.state = initialstate
       pass

  def sense_world(self, dt, sick):
    
        return self.state

  def perform_action(task):
        if task == Action.Lunch:
    
            return "I am eating lunch"
        
        elif task == Action.Breakfast:
            
            return "I am eating breakfast"
        
        elif task == Action.Sleep:
            
            return "I am going to sleep"
        
        elif task == Action.Dinner:
            
            return "I am eating dinner"
        
        elif task == Action.Gym:
            
            return "It is time for gym"
        
        elif task == Action.Class:
            
            return "I am going to class"
        
        elif task == Action.Church:
            
            return "It is time to go to church"
        
        elif task == Action.Television:
            
            return "I am watching television"
        
        elif task == Action.River:
            
            return "I am going to meet someone special by the river"
        

    
            
