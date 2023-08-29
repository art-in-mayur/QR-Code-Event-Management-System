import cv2
import time
from pyzbar.pyzbar import decode

def process_event(img, db_connection):
    for code in decode(img):
        code_data = code.data.decode('utf-8')
        display_entry_info(img, f'Code Scanned: {code_data}')
        if code_data:
            check_attendance(code_data, db_connection)

def check_attendance(code_data, db_connection):
    cursor = db_connection.cursor()

    cursor.execute('SELECT * FROM attendees WHERE qr_code = ?', (code_data,))
    attendee = cursor.fetchone()

    if attendee:
        if not attendee[5]:
            print('Approved. You may enter.')
            cursor.execute('UPDATE attendees SET check_in = 1 WHERE qr_code = ?', (code_data,))
        else:
            print('You are already checked in.')

    db_connection.commit()

def display_entry_info(img, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, text, (10, 30), font, 0.8, (0, 255, 0), 2)
