# E-Commerce Databricks Data Engineering Project

End-to-end Databricks learning project covering Bronze/Silver/Gold, Delta Lake, Unity Catalog, Auto Loader, data quality, streaming, performance, SQL and MLflow integration.

## Architecture
CSV / Volume -> Bronze Delta -> Silver -> Gold -> Dashboard -> ML/MLflow

## Unity Catalog namespace
workspace.schema.table

Example: `workspace.ecommerce_gold.sales_summary`

Raw CSV files are intentionally excluded from GitHub. Keep credentials, tokens, secrets and private data out of Git.
