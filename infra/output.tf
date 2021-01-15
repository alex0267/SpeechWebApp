output "dev_bucket_url" {
  value = google_storage_bucket.swa_dev.url
}
output "test_bucket_url" {
  value = google_storage_bucket.swa_test.url
}
output "prod_bucket_url" {
  value = google_storage_bucket.swa_prod.url
}