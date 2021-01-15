#buckets
#test
resource "google_storage_bucket" "swa_test" {
  name          = "swa-test-bucket"
  location      = "EU"
  force_destroy = true
  project     = var.project
}
#dev
resource "google_storage_bucket" "swa_dev" {
  name          = "swa-dev-bucket"
  location      = "EU"
  force_destroy = true
  project     = var.project
}
#prod
resource "google_storage_bucket" "swa_prod" {
  name          = "swa-prod-bucket"
  location      = "EU"
  force_destroy = true
  project     = var.project
}