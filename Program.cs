// .NET code to call the service

using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program {
    static async Task Main() {
        string url = "http://localhost:5000/convert";
        double amountInRs = 2100;
        string jsonInputString = "{\"amount_in_rs\": "+amountInRs+"}";

        using (HttpClient client = new HttpClient())
        using (HttpResponseMessage response = await client.PostAsync(url, new StringContent(jsonInputString)))
        using (HttpContent content = response.Content) {
            string result = await content.ReadAsStringAsync();
            Console.WriteLine($"Response Code: {response.StatusCode}");
            Console.WriteLine($"Response: {result}");
        }
    }
}
