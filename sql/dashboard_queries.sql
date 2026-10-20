-- KPI
SELECT * FROM workspace.ecommerce_gold.sales_summary;
-- Daily revenue
SELECT order_date, revenue FROM workspace.ecommerce_gold.daily_sales ORDER BY order_date;
-- Category revenue
SELECT category, revenue FROM workspace.ecommerce_gold.category_performance ORDER BY revenue DESC;
-- Top products
SELECT product_name, revenue FROM workspace.ecommerce_gold.product_performance ORDER BY revenue DESC LIMIT 10;
-- Payment methods
SELECT payment_method, revenue FROM workspace.ecommerce_gold.payment_performance ORDER BY revenue DESC;
-- Customers
SELECT * FROM workspace.ecommerce_gold.customer_performance ORDER BY revenue DESC;
-- States
SELECT state, revenue FROM workspace.ecommerce_gold.state_performance ORDER BY revenue DESC;
