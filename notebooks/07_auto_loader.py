# Databricks notebook source
# Template: create an incoming_orders directory in your Volume before running.

source_path = "/Volumes/workspace/default/ecommerce_data/incoming_orders"
checkpoint_path = "/Volumes/workspace/default/ecommerce_data/checkpoints/orders"
target_table = "workspace.ecommerce_bronze.orders_incremental"

spark.sql("CREATE SCHEMA IF NOT EXISTS workspace.ecommerce_bronze")

df = (spark.readStream.format("cloudFiles")
      .option("cloudFiles.format", "csv")
      .option("cloudFiles.inferColumnTypes", "true")
      .option("header", "true")
      .load(source_path))

query = (df.writeStream.format("delta")
         .option("checkpointLocation", checkpoint_path)
         .outputMode("append")
         .trigger(availableNow=True)
         .toTable(target_table))
query.awaitTermination()
