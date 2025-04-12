
![image](https://github.com/user-attachments/assets/1f8e231c-97ab-422f-8ee9-5ff9b69fff7e)
# Real-Time Reddit Sentiment Analysis

This project performs real-time sentiment analysis on comments from a specified Reddit subreddit (default: `r/technology`) using the PRAW Reddit API, Redis for queue management, and NLTK's VADER for sentiment scoring.

## Overview

- **Producer Script**: Continuously streams Reddit comments and pushes them to a Redis queue.
- **Consumer Script**: Processes comments from the Redis queue, analyzes sentiment, and stores the results in Redis.
- **Output**: Sentiment analysis results (Positive, Negative, or Neutral) with compound scores, saved per comment ID.

## Features

- Real-time streaming of Reddit comments.
- Sentiment analysis using VADER (Valence Aware Dictionary and sEntiment Reasoner).
- Storage of raw and analyzed data in Redis for scalability.
- Configurable via environment variables.

## Prerequisites

- Python 3.7+
- Redis server (running locally at `localhost:6379` by default)
- Required Python packages:
  - `praw` (Reddit API wrapper)
  - `redis`
  - `nltk`
  - `python-dotenv`

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
