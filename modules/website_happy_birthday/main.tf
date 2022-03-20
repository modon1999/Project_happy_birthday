resource "aws_s3_object" "object_upload1" {
  for_each     = fileset(var.folder_site, "*.html")
  bucket       = var.name_bucket
  key          = each.value
  source       = "${var.folder_site}/${each.value}"
  content_type = "text/html"
  # etag         = filemd5("../../../sites/woman/1/${each.value}")
}

resource "aws_s3_object" "object_upload2" {
  for_each     = fileset(var.folder_site, "*.js")
  bucket       = var.name_bucket
  key          = each.value
  source       = "${var.folder_site}/${each.value}"
  content_type = "application/javascript"
  # etag         = filemd5("../../../sites/woman/1/${each.value}")
}

resource "aws_s3_object" "object_upload3" {
  for_each     = fileset(var.folder_site, "*.css")
  bucket       = var.name_bucket
  key          = each.value
  source       = "${var.folder_site}/${each.value}"
  content_type = "text/css"
  # etag         = filemd5("../../../sites/woman/1/${each.value}")
}

resource "aws_s3_object" "object_upload4" {
  for_each     = fileset("${var.folder_site}/images", "*.jpeg")
  bucket       = var.name_bucket
  key          = "images/${each.value}"
  source       = "${var.folder_site}/images/${each.value}"
  content_type = "image/jpeg"
  # etag         = filemd5("../../../sites/woman/1/${each.value}")
}

resource "aws_s3_object" "object_upload5" {
  for_each     = fileset("${var.folder_site}/blog", "*.html")
  bucket       = var.name_bucket
  key          = "blog/${each.value}"
  source       = "${var.folder_site}/blog/${each.value}"
  content_type = "text/html"
  # etag         = filemd5("../../../sites/woman/1/${each.value}")
}
