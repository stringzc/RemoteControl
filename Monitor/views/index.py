from django.shortcuts import render
from ..models.Plan.Plan import Plan
from ..utils import generate_planid, encrypt_data, decrypt_data


# game/templates/multiends
def index(request):
    # raw_id = generate_planid()
    # encrypted_id = encrypt_data(raw_id)
    #
    # # 创建数据对象
    # new_plan = Plan(
    #     planid=encrypted_id,
    #     name="智能浇灌设备",
    #     description="自动化浇水方案",
    #     updateTime="2023-10-26 09:30:00",
    #     active=1,
    #     icon="GG",
    #     useTime=4
    # )
    # new_plan.save()
    return render(request, "web.html")
