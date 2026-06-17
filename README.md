# Title: SMART FIRE DETECTION SYSTEM 
## Description: Sometimes in school the fire alarm goes off randomly. It could be a false alarm or a real alarm. But to verify that I have created this programme. 
First, my code mimics the fire alarm setting off in the school. The smoke detectors in each location instantly sends the respective smoke level to the main control panel.
The main control panel looks throught the smoke level in each room and manually inputs the detected smoke level to the fire alarm system. 
If the smoke level is below the threshold the fire alarm detects it to be a false alarm and force stops the alarm.
However, if the smoke level is above the smoke threshlod the fire alarm deems it to be a true postive and continues to ring and emergency services are informed. 
This enusures that the main control panel can instantly take action whether the fire is real or not instead of spending time investigating and allocation manpower to
reset the fire alarm.

## Features: 
### 1. Plays the fire alarm sound
### 2. Sorts the smoke detectors by smoke level
### 3. Alerts Emergency services if confirmed real fire, if not force stops the alarm.

## How to Run: 
Install the following dependency: 
pygame-ce==2.5.7

Activate environment: .venv\Scripts\Activate.ps1

Run the code with python main.py 

## File structure: 
```text
├── .venv/
├── README.md
├── Fire_alarm.py
├── main.py
├── notifications.py
├── requirements.txt
├── schoolbell.wav
└── smoke_detectors.py
```

## Reflection:
### The hardest part was inputing the sound file into the code. I had spent significant amount of time learning about pygame and getting the alarm sound to work. I referred to tutorials onilne to learn about pygame to add the sound file. 
### If I had two more weeks i would have made use of APIs to fetch real time data instead of hard coded values for experimentation.