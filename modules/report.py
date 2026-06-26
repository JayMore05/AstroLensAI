from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_report(filename, prediction, confidence, nasa_info):

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    story = [

        Paragraph("<b>AstroLensAI Report</b>", styles["Heading1"]),

        Paragraph(f"Prediction : {prediction}", styles["BodyText"]),

        Paragraph(f"Confidence : {confidence}%", styles["BodyText"]),

        Paragraph(nasa_info, styles["BodyText"])

    ]

    pdf.build(story)