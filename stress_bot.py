import time

def stress_bot():
    print("Hi! I'm your Stress Buddy 😊")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!\nLet's check how stressed you are lately.\n")

    sleep_hours = int(input("🛌 How many hours do you sleep on average? (0-10): "))
    screen_time = int(input("📱 How many hours of screen time daily? (0-15): "))
    stress_level = int(input("😥 Rate your stress level from 1 (low) to 10 (high): "))

    print("\nAnalyzing", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print("\n")

    if stress_level >= 7 or sleep_hours <= 5 or screen_time >= 10:
        print("🔥 You might be under **high stress**.")
        if sleep_hours <= 5:
            print("🛌 Try to get at least 7 hours of sleep.")
        if screen_time >= 10:
            print("📵 Reduce screen time with tech breaks.")
        print("💡 Tip: Try journaling, meditation, or talking to a friend.")
    elif stress_level >= 4:
        print("😐 You're in the **moderate stress** zone.")
        print("💡 Try planning your tasks and taking breaks between study sessions.")
    else:
        print("😎 You're pretty chill! Keep up the healthy habits.")

    print(f"\nThanks for chatting, {name}! Remember to take care of yourself 💖")

stress_bot()
