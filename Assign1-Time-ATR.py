#Assign-Mass-ATR.py
#Alex Ross
# This program converts seconds to minutes and hours

def main():
    seconds = eval(input("What is the number of seconds to convert? "))
    runningsum = seconds
    hours = (runningsum // 3600)
    runningsum = runningsum - (hours * 3600)
    minutes = (runningsum // 60)
    runningsum = runningsum - (minutes * 60)


#    if runningsum < 0:
#        runningsum = 0
    
    print("There are",hours,"hours")
    print("There are",minutes,"minutes")
    print("There are",runningsum,"seconds leftover")
    
main()
