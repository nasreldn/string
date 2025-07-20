# file.txt

file = open("while/for.txt", "w")
file.write("مرحبًا بك في عالم بايثون!\nnasreldin.")
print(file)
file.close()
# file.code
file = open("while/one.py", "r")
content = file.read()
print(content)
# انشا ملف جديد والكتابه عليه
file = open("/home/nasor/Downloads/zezo.txt", "w")
file.write("حباب اللحوين")
print(file)

import os
# حاليا انت في ياتو ملف
print(os.getcwd())  
# يكتب ليك مسار  كامل
print(os.path.abspath("tow.py"))
# يكتب مسار الملف بدون اسم الملف الاخير
print(os.path.dirname("tow.py"))
# قراءه الملف فقط
file = open("data.txt", "r")
print(file.read())
file.close()
# كتابه وانشاء اذا لم يوجد
file = open("log.txt", "w")
file.write("تم فتح الملف بنجاح\n")
file.close()

# يكتب لك جميع الملفات التي توجد داحل المجلد
files = os.listdir("myfolder")  # اسم المجلد
print(files)
# الانتقال الي مجلد اخر
os.chdir("myfolder")  # تغيير المجلد النشط
print("المجلد الحالي:", os.getcwd())

