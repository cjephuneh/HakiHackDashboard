import json
import openai
import requests

# Function to load person data from a script in a GitHub repo
def load_person_data():
    # GitHub raw script URL
    github_url = 'https://raw.githubusercontent.com/cjephuneh/HakiHackDashboard/dummydata/HakiHackDashboard/PoliceDB/dummydata.py'
    
    try:
        # Make a GET request to fetch the Python script
        response = requests.get(github_url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Execute the fetched script and retrieve the `person` variable
        exec(response.text)
        
        # The `person` variable should now be available in the current context
        return person_json
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub: {e}")
        return []

# Function to find a matching profile using OpenAI API
def find_matching_person(name=None, image_url=None):
    person_data = load_person_data()
    
    # Prepare a query based on the provided input
    if name and image_url:
        query = f"Find a person with the name '{name}' and image URL '{image_url}'."
    elif name:
        query = f"Find a person with the name '{name}'."
    elif image_url:
        query = f"Find a person with the image URL '{image_url}'."
    else:
        return None

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": query}
        ]
    )
    
    # Extract the response
    result = response.choices[0].message['content']
    
    # Check for matches in the person data
    for person in person_data:
        if (name and person['name'] == name) or (image_url and person['image'] == image_url):
            return person  # Return the matching profile
    
    return None

# Main execution
if __name__ == "__main__":
    # Set your OpenAI API key
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    
    # Input name or image URL from the user
    user_input = input("Enter the person's name or image URL: ")
    
    # Check if the input is a URL
    if user_input.startswith("http://") or user_input.startswith("https://"):
        profile = find_matching_person(image_url=user_input)
    else:
        profile = find_matching_person(name=user_input)

    if profile:
        print("Matching Profile Found:")
        print(json.dumps(profile, indent=2))
    else:
        print("No matching profile found.")
