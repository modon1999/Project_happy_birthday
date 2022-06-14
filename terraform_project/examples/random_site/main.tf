#============== Provider ==============

provider "aws" {
  region = "eu-central-1"
}

#==================================

module "random_site" {
  source       = "../../modules/random_site"
  listener_arn = var.listener_arn
}
