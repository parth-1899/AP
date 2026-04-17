import pandas as pd

n = ["a","b","c","d","e"]
m = [90,80,85,70,60]

df = pd.DataFrame({"n":n,"m":m})

print(df)

print(df.head())
print(df.tail())

print(df.shape)
print(df.columns)

print(df["m"])
print(df.loc[0])
print(df.iloc[1])

print("sum =",df["m"].sum())
print("mean =",df["m"].mean())
print("max =",df["m"].max())
print("min =",df["m"].min())

df["g"] = ["A","B","A","C","B"]
print(df)

df = df.drop("g",axis=1)
print(df)

df["m"] = df["m"].astype(float)

print(df.describe())

print(df.sort_values("m"))

print(df.isnull())

df["m"] = df["m"].fillna(0)

print(df)
