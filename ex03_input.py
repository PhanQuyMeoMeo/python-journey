"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"

ten=input("nhap ten cua ban:")
print("Xin chao",ten)


# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
nam_sinh= int(input("Nhap nam sinh cua ban:"))
tinh_tuoi=2026-nam_sinh
print("nam nay ban", tinh_tuoi ,"tuoi" )


# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42

so1=int(input("nhap so thu 1"))
so2=int(input("nhap so thu 2"))
print("tong=",so1+so2)



# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui

