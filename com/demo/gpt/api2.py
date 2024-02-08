#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/2/6 9:03
# @Author : XXX
#
import os

from langchain.chains import APIChain, LLMRequestsChain, LLMChain
from langchain.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_wenxin import Wenxin

os.environ["OPENAI_API_KEY"] = "sk-CQRqoJS3mkyEYULXody7k8mrvRlWAvcF1fCCfgXA4bb05X9V"
os.environ["BAIDU_API_KEY"] = "T5h233wgC6dIGB5OQGtye2pr"
os.environ["BAIDU_SECRET_KEY"] = "dAtiyOc54j1Ux7BKauMfUavDRuGRnofQ"
llm = Wenxin(model="ernie-bot-turbo")

template = """Between >>> and <<< are the raw search result text from google.
Extract the answer to the question '{query}' or say "not found" if the information is not contained.
Use the format
Extracted:<answer or "not found">
>>> {requests_result} <<<
Extracted:"""

PROMPT = PromptTemplate(
    input_variables=["query", "requests_result"],
    template=template,
)

chain = LLMRequestsChain(llm_chain=LLMChain(llm=llm, prompt=PROMPT))
question = "诸葛亮"
inputs = {
    "query": question,
    "url": "https://www.google.com/search?q=" + question.replace(" ", "+"),
}

print(chain(inputs))
