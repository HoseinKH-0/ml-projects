# ماژول لازم برای خواندن و تمیز کاری دیتاست
import pandas as pd

# خواندن فایل دیتاست
data = pd.read_csv("customers.csv")

# پر کردن مقادیر خالی ستون age با استفاده از میانگین داده ها
data["age"] = data["age"].fillna(data["age"].mean()).astype(int)

# پر کردن مقادیر خالی ستون state با استفاده از روش mode(پر تکرار ترین مقدار)
data["state"] = data["state"].fillna(data["state"].mode()[0])

# با استفاده از تابع map ستون مقادیر ستون gender را به عدد تبدیل کردیم
# (Male = 1, Female = 0)
data["gender"] = data["gender"].map({"Male": 1, "Female": 0})

# مقادیر ستون subscribe هم با تابع map تغییر دادیم
# (Yes = 1, No = 0)
data["subscribe"] = data["subscribe"].map({"Yes": 1, "No": 0})

# پانداس نوع داده ستون signup_date رو object تشخیص داده بود
# با استفاده از تابع to_datetime نوع داده رو به تاریخ تغییر دادم
data["signup_date"] = pd.to_datetime(data["signup_date"])

# با استفاده از تابع drop_duplicates ردیف های تکراری دیتاست را حذف کردم
data = data.drop_duplicates()

print("-------------------")
print("اطلاعات دیتاست:")
print(data.info())
print("-------------------")
print(f"تعداد ردیف های تکراری در دیتاست: {data.duplicated().sum()}")
print("-------------------")
print("تعداد مقادیر گمشده یا خالی در دیتاست:")
print(data.isna().sum())
print("-------------------")

# در نهایت یک دیتاست با تغییرات جدید ایجاد کردم
data.to_csv("clean_customers.csv", index=False)
