import time
def count_down_timer(start):
    while start >= 0:
        print(start)
        time.sleep(1)
        start -= 1


    print("Time's up!💀")


if __name__ == "__main__":
    try:
        start_Time = int(input("Enter the number to start the countdown from:__"))
        count_down_timer(start_Time)

    except ValueError:
        print("Please enter a valid integer")