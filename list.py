# Question 1
my_list = []

# Question 2
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Question 3
my_list.insert(1, 15)
print(my_list)

# Question 4
new_list = [50, 60, 70]
my_list.extend(new_list)
print(my_list)

# Question 5
del my_list[-1]
print(my_list)

# Question 6
my_list.sort()
print(my_list)

# Question 7
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")