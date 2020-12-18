#Convert them into VP8, VP9, h265 & AV1. You
#can use the script that allows you to transform, or
#create a new script.
import os
import subprocess


input1 = "bbb_10sec_video_160_120"
input2 = "bbb_10sec_video_360_240"
input3 = "bbb_10sec_video_640_480"
input4 = "bbb_10sec_video_1280_720"

#exercise 1

# VP8 160_120
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis vp8_bbb_10sec_video_160_120.webm', shell=True)
# VP8 360_240
subprocess.call('ffmpeg -i '+input2+'.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis vp8_bbb_10sec_video_360_240.webm', shell=True)
# VP8 640_480
subprocess.call('ffmpeg -i '+input3+'.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis vp8_bbb_10sec_video_640_480.webm', shell=True)
# VP8 1280_720
subprocess.call('ffmpeg -i '+input3+'.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis vp8_bbb_10sec_video_1280_720.webm', shell=True)


# VP9 160_120
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 vp9_bbb_10sec_video_160_120.webm', shell=True)
# VP9 360_240
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 vp9_bbb_10sec_video_360_240.webm', shell=True)
# VP9 640_480
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 vp9_bbb_10sec_video_640_480.webm', shell=True)
# VP9 1280_720
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 vp9_bbb_10sec_video_1280_720.webm', shell=True)


# h265 160_120
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libx265 -crf 28 -c:a aac -b:a 128k h265_bbb_10sec_video_160_120.mp4',shell=True)
# h265 360_240
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libx265 -crf 28 -c:a aac -b:a 128k h265_bbb_10sec_video_360_240.mp4',shell=True)
# h265 640_480
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libx265 -crf 28 -c:a aac -b:a 128k h265_bbb_10sec_video_640_480.mp4',shell=True)
# h265 1280_720
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libx265 -crf 28 -c:a aac -b:a 128k h265_bbb_10sec_video_1280_720.mp4',shell=True)



# AV1 160_120
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental av1_bbb_10sec_video_160_120.mkv',shell=True)
# AV1 360_240
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental av1_bbb_10sec_video_360_240.mkv',shell=True)
# AV1 640_480
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental av1_bbb_10sec_video_640_480.mkv',shell=True)
# AV1 1280_720
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental av1_bbb_10sec_video_1280_720.mkv',shell=True)


#exercise 2
def allvideos(resolution):
    video1 = "vp8_bbb_10sec_video_" + resolution +".webm"
    video2 = "vp9_bbb_10sec_video_" + resolution + ".webm"
    video3 = "h265_bbb_10sec_video_" + resolution + ".webm"
    video4 = "av1_bbb_10sec_video_" + resolution + ".webm"

    subprocess.call('ffmpeg -i ' +video1+' -i ' +video2+' -i ' +video3+' -i ' +video4+' -filter_complex "nullsrc=size=1280x720 [base]; [0:v] setpts=PTS-STARTPTS,'
                                                                                      'scale=640x360 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=640x360 [upperright]; [2:v] settpts=PTS-STARTPTS, scale=640x360 [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=640x360 [lowerright]; [base][upperleft]'
                                                                                      'overlay=shortest=1 [tmp1];[tmp1][upperright] overlay=shortest=1:x=640 [tmp2];[tmp2][lowerleft] overlay=shortest=1:y=360 [tmp3];[tmp3][lowerright] overlay=shortest=1:x=640:y=360" -c:v libx265 allvideos_'+resolution+'.mp4',shell=True)
    return 'Done'

#example : allvideos("160_120")

#exercise 3
#create a live streaming, broadcast it into an IP address (locally) and open the IP or URL inside VLC Media Player

#ffmpeg -i bbb_10sec_video_640_480.mp4
#-preset ultrafast -vcodec:v libx264 -tune zerolatency \
#-b:v 900k -f mpegts udp://127.0.0.1:2222

#'preset' specifies the preset for matching streams
#vcodec: set the video codec
# -b: bitrate
#-f : force output file format

#to watch the stream, in a new terminal:
# ffplay udp:udp://127.0.0.1:2222