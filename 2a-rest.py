from flask import Flask
app=Flask("A Restful APP")

@app.route('/', methods=['GET'])
def welcome():
   return "Hey there!..."

if __name__=="__main__":
   app.run(debug=True, port=5644)