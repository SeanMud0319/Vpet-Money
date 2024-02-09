import os
import re

def get_current_money(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.search(r'money#(\d+)\b', line.strip())
            if match:
                money_number = int(match.group(1))
                return money_number
    return None

def update_money(file_path, new_money):
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'(money#\d+)', content)
        if match:
            updated_content = re.sub(r'money#\d+', f'money#{new_money}', content)
            file.seek(0)
            file.write(updated_content)
            file.truncate()
        else:
            print("Money line not found.")




folder_path = r'C:\Program Files (x86)\Steam\steamapps\common\VPet\Saves'

files = os.listdir(folder_path)

save_files = [filename for filename in files if filename.startswith('Save_') and filename.endswith('.lps')]

if not save_files:
    print("No save files found.")
else:
    numbers = [int(filename.split('_')[1].split('.')[0]) for filename in save_files]

    max_number = max(numbers)
    max_file_name = f"Save_{max_number}.lps"
    max_file_path = os.path.join(folder_path, max_file_name)

    current_money = get_current_money(max_file_path)

    if current_money is not None:
        current_money_formatted = current_money // 10**9
        print(f"Current money: {current_money_formatted}")
        new_money = input("Please enter new money: ")
        try:
            new_money = int(float(new_money) * 10**9)
            print(f"New money: {new_money // 10**9}")
            update_money(max_file_path, new_money)
            print("Data successfully update!")
            print(f"請右鍵人物->開啟設定->系統->載入備份檔, 將當前備份檔改為: {max_file_name} 後點選載入並按確定")
            input("Press Enter to exit...")
        except ValueError:
            print("Invalid money format. Please enter a valid number.")
