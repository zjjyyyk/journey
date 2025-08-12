from django.conf import settings
from django.conf.urls.static import static
from django_distill import distill_path
from gallery import views

def get_periods():
    # 返回所有期次 slug 列表，每个是元组形式，参数对应路径参数顺序
    # 比如 period 参数，必须是元组 (period,)
    return [(p['slug'],) for p in views.get_periods()]

urlpatterns = [
    distill_path('', views.index, name='index'),  # 首页不带参数
    distill_path('period/<slug:period>/', views.period_view, name='period', distill_func=get_periods),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
