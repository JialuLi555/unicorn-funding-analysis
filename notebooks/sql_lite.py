import sqlite3
import pandas as pd
import os

# -----------------------------
# 配置文件路径
# -----------------------------
data_folder = r"D:\PYTHON object\begin\unicorn-funding-analysis\data"  # CSV 文件夹
output_folder = r"D:\PYTHON object\begin\unicorn-funding-analysis\sql"  # 查询结果 & SQL 文件保存
os.makedirs(output_folder, exist_ok=True)

db_path = os.path.join(data_folder, "unicorn_funding.db")

csv_files = {
    "merged_clean_only": "merged_unicorn_funding_clean_only.csv",
    "merged_clean": "merged_unicorn_funding_clean.csv",
    "summary": "unicorn_funding_summary.csv",
    "only": "unicorn_funding_only.csv"
}

# -----------------------------
# 读取 CSV 文件
# -----------------------------
dfs = {}
for key, file in csv_files.items():
    path = os.path.join(data_folder, file)
    dfs[key] = pd.read_csv(path)

# -----------------------------
# 创建 SQLite 数据库并导入数据
# -----------------------------
conn = sqlite3.connect(db_path)

for table_name, df in dfs.items():
    df.to_sql(table_name, conn, if_exists='replace', index=False)

print("All tables imported into SQLite database.")

# -----------------------------
# SQL 查询字典
# -----------------------------
queries = {
    "top10_total_funding": {
        "desc": "查询总融资额前10公司",
        "sql": """
            SELECT company, total_funding_usd, funding_rounds, valuation_usd
            FROM only
            ORDER BY total_funding_usd DESC
            LIMIT 10;
        """
    },
    "industry_funding": {
        "desc": "按行业统计总融资额和公司数量",
        "sql": """
            SELECT industry, SUM(total_funding_usd) AS total_funding, COUNT(company) AS num_companies
            FROM only
            GROUP BY industry
            ORDER BY total_funding DESC;
        """
    },
    "multi_round_companies": {
        "desc": "多轮融资公司（融资次数>1）",
        "sql": """
            SELECT company, funding_rounds, total_funding_usd
            FROM only
            WHERE funding_rounds > 1
            ORDER BY funding_rounds DESC;
        """
    },
    "recent_funding_events": {
        "desc": "最近融资事件",
        "sql": """
            SELECT company, funding_round_type, funded_at, raised_amount_usd
            FROM merged_clean
            WHERE funded_at IS NOT NULL
            ORDER BY funded_at DESC
            LIMIT 50;
        """
    },
    "avg_valuation_by_industry": {
        "desc": "按行业平均估值",
        "sql": """
            SELECT industry, AVG(valuation_usd) AS avg_valuation
            FROM only
            GROUP BY industry
            ORDER BY avg_valuation DESC;
        """
    },
    "funding_trend_by_year": {
        "desc": "公司融资趋势（按年份统计融资轮数和总额）",
        "sql": """
            SELECT SUBSTR(funded_at,1,4) AS year, COUNT(funding_round_id) AS num_rounds,
                   SUM(raised_amount_usd) AS total_raised
            FROM merged_clean
            WHERE funded_at IS NOT NULL
            GROUP BY year
            ORDER BY year;
        """
    }
}

# -----------------------------
# 执行查询并保存 CSV + SQL 文件
# -----------------------------
for name, query_info in queries.items():
    sql = query_info["sql"]

    # 保存 SQL 文件
    sql_file_path = os.path.join(output_folder, f"{name}.sql")
    with open(sql_file_path, "w", encoding="utf-8") as f:
        f.write(f"-- {query_info['desc']}\n")
        f.write(sql.strip())

    # 执行查询并保存 CSV
    df_result = pd.read_sql(sql, conn)
    csv_file_path = os.path.join(output_folder, f"{name}.csv")
    df_result.to_csv(csv_file_path, index=False)

    print(f"Query '{name}' executed. CSV and SQL file saved.")

# -----------------------------
# 关闭数据库连接
# -----------------------------
conn.close()
print("All done.")
