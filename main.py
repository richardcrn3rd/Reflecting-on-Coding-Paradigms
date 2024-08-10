# def flatten_and_sort(arr):
#     def flatten(arr):
#         result = []
#         for item in arr:
#             if isinstance(item, list): #item is the object being checked and list is a class, type, or tuple (classes and types)
#                 result.extend(flatten(item))
#             else:
#                 result.append(item)
#         return result

#     flat_list = flatten(arr)
#     return sorted(flat_list)

# input_array = [3, [1,2,4,5], 6, [7, [8, 9]], 10]
# input_array = ('apple', 'pears', 'berries')
# sorted_array =flatten_and_sort(input_array)
# print(sorted_array)

# How does this solution ensure data immutability? The solution does not modify the data type.
# Is this solution a pure function? Why or why not? Yes, it will always return an ascending list.
# Is this solution a higher order function? Why or why not? NO, it is not returning a result as another function.
# Would it have been easier to solve this problem using a different programming style? Maybe easier if you understand other programming style. But, this was easier for me to understand.
# Why in particular is functional programming a helpful paradigm when solving this problem? 
    #Functional programming supports higher order function, immutabiity, and cleaner code etc....


# # Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

# def flatten_and_sort(array):
#     arr = []
#     for item in array:
#         for i in item:
#             arr.append(i)
#     return sorted(arr)
# print(flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]]))


# # Watto needs a new system for organizing his inventory of podracers. 
# # Help him do this by implementing an Object Oriented solution according to the following criteria.

# # First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

# # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# # # Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2

#   def repair(self):
#     self.condition = "NewCondition"
    
# # Define another class that inherits Podracer and call this one SebulbasPod. 
# # This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"

self = SebulbasPod(10,"perfect", 100)

self.max_speed = 500
self.set_max_speed(500)

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    #The solution demonstrated Ineritance, Encapsulation, and Abstraction 
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    #No, this solution provides cleaner code.
# How in particular did Object Oriented Programming assist in the solving of this problem?
    #Cleaner code by allowing you to reuse code, for example inheritance pillar.
