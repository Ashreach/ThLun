from ThLun import ProgressBar


import time

progress = ProgressBar(100, width=40)

for i in range(101):
    progress.update(i)
    time.sleep(0.02)

