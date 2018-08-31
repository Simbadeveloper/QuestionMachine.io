""""my project"""
from flask import jsonify, Flask, request, redirect, url_for
from flask_restful import reqparse
app = Flask(__name__)
app.config["SECRET_KEY"] = 'silasomurunga'

user_details = dict()
user_questions = {
    'question1': {'silas': 'what does YOYO mean?'},
    'question2': {'paul': 'How is KISS DRY concept implemented ?'},
    'question3': {'joshua': 'Why do you love coding?'},
    }
user_answers = {
    'answer1': {'paul': 'you own your own'},
    'answer2': {'joshua': 'keep it simple and stupid,dont repeat yourself'},
    'answer3': {'silas': 'its my passion, awesome'},
}

@app.route("/api/v1/", methods=['GET']) #index endpoint
def home():
    """ route for the index page"""
    return jsonify({"message" : "welcome to question and answering machine"})

@app.route("/api/v1/auth/signup", methods=['POST'])#signup endpoint
def signup():
    """route for singup for user"""
    data = request.get_json()
    username = data["username"]
    if username in user_details:
        return jsonify({"message":"username already taken choosen another username"})
    fname = data["fname"]
    lname = data["lname"]
    email = data["email"]
    password = data["password"]
    cpassword = data["cpassword"]
    user_details.update({"username":username, "fname":fname, "lname":lname,\
                          "email" :email, "password":password, "cpassword":cpassword})
    return jsonify({"message" : "successful signup"})

@app.route("/api/v1/auth/confirmation", methods=['POST']) #confirmation endpoint
def confirmation():
    """route for confirming a user"""
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]
    if user_details["username"] == username:
        if user_details["email"] == email:
            if user_details["password"] == password:
                return jsonify({"message" : "You acount has been activated"})
                return redirect(url_for('login'))
        return redirect(url_for('signup'))
    return redirect(url_for('signup'))

@app.route("/api/v1/auth/login", methods=['POST'])#login endpoint
def login():
    """route for login for activate account"""
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]
    return jsonify({"message":"logged in successful"})

@app.route('/api/v1/auth/admin', methods=['GET'])
def hello_admin():
    """route for admin priviledge only"""
    return jsonify({"message":"Hello Admin"})

@app.route('/api/v1/auth/user/<name>', methods=['GET'])#guest/admin endpoint
def hello_user(name):
    """route to detremine whether you are admin or guest user """
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

@app.route('/api/v1/auth/guest/<guest>', methods=['GET'])#guest endpoint
def hello_guest(guest):
    """route for user priveldge only"""
    return 'Hello %s as Guest' % guest

@app.route("/api/v1/auth/forgetpassword", methods=['POST', 'DELETE'])
 #resetpassword/username endpoint
def forget_password_or_username():
    """route to reset your password and username"""
    data = request.get_json()
    del user_details["username"]
    del user_details["password"]
    username = data["username"]
    password = data["password"]
    details.update({"username" : username, "password" : password})
    return redirect(url_for('confirmation'))

@app.route("/api/v1/questions", methods=['POST']) #post a question endpoint
def questions():
    """route to post your questions"""
    data = request.get_json()
    args = parser.parse_args()
    questionid =(int(max(user_questions.keys()).lstrip("question")) + 1)
    questionid = 'question%i' % questionid
    question = data["question"]
    username = data["username"]
    user_questions.update({questionid:{"username":username, "question":question}})
    return redirect(url_for('all_questions'))

@app.route("/api/v1/question/<string:questionid>", methods=['DELETE']) #delete a question endpoint
def delete_question():
    """route to delete your questions"""
    del user_questions[questionid]
    return jsonify({"message" : "Question no {} has been deleted".\
                    format(user_answers[questionid])})

@app.route("/api/v1/questions", methods=["GET"]) #all question endpoint
def all_questions():
    """route to view all question posted"""
    return jsonify(user_questions)

@app.route("/api/v1/question/<string:questionid>", methods=['GET'])
#specific question endpoint
def question_view(questionid):
    """route to view specific questions as per they id"""
    return jsonify({"answer":"Your updated question: {} ".format(user_questions[questionid])})


@app.route("/api/v1/answer", methods=['POST']) #answer post endpoint
def answer():
    """route to post an answer"""
    data = request.get_json()
    if user_details["username"] == username:
        answer = data["answer"]
        username = data["username"]
    user_answers.update({"username" : username, "answer" : answer})
    return redirect(url_for('all_answers'))

@app.route("/api/v1/answer/<string:answerid>", methods=['DELETE'])
#delete answer endpoint
def delete_answer():
    """route to delete an answer"""
    del user_answers[answerid]
    return redirect(url_for(update_or_updated))

@app.route("/api/v1/answer", methods=["GET"])#all answer endpoint
def all_answers():
    """route to view all answers made"""
    return jsonify(user_answers)

@app.route("/api/v1/answer/<string:answerid>", methods=['GET'])
#specific answer endpoint
def answer_view(answerid):
    """route to view a specific answer"""
    return jsonify({"answer":"Your updated answer: {} ".format(user_answers[answerid])})

@app.route("/api/v1/question/<string:questionid>/answer/<string:answerid>", methods=['PUT'])
#update endpoint
def update_or_updated(questionid, answerid):
    """route to update questions and answer posted"""
    data = request.get_json()
    if user_details["username"] == username:
        question = data["question"]
        answer = data["answer"]
        username = data["username"]
        user_answers.update({"username":username, "answer":answer})
        user_questions.update({"username":username, "question":question})
        return jsonify({"updated question":"your question {} and answer {} "\
        .format(user_questions[questionid], user_answers[answerid])})

@app.route("/api/v1/logout", methods=['GET']) #logout endpoint
def logout():
    """route for logging out"""
    return jsonify({"message":"successful logout"})

if __name__ == '__main__':
    app.run(debug=True)
