from flask import render_template, request, Flask

from app.src.utils.exception import MyException
from app.src.utils.logger import logging
from app.src.pipelines.prediction_pipeline import PredictionPipeline, Prediction

app = Flask(__name__,
            template_folder="frontend/templates",
            static_folder="frontend/static")

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            cgpa = float(request.form["cgpa"])
            projects = int(request.form["projects"])
            communication_skills = float(request.form["communication_skills"])
            internship = int(request.form["internship"])
            programming_skills = int(request.form["programming_skills"])
            technical_skills = int(request.form["technical_skills"])
            certifications = int(request.form["certifications"])
            aptitude = float(request.form["aptitude"])
            interview_score = float(request.form["interview_score"])

            input_data = PredictionPipeline(
                cgpa = cgpa,
                projects = projects,
                communication_skills = communication_skills,
                internship = internship,
                programming_skills = programming_skills,
                technical_skills = technical_skills,
                certifications = certifications,
                aptitude = aptitude,
                interview_score = interview_score
            )

            input_df = input_data.get_data_into_dataframe()
            classifier = Prediction()
            prediction = classifier.predict(df = input_df)
            prediction_value = int(prediction[0])

            if prediction_value == 1:
                result = "Placed"
            else:
                result = "Not Placed"

            return render_template("index.html", prediction = result)

        except Exception as e:
            return render_template("index.html", error = str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)