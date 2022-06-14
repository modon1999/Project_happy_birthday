output "name_bucket" {
  value       = aws_s3_bucket.bucket.id
  description = "Name bucket"
}

output "arn_bucket" {
  value       = aws_s3_bucket.bucket.arn
  description = "Arn bucket"
}

output "website_endpoint" {
  value       = aws_s3_bucket.bucket.website_endpoint
  description = "Domain website"
  depends_on  = [aws_s3_bucket_website_configuration.website]
}
