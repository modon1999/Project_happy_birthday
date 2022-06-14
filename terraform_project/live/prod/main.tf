#============== Provider ==============

provider "aws" {
  region = "eu-central-1"
}

#============== Templatefile ==============

module "random_site" {
  source       = "../../modules/random_site"
  listener_arn = var.name_birthday_boy
}

data "template_file" "index_file" {
  template = file("../../../sites/${var.sex_birthday_boy}/${module.random_site.random_intenger}/index.html.tpl")
  vars = {
    name = var.name_birthday_boy
  }
}

resource "null_resource" "create_index_file" {
  provisioner "local-exec" {
    command = "echo $INDEX_FILE > ../../../sites/${var.sex_birthday_boy}/${module.random_site.random_intenger}/index.html"
    environment = {
      INDEX_FILE = data.template_file.index_file.rendered
    }
  }
}

#============== S3 Bucket ==============

module "s3_bucket" {
  source      = "../../modules/s3"
  name_bucket = "happy-birthday"
  acl_policy  = "private"
  website     = true
}

module "policy_bucket" {
  source      = "../../modules/s3_policy_allow_all"
  arn_bucket  = module.s3_bucket.arn_bucket
  name_bucket = module.s3_bucket.name_bucket
}

# ============== Website ==============

module "website" {
  source      = "../../modules/website_happy_birthday"
  name_bucket = module.s3_bucket.name_bucket
  folder_site = "../../../sites/${var.sex_birthday_boy}/${module.random_site.random_intenger}"
  depends_on  = [null_resource.create_index_file, module.random_site]
}
