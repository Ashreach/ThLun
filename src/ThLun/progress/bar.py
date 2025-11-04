import time
import sys

for i in range(101):
    bar = '█' * i + '*' * (100 - i)
    sys.stdout.write(f'\r[{bar}] {i}%')
    sys.stdout.flush()
    time.sleep(0.05)

print("\nDone!")
