import os
import threading
import time



DATA_FILE_PATH="data/keys.lst"
last=""



def keypress():
	s=""
	for k in last.split("\n"):
		if (k==""):
			continue
		s+=k.title()+" + "
	print(s[:len(s)-3])
	if ("enter" in last):
		os.system("cls")



while (True):
	with open(DATA_FILE_PATH,"r") as f:
		d=f.readlines()
		if ("".join(d)!=last):
			last="".join(d)
			thr=threading.Thread(target=keypress,args=(),kwargs={})
			thr.start()
	time.sleep(0)
