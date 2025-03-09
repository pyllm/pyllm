from pydantic import BaseModel
from pyllm.llm_providers.open_ai import OpenAI_Provider




class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


def extract_event_information(description: str) -> CalendarEvent:
    client = OpenAI_Provider("Extract the event information.")
    completion=client.completion(description,CalendarEvent)
    return completion


extract_event_information("Alice and Bob are going to a science fair on Friday.")


class EventExtractor:
    def __init__(self, model: str = "gpt-4o-2024-08-06"):
        super().__init__()

    # def pseudocode(description: str) -> CalendarEvent:
    #     context = ""
    #     task = [
    #         "Extract the event information"
    #     ]
    #     # format
    #     # example
    #     # persona
    #     # tone
    #     return context, instructions

    def context():
        return ""

    def task():
        return ["Extract the event information", "if missing, dont guess, leave empty"]

    def tone():
        return "formal"

    def preview_prompt():
        return ""


extractor = EventExtractor()
extractor(description="Alice and Bob are going to a science fair on Friday.")
