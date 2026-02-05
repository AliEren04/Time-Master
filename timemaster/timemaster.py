from time import monotonic, sleep
from platform  import system
from winsound import Beep

class TimeMaster:
    def __init__(self):
        self.hours = 0
        self.minutes = 0 
        self.seconds = 0
        self.passed_seconds = 0
        self.start_time = 0 
        self.end_time = 0
        self.reminder_sound = False
        self.stopwatch_active = False


    def start_timer(self):
        self.start_time = monotonic()
      
    
    def stop_timer(self):
        self.end_time = monotonic()
       

    
    def get_elapsed(self):
        if self.start_time == 0:
            print("Timer Has Not Started Yet Please Start The Timer!")
            return
        current_end = self.end_time if self.end_time != 0 else monotonic()
        self.passed_seconds = int(current_end - self.start_time)
        self.hours = self.passed_seconds // 3600
        self.minutes = (self.passed_seconds % 3600) // 60
        self.seconds = self.passed_seconds % 60
        print(f"Total Time Elapsed Since Timer Started: {self.hours:02}:{self.minutes:02}:{self.seconds:02}")
     

    def get_hours(self):
        if self.start_time == 0: 
            print("Timer Has Not Started Yet Please Start The Timer!")
            return
        current_end = self.end_time if self.end_time != 0 else monotonic()
        self.passed_seconds = int(current_end - self.start_time)
        self.hours = self.passed_seconds // 3600
        print(f"{self.hours} hours elapsed since timer started")


    def get_minutes(self):
        if self.start_time == 0: 
            print("Timer Has Not Started Yet Please Start The Timer!")
            return
        current_end = self.end_time if self.end_time != 0 else monotonic()
        self.passed_seconds = int(current_end- self.start_time)
        self.minutes = (self.passed_seconds % 3600) // 60
        print(f"{self.minutes} minutes elapsed since timer started")


    def get_seconds(self):
        if self.start_time == 0: 
            print("Timer Has Not Started Yet Please Start The Timer!")
            return
        current_end = self.end_time if self.end_time != 0 else monotonic()
        self.passed_seconds = int(current_end - self.start_time)
        print(f"{self.passed_seconds} seconds elapsed since timer started")



    def countdown(self, hours=0, minutes=0, seconds=0):
        try: 
            self.start_timer()
            target = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
            last_print = -1 
            while True:
                self.passed_seconds = int(monotonic() - self.start_time)
                remaining_time  = target - self.passed_seconds
                self.hours = remaining_time // 3600
                self.minutes = (remaining_time % 3600) // 60
                self.seconds = remaining_time % 60
                if self.passed_seconds != last_print: 
                    print(f"\r{self.hours:02}:{self.minutes:02}:{self.seconds:02}",end="")
                    last_print = self.passed_seconds
                
                if remaining_time <= 0:
                    self.stop_timer()
                    if self.reminder_sound == True:
                        sys_name = system()
                        if sys_name == "Windows":
                            Beep(1000, 500)  
                        elif sys_name in ["Linux","Darwin"]:
                            print('\a') 
                        else:
                            print("\nPlatform Not Supported For Beeping")

                    print("\nTimer Finished")
                    break
            sleep(0.1)
        except KeyboardInterrupt:
            print("\nProgram Interrupted e.g. Ctrl c")
        
        except ValueError:
            print("Invalid Data Type Please Enter Integers For Hours Minutes and Seconds!")

    def stopwatch(self):
        try:
            print("Stopwatch starting... Press Ctrl+C to stop.")
            self.stopwatch_active = True
            self.start_timer()
            while self.stopwatch_active == True:
                self.passed_seconds = int(monotonic() - self.start_time)
                self.minutes = (self.passed_seconds % 3600) // 60
                self.seconds = self.passed_seconds % 60
                self.milliseconds = int(((monotonic() - self.start_time) % 1) * 100)
                print(f"\r{self.minutes:02d}:{self.seconds:02d}:{self.milliseconds:02d}", end="")

        except KeyboardInterrupt:
            print("\nStopwatch Stopped!")
            self.stopwatch_active = False
    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'