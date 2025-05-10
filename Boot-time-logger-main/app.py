# app.py
import os
import pandas as pd
from openpyxl import Workbook, load_workbook
from twilio.rest import Client

def boot_time():
    global today, day_of_week
    today = pd.Timestamp.today()
    day_of_week = today.day_name()[:3]

    # — TXT log —
    with open("boot_logs.txt", "a") as f:
        f.write(f"Boot time: {today} ({day_of_week})\n")

    # — Excel log —
    fn = "boot_logs.xlsx"
    if os.path.exists(fn):
        wb = load_workbook(fn)
        ws = wb.active
    else:
        wb = Workbook()
        ws = wb.active
        headers = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        for i,h in enumerate(headers,1):
            ws.cell(row=1, column=i, value=h)

    cols = {'Mon':1,'Tue':2,'Wed':3,'Thu':4,'Fri':5,'Sat':6,'Sun':7}
    col = cols[day_of_week]
    nr = ws.max_row + 1
    ws.cell(row=nr,   column=col, value=str(today.date()))
    ws.cell(row=nr+1, column=col, value=str(today.time()))

    try:
        wb.save(fn)
    except PermissionError:
        # bubble up a clear error
        raise PermissionError("Cannot write to boot_logs.xlsx – please close it in Excel and try again.")

    # — WhatsApp —
    send_whatsapp_message(today, day_of_week)


def send_whatsapp_message(boot_time, day_of_week):
    account_sid   = ''
    auth_token    = ''
    from_whatsapp = ""
    to_whatsapp   = ""

    client = Client(account_sid, auth_token)
    client.messages.create(
        body=f"Boot time logged: {boot_time} ({day_of_week})",
        from_=from_whatsapp,
        to=to_whatsapp
    )

def main():
    print("Logging boot time…")
    boot_time()
    print("Done.")

if __name__ == "__main__":
    main()
