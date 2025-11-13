
# MidTerm – Cryptography Lab

1) AES Encryption/Decryption

openssl enc -aes-128-cbc -salt -in secret.txt -out secret.enc -pass pass:MyStrongPass1
openssl enc -aes-128-cbc -d -in secret.enc -out decrypted.txt -pass pass:MyStrongPass1

ფაილი გაიშიფრა და `diff` არ აჩვენებს განსხვავებას.

2) ECC Key Pair + Signature

openssl ecparam -name prime256v1 -genkey -noout -out ecc_private.pem
openssl ec -in ecc_private.pem -pubout -out ecc_public.pem
openssl dgst -sha256 -sign ecc_private.pem -out ecc.sig ecc.txt
openssl dgst -sha256 -verify ecc_public.pem -signature ecc.sig ecc.txt

შედეგი: **Verified OK**

 3) Hashing & HMAC
ტექსტის შეცვლისას HMAC იცვლება → აჩვენებს დაცვას.

 4) Diffie–Hellman (Python)
```python
p=23; g=5
a=6; b=15
A = pow(g,a,p); B = pow(g,b,p)
shared1 = pow(B,a,p); shared2 = pow(A,b,p)
print(shared1, shared2, shared1==shared2)
