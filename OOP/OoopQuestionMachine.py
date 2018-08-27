user_details = dict()
user_posts = dict()
user_answers = dict()
user_questions = {
    1: {'silas': 'what does YOYO mean?'},
    2: {'paul': 'How is KISS DRY concept implemented ?'},
    3: {'joshua': 'Why do you love coding?'},
    }
user_answers = {
    1: {'paul': 'you own your own'},
    2: {'joshua': 'keep it simple and stupid,dont repeat yourself'},
    3: {'silas': 'its my passion, awesome'},
}

class QuestionMachine():

   def __init__(self, fname, lname, username, email, password):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

   def signup(self):
        self.username = input("Enter your username: ")
        self.fname = input("Enter your firstname: ")
        self.lname = input("Enter your lastname: ")
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")
        user_details.update({"self.username":self.username,"self.fname":self.fname,"self.lname":self.lname,"self.email":self.email,"self.password":self.password})
        print(user_details)
        return(user_details)
        self.confirmation()

   def forget_password_or_username(self):
       del user_details["self.username"]
       del user_details["self.password"]
       self.username = input("Enter your new username:  ")
       self.password = input("Enter your new password:  ")
       user_details.update({"self.username":self.username,"self.password":self.password})
       self.confirmation()

   def confirmation(self):
        self.username = input("Confirm your username: ")
        self.email = input("Confirm your email: ")
        self.password = input("Confirm your password: ")
        if user_details["self.username"] == self.username:
            if user_details["self.email"] == self.email:
                if user_details["self.password"] == self.password:
                    print("You acount has been activated")
                    self.login()
                else:
                  print("wrong password entered")
                  self.signup()
            else:
              print("wrong email entered")
              self.signup()

        else:
         print("wrong username entered")
         self.signup()

   def login(self):
        self.username = input("Enter your username to login:  ")
        self.email = input("Enter your email to login:   ")
        self.password = input("Enter your password to login:   ")
        if user_details["self.username"] == self.username:
            if user_details["self.email"] == self.email:
                if user_details["self.password"] == self.password:
                    print("Logged in successful")
                    self.question()
                else:
                  print("wrong password")
                  self.forget_password_or_username()
            else:
              print("wrong email entered")
              self.forget_password_or_username()
        else:
          print("wrong username entered")
          self.forget_password_or_username()

   def question(self,*args):
     self.question = input("Type your question here: ")
     self.username = input("Enter your username here: ")
     if self.username in user_details["self.username"]:
      user_posts.update({"self.username":self.username, "self.question":self.question})
      self.question_view()
     else:
        print("you need to log in first to post a question")
        self.login()

   def question_view(self,*args):
        print(user_posts)
        self.answer()

   def answer(self,*args):
     self.answers = input("Type your answer here: ")
     self.username = input("Enter your username here: ")
     if self.username in user_details["self.username"]:
      user_answers.update({"self.username":self.username,"self.answers":self.answers})
      self.answer_view()
     else:
        print("you need to login in first")
        self.login()

   def answer_view(self,*args):
        print(user_answers)
        self.blog()

   def blog(self):
    self.postquestion = input("Do you want to post a question (y/n) ?: ")
    if self.postquestion == "y":
        print("Here is the previous  question: {}...{}...".format(user_posts["self.question"], user_answers["self.answers"]))
    else:
        self.delete_question_answer()

    def delete_question_answer(self):
       del user_post["self.question"]
       del user_answers["self.answers"]
       self.question= input("Enter your new username:  ")
       self.answer = input("Enter your new password:  ")
       self.username = input("Enter your username:  ")
       user_post.update({"self.username":self.username,"self.question":self.question})
       user_answers.updaate({"self.username":self.username, "self.answer":self.answer})
       self.specific_question()

    def specific_question(self,*args):
        self.questionid = int(input("Choose a question number[0-9]:  "))
        self.questionid = user_questions[self.questionid]
        print(self.questionid)
        self.specific_answer()

    def specific_answer(self,*args):
        self.answerid = int(input("Choose a question number[0-9]:  "))
        self.answersid = user_answers[self.answerid]
        print(self.answerid)
        self.logout()

   def logout(self):
       self.exitme = input("Are you sure you want to log out(y/n): ")
       if self.exitme == "y":
        print("you are successful log out")
        self.login()
       else:
        self.blog()

