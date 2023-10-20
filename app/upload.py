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


    pipe.upload_artifact(
        name="upload weights",
        wait_on_upload=True,
        artifact_object="/Users/akash/Downloads/model.safetensors.gz"
    )

    pipe.start_locally(run_pipeline_steps_locally=True)
    #pipe.start(queue="k8s_scheduler")

    print("pipeline completed")

