import datetime
import time

def countdown_clock(target_event):
    # Convert target event string to datetime object
    target_datetime = datetime.datetime.strptime(target_event, '%Y-%m-%d %H:%M:%S')

    while True:
        # Calculate the time difference between now and the target event
        time_difference = target_datetime - datetime.datetime.now()

        # Check if the target event has passed
        if time_difference.total_seconds() <= 0:
            print("The countdown is over!")
            break

        # Display the remaining time
        print(f"Time remaining until {target_event}: {time_difference}")

        # Wait for one second before updating the countdown
        time.sleep(1)
# Example usage: Countdown to New Year's Day
target_event = '2023-01-01 00:00:00'
countdown_clock(target_event)
