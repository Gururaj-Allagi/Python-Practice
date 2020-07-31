from FilesFolders import FolderFunc, FileFunc

run = True
fold = FolderFunc
file = FileFunc


def folder():
    print("""

                 Folder options:
                    1 > make folder     2 > move folder     3 > backup

                    4 > archive         5 > Extract         6 > List all folders and files

        Note: If the destination folder is not given the source Folder is taken as destination folder

                 """)
    fold_opt = ''
    while not (fold_opt == "1" or fold_opt == "2" or fold_opt == "3" or fold_opt == "4" or fold_opt == "5"
               or fold_opt == "6" or fold_opt == "q"):
        fold_opt = input("Choose option: ").lower()

    if fold_opt == '1':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        print(f'Folder has been created in {src}')
        fold(src).make()

    elif fold_opt == '2':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        dst = input("Enter the destination folder (Ex: D:/blah/): ")
        print(f'Folder has been moved from {src} to {dst}')
        fold(src, dst).mov()

    elif fold_opt == '3':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        dst = input("Enter the destination folder (Ex: D:/blah/): ")
        print(f'Folder has been backed_up from {src} to {dst}')
        fold(src, dst).backup()

    elif fold_opt == '4':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        dst = input("Enter the destination folder (Ex: D:/blah/): ")
        mde = input("enter the from (ex: zip or tar)")
        print(f'Folder has been Archived in {src} to {dst}{mde}')
        fold(src, dst).archive(mde)

    elif fold_opt == '5':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        dst = input("Enter the destination folder (Ex: D:/blah/): ")
        print(f'Folder has been unpacked from {src} to {dst}')
        fold(src, dst).unpack()

    elif fold_opt == '6':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        print(f'Listing all the files and folders in  directory')
        fold(str(src)).All_fol_fil()
    else:
        pass


def fle():
    print("""
    
               File options:
                   1 > make file       2 > rename all files in a folder
                       
                   3 > move all the file/files with a particular extension
    
                   4 > archive         5 > Extract         6 > List all folders and files
                 
        Note: If the destination folder is not given the source Folder is taken as destination folder
        
               """)
    fle_opt = ''
    while not (fle_opt == "1" or fle_opt == "2" or fle_opt == "3" or fle_opt == "4" or fle_opt == "5"
               or fle_opt == "6" or fle_opt == "q"):
        fle_opt = input("Choose option: ").lower()

    if fle_opt == '1':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        print(f'Folder has been created in {src}')
        file(src).make()

    elif fle_opt == '2':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        ext = input("Enter the extension (Ex: .png or .xlsx): ")
        print(f'Renamed all files in a folder with {ext} extension ')
        file(src).rename(ext)

    elif fle_opt == '3':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        dst = input("Enter the destination folder (Ex: D:/blah/): ")
        ext = input("Enter the extension (Ex: .png or .xlsx): ")
        print(f'Files with a {ext} has been moved {src} to {dst}')
        file(src, dst, ext).move_ext_file()

    elif fle_opt == '4':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        dst = input("Enter the destination folder (Ex: D:/blah/): ")
        mde = input("enter the from (ex: zip or tar)")
        print(f'File has been Archived in {src} to {dst}{mde}')
        file(src, dst).archive(mde)

    elif fle_opt == '5':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        dst = input("Enter the destination folder (Ex: D:/blah/): ")
        print(f'File has been unpacked from {src} to {dst}')
        file(src, dst).unpack()

    elif fle_opt == '6':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        print(f'Listing all the files and folders in  directory')
        file(str(src)).All_fol_fil()

    else:
        pass


def main():
    try:
        print("""
        
        Choose operation :
            1 > Folder Functions
            2 > File Functions
            q > Quit
        """)
        func_ope = ''
        while not (func_ope == '1' or func_ope == '2' or func_ope == 'q'):
            func_ope = input("Choose option: ").lower()

        if func_ope == '1':
            folder()

        elif func_ope == '2':
            fle()
        elif func_ope == 'q':
            quit()
        else:
            pass
    except Exception as e:
        print(e)


while run:
    main()
    repeat = input("Would you like to play another hand? Enter 'y' or 'n': ")
    if repeat[0].lower() == 'y':
        run = True
        continue
    else:
        print("Thank you!")
        break
