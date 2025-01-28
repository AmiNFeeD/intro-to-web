import math
import random
import requests
import matplotlib.pyplot as plt
from flask import Flask
from datetime import datetime, timedelta
#math
radius = 5
area = math.pi * math.pow(radius, 2)
print(f"Area of the circle: {area}")
#random
names = ["Aluce", "Bob", "Charlie"]
winner = random.choice(names)
print(f"The winner is: {winner}")
#datetime
now = datetime.now()
print(f"Current time: {now}")

future_date = now + timedelta(days=7)
print(f"Date after 7 days: {future_date}")

#requests
response = requests.get("http://api.github.com")
print(response.status_code)
print(response.json())

#matplotlib

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Line graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, Flask!"
if __name__ == '__main__':
    app.run(debug=True)

