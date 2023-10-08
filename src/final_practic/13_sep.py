import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master('local').appName('SparkByExamples.com').getOrCreate()
#
# #Create DataFrame df1 with columns name,dept & age
# data = [("James","Sales",34), ("Michael","Sales",56), \
#     ("Robert","Sales",30), ("Maria","Finance",24) ]
# columns= ["name","dept","age"]
# df1 = spark.createDataFrame(data = data, schema = columns)
# # df1.printSchema()
#
# #Create DataFrame df1 with columns name,dep,state & salary
# data2=[("James","Sales","NY",9000),("Maria","Finance","CA",9000), \
#     ("Jen","Finance","NY",7900),("Jeff","Marketing","CA",8000)]
# columns2= ["name","dept","state","salary"]
# df2 = spark.createDataFrame(data = data2, schema = columns2)
# # df2.printSchema()
#
#
# #Add missing columns 'state' & 'salary' to df1
# from pyspark.sql.functions import lit
# for column in [column for column in df2.columns if column not in df1.columns]:
#     print(column)
#     df1 = df1.withColumn(column, lit(None))
#
# #Add missing column 'age' to df2
# for column in [column for column in df1.columns if column not in df2.columns]:
#     print(column)
#     df2 = df2.withColumn(column, lit(None))
#
# df1.printSchema()
# df2.printSchema()
# #Finally join two dataframe's df1 & df2 by name
# merged_df=df1.unionByName(df2)
# # merged_df.show()

#------------------------------------------------------

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, concat_ws

# spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data = [("Banana",1000,"USA"), ("Carrots",1500,"USA"), ("Beans",1600,"USA"), \
      ("Orange",2000,"USA"),("Orange",2000,"USA"),("Banana",400,"China"), \
      ("Carrots",1200,"China"),("Beans",1500,"China"),("Orange",4000,"China"), \
      ("Banana",2000,"Canada"),("Carrots",2000,"Canada"),("Beans",2000,"Mexico")]

# columns= ["Product","Amount","Country"]
# df = spark.createDataFrame(data = data, schema = columns)
# df.printSchema()
# df.show(truncate=False)
# df.withColumn('aatu',concat_ws('-','Product','Amount')).show()

# pivotDF = df.groupBy("Product").pivot("Country").sum("Amount")
# pivotDF.printSchema()
# pivotDF.show(truncate=False)
#
# pivotDF = df.groupBy("Product","Country") \
#       .sum("Amount") \
#       .groupBy("Product") \
#       .pivot("Country") \
#       .sum("sum(Amount)")
# pivotDF.printSchema()
# pivotDF.show(truncate=False)
#
# """ unpivot """
# unpivotExpr = "stack(3, 'Canada', Canada, 'China', China, 'Mexico', Mexico) as (Country,Total)"
# unPivotDF = pivotDF.select("Product", expr(unpivotExpr)) \
#     .where("Total is not null")
# unPivotDF.show(truncate=False)

# df.sort('Country').show()

# arm = 153
# sum =0
# for i in str(arm):
#       cube =int(i)**3
#       sum = sum+cube
# if arm == sum:
#       print('it is prime num',sum)
#
# else:
#       print('it is not prime num', sum)

# -------------------word count----------------

string = ' this is my last practice for final interview'
#
# rdd = spark.sparkContext.parallelize(string)
# count = rdd.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
# print(count.collect())
# for (word, count) in count.collect():
#     print("%s: %i" % (word, count))

# a = [2,3,4,5,2,5,3,3]
# x=0
# y=0
# for i in a:
#     if i>x:
#         y=x
#         x=i
#     elif i>y and i!=x:
#         y=i
# a.remove(y)
# print(a)
# from pyspark.sql.functions import size,explode,split,count,col
column = ['Region','Country','Item_Type','Sales_Channel','Order_Priority','Order_Date','Order_ID','Ship_Date','Units_old','Unit_Price','Unit_Cost','Total_Revenue','Total_Cost','Total_Profit']
df = spark.read.csv(r'D:\Brainwork\Cloud\SCD PROJECT\Ritu\sales_record_2022_05_25.csv')
rdd = df.rdd.toDF(schema=column)

print(rdd.printSchema())

# df1 = df.withColumn('count',concat_ws(' ','Region','Country','Item Type','Sales Channel','Order Priority'))
# df2=df1.select('count')
# df3=df2.withColumn('exp',explode(split('count',' ')))
# d=df3.groupby('exp').agg(count('exp')).select('count(exp)')
#
# print(d.rdd)
a=5
# for i in range(5):
#       for j in range(i):
#
#             print('*',end=" ")
#
#       for i in range(a):
#             print('?')
#
# for i in range(5,0,-1):
#
#       for k in range(1,6-i):
#             print('*',end="")
#
#       for j in range(1,1+i):
#             print("?",end="")
#       print('\n')

import os
import re
#
# a=os.listdir(r"C:\Users\Dell\OneDrive\Desktop\JBG info")
#
# from _datetime import datetime
#
#
# print(tabDays[1])
#
# for i in a:
#
#   print((os.listdir(r"C:\Users\Dell\OneDrive\Desktop\JBG info"+'\\'+i)))








