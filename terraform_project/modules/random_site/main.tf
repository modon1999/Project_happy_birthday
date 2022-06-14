# ------------------------------------------------------------------------------
# Модуль создания случайной строки от 1 до 3, для случайного выбора шаблона сайта-поздравления
# ------------------------------------------------------------------------------

#============== Provider ==============

provider "aws" {
  region = "eu-central-1"
}

#==================================

resource "random_integer" "priority" {
  min = 1
  max = 3
  keepers = {
    # Generate a new integer each time we switch to a new listener ARN
    listener_arn = "${var.listener_arn}"
  }
}
