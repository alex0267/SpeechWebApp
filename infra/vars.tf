variable "project" {}
variable "region" {
  default = "europe-west1"
}
variable "credentials" {
  default = "credentials.json"
}

variable "availability_type_prod" {
  description = "Availability type for HA"
}
variable "sql_instance_size_prod" {
  default     = "db-f1-micro"
  description = "Size of Cloud SQL instances"
}
variable "sql_disk_type_prod" {
  default     = "PD_SSD"
  description = "Cloud SQL instance disk type"
}
variable "sql_disk_size_prod" {
  default     = "10"
  description = "Storage size in GB"
}
variable "sql_require_ssl_prod" {
  default     = "false"
  description = "Enforce SSL connections"
}
variable "sql_master_zone_prod" {
  default     = "b"
  description = "Zone of the Cloud SQL master (a, b, ...)"
}
variable "sql_connect_retry_interval_prod" {
  default     = 60
  description = "The number of seconds between connect retries."
}
variable "sql_replica_zone_prod" {
  default     = "c"
  description = "Zone of the Cloud SQL replica (a, b, ...)"
}
variable "sql_user_prod" {
  default     = "postgres"
  description = "Username of the host to access the database"
}
variable "sql_pass_prod" {
  description = "Password of the host to access the database"
}

variable "availability_type_dev" {
  description = "Availability type for HA"
}
variable "sql_instance_size_dev" {
  default     = "db-f1-micro"
  description = "Size of Cloud SQL instances"

}
variable "sql_disk_type_dev" {
  default     = "PD_SSD"
  description = "Cloud SQL instance disk type"
}
variable "sql_disk_size_dev" {
  default     = "10"
  description = "Storage size in GB"
}
variable "sql_require_ssl_dev" {
  default     = "false"
  description = "Enforce SSL connections"
}
variable "sql_master_zone_dev" {
  default     = "b"
  description = "Zone of the Cloud SQL master (a, b, ...)"
}
variable "sql_connect_retry_interval_dev" {
  default     = 60
  description = "The number of seconds between connect retries."
}
variable "sql_user_dev" {
  default     = "postgres"
  description = "Username of the host to access the database"
}
variable "sql_pass_dev" {
  description = "Password of the host to access the database"
}