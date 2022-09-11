terraform {
    backend "s3" {
        profile = "terraform"
        bucket  = "terraform-henry"
        key     = "state/data-engineering-terraform/tfstate"
        region  = "us-west-2"
    }
}
