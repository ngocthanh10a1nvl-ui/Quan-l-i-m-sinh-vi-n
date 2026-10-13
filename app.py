import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
data = {
    "họ và tên": [
        "Nguyễn Văn A", "Nguyễn Văn B", "Nguyễn Văn C",
        "Nguyễn Văn D", "Nguyễn Văn E", "Nguyễn Văn F",
        "Nguyễn Văn G", "Nguyễn Văn K", "Nguyễn Văn N",
        "Nguyễn Văn M"
    ],
    "điểm chuyên cần": [7, 8, 9, 9, 7, 6, 8, 9, 6, 5],
    "điểm giữa kỳ": [8, 6, 8, 5, 6, 9, 10, 6, 8, 9],
    "điểm cuối kỳ": [8, 9, 6, 8, 6, 9, 7, 5, 5, 9]
}
Bang_diem = pd.DataFrame(data)
Bang_diem["tổng kết"] = (
    0.2 * Bang_diem["điểm chuyên cần"]
    + 0.3 * Bang_diem["điểm giữa kỳ"]
    + 0.5 * Bang_diem["điểm cuối kỳ"]
)
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"
Bang_diem["xếp loại"] = Bang_diem["tổng kết"].apply(xep_loai)
st.subheader("1. Bảng điểm sinh viên")
st.dataframe(Bang_diem, use_container_width=True)
st.subheader("2. Thống kê kết quả")
st.write("Điểm trung bình:", round(Bang_diem["tổng kết"].mean(), 2))
st.write("Điểm cao nhất:", Bang_diem["tổng kết"].max())
st.write("Điểm thấp nhất:", Bang_diem["tổng kết"].min())
so_sinh_vien_dat = (Bang_diem["tổng kết"] >= 5).sum()
st.write("Số sinh viên đạt:", so_sinh_vien_dat)
st.subheader("3. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(Bang_diem["họ và tên"], Bang_diem["tổng kết"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
