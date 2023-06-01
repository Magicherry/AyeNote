from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import re_path

from .views import register_views

urlpatterns = [
    # 登录、退出、注册
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(template_name='learning_logs/index.html'), name='logout'),
    re_path(r'^register/$', register_views, name='register'),

    # 修改密码
    re_path(r'^password_change/$', PasswordChangeView.as_view(template_name='users/password_change.html'),
            name='password_change'),
    re_path(r'^password_change/done/$', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
            name='password_change_done'),

    # 重置密码
    re_path(r'^password_reset/$', PasswordResetView.as_view(template_name='users/password_reset.html'),
            name='password_reset'),
    re_path(r'^password_reset/done/$', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
            name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
            name='password_reset_confirm'),
    re_path(r'^reset/done/$', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
            name='password_reset_complete'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 为urls设置命名空间
app_name = 'users'
