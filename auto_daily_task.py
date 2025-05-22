# Define a function named `tasks` that takes a file path as input
def tasks(file):
    # Import helper functions from a module named helper_functions
    from helper_functions import get_llm_response, upload_txt_file
    
    # Open the input file in read mode
    f = open(file, "r")
    
    # Read the entire content of the file into the variable `today`
    today = f.read()
    
    # Close the file to free system resources
    f.close()
    
    # Print the contents of the file to the console (for debugging or inspection)
    print(today)
    
    # Create a prompt by combining a fixed instruction string with the contents of the file
    prompt = (""" For each task, describe the task, state the task complexity and time to complete.
    The tasks are:
    """ + today)
    
    # Call a helper function to get a response from an LLM based on the prompt
    response = get_llm_response(prompt)
    
    # Print the response to the console (for debugging or inspection)
    print(response)
    
    # Open (or create) a new file to save the LLM's response
    f = open("tasks_response.txt", "w")
    
    # Write the response to the file
    f.write(response)
    
    # Close the file to ensure the data is written and resources are freed
    f.close()

# Call a helper function that lets the user upload a text file (likely used in a UI like Streamlit)
upload_txt_file()

# Call the `tasks` function with the uploaded file name "tasks.txt"
tasks("tasks.txt")
