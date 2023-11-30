# LLM-Generated Text Detection Service

## Overview
(You can find detailed answers to the assignment questions in a separate [file](backend/README.md))


This repository offers an Dockerized application to distinguish if a text was generated by AI or a human.
The service makes decisions based on an LLM.

The success of the task of detecting AI-generated texts is heavily dependent on the underlying model used for text generation. 
The more advanced the model, the more difficult it gets to tell artificial and human-written utterances apart. 
Open AI, the creators of ChatGPT, admitted [\[1\]](https://openai.com/blog/new-ai-classifier-for-indicating-ai-written-text) that they were not yet satifsied with the classification accuracy of an analogous detection model they had developed to identify ChatGPT-generated texts, as it could recognize only 26% of AI-texts as such.


## Features

- RESTful API for detecting AI-generated text and providing feedback
- Prometheus metrics integration for performance monitoring
- Grafana for visualizing metrics

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Build and Run

1. Clone the repository:

   ```bash
   git clone https://gitfront.io/r/marina-sp/sQtTB9zKkxdp/llm-recognition.git
   cd llm-recognition

2. Start Docker containers (setup requires some time for downloading required libraries, etc):

    ```bash
   docker-compose -f backend/docker-compose.yml -p backend up  
   
3. Run sample queries directly with CURL (CPU runtime might be longer):

    ```bash
   bash ./run_queries.sh 

### Monitoring

Access the services API docs at http://localhost:8000/docs

Access Prometheus at http://localhost:9090

Access Grafana at http://localhost:3000 (default credentials: admin/admin)
