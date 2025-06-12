import streamlit as st
import pandas as pd
import random
st.set_page_config(page_title="南宁天堂", page_icon="♣️")

# 原始餐厅数据
data = pd.DataFrame({
    "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
    "评分": [4.2, 4.5, 4.8, 4.7, 4.3],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
    "人均消费(元)": [15, 20, 25, 35, 55],
    "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
    "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
})
restaurant_details = {
    "复记老友粉": {
        "crowd": 80,
        "dishes": ["老友牛肉", "老友猪肉", "炒粉"],
        "image": "https://example.com/laoyoufen.jpg"  # 替换为实际图片URL
    },
    "星艺会尝不忘": {
        "crowd": 60,
        "dishes": ["招牌螺蛳粉", "卤鸭脚", "卤蛋"],
        "image": "https://example.com/xingyihui.jpg"  # 替换为实际图片URL
    },
    "高峰柠檬鸭": {
        "crowd": 70,
        "dishes": ["柠檬鸭", "酸笋炒肉", "白切鸡"],
        "image": "https://example.com/lemonduck.jpg"  # 替换为实际图片URL
    },
    "好友缘": {
        "crowd": 50,
        "dishes": ["海鲜自助", "烤肉", "甜品"],
        "image": "https://example.com/haoyouyuan.jpg"  # 替换为实际图片URL
    },
    "西冷牛排店": {
        "crowd": 65,
        "dishes": ["西冷牛排", "罗宋汤", "沙拉"],
        "image": "https://example.com/xileng.jpg"  # 替换为实际图片URL
    }
}

# 添加序号索引
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3, 4, 5], name='序号')
df.index = index

st.header("🍔 南宁天堂")    
st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")

st.subheader("🍔 南宁天堂")  
st.map(pd.DataFrame(data))

st.subheader("⭐ 餐厅评分")  
st.bar_chart(df, x="餐厅", y="评分")

st.subheader("💰 不同类型餐厅价格")

# 餐厅价格数据
price_data = pd.DataFrame({
    "餐厅类型": ["中餐", "快餐", "自助餐", "西餐"],
    "好友缘": [12, 8.2, 6.0, 5.5],
    "高峰柠檬鸭": [6.8, 9.0, 7.5, 11.2],
    "星艺会尝不忘": [5.5, 7.0, 9.0, 7.0],
    "复记老友粉": [8.0, 9.5, 13.0, 11.8],
    "西冷牛排店": [9.0, 12.5, 5.0, 13.0]
})

# 显示价格折线图
st.line_chart(
    price_data.set_index("餐厅类型"),
    height=400,
    use_container_width=True
)

# 用餐高峰数据
peak_data = pd.DataFrame({
    "时间": ["12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", 
           "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00"],
    "复记老友粉": [40, 70, 80, 65, 50, 40, 35, 30, 25, 20, 30, 45, 60, 55, 50, 40, 30],
    "星艺会尝不忘": [30, 50, 60, 55, 45, 35, 30, 25, 20, 15, 25, 40, 55, 50, 45, 35, 25],
    "高峰柠檬鸭": [25, 35, 45, 55, 45, 40, 40, 45, 40, 35, 45, 65, 85, 80, 70, 55, 45],
    "好友缘": [12, 15, 8.2, 10, 6.0, 8, 5.5, 7, 6, 8, 10, 15, 20, 18, 15, 12, 10],  
    "西冷牛排店": [9.0, 12, 12.5, 10, 5.0, 8, 13.0, 10, 8, 10, 12, 15, 18, 15, 12, 10, 8]
})

# 显示高峰时段折线图（使用正确的变量名peak_hours_data）
st.area_chart(
    peak_data.set_index("时间"),
    height=400,
    use_container_width=True,
   
)
st.subheader("📈 年度价格走势（2025）")

# 定义12个月价格数据（单位：元）
monthly_price = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
    "复记老友粉": [25, 40, 18, 35, 15, 28, 16, 38, 22, 42, 20, 32],
    "好友缘": [45, 30, 50, 28, 45, 22, 48, 26, 40, 50, 25, 42],
    "星艺会尝不忘": [10, 30, 8, 28, 5, 25, 7, 32, 10, 35, 5, 28],
    "高峰柠檬鸭": [35, 15, 38, 12, 35, 10, 32, 15, 38, 18, 35, 20],
    "西冷牛排店": [70, 40, 75, 35, 68, 38, 72, 40, 75, 45, 70, 50]
})

# 绘制折线图（保持颜色一致）
st.line_chart(
    monthly_price.set_index("月份"),
    height=400,
    use_container_width=True,
    
)

# ===== 侧边栏 - 餐厅选择和随机推荐 =====
st.sidebar.title("🍽️ 南宁天堂")
selected_restaurant = st.sidebar.selectbox(
    "选择餐厅查看详情",
    data["餐厅"].tolist()
)

if st.sidebar.button("🎲 帮我选午餐", type="primary"):
    selected_restaurant = random.choice(data["餐厅"].tolist())
    st.sidebar.success(f"为您推荐: {selected_restaurant}")

# ===== 主页面布局 =====
col1, col2 = st.columns([3, 1])

with col1:
    # 餐厅详情部分
    st.title("🍽️ 餐厅详情")
    st.markdown("选择餐厅查看详情")
    
    # 获取餐厅详情
    restaurant_info = data[data["餐厅"] == selected_restaurant].iloc[0]
    details = restaurant_details.get(selected_restaurant, {})
    
    # 显示餐厅基本信息
    st.header(f"## {selected_restaurant}")
    
    info_col1, info_col2 = st.columns(2)
    with info_col1:
        st.metric("评分", f"{restaurant_info['评分']}/5.0")
    with info_col2:
        st.metric("人均消费", f"{restaurant_info['人均消费(元)']}元")
    
    # 推荐菜品
    st.subheader("推荐菜品")
    if details.get("dishes"):
        for dish in details["dishes"]:
            st.markdown(f"- {dish}")
    
    # 拥挤程度
    st.subheader("当前拥挤程度")
    if "crowd" in details:
        crowd = details["crowd"]
        st.progress(crowd/100, text=f"{crowd}% 拥挤")
    
    # 随机午餐推荐区域
    st.divider()
    st.subheader("今日午餐推荐")
    if st.button("🍚 帮我选午餐", use_container_width=True, type="primary"):
        recommended = random.choice(data["餐厅"].tolist())
        st.success(f"今日推荐: {recommended}({data[data['餐厅'] == recommended].iloc[0]['类型']})")
        if restaurant_details.get(recommended) and restaurant_details[recommended].get("image"):
            st.image(restaurant_details[recommended]["image"], width=300)
        st.write("美味午餐等着你!")

