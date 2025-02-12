import matplotlib.pyplot as plt
import seaborn as sns

def plot_calories_distribution(df):
    plt.figure(figsize=(10, 5))
    sns.histplot(df["Calories"], bins=30, kde=True, color="blue")
    plt.title("Distribution of Calories Burned")
    plt.xlabel("Calories")
    plt.ylabel("Count")
    plt.show()
def ScatterPlot(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df["Duration"], y=df["Calories"], hue=df["Gender"], palette="coolwarm")
    plt.title("Exercise Duration vs Calories Burned")
    plt.xlabel("Exercise Duration (min)")
    plt.ylabel("Calories Burned")
    plt.show()


def CountPlot(df):
    plt.figure(figsize=(6, 5))
    sns.countplot(x=df["Gender"], palette="coolwarm")
    plt.title("Gender Distribution")
    plt.xticks(ticks=[0, 1], labels=["Female", "Male"])
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()


def BoxPlot(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(y=df["Calories"], color="red")
    plt.title("Box Plot of Calories Burned")
    plt.ylabel("Calories")
    plt.show()

