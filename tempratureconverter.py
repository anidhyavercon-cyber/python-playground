temprature = float(input("Enter the temprature : "))
Unit = input( "Is this temprature is in celius or farheniet? (C/F) : ")

if Unit == "C":
    result = (temprature * 9/5) + 32
    Unit = "F"
    print (f"The temprature is {result} {Unit} ")
elif Unit == "F":
    result = (( temprature - 32 ) * 5)/9  
    Unit = "C"
    print (f"The temprature is {result} {Unit} ") 
else:
    print ( f"{Unit} unit is not defined")