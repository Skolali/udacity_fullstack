import webbrowser
import time

total_breaks = 3
break_count = 0

print("Your program started at: "+time.ctime())
for break_count in  range(total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=eFjjO_lhf9c")
    
