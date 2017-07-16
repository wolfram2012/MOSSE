import numpy as np
import cv2
# from pyvision.types import Image

cap = cv2.VideoCapture(0)

if __name__ == '__main__':
	# while(1):
	#     # get a frame
	#     ret, frame = cap.read()
	#     # show a frame
	#     cv2.imshow("capture", frame)
	#     if cv2.waitKey(1) & 0xFF == ord('q'):
	#         break
	# cap.release()
	# cv2.destroyAllWindows() 

	ret, frame = cap.read()
	    # show a frame
	print "originImg message:"
	print frame.shape
	print frame.dtype
	print isinstance(frame,np.ndarray)

	GrayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	print "grayImg message:"
	print GrayImg.shape
	print GrayImg.dtype
	print isinstance(GrayImg,np.ndarray)

	bufferimg = GrayImg.transpose().tostring()
	print "bufferImg message:"
	# print bufferimg.shape
	# print bufferimg.dtype
	print isinstance(bufferimg,np.ndarray)
	print isinstance(bufferimg,str)


	cv2.imshow("capture", GrayImg)
	cv2.waitKey()
	cap.release()
	cv2.destroyAllWindows()