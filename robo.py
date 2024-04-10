import os
import subprocess

def speak(text):
    if os.name == 'posix':  # For Unix/Linux/MacOS
        subprocess.call(['say', text])
    elif os.name == 'nt':  # For Windows
        subprocess.call(['PowerShell', '-Command', f'[Console]::Beep(500, 300); Add-Type -AssemblyName System.Speech; $synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak("{text}")'])
    else:
        print("Sorry, your operating system is not supported.")

def main():
    print("Welcome to Robo Speaker!")
    while True:
        user_input = input("Enter text to be pronounced (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            speak("Goodbye! Thank you for using Robo Speaker.")
            break
        else:
            speak(user_input)

if __name__ == "__main__":
    main()

