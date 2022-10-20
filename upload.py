import streamlit as st
import os

# 先同download_button ，自行生成一个二进制文件
binary_contents = b'a bin file , hehe  da \n I\'m a new line'
# Defaults to 'application/octet-stream'
st.download_button('下载为bin文件', binary_contents)

# 再上传这个二进制文件
uploaded_file = st.file_uploader("请选择一个二进制文件：")
if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type}
    st.write(file_details)
    with open(os.path.join("tempDir",uploaded_file.name),"wb") as f:
      f.write(uploaded_file.getbuffer())
    st.success("Saved File")