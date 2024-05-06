import requests, os

server_url = "http://127.0.0.1:9048/"
def download_file(dir, file):
   down_link = f"{server_url}/download/{file}"
   response = requests.get(down_link)
   if response.status_code == 200:
      file_path = os.path.join(dir,file)
      with open(file_path, 'wb') as f:
         f.write(response.content)
      print(f"File {file_path} downloaded successfully..! in {dir}")
   else:
      print(f"File {file_path} Not Found")

if __name__=="__main__":
   file_name = 'bg.png'
   folder = '.'
   download_file(folder, file_name)
