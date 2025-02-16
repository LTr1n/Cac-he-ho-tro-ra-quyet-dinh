import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL của trang web
url = "https://codegym.vn/blog/dinh-huong-chon-nganh-nghe-phu-hop-voi-tinh-cach/"

# Gửi yêu cầu GET đến trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Phân tích cú pháp HTML    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Tìm tất cả các nhóm tính cách
    personality_groups = soup.find_all('h3')

    # Tạo một danh sách để lưu trữ kết quả
    data = []
    collecting = False

    for group in personality_groups:
        group_name = group.text.strip()

        # Bắt đầu thu thập từ nhóm "người thích sáng tạo"
        if group_name == "Nhóm người thích sáng tạo":
            collecting = True

        # Nếu đang thu thập thì giữ lại nội dung
        if collecting:
            careers = []
            next_sibling = group.find_next_sibling()
            while next_sibling and next_sibling.name != 'h3': 
                if next_sibling.name == 'p': 
                    careers.append(next_sibling.text.strip())
                next_sibling = next_sibling.find_next_sibling()

            # Thêm dữ liệu vào danh sách
            data.append({"Tính cách": group_name, "Nghề nghiệp phù hợp": ', '.join(careers)})

        # Dừng thu thập khi gặp nhóm "người thích giúp đỡ"
        if group_name == "Nhóm người thích giúp đỡ":
            careers = []
            next_sibling = group.find_next_sibling()
            while next_sibling and next_sibling.name != 'h3':
                if next_sibling.name == 'p': 
                    careers.append(next_sibling.text.strip())
                next_sibling = next_sibling.find_next_sibling()

            # Thêm dữ liệu vào danh sách
            data.append({"Tính cách": group_name, "Nghề nghiệp phù hợp": ', '.join(careers)})
            collecting = False  # Dừng thu thập sau khi thu thập xong nhóm này

    # Tạo DataFrame từ danh sách
    df = pd.DataFrame(data)

    # Lưu DataFrame vào file Excel
    df.to_excel('data.xlsx', index=False, engine='openpyxl')

    print("Dữ liệu đã được lưu vào file data.xlsx")
else:
    print("Không thể lấy dữ liệu từ trang web.")