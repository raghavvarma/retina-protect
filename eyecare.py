import subprocess as s      # to pass system commands
import platform as p        # to detect linux or osx
import time                 # for pausing the script
import os                   # legacy system command method
import win10toast
from enums import Urgency   # linux urgency settings
import sys
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk

work_time = 1
relax_time = 20
notification_expire = 5000  # linux only

# message settings
warning_title = 'Your eyes'
warning_message = 'Take a break. Just {} seconds.'.format(relax_time)
warning_urgency = Urgency.high # linux only. can be either low, medium or high

success_title = 'Good job'
success_message = 'You can get back to work.'
success_urgency = Urgency.low  # linux only. can be either low, medium or high


# get the system platform
os1 = p.system().lower()

command_method = 'modern' # 'modern' = subprocess.call | 'legacy' = os.system

if os1 == 'linux':
    command = 'notify-send'  # command being used
    expiration = '--expire-time={}'.format(notification_expire)

    while command_method == 'modern':
        time.sleep(work_time)
        s.call([command, warning_urgency, expiration, warning_title, warning_message])
        time.sleep(relax_time)
        s.call([command, success_urgency, expiration, success_title, success_message])

    while command_method == 'legacy':
        warning_cmd = "{0} {1} {2} \"{3}\" \"{4}\"".format(command, warning_urgency, expiration, warning_title, warning_message)
        success_cmd = "{0} {1} {2} \"{3}\" \"{4}\"".format(command, success_urgency, expiration, success_title, success_message)

        time.sleep(work_time)
        os.system(warning_cmd)
        time.sleep(relax_time)
        os.system(success_cmd)

if os1 == 'darwin':  # thats osx
    command1 = 'osascript -e'
    command2 = 'display notification'  # osx command, extra ' has to be there!
    with_title = 'with title'
    command_method = 'legacy'
    
    while command_method == 'modern':
        time.sleep(work_time)
        s.call([command1, "\'" + command2, '\"' + warning_message + '\"', 'with title', '\"' +  warning_title + '\"' + "\'"])
        time.sleep(relax_time)
        s.call([command1, "\'" + command2, '\"' + success_message + '\"', 'with title', '\"' + success_title + '\"' + "\'"])

    while command_method == 'legacy':
        warning_cmd = "{0} \'{1} \"{2}\" {3} \"{4}\"\'".format(command1, command2, warning_message, with_title, warning_title)
        success_cmd = "{0} \'{1} \"{2}\" {3} \"{4}\"\'".format(command1, command2, success_message, with_title, success_title)

        time.sleep(work_time)
        os.system(warning_cmd)
        time.sleep(relax_time)
        os.system(success_cmd)

if os1 == "windows":
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("python", "success", duration=10)