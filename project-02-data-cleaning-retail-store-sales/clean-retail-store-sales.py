# ماژول پانداس برای خواندن و تمیز کردن دیتاست
import pandas as pd

# خواندن فایل دیتاست
data = pd.read_csv("retail_store_sales.csv")

# پر کردن مقادیر خالی ستون Item با استفاده از روش mode(پر تکرار ترین مقدار)
data["Item"] = data["Item"].fillna(data["Item"].mode()[0])

# از همین روش mode برای ستون Discount Applied هم استفاده کردم
data["Discount Applied"] = data["Discount Applied"].fillna(data["Discount Applied"].mode()[0])

# ستون Discount Applied که شامل True یا False است رو با استفاده از astype به 0 و 1 تبدیل کردم
data["Discount Applied"] = data["Discount Applied"].astype(int)

# برخی مقادیر خالی در ستون های Quantity و Total Spent و Price Per Unit که قابل باز سازی بودن رو 
# با استفاده از رابطه ی ریاضی به دست آوردم
# Total Spent = Quantity * Price Per Unit
# Price Per Unit = Total Spent / Quantity
# Quantity = Total Spent / Price Per Unit
data["Quantity"] = data["Quantity"].fillna(data["Total Spent"] / data["Price Per Unit"])
data["Total Spent"] = data["Total Spent"].fillna(data["Quantity"] * data["Price Per Unit"])
data["Price Per Unit"] = data["Price Per Unit"].fillna(data["Total Spent"] / data["Quantity"])

# پانداس ستون Transaction Date رو از نوع object تشخیص داده بود
# من ستون رو به فرمت تاریخ تبدیل کردم
data["Transaction Date"] = pd.to_datetime(data["Transaction Date"])

# از روش های مختلفی برای به دست آوردن مقادیر ستون های Quantity  و Total Spent که با استفاده از رابطه ریاضی قابل باز سازی نبودن استفاده کردم
# اما رابطه ی خاصی بین این دو ستون و ستون های دیگه پیدا نکردم
# چون اطلاعات کافی برای بازسازی دقیق آن‌ها وجود نداشت، آن ردیف‌ها را حذف کردم
data = data.dropna(subset=["Total Spent"])
data = data.dropna(subset=["Quantity"])

# در نهایت هم یک دیتاست با تغییرات جدید ساختم
data.to_csv("clean_retail_store_sales.csv", index=False)
