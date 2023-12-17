def main ():
    value =int(input('Enter a value:')) # value =10
    myfun2(value)
    #changedValue = myfun2(value) #changes inside myfun2 will be visible in the main fun
    print ('after call', value)
   # print ('after call', changedValue)

def myfun2(value):
    value = value + 9 # value =19
    print ('inside the myfun2', value)
    return value

main()
