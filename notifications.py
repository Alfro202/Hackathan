import time

def announce_fire():
    print("\nPA SYSTEM:")

    for _ in range(3):
        print("🔊 Fire! Fire! Fire! Please evacuate now!")
        time.sleep(1)


def notify_staff():
    print("\n📱 Notifications Sent To:")
    print("- Principal")
    print("- Teachers")
    print("- Security Personnel")
    print("- School Staff")


def alert_emergency_services():
    print("\n🚒 Emergency Services Alerted")
    print("Location and incident details sent.")