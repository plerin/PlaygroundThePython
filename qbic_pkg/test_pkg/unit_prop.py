import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # sys.path에 test_pkg 상위 폴더를 추가한다. == qbic_pkg를 추가하니까 하위 모든 패키지 사용할 수 있다.

from pyspark import SparkConf, SparkContext
from prop_pkg import spark_prop as prop


if __name__ == '__main__':
    conf = SparkConf()
    sc = SparkContext(conf=prop.adapt_conf().set_medium_prop(conf))
    print(sc)
    sc.stop()