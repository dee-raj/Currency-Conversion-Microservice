# Currency Conversion Microservice

This project implements a simple currency conversion microservice using Flask in Python. The microservice exposes an endpoint that accepts an amount in Indian Rupees and converts it to another currency. Additionally, a Java client is provided to demonstrate how to consume the microservice.

## Project Structure

- **flask_server.py**: Contains the Flask application that serves as the currency conversion microservice.
- **JavaClient.java**: A Java client that sends a POST request with an amount in Indian Rupees to the Flask microservice.

## Dependencies

- Flask
- Java (for running the Java client)

### Currency Conversion Microservice Overview:

1. **Flask Microservice (`flask_server.py`):**
   - The Flask application defines a single endpoint `/convert` that accepts POST requests.
   - It expects a JSON payload with an `amount_in_rs` field representing the amount in Indian Rupees to be converted.
   - The microservice performs a simple conversion (1 INR = 0.014 USD) and returns the result in the response.

2. **Java Client (`JavaClient.java`):**
   - The Java client is a simple console application that sends a POST request to the Flask microservice.
   - It prompts the user to input the amount in Indian Rupees.
   - The input amount is included in a JSON payload, and the POST request is sent to the microservice.
   - The client then prints the response received from the microservice.


## Running the Flask Microservice

1. Install the required dependencies:

   ```bash
   pip install Flask
   ```

2. Run the Flask microservice:

   ```bash
   python flask_server.py
   ```

   The microservice will start running on `http://localhost:5000`.


## Using the Java Client

1. Open the `JavaClient.java` file in a Java development environment.

2. Update the `url` variable with the correct URL of the Flask microservice.

3. Compile and run the Java client.

   ```bash
   javac JavaClient.java
   java JavaClient
   ```

   The Java client will prompt you to enter the amount in Indian Rupees. After entering the amount, it will send a POST request to the Flask microservice and print the response.


### What a New User May Need to Modify:

1. **Flask Microservice (`flask_server.py`):**
   - If you want to change the conversion rate or add support for multiple currencies, modify the conversion logic in the Flask microservice.
   - Customize the Flask microservice to handle additional error cases or enhance functionality as needed.
   - Change the endpoint URL or port in the Flask application if necessary.

2. **Java Client (`JavaClient.java`):**
   - Modify the `url` variable to match the correct URL where the Flask microservice is running.
   - Customize the Java client to handle different user inputs or add error-checking mechanisms.
   - If you make changes to the microservice (e.g., different JSON payload structure), update the Java client accordingly.


### Additional Notes:

- Ensure that the microservice is running before executing the Java client.
- Check network configurations to allow communication between the Java client and Flask microservice.
- Review and customize the license, dependencies, and any other relevant sections in the README file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
