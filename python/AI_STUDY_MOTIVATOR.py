"""
AI Study Motivator
-------------------
This program motivates students with random quotes, study tips, and reminders.
Perfect for coding students, Hacktoberfest contributors, and interview preppers!
"""

import random
import datetime
import time

morning_quotes = [
    "Rise & grind! Every day is a new chance to be better.",
    "Good morning! Code, learn, grow.",
    "Don't stop until you're proud!",
]

afternoon_quotes = [
    "Keep pushing! Great things take time.",
    "One bug at a time. You're doing great!",
    "Stay consistent — success will follow.",
]

night_quotes = [
    "Night mode ON, excuses OFF.",
    "You are one step closer to your goals!",
    "Success = Practice + Consistency + Patience.",
]

study_tips = [
    "📌 Tip: Study 50 mins, break 10 mins (Pomodoro).",
    "📌 Tip: Write code every day, even small programs.",
    "📌 Tip: Don't memorize, understand the logic.",
]

hydration_reminders = [
    "💧 Drink water! Hydrated brain performs better.",
    "🥤 Take a sip! Productivity booster activated!",
]

def get_time_based_message():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return random.choice(morning_quotes)
    elif current_hour < 18:
        return random.choice(afternoon_quotes)
    else:
        return random.choice(night_quotes)

def motivator():
    while True:
        print("\n✨ AI STUDY MOTIVATOR ✨")
        print(get_time_based_message())
        print(random.choice(study_tips))
        print(random.choice(hydration_reminders))
        print("\n🚀 Keep going, future engineer!\n")

        time.sleep(20)  # runs every 20 seconds (you can change this)

if __name__ == "__main__":
    motivator()
