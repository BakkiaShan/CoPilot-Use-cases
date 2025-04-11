def log_message(message):
    # Function to log messages to the console
    print(f"[LOG] {message}")

def get_user_confirmation(prompt):
    # Function to prompt the user for confirmation
    response = input(f"{prompt} (y/n): ")
    return response.lower() == 'y'

def validate_input(input_value, valid_options):
    # Function to validate user input against a list of valid options
    return input_value in valid_options

def display_progress(step, total_steps):
    # Function to display progress of the migration process
    percentage = (step / total_steps) * 100
    print(f"Progress: {percentage:.2f}% ({step}/{total_steps})")