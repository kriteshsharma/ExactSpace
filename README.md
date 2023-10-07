Description: 
A multi-vendor marketplace modeled after Etsy deployed using docker.
The application runs on port 5000 and nginx is used as a load balancer to forward traffic from HTTP to the application.
Both the application and load balancer are deployed as containers.

docker-compose.yml file is being used to deploy multi-containers of application and load balancer to deploy simultaneously.

Application usage can be checked from the forked repository: https://github.com/NTielman/Betsy

To run the application as a container use the below command:
docker-compose build
docker-compose up -d (-d flag can be removed in case the user does not want to run on detach mode)
The application can be accessed at http://localhost:5000/

Note: Please comment out line 12 (create_fake_db_accounts()) from main.py after db is created as this is not handled in code and can lead to runtime error.

A Jenkins file is also provided in case of configuring applications for CI/CD.
