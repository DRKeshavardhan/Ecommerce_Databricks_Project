# Databricks notebook source
from pyspark.sql import functions as F

silver = spark.table("workspace.ecommerce_silver.orders")
spark.sql("CREATE SCHEMA IF NOT EXISTS workspace.ecommerce_gold")

def save(df, name):
    df.write.format("delta").mode("overwrite").option("overwriteSchema", True).saveAsTable(f"workspace.ecommerce_gold.{name}")

save(silver.agg(F.countDistinct("order_id").alias("total_orders"), F.sum("quantity").alias("total_quantity"), F.sum("revenue").alias("total_revenue"), F.avg("revenue").alias("average_order_value")), "sales_summary")
save(silver.groupBy("order_date").agg(F.countDistinct("order_id").alias("orders"), F.sum("quantity").alias("quantity"), F.sum("revenue").alias("revenue")).orderBy("order_date"), "daily_sales")
save(silver.groupBy("product_id", "product_name", "category").agg(F.countDistinct("order_id").alias("orders"), F.sum("quantity").alias("quantity"), F.sum("revenue").alias("revenue")).orderBy(F.desc("revenue")), "product_performance")
save(silver.groupBy("category").agg(F.countDistinct("order_id").alias("orders"), F.sum("quantity").alias("quantity"), F.sum("revenue").alias("revenue")).orderBy(F.desc("revenue")), "category_performance")
save(silver.groupBy("customer_id", "name").agg(F.countDistinct("order_id").alias("orders"), F.sum("quantity").alias("quantity"), F.sum("revenue").alias("revenue")).orderBy(F.desc("revenue")), "customer_performance")
save(silver.groupBy("city").agg(F.sum("revenue").alias("revenue"), F.countDistinct("order_id").alias("orders")).orderBy(F.desc("revenue")), "city_performance")
save(silver.groupBy("state").agg(F.sum("revenue").alias("revenue"), F.countDistinct("order_id").alias("orders")).orderBy(F.desc("revenue")), "state_performance")
save(silver.groupBy("payment_method").agg(F.sum("revenue").alias("revenue"), F.countDistinct("order_id").alias("orders")).orderBy(F.desc("revenue")), "payment_performance")
save(silver.groupBy("customer_id", "name").agg(F.sum("revenue").alias("revenue")).orderBy(F.desc("revenue")).limit(10), "top_customers")
save(silver.groupBy("product_id", "product_name").agg(F.sum("revenue").alias("revenue")).orderBy(F.desc("revenue")).limit(10), "top_products")
save(silver.groupBy("order_date", "category").agg(F.sum("revenue").alias("revenue")).orderBy("order_date", F.desc("revenue")), "daily_category_sales")

spark.sql("SHOW TABLES IN workspace.ecommerce_gold").show()
