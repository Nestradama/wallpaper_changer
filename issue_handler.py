# This file will be only to handle issues
from PyQt6.QtWidgets import QMessageBox


def is_image_gif(): #Not implemented yet
    alert = QMessageBox()
    alert.raise_()
    alert.setWindowTitle("Error")
    alert.setIcon(QMessageBox.Icon.Warning)
    alert.setText("The current image is a GIF.")
    alert.exec()


def no_value_returned_api(error):
    alert = QMessageBox()
    alert.raise_()
    alert.setWindowTitle("No results")
    alert.setIcon(QMessageBox.Icon.Warning)
    alert.setText(f"Error: {error}")
    alert.exec()


def api_sorting_set(sorting_type):
    match str(sorting_type):
        case "random":
            return "random"
        case "recently added":
            return "date_added"
        case "top-rated today":
            return "toplist1d"
        case "top-rated last 3 days":
            return "toplist3d"
        case "top-rated this week":
            return "toplist1w"
        case "top-rated this month":
            return "toplist1m"
        case "top-rated this year":
            return "toplist1y"
        case _:
            return "random"

def api_purity_set(purity_type):
    print(purity_type,"BBBBBB")
    match str(purity_type):
        case "sfw":
            return "100"
        case "sketchy":
            return "110"
        case "nsfw":
            return "111"
        case _:
            return "100"