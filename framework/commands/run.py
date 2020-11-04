"""
Console scripts runner
"""

import colorama
import sys
colorama.init(autoreset=True)


def show_usage():
    show_basic_usage()
    sc = ""
    sc += '    Type "sdet help [COMMAND]" for specific command info.\n'
    sc += '    For info on all commands, type: "sdet --help".\n'
    sc += ' * (Use "pytest" for running tests) *\n'
    print(colorama.Fore.MAGENTA + sc)


def show_basic_usage():
    print()
    show_package_location()
    show_version_info()
    print()
    sc = ""
    sc += ' * USAGE: "sdet [COMMAND] [PARAMETERS]"\n'
    sc += ' *    OR:        "qa [COMMAND] [PARAMETERS]"\n'
    sc += "\n"
    sc += "COMMANDS:\n"
    sc += "      install         [DRIVER] [OPTIONS]\n"
    sc += "      encrypt         (OR: obfuscate)\n"
    sc += "      decrypt         (OR: unobfuscate)\n"
    sc += "      download server (Selenium Server JAR file)\n"
    sc += "      grid-hub        [start|stop] [OPTIONS]\n"
    sc += "      grid-node       [start|stop] --hub=[HOST/IP]\n"
    sc += ""
    print(colorama.Fore.MAGENTA + sc)


def show_install_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = ("  " + c2 + "** " + c3 + "install" + c2 + " **" + cr)
    print(sc)
    print("")
    print("  Usage:")
    print("           sdet install [DRIVER_NAME] [OPTIONS]")
    print("           OR:    qa install [DRIVER_NAME] [OPTIONS]")
    print("                 (Drivers: chrome, gecko, edge")
    print("                           ie, opera)")
    print("  Options:")
    print("           VERSION         Specify the version.")
    print("                           (Default Chromedriver version = 2.44)")
    print('                           Use "latest" or -l for the latest version.')
    print("           -p OR --path    Also copy the driver to /usr/local/bin")
    print("  Example:")
    print("           sdet install chrome")
    print("           sdet install gecko")
    print("           sdet install edge")
    print("           sdet install chrome 85")
    print("           sdet install chrome 85.0.4183.87")
    print("           sdet install chrome latest")
    print("           sdet install chrome -p")
    print("           sdet install chrome latest -p")
    print("           sdet install edged 85.0.564.68")
    print("  Output:")
    print("           Installs the chosen webdriver to framework/drivers/")
    print("           (chrome is required for Chrome automation)")
    print("           (gecko is required for Firefox automation)")
    print("           (edge is required for Microsoft Edge automation)")
    print("           (ie is required for InternetExplorer automation)")
    print("           (opera is required for Opera Browser automation)")
    print("")


def show_encrypt_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = ("  " + c2 + "** " + c3 + "encrypt OR obfuscate" + c2 + " **" + cr)
    print(sc)
    print("")
    print("  Usage:")
    print("           sdet encrypt   ||   Super-sdet obfuscate")
    print("                                --OR--")
    print("                  qa encrypt   ||          qa obfuscate")
    print("  Output:")
    print("           Runs the password encryption/obfuscation tool.")
    print("           (Where you can enter a password to encrypt/obfuscate.)")
    print("")


def show_decrypt_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = ("  " + c2 + "** " + c3 + "decrypt OR unobfuscate" + c2 + " **" + cr)
    print(sc)
    print("")
    print("  Usage:")
    print("           sdet decrypt   ||   sdet unobfuscate")
    print("                                --OR--")
    print("                  qa decrypt   ||          qa unobfuscate")
    print("  Output:")
    print("           Runs the password decryption/unobfuscation tool.")
    print("           (Where you can enter an encrypted password to decrypt.)")
    print("")


def show_download_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = ("  " + c2 + "** " + c3 + "download" + c2 + " **" + cr)
    print(sc)
    print("")
    print("  Usage:")
    print("           sdet download server")
    print("           OR:    qa download server")
    print("  Output:")
    print("           Downloads the Selenium Standalone Server.")
    print("           (Server is required for using your own Selenium Grid.)")
    print("")


def show_grid_hub_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = ("  " + c2 + "** " + c3 + "grid-hub" + c2 + " **" + cr)
    print(sc)
    print("")
    print("  Usage:")
    print("           sdet grid-hub {start|stop|restart} [OPTIONS]")
    print("           OR:    qa grid-hub {start|stop|restart} [OPTIONS]")
    print("  Options:")
    print("           -v, --verbose  (Increase verbosity of logging output.)")
    print("                          (Default: Quiet logging / not verbose.)")
    print("           --timeout=TIMEOUT  (Close idle browser after TIMEOUT.)")
    print("                              (The default TIMEOUT: 230 seconds.)")
    print("                              (Use --timeout=0 to skip timeouts.)")
    print("  Example:")
    print("           sdet grid-hub start")
    print("  Output:")
    print("           Controls the Selenium Grid Hub Server, which allows")
    print("           for running tests on multiple machines in parallel")
    print("           to speed up test runs and reduce the total time")
    print("           of test suite execution.")
    print('           You can "start" or "stop" the Grid Hub server.')
    print("")


def show_grid_node_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = ("  " + c2 + "** " + c3 + "grid-node" + c2 + " **" + cr)
    print(sc)
    print("")
    print("  Usage:")
    print("           sdet grid-node {start|stop|restart} [OPTIONS]")
    print("           OR:    qa grid-node {start|stop|restart} [OPTIONS]")
    print("  Options:")
    print("           --hub=[HOST/IP]  (The Grid Hub Hostname / IP Address.)")
    print("                                 (Default: 127.0.0.1 if not set.)")
    print("           -v, --verbose  (Increase verbosity of logging output.)")
    print("                          (Default: Quiet logging / Not verbose.)")
    print("  Example:")
    print("           sdet grid-node start --hub=127.0.0.1")
    print("  Output:")
    print("           Controls the Selenium Grid node, which serves as a")
    print("           worker machine for your Selenium Grid Hub server.")
    print('           You can "start" or "stop" the Grid node.')
    print("")


def get_version_info():
    # from pkg_resources import get_distribution
    # version = get_distribution("framwork").version
    from framework import __version__
    version_info = None
    c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sb_text = c1 + "Super" + c2 + "Framework" + cr
    version_info = "%s %s%s%s" % (sb_text, c3, __version__, cr)
    return version_info


def show_version_info():
    version_info = get_version_info()
    print('%s' % version_info)


def get_package_location():
    import os
    import framework
    location = os.path.dirname(os.path.realpath(framework.__file__))
    if location.endswith("framework"):
        location = location[0:-len("framework")]
    return location


def show_package_location():
    location = get_package_location()
    print("%s" % location)


def show_options():
    c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = ("\n " + c2 + " ** " + c3 + " pytest CLI Options " + c2 + " ** " + cr)
    print(sc)
    print("")
    line = "Here are some cryption pytest options to use with Super Framework:"
    line = c1 + line + cr
    print(line)
    print("")
    print('--browser=BROWSER  (The web browser to use. Default: "chrome".)')
    print('--headless  (Run tests headlessly. Default mode on Linux OS.)')
    print('--demo  (Slow down and visually see test actions as they occur.)')
    print('--slow  (Slow down the automation. Faster than using Demo Mode.)')
    print('--reuse-session / --rs  (Reuse the browser session between tests.)')
    print('--crumbs  (Delete all cookies between tests reusing a session.)')
    print('--maximize  (Start tests with the web browser window maximized.)')
    print("--incognito  (Enable Chrome's Incognito mode.)")
    print("--guest  (Enable Chrome's Guest mode.)")
    print('-m MARKER  (Run tests with the specified pytest marker.)')
    print('-n NUM  (Multithread the tests using that many threads.)')
    print('-v  (Verbose mode. Prints the full names of each test run.)')
    print('--html=report.html  (Create a detailed pytest-html report.)')
    print('--collect-only / --co  (Only show discovered tests. No run.)')
    print('--co -q  (Only show full names of discovered tests. No run.)')
    print('--trace  (Enter Debug Mode immediately after starting any test.')
    print('          n: Next line of method. s: Step through. c: Continue.)')
    print('--pdb  (Enter Debug Mode if a test fails. h: Help. c: Continue.')
    print('        where: Stacktrace location. u: Up stack. d: Down stack.')
    print('        longlist / ll: See code. dir(): List namespace objects.)')
    print('-x  (Stop running the tests after the first failure is reached.)')
    print('--archive-logs  (Archive old log files instead of deleting them.)')
    print('--save-screenshot  (Save a screenshot at the end of each test.)')
    print('--check-js  (Check for JavaScript errors after page loads.)')
    print('--start-page=URL  (The browser start page when tests begin.)')
    print("--agent=STRING  (Modify the web browser's User-Agent string.)")
    print('--mobile  (Use the mobile device emulator while running tests.)')
    print('--metrics=STRING  (Set mobile "CSSWidth,CSSHeight,PixelRatio".)')
    print('--ad-block  (Block some types of display ads after page loads.)')
    print('--settings-file=FILE  (Override default Super-Framework'
          ' settings.)')
    print('--env=ENV  (Set the test env. Access with "self.env" in tests.)')
    print('--data=DATA  (Extra test data. Access with "self.data" in tests.)')
    print('--disable-csp  (Disable the Content Security Policy of websites.)')
    print('--server=SERVER  (The Selenium Grid server/IP used for tests.)')
    print('--port=PORT  (The Selenium Grid port used by the test server.)')
    print('--proxy=SERVER:PORT  (Connect to a proxy server:port for tests.)')
    print('--proxy=USER:PASS@SERVER:PORT  (Use authenticated proxy server.)')
    print("")
    line = 'For the full list of ' + c2 + 'command-line options' + cr
    line += ', type: "' + c1 + 'pytest' + cr + ' ' + c3 + '--help' + cr + '".'
    print(line)
    print("")


def show_detailed_help():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    c6 = colorama.Back.CYAN
    cr = colorama.Style.RESET_ALL
    show_basic_usage()
    print(c6 + "            " + c2 + "  Commands:  " + c6 + "            ")
    print(cr)
    show_install_usage()
    show_decrypt_usage()
    show_download_usage()
    show_grid_hub_usage()
    show_grid_node_usage()
    print('* (Use "' + c3 + 'pytest' + cr + '" for running tests) *\n')


def main():
    command = None
    command_args = None
    num_args = len(sys.argv)
    if num_args == 1:
        show_usage()
        return
    elif num_args == 2:
        command = sys.argv[1]
        command_args = []
    elif num_args > 2:
        command = sys.argv[1]
        command_args = sys.argv[2:]
    command = command.lower()

    if command == "install":
        if len(command_args) >= 1:
            from framework.commands import sb_install
            sb_install.main()
        else:
            show_basic_usage()
            show_install_usage()
    elif command == "encrypt" or command == "obfuscate":
        if len(command_args) >= 0:
            from framework.cryption import obfuscate
            obfuscate.main()
        else:
            show_basic_usage()
            show_encrypt_usage()
    elif command == "decrypt" or command == "unobfuscate":
        if len(command_args) >= 0:
            from framework.cryption import unobfuscate
            unobfuscate.main()
        else:
            show_basic_usage()
            show_decrypt_usage()
    elif command == "download":
        if len(command_args) >= 1 and command_args[0].lower() == "server":
            from framework.utilities.selenium_grid import (
                download_selenium_server)
            download_selenium_server.main(force_download=True)
        else:
            show_basic_usage()
            show_download_usage()
    elif command == "grid-hub" or command == "grid_hub":
        if len(command_args) >= 1:
            from framework.utilities.selenium_grid import grid_hub
            grid_hub.main()
        else:
            show_basic_usage()
            show_grid_hub_usage()
    elif command == "grid-node" or command == "grid_node":
        if len(command_args) >= 1:
            from framework.utilities.selenium_grid import grid_node
            grid_node.main()
        else:
            show_basic_usage()
            show_grid_node_usage()
    elif command == "version" or command == "--version":
        if len(command_args) == 0:
            show_package_location()
            show_version_info()
            print()
        else:
            show_basic_usage()
    elif command == "options" or command == "--options":
        show_options()
    elif command == "help" or command == "--help":
        if len(command_args) >= 1:
            if command_args[0] == "install":
                print("")
                show_install_usage()
                return
            elif command_args[0] == "encrypt":
                print("")
                show_encrypt_usage()
                return
            elif command_args[0] == "obfuscate":
                print("")
                show_encrypt_usage()
                return
            elif command_args[0] == "decrypt":
                print("")
                show_decrypt_usage()
                return
            elif command_args[0] == "unobfuscate":
                print("")
                show_decrypt_usage()
                return
            elif command_args[0] == "download":
                print("")
                show_download_usage()
                return
            elif command_args[0] == "grid-hub":
                print("")
                show_grid_hub_usage()
                return
            elif command_args[0] == "grid-node":
                print("")
                show_grid_node_usage()
                return
        show_detailed_help()
    else:
        show_usage()


if __name__ == "__main__":
    main()
