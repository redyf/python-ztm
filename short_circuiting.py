# Short Circuiting
# Basicamente o short circuiting diz ao interpretador para ignorar a condição posterior, caso alguma delas já seja verdadeira. Isso evita processamento desnecessário pois ele não analisa todas as condições.
is_Friend = False
is_user = True

if is_Friend and is_user:
    print(is_Friend and is_user)
