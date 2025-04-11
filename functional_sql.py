#!/usr/bin/python3

import inspect

persons = [
    {"name": "Peter", "profession": "teacher", "age": 20, "marital_status": "married"},
    {"name": "Michael", "profession": "teacher", "age": 50, "marital_status": "single"},
    {"name": "Peter", "profession": "teacher", "age": 20, "marital_status": "married"},
    {"name": "Anna", "profession": "scientific", "age": 20, "marital_status": "married"},
    {"name": "Rose", "profession": "scientific", "age": 50, "marital_status": "married"},
    {"name": "Anna", "profession": "scientific", "age": 20, "marital_status": "single"},
    {"name": "Anna", "profession": "politician", "age": 50, "marital_status": "married"}
]

def query():
    return SQL()
        
def profession(person):
    return person["profession"]

def is_teacher(person):
    return person["profession"] == "teacher"
    
def name(person):
    return person["name"]

def profession_group(group):
    return group[0]
    
def is_even(number):
    return number % 2 == 0

def parity(number):
    return "even" if is_even(number) else "odd"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Multilevel grouping:
def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while number % divisor != 0:
        divisor += 1

    return divisor == number

def prime(number):
    return "prime" if is_prime(number) else "divisible"
    
class SQL:
    def __init__(self):
        self.__func_select = ""
        self.__func_where = ""
        self.__func_group_by1 = ""
        self.__func_group_by2 = ""
        
        self.__list_sql = []
        self.__list_select = []
        self.__list_result = []
        self.__list_where = []
        self.__list_group_by = []
        self.__list_priority = [{"select": 0}, 
                            {"from_": 0}, 
                            {"where": 0}, 
                            {"order_by": 0}, 
                            {"group_by": 0}, 
                            {"having": 0}, 
                            {"execute": 0}]
    
    def select(self, func = ""):
        self.__exceptions(0)  
        self.__func_select = func
        return self
       
    def from_(self, list_new = []):
        self.__exceptions(1)
        self.__list_sql = list_new.copy()
        return self
        
    def where(self, func = ""):
        self.__exceptions(2)
        self.__func_where = func
        return self
        
    def order_by(self, func = ""):
        self.__exceptions(3)
        self.func = func
        return self
        
    def group_by(self, func1 = "", func2 = ""):
        self.__exceptions(4)
        self.__func_group_by1 = func1
        self.__func_group_by2 = func2
        return self
        
    def having(self, func = ""):
        self.__exceptions(5)
        self.func = func
        return self
    
    def execute(self):
        self.__exceptions(6)  
        
        # SELECT
        if bool(self.__func_select) and self.__func_select.__name__ not in "profession_group" :
            for x in self.__list_sql:
                temp = self.__func_select(x)
                self.__list_result.append(temp)
                self.__list_select.append({self.__func_select.__name__:temp})
        else:
            self.__list_result = self.__list_select = self.__list_sql
            
         # WHERE       
        if bool(self.__func_where):
            for x in self.__list_sql:
                if self.__func_where(x):
                    if bool(self.__func_select):
                        self.__list_where.append(x[self.__func_select.__name__])
                    else:
                       self.__list_where.append(x)    
            self.__list_result = self.__list_where 

        # GROUP BY       
        if bool(self.__func_group_by1):
            for x in self.__list_sql:
                temp = self.__func_group_by1(x)    
                if len(self.__list_group_by) == 0:
                    self.__list_group_by.append([temp, [x]])
                else:
                    i = 0
                    while i < len(self.__list_group_by):
                        if temp == self.__list_group_by[i][0]:
                            self.__list_group_by[i][1].append(x)
                            break
                        i += 1 
                    if i == len(self.__list_group_by):
                        self.__list_group_by.append([temp, [x]])
            # Second parameter
            if bool(self.__func_group_by2):
                list_temp = [["odd",[]],["even",[]]]
                for z in self.__list_group_by:
                    list_prime=["prime",[]]
                    list_divisible=["divisible",[]]
                    for w in z[1]:
                        if self.__func_group_by2(w) == "prime":
                            list_prime[1].append(w)
                        else:
                            list_divisible[1].append(w)
                    if z[0]=="odd":
                        list_temp[0][1].append(list_divisible)
                        list_temp[0][1].append(list_prime)
                    else:
                        list_temp[1][1].append(list_prime)
                        list_temp[1][1].append(list_divisible)
                self.__list_group_by = list_temp.copy()
                        
                        
            ## WHERE     
            if bool(self.__func_where):
                self.__list_result = []
                for y in self.__list_group_by:
                    if self.__func_where(y[1][0]):
                        self.__list_result = y
                        break
            ## SELECT
            elif bool(self.__func_select):
                self.__list_result = []
                for y in self.__list_group_by:
                     self.__list_result.append(self.__func_select(y))
            else:
                self.__list_result = self.__list_group_by
        
        # EXECUTE
        print(self.__list_result)
        
    def __exceptions(self, index):
        match index:
          case 0:
            assert (not(self.__list_priority[0]["select"])),"DuplicateSelectError()"
            self.__list_priority[0]["select"] += 1
          case 1:
            assert (not(self.__list_priority[1]["from_"])),"DuplicateFromError()"
            self.__list_priority[1]["from_"] += 1
          case 2:
            assert (not(self.__list_priority[2]["where"])),"DuplicateWhereError()"
            self.__list_priority[2]["where"] += 1
          case 3:
            assert (not(self.__list_priority[3]["order_by"])),"DuplicateOrder_byError()"
            self.__list_priority[3]["order_by"] += 1
          case 4:
            assert (not(self.__list_priority[4]["group_by"])),"DuplicateGroup_byError()"
            self.__list_priority[4]["group_by"] += 1
          case 5:
            assert (not(self.__list_priority[5]["having"])),"DuplicateHavingError()"
            self.__list_priority[5]["having"] += 1
          case 6:
            assert (not(self.__list_priority[6]["execute"])),"DuplicateExecuteError()"
            self.__list_priority[6]["execute"] += 1

print("SELECT * FROM numbers GROUP BY parity, is_prime")
query().select().from_(numbers).group_by(parity, prime).execute()
# [["odd", [["divisible", [1, 9]], ["prime", [3, 5, 7]]]], ["even", [["prime", [2]], ["divisible", [4, 6, 8]]]]]
# [
#   ["odd", 
    #       [
    #           ["divisible", [1, 9]], ["prime", [3, 5, 7]
    #       ]
    #   ]
    #], ["even", [["prime", [2]], ["divisible", [4, 6, 8]]]]
#]
print("\n")

"""
print("SELECT * FROM numbers GROUP BY parity") 
query().select().from_(numbers).group_by(parity).execute()
# [["odd", [1, 3, 5, 7, 9]], ["even", [2, 4, 6, 8]]]
print("\n")

print("SELECT * FROM numbers") 
query().select().from_(numbers).execute()
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n")

print("SELECT profession FROM persons GROUP BY profession")    
query().select(profession_group).from_(persons).group_by(profession).execute()
# ["teacher", "scientific", "politician"]
print("\n")

print("SELECT * FROM persons WHERE profession='teacher' GROUP BY profession")    
query().select().from_(persons).where(is_teacher).group_by(profession).execute()
# ["teacher", [
#   {"name": "Peter", "profession": "teacher", "age": 20, "marital_status": "married"},
#   {"name": "Michael", "profession": "teacher", "age": 50, "marital_status": "single"},
#   {"name": "Peter", "profession": "teacher", "age": 20, "marital_status": "married"}
# ]]
print("\n")

print("SELECT * FROM persons GROUP BY profession <- Bad in SQL but possible in this kata")    
query().select().from_(persons).group_by(profession).execute()
# [
#     ["teacher", [
#         {"name": "Peter", "profession": "teacher", ...},
#         {"name": "Michael", "profession": "teacher", ...}
#     ]],
#     ["scientific", [
#         {"name": "Anna", "profession": "scientific"},
#         ...
#     ]],
#     ...
# ]
print("\n")


print("SELECT name FROM persons WHERE profession='teacher'")    
query().select(name).from_(persons).where(is_teacher).execute()
# ["Peter", "Michael", "Peter"]
print("\n")

print("SELECT * FROM persons WHERE profession='teacher'")    
query().select().from_(persons).where(is_teacher).execute()
# [{"person": "Peter", "profession": "teacher", ...}, ...]
print("\n")

print("SELECT profession FROM persons WHERE profession='teacher'")    
query().select(profession).from_(persons).where(is_teacher).execute()
# ["teacher", "teacher", "teacher"]
print("\n")

print("SELECT *")    
query().select().execute()
# []
print("\n")  

print("FROM [1,2,3]")    
query().from_([1,2,3]).execute()
 # [1, 2, 3]
print("\n")  

print("None")    
query().execute()
# []
print("\n")  

print("SELECT profession FROM persons")    
query().select(profession).from_(persons).execute()
# ["teacher", "teacher", "teacher", "scientific", "scientific", "scientific", "politician"]
print("\n")

print("SELECT * FROM persons") 
query().select().from_(persons).execute()
# [{"name": "Peter", ...}, {"name": "Michael", ...}]
print("\n")  

print("SELECT * FROM [2,3,4,5]")
query().select().from_([2,3,4,5]).execute()
# [2,3,4,5]
print("\n")  


print("DuplicateSelectError()")    
query().select().from_(persons).select().execute()
print("\n")  
"""

