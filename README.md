# Virtual Server Management System ( IaaS )

This Flask application simulates a basic Virtual Server Management System, allowing users to create virtual servers, list existing servers, and view storage status.

## Getting Started

### Prerequisites

- Python (3.x recommended)
- Flask

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dee-raj/WS-and-CC.git
   ```

2. Navigate to the project directory:

   ```bash
   cd virtual-server-management
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. The application will be accessible at `http://127.0.0.1:5000/` by default.

## Endpoints

### Create a Server

- **Endpoint:** `/create_server`
- **Method:** `POST`
- **Data Format:**
  ```json
  {
    "server_name": "example_server",
    "cpu": 2,
    "ram": 4
  }
  ```
- Creates a virtual server with the specified name, CPU, and RAM.

### List Servers

- **Endpoint:** `/list_servers`
- **Method:** `GET`
- **Returns:** A JSON object containing a list of virtual servers.

### Get Storage Status

- **Endpoint:** `/get_storage_status`
- **Method:** `GET`
- **Returns:** A JSON object containing storage status (used and total).




# Platform Application Management Service  ( PaaS )

This Flask application provides a simple service for managing platform applications. It exposes two endpoints - one for creating a new application and another for listing all existing applications.

# Follow Steps like above and
   Run the Flask application:
   
   ```bash
   python platform_app.py
   ```
   The application will run on http://127.0.0.1:5000/.

## Endpoints

### 1. Create Application

- **Endpoint:** `/create_application`
- **Method:** `POST`
- **Payload:**
  - `app_name` (string): Name of the application.
  - `app_type` (string): Type or category of the application.
- **Example:**

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"app_name": "Decoding with Dee", "app_type": "Web"}' http://127.0.0.1:5000/create_application
  ```

- **Response:**
  - Success: 200 OK

    ```json
    {
      "message": "Application created successfully",
      "application": {
        "app_name": "Decoding with Dee",
        "app_type": "Web",
        "provider": "Dee-coding"
      }
    }
    ```

  - Failure: 400 Bad Request

    ```json
    {
      "error": "Invalid data. App name and app type are required."
    }
    ```

### 2. List Applications

- **Endpoint:** `/list_applications`
- **Method:** `GET`
- **Example:**

  ```bash
  curl http://127.0.0.1:5000/list_applications
  ```

- **Response:**
  - Success: 200 OK

    ```json
    {
      "applications": [
        {
          "app_name": "Decoding with Dee",
          "app_type": "Web",
          "provider": "Dee-coding"
        },
        ...
      ]
    }
    ```


# Platform Management API

This Flask application serves as an API for managing applications on a platform. It includes functionalities for creating applications, listing applications, and managing SaaS subscriptions.

## Setup
   please Follow the same steps given as before ...


Run the Flask application:

   ```bash
   python SaaS.py
   ```
The application will run on `http://127.0.0.1:5000/`. Use this base URL for making API requests.


## Endpoints

### 1. Create Application

- **Endpoint:** `/create_application`
- **Method:** `POST`
- **Request Payload:**
  ```json
  {
    "app_name": "Sample App",
    "app_type": "Web Application"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Application created successfully",
    "application": {
      "app_name": "Sample App",
      "app_type": "Web Application",
      "provider": "Dee-coding"
    }
  }
  ```

### 2. List Applications

- **Endpoint:** `/list_applications`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "applications": [
      {
        "app_name": "Sample App",
        "app_type": "Web Application",
        "provider": "Dee-coding"
      }
      // ... other applications
    ]
  }
  ```

### 3. Subscribe to SaaS

- **Endpoint:** `/subscribe`
- **Method:** `POST`
- **Request Payload:**
  ```json
  {
   "app_name": "Sample SaaS App"
  }
  ```
- **Response:**
  ```json
  {
   "message": "Subscribed successfully",
   "subscription": {
   "app_name": "Sample SaaS App"
   }
  }
  ```

### 4. Unsubscribe from SaaS

- **Endpoint:** `/unsubscribe`
- **Method:** `POST`
- **Request Payload:**
  ```json
  {
    "app_name": "Sample SaaS App"
  }
  ```
- **Response:**
  ```json
  {
   "message": "Unsubscribed successfully",
   "app_name": "Sample SaaS App"
  }
  ```

### 5. List SaaS Subscriptions

- **Endpoint:** `/list_subscriptions`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "subscriptions": [
      {
        "app_name": "Sample SaaS App"
      }
      // ... other subscriptions
    ]
  }
  ```

## Author

**Dee-coding**

Feel free to explore and extend the functionalities based on your project requirements!


## Contributing

Feel free to contribute to enhance the functionality or fix any issues. Please follow standard practices and guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
