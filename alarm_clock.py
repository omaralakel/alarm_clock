import time
from playsound import playsound


def alarm(seconds):

    time_elapsed = 0
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"The estimated time left is {minutes_left}:{seconds_left}")


    playsound("alarm.mp3")
alarm(10)