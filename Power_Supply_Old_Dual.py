import serial
import time

#####################################################
## V = Volts e.g "12"
## I = Current e.g "0.5"  = 500mA  "1" = 1A
## OP = Output  e.g "1"= On  "0"=Off
##################################################### 
def test_SerialOn(V,I,OP):  
	"""scan for available ports. return a list of tuples (num, name)"""
	available = []
	for i in range(256):
		print("trying {}".format(i))
		try:
			s = serial.Serial(i)
			print(i)
			available.append( (i, s.name))
			s.write("V "+str(V)+"\r\n")
			s.write("V1 "+str(V)+"\r\n")
			s.write("V2 "+str(V)+"\r\n")
			s.write("I "+str(I)+"\r\n")
			s.write("OP "+str(OP)+"\r\n")
			s.write("OP1 "+str(OP)+"\r\n")
			s.write("OP2 "+str(OP)+"\r\n")
			s.close()   # explicit close 'cause of delayed GC in java
		except serial.SerialException:
			pass
	print available
	return available
#testSerialOn(11,0.8,0)  # voltage= 12 , Current= 1A , Output = ON



test_SerialOn(12,0,1)
time.sleep(2)

