import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Completion.create(
  engine="davinci",
  prompt="This is a research paper title generator. \n Seed titles: \n The Rediscovery Hypothesis: Language Models Need to Meet Linguistics \n A Word Selection Method for Producing Interpretable Distributional Semantic Word Vectors \n Learning Realistic Patterns from Visually Unrealistic Stimuli: Generalization and Data Anonymization \n Flexible Bayesian Nonlinear Model Configuration \n Multi-Label Classification Neural Networks with Hard Logical Constraints. \n Generated titles:",
  temperature=0.5,
  max_tokens=120,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response["choices"][0]["text"])

