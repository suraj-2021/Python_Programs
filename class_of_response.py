import json

class AnonymousSurvey:
    def __init__(self, question, response):
        self.question = question
        self.response = response
        self.file_name = 'survey.json'
        
    def show_question(self):
        print(self.question)
    
    def store_response(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.response, f)
    
    def show_response(self):
        with open(self.file_name, 'r') as f:
            z = json.load(f)
            print(z)
    
    def show_results(self):
        print("Survey results")
        with open(self.file_name, 'r') as f:
            y = json.load(f)
            print(y)

x = AnonymousSurvey("how are you?", "I'm Great")
x.store_response()
x.show_response()
x.show_results()
