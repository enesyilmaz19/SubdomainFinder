import requests

target_input = "google.com"


def make_requests(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


with open("subdomainlist.txt.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()

        url = "http://" + word + "." + target_input
        response = make_requests(url)
        if response is not None:
            print("Found subdomain:  " + url)
        else:
            print(f"Cannot found subdomain {word}")

