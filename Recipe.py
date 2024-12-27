from chatterbot import ChatBot
import pandas as pd
from chatterbot.trainers import ListTrainer
import collections.abc
collections.Hashable = collections.abc.Hashable

# Load the cleaned dataset
food_data = pd.read_csv('Cleaned_Indian_Food_Dataset.csv')

# Initialize the chatbot
bot = ChatBot('Cooking Assistant')

# Define a function to train the bot
def train_bot():
    # Train using the dataset only
    custom_trainer = ListTrainer(bot)
    for index, row in food_data.iterrows():
        # Use 'TranslatedRecipeName' for dish name and 'TranslatedIngredients' for ingredients
        dish = row['TranslatedRecipeName']
        ingredients = row['TranslatedIngredients']
        instructions = row['TranslatedInstructions']
        
        # Train the bot with the formatted question and answer
        custom_trainer.train([
            f"How do I make {dish}?",
            f"Ingredients: {ingredients}. Instructions: {instructions}"
        ])

# Call the training function
train_bot()

# Define the chatbot interaction function
def chat():
    print("Cooking Assistant Bot is ready to help! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Happy Cooking!")
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")

# Ensure proper execution of the chat function
if __name__ == '__main__':
    chat()

