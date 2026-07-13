SELECT
    CAST(order_id AS INTEGER)      AS order_id,
    CAST(customer_id AS INTEGER)   AS customer_id,
    category,
    product,
    CAST(price AS NUMERIC)         AS price,
    CAST(quantity AS INTEGER)      AS quantity,
    CAST(sales AS NUMERIC)         AS sales,
    CAST(order_date AS TIMESTAMP)  AS order_date

FROM raw_orders