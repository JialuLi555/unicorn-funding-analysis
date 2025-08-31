-- 按行业统计总融资额和公司数量
SELECT industry, SUM(total_funding_usd) AS total_funding, COUNT(company) AS num_companies
            FROM only
            GROUP BY industry
            ORDER BY total_funding DESC;