Indian Food Recipe Chatbot

This repository contains the implementation of a chatbot designed to assist users with Indian food recipes.
The chatbot, named "Cooking Assistant," uses the ChatterBot library to provide recipe ingredients and instructions based on user queries.
Below, you'll find details about the project, installation instructions, and how to use the chatbot.

Features

Provides recipes and cooking instructions for various Indian dishes.

Uses a cleaned dataset of Indian food recipes.

Interactive chatbot interface for users.

Easy-to-train functionality using custom datasets.

Prerequisites

Python 3.7 or later

Libraries: chatterbot, pandas

Installation

Install the required libraries:

pip install chatterbot pandas

Add the dataset:

Place the cleaned dataset file named Cleaned_Indian_Food_Dataset.csv in the project directory.

Dataset Format

The dataset should include the following columns:

TranslatedRecipeName: Name of the dish.

TranslatedIngredients: Ingredients required for the dish.

TranslatedInstructions: Cooking instructions for the dish.

Ensure that the dataset is cleaned and formatted correctly before running the chatbot.

How to Run

Train the chatbot:
The training is automated within the script and uses the dataset provided.

Start the chatbot interaction:

python chatbot.py

Interact with the bot:

Ask the bot about a specific recipe by typing:

How do I make [dish name]?

Type exit to quit the chatbot.


Contributing

If you'd like to contribute to the project, please fork the repository and submit a pull request. Ensure any changes are well-documented and tested.



Acknowledgments

ChatterBot: A Python library for building chatbots.

Dataset sourced and cleaned for Indian recipes.

Happy Cooking!
