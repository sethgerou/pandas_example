import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Age","Rank","Value"],index=["Doug","Gina"])

print(df1)
print(df1.mean())
print(df1.mean().mean())

print(df1.Age.mean())

df2 = pandas.DataFrame([{"Name":"Doug","Age":35},{"Name":"Gina", "Age":"42"}])
print(df2)
