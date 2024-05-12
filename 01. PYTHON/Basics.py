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

#-------------------------------------------- Python Variables -------------------------------------------- 
'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''
def Variables():
    # Get the type
    x = 5
    print(type(x))

    # Type Casting
    y = int(x)
    z = float(x)
    l = str(x)
    print(y," ",z," ",l," ")

    # Single Quotes Vs Double Quotes
    x = 'Pritam'
    y = "Pritam"
    print(x," Is Equal To: ",y)

    # Case Sensitive
    x = 4;
    X = "Apple"
    print("x = ",x," Does Not Overwrite y = ",X)

    # Ways of Writing Variable
    # 1. Camel Case: Each word, except the first, starts with a capital letter
    myFirstVariableName = "Pritam"
    print(myFirstVariableName,"\n")
    # 2. Pascal Case: Each word starts with a capital letter.
    MySecondVariableName = "Das"
    print(MySecondVariableName,"\n")
    # 3. Snake Case: Each word is separated by an underscore character
    My_Third_Variable_Name = "Hello World"
    print(My_Third_Variable_Name,"\n")

    # Assign Multiple Values
    x = y = z = "pritam"
    print(x)
    print(y)
    print(z)
    x,y,z = "I", "AM", "OK"
    print(x)
    print(y)
    print(z)
    fruits = ["Apple", "Orange", "Banana"]
    x,y,z = fruits
    print(x)
    print(y)
    print(z)


def Strings_Operations():
    a = "Hello World"
    print(a)


# datatypes()
Variables()
# Strings_Operations()











