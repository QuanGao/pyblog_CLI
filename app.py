
# initialize database

# run user menu
#   if account exist, welcome message
#   if account not exist, make account

# read blog: which one?
# write blog
from database import Database
from menu import Menu

Database.initialize()

menu = Menu()

menu.run_menu()