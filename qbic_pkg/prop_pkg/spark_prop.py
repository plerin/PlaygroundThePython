from pyspark import SparkConf, SparkContext

class adapt_conf():
    
    def set_small_prop(self,conf):
        conf = conf.setAppName('[S]_ run-spark').setMaster('local') \
                    .set('spark.driver.memory', '5g') \
		            .set("spark.yarn.am.memory", "5g") \
		            .set("spark.executor.instance", "10") \
		            .set("spark.executor.memory", "8g") \
                    .set("spark.executor.cores", "2") 
        return conf
    
    def set_medium_prop(self,conf):
        conf = conf.setAppName('[M]_ run-spark').setMaster('local') \
                    .set('spark.driver.memory', '30g') \
		            .set("spark.yarn.am.memory", "30g") \
		            .set("spark.executor.instance", "10") \
		            .set("spark.executor.memory", "10g") \
                    .set("spark.executor.cores", "2") 
        return conf
    
    def set_large_prop(self,conf):
        conf = conf.setAppName('[L]_ run-spark').setMaster('local') \
                    .set('spark.driver.memory', '50g') \
		            .set("spark.yarn.am.memory", "50g") \
		            .set("spark.executor.instance", "10") \
		            .set("spark.executor.memory", "20g") \
                    .set("spark.executor.cores", "3") 
        return conf

if __name__ == '__main__':
    conf = SparkConf()
    adapt_conf = adapt_conf().set_medium_prop(conf)
    sc = SparkContext(conf=adapt_conf)
    print(sc.getConf().getAll()) # 설정 확인
    sc.stop()