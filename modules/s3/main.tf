resource "aws_s3_bucket" "bucket" {
  bucket_prefix = "${var.name_bucket}-"
}

resource "aws_s3_bucket_acl" "acl" {
  bucket = aws_s3_bucket.bucket.id
  acl    = var.acl_policy
}

resource "aws_s3_bucket_policy" "bucket_policy" {
  count  = var.bucket_policy == "" ? 0 : 1
  bucket = aws_s3_bucket.bucket.id
  policy = var.bucket_policy
}
