terraform {
  backend "gcs"{
    bucket      = "wewyse-centralesupelec-ftv-terraform-state"
    prefix      = "dev"
    credentials = "credentials.json"
  }
}