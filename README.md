# S3
Seminar3
# Exercise 1, CONVERSIONS

To convert the videos I use
# VP8 (undefined resolution)
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis vp8_bbb_10sec_video_resolution.webm', shell=True)

we can see that the resulting output is a .webm file belonging to a library 'libvorbis' and these are the parameters to transform the file to a VP8 codec.

# VP9 (undefined resolution)
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 vp9_bbb_10sec_video_resolution.webm', shell=True)

.webm file too, with these parameters

# h265 (undefined resolution)
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libx265 -crf 28 -c:a aac -b:a 128k h265_bbb_10sec_video_resolution.mp4',shell=True)

this is .mp4 output but belonging to a library libx265 with these parameters

# AV1 (undefined resolution)
subprocess.call('ffmpeg -i '+input1+'.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental av1_bbb_10sec_video_160_120.mkv',shell=True)

.mkv file at the output, belonging to a libaom-av1 library with these parameters.


# Exercise 2, 4 Videos in 1:
 I created a function that selects the concrete resolution of the previous outputs and shows us 4 videos in one.
 We could see the bitrates using ffprobe
 
1280x720
AV1: 944 kb/s
VP9: 1279 kb/s
H265: 767 kb/s
VP8: 533 kb/s

640x480
AV1: 593 kb/s
VP9: 761 kb/s
H265: 564 kb/s
VP8: 493 kb/s

360x240:
AV1: 408 kb/s
VP9: 474 kb/s
H265: 454 kb/s
VP8: 419 kb/s

160x120:
AV1: 308 kb/s
VP9: 339 kb/s
H265: 397 kb/s
VP8: 350 kb/s

Some conclusions:
- For lower resolutions, AV1 has less bitrate. For larger resolutions, VP8 has less bitrate but also less quality.
- The parameters used may not be the most efficient ones.
- AV1 can sabe about 30% bitrate compared to VP9 and h265, and about 50% h264.
- VP9 seems better, in quality terms, than h265. VP8 has the worst resolution quality of the 4 codecs.



# Exercise 3, live streaming: 
As long as I've seen on the internet, to create a live streaming I need to:
- broadcast it into an IP address (locally) and open the IP or URL inside VLC Media Player

I could use ffmpeg command in order to create a local streaming device.
ffmpeg -i bbb_10sec_video_640_480.mp4 -preset ultrafast -vcodec:v libx264 -tune zerolatency \ -b:v 900k -f mpegts udp://127.0.0.1:2222

-To watch the stream, we could use ffplay in a new terminal

ffplay udp://127.0.0.1:2222

