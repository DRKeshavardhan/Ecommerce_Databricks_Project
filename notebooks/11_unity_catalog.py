# Databricks notebook source
spark.sql("SHOW CATALOGS").show()
spark.sql("SHOW SCHEMAS IN workspace").show()
spark.sql("SHOW TABLES IN workspace.ecommerce_bronze").show()
spark.sql("SHOW TABLES IN workspace.ecommerce_silver").show()
spark.sql("SHOW TABLES IN workspace.ecommerce_gold").show()
spark.sql("DESCRIBE TABLE workspace.ecommerce_gold.sales_summary").show()
spark.sql("DESCRIBE DETAIL workspace.ecommerce_gold.sales_summary").show(truncate=False)
spark.sql("SELECT * FROM workspace.ecommerce_gold.sales_summary").show()
# Example permission syntax; do not run with a made-up principal:
# GRANT SELECT ON TABLE workspace.ecommerce_gold.sales_summary TO `group_name`;
