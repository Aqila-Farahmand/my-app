# Hello World App with Docker

This project contains a simple web application that displays "Hello World, {name}" fetched from a MongoDB database.

## Prerequisites

- Docker
- Docker Compose

## How to Build and Run the Solution

1. Clone this repository:
    ```sh
    git clone <repository-url>
    cd docker-app
    ```

2. Build and run the containers using Docker Compose:
    ```sh
    docker-compose up --build
    ```

3. Open your web browser and visit `http://localhost:5001`. You should see "Hello World, YourName".

## Clean Up

To stop and remove the containers, use:
```sh
    docker-compose down
```

## References
Some of the Dockerfiles and initial setups to pull docker images were inspired by official documentation and various publicly available tutorials. 
Refer to the [official Docker](https://docs.docker.com/) and [Docker Hub](https://hub.docker.com/) documentation for more details.