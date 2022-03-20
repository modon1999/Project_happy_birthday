resource "aws_s3_bucket_website_configuration" "happy_birthday" {
  bucket = var.name_bucket

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}

resource "aws_s3_object" "object_upload1" {
  for_each     = fileset(var.folder_site, "*.html")
  bucket       = aws_s3_bucket.happy_birthday.id
  key          = each.value
  source       = "${var.folder_site}/${each.value}"
  content_type = "text/html"
  # etag         = filemd5("../../../sites/woman/1/${each.value}")
}

resource "aws_s3_object" "object_upload2" {
  for_each     = fileset(var.folder_site, "*.js")
  bucket       = aws_s3_bucket.happy_birthday.id
  key          = each.value
  source       = "${var.folder_site}/${each.value}"
  content_type = "application/javascript"
  # etag         = filemd5("../../../sites/woman/1/${each.value}")
}

resource "aws_s3_object" "object_upload3" {
  for_each     = fileset(var.folder_site, "*.css")
  bucket       = aws_s3_bucket.happy_birthday.id
  key          = each.value
  source       = "${var.folder_site}/${each.value}"
  content_type = "text/css"
  # etag         = filemd5("../../../sites/woman/1/${each.value}")
}

resource "aws_s3_object" "object_upload4" {
  for_each     = fileset(var.folder_site / images, "*.jpeg")
  bucket       = aws_s3_bucket.happy_birthday.id
  key          = "images/${each.value}"
  source       = "${var.folder_site}/images/${each.value}"
  content_type = "image/jpeg"
  # etag         = filemd5("../../../sites/woman/1/${each.value}")
}

resource "aws_s3_object" "object_upload5" {
  for_each     = fileset(var.folder_site / blog, "*.html")
  bucket       = aws_s3_bucket.happy_birthday.id
  key          = "blog/${each.value}"
  source       = "${var.folder_site}/blog/${each.value}"
  content_type = "text/html"
  # etag         = filemd5("../../../sites/woman/1/${each.value}")
}
