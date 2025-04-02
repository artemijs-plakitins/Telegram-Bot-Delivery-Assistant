import os
from dotenv import load_dotenv

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine



load_dotenv()
engine = create_async_engine(url=os.getenv('DB_URL'))

async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Orders(Base):
    __tablename__ = 'ORDERS'

    order_id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(20))
    recipient: Mapped[str] = mapped_column(String(50))
    address_street: Mapped[str] = mapped_column(String(50))
    postal_code: Mapped[str] = mapped_column(String(7))
    payment_amount: Mapped[int] = mapped_column()
    paid_status: Mapped[str] = mapped_column(String(3))
    delivery_status: Mapped[int] = mapped_column()



async def async_main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)