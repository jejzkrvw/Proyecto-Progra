from ToDo_list.views.main import main_window
from ToDo_list.db.db_init import iniciar_db

iniciar_db()
main_window.mainloop()