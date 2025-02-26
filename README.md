# YouTube Summary

## Description

This project summarizes YouTube videos using the YouTube Transcript API and the OpenRouter API. It extracts the transcript from a YouTube video, then uses the OpenRouter API to generate a summary of the transcript.

- `main.py`: This is the main script that contains the logic for extracting the transcript and generating the summary.
- `requirements.txt`: This file contains a list of the Python packages that are required to run the project.

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2.  Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3.  Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

4.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Set the environment variable for the OpenRouter API key.

2.  Run the script:

    ```bash
    python main.py --url <youtube_video_url>
    ```

    Replace `<youtube_video_url>` with the URL of the YouTube video you want to summarize.

## API Key

You will need an OpenRouter API key to use this project. You can get an API key from [https://openrouter.ai/](https://openrouter.ai/).

Set the API key as an environment variable named `OPENROUTER_API_KEY`. For example, you can add the following line to your `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.
