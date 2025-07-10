faqs = {
    "What is your return policy?": "You can return any product within 30 days for a full refund.",
    "How can I track my order?": "You can track your order using the tracking link sent to your email.",
    "Do you offer international shipping?": "Yes, we ship to over 50 countries worldwide.",
    "How do I contact customer support?": "You can contact us via email at support@example.com or call us at 123-456-7890.",
    "What payment methods do you accept?": "We accept credit cards, debit cards, PayPal, and Apple Pay."
}
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

from nltk.corpus import stopwords

def preprocess(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    tokens = nltk.word_tokenize(text)
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)
faq_questions = list(faqs.keys())
preprocessed_questions = [preprocess(q) for q in faq_questions]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(preprocessed_questions)


def get_best_answer(user_question):
    user_question_prep = preprocess(user_question)
    user_vector = vectorizer.transform([user_question_prep])
    similarity_scores = cosine_similarity(user_vector, faq_vectors)
    best_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_index]

    if best_score < 0.3:
        return "Sorry, I couldn't find an answer to your question. Please contact support."
    else:
        return faqs[faq_questions[best_index]]
def chatbot():
    print("🤖 Hi! I'm your FAQ bot. Type 'exit' to leave.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break
        response = get_best_answer(user_input)
        print(f"Bot: {response}")

# Run it
chatbot()