from pyspark import SparkConf, SparkContext

#conf = SparkConf().setAppName('PySpark Basic').setMaster('local')

class process_small():
    sc = SparkContext()
    def __init__(self):
        self.conf = self.conf.setAppName('qbic-spark').setMaster('local') \
                    .set('spark.driver.memory', '5g') \
		            .set("spark.yarn.am.memory", "5g") \
		            .set("spark.executor.instance", "10") \
		            .set("spark.executor.memory", "8g") \
                    .set("spark.executor.cores", "2") \

        sc = SparkContext(conf=conf)

    def get_context(self):
        return sc
        

# if __name__ == '__main__':
#     small = process_small().get_context()
#     print(type(small))