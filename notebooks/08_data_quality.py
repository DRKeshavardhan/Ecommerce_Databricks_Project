# Databricks notebook source
from pyspark.sql import functions as F

df = spark.table("workspace.ecommerce_silver.orders")
checks = {
    "row_count": df.count(),
    "null_order_id": df.filter(F.col("order_id").isNull()).count(),
    "null_customer_id": df.filter(F.col("customer_id").isNull()).count(),
    "null_product_id": df.filter(F.col("product_id").isNull()).count(),
    "duplicate_order_id": df.groupBy("order_id").count().filter(F.col("count") > 1).count(),
    "invalid_quantity": df.filter(F.col("quantity") <= 0).count(),
    "invalid_price": df.filter(F.col("price") < 0).count(),
    "invalid_revenue": df.filter(F.col("revenue") < 0).count(),
}
for k, v in checks.items(): print(f"{k}: {v}")
if checks["row_count"] == 0: raise ValueError("Data quality failed: zero rows")
failures = {k:v for k,v in checks.items() if k != "row_count" and v != 0}
if failures: raise ValueError(f"Data quality failed: {failures}")
print("All data quality checks passed.")
