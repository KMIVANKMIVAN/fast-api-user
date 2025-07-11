from app.core.database import get_db_connection
from app.dtos.base_dto import BaseFilterDTO 

# todos los getters de usuarios
def get_user_all():
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        SELECT id, email, name, mobile, password, city, country_id, street, website,
               status, userCreate, userUpdate, dateCreate, dateUpdate
        FROM users
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

def get_user_by_filter(filters: BaseFilterDTO):
    conn = get_db_connection()
    cur = conn.cursor()

    query = """
        SELECT id, email, name, mobile, password, city, country_id, street, website,
               status, userCreate, userUpdate, dateCreate, dateUpdate
        FROM users
    """
    params = []
    conditions = []

    # Filtros dinámicos
    if filters.status is not None:
        conditions.append("status = %s")
        params.append(filters.status)

    if filters.userCreate is not None:
        conditions.append("userCreate = %s")
        params.append(filters.userCreate)

    if filters.userUpdate is not None:
        conditions.append("userUpdate = %s")
        params.append(filters.userUpdate)

    if filters.dateCreate is not None:
        conditions.append("dateCreate::date = %s::date")  # compara solo la fecha
        params.append(filters.dateCreate)

    if filters.dateUpdate is not None:
        conditions.append("dateUpdate::date = %s::date")
        params.append(filters.dateUpdate)

    # WHERE dinámico
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    # Pagination
    limit = filters.limit or 10
    page = filters.page or 1
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