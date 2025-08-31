-- 最近融资事件
SELECT company, funding_round_type, funded_at, raised_amount_usd
            FROM merged_clean
            WHERE funded_at IS NOT NULL
            ORDER BY funded_at DESC
            LIMIT 50;