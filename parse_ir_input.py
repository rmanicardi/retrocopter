#!/usr/bin/python
import sys
import math
try:
	bitCount = 0
	waveform = ""
	bitform = ""
	pulseLengh=-1
	header=1
	bitcount=0
	bitReg="0"
	numbers=""
	for line in sys.stdin:
		command,level = line.split(" ")
		
		if (command == 'pulse'):
			threshold = float(level)/float(650)
			pulseLenght = int(math.floor(threshold+0.5))
			pulseLenghtPrinter = pulseLenght
			while (pulseLenghtPrinter > 0):
				waveform = waveform+'0'
				pulseLenghtPrinter = pulseLenghtPrinter -1
		else:
			threshold = float(level)/float(550)
			spaceLenght = int(math.floor(threshold+0.5))
			spaceLenghtPrinter = spaceLenght
			if(spaceLenghtPrinter < 3):
				if(header==0):
					if(pulseLenght>1):
						if(bitCount > 0):
							bitform= bitform+"1"
							bitReg=bitReg+"1"
						else
							bitform= bitform+"1"
					else:
						if(bitCount > 0):
							bitform= bitform+"0"
							bitReg=bitReg+"0"
					if(bitCount == 0):
						bitform=bitform+str(pulseLengh)
						if (pulseLengh>1):
							bitform=bitform+'A '
							numbers=numbers+'A '
						else:
							bitform=bitform+'B '
							numbers=numbers+'B '
					if((bitCount==6) or (bitCount==13) or (bitCount==19)):
						bitform = bitform + ' '
						if(bitCount==19):
							bitReg=bitReg+"0"
						numbers=numbers+str(int(bitReg,2))+" "
						bitReg="0"
				if(spaceLenghtPrinter==2):
					# assuming start of the packet
					bitCount=0
					bitReg="0"
					header=0
				else:
					bitCount = bitCount +1

				while (spaceLenghtPrinter > 0):
					waveform = waveform+'_'
					spaceLenghtPrinter = spaceLenghtPrinter -1
			else:
				waveform = waveform+'_'
				bitform= bitform+"0"
				print 
				print "w:"+waveform
				print "b:"+bitform
				print "n:"+numbers
				waveform=""
				bitform=""
				numbers=""
				header = 1
				
				
		
except KeyboardInterrupt:
	sys.stdout.flush()
	pass

