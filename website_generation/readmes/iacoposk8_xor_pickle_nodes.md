# 🔐 ComfyUI XOR Text & Pickle Nodes

Three custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allow you to **encrypt and decrypt Python objects or text** using simple XOR encryption.

## Features

* Encrypt any Python object (`ANY`) or text (`STRING`) using a password.
* Decrypt encrypted hexadecimal text (from a web interface) or load encrypted objects from `.pkl` files.
* Save to or load from `.pkl` files using a file path (`STRING`).
* Pure Python — no external dependencies beyond standard libraries.

---

## Included Nodes

### `Decrypt XOR Text`
This node decrypts a hexadecimal text string produced by your JavaScript script, converting it back into a Python object.
* **Inputs:**
    * `encrypted_text` *(STRING)* – The hexadecimal string to decrypt.
    * `password` *(STRING)* – The password for decryption.
* **Output:**
    * `decrypted_object` *(ANY)* – The decrypted Python object.

---

### `Load XOR Pickle From File`
Decrypts and loads an encrypted object from a file.
* **Inputs:**
    * `filename` *(STRING)* – The path to the encrypted `.pkl` file.
    * `password` *(STRING)* – The password for decryption.
* **Output:**
    * `object` *(ANY)* – The decrypted Python object.

---

### `Save XOR Pickle To File`
Encrypts and saves a Python object to a file.
* **Inputs:**
    * `obj` *(ANY)* – The object to encrypt and save.
    * `filename` *(STRING)* – The output file path.
    * `password` *(STRING)* – The password for encryption.
* **Output:**
    * *(none – saves to disk)*

---

## Installation

To install the custom nodes, follow these steps:

1.  Go to the custom_nodes folder
2.  Launch: `git clone https://github.com/iacoposk8/xor_pickle_nodes`
