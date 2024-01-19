resource "aws_instance" "ubuntu" {
  ami           = "ami-06478978e5e72679a"
  instance_type = "t2.micro"

  tags = {
    Name = "my-ec2-instance"
  }

  provisioner "local-exec" {
    command = "aws ec2 wait instance-running --instance-ids ${self.id}"
  }
}