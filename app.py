from flask import Flask, render_template, request
import pandas as pd
from KNN import le_traits, le_interests, le_groups, knn

app = Flask(__name__)

# Tải dữ liệu Excel để cung cấp tùy chọn cho biểu mẫu
data = pd.read_excel('data.xlsx')
traits_options = data['Tính cách'].unique()
interests_options = data['Sở thích'].unique()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Nhận đầu vào từ người dùng
        user_trait = request.form.get("trait")
        user_interest = request.form.get("interest")

        # Mã hóa đầu vào
        trait_encoded = le_traits.transform([user_trait])[0]
        interest_encoded = le_interests.transform([user_interest])[0]

        # Dự đoán nhóm
        group_encoded = knn.predict([[trait_encoded, interest_encoded]])[0]
        group = le_groups.inverse_transform([group_encoded])[0]

        # Lọc các nghề nghiệp phù hợp
        careers = data[data["People"] == group]["Nghề nghiệp phù hợp"].tolist()

        result = {
            "group": group,
            "careers": careers
        }

    return render_template("index.html", traits=traits_options, interests=interests_options, result=result)

if __name__ == "__main__":
    app.run(debug=True)
