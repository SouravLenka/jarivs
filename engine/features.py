from playsound import playsound
import eel
# playing assistant sound functions
@eel.expose
def playAssistantSound():
    music_dir ="www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)