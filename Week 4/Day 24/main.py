#with open("Week 4/Day 24/my_file.txt") as file:
#    contents = file.read() 
#    print(contents)

#with open("Week 4/Day 24/my_file.txt", mode="w") as file:
#    file.write("dsadasd smh")

#with open("Week 4/Day 24/my_file.txt", mode="a") as file:
#    file.write("dsadasd smh")

with open("/Users/simon.drugan/PythonTraining/Udemy100Days/Week 4/Day 24/my_file.txt") as file:
    contents = file.read() 
    print(contents)

with open("/Users/simon.drugan/PythonTraining/Udemy100Days/Week 4/Day 24/my_file.txt", mode="a") as file:
    file.write("dsadasd smh")