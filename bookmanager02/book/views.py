from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('index')

###############################################3

from book.models import BookInfo

book=BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
        )

book.save()
################################################
BookInfo.objects.create(
    name='测试入门',
    pub_date='2001-1-1',
    readcount=10
)
#直接创建



##################################################
book=BookInfo.objects.get(id=6)

book.name='运维开发入门'
book.save()

####################################################
BookInfo.objects.filter(id=6).update(name='爬虫入门',commentcount=666)
#过滤

############################################################33
book=BookInfo.objects.get(id=6)
book.delete()
##################################################3
book=BookInfo.objects.get(id=6).delete()
book=BookInfo.objects.filter(id=5).delete()


###########################################################
# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常。
book=BookInfo.objects.get(id=1)
#
# all查询多个结果。
#
try:
    book=BookInfo.objects.get(id=10)
except BookInfo.DoesNotExist:
    print('结果不')
book=BookInfo.objects.get(id=1)
#
# all查询多个结果。
#
try:
    book=BookInfo.objects.get(id=10)
except BookInfo.DoesNotExist:
    print('结果不')
from book.models import PeopleInfo
PeopleInfo.objects.all()
PeopleInfo.objects.all()

# count查询结果数量。

BookInfo.objects.all().count()
BookInfo.objects.count()
###########################################################
# filter过滤出多个结果
book=BookInfo.objects.filter(id__gt=2)
# exclude排除掉符合条件剩下的结果
# book=BookInfo.objects.get(id=1)
# book=BookInfo.objects.get(pk=1)
# get过滤单一结果
book=BookInfo.objects.get(id=1)
book=BookInfo.objects.get(pk=1)[0]
# 查询编号为1的图书
# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5])
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

#######################################################3
from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commentcount'))
####################################################


BookInfo.objects.filter(readcount__gt=20,id__lt=3)
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)


from django.db.models import Q

BookInfo.objects.filter(Q(readcount__gt=20))|Q(id__lt=3)
BookInfo.objects.filter(~Q(id=3))
################################################################
from django.db.models import Sum,Max,Min,Avg,Count

BookInfo.objects.aggregate(Sum('readcount'))
                           #
BookInfo.objects.all().order_by('-readcount')
################################################################
BookInfo.objects.filter(peopleinfo__name__exact='clamp')
BookInfo.objects.filter(peopleinfo__name='clamp')
#####################################################################
BookInfo.objects.filter(peopleinfo__description__contains='c')


PeopleInfo.objects.filter(book__name='clamp')
PeopleInfo.objects.filter(book__name__exact='clamp')

#########################################h;###############################
PeopleInfo.objects.filter(book__readcount__gt=30)


book='abc'
##############################################################







