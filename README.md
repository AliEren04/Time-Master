Time Master
-----------

**Time Master** is a lightweight, cross-platform Python library that combines **Stopwatch** and **Countdown** functionalities into a single, easy-to-use interface.

### Key Features

*   **Dual Mode:** Use it as a **Stopwatch** to measure execution time or as a **Countdown** timer for scheduled tasks.
    
*   **High Precision:** Uses time.monotonic() to ensure measurements are accurate and immune to system clock updates (drift-free).
    
*   **Smart Notifications:** Built-in support for audible alerts on Windows (Beep), macOS, and Linux (Terminal Bell).
    
*   **Cross-Platform:** Automatically detects the operating system to provide the best user experience.
    

### 💻 Usage Examples

#### 1\. Countdown Timer (With Sound)

Perfect for tasks that require a reminder when finished.

#### Python

```
from timemaster import TimeMaster
tm = TimeMaster()
tm.reminder_sound = True  # Enable the end-of-timer alert  
tm.countdown(hours=0, minutes=1, seconds=30)

```

#### 2\. Stopwatch

#### Python

```
from timemaster import TimeMaster
tm = TimeMaster() 
tm.stopwatch()
```


#### 3\. Granular Time Data

Retrieve specific time units after stopping the measurement.

#### Python

```
from timemaster import TimeMaster
from time import sleep 
tm = TimeMaster() 
tm.start_timer()
sleep(60)
tm.stop_timer()
tm.get_elapsed() #Prints Total Time Elapsed Since Timer Started in HH:MM:SS FORMAT e.g. 00:01:00
tm.get_hours() #Prints elapsed hours
tm.get_minutes() # Prints elapsed minutes
tm.get_seconds() # Prints total elapsed seconds   `
```

### Technical Insights

*   **Defensive Design:** Methods include checks to ensure the timer has been started before attempting to retrieve data, preventing logical errors.
    
*   **Efficiency:** The countdown loop is optimized with a 0.1s sleep interval to maintain low CPU usage while keeping high responsiveness.
    
*   **Platform Logic:** Utilizes platform.system() to choose between winsound and ASCII bell dynamically.
    

### Roadmap

*   \[ \] **Visual Stopwatch:** Add a live-updating forward-counting display.
    
*   \[ \] **Lap Support:** Ability to record multiple time intervals without resetting.
    
*   \[ \] **Logging:** Automatically save time logs to a .txt or .log file.