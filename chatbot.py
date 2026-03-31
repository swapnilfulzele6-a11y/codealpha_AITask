import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time

# FAQ Data
faqs = {
    "What are your working hours?": "We are open from 9 AM to 6 PM, Monday to Friday.",
    "When are you open?": "We are open from 9 AM to 6 PM, Monday to Friday.",
    
    "Do you offer refunds?": "Yes, refunds are available within 30 days.",
    "What is your refund policy?": "You can request a refund within 30 days of purchase.",
    
    "How can I contact support?": "You can email us at support@example.com.",
    "How do I contact you?": "You can contact us via email or phone.",
    
    "Where are you located?": "We are located in Pune, India.",
    "What is your location?": "Our office is in Pune, India.",
    
    "What payment methods are accepted?": "We accept UPI, Credit Card, and Debit Card.",
    "How can I pay?": "You can pay using UPI, Credit Card, or Debit Card.",
    
    "Do you deliver products?": "Yes, we offer home delivery services.",
    "How long does delivery take?": "Delivery usually takes 3-5 business days.",
    
    "Do you have discounts?": "Yes, we offer seasonal discounts and offers.",
    "Any offers available?": "Yes, check our website for latest offers.",
    
    "Can I cancel my order?": "Yes, you can cancel your order before it is shipped.",
    "How to cancel order?": "Go to your orders and click cancel option.",
    
    "Do you have customer support?": "Yes, our support team is available 24/7.",
    "Is support available anytime?": "Yes, customer support is available 24/7.",

    "What are your working hours?": "We are open from 9 AM to 6 PM, Monday to Friday.",
    "When are you open?": "We are open from 9 AM to 6 PM, Monday to Friday.",

    "What is the timing?": "We are open from 9 AM to 6 PM, Monday to Friday.",
    "Shop timing?": "We are open from 9 AM to 6 PM, Monday to Friday.",

    "Opening hours?": "We are open from 9 AM to 6 PM, Monday to Friday.",
}

questions = list(faqs.keys())

# NLP Setup
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(questions)

# Chatbot Logic
def get_answer(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hii", "hello", "hey"]:
        return "Hello! How can I help you?"

    # 🔥 keyword fix
    if "time" in user_input or "hour" in user_input or "open" in user_input:
        return "We are open from 9 AM to 6 PM, Monday to Friday."

    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)

    max_score = similarity.max()
    index = similarity.argmax()

    if max_score < 0.3:
        return "Sorry, I didn't understand your question."

    return faqs[questions[index]]

# Typing Effect
def typing_effect(text):
    chat.insert(tk.END, "Bot: ")
    for char in str(text):
        chat.insert(tk.END, char)
        chat.update()
        time.sleep(0.02)
    chat.insert(tk.END, "\n\n")

# Send Function
def send():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat.insert(tk.END, "You: " + user_input + "\n", "user")
    entry.delete(0, tk.END)

    response = get_answer(user_input)
    typing_effect(response)

    chat.see(tk.END)

# GUI Setup
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("500x500")
root.configure(bg="#1e1e1e")

chat = tk.Text(
    root,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 12),
    wrap="word"
)
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#scrollbar
scrollbar = tk.Scrollbar(chat)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=chat.yview)

# colors for messages
chat.tag_config("user", foreground="#00ffcc")
chat.tag_config("bot", foreground="#ffffff")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=8, fill=tk.X, ipady=6)

send_btn = tk.Button(
    root,
    text="Send",
    command=send,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 13, "bold"),  # bigger text
    padx=10,
    pady=5
)
send_btn.pack(pady=8)

root.mainloop()