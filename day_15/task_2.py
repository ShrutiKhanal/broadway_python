from day_15.decorators import login_required


@login_required
def get_message():
    return"learning at broadway !"

print(get_message)