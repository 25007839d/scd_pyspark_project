conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("Test")

sc = SparkContext(conf=conf)

# Setup gcs Hadoop Configurations programmatically
# Require Google Service account
sc._jsc.hadoopConfiguration().set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
sc._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
sc._jsc.hadoopConfiguration().set("fs.gs.project.id", "inlaid-tribute-353619")
sc._jsc.hadoopConfiguration().set("fs.gs.auth.service.account.enable", "true")

spark = SparkSession.builder \
    .master('local[*]') \
    .getOrCreate()

spark._jsc.hadoopConfiguration().set("fs.gs.auth.service.account.keyfile",
                                     r"/home/g25007839d/__pycache__/inlaid-tribute-353619-3e4a267ca47b.json")
conf = SparkConf()\
    .setMaster("local[*]")\
    .setAppName("Test")   

sc = SparkContext(conf=conf)

# Setup gcs Hadoop Configurations programmatically
#Require Google Service account
sc._jsc.hadoopConfiguration().set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
sc._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
sc._jsc.hadoopConfiguration().set("fs.gs.project.id", "inlaid-tribute-353619")
sc._jsc.hadoopConfiguration().set("fs.gs.auth.service.account.enable", "true")


spark = SparkSession.builder\
    .master('local[*]')\
    .getOrCreate()
    
spark._jsc.hadoopConfiguration().set("fs.gs.auth.service.account.keyfile", r"/home/g25007839d/__pycache__/inlaid-tribute-353619-3e4a267ca47b.json")
spark._jsc.hadoopConfiguration().set("fs.gs.auth.service.account.keyfile", r"/home/g25007839d/__pycache__/inlaid-tribute-353619-3e4a267ca47b.json")