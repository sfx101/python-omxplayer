#Omxplayer Python wrapper
from subprocess import Popen, PIPE
OmxVolume = 0

class Pyomx():

	PyomxInstance = False
	volume = 0
	def __init__(self, link, output = 'hdmi', loop = True, layout = '2.1'):
		loop = '--loop' if loop else ''
		Popen('killall omxplayer.bin', stdout=PIPE, stderr=PIPE, shell=True)
		self.PyomxInstance = Popen(['omxplayer', link, '-o', output, '-b', loop, '--layout', layout, '--vol', str(OmxVolume)], stdin=PIPE, stdout=PIPE)

	def handle(self, command):
		global OmxVolume

		if command == 'play':
			send = ' '
		if command == 'pause':
			send = ' '
		elif command == 'seek_fast_rewind':
			#Down key
			send = '\x1B[B'
		elif command == 'seek_rewind':
			#Left key
			send = '\x1B[D'
		elif command == 'seek_forward':
			#Right key
			send = '\x1B[C'
		elif command == 'seek_fast_forward':
			#Up key
			send = '\x1B[A'
		elif command == 'volume_down':
			send = '-'
			OmxVolume -= 300
		elif command == 'stop':
			send = 'q'
		elif command == 'volume_up':
			send = '+'
			OmxVolume += 300
		else:
			send = ''

		try:
			if self.PyomxInstance:
				self.PyomxInstance.stdin.write(send)
			else:
				print 'An Omxplayer instance is not present, are you sure video is being played?'
		except Exception as e:
			pass
