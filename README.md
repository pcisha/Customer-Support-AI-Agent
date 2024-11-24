# Customer Support AI Agent
Customer Support AI Agent


## Online Education Support AI Agent
This project implements a simple conversational AI agent to assist users with common questions related to online education platforms. The agent uses predefined, hardcoded responses to answer questions and gracefully handles cases where the input is unclear or unrelated to the predefined dataset. A hints section is included to guide users on the types of questions they can ask.


## Features
- Predefined Responses: The agent answers based on a fixed set of questions and answers about online education topics.
- Hints Section: Provides a list of sample questions to guide users on what they can ask.
- Similarity Matching: Uses a similarity algorithm to find the best matching response for the user's question.
- Fallback Handling: If no question matches, the agent provides a fallback response prompting the user to rephrase.
- Streamlit UI: A user-friendly web-based interface for users to interact with the agent.


## Hints: Questions You Can Ask
Here are some sample questions users can ask the AI agent:

- "How do I sign up for a course?"
- "What payment methods do you accept?"
- "Can I get a refund for a course?"
- "How can I access my certificate?"
- "What are the system requirements?"
- "Can I access courses on mobile?"
- "Do you offer free courses?"
- "How do I delete my account?"
- "What if I forget my password?"

These hints are displayed directly in the application UI to improve user engagement and guide them on how to interact with the agent.


## Predefined Questions and Answers
### Sample Questions
#### Account Management:
- "How do I sign up for a course?"
- "What if I forget my password?"
- "How do I delete my account?"

#### Payment and Refunds:
- "What payment methods do you accept?"
- "Can I get a refund for a course?"

#### Courses:
- "How can I access my certificate?"
- "Can I reset my progress in a course?"

#### Technical Support:
- "What are the system requirements?"
- "Can I access courses on mobile?"

#### General:
- "Do you offer free courses?"
- "How do I contact support?"


### Example Interactions
#### Exact Match:
- User Input: "How do I sign up for a course?"
- Response: "To sign up for a course, log in to your account, browse our catalog, and click 'Enroll' on the course page. You can proceed to payment to confirm your enrollment."

#### Close Match:
- User Input: "Where can I find my certificate?"
- Response: "Once you complete the course and pass all assessments, you can download your certificate from the 'My Courses' section in your account."

#### No Match:
- User Input: "What is your company's mission?"
- Response: "I'm here to help! Can you please rephrase your question or ask something specific?"


## Installation and Setup
### Clone the Repository:
```git clone https://github.com/yourusername/education-support-agent.git ```  
```cd education-support-agent```

### Install Dependencies:
Ensure Python is installed, then install the required package:
```pip install streamlit```

### Run the Application:
Start the Streamlit server:
```streamlit run app.py```

### Access the Application:
Open your browser and navigate to the URL displayed in the terminal: ```http://localhost:8501```


## Tech Stack
- Backend:  
Python: Core programming language used for implementing the logic.  
difflib.SequenceMatcher: Used for similarity matching between user questions and predefined questions.
- Frontend:  
Streamlit: Provides an interactive, web-based UI for user interaction with the agent.
- Infrastructure:  
Local Deployment: Runs on a local development environment using Streamlit’s built-in server.


## Performance
- Time Complexity: O(n * (m+p)), where n is the number of predefined questions; m is the length of the user's question and p is the average length of predefined questions.  
- Space Complexity: O(n * p).


## Future Improvements
- Dynamic Dataset: Load questions and answers from a database or external file for easier updates.
- Semantic Matching: Replace similarity matching with NLP embeddings for better understanding.
- Multi-language Support: Add support for international users by translating predefined responses.
- Interactive Hints: Allow users to click on hints to auto-fill the input box.

##
Author: Prachi Shah (https://www.linkedin.com/in/prachisshah)

P.S. The default copyright laws apply.
