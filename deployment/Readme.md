
# General deployment instructions

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

Before deploying the application, we need to setup the environment variables that will be fed to the service docker images. As can be seen in [speech-webapp-single-deployement.yaml](./speech-webapp-single-deployment.yaml), there are 5 environment variables that will be read from the [Kubernetes secrets](https://kubernetes.io/docs/concepts/configuration/secret/):

- `RECAPTCHA`, the reCAPTCHA secret key: it is to be stored with `kubectl create secret generic recaptcha --from-literal=secret_key=<SECRET_KEY>`
- `CREDENTIALS_PRIVATE_KEY`, `CREDENTIALS_PRIVATE_KEY_ID` and `CREDENTIALS_CLIENT_ID`, respectively the bucket's private key, private key id and client id. The can be set as follows: `kubectl create secret generic bucket-credentials --from-literal=client_id=<CLIENT_ID> --from-literal=private_key=<PRIVATE_KEY> --form-literal=private_key_id=<PRIVATE_KEY_ID>`.
- `POSTGRES_PASSWORD`, the Postgresql credentials, which can be set with: `kubectl create secret generic postgres-password-dev --from-literal=db_pass=<DB_PASSWORD>`

Once these secrets have been stored, you can deploy as follows:

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

- Create / request a domain name (e.g. speech-emotion-recognition.app) on [Cloud domains](https://console.cloud.google.com/net-services/domains/registrations/list?authuser=0&project=wewyse-centralesupelec-ftv). Once it is activated, you can continue.

- Report the previous IP address in [Cloud DNS](https://console.cloud.google.com/net-services/dns/zones/speech-webapp/details?organizationId=96332070682&project=wewyse-centralesupelec-ftv) adding a type A record linking the IP address to the address that you entered for the certificate. You also have to activate the IP / domain name on [Google Domains](https://domains.google.com/).

- Verify that the certificate is activated (15min):

```
kubectl describe managedcertificate certificate-ser-webapp-dev
```

- Visit the website with https:// protocol and make sure everything works.

# Test on dev instance

A deployed testing instance runs at https://dev.speech-emotion-recognition.app

All commits and merge onto 'dev' or 'feature/' containing branches will be automatically built in Cloud build.
The images will be stored in gcr.io : `speech-web-app-dev` (the production images are under `speech-web-app`)

Once the image is built, you can manually deploy it.

For that all you need to do is to get the tag (not the name) from the [container registry](https://console.cloud.google.com/gcr/images/wewyse-centralesupelec-ftv/GLOBAL/speech-web-app-dev?project=wewyse-centralesupelec-ftv&authuser=0&gcrImageListsize=30) that matches the images you want to deploy and paste them into `./deployment/speeech-webapp-single-deployment-test.yaml` on lines 17 and 67 in place of the currently existing sha1 codes.

Next, you will need to deploy your image with the following:

```
kubectl apply -f ./deployment/speech-webapp-single-deployment-test.yaml
```

And the deployed version should be available after  a few minutes.

Please, commit and save the changes you make to the deployment file.
