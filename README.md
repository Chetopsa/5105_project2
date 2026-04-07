# Project Setup and Evaluation Guide

Group: 
- Cheston Opsasnick (opsas002)
- Quenton Ni (ni001000)

## Setting Up the Project

1. Navigate to the `docker` folder.
2. Run the following commands to set up the Docker environment:
   ```bash
   docker compose down
   docker rm -f $(docker ps -aq --filter "name=storage-node")
   docker compose up --build -d
   ```
3. Open the project repository in a development container in VsCode

## Running Evaluations

1. To evaluate the system, run:

   ```bash
   python3 evaluation/score_all_questions.py
   ```

2. To check the status of the nodes created, run:

   ```bash
   python3 evaluation/cluster_status.py
   ```

## Enabling Multi-Probe Search

1. To enable the Multi-Probe Search implementation:
   - Open `controller.py`.
   - On line 15, set the variable:

     ```python
     MULTI_PROBE_SEARCH_ENABLED = True
     ```

2. Follow the setup steps again to re-evaluate the new results, make sure to compose down first.

