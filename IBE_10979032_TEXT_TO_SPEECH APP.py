import PySimpleGUI as samuel
import pyttsx3 as ibe

engine = ibe.init()
layout = [
    [samuel.InputText()],
    [samuel.Text('Enter text to speak:')],
    [samuel.Radio('Male', 'voice', default=True, key='MALE'), samuel.Radio('Female', 'voice', key='FEMALE')],
    [samuel.Button('Speak'), samuel.Button('Cancel')],
    
]


window = samuel.Window('Text to Speech', layout)


while True:
    event, values = window.read()
    if event == samuel.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Speak':
        
        text = values[0]
        
        if values['MALE']:
            voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
        else:
            voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        
        engine.setProperty('voice', voice)
        
        engine.say(text)
        engine.runAndWait()
        
        

# Close the window
window.close()
