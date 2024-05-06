from flask import Flask, Response, send_file, request, jsonify
import os

app = Flask("UPLOADING & DOWNLOADING")
Up_Dir = 'uploads'
app.config['up'] = Up_Dir
os.makedirs(Up_Dir, exist_ok=True)

@app.route('/upload', methods=['POST', 'PUT'])
def uploading_Files():
   try:
      file = request.files['file']
      file_path = os.path.join(app.config['up'],file.filename)
      file.save(file_path)
      return jsonify({"Msg ": f"Files uploaded {file} successfully...!"})
   except Exception as e:
      return jsonify({"up Error ":str(e)}), 500

@app.route('/download/<file_name>', methods=['GET'])
def downloading_files(file_name):
   try:
      file_path = os.path.join(app.config['up'], file_name)
      if os.path.exists(file_path):
         return send_file(file_path, as_attachment=True)
      else:
         return jsonify({"Error ": "File not found"}), 404
   except Exception as e:
      return jsonify({"Down Error... ": str(e)}), 400

if __name__=="__main__":
   app.run(debug=True, port=9048)
