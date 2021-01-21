output "master_instance_sql_ipv4" {
  value       = google_sql_database_instance.master.ip_address.0.ip_address
  description = "The IPv4 address assigned for master"
}

output "master_instance_sql_ipv4_dev" {
  value       = google_sql_database_instance.master_dev.ip_address.0.ip_address
  description = "The IPv4 address assigned for master dev"
}