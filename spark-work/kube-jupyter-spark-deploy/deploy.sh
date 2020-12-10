kubectl delete deployment --ignore-not-found my-notebook-deployment
kubectl delete service --ignore-not-found my-notebook-deployment

kubectl  create -f driver-deployment.yaml