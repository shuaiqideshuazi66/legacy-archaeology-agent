from openai import OpenAI
from config import OPENAI_API_KEY, MODEL, MAX_CODE_CHARS

client = OpenAI(api_key=OPENAI_API_KEY)

class ArchaeologyAgent:
    def analyze(self, file_path, code, commits):
        prompt = f"""你是一个遗留系统考古 Agent，请基于以下信息进行分析。

【文件路径】
{file_path}

【代码】
{code[:MAX_CODE_CHARS]}

【最近 Git 提交】
{commits}

请严格按以下格式输出：
1. 模块用途：
2. 活跃度判断（活跃 / 边缘 / 废弃）：
3. 是否可删除（是 / 否 / 需进一步验证）：
4. 删除风险（低 / 中 / 高）：
5. 建议：
"""

        resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return resp.choices[0].message.content
