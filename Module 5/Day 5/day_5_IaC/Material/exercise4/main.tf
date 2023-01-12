terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.20.0"
    }
  }
}

provider "aws" {
  region = "ap-northeast-1"
  
}

module "s3_module" {
  source      = "./s3_module"
  bucket_name = var.bucket_name
}

