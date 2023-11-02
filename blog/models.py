from django.db import models

"""
13. Regionlar bor, regionlarni districtlari bor, districtlarni maktablari bor, maktablarni o'quvchilari bor.
O'quvchilarni testdan ishlagan natijalari bor.
Result:
    correct_answers = 20
    total_answers= 25
    percentage = 80

13.1 Regionlar bo'yicha o'quvchilarni o'rtacha natijalarini chiqaring.  
[{"title": "Toshkent", "student_res":81.56%}, {"title": "Sirdaryo", "student_res":87.56%}, {"title": "Jizzax", "student_res":86.56%}, {"title": "Samarqand", "student_res":87.5126%},]
13.2.Regionlarni Tumanlarini o'rtacha natijasi yuqori 3 tasini chiqarish
[{"title": "Toshkent", "tumanlar":[
    {"title":"Yunusobod", "result":67.45%}
]}, ]
13.3. O'zlashtirish natijasi yuqori bo'lgan top 3 ta maktablar tumanlar kesimida.
[{"title": "Yunusobod", "maktab":[
    {"title":"11-maktab", "result":67.45%}
]}, ]
13.4. oylar kesimida regionlarda o'zlashtirish natijasi. ( oylar kesimida degani - 12 oy (Yan, Fev,...., Dec), o'zlashtirish natijasida degani o'rtacha natija)
[
    {"title":"Yanvar", "region":[
        {"title":"Toshkent", "result":76.12%}
    ]}
]
13.5. Butun viloyatlar to'plagan ball chiqarilsin, 100-80% uchun 1 ball o'quvchiga, 80%-50% uchun 0.5 ball, undan pastiga 0 ball. Viloyatlar ballari chiqarilsin.
10 o'quvchi
2 tasi 100-80% oralig'ida=  1*2 = 2 ball
6 tasi 80%-50% uchun 0.5 * 6 = 3 ball
2 tasi 50% pas  0 ball
Region umumiy bali , 5 ball
[{"title": "Toshkent", "student_res":5}, ]
"""


class Region(models.Model):
    title = models.CharField(
        max_length=128,
    )


class District(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="districts"
    )
    title = models.CharField(
        max_length=128,
    )


class School(models.Model):
    title = models.CharField(max_length=128)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="schools"
    )


class Student(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="students"
    )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)


class Result(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="results"
    )
    correct_answers = models.IntegerField()
    total_answers = models.IntegerField()
    percentage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
