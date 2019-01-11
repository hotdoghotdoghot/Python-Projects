#Assign-box-ATR.py
#Alex Ross
# This program asks for the dimensions of a block of aluminium and calculates the density.

def main():
    density = eval(input("What is the density of the object in grams/cm^3? "))
    length = eval(input("What is the length of the box in centimeters? "))
    height = eval(input("What is the height of the box in centimeters? "))
    width = eval(input("What is the width of the box in centimeters? "))
    #Queries the user for the dimensions of the block

    volume = ( length * height * width )
    mass = (density * volume)
    
    print("The mass of the block is ",mass,"grams")

main()
