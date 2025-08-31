#  Unicorn Funding Analysis

本项目基于全球独角兽公司数据，涵盖公司基本信息、融资事件、估值等。通过 **Python + SQLite** 构建数据库，执行 SQL 查询，结合 **Python 可视化** 和 **Tableau Dashboard**，从多个角度分析独角兽企业的融资特征与发展趋势。


## 项目结构

```
.
├── data/                         # 数据文件
│   ├── dataset/                  # 原始数据集
│   │   ├── funding_rounds.csv
│   │   ├── objects.csv
│   │   ├── Unicorn_Clean.csv
│   │   ├── Unicorn_Companies1.csv
│   │   ├── Unicorn_Companies2.csv
│   │   ├── unicorn_funding_summary.csv
│   │   └── unicorns_till_sep_2022.csv
│   ├── clean_funding_data_final.csv          # 融资数据初步合并清理
│   ├── merged_unicorn_funding_clean.csv      # 融资事件汇总
│   ├── merged_unicorn_funding_clean_only.csv 
│   ├── unicorn_aux_final_dedup_date.csv      # 独角兽公司数据初步合并清理
│   ├── unicorn_funding.db                    # SQLite 数据库
│   ├── unicorn_funding_only.csv              
│   └── unicorn_funding_summary.csv           # 公司级别汇总
│
├── figures/                      # Python 可视化结果
│   ├── funding_rounds_distribution.png   
│   ├── funding_trend_by_year.png    
│   ├── industry_total_funding.png  
│   ├── rounds_vs_funding.png     
│   ├── total_funding_distribution.png   
│   ├── valuation_boxplot.png  
│   └── valuation_distribution.png   
│
├── notebooks/                    # Python 脚本
│   ├── clean_funding_data_final.py            # 融资数据初步合并清理
│   ├── long+summary.py                        # 融资数据与独角兽公司数据合并数据
│   ├── sql_lite.py                            # sqllite查询及结果
│   ├── unicorn_aux_final_dedup_date.py        # 独角兽公司数据初步合并清理
│   ├── unicorn_funding_only.py                # 仅含有融资信息的分析数据
│   └── verify_picture.py                      # 数据初步验证图
│
├── Tableau/                      # Tableau Dashboard
│   ├── Tableau_Dashboard1.png
│   ├── Tableau_Dashboard2.png
│   ├── Tableau_Dashboard3.png
│   └── Tableau_Public_Link.txt   # Tableau Public 链接
│
├── SQL/                          # SQL 查询
│   ├── avg_valuation_by_industry.sql / .csv 
│   ├── funding_trend_by_year.sql / .csv     
│   ├── industry_funding.sql / .csv    
│   ├── multi_round_companies.sql / .csv  
│   ├── recent_funding_events.sql / .csv 
│   ├── top10_total_funding.sql / .csv 
│   └── ...
│
├── requirements.txt              # Python 库
└── README.md
```


## 环境依赖

Python 版本：**>=3.9**

安装依赖：

```bash
pip install -r requirements.txt
```

`requirements.txt` 示例：

```
pandas
numpy
matplotlib
seaborn
```

SQLite 已内置在 Python 标准库中，无需额外安装。


## 使用方法

1. **构建数据库**

   ```bash
   python notebooks/sql_lite.py
   ```

   运行后会在 `data/` 下生成 `unicorn_funding.db`。

2. **运行 SQL 查询**

   * 手动执行 `SQL/` 文件夹中的 `.sql` 查询语句
   * 或运行 Python 脚本自动导出 `.csv` 结果

3. **可视化**

   * Python 可视化结果保存在 `figures/`
   * Tableau 仪表板截图见 `Tableau/`，并可通过 `Tableau_Public_Link.txt` 在线访问


## SQL 查询主题

本项目已预置多类查询，支持快速分析：

* **行业分析**
 # 按行业平均估值

  * `industry_funding.sql`：各行业融资额统计
  * `avg_valuation_by_industry.sql`：行业平均估值
* **时间趋势**

  * `funding_trend_by_year.sql`：年度融资趋势
* **公司级别**

  * `multi_round_companies.sql`：多轮融资公司列表
  * `recent_funding_events.sql`：最新融资事件
* **TOP榜单**

  * `top10_total_funding.sql`：融资总额前十公司

## 可视化展示

### Python 绘图（figures/）

* 融资轮次数分布
* 年度融资趋势
* 行业总融资额
* 融资总额 vs 估值关系
* 融资与估值分布

### Tableau Dashboard（Tableau/）

* Tableau_Dashboard1：宏观趋势（年度 + 融资类型 + 地理）
* Tableau_Dashboard2：企业与行业（公司Top10 + 散点估值融资 + 行业条形 + 行业热力图）
* Tableau_Dashboard3：公司案例（融资轮次数 + 时间线）

在线访问 Tableau Dashboard：https://public.tableau.com/app/profile/.47376857/viz/unicorn_funding_only/story


## 数据来源

* 原始数据来自Kaggle公开数据集
* 清洗与处理结果保存在 `data/` 文件夹下


## 致谢

本项目由 **Python + SQLite + Tableau** 驱动，适合 SQL 查询训练、数据可视化实践和商业分析展示。

