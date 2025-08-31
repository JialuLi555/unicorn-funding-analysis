import pandas as pd

# 路径配置
FUNDING_FILE = r"../data/dataset/funding_rounds.csv"
OBJECTS_FILE = r"../data/dataset/objects.csv"
OUTPUT_FILE = r"../data/clean_funding_data_final.csv"

# 读取数据
funding = pd.read_csv(FUNDING_FILE)
objects = pd.read_csv(OBJECTS_FILE)

# 只保留需要的字段
funding_sel = funding[[
    "funding_round_id", "object_id", "funded_at",
    "funding_round_type", "raised_amount_usd"
]]

objects_sel = objects[[
    "id", "name", "normalized_name", "founded_at",
    "country_code", "category_code"
]].rename(columns={"id": "object_id"})

# 合并
df = funding_sel.merge(objects_sel, on="object_id", how="left")

# 生成 clean_name
df["clean_name"] = df["normalized_name"].str.lower().str.replace(r"[^a-z0-9]", "", regex=True)

# 日期格式统一
df["funded_at"] = pd.to_datetime(df["funded_at"], errors="coerce").dt.strftime("%Y/%-m/%-d")
df["founded_at"] = pd.to_datetime(df["founded_at"], errors="coerce").dt.strftime("%Y/%-m/%-d")

# 金额：取整数
df["raised_amount_usd"] = df["raised_amount_usd"].fillna(0).astype(int)

# 排列顺序
df_final = df[[
    "funding_round_id", "object_id", "name", "clean_name",
    "founded_at", "country_code", "funded_at",
    "funding_round_type", "raised_amount_usd", "category_code"
]]

# 导出 CSV
df_final.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print(f"清理完成,输出文件: {OUTPUT_FILE}")
