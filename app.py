import requests
from bs4 import BeautifulSoup

print("Morse Code Encoder")
print("initialising..")

URL = "https://morsecode.scphillips.com/morse2.html"
RESPONSE = requests.get(URL)
SOUP = BeautifulSoup(RESPONSE.text, "html.parser")
TABLES = SOUP.findAll('table')

morse_key = {}
count = 0
for table in TABLES:
    count += 1
    for row in table:
        if count > 5:
            break
        try:
            letter = row.find('td').get_text()
            morse = row.find('td').find_next('td').get_text()
            if len(letter) > 1:
                letter = letter.strip(" ")[0]
            
            morse_key[letter] = morse
        except:
            pass


while True:
    message = input("\nWhat is your message? ")
    encoded = []
    for char in message:
        if char == " ":
            encoded.append("  ")
        else:
            encoded.append(morse_key[char.upper()])
            encoded.append(" ")

    print("".join(encoded))
    
    stop = input("Would you like to encode another message? (y/n): ")

    if stop[0].lower() == "n":
        print("\n**END OF PROGRAM**")
        break