# DevOpsAssignment

This repository presents an application to create and run a Docker Container exposing the Tomcat Sample application on the url http://localhost:8080/sample using an ansible playbook.

The files which are part of these repository are:

- ansible.cfg: The Ansible configuration file when running the playbook.
- ansible_inventory: The Ansible Inventory file when running the playbook.
- Dockerfile: The Dockerfile to build the Docker image.
- LICENSE: The License file of this repository. In this case, it is a BSD 3-Clause License.
- run_tomcat.yml: The Ansible Playbook to run the entire application.
- test_tomcat.yml: The Pytest Script to check if a Docker Container exposing the Tomcat sample application is already running.


## Requirements

Install git:
 - sudo apt-get install git


## Steps

- Cloning CFSNM/DevOpsAssignment Github Repository:
    git clone https://github.com/CFSNM/DevOpsAssignment.git




