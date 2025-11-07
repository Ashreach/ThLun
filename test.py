from ThLun import ProgressBar
import time

процесів = 20
закінчено = 20

pr = ProgressBar(процесів, width=40, color=2)

for i in range(закінчено + 1):
    pr.update(i)
    time.sleep(0.02)


print("\nAll done!")
