output "website_domain" {
  value       = module.s3_bucket.website_endpoint
  description = "Domain website"
}
