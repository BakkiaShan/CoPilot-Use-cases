#from gemini import GeminiClient
#from google.generativeai import GeminiClient

from google.generativeai import GenerativeModel
from google import  generativeai as genai
    


class GeminiIntegration:
    def __init__(self):
        
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.history = []

    def prompt_user(self, prompt):
        """
        Prompts the user with a message, sends the prompt to Gemini,
        and returns Gemini's response along with user confirmation.
        """
        print(prompt)  # Display the prompt to the user
        user_input = input(" (y/n): ").lower()  # Get user confirmation

        if user_input == 'y':
            gemini_response = self.send_to_gemini(prompt)
            print(f"Gemini's Response: {gemini_response}")
            self.history.append({"user": prompt, "gemini": gemini_response}) # Store interaction
            return gemini_response, True  # Return response and confirmation
        else:
            print("User declined. Skipping this step.")
            return None, False  # Return None and no confirmation

    def send_to_gemini(self, prompt):
        """Sends a prompt to the Gemini model and returns the response."""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error communicating with Gemini: {e}")
            return None

    def learn_from_history(self, new_information):
         """Updates Gemini with new information from the migration process."""
         self.history.append({"learning": new_information})
         #Potentially fine-tune the model or adjust prompts based on the new information
         print(f"Learned: {new_information}")
