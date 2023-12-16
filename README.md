
## DevSecOps pipelines/workflows with Github Actions


### SCA Scan with Snyk:

SCA (Software Composition Analysis): check external dependencies/libraries used by the project have no known vulnerabilities. Third-party dependency scanning with Snyk.

Ref: Snyk:
- https://github.com/snyk/actions
- https://github.com/snyk/actions/tree/master/python-3.8
- https://snyk.io/partners/docker/ (Snyk: Configure integration for DockerHub for docker images scanning : https://docs.snyk.io/integrate-with-snyk/snyk-container-integrations/container-security-with-docker-hub-integration/configure-integration-for-docker-hub)

Note: https://app.snyk.io/account to get SNYK_TOKEN

Note: We can use Bandit && Snyk for SAST & SCA (Software Composition Analysis) and Docker Scout for Docker Image scanning: (Bitbucket use Snyk for SCA for example)

Note: We can upload result (serif report) to GitHub Code Scanning using GitHub Action -> github/codeql-action/upload-sarif@v2 (Snyk GitHub integration @https://app.snyk.io/org/adavarski -> https://docs.snyk.io/integrate-with-snyk/git-repositories-scms-integrations-with-snyk/snyk-github-integration)

### Container Image Scanning with Docker Scout:
Identify vulnerabilities in built images -> DockerHub Scout Image Scanner

Note: Docker Scout is available through multiple interfaces, including the Docker Desktop and DockerHub user interfaces, as well as a web-based user interface and a command-line interface (CLI) plugin.
This is a demo about the integration of Docker Scout with GitHub actions using the CLI.

Ref: Docker Scout Links:
- Docker Scout: https://docs.docker.com/scout/
- Docker Scout CLI: https://docs.docker.com/engine/reference/commandline/scout/ && https://github.com/docker/scout-cli
- Docker Scout GitHub Action: https://github.com/docker/scout-action && https://docs.docker.com/scout/integrations/ci/gha/

### Deploy app to k8s (k3d) and OWASP ZAP Scan (DAST: Dynamic Application Security Testing)

Note: K8s is Kubernetes. K3s is a lightweight K8s distribution. K3d is a wrapper to run K3s in Docker. K3d/K3s are especially good for development and CI purposes, as it takes only 20-30 seconds of time till the cluster is ready (for comparison, Kind/Minikube takes more time till ready)

Note: Follow the following steps for fixing ZAP scan error "Resource not accessible by integration"

1) Go to Settings of the repo

2) Click on Actions drop down on the left hand side of the web page

3) From the Actions drop down, Click on General

4) Scroll down, Under Workflow Permissions, see the permission

5) Make sure to Select Read and write permissions
   
7) Check "Allow GitHub Actions to create and aprove pull requests"

8) Click on Save button to save your changes.


### How to generate scan reports (Snyk & Docker Scout & OWASP ZAP)

### How to analyze scan reports (json & serif report files)

Ref: 
https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning

https://www.defectdojo.org

### GitHub Code Scanning using GitHub Actions and Github CodeQL for Code scanning 

Repo "Settings" - < Code Security and Analysis (setup Code scanning: Advanced workflow and view report after CodeQL workflow execution)

### Keeping supply chain secure with Dependabot
Monitor vulnerabilities in dependencies used in your project and keep your dependencies up-to-date with Dependabot.

Ref: https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide

### GH Actions References: 

List of GitHub Actions:

https://github.com/actions
https://github.com/marketplace?type=actions

Events:

https://docs.github.com/en/free-pro-team@latest/actions/reference/events-that-trigger-workflows

GH actions we use in this repo:

https://github.com/docker/scout-action
...

### NOTES

## Demo Docker Node app 

This demo app shows a simple user profile app set up using 
- index.html with pure js and css styles
- nodejs backend with express module
- mongodb for data storage

```
### Local development

To start the application
- Start mongodb and mongo-express

docker-compose -f docker-compose.yaml up -d

You can access the mongo-express under localhost:8080 from your browser

- In mongo-express UI - create a new database "my-db"

- In mongo-express UI - create a new collection "users" in the database "my-db"

- Start node server

cd app
npm install
node server.js

- Access the nodejs application from browser

http://localhost:3000

```

### Build & Push docker image 
```
    docker build -t davarski/k8s-demo-app:v1.0 .
    docker push davarski/k8s-demo-app:v1.0
```  
## K8s local deploy

### K8s manifests

#### K8s manifest files 
- mongo-config.yaml
- mongo-secret.yaml
- mongo.yaml
- webapp.yaml

##### start K3d || KinD
```
k3d cluster create node
kind create cluster --name node
```
#### Apply k8s manifests
```
kubectl apply -f ./k8s/

$ cat k8s/mongo-secret.yaml

$ echo "bW9uZ291c2Vy=="|base64 -d
$ echo "bW9uZ29wYXNzd29yZA=="|base64 -d

kubectl port-forward svc/webapp-service 3000:3000

Browser: http://localhost:3000 ---> add new user 

$ kubectl exec -it mongo-deployment-65ffdd9df6-vh9cd /bin/bash
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
root@mongo-deployment-65ffdd9df6-vh9cd:/# mongo -u "mongouser" -p mongopassword --authenticationDatabase "admin"
MongoDB shell version v5.0.23
connecting to: mongodb://127.0.0.1:27017/?authSource=admin&compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("aa2eeaf5-41a6-4e10-9a5d-4390f9356442") }
MongoDB server version: 5.0.23
================
Warning: the "mongo" shell has been superseded by "mongosh",
which delivers improved usability and compatibility.The "mongo" shell has been deprecated and will be removed in
an upcoming release.
For installation instructions, see
https://docs.mongodb.com/mongodb-shell/install/
================
---
The server generated these startup warnings when booting: 
        2023-12-15T13:05:42.999+00:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
---
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
my-db   0.000GB

> use my-db
switched to db my-db
> show collections
users

> db.users.find()
{ "_id" : ObjectId("657c4fbb7ece34696a0a9838"), "userid" : 1, "email" : "ana.smith@example.com", "interests" : "coding,k8s", "name" : "Ana Smith" }
> 

```
```
##### get basic info about k8s components
    kubectl get node
    kubectl get pod
    kubectl get svc
    kubectl get all

##### get extended info about components
    kubectl get pod -o wide
    kubectl get node -o wide

##### get detailed info about a specific component
    kubectl describe svc {svc-name}
    kubectl describe pod {pod-name}

##### get application logs
    kubectl logs {pod-name}

#### Access web app

kubectl port-forward svc/webapp-service 3000:3000
```
##### delete K3d || Kind cluster
```
k3d cluster delete node
kind delete cluster --name=node
```
#### Links
* mongodb image on Docker Hub: https://hub.docker.com/_/mongo
* webapp image on Docker Hub: https://hub.docker.com/repository/docker/davarski/k8s-demo-app
* k8s official documentation: https://kubernetes.io/docs/home/





