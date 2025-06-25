import pickle

# 读取 pkl 文件
with open('df_1M_Tg.pkl', 'rb') as f:  # 注意必须是二进制读取模式
    data = pickle.load(f)

# 查看数据类型
print(type(data))  # 确定是列表/字典/DataFrame/自定义对象等

# 查看内容
if isinstance(data, dict):
    print("字典键值:", data.keys())  # 查看所有键
    print("示例值:", list(data.items())[:2])  # 查看前2个键值对
    
elif isinstance(data, list):
    print("列表长度:", len(data))
    print("首元素:", data[0])  # 查看第一个元素
    
elif hasattr(data, 'shape'):  # 处理 NumPy/pandas 对象
    print("数据形状:", data.shape)
    print("前5行:\n", data[:30])
    
else:
    print("对象内容:", data)  # 直接打印