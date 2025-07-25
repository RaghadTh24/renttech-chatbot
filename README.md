# RentTech Chatbot

This is a chatbot application built with Django for the RentTech electronic device rental platform.  
The chatbot helps users with rental processes, payment guidance, and general inquiries in Arabic and English.

![Chatbot Screenshot](images/Chatbot%20Renttech.png)

## Features
- Supports Arabic and English languages
- Guides users through device rental and payment
- Handles conversation context with unique conversation IDs
- Simple and clean web interface for chatting

## How to Run

1. Clone this repository  
2. Create a virtual environment and activate it  
3. Install dependencies with:  
   pip install -r requirements.txt
4. Apply migrations:
   python manage.py migrate
5. Run the development server:
   python manage.py runserver
6. Open your browser and visit:
http://127.0.0.1:8000/chatbot/
