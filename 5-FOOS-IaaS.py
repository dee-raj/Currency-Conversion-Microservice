from flask import Flask, request, jsonify

app=Flask("IaaS")
virtual_servers =[]
storage={
   'Used':0,
   'Total':100
}

@app.route('/create_server', methods=['POST'])
def create_server():
   global storage
   try:
      data = request.get_json()
      name = data.get('server_name')
      cpu = data.get('cpu')
      ram = data.get('ram')
      if not all([name, cpu, ram]):
         raise ValueError("Something is missing...")

      cpu=int(cpu)
      ram=int(ram)

      if cpu<0 and ram<0:
         raise ValueError("Cpu and ram must be a positive number")
      if cpu>10 and ram>1000:
         raise ValueError("Error....overflow")

      VM_server = {
         'Server Name':name,
         'CPU':cpu,
         'Ram':ram
      }
      virtual_servers.append(VM_server)
      storage['Used'] += cpu*ram

      return jsonify({"Msg: ":"new server created successsfully...!", "Server ":VM_server, "Used resources ":storage['Used']})

   except Exception as e:
      return jsonify({"Error... ":str(e)})

@app.route('/status', methods=['GET'])
def storage_status():
   global storage
   return jsonify(storage)

if __name__=="__main__":
   app.run(port=9087, debug=True)