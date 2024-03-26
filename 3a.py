from flask import Flask
app = Flask("My server")
@app.route('/', methods=['GET'])
def welcome():
   return "welcome to pyhton web service"
if __name__ == '__main__':
   app.run(debug=True) 
