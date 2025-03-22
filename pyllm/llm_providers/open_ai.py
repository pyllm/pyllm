try:
    import openai
except ImportError:
    raise Warning(
        "OpenAI is not installed. Please install it using `pip install openai`"
    )

from pyllm.configuration import Configuration


class OpenAI_Provider:
    def __init__(self,system_prompt:str=None):
        self.api_key = Configuration(configs={"OPENAI_API_KEY":"123"}).get(
            "OPENAI_API_KEY"
        )  # Todo: logics of geeting the api key here
        self.model = "gpt-4o-mini"
        openai.api_key = self.api_key
        openai.api_type = "openai"
        if system_prompt:
            self.system_prompt=system_prompt
        else:
            self.system_prompt="Your are a system, extract the event information."
        
        self.memory = [{"role": "assistant", "content": self.system_prompt}]

    def completion(self, user_input:str,response_formt=None) -> str:
        self.memory.append({"role": "user", "content": user_input})
        if response_formt:
            response = openai.chat.completions.create(
                model=self.model, messages=self.memory
            )# need to debug json format
            return response.choices[0].message.content
        else:
            response = openai.chat.completions.create(
                model=self.model, messages=self.memory
            )
            return response.choices[0].message.content
