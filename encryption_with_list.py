import random

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ']
alfa_key=[]
while len(alfa_key) < len(alphabets):
    random_value = random.choice(alphabets)
    
    # alfabets.remove(random_value)
    if random_value in alfa_key:
        continue
    else:
        alfa_key.append(random_value)

text=input("Enter text: ").lower()
encrypted_text=""
for elm in text:
    if elm in alphabets:
        ind=alphabets.index(elm)
        if elm in alfa_key:
            ind_key=alfa_key[ind]
            encrypted_text += ind_key
        else:
            encrypted_text += elm
    else:
        encrypted_text += elm

print(encrypted_text)

decrypted_text=""
for elm in encrypted_text:
    if elm in alfa_key:
        ind=alfa_key.index(elm)
        if elm in alphabets:
            rev_key=alphabets[ind]
            decrypted_text += rev_key
        else:
            decrypted_text += elm
    else:
        decrypted_text += elm

choice=input("If you want to decrypt the massege enter 'Yes' and 'No for exit.: ")
if choice.lower() == "yes":
    print(decrypted_text)
elif choice.lower() == "no":
    print("Thanks.")
else:
    print("Try again.")

print('Thanks.')

# print(decrypted_text)

# print(alfa_key)
# print(alfabets)