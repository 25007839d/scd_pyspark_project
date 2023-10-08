import findspark
findspark.init()
from pyspark.shell import sqlContext
from pyspark.sql.functions import spark_partition_id, asc, desc

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
if __name__ == '__main__':
    spark=SparkSession.builder.master('local[*]').appName('sparkbyexample').getOrCreate()

    data = [('James', '', 'Smith', '1991-04-01', 'M', 3000),
            ('Michael', 'Rose', '', '2000-05-19', 'M', 4000),
            ('Robert', '', 'Williams', '1978-09-05', 'M', 4000),
            ('Maria', 'Anne', 'Jones', '1967-12-01', 'F', 4000),
            ('Jen', 'Mary', 'Brown', '1980-02-17', 'F', -1)
            ]

    data1 = [('UP', 'BIJNOR', 3000),
            ('UP', 'MBD',  4000),
            ('UK', 'HRD', 4000),
             ('UK', 'BIJNOR', 3000),
             ('UP', 'BIHAR', 4000),
             ('UK', 'HRD', 4000)
            ]
    # sqlContext.setConf("spark.sql.shuffle.partitions", "8")
    # sqlContext.setConf("spark.sql.files.maxPartitionBytes", "128")

    columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]
    columns1 = ["STATE", "CITY",  "salary"]
    df = spark.createDataFrame(data=data1, schema=columns1)
    # df = spark.read.csv(r'C:\Users\Dell\OneDrive\Desktop\PC\data_file.csv',header=True)
    df.show()
# after join in rdd partition add together
    # rdd1 = spark.sparkContext.parallelize((data),5)
    # rdd2 = spark.sparkContext.parallelize((data1),3)
    # jrdd = rdd2.join(rdd1)
    # print(rdd1.getNumPartitions())
    # print(rdd2.getNumPartitions())
    # print(jrdd.getNumPartitions())
# after join df partition

    # dfa = spark.createDataFrame(data,columns)
    # dfb = spark.createDataFrame(data1, columns)
    # print(df.rdd.getNumPartitions())
    #
    #
    # jdf = dfa.join(dfb,dfa.firstname==dfb.firstname)
    # jdf.show()
    #
    # dfa \
    #     .withColumn("partitionId", spark_partition_id()) \
    #     .groupBy("partitionId") \
    #     .count() \
    #     .orderBy(asc("count")) \
    #     .show()

    # df1=df.repartition(3)
    # dfb \
    #     .withColumn("partitionId", spark_partition_id()) \
    #     .groupBy("partitionId") \
    #     .count() \
    #     .orderBy(asc("count")) \
    #     .show()
    #
    # jdf \
    #     .withColumn("partitionId", spark_partition_id()) \
    #     .groupBy("partitionId") \
    #     .count() \
    #     .orderBy(asc("count")) \
    #     .show()


    # df.withColumn('temp',array(df.salary)).show()
    # df.select(df.STATE,df.CITY,array(df.salary)).show()
    df.groupBy('STATE').agg(collect_set('salary').alias('words')).show()
    df.select()  collect_set('salary').alias('words')).show()