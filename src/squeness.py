from pyspark.shell import sqlContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import spark_partition_id, asc

spark=SparkSession.builder.master('yarn').appName('byexample').getOrCreate()
# sqlContext.setConf("spark.sql.shuffle.partitions", "8")
# sqlContext.setConf("spark.sql.files.maxPartitionBytes","128000000")

# Cloud storage connector is required to read from GCS in Spark.
conf = spark.sparkContext._jsc.hadoopConfiguration()
conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
conf.set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")

spark.conf.set('temporaryGcsBucket','ritu01')

df=spark.read.csv(r'gs://ritu01/data/sales_record_2022_05_21.csv')
df.show()

print(df.rdd.getNumPartitions())


df \
        .withColumn("partitionId", spark_partition_id()) \
        .groupBy("partitionId") \
        .count() \
        .orderBy(asc("count")) \
        .show()

df1=df.repartition(3)
df1 \
        .withColumn("partitionId", spark_partition_id()) \
        .groupBy("partitionId") \
        .count() \
        .orderBy(asc("count")) \
        .show()

# df.write.format('bigquery').option('table','spatial-shore-360518.gcs_to_bq_df.new1').mode('append').save()
# print('bq load succesfully')

# from pyspark.sql.functions import array
# df.select(df.name,array(df.currentState,df.previousState).alias("States")).show()
