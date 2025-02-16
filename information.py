import pandas as pd

# Dữ liệu tổng hợp
data = {
    "Nhóm người": [
        "Nhóm người thích sáng tạo",
        "Nhóm người thích sáng tạo",
        "Nhóm người thích sáng tạo",
        "Nhóm người thích sáng tạo",
        "Nhóm người thích sáng tạo",
        "Nhóm người thích suy nghĩ",
        "Nhóm người thích suy nghĩ",
        "Nhóm người thích suy nghĩ",
        "Nhóm người thích suy nghĩ",
        "Nhóm người thích suy nghĩ",
        "Nhóm người thích tổ chức",
        "Nhóm người thích tổ chức",
        "Nhóm người thích tổ chức",
        "Nhóm người thích tổ chức",
        "Nhóm người thích tổ chức",
        "Nhóm người thích hành động",
        "Nhóm người thích hành động",
        "Nhóm người thích hành động",
        "Nhóm người thích hành động",
        "Nhóm người thích hành động",
        "Nhóm người thích đàm phán",
        "Nhóm người thích đàm phán",
        "Nhóm người thích đàm phán",
        "Nhóm người thích đàm phán",
        "Nhóm người thích đàm phán",
        "Nhóm người thích giúp đỡ",
        "Nhóm người thích giúp đỡ",
        "Nhóm người thích giúp đỡ",
        "Nhóm người thích giúp đỡ",
        "Nhóm người thích giúp đỡ",
    ],
    "Tính cách": [
        "Tò mò", "Mở lòng", "Độc lập", "Sáng tạo", "Chấp nhận rủi ro",
        "Tư duy phản biện", "Sâu sắc", "Phân tích", "Nhạy bén", "Độc lập",
        "Chi tiết", "Có tổ chức", "Quyết đoán", "Lãnh đạo", "Có kế hoạch",
        "Năng động", "Thích phiêu lưu", "Quyết đoán", "Tích cực", "Thích thử thách",
        "Khéo léo", "Thuyết phục", "Nhạy bén", "Giao tiếp tốt", "Linh hoạt",
        "Nhân ái", "Cảm thông", "Kiên nhẫn", "Hòa đồng", "Tích cực"
    ],
    "Sở thích": [
        "Nghệ thuật", "Âm nhạc", "Viết lách", "Thử nghiệm", "Du lịch",
        "Đọc sách", "Nghiên cứu", "Thảo luận", "Giải quyết vấn đề", "Tham gia hội thảo",
        "Lên kế hoạch sự kiện", "Quản lý dự án", "Tổ chức cộng đồng", "Điều phối hoạt động", "Giao tiếp hiệu quả",
        "Thể thao", "Du lịch mạo hiểm", "Tham gia hoạt động ngoài trời", "Thực hiện các dự án thực tế", "Tham gia các hoạt động nhóm",
        "Tham gia các cuộc thảo luận", "Đàm phán hợp đồng", "Tham gia vào các hoạt động thương mại", "Giải quyết xung đột", "Thuyết trình",
        "Tình nguyện", "Giúp đỡ người khác", "Tham gia các hoạt động cộng đồng", "Hỗ trợ giáo dục", "Tham gia các tổ chức từ thiện"
    ]
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Xuất dữ liệu ra file Excel
file_name = "information.xlsx"
df.to_excel(file_name, index=False)

print(f"Dữ liệu đã được xuất vào file {file_name}")