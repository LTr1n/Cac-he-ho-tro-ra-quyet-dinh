from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Đọc dữ liệu từ file Excel
df = pd.read_excel('data.xlsx')

# Mã hóa cột "Tính cách" và "Sở thích"
le_traits = LabelEncoder() # dùng để chuyển các giá trị phân loại 
le_interests = LabelEncoder()
df['Tính cách_encoded'] = le_traits.fit_transform(df['Tính cách']) # học các nhãn dán từ cột và chuyển đổi thành số nguyên
df['Sở thích_encoded'] = le_interests.fit_transform(df['Sở thích'])

# Mã hóa cột "People"
le_groups = LabelEncoder()
df['People_encoded'] = le_groups.fit_transform(df['People'])

# Huấn luyện mô hình KNN
X = df[['Tính cách_encoded', 'Sở thích_encoded']]
y = df['People_encoded']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=1) # Tạo mô hình với 1 láng giềng gần nhất
knn.fit(X, y) # dữ liệu đầu vào 
y_pred = knn.predict(X_test)
    
# Tính độ chính xác
accuracy = accuracy_score(y_test, y_pred)
print(f"Độ chính xác của mô hình KNN: {accuracy * 100:.2f}%")

def predict_group_and_suggest_careers(trait, interest):
    try:
        # Mã hóa tính cách và sở thích của người dùng
        trait_encoded = le_traits.transform([trait])[0]
        interest_encoded = le_interests.transform([interest])[0]
        
        # Dự đoán nhóm người
        prediction = knn.predict([[trait_encoded, interest_encoded]])[0]
        
        # Lấy tên nhóm người từ mã hóa
        group = le_groups.inverse_transform([prediction])[0]
        
        # Tìm các nghề nghiệp phù hợp với nhóm
        suggested_careers = df.loc[df['People'] == group, 'Nghề nghiệp phù hợp'].tolist()
        
        return group, suggested_careers
    except Exception as e:
        print("Có lỗi xảy ra:", e)
        return None, []
