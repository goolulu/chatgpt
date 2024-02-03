from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI

from config import http_client, llm

examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
]

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)
print(few_shot_prompt.format())


final_prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a wondrous wizard of math.'),
        few_shot_prompt,
        ('human', '{input}')
    ]
)

print(final_prompt.format(input="What's the square of a triangle?"))

chain = final_prompt | llm
#
print(chain.invoke({"input": "What's the square of a triangle?"}))


