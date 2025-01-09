# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ub_xlAuOy-Pfua_XmUYLA6kvBnCSAeki
"""

!pip install --upgrade torch torchvision torchaudio

from transformers import pipeline
import pandas as pd
import json

# Initialize a list to store tasks
tasks = []

# Function to display all tasks
def display_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        print(f"Task {i+1}:")
        print(f"  Name: {task['name']}")
        print(f"  Description: {task['description']}")
        print(f"  Priority: {task['priority']}")
        print(f"  Deadline: {task['deadline']}")
        print(f"  Category: {task['category']}")
        print("-" * 30)

# Function to add a task
def add_task(name, description, priority, deadline, category):
    task = {
        "name": name,
        "description": description,
        "priority": priority,
        "deadline": deadline,
        "category": category
    }
    tasks.append(task)
    print("Task added successfully!")

# Function to delete a task
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

# Load a zero-shot classification model
classifier = pipeline("zero-shot-classification")

# Function to suggest a category for a task using AI
def suggest_category(description):
    categories = ["Work", "Personal", "Health", "Education", "Other"]
    result = classifier(description, candidate_labels=categories)
    return result["labels"][0]

# Modified function to add a task with AI category suggestion
def add_task_with_ai(name, description, priority, deadline):
    category = suggest_category(description)
    add_task(name, description, priority, deadline, category)

# Main function for task management
def task_manager():
    while True:
        print("\nTask Manager Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (Low, Medium, High): ")
            deadline = input("Enter task deadline: ")
            add_task_with_ai(name, description, priority, deadline)
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            index = int(input("Enter task index to delete: ")) - 1
            delete_task(index)
        elif choice == "4":
            save_tasks()
        elif choice == "5":
            load_tasks()
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to save tasks to a JSON file
def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)
    print("Tasks saved successfully!")

# Function to load tasks from a JSON file
def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        print("Tasks loaded successfully!")
    except FileNotFoundError:
        print("No saved tasks found.")

# Run the task manager
task_manager()