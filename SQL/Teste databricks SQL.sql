-- Databricks notebook source
select * from supermarket_sales___sheet1_csv

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Título do arquivo

-- COMMAND ----------

-- MAGIC %md ## Teste
-- MAGIC **lalalalalala**
-- MAGIC

-- COMMAND ----------

select * from supermarket_sales___sheet1_csv
where Total > 500

-- COMMAND ----------

select City, avg(`Unit price`) from supermarket_sales___sheet1_csv
group by City

-- COMMAND ----------

-- MAGIC %md
-- MAGIC comentários xyz
-- MAGIC

-- COMMAND ----------


