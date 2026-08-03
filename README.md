# Stock Trading News Alert Project

A Python application that monitors Tesla (TSLA) stock price changes and fetches relevant news when significant price movements occur (≥5% change).

## Features

- Fetches daily stock data from Alpha Vantage API
- Calculates percentage change from last two trading days
- Retrieves top 3 news articles from News API when threshold is met
- Caches API responses for efficiency
- (Optional) Sends SMS alerts via Twilio

## Setup

### Prerequisites
- Python 3.7+
- pip

### Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install requests twilio requests-cache
```

3. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

4. Add your API keys to the `.env` file:
   - Get Alpha Vantage API key from https://www.alphavantage.co
   - Get News API key from https://newsapi.org
   - (Optional) Get Twilio credentials from https://www.twilio.com

## Usage

```bash
python main.py
```

The script will:
1. Fetch Tesla's stock price from the last two trading days
2. Calculate the percentage change
3. If change ≥ 5%, fetch and display relevant news articles
4. (Optional) Send SMS notification

## Environment Variables

See `.env.example` for all required environment variables.

## API Limits

- Alpha Vantage: 5 calls/minute (free tier)
- News API: 100 requests/day (free tier)
- Responses are cached for 1 hour to minimize API calls
