#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/2/7 9:39
# @Author : XXX
#
import os

from langchain.chains.openai_functions.openapi import get_openapi_chain
from langchain_openai import ChatOpenAI
from langchain_wenxin import Wenxin, ChatWenxin

os.environ["BAIDU_API_KEY"] = "T5h233wgC6dIGB5OQGtye2pr"
os.environ["BAIDU_SECRET_KEY"] = "dAtiyOc54j1Ux7BKauMfUavDRuGRnofQ"
# llm = ChatWenxin(model="ernie-bot-turbo")
os.environ["OPENAI_API_KEY"] = "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"
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
spec = """
{
    "openapi":"3.1.0",
    "info":{
        "title":"demo",
        "description":"",
        "version":"1.0.0"
    },
    "tags":[

    ],
    "paths":{
        "/user/{name}":{
            "get":{
                "summary":"Query user ID by user name",
                "deprecated":false,
                "description":"",
                "tags":[

                ],
                "parameters":[
                    {
                        "name":"name",
                        "in":"path",
                        "description":"user name",
                        "required":true,
                        "schema":{
                            "type":"number"
                        }
                    }
                ],
                "responses":{
                    "200":{
                        "description":"成功",
                        "content":{
                            "application/json":{
                                "schema":{
                                    "type":"object",
                                    "properties":{
                                        "id":{
                                            "type":"string",
                                            "description":"user id"
                                        }
                                    },
                                    "required":[
                                        "id"
                                    ]
                                }
                            }
                        }
                    }
                },
                "security":[

                ]
            }
        },
        "/age":{
            "get":{
                "summary":"Query user age by user ID",
                "deprecated":false,
                "description":"",
                "tags":[

                ],
                "parameters":[
                    {
                        "name":"id",
                        "in":"query",
                        "description":"",
                        "required":false,
                        "schema":{
                            "type":"number"
                        }
                    }
                ],
                "responses":{
                    "200":{
                        "description":"成功",
                        "content":{
                            "application/json":{
                                "schema":{
                                    "type":"object",
                                    "properties":{
                                        "age":{
                                            "type":"number",
                                            "description":"user age"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "security":[

                ]
            }
        }
    },
    "components":{
        "schemas":{

        },
        "securitySchemes":{

        }
    },
    "servers":[
        {"url": "http://127.0.0.1:2020"}
    ]
}
"""
chain = get_openapi_chain(
    spec=spec,
    llm=llm,
    verbose=True
)
print(chain.run("Query the age of xy"))
