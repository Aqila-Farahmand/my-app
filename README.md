# Containerized Hello World App

This project is a simple containerized application that displays "hello world, {name}" where {name} is retrieved from a database.

## Components

- **Database**: MongoDB
- **Web Server**: Flask (Python)
- **Orchestration**: Docker Compose

## Prerequisites

- Docker
- Docker Compose

## Instructions to Build and Run

1. Clone this repository:
    ```sh
    git clone <https://github.com/Aqila-Farahmand/my-app.git>
    cd my-app
    ```

2. Build and run the containers using Docker Compose:
    ```sh
    docker-compose up --build
    ```

3. Open your web browser and visit `http://localhost:8080`. You should see "hello world, {name}" with {name} replaced by the name from the database.


## Security Considerations

- Environment variables are used for passing database credentials. 
- For production, consider using secret management tools like Docker Secrets or [HashiCorp Vault](https://www.vaultproject.io/).
- Ensure proper firewall settings and network configurations to protect the database from unauthorized access.
## Clean Up

To stop and remove the containers, use:
```sh
    docker compose down
```

## References
Some of the files and initial setups were inspired by official documentation. 
For more detailed information, refer to the following resources:

- [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
