# Timer
A simple console based timer made with Python

import time # import time package

# accepting user's input for hours
while True: 
    try: 
        hrs = int(input("Enter hours: "))
        break
    except ValueError:
        print("Please enter a valid number!")

# accepting user's input for minutes
while True:
    try:
        mins = int(input("Enter minutes: "))
        break
    except ValueError:
        print("Please enter a valid number!")

# accepting user's input for seconds
while True:
    try:
        secos = int(input("Enter seconds: "))
        break
    except ValueError:
        print("Please enter a valid number!")

# condition
if hrs == 0 and mins == 0 and secos == 0:
    print("All values can not be 0!")

# convert hours and minutes to seconds and add all of them together
def conversion(hrs, mins, secos):
    totalseconds = hrs*3600+mins*60+secos
    return totalseconds

# getting total number of seconds
totaltime = conversion(hrs, mins, secos)

# printing each second and the actual things that make the program
# count every second
for num in range(totaltime, 0, -1):
    print(num)
    time.sleep(1)

print("TIME UP!!!")    
