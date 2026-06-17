import pygame
import time

import Fire_alarm
from smoke_detectors import SmokeDetector

from notifications import (
    announce_fire,
    notify_staff,
    alert_emergency_services
)

pygame.init()
pygame.mixer.init()

# Create detector objects
detectors = [
    SmokeDetector("Science Lab", 82),   
    SmokeDetector("Library", 21),
    SmokeDetector("Hall", 40),
    SmokeDetector("Classroom 1", 12)
]

print("=" * 50)
print("SMART FIRE DETECTION SYSTEM")
print("=" * 50)

# Sorting demonstration
print("\nDetectors Sorted By Smoke Level:")

sorted_detectors = Fire_alarm.sort_detectors(detectors)

for detector in sorted_detectors:
    print(f"{detector.location} --> "f"{detector.smoke_level}")

# Searching demonstration
location = input("\nEnter detector location: ")

detector = Fire_alarm.search_detector(
    detectors,
    location)

if detector is None:

    print("\n❌ Detector Not Found")

    pygame.quit()
    quit()

print(f"\n✅ Detector Found: "f"{detector.location}")

# Alarm rings for 3 seconds
print("\n🚨 FIRE ALARM ACTIVATED 🚨")

Fire_alarm.start_alarm()
time.sleep(3)
Fire_alarm.stop_alarm()

# Recursion demonstration
detector.smoke_level = Fire_alarm.get_smoke_level()
if detector.is_fire():
    print("\n🔥 FIRE CONFIRMED 🔥")
    print(f"📍 Location: "f"{detector.location}")
    print("🗺 Safe Evacuation Route Displayed")

    Fire_alarm.start_alarm()

    announce_fire()
    notify_staff()
    alert_emergency_services()

    input("\nPress ENTER to stop alarm...")

    Fire_alarm.stop_alarm()

else:
    print("\n✅ FALSE ALARM DETECTED")
    print("Smoke level below threshold.")

    Fire_alarm.stop_alarm()

pygame.quit()




'''
Sometimes in school the firealarm goes off randomly. It could be a false alarm or a real alarm. But to verify that I have created this programme. 
First, my code mimics the fire alarm setting off in the school. The smoke detectors in each location instantly sends the respective smoke level to the main control panel.
The main control panel looks throught the smoke level in each room and manually inputs the detected smoke level to the fire alarm system. 
If the smoke level is below the threshold the fire alarm detects it to be a false alarm and force stops the alarm.
However, if the smoke level is above the smoke threshlod the fire alarm deems it to be a true postive and continues to ring and emergency services are informed. 
This enusures that the main control panel can instantly take action whether the fire is real or not instead of spending time investigating and allocation manpower to
reset the fire alarm. 
'''