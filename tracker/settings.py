# Settings

import os
import sys

# Search "my user agent" on Google to find user agent (Must have!)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'


# Time interval in seconds for when the tracker checks prices
# 15 minutes (1800 seconds) is recommended in order to avoid being blocked by Amazon
check_interval = 900


# Email address in which the tracker will use to send a message (Must be a gmail account)
# This is required!
sender_email = 'p7637107@gmail.com'


# Password of the sender email address (Edit the sender_password.key file to change the password)
# This is required!
with open(os.path.join(sys.path[0], "sender_password.key"), "r") as f:
    sender_password = f.read()


# Email address in which the tracker will send a message to
# This is required!
reciever_email = 'varun4563232@gmail.com'


# Phone number in which the tracker will send a message to (Do not include dashes or any extra characters!)
# Leave '' if no text is desired
reciever_phone_number = ''


# Cell provider for the phone number ('at&t', 'verizon', or 'tmobile')
# Leave '' if no phone number is given
reciever_cell_provider = ''


# You may leave this as default
CSV_ITEM_FILE = os.path.join(sys.path[0], "data", "data.csv")
ITEM_NUM_FILE = os.path.join(sys.path[0], "data", "itemNum.txt")
