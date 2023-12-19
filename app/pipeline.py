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
#    pipe.set_default_execution_queue("default")
#
#    # add pipeline components
#    pipe.add_function_step(
#        name="akash_test",
#        function=classify,
#        #function_kwargs=dict(dataset_spec_params="${pipeline.dataset_spec_params}"),
#        #function_return=["dataset_spec"],
#        cache_executed_step=False,
#        docker="dawker/bart-large-mnli:latest",
#        repo="https://github.com/slashr/LLM-Experiment",
#        repo_branch="clearml",
#    )
#
#    #pipe.start_locally(run_pipeline_steps_locally=True)
#    pipe.start(queue="default")
#
#    print("pipeline completed")
#

def execute_remotely(project_name="akash_project", task_name="akash_task"):
    # TODO - add type, tags
    task = Task.init(project_name=project_name, task_name=task_name)
    task.set_base_docker(
        docker_image="dawker/bart-large-mnli:latest"
    )
    task.execute_remotely(queue_name="default")
    # Change the directory to where the app is stored
    # Default directory is /
    os.chdir("/app")
    from api import classify
    classify()

if __name__ == "__main__":
    # Comment out to run locally
    execute_remotely(project_name="akash_project", task_name="akash_test")
