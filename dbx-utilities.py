# Databricks notebook source
# MAGIC %fs
# MAGIC ls

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

for folder_name in dbutils.fs.ls('/'):
    print(folder_name)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.notebook.run("./child_notebook", 10, {"input": "Called from the main notebook"})

# COMMAND ----------

# MAGIC %pip install pandas

# COMMAND ----------


