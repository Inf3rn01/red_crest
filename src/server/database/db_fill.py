from src.server.database.models import *


def db_fill():
    Post.create(
        title="Хирург"
    )

    Department.create(
        title="Хирургическое"
    )


    Role.create(
        title="Врач"
    )

    Role.create(
        title="User"
    ).save()

    Users.create(
        FIO="Абдуржмаев Энакентий Эдуардович",
        id_role=Role.get(Role.id == 2)
    )

    Users.create(
        FIO="Ложников Виталий Александрович",
        id_role=Role.get(Role.id == 1)
    ).save()

    AuthData.create(
        login="user",
        password="user",
        user_id=Users.get(Users.id == 2)
    )

    AuthData.create(
        login="med",
        password="med",
        user_id=Users.get(Users.id == 1)
    ).save()

    Staff.create(
        id_post=Post.get(Post.id == 1),
        id_user=Users.get(Users.id == 2),
        id_department=Department.get(Department.id == 1)
    )

    Type_of_treatment.create(
        title="Трансплантация"
    )

    Status_request.create(
        title="Принята"
    )

    Status_request.create(
        title="Отменена"
    ).save()

    Request.create(
        add_data="11/12/23 19:23",
        id_status_req=Status_request.get(Status_request.id == 1),
        id_user=Users.get(Users.id == 1)
    )

    Type_of_disease.create(
        title="Наследственный"
    )

    Disease.create(
        title="Синдром Дауна",
        description="Наследственное заболевание, обусловленное трисомией по 21-й хромосоме.",
        id_type_of_disease=Type_of_disease.get(Type_of_disease.id == 1)
    )

    Reception.create(
        id_req=Request.get(Request.id == 1),
        id_staff=Staff.get(Staff.id == 1),
        id_disease=Disease.get(Disease.id == 1),
        id_type_of_treatment=Type_of_treatment.get(Type_of_treatment.id == 1),
        description_of_treatment="Трансплантация костного мозга, также назначаются иммуноглобулины, цитостатики, антибиотик"
    )

    Treatment_status.create(
        title="Выписан"
    )

    Treatment_status.create(
        title="На больничном"
    ).save()

    Patients.create(
        id_reception=Reception.get(Reception.id == 1),
        id_status=Treatment_status.get(Treatment_status.id == 1),
        data_of_discharge="26/12/23 10:00"
    )
