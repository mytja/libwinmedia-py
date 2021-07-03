import libwinmedia
import time

print("Initilizing LibWinMedia")
lwm = libwinmedia.LibWinMedia()

file = libwinmedia.MediaFile(r"\\VBOXSVR\libwinmedia-py\libwinmedia\Kalimba.mp3")
lwm.open(file)

print("Now playing")
lwm.player.play()

rate = lwm.player.getRate()
print("Rate: " + str(rate))

balance = lwm.player.getAudioBalance()
print("Audio balance: " + str(balance))

volume = lwm.player.getVolume()
print("Volume: " + str(volume))

time.sleep(5)

lwm.player.setVolume(80.0)
volume = lwm.player.getVolume()
print("Volume: " + str(volume))

#print("Media duration: " + str(lwm.media.getDuration()))

time.sleep(10)

print("Now pausing")
lwm.player.pause()
