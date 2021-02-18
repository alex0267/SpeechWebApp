

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

Pay attention that the IP address in the previous file points to the PRIVATE IP address of the right sql instance.

From here on, followed this tutorial with adaptations to our situation:
https://cloud.google.com/kubernetes-engine/docs/how-to/managed-certs

- Reserve IP address

```
gcloud compute addresses create ser-webapp-dev --global

gcloud compute addresses describe ser-webapp-dev --global
```

Check the resulting ip address

- Create a certificate

```
kubectl apply -f ./deployment/certificate-ser-webapp-dev.yaml
```

- Create a service that expose an internal IP with the right ports:

``` 
kubectl apply -f ./deployment/service-ser-webapp-dev.yaml
```

- Add an Ingress (HTTP-level load balancer):

```
kubectl apply -f ./deployment/ingress-ser-webapp-dev.yaml
```

- Check the IP address present in the ingress (up to 10/20 min of waiting):

```
kubectl get ingress
```

- Report the IP address in [Cloud DNS](https://console.cloud.google.com/net-services/dns/zones/speech-webapp/details?organizationId=96332070682&project=wewyse-centralesupelec-ftv) adding a type A record linking the IP address to the address that you entered for the certificate.

- Verify that the certificate is activated (15min):

```
kubectl describe managedcertificate certificate-ser-webapp-dev
```

- Visit the website with https:// protocol and make sure everything works.
