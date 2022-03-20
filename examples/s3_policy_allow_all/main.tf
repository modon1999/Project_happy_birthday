#============== Provider ==============

provider "aws" {
  region = "eu-central-1"
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
  name_bucket = "example"
  acl_policy  = "private"
}
