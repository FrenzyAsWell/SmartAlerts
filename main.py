import sys, os, shutil
import colorama
import requests

from colorama import Fore, Back, Style
from colorama import init as colorama_init

class CPrintingWork:
    line_lenght = 64

    def clean_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_line(self, count_sign: int):
        for a in range(count_sign):
            print('-', end='')
        print()

    def print_logo(self):
        print(Fore.RED, end='')

        self.print_line(self.line_lenght)
        with open("Images/logo.txt", 'r') as f:
            print(f.read(), end='')

        self.print_line(self.line_lenght)

        print(Fore.BLUE, end='')
        self.print_line(self.line_lenght)

        for a in range(7):
            print("|", end='')
            if (a % 2 == 1) and (a > 0 and a < 6):
                match a:
                    case 1: print(f"{Fore.YELLOW} GitHub: https://github.com/FrenzyCode64 {Fore.BLUE}", end='')
                    case 3: print(f"{Fore.YELLOW} Steam: https://steamcommunity.com/profiles/76561198931354092/ {Fore.BLUE}", end='')
                    case 5: print(f"{Fore.YELLOW} YouTube: https://www.youtube.com/channel/UC1eDs-42u2UZ9A0ykDFXl4g {Fore.BLUE}", end='')
            print()

        self.print_line(self.line_lenght)
        print(Style.RESET_ALL)

class CScriptWork:
    save_method = -1

    range_value_first = -1
    range_value_second = -1

    range_key_first = -1
    range_key_second = -1

    def check_user(self):
        str_check = input("Enter (+) to continue: ")
        if str_check != '+':
            object_PrintingWork.clean_console()
            exit()
        else:
            object_PrintingWork.clean_console()
            
    def setup_script(self):
        self.save_method = -1

        self.range_value_first = -1
        self.range_value_second = -1

        self.range_key_first = -1
        self.range_key_second = -1

        print(f"{Fore.RED}| {Style.RESET_ALL}{Style.BRIGHT}Saving result:{Style.RESET_ALL}")

        while self.save_method < 0 or self.save_method > 1:
            print(f"{Fore.RED}| Download files {Fore.YELLOW}(1){Fore.RED} or Save urls in .txt {Fore.YELLOW}(0){Style.RESET_ALL} > ", end='')
            self.save_method = int(input())

        print(f"{Fore.RED}| {Style.RESET_ALL}{Style.BRIGHT}Ports to listen:{Style.RESET_ALL}")

        while self.range_value_first < 11111 or self.range_value_first > 99999:
            print(f"{Fore.RED}| From Port {Fore.YELLOW}(11111 - 99999){Style.RESET_ALL} > ", end='')
            self.range_value_first = int(input())

        while self.range_value_second < self.range_value_first or self.range_value_second > 99999:
            print(f"{Fore.RED}| To Port {Fore.YELLOW}({self.range_value_first + 1} - 99999){Style.RESET_ALL} > ", end='')
            self.range_value_second = int(input())

        print(f"{Fore.RED}| {Style.RESET_ALL}{Style.BRIGHT}Attribute keys to select:{Style.RESET_ALL}")

        while self.range_key_first < 111 or self.range_key_first > 999:
            print(f"{Fore.RED}| From Key {Fore.YELLOW}(111 - 999){Style.RESET_ALL} > ", end='')
            self.range_key_first = int(input())

        while self.range_key_second < 111 or self.range_key_second > 999:
            print(f"{Fore.RED}| To Key {Fore.YELLOW}(111 - 999){Style.RESET_ALL} > ", end='')
            self.range_key_second = int(input())

        print(Fore.RED, "--------------------------------", Style.RESET_ALL)

        print(f"{Style.BRIGHT}Parse: {Style.RESET_ALL}")
        print(f"{Fore.RED}From{Style.RESET_ALL} http://static.donationalerts.ru/audiodonations/{Fore.YELLOW}{self.range_value_first}{Style.RESET_ALL}/{Fore.YELLOW}{self.range_value_first}{self.range_key_first}{Style.RESET_ALL}.wav")
        print(f"{Fore.RED}To{Style.RESET_ALL} http://static.donationalerts.ru/audiodonations/{Fore.YELLOW}{self.range_value_second}{Style.RESET_ALL}/{Fore.YELLOW}{self.range_value_second}{self.range_key_second}{Style.RESET_ALL}.wav")

        sign_ready = input(f"{Style.BRIGHT}\nEnter (+) | Reset (r) | Cancel (-): {Style.RESET_ALL}")
        object_PrintingWork.clean_console()

        match sign_ready:
            case '+': return 0
            case 'r': return 2
            case _: return 1
        
    def start_script(self):
        if self.save_method == 1:
            if os.path.exists("Result"):
                shutil.rmtree("Result")

            try:
                os.mkdir("Result")
                self.start_parse("Result" + '/')
            except OSError:
                print(f"{Style.BRIGHT, Fore.RED}!Can't create directory to save files!{Style.RESET_ALL}")
                input()

                exit()
        elif self.save_method == 0:
            if os.path.exists("result.txt"):
                os.remove("result.txt")

            open("result.txt", "x")
            self.start_parse("result.txt")

    def start_parse(self, path: str):
        current_port = self.range_value_first
        current_key = self.range_key_first

        while True:
            request_url = f"http://static.donationalerts.ru/audiodonations/{current_port}/{current_port}{current_key}.wav"

            request_result = requests.get(request_url)
            if request_result.status_code == 200:
                if self.save_method == 1:
                    with open(path + str(current_port) + str(current_key) + '.wav', 'wb') as f:
                        f.write(request_result.content)
                elif self.save_method == 0:
                    with open(path, 'a') as f:
                        f.write(request_url + '\n')

                print(f"{Fore.GREEN}Found: {request_url}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Nothing: {request_url}{Style.RESET_ALL}")

            if current_key >= 999:
                current_key = 111
                current_port += 1
            
            if current_port >= self.range_value_second and current_key >= self.range_key_second:
                return

            current_key += 1

object_PrintingWork = CPrintingWork()
object_ScriptWork = CScriptWork()

def main():
    object_PrintingWork.clean_console()
    
    colorama_init()

    object_PrintingWork.print_logo()

    object_ScriptWork.check_user()

    result_setup = object_ScriptWork.setup_script()
    if result_setup == 1:
        object_PrintingWork.clean_console
        exit()
    elif result_setup == 2:
        object_ScriptWork.setup_script()

    object_ScriptWork.start_script()

if __name__ == "__main__":
    main()