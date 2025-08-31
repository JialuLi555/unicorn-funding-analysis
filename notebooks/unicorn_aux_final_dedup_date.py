import pandas as pd
import numpy as np

# 路径配置
file1 = "data/dataset/Unicorn_Clean.csv"
file2 = "data/dataset/Unicorn_Companies1.csv"
file3 = "data/dataset/Unicorn_Companies2.csv"
file4 = "data/dataset/unicorns_till_sep_2022.csv"

output_file = r"../data/unicorn_aux_final_dedup_date.csv"


def clean_company_name(name: str) -> str:
    """生成清理后的公司名 (小写 + 只保留字母数字)"""
    if pd.isna(name):
        return ""
    return (
        str(name)
        .lower()
        .replace(" ", "")
        .replace("\u00a0", "")  # 删除不可见空格
        .replace("\xa0", "")
        .encode("ascii", "ignore")
        .decode("utf-8")  # 去掉非ascii字符（中文全去掉）
    ).replace("-", "").replace(".", "")


def load_and_standardize(filepath: str, source: str) -> pd.DataFrame:
    """读取并标准化列"""
    df = pd.read_csv(filepath)

    # 统一不同文件列名
    rename_dict = {
        "Company": "company",
        "company": "company",
        "Valuation ($B)": "valuation_billion",
        "Valuation": "valuation_billion",
        "Valuation ($B)": "valuation_billion",
        "Valuation ($B)": "valuation_billion",
        "Date Joined": "joined_date",
        "Country": "country",
        "City": "city",
        "Industry": "industry",
        "Founded Year": "founded_year",
        "Year Founded": "founded_year",
    }
    df = df.rename(columns=rename_dict)

    # 添加清理过的公司名
    df["company_clean"] = df["company"].astype(str).str.strip().str.lower()
    df["company_clean"] = df["company_clean"].str.replace(r"[^a-z0-9]", "", regex=True)

    # 处理估值字段
    if "valuation_billion" in df.columns:
        df["valuation_billion"] = (
            df["valuation_billion"]
            .astype(str)
            .str.replace(r"[\$,B]", "", regex=True)
            .str.strip()
        )
        df["valuation_billion"] = pd.to_numeric(df["valuation_billion"], errors="coerce")

    # 标准化日期格式
    if "joined_date" in df.columns:
        df["joined_date"] = pd.to_datetime(
            df["joined_date"], errors="coerce"
        ).dt.strftime("%Y/%m/%d")

    # 只保留需要列
    keep_cols = [
        "company",
        "company_clean",
        "founded_year",
        "joined_date",
        "valuation_billion",
        "country",
        "city",
        "industry",
    ]
    for col in keep_cols:
        if col not in df.columns:
            df[col] = np.nan

    df = df[keep_cols]
    df["source"] = source  # 保留数据来源

    return df


# 读取并标准化四个文件
df1 = load_and_standardize(file1, "Unicorn_Clean")
df2 = load_and_standardize(file2, "Unicorn_Companies1")
df3 = load_and_standardize(file3, "Unicorn_Companies2")
df4 = load_and_standardize(file4, "Unicorns_till_sep2022")

# 合并
merged = pd.concat([df1, df2, df3, df4], ignore_index=True)

# 去重：保留 company_clean 相同且非空字段最多的行
def count_non_null(row):
    return row.notna().sum()


merged["non_null_count"] = merged.apply(count_non_null, axis=1)

# 按 company_clean 分组，取非空最多的那一行
deduped = merged.sort_values(
    by=["company_clean", "non_null_count"], ascending=[True, False]
).drop_duplicates(subset=["company_clean"], keep="first")

# 删除辅助列
deduped = deduped.drop(columns=["non_null_count", "source"])

# 导出
deduped.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"已生成 {output_file}，共 {len(deduped)} 条公司记录。")
