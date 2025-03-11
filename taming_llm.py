{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "mrg7bEjo8JZ_"
   },
   "outputs": [],
   "source": [
    "import os\n",
    "from dotenv import load_dotenv\n",
    "import groq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "Fu_hlv4-6xwj"
   },
   "outputs": [],
   "source": [
    "class LLMClient:\n",
    "    def __init__(self):\n",
    "        load_dotenv()\n",
    "        self.api_key = os.getenv(\"GROQ_API_KEY\")\n",
    "        self.client = groq.Client(api_key=self.api_key)\n",
    "        self.model = \"llama3-70b-8192\"  # Or another Groq model\n",
    "\n",
    "    def complete(self, prompt, max_tokens=1000, temperature=0.7):\n",
    "        try:\n",
    "            response = self.client.chat.completions.create(\n",
    "                model=self.model,\n",
    "                messages=[{\"role\": \"user\", \"content\": prompt}],\n",
    "                max_tokens=max_tokens,\n",
    "                temperature=temperature\n",
    "            )\n",
    "            return response.choices[0].message.content\n",
    "        except Exception as e:\n",
    "            print(f\"Error: {e}\")\n",
    "            return None\n",
    "\n",
    "    def create_structured_prompt(self, text, question):\n",
    "        return f\"\"\"\n",
    "        # Analysis Report\n",
    "\n",
    "        ## Input Text\n",
    "        {text}\n",
    "\n",
    "        ## Question\n",
    "        {question}\n",
    "\n",
    "        ## Analysis\n",
    "        \"\"\"\n",
    "\n",
    "    def extract_section(self, completion, section_start, section_end=None):\n",
    "        start_idx = completion.find(section_start)\n",
    "        if start_idx == -1:\n",
    "            return None\n",
    "        start_idx += len(section_start)\n",
    "        if section_end is None:\n",
    "            return completion[start_idx:].strip()\n",
    "        end_idx = completion.find(section_end, start_idx)\n",
    "        if end_idx == -1:\n",
    "            return completion[start_idx:].strip()\n",
    "        return completion[start_idx:end_idx].strip()\n",
    "\n",
    "    def classify_with_confidence(self, text, categories, confidence_threshold=0.8):\n",
    "        prompt = f\"\"\"\n",
    "        Classify the following text into exactly one of these categories: {', '.join(categories)}.\n",
    "\n",
    "        Response format:\n",
    "        1. CATEGORY: [one of: {', '.join(categories)}]\n",
    "        2. CONFIDENCE: [high|medium|low]\n",
    "        3. REASONING: [explanation]\n",
    "\n",
    "        Text to classify:\n",
    "        {text}\n",
    "        \"\"\"\n",
    "        response = self.complete(prompt, max_tokens=500, temperature=0)\n",
    "        category = self.extract_section(response, \"1. CATEGORY: \", \"\\n\")\n",
    "        confidence_score = self.analyze_confidence(response)\n",
    "        if confidence_score > confidence_threshold:\n",
    "            return {\n",
    "                \"category\": category,\n",
    "                \"confidence\": confidence_score,\n",
    "                \"reasoning\": self.extract_section(response, \"3. REASONING: \")\n",
    "            }\n",
    "        else:\n",
    "            return {\n",
    "                \"category\": \"uncertain\",\n",
    "                \"confidence\": confidence_score,\n",
    "                \"reasoning\": \"Confidence below threshold\"\n",
    "            }\n",
    "\n",
    "    def analyze_confidence(self, response):\n",
    "        # Placeholder for logprobs analysis; adjust as needed based on Groq API\n",
    "        if \"high\" in response:\n",
    "            return 0.9\n",
    "        elif \"medium\" in response:\n",
    "            return 0.6\n",
    "        else:\n",
    "            return 0.3\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    client = LLMClient()\n",
    "    text = \"The product arrived late and damaged.\"\n",
    "    categories = [\"Positive\", \"Mixed\", \"Negative\"]\n",
    "    result = client.classify_with_confidence(text, categories)\n",
    "    print(result)"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
