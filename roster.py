#https://goheels.com/sports/mens-basketball/roster
import pandas as pd


player = {"Last Name": ["Bacot", "Davis", "Cadeau","Trimble", "High","Ryan","Wojcik","Washington","Lebo","Okonkwo"],
          "First Name": ["Armando", "RJ","Elliot","Seth", "Zayden","Cormac","Paxson","Jalen","Creighton","James"],
          "height": [83,72,73,83,80,76,78,80,72,79],
          "weight": [240,180,180,195,225,195,195,230,180,240]}
data = pd.DataFrame(player)
print(player)

# bmi = weight in kg/height in meters squared
data["bmi"] = round((data["weight"]/2.205)/((data["height"]/39.37)**2), 2)

print(data)

data.to_csv("bmi.csv")
