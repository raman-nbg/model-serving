# Run kafka local on your development machine

1. Install docker
2. Install docker compose
3. `cd` into this directory
4. Run all services using `docker-compose up`
5. Add the following lines to you hosts file to access the services from your host machine
    ```
    127.0.0.1 kafka
    127.0.0.1 kafka-schema-registry
    127.0.0.1 kafka-rest-proxy
    127.0.0.1 kafka-topics-ui
    127.0.0.1 schema-registry-ui
    ```