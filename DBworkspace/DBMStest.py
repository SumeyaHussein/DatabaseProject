#vsc file to run after installing database in envrionment
import pandas as pd

path = pd.read_csv("spotify-2023.csv", encoding='ISO-8859-1')
print(path.head(5)) #modify this line for desired output
