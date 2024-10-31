# 儲存人
records = []

# 顯示表格格式
def display_table(data):
    if not data:
        print("目前沒有任何資料")
        return
    print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<15}")
    print("-" * 45)
    for record in data:
        print(f"{record['部門']:<10}{record['姓名']:<10}{record['年齡']:<10}{record['手機']:<15}")

# 新增
def add():
    while True:
        department = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = input("請輸入年齡: ")
        phone = input("請輸入手機號碼: ")
        
        record = {"部門": department, "姓名": name, "年齡": age, "手機": phone}
        records.append(record)
        
        cont = input("是否繼續新增資料? (y/n): ").lower()
        if cont != 'y':
            break

# 查詢資料
def search():
    name = input("請輸入要查詢的姓名: ")
    result = [record for record in records if record["姓名"] == name]
    
    if result:
        print("\n--- 查詢結果 ---")
        display_table(result)
    else:
        print("查無此人。")

# 修改資料
def modify():
    name = input("請輸入要修改的姓名: ")
    result = [record for record in records if record["姓名"] == name]
    
    if not result:
        print("查無此人。")
        return
    
    print("\n當前資料:")
    display_table(result)
    record = result[0]
    
    print("\n1. 修改部門\n2. 修改姓名\n3. 修改年齡\n4. 修改手機")
    choice = input("請選擇要修改的欄位: ")
    
    if choice == '1':
        record["部門"] = input("請輸入新的部門: ")
    elif choice == '2':
        record["姓名"] = input("請輸入新的姓名: ")
    elif choice == '3':
        record["年齡"] = input("請輸入新的年齡: ")
    elif choice == '4':
        record["手機"] = input("請輸入新的手機號碼: ")
    else:
        print("無效的選項。")
        return
    
    print("\n--- 更新後的資料 ---")
    display_table([record])

# 刪除資料
def delete():
    name = input("請輸入要刪除的姓名: ")
    result = [record for record in records if record["姓名"] == name]
    
    if not result:
        print("查無此人。")
        return
    
    print("\n找到以下資料:")
    display_table(result)
    confirm = input(f"確定要刪除 {name} 的資料嗎? (y/n): ").lower()
    
    if confirm == 'y':
        records.remove(result[0])
        print(f"{name} 的資料已刪除。")
        print("\n--- 剩餘的所有資料 ---")
        display_table(records)

# 顯示所有資料
def display_all():
    print("\n--- 所有人員資料 ---")
    display_table(records)

# 主程式
def main():
    menu = {
        '1': add,
        '2': search,
        '3': modify,
        '4': delete,
        '5': display_all,
        '6': lambda: print("系統已退出。")
    }

    while True:
        print("\n--- 人事資料管理系統 ---")
        print("1. 新增資料\n2. 查詢資料\n3. 修改資料\n4. 刪除資料\n5. 顯示所有資料\n6. 退出系統")
        print("------------------------")
        
        choice = input("請選擇功能: ")
        
        action = menu.get(choice)
        if action:
            action()
            if choice == '6':  # 退出選項
                break
        else:
            print("無效的選項，請重新選擇。")

main()
