# -*- coding: utf-8 -*-
"""Langchain.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ayPlSZwXudOSDGTG4lBC-3R4_LjS9ZAp
"""

!pip install pandas transformers langchain

!pip install transformers torch

import warnings

# Suppress the specific future warning
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers.tokenization_utils_base")

# Your existing code follows...
import pandas as pd
from transformers import pipeline
import torch

# Check if GPU is available
device = 0 if torch.cuda.is_available() else -1

# Step 3: Load your data
input_file_path = "/content/Flipkart_Products_reviews_with_sentiment.csv"
data = pd.read_csv(input_file_path)
# Display the first few rows of the dataset
print(data.head())

# Step 4: Set up the Hugging Face QA pipeline with a more advanced model
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", device=device)

# Step 5: Define the Question-Answering function
class FlipkartQA:
    def __init__(self, data, qa_pipeline):
        self.data = data
        self.qa_pipeline = qa_pipeline

    def format_context(self, relevant_columns):
        # Format the context with only relevant columns
        context = ""
        for index, row in self.data.iterrows():
            context += ", ".join([f"{col}: {row[col]}" for col in relevant_columns]) + "\n"
        return context

    def ask_question(self, question):
        # Determine relevant columns based on the question
        if "reviews" in question.lower():
            relevant_columns = ['Product_Name', 'Reviews']
        elif "rating" in question.lower():
            relevant_columns = ['Product_Name', 'Ratings']
        else:
            relevant_columns = self.data.columns.tolist()

        context = self.format_context(relevant_columns)
        answer = self.qa_pipeline(question=question, context=context)
        return answer['answer']

# Step 6: Initialize the FlipkartQA
flipkart_qa = FlipkartQA(data, qa_pipeline)

# Step 7: Enter your question
question = input("Enter your question: ")

# Step 8: Ask the question and get the answer
answer = flipkart_qa.ask_question(question)

# Print the answer
print("Question:", question)
print("Answer:", answer)