import cv2
import sys

#src url: https://gist.githubusercontent.com/JacopoDaeli/1788da2cef6217549a440ee186d47f68/raw/40f021906ba105d7d93b9a113f3af23e9d07ac73/video_to_frames.py

def video_to_frames(video_filename):
    """Extract frames from video"""
    cap = cv2.VideoCapture(video_filename)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    vid_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    vid_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    vid_fps = int(cap.get(cv2.CAP_PROP_FPS))
    print("vid_res=%d x %d, fps=%d\n" % (vid_width, vid_height,vid_fps))
    crop_width=int(vid_width/128)*128
    crop_height=int(vid_height/128)*128
    grab_step=int(vid_fps/2)
    if cap.isOpened() and video_length > 0:
        count = 0
        frame_id=0
        success, image = cap.read()
        while success and frame_id <= 9999:
            if count%grab_step==0:
                crop_img = image[0:crop_width, 0:crop_height]
                cv2.imwrite("frame%05d.jpg" % frame_id, crop_img)
                frame_id+=1
            success, image = cap.read()
            count += 1
    return frames


if len(sys.argv) < 2:
	print("Usage:"+str(sys.argv[0])+" video-file\n");
	sys.exit
video_to_frames(sys.argv[1])

