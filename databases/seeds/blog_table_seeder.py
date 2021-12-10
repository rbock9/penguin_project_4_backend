"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"mealname": "Big Mac", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/McD_Big_Mac.jpg/240px-McD_Big_Mac.jpg", "rating": "4/10", "restname": "McDonalds", "restaddress": "2328 Georgia Ave NW, Washington, DC 20001", "summary": "Not that good"})
        Blog.create({"mealname": "Hot Dogs", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Hot_dog_with_mustard.png/320px-Hot_dog_with_mustard.png", "rating": "7/10", "restname": "Yankee Stadium", "restaddress": "1 E 161 St, Bronx, NY 10451", "summary": "Pretty good, but mustard was runny"})
        Blog.create({"mealname": "Chili Half-smoke", "image": "http://1.bp.blogspot.com/-L0CoclE06CY/VIY1ys7FzeI/AAAAAAAAAF4/sjiw7ph-XWE/s1600/bens%2Bchili%2Bbowl.jpg", "rating": "8/10", "restname": "Ben's Chili Bowl", "restaddress": "1213 U St NW, Washington, DC 20009", "summary": "Solid taste, a bit pricey for small portion"})
