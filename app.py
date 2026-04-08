# app.py
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"], base_url="https://api.deepseek.com")

st.set_page_config(page_title="MEA积极认知助手", page_icon="🐘", layout="wide")

# 标题
st.title("🐘 MEA积极认知助手")
st.markdown("---")

# 输入框
input_txt = st.text_area("📝 请输入您所经历的事件", height=180)

# 按钮
col1, col2 = st.columns([1, 1])
with col1:
    analyze = st.button("✨ 开始MEA分析", type="primary", use_container_width=True)
with col2:
    clear = st.button("🧹 清空内容", use_container_width=True)

st.markdown("---")
st.subheader("☀ 积极认知转化结果")

# 清空逻辑
if clear:
    input_txt = ""
    st.rerun()

# 分析逻辑
if analyze:
    if not input_txt.strip():
        st.warning("请输入您经历的事件")
    else:
        prompt = f"""
【E：表面事件/语言】
{input_txt}

【M：当下情绪反应】

【A：非理性核心信念】

【理性认知重构】

【积极自我对话】
"""
        try:
            with st.spinner("⏳ AI 正在认真分析..."):
                client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                reply = response.choices[0].message.content
                st.code(reply, language="markdown")

        except Exception as e:
            st.error(f"AI调用失败：{str(e)}")
