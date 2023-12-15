
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

### Deploy app to k8s (k3d) and OWASP ZAP Scan

### How to generate scan reports (Snyk & Docker Scout)

### How to analyze scan reports (json & serif report files)

Ref: 
https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning

https://www.defectdojo.org

### GitHub Code Scanning using GitHub Actions and Github CodeQL for Code scanning 

Repo "Settings" - < Code Security and Analysis (setup Code scanning: Advanced workflow and view report after CodeQL workflow execution)

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

### Build & Push docker image 
```
    docker build -t davarski/k8s-demo-app:v1.0 .
    docker push davarski/k8s-demo-app:v1.0
```  
## K8s 

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





