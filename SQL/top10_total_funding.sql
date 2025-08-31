-- 查询总融资额前10公司
SELECT company, total_funding_usd, funding_rounds, valuation_usd
            FROM only
            ORDER BY total_funding_usd DESC
            LIMIT 10;