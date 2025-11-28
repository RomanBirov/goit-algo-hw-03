from datetime import datetime


def get_days_from_today(date):
    today = datetime.today()
    try:
        datedit = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(
            "parametr date must be in format yyyy-mm-dd. example: "
            + today.strftime("%Y-%m-%d")
        )
        return
    period = today - datedit
    return period.days