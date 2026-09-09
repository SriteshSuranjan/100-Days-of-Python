# Secret Code

## Goal

Make a Python program that can encode and decode messages using the given secret-code rules.

## Menu

1. Coding
2. Decoding
0. Quit

The program should keep running until the user enters `0`.

## Coding Rules

For each word:

- If length is 3 or more:
  - Remove the first character and put it at the end.
  - Generate 3 random characters.
  - Add them to the beginning.
  - Generate another 3 random characters.
  - Add them to the end.
- If length is less than 3:
  - Reverse the word.

## Decoding Rules

For each word:

- If length is less than 3:
  - Reverse the word.
- Otherwise:
  - Remove 3 characters from the beginning.
  - Remove 3 characters from the end.
  - Move the last character to the beginning.

## Functions

```python
generate_random_chars()
encrypt_word(word)
decrypt_word(word)
encrypt_message(message)
decrypt_message(message)
main()
````

 ## Variables

 Use clear variable names:

```
message
words
word
encrypted_word
decrypted_word
random_start
random_end
choice
```

 ## Later Ideas

 After the basic program works:

 - Add an encryption/decryption key.
- Allow the user to generate a random key.
- Add more menu options if useful.

 ## Development Order

 1. Generate random characters
2. Encrypt one word
3. Decrypt one word
4. Encrypt a full message
5. Decrypt a full message
6. Add the menu
7. Add a key
8. Improve if needed

## Architecture

```text
Secret Code Program
│
├── main()
│   ├── Display menu
│   ├── Get user choice
│   ├── Get message
│   └── Call required function
│
├── Random Characters
│   └── generate_random_chars()
│
├── Encryption
│   ├── encrypt_word()
│   └── encrypt_message()
│
├── Decryption
│   ├── decrypt_word()
│   └── decrypt_message()
│
└── Future
    └── Key System
```
# Program Flow
```
START
  │
  ▼
main()
  │
  ▼
Display Menu
  │
  ▼
Get Choice
  │
  ├── 1 ──► Encrypt Message
  │           │
  │           ▼
  │       encrypt_message()
  │           │
  │           ▼
  │       encrypt_word()
  │
  ├── 2 ──► Decrypt Message
  │           │
  │           ▼
  │       decrypt_message()
  │           │
  │           ▼
  │       decrypt_word()
  │
  └── 0 ──► Quit
                │
                ▼
               END

After Encrypt/Decrypt
        │
        ▼
    Show Result
        │
        ▼
    Back to Menu
```
