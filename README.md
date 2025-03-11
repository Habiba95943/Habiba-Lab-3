# Taming LLMs with Groq API
# Habiba Khalil - 202200720
## Overview
This project implements a content classification and analysis tool using the Groq API. The tool applies structured prompting, confidence analysis, and prompt strategy comparisons to evaluate model performance.

## Features
- **Basic API Completion**: Generates responses using Groq's API.
- **Structured Prompting**: Extracts specific insights from completions.
- **Classification with Confidence Analysis**: Evaluates model confidence.
- **Prompt Strategy Comparison**: Tests different approaches to prompting.

## Setup Instructions

### **1. Clone the Repository**
```sh
git clone https://github.com/Habiba95943/Habiba-Lab-3
cd taming_llm_assignment
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Set Up API Key**
1. Create a `.env` file in the root directory.
2. Add your **Groq API key**:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

### **4. Run the Script**
```sh
python taming_llm.py
```

## Notes
- Ensure the Groq API key is valid and stored in the `.env` file.
- Use structured prompts for improved accuracy.
- For debugging, handle API errors gracefully.