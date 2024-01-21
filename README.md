# Virtual Server Management System

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

## Contributing

Feel free to contribute to enhance the functionality or fix any issues. Please follow standard practices and guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
