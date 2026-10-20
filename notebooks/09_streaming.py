# Databricks notebook source
# Template: create streaming_orders directory and place incoming CSV files there.

from pyspark.sql import functions as F
source_path = "/Volumes/workspace/default/ecommerce_data/streaming_orders"
checkpoint_path = "/Volumes/workspace/default/ecommerce_data/checkpoints/streaming_orders"

stream_df = (spark.readStream.format("cloudFiles")
             .option("cloudFiles.format", "csv")
             .option("cloudFiles.inferColumnTypes", "true")
             .option("header", "true")
             .load(source_path)
             .withColumn("ingested_at", F.current_timestamp()))

query = (stream_df.writeStream.format("delta")
         .option("checkpointLocation", checkpoint_path)
         .outputMode("append")
         .trigger(availableNow=True)
         .toTable("workspace.ecommerce_bronze.streaming_orders"))
query.awaitTermination()
