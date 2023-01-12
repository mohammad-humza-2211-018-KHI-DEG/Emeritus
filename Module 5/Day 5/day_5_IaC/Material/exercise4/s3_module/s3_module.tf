variable "bucket_name" {
  type = string
}

resource "aws_s3_bucket" "s3_bucket" {
  bucket = var.bucket_name
}
resource "aws_s3_object" "day2_IaC_dir" {
  bucket = aws_s3_bucket.s3_bucket.id
  key    = "day2/IaC/"
}
