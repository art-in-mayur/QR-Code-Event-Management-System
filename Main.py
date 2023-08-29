import cv2
from event_manager import process_event
from database import connect_to_db

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    db_connection = connect_to_db()

    while True:
        _, img = cap.read()

        process_event(img, db_connection)

        cv2.imshow('Event Management with QR Code', img)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

    cap.release()
    db_connection.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
