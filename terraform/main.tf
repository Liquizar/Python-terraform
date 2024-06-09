provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "example" {
  ami           = "ami-0f58b397bc5c1f2e8"
  instance_type = var.instance_type

  tags = {
    Name = "example-instance"
  }
}

output "instance_id" {
  value = aws_instance.example.id
}
