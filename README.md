# Unicorn Funding Analysis

## Overview

This project analyzes **Unicorn companies** (startups valued at \$1B+) and their **funding patterns** using **Python** for data cleaning & SQL for queries, combined with **Tableau** for interactive dashboards.

The goal is to demonstrate my **end-to-end data analysis workflow**: from raw datasets → data cleaning → SQL queries → visualization → business insights.

**Interactive Tableau Dashboard**: [View Online](https://public.tableau.com/app/profile/.47376857/viz/unicorn_funding_only/story)


## Project Workflow

1. **Data Source**

   * All datasets are sourced from **Kaggle** public datasets.
   * They include company names, valuations, countries, industries, funding amounts, founding years, and other relevant data.

2. **Data Cleaning & Processing (Python)**

   * Standardize date formats
   * Standardize company names
   * Normalize funding amounts and valuations to USD
   * Remove duplicates and missing values
   * Build SQLite database (unicorn_funding.db) for queries
   * Plot validation charts using matplotlib

3. **SQL Queries & Analysis**

   * Funding statistics by industry
   * Industry average valuations
   * Annual funding trends
   * List of companies with multiple funding rounds
   * Latest funding events
   * Top 10 companies by total funding

4. **Visualization (Python + Tableau)**
   * Python Visualizations (figures/)
     * **Distribution of Funding Rounds**
     * **Annual Funding Trends**
     * **Total Industry Funding**
     * **Total Funding vs. Valuation Relationship**
     * **Funding and Valuation Distribution**

  
   * Tableau Dashboard (Tableau/)
   * 3 dashboards created for different perspectives:

     * **Dashboard 1**: Macro Trends (Annual + Funding Type + Geography)
     * **Dashboard 2**: Companies & Industries (Top 10 Companies + Scatter Plot of Valuation vs. Funding + Industry Bar Chart + Industry Heatmap)
     * **Dashboard 3**: Company Cases (Number of Funding Rounds + Timeline)

## Repository Structure

```
unicorn-funding-analysis/
│── data/
│   ├── dataset/                     # Raw & cleaned datasets
│   ├── unicorn_funding.db           # SQLite database
│
│── figures/                         # Exported visualizations (PNG)
│── notebooks/                       # Python scripts (data cleaning & analysis)
│── Tableau/                         # Tableau dashboards (screenshots + link)
│── SQL/                             # SQL queries & results (CSV + SQL files)
│── requirements.txt                 # Python dependencies
│── README.md                        # Project documentation
```


## Key Insights

* **Dashboard 1 (Macro Trends & Geography)**: Unicorn funding surged after 2010, dominated by the US and industries like Fintech, E-commerce, and Health.
* **Dashboard 2 (Industry & Valuation)**: A few high-growth firms achieved 30G dollar valuations with comparatively less funding.
* **Dashboard 3 (Funding Lifecycle)**: Most unicorns reach scale through Series A/B rounds, with some raising 5+ rounds to accelerate growth.


## Tech Stack

* **Python**: pandas, numpy, sqlite3, matplotlib, os, seaborn
* **SQL**: Industry/valuation/funding queries
* **Tableau Public**: Dashboard building & storytelling
* **GitHub**: Version control & project documentation


## Why This Project Matters

This project is part of my **portfolio** to showcase:

* **Data Cleaning and Analysis**
* **Data Visualization and Dashboard Design**
* **Data Insights**
