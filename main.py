from timemaster import TimeMaster
from time import sleep

def main():
    # Initialize TimeMaster instance
    tm = TimeMaster()

    # Enable audible notifications for countdown completion
    # Supports Windows (Beep), macOS/Linux (System Bell)
    tm.reminder_sound = True

    # --- PART 1: Manual Time Tracking ---
    # Manually start and stop the timer to measure custom intervals
    tm.start_timer()
    print("Task started: Simulating a 5-second process...")
    sleep(5) 
    tm.stop_timer()

    # Extracting granular time data in various formats
    tm.get_elapsed()  # Returns formatted HH:MM:SS
    tm.get_seconds()  # Returns total elapsed seconds as integer
    tm.get_minutes()  # Returns elapsed minutes part

    # --- PART 2: Visual Stopwatch ---
    # Runs an interactive stopwatch on the console
    # Note: Press Ctrl+C to trigger the built-in KeyboardInterrupt handler
    tm.stopwatch()

    # --- PART 3: Countdown Functionality ---
    # Flexible countdown timer. Arguments can be combined:
    # Example: tm.countdown(hours=1, minutes=30, seconds=0)
    print("\nStarting a short demo countdown:")
    tm.countdown(seconds=3)


if __name__ == "__main__": 
    main()