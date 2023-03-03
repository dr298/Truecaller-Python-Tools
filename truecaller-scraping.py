import subprocess

# Check if colorama is installed, install it if not
try:
    import colorama
except ImportError:
    subprocess.check_call(['pip3', 'install', 'colorama'])
    import colorama

# Initialize colorama
colorama.init()

# Check if truecallerpy is installed, install it if not
try:
    import truecallerpy
    print(f"{colorama.Fore.GREEN}truecallerpy already installed{colorama.Style.RESET_ALL}")
except ImportError:
    print(f"{colorama.Fore.YELLOW}installing truecallerpy module{colorama.Style.RESET_ALL}")
    subprocess.check_call(['pip3', 'install', 'truecallerpy'])
    import truecallerpy
    print(f"{colorama.Fore.GREEN}truecallerpy installed completely{colorama.Style.RESET_ALL}")

# Print banner and prompt user to continue
print(f"""{colorama.Fore.LIGHTRED_EX}
         .___      ________  ________  ______  
       __| _/______\_____  \/   __   \/  __  \ 
      / __ |\_  __ \/  ____/\____    />      < 
     / /_/ | |  | \/       \   /    //   --   \\
     \____ | |__|  \_______ \ /____/ \______  /
          \/               \/               \/ 
== good or bad? it depends on your point of view! ==

Follow this step to login to your truecaller account :
1. On Truecaller Android, tap on the 3 line menu on top left then click on setting's.
2. Tap on Privacy Center and then click on Download my data.
3. Now a JSON file is downloaded.
4. Save the JSON file at this tools file location
5. Rename the JSON file to truecaller.json

{colorama.Style.RESET_ALL}""")

input(f"{colorama.Fore.GREEN}Ready to go? Press Enter to continue...{colorama.Style.RESET_ALL}")

# Login to Truecaller
subprocess.check_call(['truecallerpy', '--login', '-f', 'truecaller.json'])
print(f"{colorama.Fore.GREEN}login complete{colorama.Style.RESET_ALL}")

# Read numbers from phone.txt and search on Truecaller
with open('phone.txt', 'r') as f:
    for line in f:
        number = line.strip()
        output = subprocess.check_output(['truecallerpy', '-s', number, '--name']).decode().strip()
        name = output.split(":")[1].strip()
        print(f"{number}:{name}")
        with open('result.txt', 'a') as f2:
            f2.write(f"{number} : {name}\n")

print(f"{colorama.Fore.GREEN}Done!{colorama.Style.RESET_ALL}")
