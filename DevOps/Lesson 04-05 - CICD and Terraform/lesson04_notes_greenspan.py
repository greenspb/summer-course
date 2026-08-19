#Refer to https://github.com/greenspb/skills-test-with-action, particularly .github/workflows/python-coverage.yml
#https://developer.hashicorp.com/terraform/sandbox terraform website available terraform sandboxes

cat README.md
cat main.tf #will be named "web", will be of instance_type ts.small
terraform init #will compiles all .tf files
terraform plan  #only specified ami, size in instance_type,
ls
cat localstack_override.tf
cat terraform.tf #using hashipcorp/aws
terraform apply #same as plan, plan is not required, just good practice, apply tells you the resources you are going to provision, after you hit yes, it will provision it and create it
yes
ls
terraform state list
terraform destroy
yes
