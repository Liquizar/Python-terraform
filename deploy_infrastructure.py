from python_terraform import Terraform
import sys

def initialize_terraform(tf):
    print("Initializing Terraform...")
    return_code, stdout, stderr = tf.init()
    if return_code != 0:
        print(f"Initialization failed: {stderr}")
        sys.exit(1)
    print("Initialization successful.")
    print(stdout)

def plan_infrastructure(tf, variables):
    print("Planning infrastructure...")
    return_code, stdout, stderr = tf.plan(var=variables)
    if return_code != 2:
        print(f"Plan failed with return code {return_code}")
        print(f"Error: {stderr}")
        print(f"Standard Output: {stdout}")
        sys.exit(1)
    print("Plan successful.")
    print(stdout)
    return stdout

def apply_infrastructure(tf, variables, plan_output):
    print("Applying infrastructure...")
    
    return_code, stdout, stderr = tf.apply(skip_plan=False, input=False, var=variables, auto_approve=True)
    if return_code != 0:
        print(f"Apply failed with return code {return_code}")
        print(f"Error: {stderr}")
        print(f"Standard Output: {stdout}")
        sys.exit(1)
    print("Apply successful.")
    print(stdout)

def get_output(tf):
    print("Retrieving outputs...")
    output = tf.output()
    print("Outputs retrieved:")
    for key, value in output.items():
        print(f"{key}: {value['value']}")


def main():
    tf = Terraform(working_dir='./terraform')
    variables = {
        "aws_region": "ap-south-1",
        "instance_type": "t2.micro"
    }
    
    initialize_terraform(tf)
    plan_output = plan_infrastructure(tf, variables)
    apply_infrastructure(tf, variables, plan_output)
    get_output(tf)

if __name__ == "__main__":
    main()
