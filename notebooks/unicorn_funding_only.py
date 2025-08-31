import pandas as pd

# 路径配置
merged_file = "../data/merged_unicorn_funding_clean.csv"

output_long_only = "data/merged_unicorn_funding_clean_only.csv"
output_summary_only = "data/unicorn_funding_only.csv"

# 读取文件
merged = pd.read_csv(merged_file)

# 过滤有融资数据的公司（funding_round_id 不为空）
merged_only = merged[merged["funding_round_id"].notna() & (merged["funding_round_id"] != "")].copy()

# 输出有融资数据的表
merged_only.to_csv(output_long_only, index=False, encoding="utf-8-sig")

# 公司级别汇总
summary_only = merged_only.groupby(
    ["company", "company_clean", "founded_year", "country", "city", "industry"]
).agg(
    total_funding_usd=("raised_amount_usd", "sum"),
    funding_rounds=("funding_round_id", "count"),
    valuation_usd=("valuation_usd", "first"),
    joined_date=("joined_date", "first")
).reset_index()

# 输出公司级别表
summary_only.to_csv(output_summary_only, index=False, encoding="utf-8-sig")

# === Step 6: 打印样本 ===
print("\nmerged_unicorn_funding_clean_only.csv（融资事件）：")
print(merged_only.head(10))

print("\nunicorn_funding_only.csv（公司级别汇总）：")
print(summary_only.head(10))
