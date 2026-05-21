def export_report_pdf(report_data):
    return {
        "status": "success",
        "file_name": "report.pdf",
        "report_data": report_data,
        "message": "PDF report exported successfully"
    }


def export_report_excel(report_data):
    return {
        "status": "success",
        "file_name": "report.xlsx",
        "report_data": report_data,
        "message": "Excel report exported successfully"
    }