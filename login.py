from aminofix import Client
import info

def login():
    client = Client()
    client.login(email=info.EMAIL, password=info.PASSWORD)
    return client