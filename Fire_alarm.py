import pygame



def start_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("schoolbell.wav")
    pygame.mixer.music.play(-1)


def stop_alarm():
    pygame.mixer.music.stop()


def get_smoke_level():
    try:
        level = int(input("\nEnter current smoke level (0-100): "))

        if 0 <= level <= 100:
            return level

        print("Please enter a value between 0 and 100.")
        return get_smoke_level()

    except ValueError:
        print("Numbers only.")
        return get_smoke_level()


def search_detector(detectors, location):
    for detector in detectors:
        if detector.location.lower() == location.lower():
            return detector
    return None

# Took inspiration from Hong Pengs Lesson on optimised bubble sort 
def sort_detectors(detectors):
    # The outer loop keeps track of how many full passes we make through the list.
    for i in range(len(detectors)):

        # We use a 'flag' to check if any swaps happen during this pass.
        # If no swaps happen, we know the list is completely sorted!
        flag = False

        # The inner loop compares side-by-side items.

        for j in range(1, len(detectors) - i):
            # Compare the current item (j) with the one right before it (j-1).
            # If the current one is smaller, they are in the wrong order.
            if detectors[j].smoke_level > detectors[j - 1].smoke_level:
            
            # If they are in the wrong order, swap them!
                
                detectors[j], detectors[j - 1] = (detectors[j - 1],detectors[j])
            # Once the swap is made we set the flag to True 
                flag = True
        # If no swaps were made, the list is sorted and we can exit early 
        if flag == False:
            return detectors
        # Once the list is sorted return it back.
    return detectors