Description
A multi-vendor marketplace modeled after Etsy deployed using docker.
The application is running on port 5000 and nginx is used as a load balancer to forward traffic from HTTP to the application.
Both the application and load balancer are deployed as containers.

docker-compose.yml file is being used to deploy multi-containers of application and load balancer to deploy simultaneously.

Application usage can be checked from forked repository : https://github.com/NTielman/Betsy

To run application as container use below command:
docker-compose build
docker-compose up -d (-d flag can be removed in case user does not want to run on detach mode)
Application can be accessed on http://localhost:5000/

Note: Please comment out line 12 (create_fake_db_accounts()) from main.py after db is created as this is not handled in code and can lead to runtime error.
