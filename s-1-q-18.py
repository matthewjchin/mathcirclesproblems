# Question 1.18
x = 1 # initial number of cooked spaghetti strings 
y = 2020 # total number of cooked spaghetti strings
z = 1 # iterator
y += z # required to include the 2020th cooked spaghetti string

# probability that cooked spaghetti string is looped with a string of the 2020 strings
p = 1/2020 
expec = 0 # total expectation
sum = 0

for k in range (x, y, z):
    expec += (p * x)
    sum += x
    x += 1

# return the expectation
print(expec) 