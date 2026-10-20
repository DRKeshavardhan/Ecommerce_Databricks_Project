# Databricks notebook source
# Delta Lake practice uses a separate table so the main project remains safe.

spark.sql("CREATE SCHEMA IF NOT EXISTS workspace.ecommerce_delta_practice")
spark.sql("CREATE OR REPLACE TABLE workspace.ecommerce_delta_practice.orders AS SELECT * FROM workspace.ecommerce_bronze.orders")

spark.sql("DESCRIBE HISTORY workspace.ecommerce_delta_practice.orders").show(truncate=False)

spark.sql("UPDATE workspace.ecommerce_delta_practice.orders SET quantity = quantity + 1 WHERE order_id = 1001")
spark.sql("DELETE FROM workspace.ecommerce_delta_practice.orders WHERE order_id = 1020")

updates = spark.createDataFrame([(1002, 105, 2, "2026-01-03", "UPI"), (2001, 101, 1, "2026-01-20", "Credit Card")], ["order_id", "customer_id", "quantity", "order_date", "payment_method"])
updates.createOrReplaceTempView("order_updates")

spark.sql("""
MERGE INTO workspace.ecommerce_delta_practice.orders AS t
USING order_updates AS s
ON t.order_id = s.order_id
WHEN MATCHED THEN UPDATE SET t.customer_id=s.customer_id, t.quantity=s.quantity, t.order_date=CAST(s.order_date AS DATE), t.payment_method=s.payment_method
WHEN NOT MATCHED THEN INSERT (order_id, customer_id, product_id, quantity, order_date, payment_method)
VALUES (s.order_id, s.customer_id, 1, s.quantity, CAST(s.order_date AS DATE), s.payment_method)
""")

spark.sql("ALTER TABLE workspace.ecommerce_delta_practice.orders ADD COLUMNS (customer_segment STRING)")
spark.sql("DESCRIBE HISTORY workspace.ecommerce_delta_practice.orders").show(truncate=False)
print("After DESCRIBE HISTORY, use a real prior version for time travel:")
print("SELECT * FROM workspace.ecommerce_delta_practice.orders VERSION AS OF <version>;")
