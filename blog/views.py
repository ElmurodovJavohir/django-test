from blog.models import Region, District, School, Student, Result
from django.db import models
from django.db.models.functions import Coalesce
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models.functions import JSONObject
from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.postgres.expressions import ArraySubquery
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response


class TestView(generics.GenericAPIView):
    def get(self, request):
        # region = Region.objects.all().annotate(
        #     student_res=Coalesce(
        #         models.Avg(
        #             models.F("districts__schools__students__results__correct_answers")
        #             * 100
        #             / models.F("districts__schools__students__results__total_answers")
        #         ),
        #         0,
        #         output_field=models.FloatField(),
        #     )
        # )

        # print(region)
        # for i in region:
        #     print(i.student_res)

        # district_query = (
        #     District.objects.filter(region_id=models.OuterRef("id"))
        #     .annotate(
        #         student_res=Coalesce(
        #             models.Avg(
        #                 models.F("schools__students__results__correct_answers")
        #                 * 100
        #                 / models.F("schools__students__results__total_answers")
        #             ),
        #             0,
        #             output_field=models.FloatField(),
        #         )
        #     )
        #     .annotate(
        #         json_object=JSONObject(
        #             title=models.F("title"), student_res=models.F("student_res")
        #         )
        #     )
        #     .values_list("json_object", flat=True)
        #     .order_by("-student_res")[:3]
        # )
        # region = Region.objects.all().annotate(district=ArraySubquery(district_query))
        # print(region)
        # for i in region:
        #     print(i.title)
        #     print(i.district)

        region = Region.objects.all().annotate(
            yanvar_res=Coalesce(
                models.Avg(
                    models.F("districts__schools__students__results__correct_answers")
                    * 100
                    / models.F("districts__schools__students__results__total_answers"),
                    filter=(
                        models.Q(
                            districts__schools__students__results__created_at__year=2023
                        )
                        & models.Q(
                            districts__schools__students__results__created_at__month=11
                        )
                    ),
                ),
                0,
                output_field=models.FloatField(),
            ),
            fevral_res=Coalesce(
                models.Avg(
                    models.F("districts__schools__students__results__correct_answers")
                    * 100
                    / models.F("districts__schools__students__results__total_answers"),
                    filter=(
                        models.Q(
                            districts__schools__students__results__created_at__year=2023
                        )
                        & models.Q(
                            districts__schools__students__results__created_at__month=2
                        )
                    ),
                ),
                0,
                output_field=models.FloatField(),
            ),
        )
        print(region)
        for r in region:
            print(r.title)
            print(r.yanvar_res)
        return Response({"html": "asd"})
