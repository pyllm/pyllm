from abc import abstractmethod

from pyllm.configuration import Configuration
from pyllm.llm_providers.default_models import DefaultModel


class PyLLMAbstract(Configuration):

    def __init__(self, configs: dict = None):
        super().__init__(configs)

        # OpenAI configurations
        self.openai_api_key = self.get("OPENAI_API_KEY")
        self.openai_model = DefaultModel
        
        # Claude configurations
        self.claude_api_key = self.get("CLAUDE_API_KEY")
        self.claude_model = DefaultModel

    @abstractmethod
    def text_completion(self, system: str, prompt: str, output: object = DefaultModel):
        pass
