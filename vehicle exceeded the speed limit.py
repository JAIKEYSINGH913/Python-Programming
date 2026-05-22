# 4
# A traffic monitoring system needs to determine whether a vehicle exceeded the speed limit.

SPEED_LIMIT = 100

# Get input from the user
User_Speed = int(input("Enter your speed limit: "))
if User_Speed > SPEED_LIMIT:
    print("vehicle exceeded the speed limit.")

elif User_Speed < SPEED_LIMIT:
    print("vehicle does not exceeded the speed limit.")

else:
    print("vehicle speed limit is constant.")