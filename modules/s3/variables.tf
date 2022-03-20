variable "name_bucket" {
  description = "Name of bucket"
  type        = string
  default     = "default_bucket"
}

variable "acl_policy" {
  description = "ACL polycy"
  type        = string
  default     = "private"
}

variable "website" {
  description = "Create S3-website"
  type        = bool
  default     = false
}
