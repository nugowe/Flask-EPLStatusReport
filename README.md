## ABOUT THE APP

The App is a flask Application with context revolving around the English Premier League for Season 2023/2024. It contains a carousel of the all the Logos of the 20 participating Teams in the 2023/2024 Season.

## WSGI WEBSERVER

This App contains a WSGI Server which converts Python's single-threaded apps such a Flask to a multi-thread one, to handle concurrency. It also binds the app to a listening port or socket. The WSGI Server used for this Application is Gunicorn.

## REVERSE PROXY SERVER

Nginx is used as a reverse proxy server, it acts as an intermediary between the enduser and the app, the doubles as both a reverse proxy server and a Load Balancer. This reverse proxy server listens to the defined endpoint on the app where the exposed port or unix socket is rendered. 

## KUBERNETES CLUSTER (OPTIONAL)

The CI/CD contains resources to deploy a Kubernetes cluster and Helm Charts.

## OBSERVABILITY STACK:
### PROMETHEUS: Prometheus scrapes metrics from the /metrics endpoint within the kubernetes cluster. The flavor of prometheus being deployed in that of kube-promethueus-stack. It consists of Node-Exporter, Cadvisor, Prometheus-Operator and Grafana. 

## GRAFANA LOKI:
It is used for collating logs and has the option to use Object storage like s3 buckets in order to save costs and enjoy the many benefits object storage provides. It is lighter due to the fact that metadata is indexed so it is easier to read and call logs.

## GRAFANA TEMPO:
Created by Grafana Labs, Grafana Tempo is used to provide tracing, where by user requests can be observed from enduser down to the backend. It takes advantage of the metadata labelling of Tempo to provide span view of any given log metadata.


## USAGE Dockerfile

Docker build -t nosaugowe/epl-flask:latest 7878:7878

## USAGE KUBERNETES

No ingress was defined, so you can port-forward your service deployment to view the App. 


![EPLStatusReport](https://github.com/nugowe/Flask-EPLStatusReport/assets/25004712/bd537abe-815b-4d1c-9dfc-f995b63294d3)




