resource "aws_s3_bucket" "bucket" {
  bucket_prefix = "${var.name_bucket}-"
}

resource "aws_s3_bucket_acl" "acl" {
  bucket = aws_s3_bucket.bucket.id
  acl    = var.acl_policy
}

resource "aws_s3_bucket_website_configuration" "website" {
  count  = var.website == true ? 1 : 0
  bucket = aws_s3_bucket.bucket.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}
