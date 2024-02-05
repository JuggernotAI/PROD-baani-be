# Technical Documentation for Baani: Social Media Automation Agent

## Introduction

Baani is an AI-powered social media automation agent designed to create, repurpose, schedule, and post content on behalf of users. It integrates with various platforms like LinkedIn and Twitter, and uses advanced AI techniques, including OpenAI's Dall-E, for content and image generation.

## System Overview

Baani consists of several components working together to provide a seamless user experience in social media content creation and management. The system is built using Python and Flask and interacts with external APIs for content generation and social media integration.

## Directory Structure

- `app.py`: Flask application setup and route definitions.
- `main.py`: Core functionalities for chat interactions and function execution.
- `function/`: Modules for specific functionalities (Dall-E image generation, LinkedIn and Twitter posts).
- `image/`: Image-related operations, including Dall-E image handling.
- `instructions/`: Instructions for the content creation process.
- `interface/`: User interface components, like terminal interfaces.
- `tools.py`: Definitions of tools used in the application.

## Key Modules

### 1. `app.py`

- Initializes the Flask application and sets up API routes.
- Handles requests for chat initialization, response generation, image uploads, and social media postings.
- Manages OAuth authentication for Twitter.

### 2. `main.py`

- Processes chat messages and generates responses using OpenAI's GPT model.
- Executes functions like image generation and social media posting based on user interactions.

### 3. `function/` Directory

- `dalle_executor.py`: Manages image generation using Dall-E.
- `linkedin_executor.py`: Handles posting to LinkedIn.
- `twitter_executor.py`: Manages posting tweets to Twitter.
- `twitter_function_call.py`: Alternative implementation for Twitter interactions.

### 4. `instructions/system_instructions.py`

- Contains instructions for the content creation process.
- Guides the application's interaction with users and adherence to content guidelines.

### 5. `tools.py`

- Defines a list of tools available for use in the application.
- Includes tools for adding numbers, generating images, and making posts on LinkedIn and Twitter.

## Setup and Installation

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up environment variables for API keys and tokens.
4. Run `python app.py` to start the Flask server.

## Required ENV variables

- TODO

## API

For detailed information on the available API endpoints and how to use them, please refer to the API documentation provided in [API_DOCUMENTATION.md](API_DOCUMENTATION.md).
  
## Usage

- Users can interact with Baani through the defined API endpoints.
- Baani assists users in creating content for social media, adhering to platform-specific guidelines.
- Users can request image generation, which Baani handles using Dall-E.
- After content creation, Baani can post the content to LinkedIn or Twitter with user approval.

## Contributing

- Follow the project's coding standards and guidelines for contributions.
- Ensure proper testing and documentation for any new features or changes.

## Contact and Support

For assistance or to report issues, contact the project maintainers or use the designated support channels.
