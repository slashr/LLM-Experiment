from clearml import PipelineController
from app.api import classify

if __name__ == "__main__":
    setup_pretty_logging(*PRETTY_LOGGING_MODULES, level=logging.DEBUG)

    pipe = PipelineController(
        project="bart_large",
        name="Sentiment Analysis using Bart",
        # add_pipeline_tags=False,
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
        repo="https://github.com/slashr/LLM-Experiment.git",
        repo_branch="main",
    )
