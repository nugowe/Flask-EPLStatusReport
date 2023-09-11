# Variables
IMAGE_NAME := eplstatusreport
IMAGE_TAG := latest
REGION := us-east-2
CLUSTER_NAME := epl


update_kubecontext:
	aws eks --region $(REGION) update-kubeconfig --name=$(CLUSTER_NAME)

deploy_app:
	kubectl create -f $GITHUB_WORKSPACE/src-kubernetes/