from typing import List, Tuple
from sqlalchemy import select

from app.database.models import async_session
from app.database.models import Orders


cityList = ['Riga', 'Liepaja', 'Daugavpils']


async def get_order_by_city(city: str) -> List[Tuple[int, str, int]]:
    async with async_session() as session:
        orders_address = await session.execute(
            select(Orders.order_id, Orders.address_street, Orders.paid_status)
            .where(Orders.city == city and Orders.delivery_status == 0))
        return orders_address.all()