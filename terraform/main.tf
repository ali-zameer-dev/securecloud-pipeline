provider "aws" {
  region = "ap-south-1"
}

# Intentionally misconfigured for scanning demo
resource "aws_s3_bucket" "app_bucket" {
  bucket = "securecloud-app-bucket"
}

resource "aws_s3_bucket_public_access_block" "app_bucket" {
  bucket = aws_s3_bucket.app_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_security_group" "app_sg" {
  name = "securecloud-sg"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
