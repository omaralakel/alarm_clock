import time
from playsound import playsound

CLEARS = "\033[2KJ"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEARS)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")

minutes = int(input("HOw many minutes to wait: "))
seconds = int(input("HOw many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)