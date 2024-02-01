## 框架基础概念篇

### Models

LLMS

Chat Models

### Messages

Messages是ChatModels输入输出的对象,包含了角色(role) 内容(content)

### Prompts

#### PromptValue

#### PromptTemplate

#### MessagePromptTemplate

#### MessagesPlaceholder

#### ChatPromptTemplate

### Output Parsers

#### StrOutputParser

#### OpenAI Functions Parsers

#### Agent Output Parsers


## Prompt 篇

### 概念
LangChain 提供PromptTemplate来处理prompt engineering

PromptTemplate 包含会话背景，少量提示用例(few-shot examples) 特定上下文(specific context) 指定任务(questions appropriate for a given task.)

### 工具使用

**from_template**

将模板字符串解析成PromptTemplate

```python

from langchain.prompts import PromptTemplate

# 底层默认使用python模板字符串方法,可以通过参数template_format替换,
# 所以可以在format方法使用var_name=var_value
prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)
prompt_template.format(adjective="funny", content="chickens")


```

**from_message**

将Message列表（元组）解析成ChatPromptTemplate

由于使用ChatMode,ChatMode模型相比普通Mode更重要的能力来自于上下文,以及few-shot,所以可以指定角色

如果没有指定角色，默认为human

特点:是只有ChatMode才能使用



```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
    ]
)

messages = chat_template.format_messages(name="Bob", user_input="What is your name?")
```

**format** **format_prompt** **format_message**

这些方法接收参数格式化输出不同的对象类型

format格式化成字符串

format_prompt 输出PromptValue

format_message输出Message

```python
from langchain_core.prompts import ChatPromptTemplate
chat_template = ChatPromptTemplate()
print(chat_template.format(input='获取天气'))
print(chat_template.format_prompt(input='获取天气'))
print(chat_template.format_messages(input='获取天气'))

```

## Chains篇

基础公式： chain = prompt | model | output_parser

