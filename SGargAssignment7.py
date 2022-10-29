import pandas as pd
import matplotlib.pyplot as plt


def get_csv(web_link):
    df = pd.read_csv(web_link)
    return df

df = get_csv("http://winterolympicsmedals.com/medals.csv")
print(df)

plt.scatter(df["City"], df['Event'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('City')
plt.ylabel('Event')

plt.show()