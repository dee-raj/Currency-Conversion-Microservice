from zeep import Client
client = Client("http://127.0.0.1:7567/?wsdl")
result_add = client.service.add_numbers(21, 32)
result_sub = client.service.sub_numbers(21, 32)
result_mul = client.service.mul_numbers(21, 32)
print(f"Adding number: {result_add}")
print(f"Adding number: {result_sub}")
print(f"Adding number: {result_mul}")
