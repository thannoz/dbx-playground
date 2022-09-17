# Databricks notebook source
dbutils.widgets.text("input", "", "Send the parameter value")

# COMMAND ----------

input_param = dbutils.widgets.get("input")
print(input_param)

# COMMAND ----------

print(input_param)

# COMMAND ----------

dbutils.notebook.exit(100)

# COMMAND ----------


