import cv2
import os
target_path = '/home/zehao/Downloads/yolo/data/HXD3C/cab1040/2'

frame_num = 0
for file in os.listdir(target_path):
    print file
    if os.path.splitext(file)[1] == ".mp4":
        if not os.path.exists(target_path + '/' + os.path.splitext(file)[0]):
            os.mkdir(target_path + '/' + os.path.splitext(file)[0])
        try:
            video_capture = cv2.VideoCapture(target_path + '/' + file)
        except Exception, e:
            print Exception, ":", e
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            frame_name = os.path.splitext(file)[0] + '-' + str(frame_num) + '.jpg'
            if frame_num % 10 == 0:
                cv2.imwrite(target_path + '/' + os.path.splitext(file)[0] + '/' + frame_name, frame)
            frame_num += 1
