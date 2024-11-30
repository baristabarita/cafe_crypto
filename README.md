# Cafe Crypto 🔐☕

A cryptographic project for IT3104N: Information Assurance and Security course that implements multiple layers of encryption algorithms to secure files.

## Project Structure

```
cafe-crypto/
├── client/ # Vue.js frontend
│ ├── public/ # Static assets
│ ├── src/
│ │ ├── components/ # Vue components
│ │ ├── layouts/ # Page layouts
│ │ ├── pages/ # Vue pages/routes
│ │ ├── services/ # API services
│ │ └── utils/ # Helper functions
│ └── package.json
│
└── server/ # Flask backend
├── src/
│ ├── crypto/ # Encryption algorithms
│ ├── routes/ # API endpoints
│ ├── utils/ # Utility functions
│ └── pipeline.py # Encryption pipeline
├── app.py # Flask application
└── requirements.txt
```


## Features

- File encryption and decryption
- Multiple encryption layers:
  1. Caesar Cipher
  2. Transposition Cipher
  3. Vigenère Cipher
  4. Vernam Cipher (One-Time Pad)
  5. RSA Encryption

## Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

## Installation

### Backend Setup

1. Navigate to server directory

```
cd server
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the server

```
python app.py
```

### Frontend Setup

1. Navigate to client directory

```
cd client
```

2. Install dependencies

```
npm install
```

3. Run the frontend

```
npm run dev
``` 


## Usage

1. Access the application at `http://localhost:5173`
2. Choose between encryption or decryption mode
3. For encryption:
   - Upload a file to encrypt
   - Download both the encrypted file and key file
4. For decryption:
   - Upload the encrypted file and its corresponding key file
   - Download the decrypted file

## Security Features

### Encryption Pipeline

The application implements a multi-layered encryption approach:

1. **Caesar Cipher**: Simple substitution cipher with a fixed shift
2. **Transposition Cipher**: Rearranges data using matrix transposition
3. **Vigenère Cipher**: Polyalphabetic substitution with a keyword
4. **Vernam Cipher**: One-time pad implementation for perfect secrecy
5. **RSA**: Public-key cryptography for the final encryption layer

### File Handling

- Secure file naming using `secure_filename`
- Automatic cleanup of temporary files
- Base64 encoding for key storage
- Unique file identifiers for each operation


## Acknowledgments

- Built with Vue.js and Flask
- Styled with Tailwind CSS
- Icons from PrimeIcons
