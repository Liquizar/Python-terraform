# Terraform Automation with `python-terraform`

This repository demonstrates how to automate Terraform operations using the `python-terraform` module. It includes a detailed example that covers initialization, planning, applying configurations, and retrieving outputs.

## Folder Structure

```
Python-terraform/
│
├── deploy_infrastructure.py
│
└── terraform/
    ├── main.tf
    └── variables.tf
```

### Files

- `deploy_infrastructure.py`: Python script to automate Terraform operations.
- `terraform/main.tf`: Terraform configuration file for provisioning an AWS EC2 instance.
- `terraform/variables.tf`: Terraform variables file.

## Steps to Run the Example

1. **Install Terraform and `python-terraform`:**

   - Download and install Terraform from the [official website](https://www.terraform.io/downloads.html).
   - Install the `python-terraform` library using pip:
     ```sh
     pip install python-terraform
     ```

2. **Set Up the Directory Structure:**

   - Create the `project-root` directory.
   - Inside `project-root`, create the `deploy_infrastructure.py` file.
   - Create the `terraform` directory inside `project-root`.
   - Inside the `terraform` directory, create the `main.tf` and `variables.tf` files.

3. **Populate the Files with Content:**

   - Copy the provided content into the respective files.

4. **Run the Python Script:**
   - Navigate to the `project-root` directory in your terminal.
   - Execute the Python script:
     ```sh
     python deploy_infrastructure.py
     ```

## Concepts Covered

### 1. Introduction to Terraform

Terraform is an open-source infrastructure as code (IaC) tool that allows you to define and provision infrastructure using a declarative configuration language.

### 2. What is `python-terraform`?

`python-terraform` is a Python wrapper for Terraform commands. It facilitates automation of Terraform operations via Python scripts.

### 3. Setting Up `python-terraform`

Install Terraform and `python-terraform` using the following commands:

```sh
pip install python-terraform
```

### 4. Basic Usage of `python-terraform`

**Initializing a Terraform Working Directory:**

```python
from python_terraform import Terraform

tf = Terraform()
tf.init()
```

### 5. Terraform Commands in Python

**Plan and Apply:**

```python
# Planning
return_code, stdout, stderr = tf.plan()

# Applying
return_code, stdout, stderr = tf.apply(skip_plan=True)
```

### 6. Handling Terraform Variables

**Passing Variables to Terraform:**

```python
return_code, stdout, stderr = tf.apply(vars={"aws_region": "us-west-2"})
```

### 7. Managing Terraform Outputs

**Extracting Outputs:**

```python
output = tf.output()
print(output)
```

### 8. Error Handling and Debugging

**Capturing and Handling Errors:**

```python
try:
    return_code, stdout, stderr = tf.apply()
    if return_code != 0:
        print(f"Error: {stderr}")
except Exception as e:
    print(f"Exception occurred: {str(e)}")
```

### 9. Advanced Topics

**Managing Terraform State:**
Terraform state is critical for tracking the resources it manages. Use remote backends for enhanced state management.

**Creating Custom Workflows:**

```python
def deploy_infrastructure():
    tf.init()
    return_code, stdout, stderr = tf.plan()
    if return_code == 0:
        return_code, stdout, stderr = tf.apply(skip_plan=True)
        if return_code != 0:
            print(f"Apply failed: {stderr}")
    else:
        print(f"Plan failed: {stderr}")

deploy_infrastructure()
```

## Conclusion

This example demonstrates how to use `python-terraform` to automate infrastructure management with Terraform, covering initialization, planning, applying configurations, and retrieving outputs. Follow the steps to set up your environment and run the script to see the automation in action.

Feel free to explore and modify the scripts and configurations to suit your needs!
