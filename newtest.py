import mp3play,time
data= r'pathname'
clip = mp3play.load(data)
clip.play()
time.sleep(20)
clip.stop()
