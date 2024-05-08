import requests
import xml.etree.ElementTree as ET

Url = "https://www.w3schools.com/xml/tempconvert.asmx"

temp=float(input("Enter a F Temp: "))
SOAPEnvelop = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>{temp}</Fahrenheit>
    </FahrenheitToCelsius>
  </soap:Body>
</soap:Envelope>"""

Headers ={
   "Content-type":"text/xml; charset=utf-8",
   "SOAPAction":"https://www.w3schools.com/xml/FahrenheitToCelsius"
}

response = requests.post(url=Url, data=SOAPEnvelop, headers=Headers)
root = ET.fromstring(response.text)
for child in root.iter("{https://www.w3schools.com/xml/}FahrenheitToCelsiusResult"):
   f2c = child.text
   print(f2c)
