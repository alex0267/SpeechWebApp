### Infra provisioning

this directory must contains a credentials file provided by google named as
credentials.json


Some parameters can be provided in vars.tf, most should be set in a file *.tfvars, with the 
following elements:

```
project               = "wewyse-centralesupelec-ftv"
region                = "europe-west1"
#SQL prod
availability_type_prod = "REGIONAL"
sql_instance_size_prod = "db-f1-micro"
sql_disk_type_prod              = "PD_SSD"
sql_disk_size_prod              =  "10"
sql_require_ssl_prod            = "false"
sql_master_zone_prod            = "b"
sql_connect_retry_interval_prod = 60
sql_replica_zone_prod           =  "c"
sql_user_prod                   = "postgres"
sql_pass_prod                   = "XXXXXX"
#SQL dev
availability_type_dev = "ZONAL"
sql_instance_size_dev = "db-f1-micro"
sql_disk_type_dev     = "PD_SSD"
sql_disk_size_dev     =  "10"
sql_user_dev                   = "postgres"
sql_pass_dev                   = "XXXXXXX"
```

It is important to NOT change username, as currently GCP SQL psql accept only this one.


next command can be necessary:

```
export GOOGLE_PROJECT="wewyse-centralesupelec-ftv"
export GOOGLE_CLOUD_KEYFILE_JSON=$(cat /correct/path/to/project/credentials.json)
```

---

### List of usual commands

- init terraform 

`terraform init`

- obtain a list of ressources to be created

`terraform plan`

- create those ressources 

`terraform apply`

- destroy ressources (any such command implying destruction of information can be
rejected by the provider - manual intervention is then needed)

`terraform destroy`