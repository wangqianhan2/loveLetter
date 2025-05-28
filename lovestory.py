import streamlit as st
from PIL import Image
import random

# 页面设置
st.set_page_config(
    page_title="我的心意 | 给你的情书",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 背景样式
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to bottom right, #ffcce6, #f9ecf9);
        color: #333333;
    }
    .title {
        color: #ff66b3;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .header {
        color: #cc0066;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .poem {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: 'KaiTi', '楷体', serif;
        font-size: 18px;
        line-height: 2;
    }
    .heart {
        color: #ff0066;
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)

# 标题部分
st.markdown("<h1 class='title'>💖 给我最爱的你 💖</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='header'>请收下这封特别的情书</h2>", unsafe_allow_html=True)

# 分隔线
st.markdown("---")

# 主内容
col1, col2 = st.columns([1, 2])
with col1:
    # 可以放一张图片
    try:
        image = Image.open("le.jpg")  # 替换成你自己的图片
        st.image(image, caption="你在我心中的样子", width=200)
    except:
        st.markdown("<div style='height:200px; display:flex; align-items:center; justify-content:center;'>"
                   "<span class='heart'>❤️</span></div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='poem'>
        亲爱的，<br><br>
        
        遇见你是我生命中最美好的意外。<br>
        每一天因为有你而变得不同，<br>
        每一个瞬间因为想你而变得甜蜜。<br><br>
        
        我想告诉你...<br>
    </div>
    """, unsafe_allow_html=True)

# 经典诗句
st.markdown("""
<div class='poem'>
    <center>
    To the world you may be one person, <br>
    but to one person you may be the world.
    </center>
</div>
""", unsafe_allow_html=True)

# 徐志摩的诗
st.markdown("""
<div class='poem'>
    我是天空里的一片云，<br>
    偶尔投影在你的波心——<br>
    你不必讶异，<br>
    更无须欢喜——<br>
    在转瞬间消灭了踪影。<br>
    <div style='text-align:right;'>—— Chen恒充《偶然》</div>
</div>
""", unsafe_allow_html=True)

# 互动元素
st.markdown("---")
st.subheader("我们的专属回忆")

# 日期选择器
special_date = st.date_input("选择一个我们特别的日子")
if special_date:
    st.success(f"我会永远记得 {special_date.strftime('%Y年%m月%d日')} 这一天！")

# 滑动选择器
love_level = st.slider("我对你的爱有几分？", 0, 100, 100)
st.write(f"我对你的爱是 {love_level} 分，但我的心告诉我这还不够！")

# 按钮效果
if st.button("点击收获惊喜", key="surprise"):
    hearts = " ".join(["❤️"] * random.randint(10, 20))
    st.balloons()
    st.markdown(f"<center><h2>{hearts}</h2></center>", unsafe_allow_html=True)
    st.markdown("<center><h3>你是我每天醒来的理由</h3></center>", unsafe_allow_html=True)

# 页脚
st.markdown("---")
st.markdown("<center><small>❤️ 用心制作 · 只为你 ❤️</small></center>", unsafe_allow_html=True)