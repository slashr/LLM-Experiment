from clearml import PipelineController
from clearml import Task  # type: ignore
import os
import subprocess

#if __name__ == "__main__":
#
#    pipe = PipelineController(
#        project="bart_large",
#        name="Sentiment Analysis using Bart",
#        version="1.0.0",
#        docker="dawker/bart-large-mnli:latest",
#    )
#
#    pipe.set_default_execution_queue("jobs_cpu_14gb")
#
#
##    docker_setup_script = """
##    #!/bin/bash
##    echo "Running docker setup bash script..."
##    python api.py
##    """
#
#    # add pipeline components
#    pipe.add_function_step(
#        name="akash_test",
#        function=classify,
#        #function_kwargs=dict(dataset_spec_params="${pipeline.dataset_spec_params}"),
#        #function_return=["dataset_spec"],
#        cache_executed_step=False,
#        docker="dawker/bart-large-mnli:latest",
#        docker_bash_setup_script=docker_setup_script,
#        repo="https://github.com/slashr/LLM-Experiment",
#        repo_branch="clearml",
#    )
#
#    #pipe.start_locally(run_pipeline_steps_locally=True)
#    pipe.start(queue="jobs_cpu_14gb")
#
#    print("pipeline completed")
#

def execute_in_docker():
    # This code will run in the Docker container
    print("Current Working Directory:", os.getcwd())
    os.chdir("/")
    print("Changed Working Directory:", os.getcwd())
    print("Files:", os.listdir(os.getcwd()))

    uname_result = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE, text=True)
    print("UNAME", uname_result.stdout)

    whoami_result = subprocess.run(['whoami'], stdout=subprocess.PIPE, text=True)
    print("WHOAMI", whoami_result.stdout)

    df_result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE, text=True)
    print("DF", df_result.stdout)

def execute_remotely(project_name="akash_project", task_name="akash_task"):
    # TODO - add type, tags
    task = Task.init(project_name=project_name, task_name=task_name)
    task.set_base_docker(
        docker_image="dawker/bart-large-mnli:latest"
    )
    # task.execute_remotely(queue_name="k8s_scheduler")
    task.execute_remotely(queue_name="default")
    execute_in_docker()



if __name__ == "__main__":
    # Comment out to run locally
    execute_remotely(project_name="akash_project", task_name="akash_test")
#    current_directory = os.getcwd()
#    print("Current Working Directory:", current_directory)
#    os.chdir("/") 
#    current_directory = os.getcwd()
#    print("Changed Working Directory:", current_directory)
#    print("Files:", os.listdir(current_directory))
#    uname_result = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE, text=True)
#    print("UNAME", uname_result) 
#    whoami_result = subprocess.run(['whoami'], stdout=subprocess.PIPE, text=True)
#    print("WHOAMI", whoami_result)
#    df_result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE, text=True)
#    print("DF", df_result)
#
