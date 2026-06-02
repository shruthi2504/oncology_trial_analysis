import pandas as pd

# load data
df = pd.read_excel("data/raw_data.xlsx")

print(df.head())
print(df.info())

print("\nNull values:")
print(df.isnull().sum())

print("\nUnique values:")
print(df.nunique())

# clean column names
df.columns = df.columns.str.lower().str.strip()

# clean recruitment status
df["recruitment_status"] = (
    df["recruitment_status"]
    .astype(str)
    .str.lower()
    .str.strip()
)

# clean phase
df["phase"] = df["phase"].astype(str).str.extract(r'(\d)')

# dates
df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")
df["completion_date"] = pd.to_datetime(df["completion_date"], errors="coerce")

df["start_year"] = df["start_date"].dt.year
df["duration"] = (df["completion_date"] - df["start_date"]).dt.days

# success definition
def get_success(status):
    if status == "completed":
        return 1
    else:
        return 0

df["success"] = df["recruitment_status"].apply(get_success)

print("\nSuccess Rate By Phase")
print(df.groupby("phase")["success"].mean())

print("\nSuccess Rate By Indication")
print(df.groupby("indications")["success"].mean())

print("\nSuccess Rate By Start Year")
print(df.groupby("start_year")["success"].mean())

print("\nDuplicate Trial IDs:")
print(df["nct_id"].duplicated().sum())

print("\nRecruitment Status Distribution:")
print(df["recruitment_status"].value_counts())

# save output
df.to_csv("cleaned_data.csv", index=False)

print("\nDone. Output saved as cleaned_data.csv")