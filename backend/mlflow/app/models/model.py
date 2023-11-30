import transformers
import mlflow
import torch

class LLM(torch.nn.Module):

    def __init__(self, model_path):
        """
        This method initializes the tokenizer and language model
        using the specified model snapshot directory.
        """
        super().__init__()

        # Initialize tokenizer and language model
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(model_path)

        config = transformers.AutoConfig.from_pretrained(model_path)

        self.model = transformers.AutoModelForCausalLM.from_pretrained(
            model_path,
            config=config,
            torch_dtype=torch.bfloat16,
        )
        self.model.eval()

    def _build_prompt(self, instruction):
        """
        This method generates the prompt for the model.
        """
        INSTRUCTION_KEY = "### Instruction:"
        RESPONSE_KEY = "### Response:"
        INTRO_BLURB = (
            "Below is an instruction that describes a task. "
            "Write a response that appropriately completes the request."
        )

        return f"""{INTRO_BLURB}
        {INSTRUCTION_KEY}
        {instruction}
        {RESPONSE_KEY}
        """

    def predict(self, model_input):
        """
        This method generates prediction for the given input.
        """
        prompt = model_input["prompt"]
        temperature = model_input.get("temperature", 1.0)
        max_tokens = model_input.get("max_tokens", 100)

        # Build the prompt
        prompt = self._build_prompt(prompt)

        # Encode the input and generate prediction
        encoded_input = self.tokenizer.encode(prompt, return_tensors="pt").to("cpu")
        output = self.model.generate(
            encoded_input,
            do_sample=True,
            temperature=temperature,
            max_new_tokens=max_tokens,
        )

        # Decode the prediction to text
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)

        # Removing the prompt from the generated text
        prompt_length = len(self.tokenizer.encode(prompt, return_tensors="pt")[0])
        generated_response = self.tokenizer.decode(
            output[0][prompt_length:], skip_special_tokens=True
        )

        return {"response": generated_response}
