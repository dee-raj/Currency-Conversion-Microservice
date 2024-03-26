from zeep import Client
# Create a Zeep client pointing to the SOAP service WSDL
client = Client('http://127.0.0.1:8979/?wsdl')

# Call the add_numbers method of the CalculatorService
result = client.service.add_numbers(5, 10)
print(f"Result from the SOAP service: {result}")  # Corrected the formatting for displaying the result