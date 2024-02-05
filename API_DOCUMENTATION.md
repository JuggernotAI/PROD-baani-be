# API Documentation for Baani

## Introduction

This document outlines the API endpoints available in Baani, a social media automation agent. These endpoints allow users to interact with the system for content creation, image generation, and social media posting.

## Base URL

For local development (LOCAL ENV): `http://127.0.0.1:5000`  
For production (PROD): `https://baani-backend.onrender.com`

## Endpoints

### 1. Home

- **Endpoint (LOCAL ENV)**: `http://127.0.0.1:5000/`
- **Endpoint (PROD)**: `https://baani-backend.onrender.com/`
- **Method**: `GET`
- **Description**: Basic endpoint to check the API status.
- **Response**:
  - `200 OK`: Returns a welcome message.

### 2. Initialize Chat

- **Endpoint (LOCAL ENV)**: `http://127.0.0.1:5000/chat/init`
- **Endpoint (PROD)**: `https://baani-backend.onrender.com/chat/init`
- **Method**: `GET`
- **Description**: Initializes a chat session and returns initial messages.
- **Response**:
  - `200 OK`: Returns initial chat messages.

### 3. Generate Chat Response

- **Endpoint (LOCAL ENV)**: `http://127.0.0.1:5000/chat/generate`
- **Endpoint (PROD)**: `https://baani-backend.onrender.com/chat/generate`
- **Method**: `POST`
- **Description**: Generates a response based on user input.
- **Request Body**: JSON containing `messages`.
- **Response**:
  - `200 OK`: Returns generated response.
  - `400 Bad Request`: Missing or invalid parameters.

### 4. Upload Image

- **Endpoint (LOCAL ENV)**: `http://127.0.0.1:5000/upload/image`
- **Endpoint (PROD)**: `https://baani-backend.onrender.com/upload/image`
- **Method**: `POST`
- **Description**: Uploads an image to the server.
- **Request Body**: Form-data with key `image`.
- **Response**:
  - `200 OK`: Returns the path of the uploaded image.
  - `400 Bad Request`: Image is required.

### 5. Post to LinkedIn

- **Endpoint (LOCAL ENV)**: `http://127.0.0.1:5000/post_linkedin`
- **Endpoint (PROD)**: `https://baani-backend.onrender.com/post_linkedin`
- **Method**: `POST`
- **Description**: Posts content to LinkedIn.
- **Request Body**: JSON containing `content` and optional `image`.
- **Response**:
  - `200 OK`: Successful post message.
  - `400 Bad Request`: Missing content.
  - `500 Internal Server Error`: Server or internal error.

### 6. Twitter OAuth Initialization

- **Endpoint (LOCAL ENV)**: `http://127.0.0.1:5000/twitter/auth/init`
- **Endpoint (PROD)**: `https://baani-backend.onrender.com/twitter/auth/init`
- **Method**: `GET`
- **Description**: Initiates Twitter OAuth authentication.
- **Response**:
  - `200 OK`: Returns authorization URL.

### 7. Complete Twitter OAuth

- **Endpoint (LOCAL ENV)**: `http://127.0.0.1:5000/twitter/auth/verify`
- **Endpoint (PROD)**: `https://baani-backend.onrender.com/twitter/auth/verify`
- **Method**: `POST`
- **Description**: Completes Twitter OAuth authentication.
- **Request Body**: JSON containing `verifier`.
- **Response**:
  - `200 OK`: Authentication successful message.
  - `500 Internal Server Error`: Server or internal error.

### 8. Post to Twitter

- **Endpoint (LOCAL ENV)**: `http://127.0.0.1:5000/twitter/post`
- **Endpoint (PROD)**: `https://baani-backend.onrender.com/twitter/post`
- **Method**: `POST`
- **Description**: Posts a tweet to Twitter.
- **Request Body**: JSON containing `text`.
- **Response**:
  - `200 OK`: Successful post message.
  - `400 Bad Request`: Missing text or authentication required.
  - `500 Internal Server Error`: Server or internal error.

## Usage Notes

- Ensure all API requests are made with the correct method and required parameters.
- Handle error responses appropriately in your application.
- For image uploads, use the correct form-data format.
