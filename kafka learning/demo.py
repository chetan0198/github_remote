# importing module 
import pyspark 

# importing sparksession from 
# pyspark.sql module 
from pyspark.sql import SparkSession 

# creating sparksession and giving 
# an app name 
spark = SparkSession.builder.appName('sparkdf').getOrCreate() 

# list of college data with dictionary 
data = [{'student_id': 12, 'name': 'sravan', 
		'address': 'kakumanu'}]

print(type(data),type(data[0].get('name')))


# creating a dataframe 
dataframe = spark.createDataFrame(data) 

# show data frame 
dataframe.show() 
