import pandas as pd

soldiers = [
    {'Name': 'Zoey Dolivo', 'Health': 1388, 'Strength': 92, 'Stealth': 1, 'Speed': 58, 'Accuracy': 78},
    {'Name': 'Stella Marudas', 'Health': 1107, 'Strength': 54, 'Stealth': 1, 'Speed': 80, 'Accuracy': 80},
    {'Name': 'Mia Delatejera', 'Health': 1052, 'Strength': 92, 'Stealth': 7, 'Speed': 41, 'Accuracy': 19},
    {'Name': 'Wyat Kentala', 'Health': 1791, 'Strength': 24, 'Stealth': 3, 'Speed': 73, 'Accuracy': 89},
    {'Name': 'Andrew Usoro', 'Health': 1813, 'Strength': 24, 'Stealth': 9, 'Speed': 89, 'Accuracy': 31}
    ]
df = pd.DataFrame(soldiers)
df.to_csv("sodurid.csv")

soldiers_data = pd.read_csv("sodurid.csv")


print(soldiers_data.loc[4,:])
