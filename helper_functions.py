# Import necessary modules
import os  # For interacting with the operating system and environment variables
from openai import OpenAI  # Import the OpenAI client class to interact with the API
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load the environment variables from the .env file and override any existing ones
load_dotenv('.env', override=True)

# Retrieve the OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the retrieved API key
client = OpenAI(api_key=openai_api_key)


# Define a function to send a prompt to the LLM and print the response
def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT-4o-mini model. The function then prints the response of the model.
    """
    try:
        # Check if the input is a string; if not, raise an error
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        
        # Send the prompt to the GPT-4o-mini model via the OpenAI client
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Specify the model
            messages=[  # Construct the message history
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,  # Set deterministic response
        )
        
        # Extract the response content from the completion object
        response = completion.choices[0].message.content
        
        # Print the response to the console
        print(response)
    
    # Handle a potential TypeError during processing
    except TypeError as e:
        print("Error:", str(e))


# Define a function to send a prompt to the LLM and return the response as a string
def get_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT-4o-mini model. The function then saves the response of the model as
    a string.
    """
    # Send the prompt to the GPT-4o-mini model via the OpenAI client
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Specify the model
        messages=[  # Construct the message history
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,  # Set deterministic response
    )
    
    # Extract the response content from the completion object
    response = completion.choices[0].message.content
    
    # Return the response as a string
    return response
