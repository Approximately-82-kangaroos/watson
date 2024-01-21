import requests
import csv

if __name__ == "__main__":
    username = input("Enter a username: ")
    with open("url.csv", mode = "r") as file:
        urlFile = csv.reader(file)
        for line in urlFile:
            get_req = requests.get(f"{line[1]}{username}")
            if get_req.status_code <= 299 and get_req.status_code >= 200:
                print(f"{line[0]}\tFound ({line[1]}{username})")
            else:
                print(f"{line[0]}\tNot found")