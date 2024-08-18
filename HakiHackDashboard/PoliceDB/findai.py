import json
import requests
from transformers import pipeline
from pprint import pprint

def load_person_data():
    # Make API request
    person = []

    # Add first person data
    response = requests.get('https://random-person-generator.com/api')
    data = response.json()
    person.append({
        'name': data['identification']['full_name'],
        'dob': data['identification']['date_of_birth'],
        'email': data['contact_information']['email_address'],
        'service_num': data['financial_information']['cvv2'],
        'image': data['profile_photo']['256x256']
    })

    # Generate more data
    for i in range(10):
        response = requests.get('https://random-person-generator.com/api')
        data = response.json()

        person.append({
            'name': data['identification']['full_name'],
            'dob': data['identification']['date_of_birth'],
            'email': data['contact_information']['email_address'],
            'service_num': data['financial_information']['cvv2'],
            'image': data['profile_photo']['256x256']
        })

    return person  # Return the list directly

data = load_person_data()

# Load the text generation model
model = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

def find_matching_person(name=None, image_url=None):
    person_data = data

    if name or image_url:
        if name:
            # Prepare a query for the model (optional, depending on your needs)
            query = f"Find a person with the name '{name}'."
            response = model(query, max_length=500, truncation=True)
            result = response[0]['generated_text']

        # Check for matches in the person data
        matches = []
        for person in person_data:
            if (name and name.lower() in person['name'].lower()) or (image_url and person['image'] == image_url):
                matches.append(person)

        return matches  # Return all matching profiles

    return None

# Main execution
if __name__ == "__main__":
    # Load the text generation model
    model = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

    # Input name or image URL from the user
    user_input = input("Enter the person's name or image URL: ")

    # Check if the input is a URL
    if user_input.startswith("http://") or user_input.startswith("https://"):
        profile = find_matching_person(image_url=user_input)
    else:
        profile = find_matching_person(name=user_input)

    if profile:
        print("Matching Profile Found:")
        pprint(json.dumps(profile, indent=2))
    else:
        print("No matching profile found.")

