#Assign1-Cricket-ATR
#Alex Ross
#This program calculates the temperature based on the frequency of cricket chirps

def main():
    chirps = eval(input("How many chirps did you hear in 60 seconds? "))

    val = (chirps // 4) + 40

    print("The temperature is",val,"degrees farenheit")
main()
    
    
