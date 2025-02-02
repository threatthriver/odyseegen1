import pytest
from odysee import OdyseeModel

def test_model_loading():
    model = OdyseeModel.load("base")
    assert model is not None

def test_text_generation():
    model = OdyseeModel.load("base")
    prompt = "Hello, world"
    response = model.generate(prompt)
    assert isinstance(response, str)
    assert len(response) > len(prompt)
