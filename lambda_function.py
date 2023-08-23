import requests
from bs4 import BeautifulSoup
import boto3

def lambda_handler(event, context):
    client = boto3.client('sns')
    response = requests.get("https://abd.iowa.gov/alcohol/snapshot/lottery")
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.findAll('tbody')
    table_len = len(table)
    local = []
    other= []
    for row in table[table_len-1].find_all('tr'):
        columns = row.find_all('td')
        city = columns[4].get_text().strip()
        store = columns[3].get_text().strip()
        product = columns[1].get_text().strip()
        if city == "Dubuque":
            local.append(f"Product: {product}\nStore: {store}\nCity: {city}\n")
        else:
            other.append(f"Product: {product}\nStore: {store}\nCity: {city}\n")
    local_string = ""
    other_string = ""
    for element in local:
        local_string = local_string + element + "\n"
    for element in other:
        other_string = other_string + element + "\n"
    result = f"Stores and Products allocated in Dubuque:\n{local_string} \n\n\nAll other locations in Iowa:\n{other_string}"
    print(result)
    client_response = client.publish(TopicArn='arn:aws:sns:us-east-1:181153589401:Lottery', Message=result)
    print(client_response)
    return result
    
