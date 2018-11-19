import cv2
import sys
import getopt

#src url: https://gist.githubusercontent.com/JacopoDaeli/1788da2cef6217549a440ee186d47f68/raw/40f021906ba105d7d93b9a113f3af23e9d07ac73/video_to_frames.py

def video_to_frames(video_filename,output_dir):
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
                resized_img = cv2.resize(crop_img, (128, 128)) 
                cv2.imwrite(output_dir+"/frame%05d.jpg" % frame_id, resized_img)
                frame_id+=1
            success, image = cap.read()
            count += 1
    return 0

def usage():
    print("Usage: video2frames -f video -o output_dir\n")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:o:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(1)
    filename=""
    output_dir=""
    for o,value in opts:
      if o == "-f":
          filename=value
      elif o == "-o":
          output_dir=value
    video_to_frames(filename,output_dir)

if __name__ == "__main__":
    main()
