data "aws_caller_identity" "current" {}

#################################################
#                 DATALAKE S3 BUCKET            #
#################################################
resource "aws_s3_bucket" "data_lake" {
  bucket        = "data-lake-${data.aws_caller_identity.current.account_id}"
  force_destroy = true
}

resource "aws_s3_bucket_acl" "data_lake_acl" {
  bucket = aws_s3_bucket.data_lake.id
  acl    = "private"
}
