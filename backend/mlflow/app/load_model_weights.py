import os.path
import sys
from pathlib import Path
from transformers import AutoTokenizer, AutoModel, AutoConfig

if __name__ == "__main__":
    # Specify the model name or path from Hugging Face
    model_name = "distilgpt2"
    cache_path = sys.argv[1]

    if not os.path.exists(os.path.join(cache_path, "config.json")):
        # Create a model instance
        model = AutoModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        config = AutoConfig.from_pretrained(model_name)

        # Save the weights to a local directory
        model.save_pretrained(cache_path)
        tokenizer.save_pretrained(cache_path)
        config.save_pretrained(cache_path)