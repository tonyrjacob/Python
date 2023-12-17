import math
num7=   3.9
num8=   5.7
print(math.ceil(num7))# returns the smallest integer not less than num7
print(math.floor(num7))# returns the larger integer not greater than num7
print()
print(math.ceil(num8))
print()
print("the modf is ", math.modf(num8))# returns a tuple of the integer and decoimal parts
modf_out = math.modf(num8)
print ("the fraction is: ",modf_out[0],", the integer is ",modf_out[1])
print()
num2= 5
num3= 3
the_pow= pow(num2,num3)# same as **
print (the_pow)
print()
the_sqrt =math.sqrt (16)
print (the_sqrt)
print()

round1=round(5.3468,2)
print(round1)
print()
print (max(1,2,4,3))
print (min(1,2,4,3))
print()
max1=max(1,2,4,3)
print (max1)
