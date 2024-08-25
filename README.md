# Airflow Job Scraper: Google Jobs to PostgreSQL & S3 with Docker

This project is an automated job scraper that collects job listings from Google Jobs using SerpApi, stores them in a PostgreSQL database, and uploads the job data to an S3-compatible storage service. The project is orchestrated using Apache Airflow and is designed to run in a Dockerized environment.

## Project Structure

- **`job_scraper_dag.py`**: Defines the Airflow DAG that runs the job scraper and uploads the results to S3.
- **`db_initiate.py`**: Script to initialize the PostgreSQL database and create necessary tables.
- **`db_manager.py`**: Manages database interactions, including adding new job listings and removing old ones.
- **`s3_manager.py`**: Handles file uploads to S3.
- **`scraper.py`**: Contains the logic for scraping jobs from Google Jobs using SerpApi.
- **`compose.yml`** & **`compose.override.yml`**: Docker Compose files to set up the environment, including Airflow, PostgreSQL, and MinIO.
- **`dockerfile`**: Dockerfile to build the custom Airflow image with required dependencies.
- **`requirements.txt`**: Python dependencies required for the project.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your machine.
- A SerpApi account with an API key.
- AWS S3 or S3-compatible storage service credentials (e.g., MinIO).

## Steps to Run the Project

1. **Clone the Repository**

   ```bash
   git clone https://github.com/muhtasim-rif/portfolio.git.
   
2. **Configure Environment Variables**

    Update the compose.override.yml file with your SerpApi key, S3 bucket name, and S3 credentials.

3. **Build and Start the Services**

    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images and start the Airflow, PostgreSQL, and MinIO services.

4. **Initialize the Database**

    Run the database initialization script to create the required tables in PostgreSQL:
    ```bash
    docker exec -it <airflow-container-name> python /opt/airflow/db_initiate.py

5. **Access the Airflow Web UI**

    Once all services are running, access the Airflow web UI by navigating to 
    http://localhost:8000 in your browser.

6.  **Trigger the DAG**

    In the Airflow UI, find the job_scraper DAG and trigger it manually. The DAG is also scheduled to run daily at 8:00 PM (Asia/Dhaka time).


    ## Customization


    -   Job Query: Modify the job query parameters in scraper.py if you want to scrape jobs for different roles or locations.

    -   Database Management: Customize the logic in db_manager.py to manage how job listings are updated or removed.

    ## Troubleshooting

    -   Database Connection Issues: Ensure that the AIRFLOW__CORE__SQL_ALCHEMY_CONN environment variable is correctly set in the compose.override.yml file.

    -   MinIO Setup: Verify that the MinIO service is correctly configured and running. You can access the MinIO console at http://localhost:9000.

    ## License

    This project is licensed under the MIT License. See the LICENSE file for more information.

    ## Contributing
    
    Contributions are welcome!

    ## Contact
 
    For any questions or issues, please contact muhtasim.riffat@gmail.com.

