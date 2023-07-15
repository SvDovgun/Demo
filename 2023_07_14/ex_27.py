#import datetime
from datetime import datetime

date_text = "2023.07.14"

#d = datetime.datetime.strptime(date_text, "%Y.%m.%d")
d = datetime.strptime(date_text, "%Y.%m.%d")

print(d.weekday())
