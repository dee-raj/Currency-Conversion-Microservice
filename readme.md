To perform the practical of the server-side code using Flask and the client-side code, you can follow these steps:

### Server-Side Code (Flask):

1. **Install Flask:**
   If you haven't installed Flask, you can do so using the following command:
   ```bash
   pip install Flask
   ```

2. **Create the Flask Server Script (`web_server.py`):**
   Copy and paste the provided server-side code into a file, for example, `web_server.py`.

3. **Run the Flask Server:**
   Open a terminal in the directory containing your `web_server.py` script and run the following command:
   ```bash
   python web_server.py
   ```
   This will start the Flask server.

### Client-Side Code:

1. **Install Requests:**
   If you haven't installed the `requests` library, you can do so using the following command:
   ```bash
   pip install requests
   ```

2. **Create the Client Script (`soap_client.py`):**
   Copy and paste the provided client-side code into a file, for example, `soap_client.py`.

3. **Run the Client Script:**
   Open a new terminal in the directory containing your `soap_client.py` script and run the following command:
   ```bash
   python soap_client.py
   ```
   This will execute the client script and attempt to download a file from the Flask server.

### Notes:

- Make sure the Flask server is running before executing the client script.
- The provided client script attempts to download a file named `snake.ico`. Ensure that this file exists in the server's `uploads` folder or adjust the filename accordingly.
- Adjust the paths and filenames in the code as needed based on your project structure.

With these steps, you should be able to run the Flask server and the client script to upload and download files.