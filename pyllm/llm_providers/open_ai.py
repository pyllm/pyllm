import os

from openai import OpenAI

from pyllm.llm_providers.default_models import DefaultModel
from pyllm.llm_providers.llm_abstract import PyLLMAbstract
class OpenAIProvidor(PyLLMAbstract):

    def __init__(self, configs: dict = None):
        super().__init__(configs)

        self.__client: OpenAI = OpenAI(api_key=self.openai_api_key)

    def generate_system_promt(self, system_prompt: str):
        # TODO: implement 6-steps system prompt
        return system_prompt

    def generate_code_python(self, prompt: str):
        response = self.__client.chat.completions.create(
            model=self.openai_model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()

    def text_completion(self, system: str, prompt: str, output: object = DefaultModel):
        response = self.__client.beta.chat.completions.parse(
            model=self.openai_model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            response_format=output,
        )
        return response.choices[0].message.content.strip()
