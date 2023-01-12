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

module "module_s3" {
  source      = "./s3_module"
  bucket_name = var.bucket_name
}

