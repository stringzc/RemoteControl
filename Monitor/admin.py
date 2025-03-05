from django.contrib import admin
from .models.User.User import User
from .models.ModeDevice.ModeDevice import ModeDevice
from .models.Plan.Plan import Plan
from .models.UserPlan.UserPlan import UserPlan
from .models.Device.Device import Device
from .models.Mode.Mode import Mode
from .models.PlanMode.PlanMode import PlanMode


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number')  # 显示的字段
    search_fields = ('phone_number',)  # 允许通过手机号搜索


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'description')  # 显示的字段
    search_fields = ('name', 'phone_number')  # 允许通过方案名称或手机号搜索


@admin.register(UserPlan)
class UserPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan')  # 显示的字段
    list_filter = ('user', 'plan')  # 允许按用户和方案进行筛选


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # 显示的字段
    search_fields = ('name',)  # 允许通过设备名称搜索


@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'url')  # 显示的字段
    search_fields = ('name',)  # 允许通过模式名称搜索


@admin.register(PlanMode)
class PlanModeAdmin(admin.ModelAdmin):
    list_display = ('plan', 'mode')  # 显示的字段
    list_filter = ('plan', 'mode')  # 允许按方案和模式进行筛选


@admin.register(ModeDevice)
class ModeDeviceAdmin(admin.ModelAdmin):
    list_display = ('mode', 'device')  # 显示的字段
    list_filter = ('mode', 'device')  # 允许按模式和设备进行筛选
