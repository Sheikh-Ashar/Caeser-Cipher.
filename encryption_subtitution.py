alfa={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
key_dic={

}
small_alfa='abcdefghijklmnopqrstuvwxyz'

for chr in small_alfa:
    random_elm=alfa.pop()
    key_dic[chr]=random_elm

text=input("Please enter text.: ")
encrypted_text=""
for ch in text:
    if ch in key_dic:
        encrypted_text += key_dic[ch]
    else:
        encrypted_text += ch

print(encrypted_text)

decrypted_text=''
reversed_dic={}
for key , value in key_dic.items():
    reversed_dic[value] = key

for elm in encrypted_text:
    if elm in reversed_dic:
        decrypted_text += reversed_dic[elm]
    else:
        decrypted_text += elm

choice=input("If you want to decrypt the massege enter 'Yes' and 'No for exit.: ")
if choice.lower() == "yes":
    print(decrypted_text)
elif choice.lower() == "no":
    print("Thanks.")
else:
    print("Try again.")