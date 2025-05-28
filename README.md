# Recipe Processor

## Introduction
This project aims to transform unstructured recipe text into a structured, database-friendly format. Using OpenAI's GPT-4 model, the system can parse any recipe text, regardless of its original format, and convert it into a standardized structure that includes ingredients (with amounts and units) and step-by-step instructions. This makes it easy to store, search, and manage recipes in a database system.

## Prerequisites
- Python 3.11 or higher
- Node.js and npm (for React frontend)
- OpenAI API key

## Installation

### Backend Setup
1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'  # On Windows, use: set OPENAI_API_KEY=your-api-key-here
```

### Frontend Setup
1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install the required dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

## Usage
The backend provides an API endpoint that accepts recipe text and returns structured data. The frontend provides a user-friendly interface for submitting recipes and viewing the structured results.

## License
This project is provided "as is" under the MIT License. Feel free to use, modify, and distribute it as you wish. 