provider "aws" {
    profile = "terraform"
    region  = "us-west-2" 
}

terraform {
  required_providers {
      aws = {
          source = "hashicorp/aws"
          version = ">=3.36.0"
      }
  }
}