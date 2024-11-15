import streamlit as st

# Tiêu đề cho ứng dụng
st.title("WebChat-Blockchain")

# Tabs cho các chức năng chính
tabs = ["Đăng ký/Đăng nhập", "Quản lý tài khoản", "Thiết lập bảo mật", "Kiểm soát quyền riêng tư", "Quản lý thiết bị"]
choice = st.sidebar.selectbox("Chọn chức năng", tabs)

# Đăng ký / Đăng nhập
if choice == "Đăng ký/Đăng nhập":
    st.subheader("Đăng ký/Đăng nhập")
    
    auth_choice = st.radio("Bạn đã có tài khoản chưa?", ["Đăng nhập", "Đăng ký"])
    
    if auth_choice == "Đăng ký":
        username = st.text_input("Tạo tên đăng nhập")
        password = st.text_input("Tạo mật khẩu", type="password")
        if st.button("Đăng ký"):
            st.success(f"Tài khoản {username} đã được tạo thành công!")
    
    elif auth_choice == "Đăng nhập":
        username = st.text_input("Tên đăng nhập")
        password = st.text_input("Mật khẩu", type="password")
        if st.button("Đăng nhập"):
            st.success(f"Chào mừng {username} đã đăng nhập thành công!")

# Quản lý tài khoản
elif choice == "Quản lý tài khoản":
    st.subheader("Quản lý tài khoản")
    st.text("Cập nhật thông tin cá nhân của bạn.")
    
    name = st.text_input("Tên đầy đủ")
    email = st.text_input("Email")
    phone = st.text_input("Số điện thoại")
    if st.button("Cập nhật thông tin"):
        st.success("Thông tin tài khoản đã được cập nhật thành công!")

# Thiết lập bảo mật
elif choice == "Thiết lập bảo mật":
    st.subheader("Thiết lập bảo mật")
    
    # Chọn phương thức bảo mật
    two_factor = st.checkbox("Bật xác thực hai yếu tố (2FA)")
    backup_codes = st.checkbox("Tạo mã dự phòng")
    recovery_email = st.text_input("Email phục hồi")

    if st.button("Lưu thiết lập bảo mật"):
        st.success("Thiết lập bảo mật đã được cập nhật!")

# Kiểm soát quyền riêng tư
elif choice == "Kiểm soát quyền riêng tư":
    st.subheader("Kiểm soát quyền riêng tư")
    
    show_online_status = st.checkbox("Hiển thị trạng thái online của bạn")
    allow_messages = st.checkbox("Cho phép người lạ gửi tin nhắn")
    show_last_seen = st.checkbox("Hiển thị lần cuối bạn online")
    
    if st.button("Lưu thiết lập quyền riêng tư"):
        st.success("Thiết lập quyền riêng tư đã được lưu!")

# Quản lý thiết bị
elif choice == "Quản lý thiết bị":
    st.subheader("Quản lý thiết bị")
    st.text("Kiểm tra và quản lý các thiết bị đã đăng nhập vào tài khoản của bạn.")
    
    device_list = ["Thiết bị 1 - iPhone 13", "Thiết bị 2 - MacBook Pro", "Thiết bị 3 - Windows PC"]
    for device in device_list:
        st.text(device)
        if st.button(f"Đăng xuất {device}"):
            st.success(f"Thiết bị {device} đã được đăng xuất.")

st.sidebar.info("Ứng dụng WebChat-Blockchain - Sử dụng công nghệ Blockchain để bảo mật trò chuyện.")

