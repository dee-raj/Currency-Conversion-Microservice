import requests
import xml.etree.ElementTree as ET
temp = float(input("Enter a Celsius value To convert in Fahrenheit: "))

url = "https://www.w3schools.com/xml/tempconvert.asmx"
SOAPEnvelope = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
      <Celsius>{temp}</Celsius>
    </CelsiusToFahrenheit>
  </soap:Body>
</soap:Envelope>"""

headers = {
  "Content-Type": "text/xml; charset=utf-8",
  "SOAPAction": "https://www.w3schools.com/xml/CelsiusToFahrenheit"  # Adding SOAPAction header
}
response = requests.post(url, data=SOAPEnvelope, headers=headers)
root =ET.fromstring(response.text)

for child in root.iter("{https://www.w3schools.com/xml/}CelsiusToFahrenheitResult"):
  C2F=child.text
  print(C2F)
