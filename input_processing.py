# utils/input_processing.py
def process_input(input_data):
    # Validate the input data
    if not input_data["job_title"]:
        raise ValueError("Job title is required")
    if not input_data["company_name"]:
        raise ValueError("Company name is required")

    # Format the input data
    input_data["job_title"] = input_data["job_title"].strip()
    input_data["company_name"] = input_data["company_name"].strip()

    return input_data