
# GCP variables
variable "region" {
  description = "Region of resources"
}

# Cloud SQL variables prod

variable "availability_type_prod" {
  description = "Availability type for HA"
}

variable "sql_instance_size_prod" {
  description = "Size of Cloud SQL instances"
}

variable "sql_disk_type_prod" {
  description = "Cloud SQL instance disk type"
}

variable "sql_disk_size_prod" {
  description = "Storage size in GB"
}

variable "sql_require_ssl_prod" {
  description = "Enforce SSL connections"
}

variable "sql_connect_retry_interval_prod" {
  description = "The number of seconds between connect retries."
}

variable "sql_master_zone_prod" {
  description = "Zone of the Cloud SQL master (a, b, ...)"
}

variable "sql_replica_zone_prod" {
  description = "Zone of the Cloud SQL replica (a, b, ...)"
}

variable "sql_user_prod" {
  description = "Username of the host to access the database"
}

variable "sql_pass_prod" {
  description = "Password of the host to access the database"
}

# Cloud SQL variables dev

variable "availability_type_dev" {
  description = "Availability type for HA"
}

variable "sql_instance_size_dev" {
  description = "Size of Cloud SQL instances"
}

variable "sql_disk_type_dev" {
  description = "Cloud SQL instance disk type"
}

variable "sql_disk_size_dev" {
  description = "Storage size in GB"
}

variable "sql_require_ssl_dev" {
  description = "Enforce SSL connections"
}

variable "sql_connect_retry_interval_dev" {
  description = "The number of seconds between connect retries."
}

variable "sql_master_zone_dev" {
  description = "Zone of the Cloud SQL master (a, b, ...)"
}



variable "sql_user_dev" {
  description = "Username of the host to access the database"
}

variable "sql_pass_dev" {
  description = "Password of the host to access the database"
}