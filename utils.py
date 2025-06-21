import os
from prompt_template import system_template_text,user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from xiaohongshu_model import Xiaohongshu



def generate_xiaohongshu(theme,deepseek_api_key):
    # 构建提示模板
    prompt =ChatPromptTemplate.from_messages([
        ("system",system_template_text),
        ("user",user_template_text)
    ])
    # 配置DeepSeek模型
    model = ChatOpenAI(
        openai_api_key=deepseek_api_key,
        openai_api_base="https://api.deepseek.com",  # DeepSeek专用API端点
        model="deepseek-chat",  # 或使用"deepseek-reasoner"（推理专用模型）
    )
    # model = ChatOpenAI(model ="gpt-3.5-turbo",api_key=openai_api_key)
    # 定义输出解析器
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    # 构建链式流程
    chain = prompt | model | output_parser
    # 调用并返回结果
    result = chain.invoke({
        "parser_instructions":output_parser.get_format_instructions(),
        "theme":theme
    })
    return result

# print(generate_xiaohongshu("公共营养师",os.getenv("DeepSeek API Key")))