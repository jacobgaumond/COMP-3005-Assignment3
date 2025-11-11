# COMP-3005-Assignment3

This repo is a submission to a university project for the course COMP 3005 Database Management Systems at Carleton University

## Purpose

This project locally hosts a PostgreSQL server through a podman (preferred) or docker container.

The PostgreSQL server is initialized with a setup script by the podman container.

The project interacts with the PostgreSQL server using limited commands through a python application.

## Instructions

All commands are executed through the CLI using this repo's directory.

### Requirements

The following applications must be installed to run this project:
    - python3
    - podman (or docker)
    - podman compose (or docker compose)

### Python Setup

This project requires a python virtual environment with a pip package used to interact with PostgreSQL.

To automatically setup the python virtual environment, execute the following:
    - `./setup-python.sh`

### Database Setup

To launch the database, use the following CLI command:
    - `podman compose up -d` or `docker compose up -d`

### Running The App

Assuming the python setup command (above) has been ran, run the app with the following:
    - `./run-app.sh`

### Database Teardown

To stop the database, use the following CLI command:
    - `podman compose down` or `docker compose down`
