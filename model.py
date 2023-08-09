import pprint
#Import the Pipeline
from transformers import pipeline

classifier = pipeline(
                      task="zero-shot-classification",
                      device="1",
                      model="facebook/bart-large-mnli"
                    )

S = "I am not able to focus on my work"
L = ["Employment", "News", "Disease"]

predictions = classifier(S, L, multi_class=False)
pprint.pprint(predictions)