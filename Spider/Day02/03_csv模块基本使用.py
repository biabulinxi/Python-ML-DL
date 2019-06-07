import csv 

with open('test.csv','w',newline='',encoding='utf-8') as f:
    # 初始化写入对象
    writer = csv.writer(f)
    # 利用对象的writerow方法写数据
    writer.writerow(['小姐姐','20'])
    writer.writerow(['小哥哥','25'])