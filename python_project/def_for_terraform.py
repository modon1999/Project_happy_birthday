import os
import subprocess


def create_congratulation(nickname, sex, iteration_number):
    """
    Функция создания нового workspace и создания в нем сайта поздравления, возвращает имя workspace и ссылку на сайт
    """
    iteration_number = str(iteration_number)
    command = f'''
        rm ../../../sites/man/1/index.html
        rm ../../../sites/man/2/index.html
        rm ../../../sites/man/3/index.html
        rm ../../../sites/woman/1/index.html
        rm ../../../sites/woman/2/index.html
        rm ../../../sites/woman/3/index.html
        terraform workspace new birthday-{iteration_number}
        terraform workspace select birthday-{iteration_number}
        terraform apply -auto-approve -target=module.random_site -var='name_birthday_boy={nickname}' -var='sex_birthday_boy={sex}'
        terraform apply -auto-approve -var='name_birthday_boy={nickname}' -var='sex_birthday_boy={sex}'
        terraform apply -auto-approve -var='name_birthday_boy={nickname}' -var='sex_birthday_boy={sex}'
        '''
    os.system(command)  # Создаем сайт
    name_workspace = "birthday-" + iteration_number  # Получаем название workspace

    command1 = f'''
            terraform workspace select birthday-{iteration_number}
            terraform output -raw website_domain
            '''
    res = subprocess.check_output(command1, shell=True)
    link_site = res.decode("utf-8")  # Получение output с ссылкой на сайт-поздравление
    return name_workspace, link_site


def destroy_congratulation(nickname, sex, name_workspace):
    """
    Функция уничтожения сайта-поздравления
    """
    command = f'''
        terraform workspace select {name_workspace}
        terraform destroy -auto-approve -var='name_birthday_boy={nickname}' -var='sex_birthday_boy={sex}'
        terraform workspace select default
        terraform workspace delete {name_workspace}
        '''
    os.system(command)
    return 0
