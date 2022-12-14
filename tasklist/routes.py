from flask import Blueprint

from . import controllers, actionControllers

mainBP = Blueprint("main", __name__)
actionBP = Blueprint("action", __name__, url_prefix="/action")

mainBP.add_url_rule("/", "index", controllers.index)
mainBP.add_url_rule("/home", "home", controllers.home)
mainBP.add_url_rule("/admin", "admin", controllers.admin_panel, methods=["GET", "POST"])
mainBP.add_url_rule("/users", "users", controllers.user_list)
mainBP.add_url_rule("/tasks/<user>", "tasks", controllers.tasks)

actionBP.add_url_rule("/remove_user/<user_id>", "remove_user", actionControllers.remove_user)
actionBP.add_url_rule("/remove_task/<task_id>", "remove_task", actionControllers.remove_task)
actionBP.add_url_rule("/assign_task/<user_id>/<task_id>", "assign_task", actionControllers.assign_task)
