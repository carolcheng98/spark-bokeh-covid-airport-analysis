if [ "$#" -ne 2 ] ; then
	echo "two args: from? to?"
	exit
fi
echo "from= $1 to=$2"
FROM=$1
TO=$2


scp -i ~/.ssh/xm.pem $FROM cc@129.114.24.206:~/work/spark_work/$TO