from clearml import PipelineController
from api import classify

if __name__ == "__main__":

    pipe = PipelineController(
        project="bart_large",
        name="Sentiment Analysis using Bart",
        version="1.0.0",
        docker="dawker/bart-large-mnli:latest",
    )

    pipe.set_default_execution_queue("k8s_scheduler")

    # add pipeline components
    pipe.add_function_step(
        name="Run Model",
        function=classify,
        #function_kwargs=dict(dataset_spec_params="${pipeline.dataset_spec_params}"),
        #function_return=["dataset_spec"],
        cache_executed_step=False,
        docker="dawker/bart-large-mnli:latest",
        docker_bash_setup_script="./run.sh"
    )

    pipe.start(queue="k8s_scheduler")

    print("pipeline completed")

