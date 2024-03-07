# crypto


## OpenSSL

### RSA

```
# 秘密鍵
openssl genrsa 2048 > RS256_private.pem
openssl rsa -text < RS256_private.pem

# 公開鍵
openssl rsa -in RS256_private.pem -pubout > RS256_public.pem
openssl rsa -pubin -text < RS256_public.pem
```

### EC

```
# 秘密鍵
openssl ecparam -name prime256v1 -genkey -noout > ES256_private.pem
openssl ec -text < ES256_private.pem

# 公開鍵
openssl ec -in ES256_private.pem -pubout > ES256_public.pem
openssl ec -pubin -text < ES256_public.pem
```

### HMAC

```
# 鍵
openssl rand -hex 32

# 署名
echo -n "hello world" | openssl dgst -sha256 -mac hmac -macopt hexkey:ad4c96714d2a6289ed1731742ecfb1959430469ab30d7b2c4c212124153c23bf
```
