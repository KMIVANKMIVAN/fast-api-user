from app.core.database import get_db_connection

from app.dtos import UserCreateDTO, UserUpdateDTO, BaseAuditDTO, BaseFilterDTO


# todos los getters de usuarios
def get_user_all():
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        SELECT id, email, name, mobile, password, city, country_id, street, website,
            status, user_create, user_update, date_create, date_update
        FROM users
    """
    cur.execute(query)
    row = cur.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "email": row[1],
            "name": row[2],
            "mobile": row[3],
            "password": row[4],
            "city": row[5],
            "country_id": row[6],
            "street": row[7],
            "website": row[8],
            "status": row[9],
            "userCreate": row[10],  # puedes mantener este alias si quieres
            "userUpdate": row[11],
            "dateCreate": row[12],
            "dateUpdate": row[13],
        }
    return None


def get_users_by_filter(baseFilterDTO: BaseFilterDTO):
    conn = get_db_connection()
    cur = conn.cursor()

    query = """
        SELECT *
        FROM users
    """
    params = []
    conditions = []

    # Filtros dinámicos
    if baseFilterDTO.status is not None:
        conditions.append("status = %s")
        params.append(baseFilterDTO.status)

    if baseFilterDTO.userCreate is not None:
        conditions.append("userCreate = %s")
        params.append(baseFilterDTO.userCreate)

    if baseFilterDTO.userUpdate is not None:
        conditions.append("userUpdate = %s")
        params.append(baseFilterDTO.userUpdate)

    if baseFilterDTO.dateCreate is not None:
        conditions.append("dateCreate::date = %s::date")  # compara solo la fecha
        params.append(baseFilterDTO.dateCreate)

    if baseFilterDTO.dateUpdate is not None:
        conditions.append("dateUpdate::date = %s::date")
        params.append(baseFilterDTO.dateUpdate)

    # WHERE dinámico
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    # Pagination
    limit = baseFilterDTO.limit or 10
    page = baseFilterDTO.page or 1
    offset = (page - 1) * limit

    query += " ORDER BY id DESC LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    cur.execute(query, tuple(params))
    rows = cur.fetchall()
    conn.close()

    # Retornar como lista de diccionarios
    return [
        {
            "id": row[0],
            "email": row[1],
            "name": row[2],
            "mobile": row[3],
            "password": row[4],
            "city": row[5],
            "country_id": row[6],
            "street": row[7],
            "website": row[8],
            "status": row[9],
            "userCreate": row[10],
            "userUpdate": row[11],
            "dateCreate": row[12],
            "dateUpdate": row[13],
        }
        for row in rows
    ]


def get_user_by_email(email: str):
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        SELECT id, email, name, mobile, password, city, country_id, street, website,
               status, userCreate, userUpdate, dateCreate, dateUpdate
        FROM users
        WHERE email = %s
    """
    cur.execute(query, (email,))
    row = cur.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "email": row[1],
            "name": row[2],
            "mobile": row[3],
            "password": row[4],
            "city": row[5],
            "country_id": row[6],
            "street": row[7],
            "website": row[8],
            "status": row[9],
            "userCreate": row[10],
            "userCreate": row[11],
            "dateCreate": row[12],
            "dateUpdate": row[13],
        }
    return None


def post_user_create(user: UserCreateDTO):
    conn = get_db_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO users (
            email, name, mobile, password, city, country_id, street, website,
            status, user_create, user_update, date_create, date_update
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """

    values = (
        user.email,
        user.name,
        user.mobile,
        user.password,
        user.city,
        user.country_id,
        user.street,
        user.website,
        user.status,
        user.user_create,
        user.user_update,
        user.date_create,
        user.date_update,
    )

    cur.execute(query, values)
    user_id = cur.fetchone()[0]
    conn.commit()
    conn.close()

    return {"id": user_id}


class UserRepository:
    get_user_all = staticmethod(get_user_all)
    get_user_by_email = staticmethod(get_user_by_email)
    get_user_by_filter = staticmethod(get_users_by_filter)
    post_user_create = staticmethod(post_user_create)


userRepository = UserRepository()
