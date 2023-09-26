# This Terraform script will generate a local file with the given content

resource "local_file" "foo" {
  content  = "This is a local text file, created using Terraform."
  filename = "${path.module}/files/terraform-local-file.txt"
}
