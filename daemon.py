import datetime
import time
import subprocess

daemon_start=datetime.time(18, 55, 30)
daemon_end=datetime.time(18, 56, 00)

if __name__=="__main__":
	while True:
		time_only = datetime.datetime.now().time().replace(microsecond=0)
		print(time_only)
		if time_only == daemon_start:
			subprocess.Popen(["python", "open.py"])
		if time_only == daemon_end:
			subprocess.Popen(["python", "close.py"])
		time.sleep(0.5)