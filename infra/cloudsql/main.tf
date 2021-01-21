#PROD
provider "random" {}

resource "random_id" "id_prod" {
  byte_length = 4
  prefix = "sql-prod-"
}

resource "google_sql_database_instance" "master" {
  name = random_id.id_prod.hex
  region = var.region
  database_version = "POSTGRES_11"
  deletion_protection = false

  settings {
    availability_type = var.availability_type_prod
    tier = var.sql_instance_size_prod
    disk_type = var.sql_disk_type_prod
    disk_size = var.sql_disk_size_prod
    disk_autoresize = true

    ip_configuration {
      authorized_networks  {
        value = "0.0.0.0/0"
      }

      require_ssl = var.sql_require_ssl_prod
      ipv4_enabled = true
    }

    location_preference {
      zone = "${var.region}-${var.sql_master_zone_prod}"
    }

    backup_configuration {
      #      binary_log_enabled = true
      enabled = true
      start_time = "00:00"
    }
  }
}

resource "random_id" "id_prod_replica" {
  byte_length = 4
  prefix = "sql-prod-replica"
}
resource "google_sql_database_instance" "replica" {
  depends_on = [
    google_sql_database_instance.master,
  ]

  name = random_id.id_prod_replica.hex
  count = "1"
  region = var.region
  database_version = "POSTGRES_11"
  master_instance_name = google_sql_database_instance.master.name
  deletion_protection = false

  settings {
    tier = var.sql_instance_size_prod
    disk_type = var.sql_disk_type_prod
    disk_size = var.sql_disk_size_prod
    disk_autoresize = true

    location_preference {
      zone = "${var.region}-${var.sql_replica_zone_prod}"
    }
  }
}

resource "google_sql_user" "user_prod" {
  depends_on = [
    google_sql_database_instance.master,
    google_sql_database_instance.replica,
  ]

  instance = google_sql_database_instance.master.name
  name = var.sql_user_prod
  password = var.sql_pass_prod
}


#DEV

resource "random_id" "id_dev" {
  byte_length = 4
  prefix = "sql-dev-"
}

resource "google_sql_database_instance" "master_dev" {
  name = random_id.id_dev.hex
  region = var.region
  database_version = "POSTGRES_11"
  deletion_protection = false


  settings {
    availability_type = var.availability_type_dev
    tier = var.sql_instance_size_dev
    disk_type = var.sql_disk_type_dev
    disk_size = var.sql_disk_size_dev
    disk_autoresize = true

    ip_configuration {
      authorized_networks  {
        value = "0.0.0.0/0"
      }

      require_ssl = var.sql_require_ssl_dev
      ipv4_enabled = true
    }

    location_preference {
      zone = "${var.region}-${var.sql_master_zone_dev}"
    }

    backup_configuration {
      #      binary_log_enabled = true
      enabled = true
      start_time = "00:00"
    }
  }
}

resource "google_sql_user" "user" {
  depends_on = [
    google_sql_database_instance.master_dev,
  ]

  instance = google_sql_database_instance.master_dev.name
  name = var.sql_user_dev
  password = var.sql_pass_dev
}

