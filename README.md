# FastAPI Tweet Search API

This is a simple API built with FastAPI that allows users to search for tweets containing specific terms.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

First, clone the repository to your local machine:

```bash
git clone https://github.com/rajshirolkar/tweet_search.git
```

Navigate to the cloned repository:

```bash
cd tweet_search
```

It is recommended to use a virtual environment to isolate the project dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Then install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Server

To start the FastAPI server, use the following command:

```bash
uvicorn app:app --reload
```

The `--reload` flag enables auto-reloading of the server after changes to the code, which is useful during development.


## Quick Start

If you're feeling lazy and want to get everything up and running quickly, you can use the provided script `start_server.sh`. This script will create a virtual environment, install the required dependencies, and start the FastAPI server.

Run the following command in the terminal:

```bash
./start_server.sh
```

You might need to give executable permissions to the script before running it:

```bash
chmod +x start_server.sh
```

## Using the API

Once the server is running, you can interact with the API in two ways:

### Swagger UI

FastAPI generates a Swagger UI for your API, which allows you to test the API endpoints directly from your browser.

- Open your web browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
- You will see a list of available API endpoints. Click on the `/search/` endpoint.
- Click on "Try it out".
- You can add search terms by clicking on "Add string item" under the `terms` query parameter.
- After adding your search terms, click "Execute" to send a request to the API.
- The Swagger UI will display the curl command, the request URL, and the server response.

### curl

You can also use `curl` from the command line to send requests to the API:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/search/?terms=sounds&terms=here%27s' \
  -H 'accept: application/json'
```

Replace `sounds` and `here's` with your search terms. The response will be the JSON representation of the top tweets related to the search terms.