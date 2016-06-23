import time
t=time.localtime()
for hora in range(1,25):
	for minuto in range (1,60):
		for segundo in range (1,60):
			print(str (hora)+":"+ str(minuto)+":"+str(segundo))
			time.sleep(1)

