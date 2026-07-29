import pandas as pd
# STEP 1: Read CSV File
df = pd.read_csv(r"C:\Users\huree\OneDrive\Desktop\python\class12\Beskilled_Internship\data.csv")

print("========== Original Dataset ==========")
print(df)

# STEP 2: Display First 5 Rows
print("\n========== First 5 Rows ==========")
print(df.head())

# STEP 3: Display Last 5 Rows
print("\n========== Last 5 Rows ==========")
print(df.tail())

# STEP 4: Dataset Information
print("\n========== Dataset Information ==========")
df.info()

# STEP 5: Dataset Shape
print("\n========== Shape ==========")
print(df.shape)

# STEP 6: Column Names
print("\n========== Columns ==========")
print(df.columns)

# STEP 7: Statistical Summary
print("\n========== Statistics ==========")
print(df.describe())

# STEP 8: Check Missing Values
print("\n========== Missing Values Before Cleaning ==========")
print(df.isnull().sum())

# STEP 9: Fill Missing Calories
df["Calories"] = df["Calories"].fillna(df["Calories"].mean())

# STEP 10: Fill Missing Date
df["Date"] = df["Date"].ffill()

# STEP 11: Check Missing Values Again
print("\n========== Missing Values After Cleaning ==========")
print(df.isnull().sum())

# STEP 12: Check Duplicate Rows
print("\n========== Duplicate Rows ==========")
print(df.duplicated())

print("\nTotal Duplicate Rows:")
print(df.duplicated().sum())

# STEP 13: Remove Duplicate Rows
df.drop_duplicates(inplace=True)

print("\nDuplicates After Removing:")
print(df.duplicated().sum())

# STEP 14: Replace Outlier
# Duration greater than 120 becomes 120
df.loc[df["Duration"] > 120, "Duration"] = 120

print("\n========== Dataset After Removing Outlier ==========")
print(df)

# STEP 15: Filter Rows
# Duration greater than 60

print("\n========== Duration > 60 ==========")
print(df[df["Duration"] > 60])

# STEP 16: Filter Calories Greater Than 300
print("\n========== Calories > 300 ==========")
print(df[df["Calories"] > 300])

# STEP 17: Create New Column
df["Intensity"] = df["Pulse"].apply(
    lambda x: "High" if x > 100 else "Normal"
)

print("\n========== Intensity Column ==========")
print(df)

# STEP 18: Create Another Column
df["Pulse_Difference"] = df["Maxpulse"] - df["Pulse"]

print("\n========== Pulse Difference ==========")
print(df)
# STEP 19: Convert Date to Datetime
# Remove quotes
df["Date"] = df["Date"].astype(str).str.replace("'", "", regex=False)

# Fix the row with 20201226
df.loc[df["Date"] == "20201226", "Date"] = "2020/12/26"

# Convert to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%Y/%m/%d")

print(df.dtypes)
# STEP 20: Save Cleaned Dataset

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully as cleaned_data.csv")

import matplotlib.pyplot as plt

#Bar chart for Calories
df["Calories"].head(10).plot(kind="bar")

plt.title("Calories Burned")
plt.xlabel("Workout")
plt.ylabel("Calories")

plt.show()

#line chart for Pulse
plt.plot(df["Pulse"])

plt.title("Pulse Trend")
plt.xlabel("Workout")
plt.ylabel("Pulse")

plt.show()

#Histogram for Calories
plt.hist(df["Calories"])

plt.title("Calories Distribution")
plt.xlabel("Calories")
plt.ylabel("Frequency")

plt.show()

import seaborn as sns

sns.scatterplot(data=df, x="Pulse", y="Calories")

plt.title("Pulse vs Calories")

plt.show()

# Save the cleaned dataset
df.to_csv(r"C:\Users\huree\OneDrive\Desktop\Beskilled\Python-Data-Assignment\cleaned_data.csv", index=False)

print("Cleaned data saved successfully!")