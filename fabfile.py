from fabric.api import env, local, run, sudo, cd, settings

env.hosts = ['user@host']


def test():
    local('pip list')


def upgrade_libs():
    sudo("apt-get update")
    sudo("apt-get upgrade")


def setup():
    upgrade_libs()

    sudo("apt-get install -y nginx")
    sudo("apt-get install -y git")
    sudo("apt-get install -y build-essential")
    sudo("apt-get install -y python3")
    sudo("apt-get install -y python-pip")
    sudo("apt-get install -y python-all-dev")
    sudo("apt-get install -y supervisor")

    with settings(warn_only=True):
        result = run('id deploy')
    if result.failed:
        run("useradd -d /home/deploy/ deploy")
        run("gpasswd -a deploy sudo")

    sudo("chown -R deploy /usr/local/")
    sudo("chown -R deploy /usr/lib/python2.7/")

    run("git config --global credential.helper store")

    with cd("/home/deploy/"):
        run("git clone http://yourgitrepo.com")

    with cd('/home/deploy/mysite'):
        run("pip install -r requirements.txt")
        run("python manage.py setup_db")


def deploy():

    with cd('/home/deploy/mysite'):
        run("git pull")
        run("pip install -r requirements.txt")

        sudo("cp supervisord.conf /etc/supervisor/conf.d/mysite.conf")

        sudo("cp nginx.conf /etc/nginx/sites-available/mysite.conf")
        sudo("ln -sf /etc/nginx/sites-available/mysite.conf "
             "/etc/nginx/sites-enabled/mysite.conf")


    sudo("service nginx restart")
