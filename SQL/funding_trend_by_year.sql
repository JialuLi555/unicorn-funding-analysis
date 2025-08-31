-- 公司融资趋势（按年份统计融资轮数和总额）
SELECT SUBSTR(funded_at,1,4) AS year, COUNT(funding_round_id) AS num_rounds,
                   SUM(raised_amount_usd) AS total_raised
            FROM merged_clean
            WHERE funded_at IS NOT NULL
            GROUP BY year
            ORDER BY year;