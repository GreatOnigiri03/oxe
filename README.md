# oxe
oxe is a simple, yet secure xor cipher method.

Here is some example:
```
import oxe

# You can generate a random key, and set a custom length.
key = oxe.generate(256)
# 256 is a good choice.
# It will be hard enough for hackers to get the key.

message = oxe.encrypt('Hello, World!', key)
oxe.decrypt(message, key)
# The output will be "Hello, World!".
```
