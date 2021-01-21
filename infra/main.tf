module "cloudsql" {
  source                     = "./cloudsql"
  region                     = var.region
  availability_type_prod     = var.availability_type_prod
  sql_instance_size_prod          = var.sql_instance_size_prod
  sql_disk_type_prod              = var.sql_disk_type_prod
  sql_disk_size_prod              = var.sql_disk_size_prod
  sql_require_ssl_prod            = var.sql_require_ssl_prod
  sql_master_zone_prod            = var.sql_master_zone_prod
  sql_connect_retry_interval_prod = var.sql_connect_retry_interval_prod
  sql_replica_zone_prod           = var.sql_replica_zone_prod
  sql_user_prod                   = var.sql_user_prod
  sql_pass_prod                   = var.sql_pass_prod

  availability_type_dev          = var.availability_type_dev
  sql_instance_size_dev          = var.sql_instance_size_dev
  sql_disk_type_dev              = var.sql_disk_type_dev
  sql_disk_size_dev              = var.sql_disk_size_dev
  sql_require_ssl_dev            = var.sql_require_ssl_dev
  sql_master_zone_dev            = var.sql_master_zone_dev
  sql_connect_retry_interval_dev = var.sql_connect_retry_interval_dev
  sql_user_dev                   = var.sql_user_dev
  sql_pass_dev                   = var.sql_pass_dev
}