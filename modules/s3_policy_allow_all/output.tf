output "policy_json" {
  value       = data.aws_iam_policy_document.allow_access_from_another_account.json
  description = "Bucket policy in json"
}
