#example usage
#python client.py -s 192.168.43.147
#refrence client ips on my network
	#1:
	#2:
	#3:
	#4:

# import the necessary packages
from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True,
	help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())
 
# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(
	args["server_ip"]))

# get the host name, initialize the video stream, and allow the
# camera sensor to warmup
rpiName = socket.gethostname()
vs = VideoStream(usePiCamera=True,resolution=(480,480)).start()
#vs = VideoStream(src=0).start()

print("warming up!")
time.sleep(2.0)
 
while True:
	# read the frame from the camera and send it to the server
	frame = vs.read()
	sender.send_image(rpiName, frame)
