from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

# Define pairs for chatbot
pairs = [
    [r"(hi|hello|hey)", ["Hello! How can I assist you today?", "Hi there! How’s your day going?"]],
    [r"what is your name?", ["I'm your personal assistant, Chatbot!", "You can call me Chatbot. What’s your name?"]],
    [r"my name is (.*)", ["Nice to meet you, %1!", "Hello, %1! How can I help you today?"]],
    [r"how are you?", ["I'm just a program, but I'm here to assist you!", "I'm great, thanks for asking! How about you?"]],
    [r"i am (good|great|fine)", ["That’s wonderful to hear!", "I’m glad you’re doing well."]],
    [r"tell me a joke", [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "Why did the math book look sad? Because it had too many problems!",
        "Why can’t you give Elsa a balloon? Because she’ll let it go!"
    ]],
    [r"tell me an interesting fact", [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes!",
        "Octopuses have three hearts, and two of them stop beating when they swim!"
    ]],
    [r"what is your hobby?", [
        "I enjoy helping people and learning new things from our conversations.",
        "My hobby is making your day better. What about you?"
    ]],
    [r"can you give me some advice?", [
        "Sure! Always strive to learn something new every day. Growth happens outside of your comfort zone.",
        "Of course! Focus on what you can control, and let go of what you can’t."
    ]],
    [r"(.*) python (.*)", [
        "Python is a versatile programming language used for web development, AI, data analysis, and more!",
        "It’s great to see you’re interested in Python! What specifically would you like to learn about?"
    ]],
    [r"what is (ai|artificial intelligence)?", [
        "Artificial Intelligence is the simulation of human intelligence in machines that are programmed to think and learn.",
        "AI enables machines to mimic cognitive functions like learning, problem-solving, and decision-making."
    ]],
    [r"what is the meaning of life?", [
        "42! According to 'The Hitchhiker’s Guide to the Galaxy', at least. What’s your take?",
        "The meaning of life is to give life a meaning. Create your own purpose!"
    ]],
    [r"can you dance?", [
        "I can’t physically dance, but I can help you pick a playlist for a dance party!",
        "Not yet, but imagine me doing the robot dance. :)"
    ]],
    [r"bye", ["Goodbye! It was nice chatting with you!", "Take care! See you next time."]],
    [r"(.*)", [
        "I’m not sure how to respond to that. Could you elaborate?",
        "Interesting! Tell me more.",
        "That’s something I’d love to learn more about. Let’s keep chatting!"
    ]]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Create Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_input = data.get("user_input", "").lower()
    response = chatbot.respond(user_input)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
