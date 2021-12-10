"""CreateBlogsTable Migration."""

from masoniteorm.migrations import Migration


class CreateBlogsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("blogs") as table:
            table.increments("id")
            table.string("mealname")
            table.string("image")
            table.string("rating")
            table.string("restname")
            table.string("restaddress")
            table.string("summary")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("blogs")
