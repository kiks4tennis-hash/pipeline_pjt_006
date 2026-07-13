
  
    

  create  table "airflow"."public"."sales_summary__dbt_tmp"
  
  
    as
  
  (
    SELECT

    category,

    COUNT(order_id) AS order_count,

    SUM(quantity) AS total_quantity,

    SUM(sales) AS total_sales,

    ROUND(AVG(price),2) AS avg_price

FROM "airflow"."public"."stg_orders"

GROUP BY category

ORDER BY total_sales DESC
  );
  