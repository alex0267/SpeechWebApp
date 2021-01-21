output "dev_bucket_url" {
  value = google_storage_bucket.swa_dev.url
}
output "test_bucket_url" {
  value = google_storage_bucket.swa_test.url
}
output "prod_bucket_url" {
  value = google_storage_bucket.swa_prod.url
}

output "master_instance_sql_ipv4" {
  value       = module.cloudsql.master_instance_sql_ipv4
  description = "The IPv4 address assigned for master"
}

output "master_instance_sql_ipv4_dev" {
  value       = module.cloudsql.master_instance_sql_ipv4_dev
  description = "The IPv4 address assigned for master dev"
}