

Deploying the application on GCP is a multi-step process:

- Create a GKE cluster [here](https://console.cloud.google.com/kubernetes/list?authuser=0&project=wewyse-centralesupelec-ftv), make sure you select the proper service account and create a local keyfile:

```
gcloud iam service-accounts keys create --iam-account "web-runtime@wewyse-centralesupelec-ftv.iam.gserviceaccount.com" service-account.json
```

- Next in a configured gcloud / kubectl local shell (with the corresponding username attached to `wewyse-centralesupelec-ftv` project), get access to the created cluster:

```
gcloud container clusters get-credentials [CLUSTER_NAME] 
```

- Verify the right context with `kubectl config view` and activate it with something similar to:

```
kubectl config use-context gke_wewyse-centralesupelec-ftv_europe-west1-b_speech-webapp-cluster-dev
```

- Add the service account authorizations and the password for the gcloud SQL in kubernetes secrets: 

``` 
kubectl create secret generic cloudsql-instance-credentials --from-file ./service-account.json
kubectl create secret generic postgres-password-dev \
    --from-literal=db_pass='[verycomplicatedpassword]'
```

- Deploy the application:

```
kubectl apply -f ./deployment/speech-webapp-single-deployment.yaml
```

- Add a load balancer from the interface.
- Setup domain name, SSL certificates etc.