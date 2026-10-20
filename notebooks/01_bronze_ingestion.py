# Databricks notebook source
from pyspark.sql import functions as F

CUSTOMERS = "/Volumes/workspace/default/ecommerce_data/customers.csv"
PRODUCTS = "/Volumes/workspace/default/ecommerce_data/products.csv"
ORDERS = "/Volumes/workspace/default/ecommerce_data/orders.csv"

spark.sql("CREATE SCHEMA IF NOT EXISTS workspace.ecommerce_bronze")

customers = spark.read.option("header", True).option("inferSchema", True).csv(CUSTOMERS)
products = spark.read.option("header", True).option("inferSchema", True).csv(PRODUCTS)
orders = spark.read.option("header", True).option("inferSchema", True).csv(ORDERS)

customers.write.format("delta").mode("overwrite").option("overwriteSchema", True).saveAsTable("workspace.ecommerce_bronze.customers")
products.write.format("delta").mode("overwrite").option("overwriteSchema", True).saveAsTable("workspace.ecommerce_bronze.products")
orders.write.format("delta").mode("overwrite").option("overwriteSchema", True).saveAsTable("workspace.ecommerce_bronze.orders")

print("Bronze ingestion completed.")
print("Customers:", spark.table("workspace.ecommerce_bronze.customers").count())
print("Products:", spark.table("workspace.ecommerce_bronze.products").count())
print("Orders:", spark.table("workspace.ecommerce_bronze.orders").count())
