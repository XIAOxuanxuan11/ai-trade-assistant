# AI外贸文档助手 - 翻译示例
import openai

def translate_tech_doc(text):
    """
    翻译工业技术文档，保留专业术语和关键参数
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是专业的工业技术翻译，擅长铸锻、冲压领域，翻译要准确、简洁，保留关键参数。"},
            {"role": "user", "content": f"翻译这段技术文档：{text}"}
        ]
    )
    return response.choices[0].message['content']

# 示例调用
if __name__ == "__main__":
    tech_text = "This forging is made from 42CrMo4 steel, with a hardness of 280-320 HB, and meets ISO 9001 quality standards."
    result = translate_tech_doc(tech_text)
    print(result)
