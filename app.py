import pandas as pd
import matplotlib.pyplot as plt
import streamlit as sti
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Bảng điểm, thống kê và xếp loại sinh viên")
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
st.dataframe(
    Bang_diem,
    use_container_width=True,
    hide_index=True
)
st.subheader("2. Thống kê kết quả học tập")
diem_trung_binh = Bang_diem["tổng kết"].mean()
diem_cao_nhat = Bang_diem["tổng kết"].max()
diem_thap_nhat = Bang_diem["tổng kết"].min()
so_sinh_vien_dat = (Bang_diem["tổng kết"] >= 5).sum()
cot1, cot2, cot3, cot4 = st.columns(4)
cot1.metric("Điểm trung bình", f"{diem_trung_binh:.2f}")
cot2.metric("Điểm cao nhất", f"{diem_cao_nhat:.2f}")
cot3.metric("Điểm thấp nhất", f"{diem_thap_nhat:.2f}")
cot4.metric("Số sinh viên đạt", int(so_sinh_vien_dat))
col_top, col_bot = st.columns(2)
with col_top:
    st.write("**Sinh viên có điểm cao nhất:**")
    sv_max = Bang_diem.loc[
        Bang_diem["tổng kết"] == diem_cao_nhat, 
        ["họ và tên", "tổng kết"]
    ]
    st.dataframe(sv_max, hide_index=True, use_container_width=True)
with col_bot:
    st.write("**Sinh viên có điểm thấp nhất:**")
    sv_min = Bang_diem.loc[
        Bang_diem["tổng kết"] == diem_thap_nhat, 
        ["họ và tên", "tổng kết"]
    ]
    st.dataframe(sv_min, hide_index=True, use_container_width=True)
st.subheader("3. Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(
    Bang_diem["họ và tên"],
    Bang_diem["tổng kết"],
    color="skyblue",
    edgecolor="black"
)
ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10.5)
for i, diem in enumerate(Bang_diem["tổng kết"]):
    ax.text(
        i,
        diem + 0.15,
        f"{diem:.1f}",
        ha="center",
        fontsize=9
    )
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
st.pyplot(fig, use_container_width=True)
plt.close(fig)
st.divider()
st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 12px;">
        Thực hiện bởi: Tống Nguyễn Ngọc Thành &nbsp;|&nbsp; MSSV: 054208005728
    </div>
    """,
    unsafe_allow_html=True
)
