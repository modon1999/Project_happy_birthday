# ------------------------------------------------------------------------------
# Модуль создания политики AWS S3 Bucket
# ------------------------------------------------------------------------------

#============== Data ==============

data "aws_iam_policy_document" "allow_access_from_another_account" {
  statement {
    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = [
      "s3:GetObject",
    ]

    resources = [
      "${var.arn_bucket}/*",
    ]
  }
}

resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = var.name_bucket
  policy = data.aws_iam_policy_document.allow_access_from_another_account.json
}
