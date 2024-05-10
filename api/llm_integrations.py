from langchain_community.chat_models import (
    ChatOpenAI,
    # can add other models here
)
from langchain_mistralai.chat_models import ChatMistralAI
import os


LLM_TYPE = os.getenv("LLM_TYPE", "openai")


def init_openai_chat(temperature):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "openai")
    return ChatOpenAI(
        openai_api_key=OPENAI_API_KEY, streaming=True, temperature=temperature
    )


MAP_LLM_TYPE_TO_CHAT_MODEL = {
    "openai": init_openai_chat,
}


def get_llm(temperature=0):
    if not LLM_TYPE in MAP_LLM_TYPE_TO_CHAT_MODEL:
        raise Exception(
            "LLM type not found. Please set LLM_TYPE to one of: "
            + ", ".join(MAP_LLM_TYPE_TO_CHAT_MODEL.keys())
            + "."
        )

    return MAP_LLM_TYPE_TO_CHAT_MODEL[LLM_TYPE](temperature=temperature)