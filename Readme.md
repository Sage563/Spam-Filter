# Spam Filter

This project is a Python-based spam filtering system that uses machine learning models to classify YouTube comments as "Spam" or "Not Spam." It also provides sentiment analysis and scoring for the comments.

## Features

1. **YouTube Comment Fetching**:
   - Fetches comments from a YouTube video using the YouTube Data API.
   - Saves the fetched comments in `video_data.json`.

2. **Spam Detection**:
   - Uses a pre-trained DistilBERT model for spam classification.
   - Results are saved in `fullresults.json` and filtered non-spam comments are saved in `spam_results.json`.

3. **Sentiment Analysis**:
   - Uses a multilingual sentiment analysis model to classify comments into sentiment categories: "Very Negative," "Negative," "Neutral," "Positive," and "Very Positive."
   - Results are saved in `results.json`.

4. **Scoring System**:
   - Calculates an overall score based on the sentiment of the comments.
   - Provides a rating based on the score.

5. **Interactive CLI**:
   - Allows users to input a YouTube video URL and the number of comments to fetch.
   - Provides options to display results, overall score, and spam detection results.

## File Structure




## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd spam_filter