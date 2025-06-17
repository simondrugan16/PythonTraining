
balls = 1

def increase_balls():
    balls = 2
    time = 1
    print(f"Number balls inside f(balls) = {balls}")

increase_balls()
print(f"Number balls outside f(balls) = {balls}")
# print(f"Can't bloody access time outside of the method... time = {time}")


list_of_things = ["list", "of", "things"]

if balls > 2:
    thing = list_of_things[2]

# print(f"What is this thing? {thing}")

global_variable = "dunno"

def change_global_variable():
    global global_variable
    global_variable = "dunno2"

print(global_variable)
change_global_variable()
print(global_variable)

global_variable_2 = "what"

def change_global_variable_2():
    global_variable_2 = "what2"
    return global_variable_2

print(global_variable_2)
global_variable_2 = change_global_variable_2()
print(global_variable_2)

