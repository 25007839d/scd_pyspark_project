# import findspark
# findspark.init()
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import row_number, col, dense_rank, rank, lead, lag, udf
from pyspark.sql.types import StringType, StructField, StructType,DateType




# if __name__=="__main__":
#     spark = SparkSession.\
#         builder.master('local[*]').\
#         appName('interview').\
#         getOrCreate()
#     sc = SparkContext.getOrCreate()

    # path = r"C:\Users\KAJAL\OneDrive\Desktop\Brainwork\Cloud\SCD PROJECT\Dushyant\Raw_data_file"
    #
    # schema = StructType([StructField('name',StringType()),StructField('email',StringType()),StructField('age',StringType())])
    # dataframe =  spark.read.csv(path,header=True)
    # dataframe.show()
    # from pyspark.sql.window import *
    # wndow = Window.partitionBy('country').orderBy('name')
    # df=dataframe.withColumn('row_number',row_number().over(wndow)).where(col('row_number')==1)
    # df.withColumn('lead',lead('row_number',1).over(wndow)).show()
    #
    # win= Window.partitionBy('row_number').orderBy('name')
    # df.withColumn('lag',lag('row_number',1).over(win)).show()
    # def replace(x):
    #     z = ''
    #     for i in x:
    #
    #         if i =='-':
    #             continue
    #
    #         else:
    #             z=z+i
    #
    #     return z
    # rep = udf(lambda x: replace(x))
    # udfdf = df.withColumn('dept_id',rep(col('dept_id')))
    # udfdf.show()


    # df.write.mode('overwrite').option('header',True).csv(r"C:\Users\KAJAL\OneDrive\Desktop\Brainwork\Cloud\SCD PROJECT\Dushyant\Final_target_3")

    import pyspark
    # from pyspark.sql import SparkSession


    # state = {'Nebraska':'NE','Florida':'FL'}
    # broadvar = spark.sparkContext.broadcast(state)

    # convert  df to rdd
    # bdf=df.rdd.map(lambda x:(x[0],x[1],x[2],x[3],x[5])).toDF()
    # bdf.show()

### broadcast
    # states = {"NY": "New York", "CA": "California", "FL": "Florida"}
    # broadcastStates = spark.sparkContext.broadcast(states)
    #
    # data = [("James", "Smith", "USA", "CA"),
    #         ("Michael", "Rose", "USA", "NY"),
    #         ("Robert", "Williams", "USA", "CA"),
    #         ("Maria", "Jones", "USA", "FL")
    #         ]
    #
    # rdd = spark.sparkContext.parallelize(data)
    # print(rdd.collect())
    #
    #
    # def state_convert(code):
    #     return broadcastStates.value[code]
    #
    #
    # result = rdd.map(lambda x: (x[0], x[1], x[2], state_convert(x[3]))).collect()
    # print(result)


####accumulator

    # accumCount = spark.sparkContext.accumulator(0)
    # rdd2 = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
    # rdd2.foreach(lambda x: accumCount.add(1))
    # print(accumCount.value)


# RDD operation


    #sc.parallelize()

    # rdd = sc.parallelize([[1,3,2,5,3,2,2],[3,2,5,2,1]])
    # print(rdd.collect())
    # print(rdd.take(3))
    # print(rdd.first())
    #
    # #.flatMap  It is a common practice to separate the text content for analysis
    #
    # rdd1 = rdd.flatMap(lambda x: x.split(','))
# .map()
# The map is useful if you want to apply some transformation to each element of an RDD or use a condition.
#     wordsAsTuples = words.map(lambda x: (x.lower(), 1))wordsAsTuples.take(4)

    # a= [tuple('0005015155614')]
    #
    # rdd1 = sc.parallelize(a)
    # print(rdd1.collect())
    # # col = ['one','two','three','foure']
    # df = rdd1.toDF()
    # df.show()

