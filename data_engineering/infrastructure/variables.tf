variable "environment" {
    description = "Environment"
    type = string
    default = "dev"
}

variable "profile" {
    description = "AWS profile"
    type = string
    default = "terraform"
}

variable "region" {
    description = " AWS region where resources will be deployed"
    type = string
    default = "us-west-2"
}

