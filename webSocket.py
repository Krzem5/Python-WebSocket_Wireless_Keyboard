from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import threading
import time



KEY_DOWN_TIME=0.1
FILE_PATH="./data/keys.lst"
with open(FILE_PATH,"w") as f:
	pass



def add_key(k):
	with open(FILE_PATH,"r") as f:
		for ln in f.readlines():
			if (ln.replace("\n","")==k):
				return
	with open(FILE_PATH,"a") as f:
		f.write(k+"\n")
def remove_key(k):
	l=[]
	with open(FILE_PATH,"r") as f:
		l=f.readlines()
	with open(FILE_PATH,"w") as f:
		for ln in l:
			if (ln.replace("\n","")==k):
				continue
			f.write(ln)



class Client(WebSocket):
	def handleMessage(self):
		thr=threading.Thread(target=self.process_message,args=(),kwargs={})
		thr.deamon=True
		thr.start()
	def handleConnected(self):
		pass
	def handleClose(self):
		pass
	def process_message(self,*args):
		msg=self.data
		self.sendMessage("null")
		if (msg[:4]=="key:"):
			add_key(msg[4:])
			time.sleep(KEY_DOWN_TIME)
			remove_key(msg[4:])
		elif (msg[:5]=="keyD:"):
			add_key(msg[5:])
		elif (msg[:5]=="keyU:"):
			remove_key(msg[5:])



server=SimpleWebSocketServer("192.168.178.56",8080,Client)
print("\nWebSocketServer has started on port 8080!\n")
server.serveforever()