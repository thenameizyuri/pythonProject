#Nobel Cs cluB
import datetime
from playsound import playsound


alarm_time = input("Enter the time in a format HH:MM:SS:AMorPM\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")


while True:
    current_time = datetime.now()
    current_hour = current_time.strftime("%H")
    current_minute = current_time.strftime("%M")
    current_seconds = current_time.strftime("%S")
    current_period = current_time.strftime("%p")


    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break