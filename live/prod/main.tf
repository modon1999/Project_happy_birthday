#============== Provider ==============

provider "aws" {
  region = "eu-central-1"
}

#============== Templatefile ==============

data "template_file" "index_file" {
  template = file("../../../sites/woman/1/index.html.tpl")
  vars = {
    name = "Викулечка"
  }
}

resource "null_resource" "create_index_file" {
  provisioner "local-exec" {
    command = "echo $INDEX_FILE >> ../../../sites/woman/1/index.html"
    environment = {
      INDEX_FILE = data.template_file.index_file.rendered
    }
  }
}

#============== Data ==============

module "policy_bucket" {
  source      = "github.com/modon1999/Project_happy_birthday//modules/s3_policy_allow_all?ref=v0.0.4"
  arn_bucket  = module.s3_bucket.arn_bucket
  name_bucket = module.s3_bucket.name_bucket
}

#============== S3 Bucket ==============

module "s3_bucket" {
  source      = "github.com/modon1999/Project_happy_birthday//modules/s3?ref=v0.0.4"
  name_bucket = "vikilichka-happy-birthday"
  acl_policy  = "private"
  website     = true
}

#============== Website ==============

module "website" {
  source      = "github.com/modon1999/Project_happy_birthday//modules/website_happy_birthday?ref=v0.0.4"
  name_bucket = module.s3_bucket.name_bucket
  folder_site = "../../../sites/woman/1"
  # depends_on  = [null_resource.create_index_file]
}
