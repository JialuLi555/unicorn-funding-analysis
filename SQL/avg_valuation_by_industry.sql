-- 按行业平均估值
SELECT industry, AVG(valuation_usd) AS avg_valuation
            FROM only
            GROUP BY industry
            ORDER BY avg_valuation DESC;