import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# 路径配置
# -----------------------------
data_folder = r"D:\PYTHON object\begin\unicorn-funding-analysis\data"
output_folder = r"D:\PYTHON object\begin\unicorn-funding-analysis\figures"
os.makedirs(output_folder, exist_ok=True)

# -----------------------------
# 读取公司汇总表数据
# -----------------------------
only_path = os.path.join(data_folder, "unicorn_funding_only.csv")
df_only = pd.read_csv(only_path)

# 读取融资表数据
merged_path = os.path.join(data_folder, "merged_unicorn_funding_clean_only.csv")
df_long = pd.read_csv(merged_path)

# -----------------------------
# 图1：融资总额分布
# -----------------------------
plt.figure(figsize=(10,6))
sns.histplot(df_only['total_funding_usd'], bins=50, kde=True)
plt.title("Distribution of Total Funding (USD)")
plt.xlabel("Total Funding (USD)")
plt.ylabel("Number of Companies")
plt.xscale('log')  # 金额跨度大，使用对数
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "total_funding_distribution.png"))
plt.close()

# -----------------------------
# 图 2：融资次数分布
# -----------------------------
plt.figure(figsize=(10,6))
sns.countplot(x='funding_rounds', data=df_only)
plt.title("Distribution of Funding Rounds")
plt.xlabel("Number of Funding Rounds")
plt.ylabel("Number of Companies")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "funding_rounds_distribution.png"))
plt.close()

# -----------------------------
# 图 3：行业融资总额对比
# -----------------------------
industry_funding = df_only.groupby('industry')['total_funding_usd'].sum().sort_values(ascending=False)
plt.figure(figsize=(12,6))
sns.barplot(x=industry_funding.index, y=industry_funding.values)
plt.xticks(rotation=45, ha='right')
plt.title("Total Funding by Industry")
plt.ylabel("Total Funding (USD)")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "industry_total_funding.png"))
plt.close()

# -----------------------------
# 图 4：估值分布（直方图 + 箱线图）
# -----------------------------
plt.figure(figsize=(10,6))
sns.histplot(df_only['valuation_usd'], bins=50, kde=True)
plt.title("Distribution of Company Valuation (USD)")
plt.xlabel("Valuation (USD)")
plt.ylabel("Number of Companies")
plt.xscale('log')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "valuation_distribution.png"))
plt.close()

plt.figure(figsize=(10,4))
sns.boxplot(x=df_only['valuation_usd'])
plt.xscale('log')
plt.title("Boxplot of Company Valuation (USD)")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "valuation_boxplot.png"))
plt.close()

# -----------------------------
# 图 5：融资轮次 vs 融资总额（散点图）
# -----------------------------
plt.figure(figsize=(10,6))
sns.scatterplot(x='funding_rounds', y='total_funding_usd', data=df_only)
plt.yscale('log')
plt.title("Funding Rounds vs Total Funding")
plt.xlabel("Funding Rounds")
plt.ylabel("Total Funding (USD)")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "rounds_vs_funding.png"))
plt.close()

# -----------------------------
# 图 6：融资年份趋势
# -----------------------------
df_long['funded_year'] = pd.to_datetime(df_long['funded_at'], errors='coerce').dt.year
funding_by_year = df_long.groupby('funded_year')['raised_amount_usd'].sum().dropna()
plt.figure(figsize=(12,6))
funding_by_year.plot(kind='line', marker='o')
plt.title("Total Funding Raised per Year")
plt.xlabel("Year")
plt.ylabel("Total Raised (USD)")
plt.yscale('log')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "funding_trend_by_year.png"))
plt.close()

print("All figures saved to:", output_folder)
