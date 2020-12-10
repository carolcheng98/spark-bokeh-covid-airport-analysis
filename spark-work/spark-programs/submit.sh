#!/bin/bash
if [ "$#" -ne 4 ] ; then
        echo "four arguments needed: inputfile  outputdirectory appfile instance#"
        exit
fi
echo "inputfile=$1 , outputdirectory=$2 appfile=$3 instance=$4"
spark-submit     --master k8s://https://10.212.96.128:6443 --deploy-mode cluster     --name energy     --conf spark.executor.instances=$4 --conf spark.kubernetes.container.image=python/spark-py:1.0 --conf spark.kubernetes.driver.volumes.hostPath.workdir.mount.path=/work --conf spark.kubernetes.driver.volumes.hostPath.workdir.mount.readOnly=false  --conf spark.kubernetes.driver.volumes.hostPath.workdir.options.path=/home/cc/work/spark_work  --conf spark.kubernetes.executor.volumes.hostPath.workdir.mount.path=/work --conf spark.kubernetes.executor.volumes.hostPath.workdir.mount.readOnly=false  --conf spark.kubernetes.executor.volumes.hostPath.workdir.options.path=/home/cc/work/spark_work local:///work/$3 -i file:///work/$1  -o file:///work/$2