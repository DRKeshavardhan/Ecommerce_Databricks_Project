CREATE SCHEMA IF NOT EXISTS workspace.ecommerce_delta_practice;
CREATE OR REPLACE TABLE workspace.ecommerce_delta_practice.orders AS SELECT * FROM workspace.ecommerce_bronze.orders;
DESCRIBE HISTORY workspace.ecommerce_delta_practice.orders;
UPDATE workspace.ecommerce_delta_practice.orders SET quantity = quantity + 1 WHERE order_id = 1001;
DELETE FROM workspace.ecommerce_delta_practice.orders WHERE order_id = 1020;
-- After checking history, use a real version:
-- SELECT * FROM workspace.ecommerce_delta_practice.orders VERSION AS OF <version>;
DESCRIBE DETAIL workspace.ecommerce_delta_practice.orders;
