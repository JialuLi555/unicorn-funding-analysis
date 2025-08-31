import pandas as pd
import numpy as np

# 文件路径
unicorn_file = "../data/unicorn_aux_final_dedup_date.csv"
funding_file = "../data/clean_funding_data_final.csv"

output_long = "data/merged_unicorn_funding_clean.csv"
output_summary = "data/unicorn_funding_summary.csv"

# === Step 1: 读取数据 ===
unicorns = pd.read_csv(unicorn_file)
funding = pd.read_csv(funding_file)

# === Step 2: 预处理 & 合并 ===
funding = funding.rename(
    columns={"clean_name": "company_clean"}
)

# 确保 company_clean 对齐
unicorns["company_clean"] = unicorns["company_clean"].astype(str).str.lower()
funding["company_clean"] = funding["company_clean"].astype(str).str.lower()

# 合并：一家公司可能有多条融资记录
merged = unicorns.merge(
    funding[[
        "funding_round_id", "object_id", "company_clean",
        "founded_at", "funded_at", "funding_round_type", "raised_amount_usd"
    ]],
    on="company_clean",
    how="left"
)

# === Step 3: 补全 founded_year ===
merged["founded_at"] = pd.to_datetime(merged["founded_at"], errors="coerce")
merged["founded_at_year"] = merged["founded_at"].dt.year

# 如果 unicorn 表里 founded_year 为空，则用 founded_at_year 填补
merged["founded_year"] = merged["founded_year"].fillna(merged["founded_at_year"])
merged = merged.drop(columns=["founded_at", "founded_at_year"])

# === Step 4: 行业映射 ===
industry_map = {
    "Fintech": "Fintech",
    "Internet software & services": "Internet",
    "Internet": "Internet",
    "Hardware": "Hardware",
    "Cybersecurity": "Cybersecurity",
    "Artificial intelligence": "Artificial intelligence",
    "Data management & analytics": "Data",
    "Health": "Health",
    "Edtech": "Edtech",
    "Auto & transportation": "Auto & transportation",
    "E-commerce & direct-to-consumer": "E-commerce & direct-to-consumer",
    "Supply chain logistics & delivery": "Supply chain, logistics, & delivery",
    "Supply chain, logistics, & delivery": "Supply chain, logistics, & delivery",
    "Consumer & retail": "Consumer & retail",
    "Mobile & telecommunications": "Mobile & telecommunications",
    "Travel": "Travel",
    "GIC. Apis Partners, Insight Partners": "Other",
    "0": "Other"
}
merged["industry"] = merged["industry"].map(industry_map).fillna("Other")

# === Step 5: 标准化字段格式 ===
# 日期
merged["joined_date"] = pd.to_datetime(merged["joined_date"], errors="coerce")
merged["funded_at"] = pd.to_datetime(merged["funded_at"], errors="coerce")

# 金额
merged["raised_amount_usd"] = pd.to_numeric(merged["raised_amount_usd"], errors="coerce")

# 估值 (billion → USD)
merged["valuation_usd"] = merged["valuation_billion"].astype(float) * 1e9

# === Step 6: 输出长表（公司 × 融资事件） ===
merged.to_csv(output_long, index=False, encoding="utf-8-sig")

# === Step 7: 汇总（公司级别） ===
summary = merged.groupby(
    ["company", "company_clean", "founded_year", "country", "city", "industry"]
).agg(
    total_funding_usd=("raised_amount_usd", "sum"),
    funding_rounds=("funding_round_id", "count"),
    valuation_usd=("valuation_usd", "first"),
    joined_date=("joined_date", "first")
).reset_index()

summary.to_csv(output_summary, index=False, encoding="utf-8-sig")

# === Step 8: 展示样本 & 关键统计 ===
print("\n✅ 样本数据（merged 长表）:")
print(merged.head(10))

print("\n✅ 公司级别汇总（summary 宽表）:")
print(summary.head(10))

print("\n📊 融资次数分布:")
print(summary["funding_rounds"].describe())

print("\n📊 融资总额 vs 估值（美元，单位=十亿）:")
print(summary[["total_funding_usd", "valuation_usd"]].describe())
