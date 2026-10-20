# Databricks notebook source
from pyspark.sql import functions as F

orders = spark.table("workspace.ecommerce_silver.orders")
customers = spark.table("workspace.ecommerce_bronze.customers")

orders.groupBy("state").agg(F.sum("revenue").alias("revenue")).explain(True)
result = orders.join(F.broadcast(customers.select("customer_id", "age")), "customer_id", "left")
result.explain(True)
print("Current partitions:", orders.rdd.getNumPartitions())
orders.cache()
print("Cached count:", orders.count())
orders.unpersist()
print("Performance practice completed.")
