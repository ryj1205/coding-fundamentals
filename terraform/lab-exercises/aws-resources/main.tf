# This Terraform script allows you to provision an EC2 instance in AWS.
# NOTE: You must input your own access and secret keys via the AWS CLI in order for this to work in your AWS account.

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "eu-west-2"
}

resource "aws_instance" "example_server" {
  ami           = "ami-0b25f6ba2f4419235" # Amazon Linux 2023 AMI (Free Tier)
  instance_type = "t2.micro"

  tags = {
    Name = "EC2_Ubuntu_Terraform"
  }
}
