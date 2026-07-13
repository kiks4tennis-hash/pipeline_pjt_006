
  
    

  create  table "airflow"."public"."customer_summary__dbt_tmp"
  
  
    as
  
  (
    SELECT

    customer_id,

    COUNT(order_id) AS order_count,

    SUM(sales) AS total_sales,

    MAX(order_date) AS last_order_date,

    ROUND(AVG(sales),2) AS avg_order_value

FROM "airflow"."public"."stg_orders"

GROUP BY customer_id
  );
  