import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\\Users\\ASUS\\Desktop\\EcommercePurchases.csv")
print("Top 10 rows:")
print(df.head(10))

print("\nBottom 10 rows:")
print(df.tail(10))

# Checking if any null values
print(df.info())

#Checking the datatypes for each column
print(df.dtypes)

#finding highest, lowest purchase prices and average purchase price
highest_pp = df['Purchase Price'].max()
print('Highest purchase price is ' + str(highest_pp))
lowest_pp = df['Purchase Price'].min()
print('Lowest Purchase Price is ' + str(lowest_pp))
avg_pp = df['Purchase Price'].mean()
print('Average Purchase Price is ' + str(avg_pp))

# People with French as their language, also people with engineer in their job title
french_people = df[df['Language'] == 'fr']
print(french_people)
engineer_job = df[df['Job'].str.contains('engineer', case=False)]
print(engineer_job)

#The analysis involves finding the email of a person with a specific IP address, 
email_ip= df[df['IP Address'] == '213.203.143.215'] ['Email']
print(email_ip)
# identifying individuals with Mastercard as their credit card provider who made purchases above $50, 
Master_50 = df[(df['CC Provider'] == 'Mastercard') & (df['Purchase Price'] > 50)]
print(Master_50)

# finding the email of a person with a specific credit card number.
credit = df[df['Credit Card'] == 675957666125] ['Email']
print(credit)



