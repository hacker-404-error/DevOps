
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
    pass

datatypes()

def Strings():
    #Printing a string
    print("Hii")









