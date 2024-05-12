
#-------------------------------------------- DATA TYPESS -------------------------------------------- 

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''  
def datatypes():

    a = "Hello World"
    print(a," : ",type(a),"\n")

    b = 20
    print(b," : ",type(b),"\n")

    c = 2.5
    print(c," : ",type(c),"\n")

    d = 1j
    print(d," : ",type(d),"\n")

    e = [1,2,"Apple","Green"]
    print(e," : ",type(e),"\n")

    f = (1,2,"Apple","Green")
    print(f," : ",type(f),"\n")

    g = range(6)
    print(g," : ",type(g),"\n")

    h = {"Apple", "Green", 1, 2}
    print(h," : ",type(h),"\n")

    g = { "Red" : "Banana", 1 : "True" }
    print(g," : ",type(g),"\n")

    h = frozenset(g)
    print(h," : ",type(h),"\n")

    i = True
    print(i," : ",type(i),"\n")

    j = b"HEllo"
    print(j," : ",type(j),"\n")

    k = bytearray(5)
    print(k," : ",type(k),"\n")

    l = memoryview(bytes(5))
    print(l," : ",type(l),"\n")

    m = None
    print(m," : ",type(m),"\n")

def Variables():
    # Get the type
    x = 5
    print(x,"\n")

    # Type Casting
    y = int(x)
    z = float(x)
    l = str(x)
    print(y," ",z," ",l," ")

def Strings_Operations():
    # Printing String
    print("Hello World")

    # Quotes inside String
    print("I'm fine")
    print("Hello this is 'Jay' ")
    print('Hello Jay, This is "Jacob" ')

    # Assigning String to a Variable
    s = "Hello"
    print(s)

    # Multiline String
    a = """Hello everyone,
      this is a example of multiline string,
      this can be achieved using three double quotes """
    print(a)

    b = '''Hello everyone,
    this is a example of multiline string,
    this can be achieved using three single quotes also.'''
    print(b)

    # String are Arrays
    arr = "Hello World!"
    print(arr[1]) # prints e, indexing starts from 0 
    print(len(arr)) #Gives length of array arr 

    # Looping through a string
    for x in "banana":
        print(x)




datatypes()
Strings_Operations()

def Strings():
    #Printing a string
    print("Hii")









