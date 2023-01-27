# APIHarvest

## Installation

You need the following dependencies:

-   Node.js and npm (the Node.js package manager)
-   Python 3.9
-   docker

You can start the Elasticsearch server by running the following command in your terminal:

    docker pull elasticsearch:7.10.1

    docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.10.1

### Clone the repository

To get started, clone the repository to your local machine:

`git clone https://github.com/soarsmu/APIHarvest.git` 

### Install the dependencies

Navigate to the project directory:

`cd APIHarvest` 

Install the Node.js dependencies:

`npm install` 

Install the Python dependencies:

`pip install -r requirements.txt` 

### Start the application

To start the application, run the following command:

`npm start` 

The application will be available at [http://localhost:3000](http://localhost:3000/).



