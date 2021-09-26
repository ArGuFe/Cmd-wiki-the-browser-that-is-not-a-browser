import wikipedia
import requests

search = False
download = False
print("Welcome to Cmd wiki!")

while True:
        choose = input("Choose one.\n\n[1]Search\n[2]Download\n[3]Quit\n\n")
        
        if choose == "1":
                search = True
                
                while search:
                        print("Type 'esc' to leave")
                        lookingFor = input("Search: ")
                        
                        if lookingFor == "esc":
                                search = False

                        if search:
                                try:
                                        print("\n\n" + wikipedia.page(lookingFor).content + "\n\n")
                                except:
                                        print("I can't find the answer.\nYou maybe could try doing it a different way.")
        
        elif choose == "2":
                download = True
                
                while download:
                        print("Type 'esc' to leave")
                        downloadFile = input("Download url: ")
                        canGoInstallation = False
                        installer = ""
                        
                        if downloadFile == "esc":
                                download = False

                        if download:
                                try:
                                        installer = requests.get(downloadFile)
                                        canGoInstallation = True
                                except:
                                        print("This url does not exist.")
                        
                                if canGoInstallation:
                                        fileName = installer.split('/')[-1]
                                
                                with open(fileName, 'wb') as out_file:
                                        out_file.write(installer.content)
                                if canGoInstallation:
                                        print("Installation complete!")
        
        else:
                quit()
