# @author prachi.shah

import streamlit as st
from difflib import SequenceMatcher

# Predefined dataset of questions and answers
PREDEFINED_RESPONSES = {
    "How do I sign up for a course?":
        "To sign up for a course, log in to your account, browse our catalog, and click 'Enroll' on the course page. You can proceed to payment to confirm your enrollment.",
    "What if I forget my password?":
        "If you forget your password, click 'Forgot Password' on the login page. Follow the instructions sent to your registered email to reset your password.",
    "How do I delete my account?":
        "To delete your account, go to the 'Account Settings' page and select 'Delete Account.' Please note this action is irreversible.",
    "How do I update my email address?":
        "You can update your email address in the 'Account Settings' section. Make sure to verify your new email after updating.",
    "What payment methods do you accept?":
        "We accept Visa, MasterCard, American Express, PayPal, and various digital wallets like Apple Pay and Google Pay.",
    "Can I get a refund for a course?":
        "Refunds are available within 7 days of purchase for most courses, provided less than 20% of the content has been accessed. Check our refund policy for more details.",
    "How can I access my certificate?":
        "Once you complete the course and pass all assessments, you can download your certificate from the 'My Courses' section in your account.",
    "Can I access courses on mobile?":
        "Yes, our platform is mobile-friendly, and we also have an app available for iOS and Android. Download it from the App Store or Google Play.",
    "What are the system requirements?":
        "Our platform works on most modern browsers and devices. For the best experience, use the latest versions of Chrome, Firefox, or Safari. A stable internet connection is recommended.",
    "Do you offer free courses?":
        "Yes, we offer a selection of free courses in various subjects. Browse the 'Free Courses' section in our catalog to see what's available."
}

# Preprocess the questions once to optimize repeated searches
PREPROCESSED_QUESTIONS = {q.lower().strip(): q for q in PREDEFINED_RESPONSES.keys()}


# Function to find the best matching response
def get_best_response(user_question):
    """
    Retrieve the most relevant response for a user's question
    based on predefined responses using similarity matching.
    """
    # Preprocess user input (lowercase and strip)
    user_question = user_question.lower().strip()

    # Set up for similarity matching
    best_match = None
    highest_similarity = 0.7  # Minimum threshold for a valid response

    # Iterate through predefined questions and compute similarity
    for processed_question, original_question in PREPROCESSED_QUESTIONS.items():
        # Early skip for low-similarity questions
        similarity = SequenceMatcher(None, user_question, processed_question).ratio()
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = PREDEFINED_RESPONSES[original_question]

    # Return the best match or a fallback response
    if best_match:
        return best_match
    else:
        return "I'm here to help! Can you please rephrase your question or ask something specific?"


# Streamlit UI
st.title("Online Education Support AI Agent")

st.write("Hello! I'm here to assist you with your online education platform-related questions. Ask me anything!")

# Display a list of sample questions
st.write("### Hints: Questions You Can Ask")
hints = [
    "How do I sign up for a course?",
    "What payment methods do you accept?",
    "Can I get a refund for a course?",
    "How can I access my certificate?",
    "What are the system requirements?",
    "Can I access courses on mobile?",
    "Do you offer free courses?",
    "How do I delete my account?",
    "What if I forget my password?"
]
for hint in hints:
    st.write(f"- {hint}")

# Input box for user to type their question
user_question = st.text_input("Your question:")

# Check user input and generate a response
if user_question:
    response = get_best_response(user_question)
    st.write("### Answer:")
    st.write(response)
