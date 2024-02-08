import os

from langchain.chains import APIChain
from langchain.chains.api import open_meteo_docs
from langchain_openai import OpenAI


os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=0)
chain = APIChain.from_llm_and_api_docs(
    llm,
    open_meteo_docs.OPEN_METEO_DOCS,
    verbose=True,
    limit_to_domains=["https://api.open-meteo.com/"],
)
chain.run(
    "What is the weather like right now in Munich, Germany in degrees Fahrenheit?"
)
