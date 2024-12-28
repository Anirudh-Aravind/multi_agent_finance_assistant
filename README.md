
# Financial Analysis Assistant

## Overview

The **Financial Analysis Assistant** is a multi-agent system designed to provide comprehensive financial analysis and market news insights. Utilizing advanced AI agents, this application can analyze stock data, retrieve recent news, and provide key financial metrics for various companies.


![image](https://github.com/user-attachments/assets/1d000f98-bb5b-46e9-b788-646bb568ce93)

![image](https://github.com/user-attachments/assets/7a405d16-3595-44d9-a5f5-e05f3fc7e89c)


## Features

- **Stock Analysis**: Get detailed insights on stocks, including:
  - Latest analyst recommendations
  - Recent news and market sentiment
  - Key financial metrics
  - Market position and competitive analysis

- **Market News**: Analyze recent market trends and news related to specific topics.

- **Enhanced Agents**: The system uses specialized agents for web searching and financial analysis, ensuring accurate and up-to-date information.

- **User-Friendly Interface**: Built with Streamlit for an interactive user experience.

## Technologies Used

- **Python**: The programming language used to develop the application.
- **Streamlit**: A framework for building interactive web applications quickly.
- **phi**: An AI agent framework that facilitates the creation of intelligent agents.
- **Groq**: A model used for processing natural language queries and providing responses.
- **DuckDuckGo**: A search engine used for retrieving web information.
- **GoogleSearch**: A tool for conducting searches on Google to gather relevant data.
- **Yahoo Finance API**: Provides access to financial data and stock market information.

## Installation

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You will also need to have `pip` for package management.

### Clone the Repository

```
git clone https://github.com/Anirudh-Aravind/multi_agent_finance_assistant.git
cd multi_agent_finance_assistant
```

### Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```
python -m venv ai_env
source ai_env/bin/activate  # On Windows use `ai_env\Scripts\activate`
```

### Install Dependencies

Install the required libraries using pip:

```
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root of the project directory and add your API keys:

```
GROQ_API_KEY=your_groq_api_key_here
```

Make sure to replace `your_groq_api_key_here` with your actual API key from Groq (https://console.groq.com/keys).

## Usage

### Running the Application

To start the application, run the following command:

```
streamlit run app.py
```

This will launch the Streamlit app in your default web browser at `http://localhost:8501`.

### Interacting with the Application

1. **Select Analysis Type**: Choose between "Stock Analysis" or "Market News" in the sidebar.
2. **Input Stock Ticker**: For stock analysis, enter the stock ticker symbol (e.g., NVDA for NVIDIA).
3. **Get Analysis**: Click the "Analyze" button to retrieve insights.
4. **View Results**: The analysis results will be displayed along with sources and debugging information.

## Example Usage

- To analyze NVIDIA Corporation (NVDA), enter `NVDA` in the stock ticker input field and click "Analyze".
- For market news related to AI in the semiconductor industry, enter `AI Semiconductor Industry` in the market topic input field and click "Get Analysis".


## Live Demo

You can try out the Financial Analysis Assistant live at the following URL:

https://multi-agent-finance-assistant.streamlit.app/  

**Note**: This is a demo UI. While you can explore the interface, please be aware that hitting any action buttons result in errors due to missing API keys, which are not included in this public repository for security reasons. To run the application locally, you will need to set up your own API keys as described in the installation section.
