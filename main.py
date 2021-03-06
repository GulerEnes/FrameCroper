import cv2 as cv
import os

video_name = 'output_6.avi'
directory_name = ''.join(video_name.split('.')[:-1])
parent_path = os.getcwd()
exact_path = os.path.join(parent_path, directory_name)
os.mkdir(exact_path)

cap = cv.VideoCapture(video_name)

count = 100000
while True:
	ret, frame = cap.read()
	if ret:
		cv.imshow("out", frame)

		key = cv.waitKey() & 0xFF
		if key == ord(" "):
			cv.imwrite(exact_path + '/image' + str(count) + '.jpg', frame)
			count = count + 1
		if key == ord("p"):
			pass

