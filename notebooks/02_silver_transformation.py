# Databricks notebook source
from pyspark.sql import functions as F

spark.sql("CREATE SCHEMA IF NOT EXISTS workspace.ecommerce_silver")
orders = spark.table("workspace.ecommerce_bronze.orders")
products = spark.table("workspace.ecommerce_bronze.products")
customers = spark.table("workspace.ecommerce_bronze.customers")

silver = (orders.alias("o")
    .join(products.alias("p"), F.col("o.product_id") == F.col("p.product_id"), "left")
    .join(customers.alias("c"), F.col("o.customer_id") == F.col("c.customer_id"), "left")
    .select("o.order_id", "o.customer_id", "c.name", "c.city", "c.state", "c.age",
            "o.product_id", "p.product_name", "p.category", "p.price", "o.quantity",
            "o.order_date", "o.payment_method",
            (F.col("p.price") * F.col("o.quantity")).alias("revenue"),
            F.year("o.order_date").alias("order_year"),
            F.month("o.order_date").alias("order_month"),
            F.dayofmonth("o.order_date").alias("order_day"))
    .dropDuplicates(["order_id"]))

silver.write.format("delta").mode("overwrite").option("overwriteSchema", True).saveAsTable("workspace.ecommerce_silver.orders")
print("Silver rows:", silver.count())
