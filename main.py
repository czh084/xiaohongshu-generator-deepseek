import streamlit as st

from utils import generate_xiaohongshu

st.header("HP爆款小红书AI写作助手")
with st.sidebar:
    DeepSeek_API_Key = st.text_input("请输入DeepSeek API密钥：",type="password")
    st.markdown("[获取DeepSeek API密钥](https://platform.deepseek.com/api_keys)")

theme =st.text_input("主题")
submit = st.button("开始写作")

# 新增API密钥格式验证
def is_valid_deepseek_key(api_key):
    """验证DeepSeek API密钥格式"""
    # DeepSeek API密钥通常以"sk-"开头，长度为35个字符
    return api_key.startswith("sk-") and len(api_key) == 35
if submit:
    # 检查API密钥是否存在且格式正确
    if not DeepSeek_API_Key:
        st.error("❌ 请输入你的DeepSeek API密钥")
        st.stop()
    elif not is_valid_deepseek_key(DeepSeek_API_Key.strip()):
        st.error("❌ 无效的API密钥格式！请确保输入的是DeepSeek API密钥（以'sk-'开头，共35个字符）")
        st.stop()

if submit and not theme:
    st.info("请输入生成内容的主题")
    st.stop()

if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result = generate_xiaohongshu(theme,DeepSeek_API_Key)

    st.divider()
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown("##### 小红书标题1")
        st.write(result.titles[0])
        st.markdown("##### 小红书标题2")
        st.write(result.titles[1])
        st.markdown("##### 小红书标题3")
        st.write(result.titles[2])
        st.markdown("##### 小红书标题4")
        st.write(result.titles[3])
        st.markdown("##### 小红书标题5")
        st.write(result.titles[4])
    with right_column:
        st.markdown("##### 小红书正文")
        st.write(result.content)