danh_sach_tai_khoan = {"admin": "123456"}
tai_khoan_hien_tai = ""

while True:
    if not tai_khoan_hien_tai:
        print("\n--- MINI SOCIAL ---")
        print("1. Đăng nhập")
        print("2. Đăng ký")
        print("3. Thoát")
        lua_chon = input("Chọn chức năng (1-3): ").strip()

        if lua_chon == "1":
            tk = input("Tên đăng nhập: ").strip()
            mk = input("Mật khẩu: ").strip()

            if not tk or not mk:
                print("Vui lòng nhập đầy đủ thông tin!")
            elif tk not in danh_sach_tai_khoan:
                print("Tài khoản không tồn tại!")
            elif danh_sach_tai_khoan[tk] != mk:
                print("Mật khẩu không đúng!")
            else:
                tai_khoan_hien_tai = tk
                print(f"Đăng nhập thành công! Xin chào, {tai_khoan_hien_tai}!")

        elif lua_chon == "2":
            tk = input("Tên đăng nhập mới: ").strip()
            mk = input("Mật khẩu: ").strip()
            nmk = input("Nhập lại mật khẩu: ").strip()

            if not tk or not mk:
                print("Vui lòng nhập đầy đủ thông tin!")
            elif tk in danh_sach_tai_khoan:
                print("Tên đăng nhập đã tồn tại!")
            elif len(tk) < 3:
                print("Tên đăng nhập phải từ 3 ký tự trở lên!")
            elif len(mk) < 4:
                print("Mật khẩu phải từ 4 ký tự trở lên!")
            elif mk != nmk:
                print("Mật khẩu nhập lại không khớp!")
            else:
                danh_sach_tai_khoan[tk] = mk
                print("Đăng ký thành công! Bạn có thể đăng nhập ngay bây giờ.")

        elif lua_chon == "3":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

    else:
        print(f"\n--- TRANG CHỦ (Xin chào, {tai_khoan_hien_tai}) ---")
        print("1. Đăng xuất")
        print("2. Thoát chương trình")
        lua_chon = input("Chọn chức năng (1-2): ").strip()

        if lua_chon == "1":
            print(f"Tài khoản {tai_khoan_hien_tai} đã đăng xuất.")
            tai_khoan_hien_tai = ""
        elif lua_chon == "2":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ!")