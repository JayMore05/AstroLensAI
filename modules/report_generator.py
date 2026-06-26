"""
Generate PDF reports.
"""

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)


class ReportGenerator:

    def create(self, filename, result):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>AstroLensAI Report</b>",
                styles["Title"]
            )
        )

        for key, value in result.items():

            story.append(

                Paragraph(
                    f"<b>{key}</b> : {value}",
                    styles["BodyText"]
                )

            )

        doc.build(story)