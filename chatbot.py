import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier

# Sample training data
data = {
    'sleep_hours': [8, 6, 5, 7, 4, 9, 6, 5, 7],
    'screen_time': [4, 10, 12, 5, 14, 3, 9, 13, 6],
    'study_hours': [4, 2, 1, 3, 1, 5, 2, 1, 3],
    'exercise_minutes': [30, 15, 10, 25, 5, 40, 15, 10, 20],
    'stress_level': [3.2, 7.8, 8.5, 4.0, 9.0, 2.5, 6.8, 8.2, 4.5],
    'time_management': ['Good', 'Poor', 'Poor', 'Good', 'Poor', 'Good', 'Poor', 'Poor', 'Good']
}

df = pd.DataFrame(data)

# Train the regression and classifier models
X = df[['sleep_hours', 'screen_time', 'study_hours', 'exercise_minutes']]
y_stress = df['stress_level']
regressor = LinearRegression()
regressor.fit(X, y_stress)

y_time_mgmt = df['time_management'].map({'Poor': 0, 'Good': 1})
clf = RandomForestClassifier()
clf.fit(X, y_time_mgmt)

# 🌟 Interactive Chatbot Begins
print("Bot: Hey! I'm your wellness buddy. Let's check how you're doing. 😊")

sleep_hours = float(input("Bot: How many hours do you sleep on average?\nUser: "))
screen_time = float(input("Bot: And how much time do you spend on screens daily (in hours)?\nUser: "))
study_hours = float(input("Bot: Cool! How many hours do you study daily?\nUser: "))
exercise_minutes = float(input("Bot: Do you exercise? If yes, how many minutes a day?\nUser: "))

# Prepare input for prediction
input_data = pd.DataFrame([{
    'sleep_hours': sleep_hours,
    'screen_time': screen_time,
    'study_hours': study_hours,
    'exercise_minutes': exercise_minutes
}])

# Make predictions
predicted_stress = regressor.predict(input_data)[0]
predicted_mgmt = clf.predict(input_data)[0]

# Interpret results
stress_category = 'High' if predicted_stress >= 6 else 'Low'
time_management = 'Good' if predicted_mgmt >=5 else 'Poor'

# Final response
print("\nBot: Based on your inputs...")
print(f"→ Your Predicted Stress Level: {predicted_stress:.2f} / 10")
print(f"→ Stress Category: {stress_category}")
print(f"→ Time Management: {time_management}")

print("\n💡 Suggestions:")
if stress_category == 'High':
    print("- Try mindfulness, short walks, or music breaks to reduce stress.")
else:
    print("- You're managing your stress well! Keep it up!")

if time_management == 'Poor':
    print("- Make a to-do list, prioritize tasks, and avoid long screen hours.")
else:
    print("- Great time management! Maybe share your secret? 😄")

print("\nBot: Stay awesome and take care of yourself! 🌱 You've got this! 💖")
