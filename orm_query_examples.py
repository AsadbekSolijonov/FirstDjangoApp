import os
import django
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q, F, Count, Max, Min, Avg
from django.db import connection

from blog.models.students import Student

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


def all_students():
    return Student.objects.all()


def lastest_students(limit=5):
    return Student.objects.order_by('-created_at')[:limit]


def less_then_point(point=60):
    return Student.objects.filter(total_points__lt=point)


def greater_then_equal_point(point=60):
    return Student.objects.filter(total_points__gte=point)


def get_only_fields(*args):
    return Student.objects.values(*args)


def get_list_only_fields(*args):
    return Student.objects.values_list(*args)


def get_all_desc_by_total_points():
    return Student.objects.order_by('-total_points')


def image_is_null_users(null=True):
    return Student.objects.filter(image__isnull=null)


def get_first_name_or_last_name():
    return Student.objects.filter(Q(first_name__icontains='bek') | Q(last_name__icontains='ov'))


def get_first_name_and_last_name():
    return Student.objects.filter(Q(first_name__icontains='bek') & Q(last_name__icontains='ov'))


def get_not_first_name(value):
    return Student.objects.filter(~Q(first_name__exact=value))


def get_first_name_startswith(value):
    return Student.objects.filter(first_name__startswith=value)


def get_total_points_in(values):
    return Student.objects.filter(total_points__in=values)


def get_total_points_not_in(values):
    return Student.objects.filter(~Q(total_points__in=values))


def get_greater_then_equal_from_passed_points():
    return Student.objects.filter(total_points__gte=F('passed_points'))


def get_first_name_total_count():
    return Student.objects.values('first_name').annotate(total=Count('id')).order_by('-total')


def get_max_min_avg_points():
    return Student.objects.aggregate(max_point=Max('total_points'),
                                     min_point=Min('total_points'),
                                     avg_point=Avg('total_points'))


def get_lastnames_with_more_than_3_students():
    return Student.objects.values('last_name').annotate(total=Count('id'), ids=ArrayAgg('id', ordering='-id')).filter(
        total__gte=3)


def total_students():
    return Student.objects.aggregate(total=Count('id'))


def get_all_users_in_raw():
    with connection.cursor() as curr:
        curr.execute("""
        SELECT * FROM blog_student;
        """)
        datas = curr.fetchall()
        return datas


if __name__ == '__main__':
    q1 = all_students()
    q2 = lastest_students()
    q3 = less_then_point()
    q4 = greater_then_equal_point()
    q5 = get_only_fields('first_name', 'last_name', 'total_points')
    q6 = get_list_only_fields('first_name', 'last_name', 'total_points')
    q7 = get_all_desc_by_total_points()
    q8 = image_is_null_users()
    q9 = get_first_name_or_last_name()
    q10 = get_first_name_and_last_name()
    q11 = get_not_first_name('Abek')
    q12 = get_first_name_startswith('A')
    q13 = get_total_points_in([60, 70, 55, 90, 95, 100])
    q14 = get_total_points_not_in([60, 70, 55, 90, 95, 100])
    q15 = get_greater_then_equal_from_passed_points()
    q16 = get_first_name_total_count()
    q17 = get_max_min_avg_points()
    q18 = get_lastnames_with_more_than_3_students()
    q19 = total_students()
    q20 = get_all_users_in_raw()
    # print(q5)
    # print(str(q5.query))
    # print()
    print(q20)
    # print(q20.query)
    # for q in q19:
    #     print(q.id, q.first_name, q.countings)
