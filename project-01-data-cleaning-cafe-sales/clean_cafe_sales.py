# ماژول پانداس برای پاک سازی و تمیز کردن دیتاست
import pandas as pd

# خواندن فایل دیتاست
data = pd.read_csv("dirty_cafe_sales.csv")

# در بیشتر ستون ها مقادیر نامعتبری وجود داشت آن ها رو با مقدار NA خود پانداس جایگزین کردم
data = data.replace(["ERROR", "UNKNOWN"], pd.NA)

# پانداس ستون‌های Quantity، Price Per Unit و Total Spent رو از نوع داده‌ی object تشخیص داده بود.
# با استفاده از دستور to_numeric اون مقدار ها رو به عدد تبدیل کردم
data["Quantity"] = pd.to_numeric(data["Quantity"])
data["Price Per Unit"] = pd.to_numeric(data["Price Per Unit"])
data["Total Spent"] = pd.to_numeric(data["Total Spent"])

# پانداس ستون Transaction Date رو از نوع داده ی object تشخیص داده بود
# ستون رو با استفاده از دستور to_datetime به نوع تاریخ در خود پانداس تبدیل کردم
data["Transaction Date"] = pd.to_datetime(data["Transaction Date"])

# مقادیر خالیه سه ستونه Item و Location و Payment Method رو نمیشه با استفاده از فرمول خاصی به دست آورد
# پس مقادیر خالی رو با استفاده از دستور mode (پرتکرارترین مقدار) به دست آوردم
data["Item"] = data["Item"].fillna(data["Item"].mode()[0])
data["Location"] = data["Location"].fillna(data["Location"].mode()[0])
data["Payment Method"] = data["Payment Method"].fillna(data["Payment Method"].mode()[0])

# بین این سه ستون یک رابطه ی ریاضی ساده وجود داشت
# Total Spent = Quantity * Price Per Unit
# Quantity = Total Spent / Price Per Unit
# Price Per Unit = Total Spent / Quantity
# با استفاده از همین رابطه مقادیر خالی رو پر کردم
data["Price Per Unit"] = data["Price Per Unit"].fillna(data["Total Spent"] / data["Quantity"])
data["Quantity"] = data["Quantity"].fillna(data["Total Spent"] / data["Price Per Unit"])
data["Total Spent"] = data["Total Spent"].fillna(data["Quantity"] * data["Price Per Unit"])

# اما نمیشه تمامی مقادیر خالی رو با استفاده از این فرمول به دست آورد
# دلیلش این هست که ما برای به دست آوردن یکی از مقادیر این سه ستون نیاز به حداقل دو مقدار رو داریم تا بتونیم مقدار سوم رو به دست بیاریم
# پس از آنجایی که نمی‌شد این مقادیر رو به دست آورد، آن‌ها رو حذف کردم
data = data.dropna(subset=["Price Per Unit", "Quantity", "Total Spent"])

# ستون Transaction Date سطر های خالی داشت
# در این پروژه چون تاریخ‌های گمشده قابل بازسازی نبودند، سطر های دارای تاریخ گمشده رو حذف کردم
data = data.dropna(subset=["Transaction Date"])

print(f"مقدار خالیه هر ستون: \n{data.isna().sum()}")
print("\n- - - - - - - - - - - - -\n")
print(f"بررسی نوع داده ها: \n{data.dtypes}")

# در نهایت یک دیتاست با تغییرات جدید ایجاد کردم
data.to_csv("clean_cafe_sales.csv", index=False)
