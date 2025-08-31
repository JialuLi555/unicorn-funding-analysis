-- 多轮融资公司（融资次数>1）
SELECT company, funding_rounds, total_funding_usd
            FROM only
            WHERE funding_rounds > 1
            ORDER BY funding_rounds DESC;