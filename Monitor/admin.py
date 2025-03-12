from django.contrib import admin
from .models.User.User import User
from .models.ModeDevice.ModeDevice import ModeDevice
from .models.Plan.Plan import Plan
from .models.UserPlan.UserPlan import UserPlan
from .models.Device.Device import Device
from .models.Mode.Mode import Mode
from .models.PlanMode.PlanMode import PlanMode


admin.site.register(User)


admin.site.register(Plan)


admin.site.register(UserPlan)


admin.site.register(Device)


admin.site.register(Mode)


admin.site.register(PlanMode)


admin.site.register(ModeDevice)
