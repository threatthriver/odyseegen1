import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class OdyseeModel:
    def __init__(self, model_name="gpt2"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)

    @classmethod
    def load(cls, version="base"):
        model_map = {
            "base": "gpt2",
            "medium": "gpt2-medium",
            "large": "gpt2-large"
        }
        return cls(model_map.get(version, "gpt2"))

    def generate(self, prompt, max_length=100):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            **inputs,
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.7
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
