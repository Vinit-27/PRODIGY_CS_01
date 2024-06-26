import streamlit as st

def Caesar_encrypt(data,key):
    cipher = ''
    flag = 1
    for i in data:
        if i >= 'A' and i <= 'Z':
            cipher += chr((ord(i)-ord('A')+key)%26 + ord('A'))
        elif i >= 'a' and i <= 'z':
            cipher += chr((ord(i)-ord('a')+key)%26 + ord('a'))
        else:
            cipher += i
    return cipher,flag

def Caesar_decrypt(cipher,key):
    Decipher = ''
    flag = 1
    for i in cipher:
        if i >= 'A' and i <= 'Z':
            Decipher += chr((ord(i)-ord('A')-key)%26 + ord('A'))
        elif i >= 'a' and i <= 'z':
            Decipher += chr((ord(i)-ord('a')-key)%26 + ord('a'))
        else:
            Decipher += i
    return Decipher,flag

st.title('Caesar Cipher')
plaintext = st.text_area('Plain text')
key = st.number_input('key',min_value=1,max_value=25,step=1)

flag = 0
cipher=''
if len(plaintext)!=0:
    cipher,flag = Caesar_encrypt(plaintext,int(key))
    if flag == 1:
        st.write("Woohoo!! Encryption Done!")
        st.text_area('Cipher text',value=cipher)

if len(cipher)!=0:
    decipher,flag = Caesar_decrypt(cipher,int(key))
    if flag == 1:
        st.write("Woohoo!! Decryption Done!")
        st.text_area('decipher text',value=decipher)
