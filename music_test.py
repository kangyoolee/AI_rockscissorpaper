from playsound import playsound
import keyboard

if keyboard.is_pressed("q"):
    playsound( "가위바위보.mp3" )