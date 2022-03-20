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

variable "bucket_policy" {
  description = "ACL polycy"
  type        = string
  default     = ""
}
