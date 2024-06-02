#!sudo apt update
#!apt-get install openjdk-8-jdk-headless -qq > /dev/null
# https://www.apache.org/dyn/closer.lua/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3-scala2.13.tgz
#!wget -q https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
#!tar xf spark-3.5.1-bin-hadoop3.tgz
#!pip install -q findspark
#!pip install pyspark
#!pip install py4j
#import findspark
#findspark.init()
#findspark.find()
#import pyspark
