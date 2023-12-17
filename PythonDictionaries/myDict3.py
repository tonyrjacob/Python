dict1={'jincy':30,'john':29,'mary':41,'george':19,'may':35, 'salma':21}
search =int(input ("Enter the age to search: "))
for name,age in dict1.items():
   #print (name," : ",age)
    if search==age: # == is a relational (comparison) operator to compare two values
        print ("I found: ",name)
print ("thanks for trying!")
