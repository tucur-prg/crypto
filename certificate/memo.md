
https://lapo.it/asn1js/

openssl genrsa 2048 > server.key

openssl req -new -key server.key > server.csr

openssl x509 -req -days 3650 -signkey server.key < server.csr > server.crt
