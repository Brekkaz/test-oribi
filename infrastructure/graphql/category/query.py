from typing import List

import strawberry
from strawberry import ID
from strawberry.types import Info

from infrastructure.graphql.category.objects import Category
from domain.utils.error_handling import AppError


@strawberry.type
class CategoryQuery:

    @strawberry.field()
    async def categories(self, info: Info) -> List[Category]:
        """
        Habilita la query para listar las categorias
        """
        try:
            results = await info.context.category.get()
            return [Category.from_entity(entity=category) for category in results]
        except AppError as e:
            raise e.extend()

    @strawberry.field()
    async def category(self, info: Info, id: ID) -> Category:
        """
        Habilita la query consultar una categoria
        """
        try:
            category = await info.context.category.get_by_id(id=id)
            return Category.from_entity(entity=category)
        except AppError as e:
            raise e.extend()
