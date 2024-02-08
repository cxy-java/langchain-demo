#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/1/24 9:08
# @Author : XXX
# @Site :
# @File : Chatbots.py
# @Software: PyCharm
import os

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "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"
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2, verbose=True)
response = chat.invoke(
    [
        HumanMessage(
            content="你在吗？"
        )
    ]
)

print(response)
response = chat.invoke(
    [
        HumanMessage(
            content="你是谁？能给我背首唐诗吗"
        )
    ]
)

print(response)
