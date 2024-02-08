#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/2/7 15:26
# @Author : XXX
#
import os

from langchain.chains import create_extraction_chain
from langchain_openai import ChatOpenAI

# Schema
schema = {
    "properties": {
        "fundName": {"type": "string"},
        "fundCode": {"type": "string"},
        "netValue": {"type": "number"},
        "change": {"type": "number"},
    },
    "required": ["fundName", "fundCode"],
}

# Input
inp = "我想查找华夏成长混合基金(000001)的今日净值为1000 涨幅为0.11"
# Run chain
os.environ["OPENAI_API_KEY"] = "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"
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = create_extraction_chain(schema, llm)
print(chain.run(inp))
