import requests
from bs4 import BeautifulSoup

# Program runs until this changes to false when the user selects 'N'.
program_to_continue = True

while (program_to_continue):

    print("Enter username to look up: ")
    username = input()

    while (username[0] == "@" or " " in username):

        if (username[0] == "@" and " " in username):
            print("Don't include '@' or any spaces. Try again: ")
            username = input()

        elif (username[0] == "@" and " " not in username):
            print("Don't include '@' symbol. Try again: ")
            username = input()

        elif (username[0] != "@" and " " in username):
            print("Don't include any spaces. Try again: ")
            username = input()

    url_to_search = f'http://www.tinder.com/@{username}'

    response = requests.get(url_to_search)

    soup = BeautifulSoup(response.text, 'html.parser')

    if (soup.title.text[len(soup.title.text) - 6 : len(soup.title.text)] == "Tinder"):

        print(f'User found: {url_to_search}')
        program_to_continue = False

    else:
        
        print(f'The username @{username} does not exist on Tinder.')
        print("Try again? Y/N: ")

        yes_no = input()

        while (yes_no.upper() != "Y" and yes_no.upper() != "N"):
            print("Please enter Y/N: ")
            yes_no = input()

        if (yes_no.upper() == "N"):
            program_to_continue = False
